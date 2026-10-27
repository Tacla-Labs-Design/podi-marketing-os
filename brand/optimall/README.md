# Brand — Optimall

Regras da marca Optimall. Valem **junto** com as regras comuns de [`brand/README.md`](../README.md)
— camada mais alta do Marketing OS: **nada abaixo pode contradizer as duas**.

Fontes da identidade: o site publicado [optimall.com.br](https://www.optimall.com.br) (código em
`lp-optimall`, que é a referência — o `DESIGN.md` de lá tem hex antigos) e os arquivos do
Figma *Apresentação Comercial 2026* e *Social Media – Optimall*. Aprovado pelo maintainer em
2026-09-30.

| Arquivo | O que tem |
|---|---|
| [`marca.json`](marca.json) | Fonte de máquina: cores, logo, links, textos, redes, contato, fonte |
| [`mensagens.md`](mensagens.md) | **O que dizer**: público, posicionamento, módulos, números oficiais, voz, frases aprovadas |
| [`links-oficiais.md`](links-oficiais.md) | CTA, contato, rodapé legal, redes, textos fixos |
| [`photography/STYLE-LOCK-OPTIMALL.md`](photography/STYLE-LOCK-OPTIMALL.md) | Direção fotográfica |
| `assets/` | Logo, ícones sociais e de interface, clientes, parceiros, produto, fotos, grafismos |

---

## Marca

**Optimall** — a plataforma B2B que reúne Campanhas, Aplicativo, Clube de Benefícios e CRM
para shoppings, com a marca de cada empreendimento. **A peça do Optimall é 100% dele**:

- **não cita o Podi**, não usa o logo, a cor, as redes nem os links do Podi;
- **não leva a Tacla Labs**.

**A marca é masculina.** Escreva sempre **o Optimall**, **do Optimall**, **no Optimall**,
**pelo Optimall**. Nunca "a Optimall" — nem quando a frase vem do site, que ainda usa o feminino.

## Público e tom

**B2B, sempre.** Fala com quem decide no shopping — superintendência, marketing, CRM, operação
— e com parceiros comerciais. **Não fala com o consumidor final.** Tom objetivo, seguro,
orientado a número, um CTA por bloco: *Fale com um consultor*. Tudo em
[`mensagens.md`](mensagens.md).

## Cor

| Papel | Hex | Uso |
|---|---|---|
| Roxo Optimall | `#9934FF` | A cor da marca. Fundo de capa, faixa, botão, chip de ícone, destaque |
| Texto sobre o roxo | `#FFFFFF` | **Sempre branco** sobre o roxo (4,9:1). Nunca `#101010`, nunca cinza |
| Roxo de texto | `#9025F4` | O roxo quando ele é **texto** sobre fundo claro (link, número, palavra de destaque) |
| Lavanda | `#FAF5FF` · `#F3E8FF` · `#E9D5FF` | Fundos claros, cards, chips |
| Lilás | `#C084FC` · `#D8B4FE` | Só grafismo: pontos do pattern, linhas, brilho |
| Tinta | `#18181B` | Títulos sobre claro |
| Corpo | `#353E4F` | Texto corrido sobre claro |
| Apoio | `#525A6F` | Legenda, rótulo, texto secundário |

Diferente do Podi, **o roxo do Optimall pode ser texto** sobre fundo claro — mas na versão
`#9025F4`, que passa 4,5:1 sobre branco e sobre as lavandas. O `#9934FF` fica para fundo,
ícone e grafismo.

O Optimall **não tem secundária**: régua, chip e bullet usam o próprio roxo. Os degradês, o
vidro e os lilases do deck e do post estão nos `tokens.md` de cada material
(`design-system/apresentacao/optimall/tokens.md`, `design-system/post/optimall/tokens.md`)
e em `paleta_extra` do `marca.json`. Nenhuma cor fora dessas listas.

No **e-mail**, a paleta entra pelo `scripts/aplicar-marca.py aplicar optimall` (papel por
papel, a partir dos blocos do Podi). No **deck** e no **post**, a peça já nasce na biblioteca
própria do Optimall — não se recolore.

## Tipografia

**Halyard Text** (Adobe Fonts, licença do time). Pesos em uso: **400** (corpo) e **500**
(títulos, números, botões). Títulos com espaçamento negativo (−0,02em).

- Precisa estar **ativada no computador** (Creative Cloud → Fontes). O `scripts/exportar.py`
  confere antes de gerar PNG ou PDF e para se ela faltar.
- **E-mail não usa Halyard**: quem recebe não tem a fonte. O e-mail segue a pilha de fontes do
  design system de newsletter.

## Logo

Em `assets/header/`. O logo do Optimall é **tricolor** — símbolo de três formas sobrepostas e
a palavra *optimall*. Tem duas versões oficiais, e **nenhuma se recolore**:

| Arquivo | Versão | Onde |
|---|---|---|
| `logo-optimall.svg` | Positivo: símbolo `#9934FF`/`#525A6F`/`#C084FC`, palavra `#525A6F` | Fundo branco ou lavanda |
| `logo-optimall-negativo.svg` | Negativo: símbolo `#E5CCFF`/branco/`#B770FF`, palavra branca | Fundo roxo |
| `simbolo-optimall.svg` | Só o símbolo, positivo | Selo pequeno, avatar, favicon |
| `logo-optimall.png` | Positivo, 2x, transparente (286×48, exibido a 143×24) | E-mail (`01b` e `90b` variante B) |

Diferente do Podi, o logo **não é monocromático**: não se pinta por `currentColor`, não se troca
cor por `filter`, não se redesenha. No deck e no post ele entra como os dois `<symbol>` do
template da marca (`#logo-optimall` e `#logo-optimall-negativo`).

## Grafismos

A linguagem visual do Optimall (deck e post) — degradê radial roxo, pattern de pontos lilás
que some em direção ao centro, o símbolo gigante em transparência, cards brancos e painéis de
vidro sobre lavanda, pílulas de número, chips de ícone roxos. Arquivos em
`assets/grafismos/`; as receitas, nos `tokens.md` de deck e post.

## Imagens de produto e clientes

- `assets/produto/` — telas do painel e do app (do site e do Figma). São a prova visual do
  produto: preferir estas a foto genérica.
- `assets/clientes/` — logos dos shoppings clientes: `<nome>-roxo.svg` (deck, do Figma) e
  `<nome>.png` (cinza-azulado, do site).
- `assets/parceiros/` — logos das integrações (estacionamento, cinema, IntranetMall).
- `assets/fotos/` — as fotos aprovadas dos posts.
- `assets/icones-ui/` — ícones HugeIcons bulk em `currentColor`, para chips de deck e post.

## E-mail

O e-mail do Optimall **não sai pelo servidor do Podi** — sai por outro sistema, cujas regras
(variáveis aceitas, hospedagem das imagens) ainda não foram passadas. Até lá:

- a peça sai **sem nenhuma variável `{{...}}`** — nem `{{email}}` no rodapé;
- o relatório de entrega avisa que a regra de envio está pendente.

O botão do e-mail é roxo com **texto branco** (o `aplicar` troca). O rodapé legal leva só a
Política de Privacidade: o Optimall não tem Termos de Uso.

Ver `envio` em `marca.json` e `design-system/newsletter/guidelines/variaveis-envio.md`.

## Fotografia

Mesma direção do Podi — luz, lente, composição —, com a paleta e as cenas do Optimall:
[`photography/STYLE-LOCK-OPTIMALL.md`](photography/STYLE-LOCK-OPTIMALL.md).
