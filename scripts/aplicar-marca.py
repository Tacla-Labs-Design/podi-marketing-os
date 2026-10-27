#!/usr/bin/env python3
"""Marca da peça: Podi ou Optimall (ou outra marca irmã em brand/<marca>/).

Os componentes de e-mail (e os slides do Podi) são escritos com os valores do Podi; um
e-mail de outra marca é montado igual e, no fim, este script troca cada cor pelo mesmo papel
da marca dela e confere o resultado. A paleta de cada marca mora em brand/<marca>/marca.json.
Regra completa: design-system/newsletter/guidelines/marcas.md.

Marca com biblioteca própria de deck e post (o Optimall: design-system/apresentacao/optimall/,
design-system/post/optimall/) não recolore deck nem post — eles já nascem na paleta dela. Para
eles, só o `conferir`, que aceita também a `paleta_extra` do marca.json.

Uso:
  python3 scripts/aplicar-marca.py validar  <marca>
        confere se o marca.json está completo e se os contrastes obrigatórios passam
  python3 scripts/aplicar-marca.py derivar  <marca> "<principal>" ["<secundária>"] [--gravar]
        propõe o grupo de marca a partir da cor principal (maintainer). Com --gravar,
        escreve as cores no marca.json e gera os ícones sociais da marca
  python3 scripts/aplicar-marca.py aplicar  <marca> saida/<slug>/index.html [...]
        troca, na peça montada, as cores, links, redes, ícones, rodapé e logo do deck
  python3 scripts/aplicar-marca.py conferir <marca> saida/<slug>/index.html [...]
        só leitura: acusa cor fora da paleta, sobra de outra marca e variável não permitida

Saída 0 = ok. Saída 1 = pendência (não entregar assim). Saída 2 = uso errado.
Só biblioteca padrão do Python: nada para instalar.
"""

import json
import os
import re
import sys

from _cor import contraste, de_lch, hex_rgb, lch, recolorir_png, rgb_hex, rgb_oklab

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCIA = "podi"          # a marca em que componentes e slides são escritos
CONTRASTE_MIN = 4.5
CONTRASTE_GRAFICO = 3.0       # detalhe gráfico (ícone, régua, borda): WCAG 1.4.11
REDES_ICONE = ["instagram", "facebook", "linkedin", "spotify"]

# Cores técnicas do shell do deck que não são token (fundo do preview na tela).
TOLERADAS = {"#2A2A2A"}

# Papéis do grupo de marca, derivados da cor principal (ou da secundária).
GRUPO_MARCA = ["brand", "ink-on-brand", "accent-ink", "accent-on-dark", "page-light",
               "accent-soft", "hairline", "surface-alt", "accent-soft-dark"]
GRUPO_SECUNDARIA = ["accent-2", "accent-2-mid", "accent-2-soft", "accent-2-line"]

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
def carregar(marca):
    caminho = os.path.join(RAIZ, "brand", marca, "marca.json")
    if not os.path.exists(caminho):
        existentes = sorted(d for d in os.listdir(os.path.join(RAIZ, "brand"))
                            if os.path.exists(os.path.join(RAIZ, "brand", d, "marca.json")))
        raise SystemExit(f"Marca '{marca}' não existe. Marcas disponíveis: {', '.join(existentes)}.")
    with open(caminho, encoding="utf-8") as f:
        m = json.load(f)
    m["_arquivo"] = caminho
    m["_slug"] = marca
    return m


def norm(h):
    return h.upper() if h else h


def pendencias_marca(m):
    """O que falta no marca.json para uma peça poder ser montada."""
    p = []
    for papel, v in m["cores"].items():
        if not v:
            p.append(f"cor '{papel}' sem valor")
    for chave in ("cta", "privacidade", "termos"):
        # false = a marca não tem esse documento (o Optimall não tem Termos de Uso): o link sai da peça.
        if m["links"].get(chave) is False and chave != "cta":
            continue
        if not m["links"].get(chave):
            p.append(f"link '{chave}' sem valor")
    for chave in ("svg", "png"):
        arq = m["logo"].get(chave)
        if not arq or not os.path.exists(os.path.join(RAIZ, arq)):
            p.append(f"logo {chave.upper()} não encontrado ({arq})")
    for rede, url in m["redes"].items():
        if url and not os.path.exists(os.path.join(RAIZ, m["icones"].format(rede=rede))):
            p.append(f"ícone de {rede} não encontrado ({m['icones'].format(rede=rede)})")
    return p


def biblioteca_propria(marca):
    """Deck e post com layout próprio da marca: não se recolorem a partir do Podi."""
    return os.path.isdir(os.path.join(RAIZ, "design-system", "apresentacao", marca))


def _num(v, casas=2):
    return f"{v:.{casas}f}".replace(".", ",")


def contrastes(m):
    c, linhas = m["cores"], []
    for rotulo, fg, bg, minimo in PARES:
        if c.get(fg) and c.get(bg):
            v = contraste(c[fg], c[bg])
            linhas.append((v >= minimo, rotulo, c[fg], c[bg], v, minimo))
    return linhas


# ---------------------------------------------------------------------------
# validar
# ---------------------------------------------------------------------------
def cmd_validar(marca):
    m = carregar(marca)
    print(f"Marca {m['nome']} · status {m['status']}\n")
    falhou = False
    pend = pendencias_marca(m)
    if pend:
        falhou = True
        print("Faltando no marca.json")
        for p in pend:
            print(f"  ✗ {p}")
        print()
    print("Contrastes obrigatórios")
    for ok, rotulo, fg, bg, v, minimo in contrastes(m):
        falhou |= not ok
        print(f"  {'✓' if ok else '✗'} {rotulo:<40} {fg} / {bg}  {_num(v)}:1 (mín. {_num(minimo, 1)})")
    if not m["envio"].get("variaveis"):
        print("\n  ! regra de envio pendente: nenhuma variável {{...}} é permitida até ela ser definida")
    ref = carregar(REFERENCIA)
    if m["cores"].get("ink-on-brand") and norm(m["cores"]["ink-on-brand"]) != norm(ref["cores"]["ink-on-brand"]):
        if biblioteca_propria(marca):
            print(f"\n  · texto sobre a cor de marca é {m['cores']['ink-on-brand']}: o e-mail troca no botão;"
                  "\n    deck e post da marca têm biblioteca própria, já escrita com essa regra")
        else:
            print(f"\n  ! o texto sobre a cor de marca é {m['cores']['ink-on-brand']}: o e-mail troca só no botão;"
                  "\n    o deck, que usa a cor de marca como fundo do slide, ainda não tem regra para isso — proposta")
    if falhou:
        print("\n✗ Marca incompleta ou com contraste reprovado. Não montar peça dela.")
        return 1
    if m["status"] != "aprovado":
        print("\n✓ Tudo preenchido e com contraste. Falta o maintainer marcar \"status\": \"aprovado\".")
        return 1
    print("\n✓ Marca pronta para uso.")
    return 0


# ---------------------------------------------------------------------------
# derivar (maintainer)
# ---------------------------------------------------------------------------
def _fator(base, ref_hex):
    _, c_base, _ = lch(rgb_oklab(hex_rgb(base)))
    _, c_ref, _ = lch(rgb_oklab(hex_rgb(ref_hex)))
    return max(0.4, min(1.0, c_base / c_ref)) if c_ref else 1.0


def _mesma_luz(ref_hex, base, fator):
    """Claridade e saturação relativa do token de referência, na matiz da base."""
    L, C, _ = lch(rgb_oklab(hex_rgb(ref_hex)))
    _, _, H = lch(rgb_oklab(hex_rgb(base)))
    return de_lch(L, C * fator, H)


def _ajustar(cor, fundos, subir):
    """Escurece (ou clareia) em OKLab, mesma matiz, até passar 4,5:1 em todos os fundos."""
    L, C, H = lch(rgb_oklab(hex_rgb(cor)))
    while min(contraste(cor, f) for f in fundos) < CONTRASTE_MIN and 0 < L < 1:
        L = min(1.0, L + 0.005) if subir else max(0.0, L - 0.005)
        cor = de_lch(L, C, H)
    return cor


def derivar(ref, principal, secundaria):
    rc = ref["cores"]
    base = rgb_hex(hex_rgb(principal))
    f = _fator(base, rc["brand"])
    c = {"brand": base}
    for papel in ("page-light", "accent-soft", "hairline", "surface-alt", "accent-soft-dark", "accent-on-dark"):
        c[papel] = _mesma_luz(rc[papel], base, f)
    c["accent-ink"] = _ajustar(base, [rc["surface"], c["page-light"], c["accent-soft"]], subir=False)
    c["accent-on-dark"] = _ajustar(c["accent-on-dark"], [rc["page-dark"], rc["ink"]], subir=True)
    if contraste(rc["ink"], base) >= CONTRASTE_MIN:
        c["ink-on-brand"] = rc["ink"]
    elif contraste(rc["surface"], base) >= CONTRASTE_MIN:
        c["ink-on-brand"] = rc["surface"]
    else:
        c["ink-on-brand"] = None
    if secundaria:
        sec = rgb_hex(hex_rgb(secundaria))
        f2 = _fator(sec, rc["accent-2"])
        c["accent-2"] = sec
        for papel in ("accent-2-mid", "accent-2-soft", "accent-2-line"):
            c[papel] = _mesma_luz(rc[papel], sec, f2)
    else:
        # Sem secundária: o detalhe gráfico sai do próprio grupo de marca (proposta).
        c.update({"accent-2": c["accent-ink"], "accent-2-mid": base,
                  "accent-2-soft": c["accent-soft"], "accent-2-line": c["hairline"]})
    return c


def cmd_derivar(marca, principal, secundaria, gravar):
    if marca == REFERENCIA:
        print("O Podi é a referência: a paleta dele não se deriva, está nos tokens.")
        return 2
    ref, m = carregar(REFERENCIA), carregar(marca)
    try:
        novas = derivar(ref, principal, secundaria)
    except ValueError:
        print("Cor inválida. Use hex de 6 dígitos, como #1B4DFF.")
        return 2
    _, c_base, _ = lch(rgb_oklab(hex_rgb(novas["brand"])))
    if c_base < 0.02:
        print(f"✗ {novas['brand']} é neutra demais para derivar um grupo de marca (saturação {c_base:.3f}).")
        return 1
    if novas["ink-on-brand"] is None:
        print(f"✗ Nem #101010 nem branco passam 4,5:1 sobre {novas['brand']}. Não serve de cor de fundo de botão.")
        return 1

    print(f"Proposta de paleta · {m['nome']} · principal {novas['brand']}"
          + (f" · secundária {novas['accent-2']}" if secundaria else " · sem secundária") + "\n")
    print("  Papel              Podi       " + m["nome"])
    for papel in GRUPO_MARCA + GRUPO_SECUNDARIA:
        print(f"  {papel:<18} {ref['cores'][papel]}    {novas[papel]}")
    if not secundaria:
        print("\n  ! sem secundária: régua, chip e bullet usam o próprio grupo de marca (proposta — decidir)")
    if novas["ink-on-brand"] != ref["cores"]["ink-on-brand"]:
        print(f"\n  ! texto sobre a cor de marca vira {novas['ink-on-brand']}: e-mail ok (troca no botão);"
              "\n    o deck ainda não tem regra para fundo de slide escuro — proposta")

    teste = dict(m, cores=dict(m["cores"], **novas))
    print("\nContrastes")
    reprovou = False
    for ok, rotulo, fg, bg, v, minimo in contrastes(teste):
        reprovou |= not ok
        print(f"  {'✓' if ok else '✗'} {rotulo:<40} {fg} / {bg}  {_num(v)}:1 (mín. {_num(minimo, 1)})")
    if reprovou:
        print("\n✗ Contraste reprovado. Revisar as cores com o design antes de gravar.")
        return 1

    if not gravar:
        print("\nNada foi gravado. Revisar a tabela e rodar de novo com --gravar para escrever no marca.json.")
        return 0

    m_arq = m.pop("_arquivo")
    m.pop("_slug")
    m["cores"].update(novas)
    with open(m_arq, "w", encoding="utf-8") as fh:
        json.dump(m, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n✓ Cores gravadas em {os.path.relpath(m_arq, RAIZ)} (status continua '{m['status']}').")

    print("\nÍcones sociais")
    for rede in REDES_ICONE:
        origem = os.path.join(RAIZ, ref["icones"].format(rede=rede))
        destino = os.path.join(RAIZ, m["icones"].format(rede=rede))
        if not os.path.exists(origem):
            continue
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        w, h = recolorir_png(origem, destino, novas["brand"])
        print(f"  ✓ {os.path.relpath(destino, RAIZ)}  {w}×{h}")
    return 0


# ---------------------------------------------------------------------------
# aplicar
# ---------------------------------------------------------------------------
def _viewbox(svg_caminho):
    svg = open(os.path.join(RAIZ, svg_caminho), encoding="utf-8").read()
    vb = re.search(r'viewBox="([^"]+)"', svg)
    if not vb:
        raise SystemExit(f"{svg_caminho}: SVG sem viewBox.")
    return vb.group(1)


def _symbol(svg_caminho):
    svg = open(os.path.join(RAIZ, svg_caminho), encoding="utf-8").read()
    vb = re.search(r'viewBox="([^"]+)"', svg)
    corpo = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S)
    if not vb or not corpo:
        raise SystemExit(f"{svg_caminho}: SVG sem viewBox ou sem conteúdo.")
    interno = re.sub(r"<title>.*?</title>\s*", "", corpo.group(1).strip(), flags=re.S)
    interno = re.sub(r'\s(fill|stroke)="(?!none)[^"]*"', "", interno)
    return f'<symbol id="logo-marca" viewBox="{vb.group(1)}">{interno}</symbol>'


def aplicar(html, ref, m):
    rc, mc = ref["cores"], m["cores"]
    pend = []

    # 1. Texto do botão: só onde o fundo é a cor de marca (as duas metades do CTA).
    if norm(mc["ink-on-brand"]) != norm(rc["ink-on-brand"]):
        marca_ref, tinta_ref = re.escape(rc["brand"]), re.escape(rc["ink-on-brand"])
        html = re.sub(r'<a [^>]*background-color:%s[^>]*>' % marca_ref,
                      lambda a: re.sub(r'([;"])color:%s' % tinta_ref, r"\1color:__INK_ON_BRAND__", a.group(0), flags=re.I),
                      html, flags=re.I)
        html = re.sub(r'(fillcolor="%s">.*?<center style="color:)%s' % (marca_ref, tinta_ref),
                      r"\1__INK_ON_BRAND__", html, flags=re.I | re.S)
        if "--accent:" in html and not biblioteca_propria(m["_slug"]):
            pend.append("deck com texto claro sobre a cor de marca ainda não tem regra — avisar o maintainer")

    # 2. Cores: cada hex do Podi vira o mesmo papel da marca, numa passada só.
    mapa = {}
    for papel, v in rc.items():
        if papel == "ink-on-brand" or not mc.get(papel):
            continue
        mapa.setdefault(norm(v), norm(mc[papel]))
    html = re.sub(r"#[0-9A-Fa-f]{6}\b", lambda x: mapa.get(x.group(0).upper(), x.group(0)), html)
    html = html.replace("__INK_ON_BRAND__", norm(mc["ink-on-brand"]))

    # 3. Ícones sociais, links, redes e rodapé.
    padrao_ref = re.escape(ref["icones"]).replace(r"\{rede\}", "([a-z]+)")
    html = re.sub(padrao_ref, lambda x: m["icones"].format(rede=x.group(1)), html)
    for chave, url in ref["links"].items():
        if m["links"].get(chave):
            html = html.replace(url, m["links"][chave])
    for rede, url in ref["redes"].items():
        if m["redes"].get(rede):
            html = html.replace(url, m["redes"][rede])
    if m["links"].get("termos") is False:
        # Marca sem Termos de Uso: sai o link e o separador que vem antes dele no rodapé legal.
        html = re.sub(r'\s*&nbsp;\|&nbsp;\s*<a [^>]*href="%s"[^>]*>.*?</a>' % re.escape(ref["links"]["termos"]),
                      "", html, flags=re.S)
    html = html.replace(ref["rodape"]["assinatura"], m["rodape"]["assinatura"])
    html = re.sub(r"\n[ \t]*\.logo-tacla\s*\{[^}]*\}", "", html)   # classe da assinatura Podi + Tacla

    # 4. Deck: logo vetorial (o <symbol> e a proporção de cada <svg> que o usa) e rótulo acessível.
    if '<symbol id="logo-marca"' in html:
        html = re.sub(r'<symbol id="logo-marca".*?</symbol>', lambda _: _symbol(m["logo"]["svg"]), html, flags=re.S)
        vb_ref, vb = _viewbox(ref["logo"]["svg"]), _viewbox(m["logo"]["svg"])
        html = re.sub(r'(<svg class="logo[^"]*"[^>]*viewBox=")%s(")' % re.escape(vb_ref), r"\g<1>%s\2" % vb, html)
    html = html.replace(f'aria-label="{ref["nome"]}"', f'aria-label="{m["nome"]}"')
    html = html.replace(f'<title>{ref["nome"]}</title>', f'<title>{m["nome"]}</title>')
    return html, pend


def cmd_aplicar(marca, arquivos):
    if marca == REFERENCIA:
        print("Peça do Podi: nada a trocar, os componentes já são do Podi.")
        return 0
    ref, m = carregar(REFERENCIA), carregar(marca)
    if m["status"] != "aprovado" or pendencias_marca(m):
        print(f"✗ A marca {m['nome']} ainda não está pronta (status '{m['status']}'). "
              f"Rode: python3 scripts/aplicar-marca.py validar {marca}")
        return 1
    falhou = False
    for arq in arquivos:
        if not os.path.exists(arq):
            print(f"✗ {arq}: arquivo não existe")
            return 2
        html = open(arq, encoding="utf-8").read()
        if biblioteca_propria(marca) and re.search(r'class="[^"]*\b(slide|post)\b', html):
            print(f"✗ {arq}: deck e post do {m['nome']} já nascem na biblioteca própria da marca — "
                  "não se recolorem. Rode só o conferir.")
            return 1
        novo, pend = aplicar(html, ref, m)
        open(arq, "w", encoding="utf-8").write(novo)
        pend += conferir(novo, m, ref)
        falhou |= bool(pend)
        print(f"{'✓' if not pend else '✗'} {arq} — marca {m['nome']} aplicada")
        for p in pend:
            print(f"    - {p}")
    return 1 if falhou else 0


# ---------------------------------------------------------------------------
# conferir
# ---------------------------------------------------------------------------
def _sem_comentarios(html):
    return re.sub(r"/\*.*?\*/", "", re.sub(r"<!--(?!\[if).*?-->", "", html, flags=re.S), flags=re.S)


def conferir(html, m, ref):
    pend, mc = [], m["cores"]
    limpo = _sem_comentarios(html)

    cores = {c.upper() for c in re.findall(r"#[0-9A-Fa-f]{6}\b", limpo)}
    extra = {norm(v) for k, v in (m.get("paleta_extra") or {}).items() if not k.startswith("_")}
    paleta = {norm(v) for v in mc.values() if v} | extra | TOLERADAS
    if m["_slug"] != REFERENCIA:
        do_ref = {norm(v) for v in ref["cores"].values()} - paleta
        sobra = sorted(cores & do_ref)
        if sobra:
            pend.append(f"cor do {ref['nome']} sobrando: " + ", ".join(sobra))
        cores -= do_ref
    fora = sorted(cores - paleta)
    if fora:
        pend.append("cor fora da paleta da marca: " + ", ".join(fora))

    # Cor de marca como texto só é proibida quando ela não passa 4,5:1 sobre branco (o verde do Podi).
    if (contraste(mc["brand"], mc["surface"]) < CONTRASTE_MIN
            and re.search(r"(?<![\w-])color:\s*%s" % re.escape(mc["brand"]), limpo, re.I)):
        pend.append(f"a cor de marca {mc['brand']} aparece como cor de texto (só pode ser fundo)")
    soltos = re.findall(r"(?<![\w-])color:var\(--accent\)", limpo)
    if len(soltos) > limpo.count(".logo--marca{color:var(--accent)}"):
        pend.append("color:var(--accent) fora do .logo--marca — a cor de marca não é cor de texto")

    for termo in m.get("nao_pode_conter", []):
        n = len(re.findall(termo, limpo, re.I))
        if n:
            pend.append(f"sobra de outra marca: '{termo.replace(chr(92) + 'b', '')}' aparece {n}×")

    peca_de_tela = bool(re.search(r'<section[^>]*class="[^"]*\b(slide|post)\b', limpo))
    permitidas = set() if peca_de_tela else set(m["envio"].get("variaveis") or [])
    sobras = sorted({v for v in re.findall(r"\{\{\s*([^}]+?)\s*\}\}", limpo) if v not in permitidas})
    if sobras:
        if peca_de_tela:
            motivo = "campo não preenchido"      # deck e post não têm variável de envio
        else:
            motivo = ("placeholder não preenchido ou variável fora das permitidas" if permitidas
                      else "regra de envio da marca pendente: nenhuma variável é permitida")
        pend.append(f"{motivo}: " + ", ".join("{{%s}}" % s for s in sobras))
    return pend


def cmd_conferir(marca, arquivos):
    ref, m = carregar(REFERENCIA), carregar(marca)
    if marca != REFERENCIA and pendencias_marca(m):
        print(f"✗ A marca {m['nome']} está incompleta. Rode: python3 scripts/aplicar-marca.py validar {marca}")
        return 1
    falhou = False
    for arq in arquivos:
        if not os.path.exists(arq):
            print(f"✗ {arq}: arquivo não existe")
            return 2
        pend = conferir(open(arq, encoding="utf-8").read(), m, ref)
        falhou |= bool(pend)
        print(f"{'✓' if not pend else '✗'} {arq}")
        for p in pend:
            print(f"    - {p}")
    return 1 if falhou else 0


# ---------------------------------------------------------------------------
def main(argv):
    args = list(argv)
    gravar = "--gravar" in args
    if gravar:
        args.remove("--gravar")
    if len(args) < 2:
        print(__doc__)
        return 2
    cmd, marca, resto = args[0], args[1].lower(), args[2:]
    if cmd == "validar" and not resto:
        return cmd_validar(marca)
    if cmd == "derivar" and 1 <= len(resto) <= 2:
        return cmd_derivar(marca, resto[0], resto[1] if len(resto) == 2 else None, gravar)
    if cmd == "aplicar" and resto:
        return cmd_aplicar(marca, resto)
    if cmd == "conferir" and resto:
        return cmd_conferir(marca, resto)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
