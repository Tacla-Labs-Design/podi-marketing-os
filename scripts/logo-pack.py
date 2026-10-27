#!/usr/bin/env -S python3 -I
"""Monta o logo pack do Podi: a pasta com a página da marca e o .zip para baixar.

O logo é o SVG oficial (brand/assets/header/logo-podi.svg) com a cor gravada, nas três cores
oficiais — verde, branco, preto —, igual ao que o hub publica em podi/logos/. O desenho não
muda: nada de símbolo isolado, app icon, favicon ou animação, que o Podi não tem.

A página vem de hub/guia/index.html: mude lá e rode de novo. Os caminhos dela são relativos ao
pack, então ela abre do zip e no hub (https://marcas.taclalabs.workers.dev/podi/guia/).

Uso:
  python3 -I scripts/logo-pack.py
Saída (fora do Git): saida/logo-pack/podi-logo-pack/ e saida/logo-pack/podi-logo-pack.zip
scripts/publicar roda este script e envia a pasta e o zip ao hub.
"""

import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

# _logo.py mora ao lado; com `python3 -I` a pasta do script não entra sozinha no caminho.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _logo import LOGOS, RAIZ, pintar, png  # noqa: E402

BASE = RAIZ / "saida" / "logo-pack"
PACK = BASE / "podi-logo-pack"
ZIP = BASE / f"{PACK.name}.zip"
PAGINA = RAIZ / "hub" / "guia" / "index.html"
LARGURAS = (512, 1024, 2048, 4096)
MESES = "jan fev mar abr mai jun jul ago set out nov dez".split()


def main():
    if PACK.exists():
        shutil.rmtree(PACK)
    (PACK / "01-logo/svg").mkdir(parents=True)
    (PACK / "01-logo/png").mkdir(parents=True)

    pedidos = []
    for nome, (cor, _) in LOGOS.items():
        svg = PACK / f"01-logo/svg/{nome}.svg"
        svg.write_text(pintar(cor))
        pedidos += [(svg, PACK / f"01-logo/png/{nome}-{largura}.png", largura) for largura in LARGURAS]
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(lambda p: png(*p), pedidos))

    hoje = date.today()
    pagina = PAGINA.read_text()
    if pagina.count("VERSAO_DO_PACK") != 1:
        raise SystemExit("hub/guia/index.html: esperava um único VERSAO_DO_PACK para a data.")
    (PACK / "index.html").write_text(
        pagina.replace("VERSAO_DO_PACK", f"{hoje.day} {MESES[hoje.month - 1]} {hoje.year}"))

    # A página só pode citar arquivo que está no pack.
    faltam = sorted({c for c in re.findall(r'(?:src|href)="(01-[^"#?]+)"', pagina)
                     if not (PACK / c).is_file()})
    if faltam:
        raise SystemExit("hub/guia/index.html cita arquivo que não está no pack: " + ", ".join(faltam))

    ZIP.unlink(missing_ok=True)
    subprocess.run(["zip", "-rqX", ZIP.name, PACK.name, "-x", "*.DS_Store"], cwd=BASE, check=True)
    print(PACK)
    print(ZIP)


if __name__ == "__main__":
    main()
