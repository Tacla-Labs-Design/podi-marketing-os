# QA — rodar antes de entregar qualquer e-mail

## Estrutura
- [ ] `<!DOCTYPE>` XHTML Transitional com `xmlns:v` e `xmlns:o`
- [ ] Bloco `<!--[if mso]>` com `PixelsPerInch` 96 e o override de `font-family: Arial !important`
- [ ] Preheader oculto é o primeiro elemento do `<body>`, com 60–90 caracteres
- [ ] Nenhum `<div>` fazendo papel de layout; só tabelas com `role="presentation"`
- [ ] Container 600px com ghost table MSO em volta
- [ ] Nenhum `margin` em elemento de layout (só em `<p>`/`<h*>` como reset)

## CSS
- [ ] Todo estilo visual está inline; o `<style>` só tem reset, media query e dark mode
- [ ] Zero `var()`, `calc()`, `flex`, `grid`, `position`, `float`, `rem`
- [ ] Nenhum texto abaixo de 15px (exceto legal 12px, eyebrow 12px e label de número 14px)
- [ ] Todo `<td>` com texto declara `font-family`, `font-size`, `line-height` e `color`

## Imagens
- [ ] Todas com `alt` descritivo, atributo `width` e `display:block;border:0`
- [ ] Todas em JPG/PNG (nada de WebP/SVG/AVIF) e exportadas em 2x
- [ ] URLs absolutas `https://`
- [ ] Teste com imagens bloqueadas: o e-mail continua compreensível e o CTA continua clicável

## Botões
- [ ] Todo CTA usa o par `<v:roundrect>` + `<a>` com `mso-hide:all`, e os condicionais do
      Outlook (`<!--[if mso]>`, `<!--[if !mso]><!-->`, `<!--<![endif]-->`) estão inteiros —
      sem eles o botão some (o `conferir` acusa)
- [ ] Largura do `roundrect` conferida contra o tamanho real do label
- [ ] Altura de toque ≥ 44px

## Responsivo
- [ ] Colunas lado a lado empilham em ≤600px
- [ ] Com a media query desativada, o layout ainda é legível
- [ ] Imagens não estouram o container em 320px de largura

## Dark mode (peça Podi — no modo empreendimento, ver a seção própria abaixo)
- [ ] Testado em Apple Mail dark e Outlook.com dark
- [ ] Logo legível sobre fundo escuro
- [ ] Nenhum texto escuro sobre fundo escuro

## Conteúdo e envio
- [ ] Subject ≤ 45 caracteres, sem emoji duplicado, sem CAPS
- [ ] Rodapé com `© <ano> - Podi App` e motivo do recebimento
- [ ] **Nenhum link de descadastro** na peça (o servidor não suporta a variável)
- [ ] `python3 -I scripts/conferir.py arquivo.html` sai com 0 — só `{{email}}`, `{{topicId}}`
      ou `{{campaignId}}`, nada de `{{MAIUSCULA}}` sobrando (`variaveis-envio.md`).
      Disparo por outro sistema: `--campos` com os campos do briefing, exatamente como ele
      os escreve, e a entrega avisa que a peça não pode sair pelo servidor do Podi
- [ ] Links de Política de Privacidade e Termos de Uso conforme `brand/links-oficiais.md`
- [ ] Todos os links testados e com `target="_blank"`
- [ ] HTML final < 100 KB (o `conferir` mede)
- [ ] Sem `<script>`, `<form>`, `<iframe>`, `<video>`
- [ ] Versão texto puro gerada (se a ferramenta de envio não gerar sozinha)

## Modo empreendimento (`marca-empreendimento.md`)
Substitui a seção "Dark mode" acima. Todo o resto do checklist continua valendo.

- [ ] `python3 -I scripts/paleta-empreendimento.py "<cor base>"` aprovou os quatro contrastes
      (muted/page, accent-ink/page, accent-ink/accent-soft, texto do CTA/base)
- [ ] `python3 -I scripts/paleta-empreendimento.py "<cor base>" --conferir <arquivo>` sem
      pendência — é ele que garante os itens abaixo marcados com ⚙
- [ ] ⚙ Nenhuma cor do Podi sobrando: grupo verde, tokens de dark mode e o roxo `#9934FF`
- [ ] ⚙ Texto do CTA é o que o contraste decidiu, nas duas metades do botão
- [ ] ⚙ Modo claro forçado: `color-scheme: light only`, sem bloco `prefers-color-scheme`
      ou `[data-ogsc]`, sem nenhuma classe `dm-*`
- [ ] ⚙ Logo e redes do empreendimento, **nunca misturados** com os do Podi: nada de
      `logo-podi`, `logo-tacla-labs` ou URL social do Podi
- [ ] ⚙ Ícones sociais apontam para `imagens/icones/<rede>-campanha.png`, não para `brand/`
- [ ] Ícones recoloridos incluídos na lista de imagens a hospedar
- [ ] Logo do empreendimento em PNG colorido para fundo claro, 24px de altura, até 150px de
      largura, arquivo em 2x — o mesmo no cabeçalho e no rodapé social
- [ ] Estrutura na ordem do modo: `01b` → `03` → `08` B → `13` → `90b` B → `91`
- [ ] Linha fina antes do CTA e um CTA só no card
- [ ] Imagens da galeria 1:1 com no mínimo 448 × 448
- [ ] Texto legal da promoção antes do `©`, em 12/18 `muted`; `© <ano> - Podi App`, motivo
      do recebimento, Privacidade e Termos logo depois
