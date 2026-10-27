# Canvas 16:9 — regras técnicas

## O canvas é fixo

Um slide tem **exatamente 1920 × 1080 px**. Não é um site: não rola, não quebra, não tem
versão mobile. O que não cabe em 1080px de altura **vira outro slide** — nunca fonte menor,
nunca margem apertada.

- Todo slide é um `<section class="slide">` com `overflow:hidden`.
- **Margem de segurança de 96px** em todos os lados (`.slide__pad`). Projetor e TV cortam
  borda; conteúdo colado no canto some na sala.
- A única exceção à margem: imagem sangrada, que é sangria de propósito
  (`04-split-foto-cards`, `07-mockup-app`, `09-foto-full`).

## Pode usar CSS moderno

As regras de `design-system/newsletter/guidelines/email-compat.md` **não valem aqui**.
Isto abre num navegador, não no Outlook. São permitidos e recomendados:

- `display:flex` e `display:grid`
- `var(--token)` — e é obrigatório: cor solta é proibida
- gradiente, `border-radius`, `box-shadow`, `object-fit`, `filter`
- SVG inline

O que continua proibido:

- **Cor escrita direto** fora do `:root` do template. Toda cor sai de `../tokens.md`.
- **Fonte que não seja a da marca**: Inter do Google Fonts no Podi; Halyard Text, instalada
  na máquina (Adobe Fonts), no Optimall.
- `<script>` que mude conteúdo. O único JS do template é o que escala o canvas na tela.
- Imagem carregada de URL externa. Tudo em `assets/` da própria pasta.

## Preview na tela

O template escala o deck por `transform:scale()` para caber na janela. É só preview: os
números do CSS continuam sendo os de 1920 × 1080, e é neles que se pensa ao montar.

```bash
open saida/<slug>/index.html
```

## Export em PDF

O caminho padrão é o script, que usa o Chrome da máquina, confere antes se a fonte da marca
está instalada e confere depois se saiu uma página por slide:

```bash
python3 scripts/exportar.py pdf saida/<slug>/index.html     # → saida/<slug>/<slug>.pdf
```

À mão, pelo navegador, também funciona:

1. Cmd+P no navegador
2. **Paisagem**, margens **nenhuma**, "Imprimir fundos" **ligado**
3. Salvar como PDF

Sai um slide por página, no tamanho exato. O `@page{size:1920px 1080px;margin:0}` do
template é o que garante isso — se alguém tirar essa regra, o PDF sai com margem branca e
os fundos cortados.

**Conferir o PDF antes de entregar.** Fundo que não imprimiu e slide cortado só aparecem
aqui, nunca no navegador.

## PowerPoint

O padrão não gera `.pptx`. Quem precisar levar para o PowerPoint importa o PDF como
imagem de fundo — a tipografia fica travada e correta, e nenhuma fonte é substituída na
máquina de outra pessoa. Deck que precisa ser editado no PowerPoint depois é um pedido
diferente: falar com quem cuida do padrão.
