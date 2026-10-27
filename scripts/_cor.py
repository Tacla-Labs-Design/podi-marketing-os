"""Cor e PNG — funções comuns aos scripts de paleta do Marketing OS.

Usado por scripts/paleta-empreendimento.py. Nenhuma regra de
marca mora aqui: só a conta (sRGB <-> OKLab, contraste WCAG) e a leitura/gravação de PNG.

Só biblioteca padrão do Python: nada para instalar.
"""

import math
import re
import struct
import zlib


# ---------------------------------------------------------------------------
# Cor: sRGB <-> OKLab, contraste WCAG
# ---------------------------------------------------------------------------
def hex_rgb(h):
    h = h.strip().lstrip("#")
    if not re.fullmatch(r"[0-9a-fA-F]{6}", h):
        raise ValueError(h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02X}" for c in rgb)


def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _gam(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def rgb_oklab(rgb):
    r, g, b = (_lin(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (math.copysign(abs(x) ** (1 / 3), x) for x in (l, m, s))
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def oklab_rgb_linear(lab):
    L, a, b = lab
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def lch(lab):
    L, a, b = lab
    return L, math.hypot(a, b), math.atan2(b, a)


def de_lch(L, C, H):
    """OKLCh -> hex, com gamut clamp em sRGB: mantém L e H e reduz C até caber."""
    def cabe(c):
        return all(-1e-7 <= x <= 1 + 1e-7 for x in oklab_rgb_linear((L, c * math.cos(H), c * math.sin(H))))
    if not cabe(C):
        lo, hi = 0.0, C
        for _ in range(40):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if cabe(mid) else (lo, mid)
        C = lo
    lin = oklab_rgb_linear((L, C * math.cos(H), C * math.sin(H)))
    return rgb_hex(tuple(_gam(max(0, min(1, x))) for x in lin))


def luminancia(h):
    r, g, b = (_lin(c) for c in hex_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# ---------------------------------------------------------------------------
# PNG RGBA 8 bits, sem Pillow
# ---------------------------------------------------------------------------
def _ler_png_rgba(caminho):
    d = open(caminho, "rb").read()
    if d[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{caminho} não é PNG")
    i, idat, ihdr = 8, b"", None
    while i < len(d):
        n, tipo = struct.unpack(">I4s", d[i:i + 8])
        corpo = d[i + 8:i + 8 + n]
        if tipo == b"IHDR":
            ihdr = struct.unpack(">IIBBBBB", corpo)
        elif tipo == b"IDAT":
            idat += corpo
        i += 12 + n
    w, h, prof, tipo_cor, _, _, entrelace = ihdr
    if (prof, tipo_cor, entrelace) != (8, 6, 0):
        raise ValueError(f"{caminho}: esperado PNG RGBA 8 bits sem entrelaçamento")
    bruto, bpp, linha = zlib.decompress(idat), 4, w * 4
    px, ant, p = [], bytearray(linha), 0
    for _ in range(h):
        filtro, cur = bruto[p], bytearray(bruto[p + 1:p + 1 + linha])
        p += 1 + linha
        for x in range(linha):
            a = cur[x - bpp] if x >= bpp else 0
            b = ant[x]
            c = ant[x - bpp] if x >= bpp else 0
            if filtro == 1:
                cur[x] = (cur[x] + a) & 255
            elif filtro == 2:
                cur[x] = (cur[x] + b) & 255
            elif filtro == 3:
                cur[x] = (cur[x] + (a + b) // 2) & 255
            elif filtro == 4:
                pa, pb, pc = abs(b - c), abs(a - c), abs(a + b - 2 * c)
                cur[x] = (cur[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        px.append(bytes(cur))
        ant = cur
    return w, h, px


def _gravar_png_rgba(caminho, w, h, linhas):
    def chunk(tipo, corpo):
        return struct.pack(">I", len(corpo)) + tipo + corpo + struct.pack(">I", zlib.crc32(tipo + corpo) & 0xFFFFFFFF)
    dados = b"".join(b"\x00" + l for l in linhas)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0))
           + chunk(b"IDAT", zlib.compress(dados, 9))
           + chunk(b"IEND", b""))
    open(caminho, "wb").write(png)


def recolorir_png(origem, destino, cor):
    """Pinta todo pixel de `origem` com `cor`, mantendo só o canal alfa. Devolve (w, h)."""
    r, g, b = (round(c * 255) for c in hex_rgb(cor))
    w, h, linhas = _ler_png_rgba(origem)
    novas = [bytes(v for x in range(w) for v in (r, g, b, l[x * 4 + 3])) for l in linhas]
    _gravar_png_rgba(destino, w, h, novas)
    return w, h
