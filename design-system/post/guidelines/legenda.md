# Legenda

Todo post sai com a legenda pronta em `saida/<slug>/legenda.txt` — o texto que vai no campo
de legenda do Instagram e do LinkedIn. A arte chama; a legenda explica.

## Estrutura

```
linha 1   o gancho — é o que aparece antes do "mais". Até ~125 caracteres
          (corpo)  2 a 5 frases curtas, uma ideia por parágrafo
          CTA      um só, o do Podi
          hashtags (Instagram) no fim, separadas por uma linha em branco
```

- **A primeira linha se lê sozinha.** Não começa com "Você sabia", nem com emoji, nem com o
  nome da marca.
- **Um CTA.** O do Podi (`brand/links-oficiais.md`). Instagram não tem link clicável
  na legenda: "link na bio" ou o site escrito. LinkedIn aceita a URL.
- **Número só com fonte** — o briefing ou a documentação oficial do Podi. Número sem origem
  não entra.
- **Emoji:** no máximo um por parágrafo, nunca no lugar de palavra. Na frente `interno`, de
  preferência nenhum.
- **Hashtags:** de 3 a 5, específicas do assunto. Nada de hashtag genérica (#marketing,
  #sucesso). No LinkedIn, no máximo 3.
- Menção a cliente (@ de shopping) só com autorização dita no briefing.

## Formato do arquivo

```
INSTAGRAM
<legenda completa>

LINKEDIN
<legenda completa, adaptada: URL no lugar de "link na bio", até 3 hashtags>

ALT
01: <descrição do card 1 para acessibilidade>
02: …
```

O texto alternativo (ALT) de cada card vai para o campo de "texto alternativo" da rede: diz o
que a imagem mostra e o texto que está nela, em uma ou duas frases.
