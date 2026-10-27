# Compatibilidade de e-mail — regras não negociáveis

Newsletter é **HTML de e-mail**, não HTML de site. Metade do que funciona no navegador
não funciona aqui. Estas regras não são preferência de estilo: são o que separa um
e-mail que renderiza de um que quebra no Outlook.

Alvos suportados: Gmail (web, iOS, Android), Apple Mail (macOS/iOS), Outlook 2016–2021
Windows, Outlook.com, Outlook para Mac, Yahoo/AOL, Thunderbird, Samsung Mail,
Superhuman, Hey.

## Estrutura

- **Layout só com `<table>`.** Proibido: `flexbox`, `grid`, `float`, `position`, `calc()`.
- Toda tabela leva `role="presentation" cellpadding="0" cellspacing="0" border="0"`.
- Largura do container: **600px** máximo, com `width="100%"` + `max-width:600px`.
- Nunca aninhar mais de 4 níveis de tabela sem necessidade — o Outlook acumula erro de
  arredondamento.
- Espaçamento **sempre** via `padding` em `<td>`. `margin` é ignorado no Outlook.
  Espaçadores verticais usam
  `<tr><td height="32" style="height:32px;line-height:32px;font-size:0;">&nbsp;</td></tr>`.

## CSS

- **Todo CSS visual vai inline** no atributo `style` do elemento. O `<style>` do head
  serve apenas para media queries, `@font-face`/webfont e overrides de client — nunca
  como única fonte de estilo.
- Proibido: shorthand `background` com imagem, `box-shadow` como elemento essencial,
  pseudo-elementos, CSS custom properties (`var()`), `rem`, `em` para fontes,
  seletores complexos.
- Usar `px` para tudo. `line-height` sem unidade é aceito, mas prefira `px`.
- `border-radius` é permitido, mas **assumir que o Outlook Windows renderiza quadrado**.
  Isso é degradação aceita — nunca deixe o layout depender do raio.

## Tipografia

- Stack obrigatório:
  `font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;`
- Webfont carregada só fora do MSO:
  ```html
  <!--[if !mso]><!--><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"><!--<![endif]-->
  ```
- Sempre incluir
  `<!--[if mso]><style>* {font-family: Arial, Helvetica, sans-serif !important;}</style><![endif]-->`,
  senão o Outlook cai em Times New Roman.
- Corpo de texto mínimo **15px** (o iOS amplia qualquer coisa < 13px e quebra o layout).
  Exceções reais: legal 12px, eyebrow 12px, label de número 14px.
- Todo `<td>` com texto declara explicitamente `font-family`, `font-size`, `line-height`
  e `color`. Não confiar em herança.

Tamanhos e papéis exatos: [`../tokens.md`](../tokens.md).

## Imagens

- `<img>` sempre com: `width` (atributo HTML, em px), `alt` descritivo,
  `style="display:block;border:0;outline:none;text-decoration:none;width:100%;max-width:XXXpx;height:auto;"`.
- Exportar em **2x** a largura de exibição, servir com `width` em 1x.
- Formato: **JPG ou PNG**. Proibido WebP, AVIF e SVG (Outlook e Gmail não renderizam).
- Nenhuma informação crítica pode existir só em imagem — imagens vêm bloqueadas por
  padrão. Texto de headline, preço e CTA sempre em HTML.
- `background-image` só como enfeite, sempre com `bgcolor` sólido de fallback.
- **E-mail não recorta imagem.** O arquivo entra com a forma que tem: fora da proporção,
  ele distorce ou estoura a coluna. Recorte é decisão de quem fez a foto, não da IA.

## Botões / CTA

- Sempre o padrão VML do `components/_button.html`: `<v:roundrect>` para MSO + `<a>`
  para o resto. Nunca um `<a>` solto com `border-radius`.
- Área de toque mínima: 44px de altura.

## Mobile

- Media query única em `@media only screen and (max-width:600px)`, usando classes com
  `!important`. Classes disponíveis: `.stack`, `.p-mobile`, `.full-bleed`, `.h-mobile`,
  `.center-mobile`.
- Colunas lado a lado **sempre** empilham no mobile via `.stack`. Única exceção:
  miniatura de até 96px (`12-card-noticia-compacta.html`), que fica lado a lado até
  320px — empilhar transformaria um print de celular em imagem de largura inteira.
- O layout precisa ficar legível **mesmo se a media query for ignorada**.

## Dark mode

> **Exceção — modo empreendimento.** Peça com a marca do empreendimento é sempre clara:
> `color-scheme: light only`, sem bloco de dark mode e sem classes `dm-*`. O shell já vem
> assim (`templates/newsletter/base-empreendimento.html`). Motivo e limitação em
> [`marca-empreendimento.md`](marca-empreendimento.md). O resto deste arquivo vale igual.

- `<meta name="color-scheme" content="light dark">` e
  `<meta name="supported-color-schemes" content="light dark">`.
- Fornecer bloco `@media (prefers-color-scheme: dark)` ajustando fundo, texto e o fundo
  dos cards.
- CTA escuro **precisa** inverter no dark (`.dm-btn` → fundo branco, texto preto),
  senão vira preto sobre preto.
- **Logos: sempre a versão light mode.** No dark, envolver o logo num `<td class="dm-logo">`
  — a classe pinta uma placa branca atrás dele para a arte escura não sumir. Nunca
  depender de troca de arquivo por CSS.
- Imagens com fundo branco precisam de `padding` ou fundo próprio para não "flutuar"
  no dark.

## Head obrigatório

- `<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" ...>` com `xmlns:v` e `xmlns:o`.
- `<meta name="viewport" content="width=device-width,initial-scale=1">`.
- Bloco `<o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch>` dentro de `<!--[if mso]>`.
- **Preheader** oculto como primeiro elemento do `<body>` (ver `templates/newsletter/base.html`).

## Conteúdo e entregabilidade

- Rodapé sempre com: `© <ano> - Podi App`, motivo do recebimento, Política de Privacidade
  e Termos de Uso — os dois últimos com as URLs oficiais de `brand/links-oficiais.md`.
  **Sem link de descadastro** (ver `variaveis-envio.md`).
- Só três variáveis existem no envio: `{{email}}`, `{{topicId}}`, `{{campaignId}}`.
  Qualquer outra derruba a campanha — regra completa em `variaveis-envio.md`.
- Sem `<form>`, `<script>`, `<iframe>`, `<video>`, `<embed>`, `<object>`.
- **Nenhum JavaScript em nenhuma forma.** Sem `<script>`, sem atributos `on*`
  (`onclick`, `onload`, `onmouseover` etc.), sem `href="javascript:..."`. Clientes de
  e-mail removem ou bloqueiam o e-mail inteiro ao detectar JS — não é degradação
  graciosa, é risco de a mensagem não entregar.
- Sem tracking pixel inventado — usar só o que a ferramenta de envio injeta.
- Peso do HTML final < **100 KB** (o Gmail corta acima disso e mostra "[Mensagem truncada]").
- Todos os links absolutos com `https://`, e `target="_blank"`.
