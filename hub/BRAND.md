# Podi · regras da marca

O Podi é o app dos shoppings: ofertas, cupons, campanhas, eventos e o mapa do shopping no
bolso do cliente. Fala com o **consumidor** dos shoppings e com o **time** (endomarketing). A
Tacla Labs assina o Podi junto, no topo das peças.

Arquivos: https://marcas.taclalabs.workers.dev/podi/manifest.json

**A marca é masculina:** o Podi, do Podi, no Podi. Nunca "a Podi".

## Logo

- Uma forma só, publicada em três cores. Use sempre os arquivos do hub; nunca redesenhe,
  gere, recorte, distorça, contorne nem aplique sombra ou filtro. Não escreva "podi" em texto no
  lugar do logo.
- `podi-logo-branco`: sobre o verde de marca `#31D06E`, sobre o preto `#101010` e sobre foto, numa
  área calma, média ou escura.
- `podi-logo-verde`: sobre fundo branco ou claro, em qualquer tamanho — inclusive pequeno, no
  rodapé. É marca gráfica, não texto: o contraste baixo ali é aceito.
- `podi-logo-preto`: impressão a uma cor.
- **Assinatura conjunta com a Tacla Labs** (e-mail): logo do Podi à esquerda, Tacla Labs à
  direita, numa placa branca — o "Tacla" é preto e some em fundo escuro. Arquivos:
  `podi/email/logo-podi-transparente.png` e `podi/email/logo-tacla-labs.png`.

## Cor

| Papel | Cor | Regra |
|---|---|---|
| Marca | `#31D06E` | **Só fundo**: botão, tag, régua, slide. **Nunca cor de texto** (2,02:1 sobre branco) |
| Texto sobre o verde | `#101010` | **Nunca branco** sobre o verde |
| Tagline sobre o verde | `#074A21` | Só a frase de marca da capa do deck (5,2:1) |
| Link e destaque de marca sobre branco | `#0C6E3B` | 6,4:1 |
| Marca no modo escuro | `#6FE9A2` | Texto e link sobre `#1A1A1A` |
| Fundo de página | `#EDF7F1` | E-mail e slide claro |
| Tag, fundo de destaque | `#D4F0DF` | |
| Linha fina | `#D2E7DA` | |
| Texto | `#101010` títulos · `#4A4A4A` corpo · `#6E6E6E` legenda | |
| Roxo | `#9934FF` | **Só detalhe gráfico**: ícone, régua sob título, bullet, borda fina. Nunca texto, título, número, fundo grande nem nada em cima do verde |

- Nenhum texto abaixo de 4,5:1. Nenhuma cor fora desta tabela — nada de cor nova "para
  combinar".
- O roxo é tempero: no máximo 3 tipos de detalhe roxo por slide. O que se repete numa grade (o
  ícone de cada card, a régua de cada card) conta uma vez.

## Tipografia

- **DM Sans** (Google Fonts) em qualquer peça. Nenhuma outra família. Pesos com papel fixo:
  **600** nos títulos e rótulos, **400** no texto, **700** só no destaque dentro do texto e em
  números grandes. O e-mail usa só 400 e 600.
  `<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&display=swap" rel="stylesheet">`
- No e-mail, a pilha é `'DM Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif`.

## Ícones

- O sistema de ícones do Podi é o **HugeIcons Bulk Rounded**. Pack:
  `https://marcas.taclalabs.workers.dev/podi/icones/<nome>.svg`. A lista, com o uso de cada um,
  está em `podi/icones/index.json`: escolha pelo assunto e baixe só o que a peça usa.
- Cole os `<path>` do SVG dentro do `<svg>` da peça. Eles pintam com `fill="currentColor"`: a
  cor é o roxo `#9934FF`. Ícone solto, sem chip nem círculo, sempre ao lado de um rótulo.
- Sem ícone que sirva no pack, desenhe um novo na mesma estética:
  - `viewBox="0 0 24 24"`, área útil de 21px;
  - a silhueta inteira, cheia, com `opacity="0.4"`;
  - por cima, os detalhes cheios a 100%: traços de 1,5px desenhados como forma, pontas e cantos
    arredondados;
  - só `fill="currentColor"`: nada de cor gravada, `stroke`, gradiente ou sombra.
  Compare com dois ícones do pack antes de usar, e diga na entrega que o ícone é novo.

## Voz

| Frente | Público | Tom |
|---|---|---|
| Cliente | Consumidor dos shoppings, usuário do app | Direto, aspiracional, um pedido por bloco |
| Interno | O time do Podi | Próximo, celebratório, foco em pessoas |

- Português do Brasil, frases curtas. Diga o que a pessoa ganha e o que ela faz.
- Número só com fonte (briefing ou dado oficial). Sem superlativo que o número não sustenta.

## Links fixos

- **App:** `https://podi.podiapp.com.br/podi-e931a` — para "Baixar o app", "Baixe agora" e
  qualquer CTA de download. **Nunca `podi.com.br/app`**: esse endereço não existe.
- Rodapé legal: `© <ano> - Podi App` · Política de Privacidade
  `https://www.podiapp.com.br/politica-privacidade/` · Termos de Uso
  `https://www.podiapp.com.br/termos-de-uso.html`.
- Redes: Instagram `https://www.instagram.com/podibr` · Facebook
  `https://www.facebook.com/podibr` · LinkedIn `https://www.linkedin.com/company/podiapp` ·
  Spotify (no modelo de e-mail). No deck, a rede é `@podibr`.

## E-mail: variáveis de envio

O e-mail sai pelo servidor do Podi, que aceita **só três variáveis**: `{{email}}`,
`{{topicId}}` e `{{campaignId}}`. Qualquer outra `{{...}}` derruba o envio inteiro. Por isso
**nenhuma peça leva link de descadastro** — não existe variável para ele.

## O que fica só no repositório

- **E-mail com marca do empreendimento** (o remetente é o shopping, não o Podi): a cor do
  shopping entra no lugar do verde, com paleta calculada por script e conferida por contraste.
  Não monte pelo hub: use o repositório `podi-marketing-os` (`/newsletter-podi`).
- **Post de rede social:** os modelos de post do Podi ainda não foram carregados. Não monte
  post do Podi com modelo de deck nem de outra marca; avise o time de marca.
- **Referências fotográficas** (`refs/`): ficam no repositório. O hub tem o Style Lock no
  guia de foto.

## Fotografia

Toda foto de marca segue o Style Lock: luz natural de claraboia, câmera baixa, um único
accent verde em três valores, tela do celular sempre ilegível. Guia: `podi/guias/foto.md`.
Os blocos em inglês se copiam sem editar uma palavra.
