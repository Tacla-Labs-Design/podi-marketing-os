# Carrossel

Carrossel é uma sequência de posts do mesmo canvas que a pessoa arrasta. Serve para **uma
história em passos** — um problema e a solução, os módulos de uma plataforma, um passo a
passo, um case com números. Não serve para juntar posts soltos.

## Estrutura

```
01  capa      a promessa, em uma frase — é o único card que aparece no feed
02… miolo     um ponto por card, na ordem em que a história anda
NN  fecho     o pedido: um CTA só, com a marca
```

- **De 3 a 10 cards.** Menos de 3 é post único; mais de 10 o Instagram não aceita.
- A **capa** decide se a pessoa arrasta: título grande, sem parágrafo. Pode dizer que tem
  mais ("5 motivos…", "Como funciona →").
- **Um ponto por card no miolo.** Se o card precisa de dois parágrafos, são dois cards.
- O **fecho** repete a marca e leva o CTA da marca (`textos.cta_deck` e o site ou "link na bio").
- Mesmo modelo em cards seguidos é aceitável e até desejável no miolo (dá ritmo de lista).
  Capa e fecho se distinguem do miolo.
- Numerar o card (`2/6`) só quando a sequência importa — passo a passo, ranking.

## Continuidade

A pessoa vê o card seguinte espiando na borda. Grafismo de fundo que continua de um card para
o outro (o pattern, o símbolo, o degradê) ajuda a arrastar — mas o conteúdo nunca fica
cortado entre dois cards: cada PNG se lê sozinho.

## Legenda

Um carrossel tem **uma** legenda, que vale para todos os cards (`legenda.md`).
