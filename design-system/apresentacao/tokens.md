# Tokens — Apresentação Podi

> Os valores abaixo são os do **Podi**, e é com eles que o `:root` de
> `templates/apresentacao/base.html` está escrito. Trocar cor é mexer neste arquivo, no `:root`
> do template e em `brand/marca.json`, na mesma leva (`CHANGELOG.md`).

Os nomes de token são os mesmos de `design-system/newsletter/tokens.md` sempre que o papel
é o mesmo — `ink`, `body`, `muted`, `surface`, `hairline`. Um token com nome igual e valor
diferente (`page`) está marcado abaixo.

## Cor de marca

**`#48DB84`** (verde Podi).

Contraste sobre branco: **1,79:1** — reprova em qualquer texto. Isso governa três regras:

| Situação | Cor certa | Por quê |
|---|---|---|
| Texto **em cima** do verde | `#101010` | 10,6:1. Texto branco sobre o verde é **proibido** |
| Texto/link de marca **sobre branco** | `#0C6E3B` | 6,4:1 |
| Texto/link de marca no **dark mode** | `#6FE9A2` | 11,5:1 sobre `#1A1A1A` |

Na apresentação o verde tem um papel a mais que no e-mail: ele é o **fundo do slide**
(`page`), o campo de cor sobre o qual os cards brancos flutuam. Continua não sendo cor
de texto em nenhuma hipótese.

## Cor secundária

**`#9934FF`** (roxo Tacla Labs). Só **detalhe gráfico** — ver
[`brand/README.md`](../../brand/README.md) e [`guidelines/uso-do-roxo.md`](guidelines/uso-do-roxo.md).

| Token | Hex | Uso — e só este |
|---|---|---|
| `accent-2` | `#9934FF` | Glifo do ícone, ponto de timeline, bullet, régua sob título (início do gradiente) |
| `accent-2-mid` | `#C58CFF` | Fim do gradiente da régua |
| `accent-2-soft` | `#E9DBFF` | Fundo do chip que segura o ícone |
| `accent-2-line` | `#E0CCFA` | Borda fina de container e de tabela |

Contraste do `accent-2` sobre `surface`: **4,9:1**. Sobre o verde `page`: **2,4:1** —
por isso detalhe roxo só existe **dentro de card branco**, nunca solto sobre o verde.

## Fundos

| Token | Hex | Uso |
|---|---|---|
| `page` | `#48DB84` | Fundo do slide — o campo de cor da marca |
| `page-light` | `#EDF7F1` | Fundo do slide quando o deck é claro (decks longos, muitos dados) |
| `surface` | `#FFFFFF` | Fundo dos cards, containers e faixas de conteúdo |
| `surface-alt` | `#F6FAF7` | Linha zebrada de tabela, card de segundo nível |
| `hairline` | `#D2E7DA` | Divisores neutros |
| `ink-field` | `#101010` | Fundo de slide preto — capa alternativa e divisor de seção |

`page` e `page-light` são exclusivos: **um deck escolhe um dos dois e não alterna**, exceto
nos divisores de seção, que são sempre o oposto do corpo do deck para marcar a virada.

## Texto

| Token | Hex | Uso | Contraste sobre `surface` |
|---|---|---|---|
| `ink` | `#101010` | Títulos e texto forte | 19,3:1 |
| `body` | `#4A4A4A` | Texto corrido | 9,0:1 |
| `muted` | `#6E6E6E` | Legendas, fonte do dado, rodapé do slide | 5,2:1 |
| `ink-on-accent` | `#101010` | Todo texto **em cima do verde** | 10,6:1 |
| `ink-inverse` | `#FFFFFF` | Texto sobre `ink-field` `#101010` | 19,3:1 |
| `accent-ink` | `#0C6E3B` | Texto/link **de marca** sobre fundo claro | 6,4:1 |
| `accent-on-dark` | `#6FE9A2` | Texto/link **de marca** sobre `ink-field` | 11,5:1 sobre `#101010` |

O verde `#48DB84` **nunca** é `color:` — nem sobre preto, onde passaria de contraste.
Texto que precisa ser verde usa `accent-ink` (fundo claro) ou `accent-on-dark` (fundo preto).

`muted` sobre o verde `page` dá 3,1:1 — **legenda solta sobre o verde é proibida**. Ou vai
em card branco, ou sobe para `ink-on-accent`.

## Tipografia

Stack: `'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif`

Dimensionada para projeção em 1920 × 1080. Máximo de **dois pesos por deck** (400 e 700).

| Papel | Tamanho / line-height / peso |
|---|---|
| Título de capa | 96px / 104px / 700, letter-spacing -2px |
| Título de slide | 64px / 72px / 700, letter-spacing -1px |
| Subtítulo de slide | 32px / 44px / 400 |
| Título de card | 40px / 48px / 700 |
| Título de card compacto | 32px / 40px / 700 |
| Body | 28px / 40px / 400 |
| Body small | 24px / 34px / 400 |
| Número de destaque | 88px / 96px / 700, letter-spacing -2px |
| Label de número | 24px / 32px / 400 |
| Eyebrow / tag | 20px / 26px / 700, letter-spacing 1px, uppercase |
| Legenda / fonte do dado | 20px / 28px / 400 |
| Número do slide | 20px / 20px / 400 |

**Piso de 24px** para qualquer texto que a plateia precise ler. Abaixo disso só legenda,
fonte de dado e número de página — coisas que existem para quem recebe o PDF depois.

## Espaçamento e formas

Escala: `16 · 24 · 32 · 40 · 48 · 64 · 80 · 120`

- **Margem de segurança do slide: 96px** em todos os lados. Nada de conteúdo fora dela —
  projetor corta borda.
- Padding interno de card: 48–64px
- Gap entre cards de uma grade: 32px · entre blocos de conteúdo: 64px
- Raio: card 32px · card compacto 24px · imagem 24px · chip de ícone 20px · botão 100px
- Régua roxa sob título: 120 × 6px, raio 3px, gradiente `accent-2` → `accent-2-mid`
- Chip de ícone: 88 × 88px, fundo `accent-2-soft`, glifo 40px em `accent-2`
- Borda fina: 2px em `accent-2-line`

## Imagens

Tudo exportado em **2x** do tamanho de exibição — o slide já é grande, e o deck vira PDF.

| Slot | Exibição | Exportar (2x) | Proporção |
|---|---|---|---|
| Foto sangrada de slide inteiro | 1920 × 1080 | 3840 × 2160 | 16:9 |
| Meia tela (split) | 960 × 1080 | 1920 × 2160 | 8:9 — vertical |
| Foto no topo de card | 768 × 432 | 1536 × 864 | 16:9 |
| Celular na meia tela | 520 × 1040 | 1040 × 2080 | 1:2 vertical — mockup em PNG transparente **ou** foto do celular em mão |
| Logo de cliente na grade | 240 × 120 | 480 × 240 | Caixa fixa, logo centralizado |
| Retrato de citação | 200 × 200 | 400 × 400 | 1:1 |

O **logo Podi não entra nesta tabela**: ele é vetor (`<use href="#logo-marca">`), não tem
exportação e não perde qualidade em nenhum tamanho. Ver `slides/README.md` → "O logo".

Foto fora da proporção **não se distorce e não se corta por conta própria** — mesma regra do
e-mail. Relatar o arquivo, a proporção que veio e a esperada.
