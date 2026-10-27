# Componentes — newsletter

Blocos de HTML de e-mail. **Copiar e colar** dentro do
[`templates/newsletter/base.html`](../../../templates/newsletter/base.html), no lugar marcado.
Não editar o arquivo do componente por campanha.

A numeração é a ordem em que os blocos costumam aparecer na peça.

| Arquivo | O que é |
|---|---|
| `00-hero-podi-news.html` | Header completo das edições do Podi News (ver abaixo) |
| `01-header.html` | Header padrão: logos Podi + Tacla Labs |
| `01b-header-empreendimento.html` | Header de **logo único**, centralizado numa placa branca: logo do shopping (modo empreendimento) |
| `02-hero-title.html` | Headline de abertura |
| `02a-eyebrow.html` | Tag / eyebrow acima de um título |
| `02b-titulo-secao.html` | Título de seção |
| `03-hero-image.html` | Imagem de abertura, largura inteira |
| `04-texto-cta.html` | Bloco de texto com CTA |
| `05-card-quote.html` | Citação |
| `06-card-oferta.html` | Card de oferta |
| `07-artigos-alternados.html` | Artigos com imagem alternando esquerda/direita (1:1) |
| `08-destaque-numeros.html` | Números de destaque com label. Variante A 3 colunas, B 1 coluna |
| `09-galeria-2col.html` | Galeria de duas colunas |
| `10-divider.html` | Divisor |
| `11-card-noticia.html` | Notícia com imagem no topo, largura inteira (16:9) |
| `12-card-noticia-compacta.html` | Notícia com miniatura ao lado do texto (1:1) |
| `13-card-conteudo.html` | Card único com todo o conteúdo dentro + os itens dele (texto, título de grupo, lista, nota, linha fina, CTA) |
| `13a-card-galeria-2col.html` | Item do `13`: galeria de 2 colunas 1:1 com texto e etiqueta opcional |
| `13b-card-extrato.html` | Item do `13`: extrato de dados, rótulo à esquerda e valor à direita |
| `90-social.html` | Ícones sociais do rodapé, centralizados — URLs já fixas |
| `90b-social-logo.html` | Rodapé social com logo à esquerda e ícones à direita. Variante A Podi, B logo e redes do empreendimento |
| `91-footer-legal.html` | Rodapé legal completo |
| `99-spacer.html` | Espaçador vertical |
| `_button.html` | CTA no padrão VML (`<v:roundrect>` + `<a>`). Variante A verde, B neutra escura |

Obrigatórios em toda peça: `01-header` (ou `00-hero-podi-news`), `90-social` (ou `90b-social-logo`),
`91-footer-legal`. No modo empreendimento: `01b-header-empreendimento`, `90b-social-logo`
variante B e `91-footer-legal`.
Entre blocos, usar `99-spacer`.

---

## O header do Podi News

Toda edição do **Podi News** abre com `00-hero-podi-news.html` — um único card de
raio 20px que empacota, nesta ordem:

1. topbar de 88px com logo Podi à esquerda e Tacla Labs à direita;
2. imagem da edição, 536×301, **flush e sem raio** (fica no meio do card);
3. eyebrow (ex.: `EDIÇÃO DE AGOSTO`), headline 30/38 e texto de apoio 16/25, centralizados.

Fonte do design: Figma **Podi-News-26-27**, node `1:422` (`hero-podi-news`).

**Não** usar `01-header` + `02a` + `02` + `03` soltos numa edição do Podi News. Nas outras
frentes, o header continua sendo o `01-header.html`.

Dark mode:

- O card **escurece como os cards de notícia**. Ele leva `.dm-surface`, e o texto leva
  `.dm-ink` / `.dm-body` / `.dm-tag` / `.dm-accent` como em qualquer outra seção.
- **A topbar é a exceção.** Ela fica numa placa branca própria (`.dm-logo`, com raio
  `20px 20px 0 0` para casar com o topo do card) e permanece branca nos dois modos.
  O "Tacla" do logo da Tacla Labs é preto e sumiria sobre `#242424`, e o
  `email-compat.md` proíbe trocar arquivo de imagem por CSS — a troca falha no Gmail e
  no Outlook. Por isso os dois logos ficam sem classe de dark mode: o fundo atrás deles
  é branco de qualquer jeito.
- Quando existir uma arte oficial da Tacla Labs legível sobre fundo escuro, a placa sai
  e a topbar passa a herdar o `.dm-surface` do card. Até lá, ela fica.

---

## Rodapé social: dois modelos

| Modelo | Arquivo | Quando usar |
|---|---|---|
| Ícones centralizados | `90-social.html` | Padrão de toda peça do Podi |
| Logo + ícones | `90b-social-logo.html` · variante A | Peça do Podi que quer a assinatura do logo no rodapé |
| Logo + ícones | `90b-social-logo.html` · variante B | Peça em que o remetente é o empreendimento (shopping, outlet) |

- A **variante A** usa o logo Podi verde e as redes oficiais do Podi — URLs fixas, como no `90-social`.
- A **variante B** usa o logo colorido do empreendimento e as redes **dele**, que vêm do
  briefing. Nunca misturar: logo do empreendimento com redes do Podi, ou o contrário.
- Os dois modelos ficam numa linha só também no mobile. O limite de largura do logo está
  no comentário do componente.
- Em qualquer modelo de peça Podi o `91-footer-legal` continua igual, com `© <ano> - Podi App`.

---

## Modo empreendimento

Peça em que o remetente é o empreendimento. Regra completa:
[`guidelines/marca-empreendimento.md`](../guidelines/marca-empreendimento.md). Resumo do que
o catálogo muda:

| Bloco | Uso no modo |
|---|---|
| `01b-header-empreendimento` | No lugar do `01-header`. Sem link e sem classe de dark mode |
| `03-hero-image` | A imagem da campanha |
| `08-destaque-numeros` variante B | O número principal: rótulo 16px em cima, número 32px embaixo |
| `13-card-conteudo` + itens `13a`/`13b` | Todo o resto do conteúdo, num card só, com um CTA no fim |
| `90b-social-logo` variante B | Logo e redes do empreendimento, ícones recoloridos |
| `91-footer-legal` | Igual, com o texto legal da promoção antes do `©` |

Os componentes vêm com os tokens e as classes `dm-*` do Podi, porque os blocos `08`, `13`,
`13a` e `13b` também servem às peças do Podi. No modo empreendimento, depois de colar:
trocar o grupo verde pela tabela do `scripts/paleta-empreendimento.py`, tirar as classes
`dm-*` e apontar os ícones para `imagens/icones/<rede>-campanha.png`. O `--conferir` do
script acusa o que sobrar.

### O card único

`13-card-conteudo` resolve e-mail curto de uma mensagem só — transacional, gatilho de
campanha —, em que vários cards soltos quebrariam a leitura. Ele conta como **uma** seção
no limite de quatro. Dentro dele:

- linha fina entre grupos, e **sempre** antes do botão (o item CTA já traz a linha);
- **um CTA só**, sempre o último item;
- `13a` é diferente do `09-galeria-2col`: o `09` é solto na página, 4:3 e sem texto; o
  `13a` vive dentro do card, é 1:1 e carrega texto.

---

## Caminhos de imagem

Os `src` dos componentes apontam para `../../brand/assets/…`, que é o caminho correto a
partir de `saida/<slug>/index.html`. Se o arquivo montado for para outro lugar, ajustar.
Antes de enviar, esses caminhos relativos viram URLs absolutas `https://`.
