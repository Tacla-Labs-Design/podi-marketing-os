# Tokens — post do Optimall

Os valores dos posts do Optimall. A fonte de máquina é o `:root` de
[`templates/post/base-optimall.html`](../../../templates/post/base-optimall.html). Os posts
usam só `var(--token)` — nunca hex.

As cores são **as mesmas do deck** — tabela completa em
[`design-system/apresentacao/optimall/tokens.md`](../../apresentacao/optimall/tokens.md).
Aqui ficam só o que é próprio do post.

Origem: o Figma *Social Media – Optimall*. O post **não é recolorido**: nasce nesta paleta e
passa só pelo `aplicar-marca.py conferir optimall`.

## Cores próprias do post

| Token | Hex | Uso |
|---|---|---|
| `--roxo-fundo-escuro` | `#7500EB` | Fim do degradê vertical do post roxo (`.post--roxo-desce`) |
| `--roxo-vidro-1` → `--roxo-vidro-2` | roxo escuro a 50% | Painel de vidro escuro do post de citação |
| `--lilas-painel` | `#BD7CFF` | Painel de destaque sobre a faixa roxa |
| `--lilas-pontos` | `#E0C3FF` | Pontos e anéis do post |
| `--lavanda-luz` | `#FCFAFF` | Centro do degradê claro (`.post--claro`) |

## Fundos

| Classe | O que é |
|---|---|
| `.post--lavanda` | `--lavanda` chapado — o fundo dos posts de foto e de citação |
| `.post--claro` | Radial `--lavanda-luz` → `--lavanda` |
| `.post--roxo` | `--roxo` chapado |
| `.post--roxo-desce` | `--roxo` → `--roxo-fundo-escuro`, de cima para baixo |

**Texto sobre o roxo é sempre branco** (ou `--lavanda` no vidro).

## Tipografia

**Halyard Text**, a mesma do deck. O Figma dos posts foi desenhado em DM Sans; o padrão usa a
fonte da marca, com os mesmos tamanhos e um peso abaixo (a Halyard é mais encorpada que a DM
Sans: título em 400, corpo em Book).

| Classe | Tamanho / entrelinha | Peso | Uso |
|---|---|---|---|
| `.t-display` | 96 / 1.05, −0,02em | normal | Título de post roxo |
| `.t-titulo-lg` | 88 / 1.1, −0,03em | normal | Título centralizado |
| `.t-titulo` | 64 / 1.05, −0,02em | normal | Título sobre claro (degradê cinza); branco sobre roxo |
| `.t-titulo-md` | 60 / 1.1 | normal | Título de painel |
| `.t-citacao` | 80 / 1.05, −0,03em | semi | Citação curta |
| `.t-citacao-md` | 56 / 1.1 | livro | Citação longa (com `<b>` no trecho forte) |
| `.t-sub` | 36 / 1.2 | livro | Subtítulo (`--apoio`) |
| `.t-card` | 40 / 1.2 | semi | Título de card |
| `.t-corpo` | 36 / 1.2 | livro | Corpo |
| `.t-corpo-sm` | 28 / 1.4 | livro | Corpo curto |
| `.t-lista` | 24 / 1.5 | livro | Lista curta de apoio |
| `.t-url` | 30 / 1.2 | livro | Site escrito |
| `.t-autor` / `.t-cargo` | 30 / 24 | negrito / normal | Autor do depoimento |
| `.t-cta` | 35 / 1 | livro (+ `<b>`) | Pílula de chamada |

**Mínimo de 24px**, e só para apoio. Título e frase principal a partir de 56px.

## Forma

Margem de segurança **64px** para texto e logo; o topo costuma começar em 80. Raio de foto,
faixa e card: `--r-card-sm` (32px). Pílula: `--r-pill`.

## Logo

Os mesmos três `<symbol>` do deck. No post, o logo **positivo** fica centralizado no pé
(≈326px) nos posts claros; o **negativo**, no topo ou no card, nos posts roxos.

## Imagens

`brand/optimall/assets/fotos/` (fotos de pessoas dos modelos), `produto/` (telas),
`grafismos/`. Foto nova segue o Style Lock do Optimall e entra na mesma proporção do slot.
