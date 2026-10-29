#!/usr/bin/env python3
"""Exporta a peça montada: post em PNG, deck em PDF.

Usa o Google Chrome da máquina em modo sem janela — nada para instalar.

Uso:
  python3 scripts/exportar.py png saida/<slug>/index.html
        um PNG por <section class="post"> (ou "slide"), em saida/<slug>/png/01.png, 02.png…
        no tamanho real do canvas (post 1080×1350, slide 1920×1080)
  python3 scripts/exportar.py pdf saida/<slug>/index.html
        o deck inteiro em saida/<slug>/<slug>.pdf, um slide por página, em paisagem
  python3 scripts/exportar.py fontes saida/<slug>/index.html
        só confere se a fonte da peça carregou

Antes de exportar, confere se a primeira fonte de `--font` do :root carregou. Se não
carregou, o Chrome trocaria por outra em silêncio e a peça sairia fora do padrão — então para.

Saída 0 = ok. Saída 1 = não exportou (fonte ausente, Chrome ausente, nada para exportar).
Saída 2 = uso errado.
"""

import html as html_mod
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

CHROME_CANDIDATOS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]

# Tamanho de cada tipo de canvas. É o que o design system fixa (canvas.md de cada material).
CANVAS = {"post": (1080, 1350), "slide": (1920, 1080)}

# Some com a prévia (fundo, espaçamento, escala) e deixa só a seção pedida no canto 0,0.
CSS_EXPORTAR = """
<style id="__exportar">
html,body{background:transparent!important;padding:0!important;margin:0!important}
.stage,.deck,.grade{transform:none!important;zoom:1!important;width:auto!important;height:auto!important;
  margin:0!important;padding:0!important;display:block!important;gap:0!important}
.%(tipo)s{margin:0!important;box-shadow:none!important}
.%(tipo)s:not([data-exportar]){display:none!important}
.previa-legenda{display:none!important}
</style>
"""

# Mede a largura de um texto com a fonte da peça e com duas genéricas diferentes: se as duas
# medidas batem com as genéricas, a fonte não existe nesta máquina.
JS_FONTES = """
<script id="__fontes">
(function(){
  function largura(f){var c=document.createElement('canvas').getContext('2d');
    c.font='48px '+f;return c.measureText('Mais clientes mmmwwwiii 0123').width}
  var familia=(getComputedStyle(document.documentElement).getPropertyValue('--font')||'')
    .split(',')[0].trim();
  (document.fonts?document.fonts.ready:Promise.resolve()).then(function(){
    var ok=!!familia&&largura(familia+',monospace')!==largura('monospace')
                    &&largura(familia+',serif')!==largura('serif');
    document.documentElement.setAttribute('data-fontes',JSON.stringify({familia:familia,ok:ok}));
  });
})();
</script>
"""


def chrome():
    for c in CHROME_CANDIDATOS:
        if c and os.path.exists(c):
            return c
    raise SystemExit("✗ Não encontrei o Google Chrome nesta máquina. Ele é necessário para exportar.")


def rodar(args):
    return subprocess.run([chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                           "--no-first-run", "--no-default-browser-check", *args],
                          capture_output=True, text=True, timeout=180)


def temporario(original, conteudo):
    """Cópia ao lado do original, para os caminhos relativos (assets/) continuarem valendo."""
    fd, caminho = tempfile.mkstemp(prefix=".exportar-", suffix=".html", dir=os.path.dirname(original))
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(conteudo)
    return caminho


def injetar(html, trecho):
    return html.replace("</head>", trecho + "</head>", 1) if "</head>" in html else trecho + html


def conferir_fontes(arquivo):
    html = open(arquivo, encoding="utf-8").read()
    tmp = temporario(arquivo, injetar(html, JS_FONTES))
    try:
        r = rodar(["--virtual-time-budget=5000", "--dump-dom", "file://" + tmp])
    finally:
        os.remove(tmp)
    achado = re.search(r'data-fontes="([^"]*)"', r.stdout)
    if not achado:
        return None, False
    dado = json.loads(html_mod.unescape(achado.group(1)))
    return dado["familia"].strip("'\""), dado["ok"]


def exigir_fontes(arquivo):
    familia, ok = conferir_fontes(arquivo)
    if familia is None:
        print("✗ Não consegui abrir a peça no Chrome para conferir a fonte.")
        return False
    if not ok:
        print(f"✗ A fonte {familia} não carregou. Sem ela a peça sai com outra letra.\n"
              "  A DM Sans vem do Google Fonts (link no <head> do template): confira a internet e se "
              "o link está na peça, e rode de novo.")
        return False
    print(f"✓ fonte {familia} carregada")
    return True


def sem_comentarios(html):
    """Troca cada comentário HTML por espaços do mesmo tamanho: as posições continuam valendo,
    e um <section class="post"> citado num comentário do template não conta como post."""
    return re.sub(r"<!--.*?-->", lambda c: " " * len(c.group(0)), html, flags=re.S)


def secoes(html, tipo):
    return list(re.finditer(r'<section([^>]*class="[^"]*\b%s\b[^"]*"[^>]*)>' % tipo, sem_comentarios(html)))


def tipo_da_peca(html):
    for tipo in ("post", "slide"):
        if secoes(html, tipo):
            return tipo
    return None


def cmd_png(arquivo):
    html = open(arquivo, encoding="utf-8").read()
    tipo = tipo_da_peca(html)
    if not tipo:
        print('✗ Nenhum <section class="post"> nem "slide" na peça.')
        return 1
    if not exigir_fontes(arquivo):
        return 1
    achadas = secoes(html, tipo)
    largura, altura = CANVAS[tipo]
    pasta = os.path.join(os.path.dirname(arquivo), "png")
    os.makedirs(pasta, exist_ok=True)
    for antigo in os.listdir(pasta):
        if re.fullmatch(r"\d{2}\.png", antigo):
            os.remove(os.path.join(pasta, antigo))
    base = injetar(html, CSS_EXPORTAR % {"tipo": tipo})
    feitos = 0
    desloc = len(base) - len(html)          # o CSS injetado fica antes de todas as seções
    for n, s in enumerate(achadas, 1):
        # Marca só a n-ésima seção; as outras somem pelo CSS injetado.
        fim = s.end() + desloc
        marcado = base[:fim - 1] + " data-exportar>" + base[fim:]
        tmp = temporario(arquivo, marcado)
        destino = os.path.join(pasta, f"{n:02d}.png")
        try:
            rodar([f"--window-size={largura},{altura}", "--virtual-time-budget=5000",
                   "--default-background-color=00000000", f"--screenshot={destino}", "file://" + tmp])
        finally:
            os.remove(tmp)
        if os.path.exists(destino):
            feitos += 1
            print(f"  ✓ {os.path.relpath(destino)}  {largura}×{altura}")
        else:
            print(f"  ✗ {tipo} {n}: o Chrome não gerou a imagem")
    print(f"{'✓' if feitos == len(achadas) else '✗'} {feitos} de {len(achadas)} {tipo}s exportados em {os.path.relpath(pasta)}/")
    return 0 if feitos == len(achadas) else 1


def cmd_pdf(arquivo):
    html = open(arquivo, encoding="utf-8").read()
    if tipo_da_peca(html) != "slide":
        print('✗ PDF é para deck: a peça não tem <section class="slide">.')
        return 1
    if not exigir_fontes(arquivo):
        return 1
    pasta = os.path.dirname(os.path.abspath(arquivo))
    destino = os.path.join(pasta, os.path.basename(pasta) + ".pdf")
    rodar(["--no-pdf-header-footer", "--virtual-time-budget=5000",
           f"--print-to-pdf={destino}", "file://" + os.path.abspath(arquivo)])
    if not os.path.exists(destino):
        print("✗ O Chrome não gerou o PDF.")
        return 1
    paginas = len(re.findall(rb"/Type\s*/Page[^s]", open(destino, "rb").read()))
    slides = len(secoes(html, "slide"))
    ok = paginas == slides
    print(f"{'✓' if ok else '✗'} {os.path.relpath(destino)} — {paginas} páginas para {slides} slides")
    return 0 if ok else 1


def main(argv):
    if len(argv) != 2 or argv[0] not in ("png", "pdf", "fontes"):
        print(__doc__)
        return 2
    cmd, arquivo = argv
    if not os.path.exists(arquivo):
        print(f"✗ {arquivo}: arquivo não existe")
        return 2
    arquivo = os.path.abspath(arquivo)
    if cmd == "fontes":
        return 0 if exigir_fontes(arquivo) else 1
    return cmd_png(arquivo) if cmd == "png" else cmd_pdf(arquivo)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
