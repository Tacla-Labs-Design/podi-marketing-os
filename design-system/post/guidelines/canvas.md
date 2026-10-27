# Canvas do post — regras técnicas

## O canvas é fixo

Um post tem **exatamente 1080 × 1350 px** (feed 4:5 — o maior espaço que Instagram e LinkedIn
dão no feed). Não rola, não quebra, não tem outra versão.

- Todo post é um `<section class="post">` com `overflow:hidden`, dentro do `<div class="grade">`
  do template.
- **Margem de segurança de 64px** em todos os lados para texto e logo. O Instagram corta a
  prévia da grade do perfil para 3:4 no centro (1012 × 1350): nada importante nos 34px de cada
  lateral além da margem.
- A exceção à margem é o que sangra de propósito: foto, mockup, grafismo de fundo.
- **Tamanho mínimo de texto: 24px**, e só para texto de apoio (lista curta, cargo, URL). Título
  e frase principal começam em 56px. No celular o post aparece com ~1/3 da largura: 24px vira
  ~8pt — é o limite do legível.

## Formatos

| Formato | Tamanho | Estado |
|---|---|---|
| Feed 4:5 | 1080 × 1350 | **Padrão** — todos os modelos |
| Quadrado 1:1 | 1080 × 1080 | *Proposta* — sem modelo aprovado |
| Story / Reels 9:16 | 1080 × 1920 | *Proposta* — sem modelo aprovado |

Pedido de story ou quadrado: montar em 4:5 e relatar a ausência como proposta. Nunca esticar
nem cortar um modelo 4:5 para outro formato.

## Pode usar CSS moderno

Flex, grid, `var(--token)`, degradê, `backdrop-filter`, `mask-image`, SVG inline. Continua
proibido:

- **Cor escrita direto** fora do `:root` do template. Toda cor sai de `../tokens.md`.
- **Fonte que não seja a do Podi.**
- `<script>` que mude conteúdo. O único JS do template é o da prévia.
- Imagem de URL externa. Tudo em `assets/` da própria pasta.

## Prévia e export

```bash
open saida/<slug>/index.html                              # prévia: os posts lado a lado
python3 -I scripts/exportar.py png saida/<slug>/index.html   # → saida/<slug>/png/01.png, 02.png…
```

O `exportar.py` abre a peça no Chrome da máquina, confere se a fonte da peça carregou
(para se não carregou — sem ela o post sai com outra letra), e fotografa cada `<section
class="post">` no tamanho real, na ordem do arquivo. Carrossel de 6 cards = 6 PNGs numerados,
na ordem em que sobem.

**Conferir os PNGs antes de entregar**, abrindo cada um: é no PNG que aparece texto cortado,
imagem que não carregou e fonte trocada.
