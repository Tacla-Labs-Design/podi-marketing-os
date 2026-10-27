#!/usr/bin/env python3
"""Paleta do e-mail com marca do empreendimento.

Rodado pela skill /newsletter-podi antes de montar um e-mail em que o remetente é o
empreendimento (shopping, outlet). A cor base da campanha substitui o verde Podi, e o
resto do grupo verde é derivado dela sempre pela mesma conta — a IA não refaz o cálculo
à mão. Regra completa: design-system/newsletter/guidelines/marca-empreendimento.md.

Uso:
  python3 scripts/paleta-empreendimento.py "#173B2A"                 só calcula e confere
  python3 scripts/paleta-empreendimento.py "#173B2A" <slug>          + gera os ícones em saida/<slug>/imagens/icones/
  python3 scripts/paleta-empreendimento.py "#173B2A" --conferir saida/<slug>/*.html
                                                                     confere peças montadas (só leitura)

Opções:
  --redes instagram,facebook,linkedin   quais ícones gerar (padrão: esses três)

Saída 0 = paleta aprovada (e, com --conferir, peças sem pendência).
Saída 1 = contraste reprovado, cor base sem matiz ou peça com pendência. Não montar assim.
Saída 2 = uso errado (cor inválida, arquivo que não existe).

Só biblioteca padrão do Python: nada para instalar.
"""

import os
import re
import sys

from _cor import contraste, de_lch, hex_rgb, lch, recolorir_png, rgb_hex, rgb_oklab

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONES_BRAND = os.path.join(RAIZ, "brand", "podi", "assets", "icones")

# ---------------------------------------------------------------------------
# Tokens do Podi (design-system/newsletter/tokens.md). Só o grupo verde muda.
# ---------------------------------------------------------------------------
PODI_BRAND = "#48DB84"
PODI_ACCENT_INK = "#0C6E3B"
PODI_DERIVADOS = {           # token -> hex original do Podi
    "page": "#EDF7F1",       # page e canvas são a mesma cor
    "accent-soft": "#D4F0DF",
    "hairline": "#D2E7DA",
}
INK, BODY, MUTED, BRANCO = "#101010", "#4A4A4A", "#6E6E6E", "#FFFFFF"

FATOR_SATURACAO = 0.60       # derivados levam 60% da saturação (C) do token do Podi
CONTRASTE_MIN = 4.5
CROMA_MIN_BASE = 0.02        # abaixo disso a cor base não tem matiz confiável

# Cores que só existem no Podi (grupo verde, dark mode, roxo) e não podem sobrar numa peça.
PODI_PROIBIDAS = {
    "#48DB84", "#0C6E3B", "#EDF7F1", "#D4F0DF", "#D2E7DA",               # grupo verde
    "#6FE9A2", "#1A1A1A", "#242424", "#16281E", "#F5F5F5", "#C9C9C9",     # dark mode
    "#8F8F8F", "#333333",
    "#9934FF",                                                           # roxo Tacla Labs
}


# ---------------------------------------------------------------------------
# Paleta
# ---------------------------------------------------------------------------
def calcular(base):
    base = rgb_hex(hex_rgb(base))
    _, c_base, h_base = lch(rgb_oklab(hex_rgb(base)))
    if c_base < CROMA_MIN_BASE:
        return None, base, c_base

    tokens = {"brand": base}
    for nome, podi in PODI_DERIVADOS.items():
        L, C, _ = lch(rgb_oklab(hex_rgb(podi)))
        tokens[nome] = de_lch(L, C * FATOR_SATURACAO, h_base)

    # accent-ink: a própria base; se não passar sobre page e accent-soft, escurece em OKLab
    # (mesma matiz e saturação, claridade menor) até passar nos dois.
    L, C, H = lch(rgb_oklab(hex_rgb(base)))
    ink = base
    while min(contraste(ink, tokens["page"]), contraste(ink, tokens["accent-soft"])) < CONTRASTE_MIN and L > 0:
        L = max(0.0, L - 0.005)
        ink = de_lch(L, C, H)
    tokens["accent-ink"] = ink

    tokens["cta-texto"] = BRANCO if contraste(BRANCO, base) >= CONTRASTE_MIN else INK
    return tokens, base, c_base


def checagens(t):
    return [
        ("muted sobre page", MUTED, t["page"]),
        ("accent-ink sobre page", t["accent-ink"], t["page"]),
        ("accent-ink sobre accent-soft", t["accent-ink"], t["accent-soft"]),
        ("texto do CTA sobre a base", t["cta-texto"], t["brand"]),
    ]


def trocas(t):
    """De -> para, na ordem em que a peça montada com os componentes do Podi é convertida."""
    return [
        (PODI_BRAND, t["brand"], "brand: fundo do CTA (bgcolor, fillcolor, background-color)"),
        (PODI_ACCENT_INK, t["accent-ink"], "accent-ink: número, marcador, etiqueta, link de marca"),
        (PODI_DERIVADOS["page"], t["page"], "page/canvas: fundo da mensagem e do container"),
        (PODI_DERIVADOS["accent-soft"], t["accent-soft"], "accent-soft: faixa do destaque, fundo de etiqueta"),
        (PODI_DERIVADOS["hairline"], t["hairline"], "hairline: linhas finas"),
    ]


def gerar_icones(base, slug, redes):
    destino = os.path.join(RAIZ, "saida", slug, "imagens", "icones")
    os.makedirs(destino, exist_ok=True)
    gerados = []
    for rede in redes:
        origem = os.path.join(ICONES_BRAND, f"{rede}-green.png")
        if not os.path.exists(origem):
            print(f"  ✗ não existe ícone oficial para '{rede}' em brand/podi/assets/icones/ — não gerado")
            continue
        arq = os.path.join(destino, f"{rede}-campanha.png")
        w, h = recolorir_png(origem, arq, base)
        gerados.append((os.path.relpath(arq, RAIZ), w, h))
    return gerados


# ---------------------------------------------------------------------------
# Conferência de peça montada (só leitura)
# ---------------------------------------------------------------------------
def conferir(caminho, t):
    html = open(caminho, encoding="utf-8").read()
    pend = []
    cores = {c.upper() for c in re.findall(r"#[0-9A-Fa-f]{6}\b", html)}
    permitidas = {t["brand"], t["accent-ink"], t["page"], t["accent-soft"], t["hairline"], INK, BODY, MUTED, BRANCO}
    sobrando = sorted(cores & (PODI_PROIBIDAS - permitidas))
    if sobrando:
        pend.append("cor do Podi sobrando: " + ", ".join(sobrando))
    fora = sorted(cores - permitidas - PODI_PROIBIDAS)
    if fora:
        pend.append("cor fora da paleta derivada: " + ", ".join(fora))
    if not re.search(r'<meta name="color-scheme" content="light only"', html):
        pend.append('falta <meta name="color-scheme" content="light only">')
    if "prefers-color-scheme" in html or "[data-ogsc]" in html:
        pend.append("sobrou bloco de dark mode no <style>")
    dm = sorted(set(re.findall(r"\bdm-[a-z]+", html)))
    if dm:
        pend.append("sobraram classes de dark mode: " + ", ".join(dm))
    if re.search(r"-green\.png|brand/podi/assets/icones", html):
        pend.append("ícone social ainda aponta para o verde do Podi em brand/")
    if re.search(r"podibr|company/podiapp|open\.spotify\.com/user/31ipy", html):
        pend.append("rede social do Podi numa peça do empreendimento")
    if re.search(r'<img [^>]*src="[^"]*(logo-podi|logo-tacla)', html):
        pend.append("logo do Podi ou da Tacla Labs numa peça do empreendimento")
    # CTA: as duas metades com a base de fundo e o texto que o contraste decidiu
    for m in re.finditer(r'<a [^>]*background-color:%s[^>]*>' % re.escape(t["brand"]), html, re.I):
        if not re.search(r"[;\"]color:%s;" % re.escape(t["cta-texto"]), m.group(0), re.I):
            pend.append(f"texto do CTA (<a>) não é {t['cta-texto']}")
            break
    for m in re.finditer(r'fillcolor="%s">.*?<center style="color:(#[0-9A-Fa-f]{6})' % re.escape(t["brand"]), html, re.I | re.S):
        if m.group(1).upper() != t["cta-texto"]:
            pend.append(f"texto do CTA (VML) não é {t['cta-texto']}")
            break
    return pend


# ---------------------------------------------------------------------------
def main(argv):
    args, redes, arquivos = list(argv), ["instagram", "facebook", "linkedin"], None
    if "--redes" in args:
        i = args.index("--redes")
        redes = [r.strip() for r in args[i + 1].split(",") if r.strip()]
        del args[i:i + 2]
    if "--conferir" in args:
        i = args.index("--conferir")
        arquivos = args[i + 1:]
        del args[i:]
    if not args or len(args) > 2:
        print(__doc__)
        return 2
    try:
        tokens, base, c_base = calcular(args[0])
    except ValueError:
        print(f"Cor base inválida: {args[0]!r}. Use hex de 6 dígitos, como #173B2A.")
        return 2

    if tokens is None:
        print(f"✗ A cor base {base} é neutra demais (saturação OKLab {c_base:.3f} < {CROMA_MIN_BASE}).")
        print("  Preto, cinza ou branco não têm matiz para derivar a paleta. Não montar:")
        print("  o modo empreendimento ainda não tem regra para base neutra — avisar o maintainer.")
        return 1

    print(f"Paleta do empreendimento · base {base}\n")
    print("  Token          Hex        Origem")
    print(f"  brand          {tokens['brand']}    cor base")
    print(f"  accent-ink     {tokens['accent-ink']}    " + ("cor base" if tokens["accent-ink"] == base else "cor base escurecida em OKLab até passar 4,5:1"))
    for nome, podi in PODI_DERIVADOS.items():
        print(f"  {nome:<14} {tokens[nome]}    derivado de {podi}")
    print(f"  cta-texto      {tokens['cta-texto']}    " + ("branco: passa 4,5:1 sobre a base" if tokens["cta-texto"] == BRANCO else "#101010: o branco não passa 4,5:1 sobre a base"))
    print(f"  ink/body/muted {INK} {BODY} {MUTED}  iguais ao Podi")

    print("\nContrastes obrigatórios (mínimo 4,5:1)")
    reprovou = False
    for rotulo, fg, bg in checagens(tokens):
        c = contraste(fg, bg)
        ok = c >= CONTRASTE_MIN
        reprovou |= not ok
        print(f"  {'✓' if ok else '✗'} {rotulo:<30} {fg} / {bg}  {c:.2f}:1".replace(".", ","))

    print("\nTroca na peça montada (componentes do Podi → empreendimento)")
    for de, para, uso in trocas(tokens):
        print(f"  {de} → {para}   {uso}")
    if tokens["cta-texto"] == BRANCO:
        print(f"  CTA: color:{INK} → color:{BRANCO} só nas duas metades do botão (<center> do VML e <a>)")

    if reprovou:
        print("\n✗ Contraste reprovado. Não montar com esta cor base — pedir outra ao empreendimento.")
        return 1

    if len(args) == 2 and arquivos is None:
        print(f"\nÍcones sociais (saida/{args[1]}/imagens/icones/)")
        for arq, w, h in gerar_icones(base, args[1], redes):
            print(f"  ✓ {arq}  {w}×{h}")

    if arquivos is not None:
        print("\nConferência das peças")
        falhou = False
        for arq in arquivos:
            if not os.path.exists(arq):
                print(f"  ✗ {arq}: arquivo não existe")
                return 2
            pend = conferir(arq, tokens)
            falhou |= bool(pend)
            print(f"  {'✓' if not pend else '✗'} {os.path.basename(arq)}")
            for p in pend:
                print(f"      - {p}")
        if falhou:
            return 1

    print("\n✓ Paleta aprovada.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
