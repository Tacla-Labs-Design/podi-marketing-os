# Slides — apresentação

Os 16 tipos de slide. Cada arquivo é um `<section class="slide">` completo, com o CSS do
próprio layout — **se copia** para dentro de `templates/apresentacao/base.html`, não se
edita aqui.

O `NN` é a ordem típica no deck, não uma obrigação: ninguém precisa usar os 16, e a ordem
real vem do roteiro.

| Arquivo | O que é |
|---|---|
| `_slide.html` | O shell de um slide. Todo tipo começa daqui |
| `00-capa.html` | Abertura. Verde cheio, logo grande, tagline |
| `01-agenda.html` | O que o deck vai cobrir. Bullet roxo |
| `02-divisor-secao.html` | Virada de assunto. Fundo preto, número + nome da seção |
| `03-titulo-texto.html` | Uma ideia só, sem apoio visual. Coluna única |
| `04-split-foto-cards.html` | Foto sangrando à esquerda, grade 2×2 de cards à direita. `split--dir` espelha |
| `05-cards-grid.html` | 3 ou 4 cards de peso igual, com chip de ícone |
| `06-features-2col.html` | Lista longa de recursos em duas colunas, container de borda fina |
| `07-mockup-app.html` | Mockup de celular à esquerda, conteúdo em faixa branca à direita |
| `08-numeros.html` | 2 a 4 números grandes com label e fonte do dado |
| `09-foto-full.html` | Foto sangrada de slide inteiro com faixa de legenda |
| `10-citacao.html` | Depoimento. Uma citação por slide |
| `11-comparativo.html` | Duas colunas lado a lado — antes/depois, com/sem |
| `12-timeline.html` | Trilho horizontal de 3 a 5 marcos |
| `13-tabela.html` | Planos, escopo, comparativo de números. Até 6 × 4 |
| `14-logos.html` | Grade de logos de clientes e parceiros |
| `15-encerramento.html` | Fecho: um pedido só, link do app, contatos |

---

## Como escolher o tipo

Escolhe-se pelo **formato da informação**, não pela vontade de variar:

| A informação é… | Slide |
|---|---|
| Uma frase que precisa pousar | `03-titulo-texto` |
| Três ou quatro coisas de peso igual | `05-cards-grid` |
| Uma lista de doze recursos | `06-features-2col` |
| Um produto que se vê na tela | `07-mockup-app` |
| Uma prova em número | `08-numeros` |
| Uma prova em pessoa | `10-citacao` |
| Uma escolha entre duas opções | `11-comparativo` |
| Uma sequência no tempo | `12-timeline` |
| Uma matriz de valores | `13-tabela` |
| Prova social | `14-logos` |

Dois slides seguidos do mesmo tipo são aceitáveis. **Cinco não** — se o deck inteiro é
`05-cards-grid`, o conteúdo está sendo espremido no layout errado.

## Caminhos de imagem

Todas as imagens do deck ficam em `saida/<slug>/assets/`, referenciadas relativamente:
`src="assets/nome.jpg"`. Nunca caminho absoluto da máquina, nunca `../`.

Os ativos fixos da marca — logo, imagem do fecho, ícones — **se copiam** de
`brand/assets/` para `assets/` do deck no momento da montagem. O deck precisa abrir
sozinho quando alguém mandar a pasta por e-mail.

Dimensões e proporção de cada slot: [`../tokens.md`](../tokens.md) → "Imagens".

## Espelhar o split

O `04-split-foto-cards` nasce com a foto à esquerda. Para inverter, é só acrescentar
`split--dir` no `<section>`:

```html
<section class="slide split split--dir">
```

A classe troca a ordem **e** o lado do arredondamento de uma vez. O raio vai sempre no lado
**de dentro** — o que encosta no conteúdo —, como no `07-mockup-app`. Alternar o lado entre
dois splits do mesmo deck evita que os dois slides pareçam o mesmo slide repetido.

## O logo

O logo da marca **não é imagem** nestes slides: ele é um `<symbol>` que o template
`templates/apresentacao/base.html` carrega **uma vez**, logo depois do `<body>`. Cada slide
que precisa dele faz:

```html
<svg class="logo" style="width:520px" viewBox="0 0 263 128" role="img" aria-label="Podi">
  <title>Podi</title><use href="#logo-marca"/></svg>
```

A cor vem do CSS, não do arquivo:

| Fundo | Classe |
|---|---|
| Cor de marca ou preto | `logo` — branco |
| Claro | `logo logo--marca` — o verde de marca `#48DB84`, em qualquer tamanho |

**O rodapé de todo slide é assinado pelo logo**, nunca pelo nome da marca escrito —
`.slide__foot` já dimensiona em 72px. Em fundo claro ele é a cor de marca, discreto de propósito.

Nunca trocar por um PNG, nunca aplicar `filter` para mudar a cor, e nunca colar o `<path>`
de novo dentro de um slide: existe uma cópia só, e é a do template. Fonte do desenho:
`brand/assets/header/logo-podi.svg`.

Tamanhos em uso: **520px** na capa, **360px** no encerramento, **280px** no mockup.

## Os ícones

Os `<svg>` dos chips são **marcadores de posição** com formas genéricas. Trocar pelo
glifo certo do assunto na hora da montagem, mantendo `fill="currentColor"` — é o
`currentColor` que faz o ícone herdar o roxo do chip. Nunca colar SVG com cor fixa dentro.
