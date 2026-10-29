# Tokens — Apresentação Podi

> Os valores abaixo são os do **Podi**, e é com eles que o `:root` de
> `templates/apresentacao/base.html` está escrito. Trocar cor é mexer neste arquivo, no `:root`
> do template e em `brand/marca.json`, na mesma leva (`CHANGELOG.md`).

Os nomes de token são os mesmos de `design-system/newsletter/tokens.md` sempre que o papel
é o mesmo — `ink`, `body`, `muted`, `surface`, `hairline`. Um token com nome igual e valor
diferente (`page`) está marcado abaixo.

Referência visual: os slides do arquivo **[DECK] Simple Deck - Podi**, no Figma — capa, split
com cards e plataforma com lista de recursos. Medidas em px do canvas de 1920 × 1080.

## Cor de marca

**`#31D06E`** (verde Podi).

Contraste sobre branco: **2,02:1** — reprova em qualquer texto. Isso governa três regras:

| Situação | Cor certa | Por quê |
|---|---|---|
| Texto **em cima** do verde | `#101010` | 9,4:1. Texto branco sobre o verde é **proibido** |
| Texto/link de marca **sobre branco** | `#0C6E3B` | 6,4:1 |
| Texto/link de marca no **dark mode** | `#6FE9A2` | 11,5:1 sobre `#1A1A1A` |

Na apresentação o verde tem um papel a mais que no e-mail: ele é o **fundo do slide**
(`page`), o campo de cor sobre o qual os cards brancos flutuam. Continua não sendo cor
de texto em nenhuma hipótese.

| Token | Hex | Uso — e só este |
|---|---|---|
| `accent-deep` | `#074A21` | Tagline e frase de marca **em cima do verde** (capa). 5,2:1 |
| `accent-line` | `#2E9054` | Linhas do ripple sobre o verde. Vem gravado em `brand/assets/deck/ripple-podi.svg` |
| `accent-edge` | `#28C463` | Borda de 3px das telas do app sobre o verde |

## Cor secundária

**`#9934FF`** (roxo Tacla Labs). Só **detalhe gráfico** — ver
[`brand/README.md`](../../brand/README.md) e [`guidelines/uso-do-roxo.md`](guidelines/uso-do-roxo.md).

| Token | Hex | Uso — e só este |
|---|---|---|
| `accent-2` | `#9934FF` | Ícone, ponto de timeline, bullet, régua sob título |
| `accent-2-soft` | `#E9DBFF` | Miolo do ponto da timeline |
| `accent-2-line` | `#E6CCFF` | Borda fina da caixa de recursos e de tabela |
| `accent-2-mid` | `#C58CFF` | Reserva: hoje nenhum slide usa |

Contraste do `accent-2` sobre `surface`: **4,9:1**. Sobre o verde `page`: **2,4:1** —
por isso detalhe roxo só existe **dentro de card branco** ou sobre fundo claro, nunca solto
sobre o verde.

## Fundos

| Token | Hex | Uso |
|---|---|---|
| `page` | `#31D06E` | Fundo do slide — o campo de cor da marca |
| `page-light` | `#EDF7F1` | Fundo do slide quando o deck é claro (decks longos, muitos dados) |
| `surface` | `#FFFFFF` | Fundo dos cards, containers, faixas de conteúdo e do painel do `07` |
| `surface-alt` | `#F6FAF7` | Linha zebrada de tabela, card de segundo nível |
| `hairline` | `#D2E7DA` | Divisores neutros |
| `ink-field` | `#101010` | Fundo de slide preto — divisor de seção |

`page` e `page-light` são exclusivos: **um deck escolhe um dos dois e não alterna**, exceto
nos divisores de seção, que são sempre o oposto do corpo do deck para marcar a virada.
`slide--white` (o `06` e o painel do `07`) vale nos dois.

## Texto

| Token | Hex | Uso | Contraste sobre `surface` |
|---|---|---|---|
| `ink` | `#101010` | Títulos e texto forte | 19,3:1 |
| `body` | `#4A4A4A` | Texto corrido | 9,0:1 |
| `muted` | `#6E6E6E` | Legendas, fonte do dado, rodapé do slide | 5,2:1 |
| `ink-on-accent` | `#101010` | Todo texto **em cima do verde**, menos a tagline | 9,4:1 |
| `accent-deep` | `#074A21` | Tagline em cima do verde | 5,2:1 sobre o verde |
| `ink-inverse` | `#FFFFFF` | Texto sobre `ink-field` `#101010` | 19,3:1 |
| `accent-ink` | `#0C6E3B` | Texto/link **de marca** sobre fundo claro | 6,4:1 |
| `accent-on-dark` | `#6FE9A2` | Texto/link **de marca** sobre `ink-field` | 11,5:1 sobre `#101010` |

O verde `#31D06E` **nunca** é `color:` — nem sobre preto, onde passaria de contraste.
Texto que precisa ser verde usa `accent-ink` (fundo claro) ou `accent-on-dark` (fundo preto).

`muted` sobre o verde `page` dá 2,5:1 — **legenda solta sobre o verde é proibida**. Ou vai
em card branco, ou sobe para `ink-on-accent`.

## Tipografia

Stack: `'DM Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif`

Dimensionada para projeção em 1920 × 1080. Três pesos, cada um com papel fixo: **600** nos
títulos e rótulos, **400** no texto, **700** só no destaque dentro do texto (`<strong>`) e nos
números grandes.

| Papel | Classe | Tamanho / line-height / peso |
|---|---|---|
| Título de capa e divisor | `t-capa` | 96px / 104px / 600, letter-spacing -2% |
| Título de slide | `t-slide` | 64px / 70px / 600, letter-spacing -2% |
| Frase de abertura (`07`) | `t-lead` | 52px / 62px / 600, letter-spacing -1% |
| Tagline (capa) | `t-tagline` | 40px / 48px / 400, `<strong>` 700, letter-spacing -2% |
| Subtítulo de slide | `t-sub` | 32px / 44px / 400 |
| Título de card | `t-card` | 48px / 58px / 600 |
| Título de card compacto | `t-card-sm` | 32px / 40px / 600 |
| Rótulo de item de lista | `t-item` | 24px / 29px / 600 |
| Body | `t-body` | 28px / 42px / 400 |
| Body small — o texto dos cards | `t-body-sm` | 24px / 36px / 400 |
| Número de destaque | `t-num` | 88px / 96px / 700, letter-spacing -2% |
| Label de número | `t-num-label` | 24px / 32px / 400 |
| Eyebrow / tag | `t-eyebrow` | 20px / 26px / 600, letter-spacing 1px, uppercase |
| Legenda / fonte do dado | `t-legenda` | 20px / 28px / 400 |
| Número do slide | — | 20px / 20px / 400 |

**Piso de 24px** para qualquer texto que a plateia precise ler. Abaixo disso só legenda,
fonte de dado e número de página — coisas que existem para quem recebe o PDF depois.

## Espaçamento e formas

Escala: `16 · 24 · 32 · 40 · 48 · 56 · 64 · 80 · 120`

- **Margem de segurança do slide: 64px** em todos os lados para texto. Card pode encostar a
  24px da borda, porque o texto dentro dele já fica a 64px (24 + 40 de padding).
- Padding interno de card: 40px (`card--lg`: 64px)
- Gap entre cards de uma grade: 24px · entre blocos de conteúdo: 48px · título → régua → texto: 24 a 32px
- Raio: card 32px · card compacto 24px · caixa de recursos 40px · tela do app 38px · imagem 24px ·
  botão 100px · canto do painel branco do `07`: 160px, só embaixo à esquerda
- **Régua roxa**: 4px de altura, raio 2px, gradiente `accent-2` → transparente. 200px sob título
  (`regua`), 56px dentro de card (`regua regua--sm`)
- **Ícone**: HugeIcons Bulk Rounded, solto, sem chip, em `accent-2`. 80px no alto de card
  (`ico ico--lg`), 32px em lista (`ico`). Pack em `brand/assets/icones-bulk/`
- **Caixa de recursos** (`.feat`): borda 2px `accent-2-line`, raio 40px, padding 56px 40px,
  duas colunas, gap 32px 40px, item = ícone de 32px + 24px + rótulo `t-item`
- **Tela do app** (`.tela`): borda 3px `accent-edge`, raio 38px, sombra
  `drop-shadow(78px 78px 58px rgba(10,13,18,.12))`

## Imagens

Tudo exportado em **2x** do tamanho de exibição — o slide já é grande, e o deck vira PDF.

| Slot | Exibição | Exportar (2x) | Proporção |
|---|---|---|---|
| Foto sangrada de slide inteiro | 1920 × 1080 | 3840 × 2160 | 16:9 |
| Foto do split (`04`) | 1087 × 1080 | 2174 × 2160 | ~1:1 — com área calma onde o logo branco pousa |
| Foto no topo de card | 768 × 432 | 1536 × 864 | 16:9 |
| Tela do app (`00`, `07`) | 344 × 737 · 237 × 508 | 786 × 1704 | 393 × 852, captura de tela do app |
| Logo de cliente na grade | 240 × 120 | 480 × 240 | Caixa fixa, logo centralizado |
| Retrato de citação | 200 × 200 | 400 × 400 | 1:1 |

**Ativos fixos** (`brand/assets/deck/`, copiar para `assets/` do deck): `ripple-podi.svg` (as
linhas em volta do logo), `mao-celular.png` (a mão com o app aberto, PNG transparente),
`tela-app-nota.png` e `tela-app-campanha.png` (as duas telas de apoio). Não se redesenham.

O **logo Podi não entra nesta tabela**: ele é vetor (`<use href="#logo-marca">`), não tem
exportação e não perde qualidade em nenhum tamanho. Ver `slides/README.md` → "O logo".

Foto fora da proporção **não se distorce e não se corta por conta própria** — mesma regra do
e-mail. Relatar o arquivo, a proporção que veio e a esperada.
