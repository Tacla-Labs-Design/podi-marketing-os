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
- `podi-logo-branco`: sobre o verde de marca `#48DB84` e sobre o preto `#101010`.
- `podi-logo-verde`: sobre fundo branco ou claro, em qualquer tamanho — inclusive pequeno, no
  rodapé. É marca gráfica, não texto: o contraste baixo ali é aceito.
- `podi-logo-preto`: impressão a uma cor, e como assinatura pequena no rodapé de slide verde.
- **Assinatura conjunta com a Tacla Labs** (e-mail): logo do Podi à esquerda, Tacla Labs à
  direita, numa placa branca — o "Tacla" é preto e some em fundo escuro. Arquivos:
  `podi/email/logo-podi-transparente.png` e `podi/email/logo-tacla-labs.png`.

## Cor

| Papel | Cor | Regra |
|---|---|---|
| Marca | `#48DB84` | **Só fundo**: botão, tag, régua, slide. **Nunca cor de texto** (1,79:1 sobre branco) |
| Texto sobre o verde | `#101010` | **Nunca branco** sobre o verde |
| Link e destaque de marca sobre branco | `#0C6E3B` | 6,4:1 |
| Marca no modo escuro | `#6FE9A2` | Texto e link sobre `#1A1A1A` |
| Fundo de página | `#EDF7F1` | E-mail e slide claro |
| Tag, fundo de destaque | `#D4F0DF` | |
| Linha fina | `#D2E7DA` | |
| Texto | `#101010` títulos · `#4A4A4A` corpo · `#6E6E6E` legenda | |
| Roxo | `#9934FF` | **Só detalhe gráfico**: ícone, régua sob título, bullet, borda fina. Nunca texto, título, número, fundo grande nem nada em cima do verde |

- Nenhum texto abaixo de 4,5:1. Nenhuma cor fora desta tabela — nada de cor nova "para
  combinar".
- O roxo é tempero: no máximo 3 detalhes roxos por slide.

## Tipografia

- **Inter** (Google Fonts), dois pesos por peça: regular e semibold (e-mail) ou regular e
  bold (deck). Nenhuma outra família.
  `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">`
- No e-mail, a pilha é `'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif`.

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
