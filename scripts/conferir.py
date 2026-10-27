#!/usr/bin/env python3
"""Confere a peça montada contra a marca do Podi (brand/marca.json).

Só lê e acusa o que não pode sair assim. Peça do modo empreendimento (remetente é o shopping)
tem paleta derivada e se confere com `scripts/paleta-empreendimento.py --conferir`.

Uso:
  python3 -I scripts/conferir.py saida/<slug>/index.html [saida/<slug>/legenda.txt ...]
        acusa cor fora da paleta, o verde de marca como cor de texto, "a Podi", variável
        fora das três do servidor do Podi, placeholder {{...}} sobrando e
        imagem sem alt. No e-mail, também peso, CSS proibido, tabela sem role e link sem
        target. No deck e no post, imagem fora de assets/ — e diz quantos slides ou cards há.
        Arquivo .txt (legenda): só as regras de texto.
        Comentários do HTML não contam.
  python3 -I scripts/conferir.py --campos nome,economia_total saida/<slug>/index.html
        disparo por outro sistema: aceita também os campos do briefing, e só eles
  python3 -I scripts/conferir.py --marca
        (maintainer) confere se o marca.json está completo e se os contrastes obrigatórios
        passam — rodar depois de mexer na paleta

Saída 0 = ok. Saída 1 = pendência (não entregar assim). Saída 2 = uso errado.
Só biblioteca padrão do Python: nada para instalar.
"""

import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARCA = os.path.join(RAIZ, "brand", "marca.json")
CONTRASTE_MIN = 4.5
CONTRASTE_GRAFICO = 3.0       # detalhe gráfico (ícone, régua, borda): WCAG 1.4.11

# Cores técnicas do shell do deck que não são token (fundo da prévia na tela).
TOLERADAS = {"#2A2A2A"}

# Endereço das versões publicadas no hub de marcas: o deck pode citar imagem de lá.
HUB_PODI = "https://marcas.taclalabs.workers.dev/podi/"

# Pares obrigatórios: (rótulo, texto, fundo, mínimo)
PARES = [
    ("texto sobre a cor de marca", "ink-on-brand", "brand", CONTRASTE_MIN),
    ("accent-ink sobre branco", "accent-ink", "surface", CONTRASTE_MIN),
    ("accent-ink sobre page-light", "accent-ink", "page-light", CONTRASTE_MIN),
    ("accent-ink sobre accent-soft", "accent-ink", "accent-soft", CONTRASTE_MIN),
    ("accent-on-dark sobre page-dark", "accent-on-dark", "page-dark", CONTRASTE_MIN),
    ("accent-on-dark sobre ink (fundo preto)", "accent-on-dark", "ink", CONTRASTE_MIN),
    ("muted sobre page-light", "muted", "page-light", CONTRASTE_MIN),
    ("body sobre surface-alt", "body", "surface-alt", CONTRASTE_MIN),
    ("secundária sobre branco (detalhe)", "accent-2", "surface", CONTRASTE_GRAFICO),
    ("secundária sobre o chip", "accent-2", "accent-2-soft", CONTRASTE_GRAFICO),
]


# ---------------------------------------------------------------------------
# contraste (WCAG 2.x)
# ---------------------------------------------------------------------------
def _canal(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminancia(h):
    h = h.strip().lstrip("#")
    r, g, b = (_canal(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _num(v, casas=2):
    return f"{v:.{casas}f}".replace(".", ",")


# ---------------------------------------------------------------------------
def carregar():
    with open(MARCA, encoding="utf-8") as f:
        return json.load(f)


def pendencias_marca(m):
    """O que falta no marca.json para uma peça poder ser montada."""
    p = []
    for papel, v in m["cores"].items():
        if not v:
            p.append(f"cor '{papel}' sem valor")
    for chave, v in m["links"].items():
        if not v:
            p.append(f"link '{chave}' sem valor")
    for chave in ("svg", "png"):
        arq = m["logo"].get(chave)
        if not arq or not os.path.exists(os.path.join(RAIZ, arq)):
            p.append(f"logo {chave} não encontrado ({arq})")
    for rede, url in m["redes"].items():
        icone = m["icones"].format(rede=rede)
        if url and not os.path.exists(os.path.join(RAIZ, icone)):
            p.append(f"ícone de {rede} não encontrado ({icone})")
    return p


def cmd_marca():
    m = carregar()
    print(f"Marca {m['nome']}\n")
    falhou = False
    pend = pendencias_marca(m)
    if pend:
        falhou = True
        print("Faltando no marca.json")
        for p in pend:
            print(f"  ✗ {p}")
        print()
    print("Contrastes obrigatórios")
    c = m["cores"]
    for rotulo, fg, bg, minimo in PARES:
        if c.get(fg) and c.get(bg):
            v = contraste(c[fg], c[bg])
            falhou |= v < minimo
            print(f"  {'✓' if v >= minimo else '✗'} {rotulo:<40} {c[fg]} / {c[bg]}  "
                  f"{_num(v)}:1 (mín. {_num(minimo, 1)})")
    if falhou:
        print("\n✗ marca.json incompleto ou com contraste reprovado.")
        return 1
    print("\n✓ marca.json completo.")
    return 0


# ---------------------------------------------------------------------------
def _sem_comentarios(html):
    # Os marcadores do "não-Outlook" (<!--[if !mso]><!--> … <!--<![endif]-->) não são comentário:
    # o que está entre eles é o botão que todo cliente fora do Outlook mostra.
    html = html.replace("<!--[if !mso]><!-->", "\x00ABRE\x00").replace("<!--<![endif]-->", "\x00FECHA\x00")
    html = re.sub(r"<!--(?!\[if).*?-->", "", html, flags=re.S)
    html = html.replace("\x00ABRE\x00", "<!--[if !mso]><!-->").replace("\x00FECHA\x00", "<!--<![endif]-->")
    return re.sub(r"/\*.*?\*/", "", html, flags=re.S)


def conferir_texto(texto, m):
    pend = []
    feminino = re.findall(r"\b(a|da|na|pela)\s+Podi\b", re.sub(r"<[^>]+>", " ", texto))
    if feminino:
        pend.append(f'"{feminino[0]} Podi" — a marca é masculina: "o Podi", "do Podi"')
    return pend


def conferir(html, m, campos=()):
    pend, mc = [], m["cores"]
    limpo = _sem_comentarios(html)

    cores = {c.upper() for c in re.findall(r"#[0-9A-Fa-f]{6}\b", limpo)}
    paleta = {v.upper() for v in mc.values() if v} | TOLERADAS
    fora = sorted(cores - paleta)
    if fora:
        pend.append("cor fora da paleta do Podi: " + ", ".join(fora))

    # O verde não passa 4,5:1 sobre branco: só fundo, nunca texto. Texto de marca é o accent-ink.
    if (contraste(mc["brand"], mc["surface"]) < CONTRASTE_MIN
            and re.search(r"(?<![\w-])color:\s*%s" % re.escape(mc["brand"]), limpo, re.I)):
        pend.append(f"a cor de marca {mc['brand']} aparece como cor de texto (só pode ser fundo) — "
                    f"texto de marca é {mc['accent-ink']}")
    soltos = re.findall(r"(?<![\w-])color:var\(--accent\)", limpo)
    if len(soltos) > limpo.count(".logo--marca{color:var(--accent)}"):
        pend.append("color:var(--accent) fora do .logo--marca — a cor de marca não é cor de texto")

    pend += conferir_texto(limpo, m)

    imgs = re.findall(r"<img\b[^>]*>", limpo, re.I)
    sem_alt = [i for i in imgs if not re.search(r"\balt=", i)]
    if sem_alt:
        pend.append(f"{len(sem_alt)} imagem(ns) sem alt")

    secoes = re.findall(r'<section[^>]*class="[^"]*\b(slide|post)\b', limpo)
    peca_de_tela = bool(secoes)
    if peca_de_tela:
        # Vale: assets/ da peça, data:, a versão publicada no hub de marcas e, no modelo do
        # hub, a imagem vazia marcada com data-slot (quem usa o modelo preenche).
        fora = sorted({s for tag in re.findall(r"<img\b[^>]*>", limpo, re.I)
                       for s in re.findall(r'\bsrc="([^"]*)"', tag)
                       if not s.startswith(("assets/", "data:", HUB_PODI))
                       and not (s == "" and "data-slot=" in tag)})
        if fora:
            pend.append("imagem fora de assets/ (a peça não abre sozinha): " + ", ".join(fora))
    else:
        kb = len(html.encode("utf-8")) / 1024
        if kb >= 100:
            pend.append(f"HTML com {_num(kb, 1)} KB — o Gmail corta acima de 100 KB")
        proibido = sorted(set(re.findall(r"<script|<form|<iframe|display:\s*flex|calc\(|var\(--", limpo, re.I)))
        if proibido:
            pend.append("recurso que e-mail não suporta: " + ", ".join(proibido))
        sem_role = [t for t in re.findall(r"<table\b[^>]*>", limpo, re.I) if 'role="presentation"' not in t]
        if sem_role:
            pend.append(f'{len(sem_role)} tabela(s) sem role="presentation"')
        abre = len(re.findall(r"<!--\[if !mso\]>", limpo))
        if abre != len(re.findall(r"<!--\[if !mso\]><!-->", limpo)) or \
                abre != len(re.findall(r"<!--<!\[endif\]-->", limpo)):
            pend.append("condicional do Outlook quebrado (<!--[if !mso]><!--> … <!--<![endif]-->): "
                        "o botão ou o trecho some fora do Outlook")
        botoes = len(re.findall(r"<v:roundrect\b", limpo))
        links_botao = len(re.findall(r'<a [^>]*border-radius:100px', limpo))
        if botoes != links_botao:
            pend.append(f"{botoes} botão(ões) no Outlook e {links_botao} fora dele — cada CTA leva as duas metades")
        sem_target = [a for a in re.findall(r'<a [^>]*href="http[^>]*>', limpo, re.I) if 'target="_blank"' not in a]
        if sem_target:
            pend.append(f'{len(sem_target)} link(s) sem target="_blank"')
    permitidas = set() if peca_de_tela else set(m["envio"].get("variaveis") or []) | set(campos)
    sobras = sorted({v for v in re.findall(r"\{\{\s*([^}]+?)\s*\}\}", limpo) if v not in permitidas})
    if sobras:
        if peca_de_tela:
            motivo = "campo não preenchido"      # deck e post não têm variável de envio
        else:
            motivo = "placeholder não preenchido ou variável fora das permitidas"
        pend.append(f"{motivo}: " + ", ".join("{{%s}}" % s for s in sobras))
    if peca_de_tela:
        tipo = secoes[0]
        resumo = f"{len(secoes)} {'slides' if tipo == 'slide' else 'cards'}"
    else:
        resumo = f"e-mail, {_num(len(html.encode('utf-8')) / 1024, 1)} KB"
    return pend, resumo


def cmd_conferir(arquivos, campos=()):
    m = carregar()
    falhou = False
    for arq in arquivos:
        if not os.path.exists(arq):
            print(f"✗ {arq}: arquivo não existe")
            return 2
        conteudo = open(arq, encoding="utf-8").read()
        if arq.endswith(".txt"):
            pend, resumo = conferir_texto(conteudo, m), "texto"
        else:
            pend, resumo = conferir(conteudo, m, campos)
        falhou |= bool(pend)
        print(f"{'✓' if not pend else '✗'} {arq} — {resumo}")
        for p in pend:
            print(f"    - {p}")
    return 1 if falhou else 0


# ---------------------------------------------------------------------------
def main(argv):
    if argv == ["--marca"]:
        return cmd_marca()
    campos = ()
    if len(argv) >= 3 and argv[0] == "--campos":
        campos = tuple(c.strip() for c in argv[1].split(",") if c.strip())
        argv = argv[2:]
    if argv and not any(a.startswith("-") for a in argv):
        return cmd_conferir(argv, campos)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
