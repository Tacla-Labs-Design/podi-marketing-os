# Briefing de demonstração

Uma pasta de briefing **fictícia**, pronta para você montar o seu primeiro e-mail sem
precisar esperar conteúdo real.

## Como usar

Peça ao Claude, em português:

> Copia o briefing de demonstração para o meu inbox e monta a newsletter

Ou faça o caminho completo você mesmo, que é o mesmo de um envio de verdade:

1. Copie esta pasta para `projects/_inbox/`, com o nome `2026-09-cliente-podi-news-demo`
2. Rode `/newsletter-podi 2026-09-cliente-podi-news-demo`
3. Veja o resultado em `saida/2026-09-cliente-podi-news-demo/index.html`

## O que tem aqui

```
brief.md      Os textos: cabeçalho do envio + 3 notícias numeradas
imagens/      Quatro imagens nos nomes e proporções certos
```

| Arquivo | Onde aparece | Proporção |
|---|---|---|
| `capa.jpg` | Abertura da edição | 1072 × 602 |
| `01-cinema.jpg` | Topo do bloco 01 | 1072 × 604 |
| `02-parque.jpg` | Topo do bloco 02 | 1072 × 604 |
| `03-clubinho-1x1.jpg` | Ao lado do texto do bloco 03 | 496 × 496 |

As imagens são **placas coloridas de teste**, não fotografia — existem para você ver o
encaixe e a proporção funcionando. Foto de marca de verdade segue
[`brand/podi/photography/STYLE-LOCK-PODI.md`](../../brand/podi/photography/STYLE-LOCK-PODI.md).

## Para reparar no resultado

- A edição é da frente **cliente**, então o rodapé sai com o motivo do recebimento em
  `{{email}}` — e **sem** link de descadastro, que o servidor de envio não suporta
- O bloco 03 usa imagem quadrada e ganha layout lateral, sem você pedir
- O bloco 01 tem CTA; os outros dois não — e o e-mail não fica torto por isso

Quer entender o formato para escrever o seu próprio briefing?
[`docs/como-enviar-conteudo.md`](../../docs/como-enviar-conteudo.md).
