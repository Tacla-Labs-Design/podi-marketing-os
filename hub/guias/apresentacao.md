# Podi · apresentação 16:9

Deck para shopping, parceiro ou time. Canvas fixo de 1920 × 1080; sai em PDF, uma página por
slide, a partir do HTML.

## Briefing

Obrigatório: para quem (shopping, parceiro ou time), quanto tempo, e o pedido do fim (o que a
plateia deve fazer depois).

Padrão se faltar:
- Tempo: 10 minutos, uns 8 slides. Teto de 20 slides em qualquer caso.
- Pedido: "Baixar o app Podi" (é o botão fixo do encerramento).

Antes de montar, escreva o roteiro — número, tipo de slide, o que ele diz em uma frase — e
confirme com quem pediu.

## Modelo

`podi/modelos/apresentacao-16x9.html`. Copie a `<section>` de cada tipo na ordem do roteiro e
troque só os `data-slot`. Não crie layout novo.

| Tipo | Quando usar | Limites |
|---|---|---|
| capa | primeiro slide, sempre | tagline, ripple, mão e telas fixos: não troque nada |
| título + texto | uma frase que precisa pousar | título até 60 · texto até ~60 palavras |
| foto + cards | 4 valores ou benefícios com uma foto | card: título até 14, texto até 90 · foto com área calma para o logo |
| cards | 3 ou 4 coisas de peso igual | título até 50 · card: título até 20, texto até 90 |
| plataforma | o produto, com até 12 recursos | frase até 110 · parágrafo até 160 · recurso até 34 |
| divisor | virada de assunto, a cada 4 a 6 slides | nome até 40 · apoio até 90 |
| números | 2 a 4 provas em número | número até 8 caracteres · legenda até 40 · fonte obrigatória |
| linha do tempo | 3 a 5 marcos em sequência | quando até 16 · texto até 80 |
| encerramento | último slide, sempre | o pedido em uma frase, até 60 caracteres |

- **Uma ideia por slide**, ~60 palavras no máximo. O que não cabe vira outro slide — nunca
  fonte menor, nunca margem menor que 64 px.
- Nunca dois slides de cards seguidos. Alterne o fundo: verde, claro, o divisor preto.
- Texto sobre o verde é `#101010`, **nunca branco**. O verde nunca é cor de texto.
- O roxo `#9934FF` é só detalhe (ícone, régua, borda da caixa, ponto da linha do tempo): no
  máximo 3 tipos por slide, nunca texto, nunca sobre o verde.
- Logo pelo hub: `podi-logo-branco` sobre o verde, o preto e foto; `podi-logo-verde` sobre claro.
  Nunca PNG esticado, nunca filtro.
- Ícones: troque os de exemplo pelo do assunto, do pack `podi/icones/` (lista em
  `podi/icones/index.json`). Cole os `<path>` dentro do `<svg class="ico">` do slide. Sem ícone
  que sirva, desenhe um na mesma estética (`podi/BRAND.md` → Ícones).
- Número só com fonte, que vai na legenda do slide.
- DM Sans: semibold nos títulos, regular no texto, bold só no destaque. Nenhuma outra fonte.
- Foto de marca nova: ver `podi/guias/foto.md`.

## Gerar o PDF

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --no-pdf-header-footer \
  --virtual-time-budget=8000 --print-to-pdf="apresentacao.pdf" "file://$PWD/apresentacao.html"
```

No Windows, o Chrome fica em `C:\Program Files\Google\Chrome\Application\chrome.exe`. O
modelo já define a página de 1920 × 1080; confira se saiu uma página por slide.

## Conferência

- [ ] Capa primeiro, encerramento por último.
- [ ] Nenhum texto entre colchetes sobrou; nada passa da margem nem fica cortado.
- [ ] Nenhum texto branco sobre o verde; nenhum texto em `#31D06E` ou em roxo.
- [ ] No máximo 3 tipos de detalhe roxo por slide; ícones do pack Bulk ou desenhados na mesma estética.
- [ ] Botão do encerramento com `https://podi.podiapp.com.br/podi-e931a`.
- [ ] Todo número com fonte; sempre "o Podi".
- [ ] PDF em paisagem, uma página por slide.
