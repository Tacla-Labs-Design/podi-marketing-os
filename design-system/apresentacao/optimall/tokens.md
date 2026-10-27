# Tokens — apresentação do Optimall

Os valores do deck do Optimall. A fonte de máquina é o `:root` de
[`templates/apresentacao/base-optimall.html`](../../../templates/apresentacao/base-optimall.html);
este arquivo explica **para que serve cada um**. Os slides usam só `var(--token)` — nunca hex.

Origem: o Figma *Apresentação Comercial 2026* e o site optimall.com.br. As cores de marca
também estão em `brand/optimall/marca.json` (`cores` e `paleta_extra`), que é o que o
`aplicar-marca.py conferir` usa para recusar cor fora da paleta.

O deck do Optimall **não é recolorido**: nasce nesta paleta. Não passar pelo `aplicar`.

## Cor

### Marca

| Token | Hex | Uso |
|---|---|---|
| `--roxo` | `#9934FF` | A cor da marca. Fundo de capa e fecho, chip sólido, ícone sobre claro, grafismo |
| `--roxo-texto` | `#9025F4` | O roxo quando ele é **texto** sobre fundo claro (tag, link, palavra) — passa 4,5:1 |
| `--roxo-luz` | `#AD5CFF` | Centro do degradê radial do fundo roxo |
| `--roxo-700` | `#821FE5` | Palavra de destaque em título (`.t-destaque`), pílula de número |
| `--roxo-500` | `#A855F7` | Régua sob título, ponto de status, conector |
| `--roxo-sombra` | `#4F009E` | Só dentro do símbolo gigante (marca d'água) |
| `--disco-meio`, `--disco-borda` | `#AB57FF`, `#BC7AFF` | Degradê do disco do símbolo (`.disco`) |

**Texto sobre o roxo é sempre branco** (`--branco`, ou `--branco-90`/`--branco-80` para
subtítulo e legenda). Nunca preto, nunca cinza, nunca lilás.

### Lilases e lavandas

| Token | Hex | Uso |
|---|---|---|
| `--lilas-400` | `#C084FC` | Pontos do pattern sobre roxo, tag grande, linha tracejada |
| `--lilas-300` | `#D8B4FE` | Pontos do pattern, tag de status |
| `--lilas-200` | `#E9D5FF` | Tag, chip claro, pontos, borda de card |
| `--lilas-borda` | `#E6CCFF` | Borda de grade e de card |
| `--lavanda` | `#F3E8FF` | Borda do degradê claro, painel de lista |
| `--lavanda-50` | `#FAF5FF` | Fundo claro chapado |

### Neutros

| Token | Hex | Uso |
|---|---|---|
| `--branco` | `#FFFFFF` | Card, texto sobre roxo |
| `--titulo-1` → `--titulo-2` | `#353E4F` → `#525A6F` | Degradê do título sobre fundo claro |
| `--tinta` | `#181D27` | Título de card |
| `--texto` | `#374151` | Corpo sobre claro |
| `--apoio` | `#525A6F` | Corpo de card, legenda, número do slide |
| `--borda-card` | `#E2E8F0` | Borda fina de card |
| `--borda-device` | `#E5E5E5` | Moldura de tela (`.device`) |

Transparências são sempre do branco ou do roxo da marca, e já são tokens: `--branco-90` …
`--branco-0`, `--roxo-10`, `--roxo-07`, `--roxo-0`, `--sombra`.

## Fundos

| Classe | O que é | Onde |
|---|---|---|
| `.slide--roxo` | Degradê radial `--roxo-luz` → `--roxo`, a partir do canto superior esquerdo | Capa, fecho, plataforma, divisor |
| `.slide--claro` | Branco com degradê radial para `--lavanda` no canto inferior direito | Slides de módulo |
| `.slide--claro-2` | Branco com degradê radial para `--lavanda` a partir da esquerda | White label, cards, título + texto |
| `.slide--branco` | Branco chapado | Segurança (os anéis dão o tom) |

## Grafismos

- **Pattern de pontos** — `.pontos` (1600×1200): pontos de 2,5px a cada 19,17px, que somem num
  degradê radial. `--baixo` inverte o sentido do sumiço. Cor: `--sobre-roxo` (`#C084FC`, sobre o
  roxo), `--200` ou `--300` (sobre claro). A posição de cada um é do slide: em geral um sangrando
  no canto superior esquerdo e outro no inferior direito.
- **Anéis** — `.aneis`: círculos concêntricos de roxo 7% → transparente. Tamanho e centro do slide.
- **Símbolo gigante** — `assets/simbolo-gigante.svg` (1669×1106), marca d'água sobre o roxo na
  capa e no fecho. Sai de `brand/optimall/assets/grafismos/`.
- **Disco do símbolo** — `.disco`: círculo com degradê roxo e o símbolo do logo negativo no
  centro. Une os quatro cards do slide de plataforma e o zigue-zague do CRM.
- **Vidro** — `.vidro` e os retângulos concêntricos translúcidos, só sobre o roxo.
- **Régua** — `.regua` (400×4, roxo → transparente); `.regua--centro` em slide centralizado;
  branca sobre o roxo.

## Tipografia

**Halyard Text**, instalada na máquina (Adobe Fonts). Pesos por token: `--w-livro` (Book),
`--w-normal`, `--w-medio`, `--w-semi`, `--w-negrito`. Nenhuma outra fonte — onde o Figma usa
Inter ou DM Sans em algum texto de apoio, o deck usa Halyard com o mesmo tamanho.

| Classe | Tamanho / entrelinha | Peso | Uso |
|---|---|---|---|
| `.t-capa` | 96 / 1.2, −0,02em | normal | Frase da capa |
| `.t-fecho` | 88 / 1.2, −0,02em | normal | Frase do fecho |
| `.t-titulo` | 72 / 1.1, −0,01em | semi | Título do slide. Degradê cinza sobre claro, branco sobre roxo |
| `.t-titulo-md` | 64 / 1.1 | semi | Título longo (slide de problema) |
| `.t-destaque` | — | — | Palavra do título em `--roxo-700` |
| `.t-sub` | 32 / 1.4 | livro | Subtítulo sobre roxo (`--branco-90`) |
| `.t-lead` | 28 / 1.4 | médio | Primeira frase do corpo |
| `.t-corpo` | 28 / 1.4 | livro | Corpo |
| `.t-corpo-sm` | 24 / 1.5 | livro | Corpo longo |
| `.t-item` | 24 / 1.3 | livro | Item de lista com chip |
| `.t-card` | 32 / 1.2 | médio | Título de card |
| `.t-card-sm` | 28 / 1.3 | semi | Título de card pequeno |
| `.t-card-corpo` | 28 / 1.4 | livro | Corpo de card |
| `.t-card-corpo-sm` | 24 / 1.5 | livro | Corpo de card pequeno |
| `.t-num` / `.t-num-pre` / `.t-num-label` | 80 / 48 / 32 | normal / médio / normal | Número, "+ de", legenda do número |
| `.tag` | 16 / 1.1, +0,05em, caixa alta | semi | Eyebrow: "MÓDULO", "WHITE LABEL" |
| `.t-rotulo` | 18 / 1.4, +0,05em, caixa alta | semi | Rótulo sobre roxo ("FALE COM NOSSO TIME COMERCIAL") |

**Mínimo de 24px** para qualquer texto que a plateia precise ler (é o mesmo limite do Podi).

## Forma

| Token | Valor | Uso |
|---|---|---|
| `--r-painel` | 72px | Painel grande |
| `--r-card` | 48px | Card, faixa |
| `--r-card-md` | 42px | Card com borda |
| `--r-card-sm` | 32px | Tile, imagem |
| `--r-chip` / `--r-chip-sm` | 24 / 20px | Chip sólido / chip claro |
| `--r-pill` | 9999px | Tag, pílula, disco |
| `--safe` | 64px | Margem de segurança do texto |

**Margem de segurança: 64px** (não 96 como no Podi — é a grade do Figma do Optimall). Mockup,
foto e grafismo podem sangrar.

## Chips de ícone

| Classe | Tamanho | Fundo | Ícone |
|---|---|---|---|
| `.chip` | 80 | `--roxo`, borda `--branco-12` | branco |
| `.chip--lg` / `.chip--xl` | 120 / 112 | idem | branco |
| `.chip--claro` (`-sm`, `-xs`) | 64 (56, 48) | `--lilas-200` | `--roxo`, 32px |
| `.chip--branco` | 104 | branco com sombra | `--roxo` |

Ícones: **HugeIcons bulk** (duas camadas, a de trás a 40%), em `currentColor`, colados inline.
Os arquivos ficam em `brand/optimall/assets/icones-ui/`. Nunca ícone de outra família.

## Logo

Dois `<symbol>` no template, tricolores, **nunca recoloridos**:

| Fundo | Uso |
|---|---|
| Roxo | `<use href="#logo-optimall-negativo"/>`, `viewBox="0 0 143 24"` |
| Claro | `<use href="#logo-optimall"/>`, `viewBox="0 0 238 40"` |
| Selo | `<use href="#simbolo-optimall"/>`, `viewBox="0 0 40 40"` |
| Selo sobre roxo | `<svg viewBox="0 0 36.2 24"><use href="#logo-optimall-negativo" width="143" height="24"/></svg>` |

Tamanhos em uso: 443px na capa, 599px no fecho, 332px em faixa.

## Imagens

Tudo em `saida/<slug>/assets/`, copiado de `brand/optimall/assets/` (`produto/`, `clientes/`,
`parceiros/`, `grafismos/`, `fotos/`). As telas de produto dos modelos já estão no tamanho do
slot, em 2x. Tela nova do painel ou do app: PNG com fundo transparente, na mesma proporção da
que ela substitui — não distorcer, não cortar.
