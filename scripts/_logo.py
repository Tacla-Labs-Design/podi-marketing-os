"""Logo do Podi — as três cores oficiais e a rasterização em PNG.

Usado por scripts/logo-pack.py (monta o logo pack) e scripts/publicar (que envia o pack ao hub).
O desenho não muda: o logo é uma forma só, pintada por currentColor (brand/assets/header/
logo-podi.svg), e cada versão é o mesmo SVG com a cor gravada. Regra de qual cor vai em qual
fundo: brand/README.md.

PNGs saem do Google Chrome da máquina, fundo transparente. Só biblioteca padrão do Python.
"""

import re
import subprocess
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

LOGO_FONTE = "brand/assets/header/logo-podi.svg"
LOGOS = {
    "podi-logo-verde": ("#31D06E", "Verde: fundo branco ou claro, em qualquer tamanho"),
    "podi-logo-branco": ("#FFFFFF", "Branco: sobre o verde de marca, o preto ou foto"),
    "podi-logo-preto": ("#101010", "Preto: uma cor, impressão"),
}


def pintar(cor):
    """O SVG oficial com a cor gravada no lugar de currentColor."""
    fonte = (RAIZ / LOGO_FONTE).read_text()
    if fonte.count('fill="currentColor"') != 1:
        raise SystemExit(f"{LOGO_FONTE}: esperava um único fill=\"currentColor\" para pintar.")
    return fonte.replace('fill="currentColor"', f'fill="{cor}"')


def svg_tamanho(svg):
    m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', svg.read_text())
    return float(m.group(1)), float(m.group(2))


def png(svg, destino, largura):
    """Rasteriza o SVG no Chrome, fundo transparente, na largura pedida."""
    w, h = svg_tamanho(svg)
    altura = round(largura * h / w)
    with tempfile.TemporaryDirectory() as tmp:
        pagina = Path(tmp) / "r.html"
        pagina.write_text(f"<html><body style='margin:0'><img src='file://{svg}' "
                          f"style='display:block;width:{largura}px;height:{altura}px'></body></html>")
        subprocess.run([CHROME, "--headless", "--hide-scrollbars", "--default-background-color=00000000",
                        "--force-device-scale-factor=1", f"--window-size={largura},{altura}",
                        f"--screenshot={destino}", f"file://{pagina}"], capture_output=True, check=True)
