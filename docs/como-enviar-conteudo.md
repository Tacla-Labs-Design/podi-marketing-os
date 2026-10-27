# Como enviar o conteúdo para o Claude montar a newsletter

Guia para quem escreve a newsletter. Não precisa saber HTML.

Você entrega **duas coisas**: um documento com os textos e uma pasta com as imagens.
O Claude cuida do resto — layout, cores, dark mode, versão mobile, QA.

---

## 1. Crie a pasta do envio

Dentro de `projects/_inbox/`, crie uma pasta com este nome:

```
AAAA-MM-<frente>-<assunto>
```

- **frente** é `cliente` (consumidor dos shoppings) ou `interno` (colaboradores)
- exemplos: `2026-09-cliente-podi-news`, `2026-09-interno-case-shopping-norte`

A frente não é detalhe: ela decide o tom e o texto do rodapé — o motivo do recebimento e o
contato mudam entre cliente final e interno. **Link de descadastro nenhuma das duas leva:**
o servidor de envio não suporta essa variável.

Dentro dela:

```
2026-09-cliente-podi-news/
├── brief.docx          ← os textos (pode ser .md, .txt ou .pdf também)
└── imagens/            ← as fotos (ou um imagens.zip, o Claude descompacta)
```

---

## 2. Escreva o documento

Não precisa formatar bonito. O que o Claude precisa achar:

**No começo, o cabeçalho do envio:**

```
Frente: cliente
Data de envio: 15/09/2026
Objetivo: divulgar os eventos de setembro nos shoppings
Chamada da edição: Setembro chegou com novidades
Texto de apoio: Veja o que preparamos para você neste mês.
```

**Depois, uma notícia por bloco, numerada na ordem em que deve aparecer:**

```
## 01 — Cinema exclusivo
Tag: Experiência
Subtítulo: Estreia de Moana Live Action · 100 convidados
Texto: Julho teve sessão exclusiva para a estreia de Moana Live Action,
reunindo jornalistas, parceiros e os melhores usuários do app.

## 02 — Parque da Cidade
Tag: Cidade Sorocaba
Subtítulo: Inauguração em 9 de julho
Texto: A abertura reuniu as famílias numa tarde de diversão e lazer.
```

O número (`01`, `02`…) é o que amarra o texto à imagem. É a parte que não pode faltar.

**Se houver botão**, diga o rótulo e o link:

```
CTA: Ver a programação → https://exemplo.com.br/programacao
```

Para o botão de baixar o app não precisa mandar link — ele já é fixo no projeto.

---

## 3. Nomeie as imagens

Este é o ponto que mais economiza retrabalho. O nome do arquivo diz ao Claude **de qual
notícia é a imagem** e **como ela vai ser usada**.

```
NN-nome-curto.jpg          → imagem no topo do bloco, ocupando a largura inteira
NN-nome-curto-1x1.jpg      → imagem ao lado do texto (esquerda ou direita)
capa.jpg                   → a imagem grande da abertura da edição
```

O `NN` é o mesmo número da notícia no documento. O `nome-curto` é só para você se achar —
o Claude usa o número.

Exemplo de uma pasta completa:

```
imagens/
├── capa.jpg                    → abertura da edição
├── 01-cinema.jpg               → notícia 01, imagem no topo
├── 02-parque-cidade.jpg        → notícia 02, imagem no topo
├── 03-panna-city-1x1.jpg       → notícia 03, imagem lateral
└── 04-clubinho-1x1.jpg         → notícia 04, imagem lateral
```

Se um bloco não tiver imagem, é só não mandar — o Claude usa um layout só de texto.

### As duas proporções

Não é preferência de estilo: e-mail **não recorta imagem**. O arquivo entra com a forma
que tem. Fora da proporção, ele distorce ou estoura a coluna.

| Sufixo | Onde aparece | Proporção | Tamanho mínimo |
|---|---|---|---|
| *(sem sufixo)* | Topo do bloco, largura inteira | **16:9 ou mais panorâmica** | 1072 × 604 |
| `-1x1` | Ao lado do texto | **1:1 exata** (quadrada) | 496 × 496 |
| `capa` | Abertura da edição | **16:9 ou mais panorâmica** | 1072 × 602 |

Os tamanhos são o dobro do que aparece na tela — é o que mantém a imagem nítida em
celular moderno. Menor que isso, borra.

**Sobre o 1:1:** se a foto original é vertical (print de celular, foto em pé), recorte
num quadrado **antes** de mandar. Você escolhendo o recorte sai melhor do que qualquer
corte automático.

### Formato

**JPG ou PNG.** Não mande WebP, AVIF, HEIC nem SVG — Outlook e Gmail não abrem, e o
leitor vê um quadrado vazio. Se saiu do iPhone em HEIC, exporte como JPG antes.

---

## E-mail com a marca do empreendimento

Quando **quem assina o e-mail é o shopping ou o outlet** — uma campanha dele, com o logo e as
cores dele —, o e-mail sai com a marca do empreendimento no lugar da do Podi. O rodapé legal
continua sendo do Podi.

Diga isso logo no começo do documento:

```
Remetente: City Center Outlet Premium
Disparo: pelo sistema da campanha        ← ou: pelo Podi
```

E mande, além dos textos:

| O quê | Como |
|---|---|
| **Logo** | PNG **colorido, para fundo claro**, com fundo transparente. No mínimo 300 px de largura |
| **Cor da campanha** | O código da cor, como `#173B2A`. Peça para o designer do empreendimento |
| **Redes sociais** | O link de cada rede do empreendimento (Instagram, Facebook, LinkedIn) |
| **Texto legal** | O regulamento curto da promoção, do jeito que o jurídico aprovou |
| **Imagem da campanha** | A arte de abertura, horizontal, no mínimo 1072 px de largura |
| **Imagens de produto ou benefício** | **Quadradas**, no mínimo 448 × 448 |

**Não precisa decidir** cabeçalho, rodapé nem cores de fundo: isso já vem pronto no padrão.
O Claude testa se a cor da campanha dá leitura no e-mail. Se não der, ele avisa e pede
outra — não é implicância, é o texto ficar ilegível.

**Campos como `{{nome}}` ou `{{economia_total}}`:** escreva exatamente como o sistema da
campanha espera e diga por onde o e-mail vai sair. Esses campos só funcionam quando o disparo
**não** é pelo Podi — pelo servidor do Podi, eles derrubam o envio inteiro. Se o documento
não disser, o Claude pergunta antes de montar.

**Link de descadastro não entra**, como em qualquer e-mail do padrão.

**Sempre em modo claro.** Esse e-mail não tem versão escura. A maioria dos leitores respeita
isso; o app do Gmail e algumas versões do Outlook podem escurecer por conta própria.

---

## Post ou carrossel

**Os modelos de post do Podi ainda não foram carregados no padrão.** Até chegarem, o
`/post-podi` avisa e não monta — e não monta com modelo de outra marca nem com layout
improvisado. Quando os modelos chegarem, o briefing segue a mesma lógica do e-mail: uma pasta
em `projects/_inbox/`, um bloco numerado por card, uma ideia por card; o texto longo vai para
a legenda, que o Claude escreve.

---

## 4. Peça a geração

Abra o Claude Code na pasta do projeto e escreva:

```
/newsletter-podi 2026-09-cliente-podi-news
```

Ou, em português mesmo:

> Gera a newsletter de projects/_inbox/2026-09-cliente-podi-news

---

> Antes de montar, o Claude atualiza sozinho o padrão para a versão mais recente — você
> não precisa fazer nada. Se ele avisar que não conseguiu, é só falar com quem cuida do
> padrão. O que mudou em cada versão fica no [CHANGELOG.md](../CHANGELOG.md).

## 5. O que você recebe de volta

- O arquivo montado em `saida/<slug>/index.html` — pasta local, não vai para o Git
- **Subject line** (até 45 caracteres) e **preheader** (60 a 90)
- A lista de imagens para hospedar, com o tamanho final de cada uma
- O que ficou de fora do briefing e por quê

---

## Erros que aparecem toda semana

**Imagem sem número.** `foto-legal.jpg` não diz a que notícia pertence. O Claude vai
perguntar em vez de adivinhar — e você perde uma rodada.

**Vertical marcada como `-1x1`.** Um print de celular 9:16 salvo como `03-app-1x1.jpg`
não vira quadrado sozinho. Recorte antes.

**Imagem pequena.** Uma foto de 600px de largura numa faixa que precisa de 1072 fica
borrada em qualquer celular recente.

**Texto importante dentro da imagem.** Preço, data, título de manchete: a maioria dos
clientes de e-mail bloqueia imagem por padrão, e quem abre vê um retângulo cinza. Esse
tipo de informação tem que estar no documento, como texto.

**Mais de 4 blocos de conteúdo.** Acima disso o e-mail cansa e a taxa de clique cai.
Se o mês rendeu muito, o caminho é dividir em dois envios.
