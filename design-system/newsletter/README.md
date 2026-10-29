# Design System — Newsletter

O sistema visual das newsletters e e-mails do Podi.

```
tokens.md        Cor, tipografia, espaçamento, dark mode, tamanhos de imagem
components/      Os 23 blocos de HTML de e-mail + o botão VML
guidelines/
  ├── email-compat.md   Regras técnicas de HTML de e-mail (não negociáveis)
  ├── layout-ritmo.md   Hierarquia, ritmo da peça, limites de CTA e de seções
  ├── variaveis-envio.md As variáveis que o servidor de envio aceita e por que não há descadastro
  ├── marca-empreendimento.md  Modo empreendimento: logo, cor e redes do shopping; sempre claro
  ├── qa-checklist.md   Checklist obrigatório antes de entregar
  └── refs/             Referências visuais de design (leitura humana)
```

## Autoridade

Este design system **obedece** ao [`brand/`](../../brand/README.md) e não pode contradizê-lo.
A regra de contraste da cor de marca nasce lá (o verde `#31D06E`: `brand/README.md`); aqui ela
só é aplicada.

## O que é específico de e-mail

Quase tudo em `guidelines/email-compat.md` e a tabela de tamanhos de imagem em `tokens.md`
existem por causa das limitações dos clientes de e-mail. Não servem para outro material.

**O que sobreviveria a outro suporte:** a paleta e a regra de contraste, os papéis
tipográficos (não os px de e-mail), a escala de espaçamento, o raio de 20px do card e o
princípio "cards brancos estruturam, fundo não se destaca".

Quando surgir um segundo tipo de material, nasce `design-system/<material>/` e o que for
comum sobe para `brand/`. **Essa promoção não se faz por antecipação** — só com um segundo
caso de uso real que a confirme.

## Alterar isto

Só maintainer. Ver [`docs/governanca.md`](../../docs/governanca.md).
