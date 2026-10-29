# Layout e ritmo do deck

## O princípio

**Uma ideia por slide.** Se o slide precisa de duas frases para explicar do que ele trata,
são dois slides. Deck bom não é deck curto — é deck onde cada slide tem um trabalho só.

Quem lê está a metros da tela e tem 30 segundos por slide. Tudo aqui existe por causa disso.

## Hierarquia dentro de um slide

```
eyebrow          o assunto, 20px uppercase       (opcional)
    ↓
título           a ideia, 64px semibold          (obrigatório, exceto capa e foto full)
    ↓
régua roxa       200 × 4px, some para a direita  (a pausa antes do conteúdo)
    ↓
conteúdo         cards, números, lista, foto
    ↓
rodapé           fonte do dado · número do slide
```

A régua roxa não é enfeite: ela é o intervalo que separa o título do conteúdo sem gastar
mais 40px de espaço vertical.

## Ritmo do deck

- **Capa → agenda → seções → encerramento.** Um divisor de seção a cada 4 a 6 slides.
- **Alternar o campo de cor.** Verde, verde, verde cansa. `slide--light` e `slide--white`
  existem para dar respiro; o divisor preto marca a virada.
- **Uma foto a cada 5 slides**, no mínimo. Deck sem foto vira relatório.
- **Nunca dois `05-cards-grid` seguidos.** Repetir o mesmo layout duas vezes seguidas faz a
  plateia achar que voltou o slide.

## Limites

| | Limite | Por quê |
|---|---|---|
| Slides no deck | 20 | Acima disso ninguém termina a apresentação |
| Palavras num slide | ~60 | Slide não é documento |
| Cards numa grade | 4 | O quinto card encolhe o texto abaixo do piso de 24px |
| Números num slide | 4 | Mais que isso e nenhum é lembrado |
| Itens numa lista | 12 | É o que cabe em duas colunas sem apertar |
| Linhas numa tabela | 6 | Tabela maior não se lê projetada |
| Tipos de detalhe roxo num slide | 3 | Repetição numa grade conta uma vez. Ver [`uso-do-roxo.md`](uso-do-roxo.md) |

Estourou um limite: o conteúdo vira dois slides. Nunca fonte menor, nunca margem menor.

## O verde é fundo, o branco é estrutura

Mesmo princípio da newsletter: o campo de cor não organiza nada sozinho. **Quem constrói a
hierarquia visual são os cards brancos** flutuando sobre o verde. Um slide verde com texto
solto em cima parece um aviso; um slide verde com cards parece o produto.

Exceções legítimas: capa, divisor de seção e encerramento — os três slides que existem
para respirar, não para informar.

## De onde isto veio

Este design system foi escrito a partir de três slides que o time de marketing usa nas
apresentações — a capa com o app na mão, o split foto + cards de valores e o slide da
plataforma com a lista de recursos (arquivo **[DECK] Simple Deck - Podi**, no Figma). Eles são o
`00-capa`, o `04-split-foto-cards` e o `07-mockup-app`, medida por medida; o `05` e o `06`
herdam o card e a caixa de recursos deles. O padrão **descreve o que já existia**; não inventou
direção nova. Se o Figma mudar, o DS muda junto.
