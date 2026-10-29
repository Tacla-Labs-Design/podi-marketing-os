# Design System — Apresentação

O sistema visual dos decks e apresentações do Podi. Canvas fixo **16:9, 1920 × 1080**.

```
tokens.md        Cor, cor secundária, tipografia de projeção, espaçamento, imagens
slides/          Os 16 tipos de slide + o shell `_slide.html`
  └── README.md  Catálogo, como escolher o tipo, caminhos de imagem
guidelines/
  ├── canvas-16-9.md   O canvas fixo, a escala de tela, o export em PDF
  ├── uso-do-roxo.md    Onde o `#9934FF` pode e não pode entrar
  ├── layout-ritmo.md   Hierarquia dentro do slide e ritmo do deck
  └── qa-checklist.md   Checklist obrigatório antes de entregar
```

## Autoridade

Este design system **obedece** ao [`brand/`](../../brand/README.md) e não pode contradizê-lo.
A regra da cor de marca e a da secundária de detalhe nascem lá (o verde `#31D06E` e o roxo
`#9934FF`); aqui elas só são aplicadas a um canvas de 1920 × 1080.

Shell de montagem: `templates/apresentacao/base.html`. Procedimento: `/apresentacao-podi`.

## O que é específico de apresentação

- **O canvas é fixo.** Um slide tem exatamente 1920 × 1080 px. Não existe "rolar a página",
  não existe mobile: o que não cabe vira outro slide.
- **A tipografia é de projeção**, não de leitura de perto. O texto começa em 24px porque a
  pessoa está a metros da tela — os 16px do e-mail seriam ilegíveis.
- **O verde é o fundo do slide**, não a cor do botão. No e-mail o `page` é o `#EDF7F1`
  discreto; aqui o `#31D06E` é campo de cor inteiro, e os cards brancos flutuam sobre ele.
- **Pode usar CSS moderno.** Flex, grid, `var()`, gradiente — nada disso passa em cliente de
  e-mail, e tudo isso passa num navegador. As restrições de
  `design-system/newsletter/guidelines/email-compat.md` **não valem aqui**.

**O que sobreviveria a outro suporte:** a paleta e as duas regras de contraste, os papéis
tipográficos (não os px), o princípio "cards brancos estruturam, o fundo é campo de cor",
e o roxo como detalhe que nunca carrega informação sozinho.

## Alterar isto

Só maintainer. Ver [`docs/governanca.md`](../../docs/governanca.md).
