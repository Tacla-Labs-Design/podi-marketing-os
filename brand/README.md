# Brand — Podi

Camada mais alta do Marketing OS. **Nada abaixo pode contradizer esta pasta.**

Se um pedido conflita com o que está aqui, a IA sinaliza o conflito em vez de alterar
a identidade. Ver `docs/governanca.md`.

| Arquivo | O que guarda |
|---|---|
| `README.md` | Este: voz, logo, cor de marca, roxo de detalhe, tipografia, ícones, frentes, empreendimento |
| [`links-oficiais.md`](links-oficiais.md) | Link do app, rodapé legal, redes, textos fixos do deck |
| [`marca.json`](marca.json) | Os mesmos valores, para máquina — lido por `scripts/conferir.py` e pelas skills |
| `assets/` | Logos (SVG e PNG para e-mail), ícones sociais, o pack de ícones Bulk (`icones-bulk/`), ativos fixos do deck (`deck/`) |
| [`photography/`](photography/README.md) | Style Lock — a direção fotográfica |

---

## Marca

**Podi** — app e comunicação dos shoppings. Assinatura conjunta com **Tacla Labs** no
topo de toda peça (logo Podi à esquerda, Tacla Labs à direita). A única exceção são as
[peças com marca do empreendimento](#peças-com-marca-do-empreendimento).

**A marca é masculina.** Escreva sempre **o Podi**, **do Podi**, **no Podi**, **pelo Podi**.
Nunca "a Podi", "da Podi", "na Podi". Vale em qualquer material — newsletter, apresentação,
copy de campanha — e na conversa com o time.

Logos oficiais em `brand/assets/header/`. Na **assinatura conjunta**, sempre a versão light
mode (arte escura sobre fundo claro): o "Tacla" do logo é preto, então em fundo escuro a
assinatura vai dentro de uma placa branca — nunca se troca o arquivo por CSS.

O logo Podi **sozinho** tem uma versão vetorial monocromática: `logo-podi.svg`. Ela é uma
forma só, sem cor gravada — a cor vem de fora, por `currentColor`. É o arquivo a usar
sempre que o logo aparecer sem a Tacla Labs:

| Fundo | Cor do logo |
|---|---|
| Verde de marca `#31D06E` | Branco `#FFFFFF` |
| Preto `#101010` | Branco `#FFFFFF` |
| Foto, numa área calma, média ou escura | Branco `#FFFFFF` |
| Branco ou claro | Verde de marca `#31D06E` |

Sobre fundo claro é **sempre o verde original `#31D06E`**, em qualquer tamanho — inclusive
na assinatura pequena do rodapé. Ele dá 1,85:1 ali, e é uma marca discreta de propósito:
como o ícone social verde do rodapé do e-mail, é ornamento, não alvo de leitura. O que
identifica a peça é a forma do logo, não o contraste dele.

**Logo não é texto.** A regra de contraste do verde governa palavras; o logo é uma marca
gráfica, e branco sobre o verde é como o Podi assina desde sempre. O que continua proibido
é **recolorir por filtro ou por efeito** — trocar a cor é trocar o `color` do SVG, e ponto.

## Cor de marca — e a regra que ela impõe

**`#31D06E`** (verde Podi). Contraste sobre branco: **2,02:1** — reprova em qualquer texto.

| Situação | Cor certa | Contraste |
|---|---|---|
| Texto **em cima** do verde | `#101010` | 9,4:1 — texto branco sobre o verde é **proibido** |
| Tagline e frase de marca **em cima** do verde | `#074A21` | 5,2:1 — o verde-escuro da capa do deck |
| Texto/link de marca **sobre branco** | `#0C6E3B` | 6,4:1 |
| Texto/link de marca no **dark mode** | `#6FE9A2` | 11,5:1 sobre `#1A1A1A` |

O `#31D06E` só entra como **fundo** — botão, tag, régua de destaque. **Nunca como cor
de texto.** Esta regra não é negociável em nenhum material, de e-mail a impresso.

**Nenhum texto abaixo de 4,5:1**, em qualquer material. **Nunca escreva cor solta:** toda cor
sai dos tokens do material (`design-system/<material>/tokens.md`).

Paleta completa e tokens derivados: `design-system/newsletter/tokens.md` (e-mail) e
`design-system/apresentacao/tokens.md` (apresentação). Os mesmos valores, para máquina:
[`marca.json`](marca.json).

## Cor secundária — roxo de detalhe

**`#9934FF`** (roxo Tacla Labs). Entra como **detalhe gráfico**, nunca como conteúdo.

| Onde pode | Onde não pode |
|---|---|
| Ícone Bulk solto, em fundo branco ou claro | Texto corrido |
| Régua ou gradiente fino sob um título | Título, subtítulo, número de destaque |
| Bullet de lista, ponto de linha do tempo | Fundo de área grande — esse papel é do verde |
| Borda fina de container | Qualquer coisa **em cima do verde** (2,4:1) |

Contraste sobre branco: **4,9:1** — passaria em texto. A regra é mais restritiva de
propósito: **o verde é a marca, o roxo é tempero.** Se o roxo virar cor de texto, a peça
deixa de parecer Podi em duas ou três seções.

Como o ícone social verde, **um detalhe roxo nunca carrega informação sozinho**: ele
acompanha um rótulo, não substitui um.

Tokens derivados e as versões claras do roxo: `design-system/apresentacao/tokens.md`.

## Tipografia

**DM Sans** (Google Fonts), em qualquer material — e-mail, deck, post, impresso. Nenhuma
outra família. É a fonte do app e dos decks que o time já usa.

| Peso | Papel |
|---|---|
| 400 Regular | Texto corrido, legenda, tagline |
| 600 SemiBold | Títulos, rótulos, botões |
| 700 Bold | Só destaque dentro do texto (`<strong>`) e números grandes |

O material pode usar menos pesos, nunca outros. Pilha em HTML:
`'DM Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif`.

## Ícones

O sistema de ícones do Podi é o **HugeIcons Bulk Rounded** (licença Pro da Tacla Labs). O pack
oficial fica em [`assets/icones-bulk/`](assets/icones-bulk/), com `index.json` dizendo o uso de
cada ícone, e vai ao hub de marcas em `podi/icones/`.

- Cada ícone tem **duas camadas da mesma cor**: a forma de fundo a 40% de opacidade e os detalhes
  a 100%. A cor vem de quem usa, por `currentColor` — no Podi, o roxo `#9934FF`.
- O ícone vai **solto**, sem chip ou círculo de fundo, sempre ao lado de um rótulo.
- Tamanhos no deck: **80px** no alto de card, **32px** em lista.

**Quando o pack não tem o ícone do assunto**, desenhe um novo na mesma estética, e só nesse caso:

1. `viewBox="0 0 24 24"`, área útil de 21px (1,5px de respiro em volta).
2. A silhueta inteira do objeto, cheia, com `opacity="0.4"`.
3. Por cima, os detalhes cheios a 100%: traços de 1,5px desenhados como forma, pontas e cantos
   arredondados (raio de 1,5 a 3px). Nada de `stroke` solto, nada de ponta reta.
4. Só `fill="currentColor"`. Nenhuma cor gravada, nenhum gradiente, nenhuma sombra.
5. Compare lado a lado com dois ícones do pack antes de usar. Ícone novo é da peça: para entrar
   no pack, passa pelo maintainer (`scripts/icones.py`).

## As duas frentes

Mesma marca, mesma paleta. O que muda é público, tom e obrigação legal.

| | Cliente final | Endomarketing |
|---|---|---|
| Público | Consumidor dos shoppings, usuário do app | Colaboradores Podi |
| Objetivo | Promoções, eventos, novidades do app, aniversariantes | Cases de uso, resultados, bastidores |
| Tom | Direto, aspiracional, 1 CTA por bloco | Próximo, celebratório, foco em pessoas |
| Rodapé | Completo: `© <ano> - Podi App`, motivo do recebimento, privacidade e termos | Contato de comunicação interna / RH |

**Nenhuma das duas leva link de descadastro.** O servidor de envio não suporta a variável,
e variável não suportada derruba a campanha inteira. A saída do descadastro é tratada fora
do HTML, por quem opera o envio. As únicas variáveis permitidas em e-mail são `{{email}}`,
`{{topicId}}` e `{{campaignId}}` — regra completa em
[`design-system/newsletter/guidelines/variaveis-envio.md`](../design-system/newsletter/guidelines/variaveis-envio.md).

## Peças com marca do empreendimento

Há peças em que **o remetente é o empreendimento** — o shopping, o outlet, ou uma campanha
dele — e o Podi é a plataforma por trás. Nelas a identidade visual da frente é a do
empreendimento, e isso **não é conflito de marca**.

**Quando é permitido:** só quando o briefing diz que o remetente é o empreendimento. Peça
assinada pelo Podi, mesmo falando de um shopping, continua sendo Podi.

**O que sai, e só nesse caso:**

- o verde Podi e seus derivados — dão lugar à cor base da campanha, com a paleta derivada
  por conta fixa;
- o header Podi + Tacla Labs — dá lugar ao logo do empreendimento;
- as redes e os ícones verdes do Podi — dão lugar às redes do empreendimento, com os ícones
  recoloridos;
- o roxo de detalhe `#9934FF` — é cor da Tacla Labs e não entra na peça do empreendimento.

Fora desse caso, o verde Podi não sai de peça nenhuma.

**O que continua sendo Podi:**

- o rodapé legal com `© <ano> - Podi App`, Política de Privacidade e Termos de Uso;
- o link do app, `https://podi.podiapp.com.br/podi-e931a`;
- as regras de texto — "o Podi" no masculino, sem link de descadastro, as variáveis de envio;
- a regra de contraste: nenhum texto abaixo de 4,5:1. O texto do botão é branco ou `#101010`
  conforme o contraste medido sobre a cor base.

Hoje o modo existe para e-mail. Regra completa, algoritmo da paleta e limitações:
[`design-system/newsletter/guidelines/marca-empreendimento.md`](../design-system/newsletter/guidelines/marca-empreendimento.md).

## Fotografia

Direção fotográfica oficial: [`photography/STYLE-LOCK-PODI.md`](photography/STYLE-LOCK-PODI.md).
Vale para qualquer foto de marca, em qualquer material. O bloco `STYLE LOCK` se copia sem
editar uma palavra — é ele que faz as imagens parecerem do mesmo ensaio.

Lá o verde é figurino e objeto dentro da foto, não texto: a regra de contraste acima
continua valendo integralmente.

## Ativos e links fixos

Ver [`links-oficiais.md`](links-oficiais.md). Não se inventa URL, não se cria arte nova para o que já tem.

## Mudança de paleta

É trabalho do maintainer, nunca de campanha: mudar a paleta do Podi é mudar os tokens, os
componentes, os slides e o [`marca.json`](marca.json) na mesma leva, com entrada no
`CHANGELOG.md`. Depois, conferir os contrastes obrigatórios:

```bash
python3 -I scripts/conferir.py --marca
```
