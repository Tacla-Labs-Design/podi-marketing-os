---
name: newsletter-podi
description: Monta uma newsletter, Podi News, informativo interno ou e-mail marketing do Podi a partir de um briefing em projects/_inbox/<slug>/. Use quando pedirem para gerar, montar ou criar uma newsletter, um Podi News, um informativo interno ou um e-mail marketing a partir de um documento e uma pasta de imagens.
---

# Montar uma newsletter Podi

Argumento: o slug da pasta em `projects/_inbox/`. Sem argumento, listar as pastas
disponíveis e perguntar qual.

Esta skill é o **procedimento**. As regras que ela obedece estão em outros lugares e
valem integralmente:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/README.md`, `brand/links-oficiais.md`, `brand/marca.json` | Identidade, contraste, frentes, links fixos, regra de envio |
| Brand | `brand/photography/STYLE-LOCK-PODI.md` | Direção fotográfica — só quando a peça pedir **foto nova** |
| Design System | `design-system/newsletter/` | Tokens, componentes, compatibilidade, ritmo, variáveis de envio, QA |
| Design System | `design-system/newsletter/guidelines/marca-empreendimento.md` | Modo empreendimento — só quando o remetente é o shopping |
| Template | `templates/newsletter/base.html` | O shell |
| Template | `templates/newsletter/base-empreendimento.html` | O shell do modo empreendimento, sempre claro |

Em caso de conflito, a camada mais alta prevalece. Ver `docs/governanca.md`.

## 0. Atualizar o padrão

Antes de qualquer coisa, e **sem perguntar nada ao usuário**:

```bash
./scripts/check-atualizacao.sh --atualizar
```

Quem usa este comando não é pessoa técnica (`CLAUDE.md`). Não peça para ela rodar Git:
o script já traz a versão nova sozinho.

- **Saída 0** → seguir. Se o script disse que atualizou, mencione em uma linha, em
  português comum: *"Atualizei o padrão para a versão mais recente antes de montar."*
  Se não atualizou nada, não comente — silêncio é o esperado.
- **Saída 1** → houve alteração local conflitante. **Parar.** Dizer que esta cópia do
  padrão está diferente da oficial e que é preciso avisar quem cuida do repositório.
  Não tentar resolver, não sugerir comando, não montar assim mesmo: o e-mail sairia com
  o template antigo e nada no arquivo denunciaria isso.

Sem Git, sem remoto ou offline, o script sai 0 e o trabalho segue normalmente.

## 1. Ler tudo antes de decidir qualquer coisa

```bash
ls -R projects/_inbox/<slug>/
```

- `.docx` → `textutil -convert txt -stdout arquivo.docx`
- `.pdf` → `pdftotext arquivo.pdf -`
- `.zip` → `unzip -o arquivo.zip -d projects/_inbox/<slug>/imagens/`
- Imagens → **abrir de fato** com a tool Read. Nome de arquivo não é prova de conteúdo,
  e você precisa da proporção real para escolher o bloco.

## 1a. Detectar o modo: quem é o remetente

Se o briefing diz que o **remetente é o empreendimento** (shopping, outlet, campanha dele)
— `Remetente: City Center Outlet Premium`, por exemplo —, a peça é do **modo
empreendimento** (`design-system/newsletter/guidelines/marca-empreendimento.md`). Se o
remetente é o Podi, ou o briefing não fala nisso e o conteúdo é do Podi, é peça Podi normal
e esta seção não se aplica. Se o briefing é de um shopping e não diz quem assina, perguntar.

**O modo já decide, e não se pergunta de novo:** cabeçalho (`01b`), rodapé social (`90b`
variante B), rodapé legal Podi, estrutura da peça e modo sempre claro. Se a pessoa pedir
dark mode, explicar em uma frase que o modo é sempre claro porque ainda não há regra de
escuro para outra cor, e seguir.

**O que pedir, se faltar** — tudo numa pergunta só:

- logo **colorido, em PNG, para fundo claro** (vai a 24px de altura, até 150px de largura;
  o arquivo precisa ter o dobro);
- **cor base** da campanha em hex (ex.: `#173B2A`);
- **URLs das redes** do empreendimento — nunca usar as do Podi no lugar;
- **texto legal** da promoção;
- **imagens** — os benefícios/produtos da galeria em **1:1**, mínimo 448 × 448;
- **por onde sai o disparo**, se o briefing traz campos como `{{nome}}` e não diz (§4, item 7).

Com a cor base em mãos, **antes de montar**:

```bash
python3 -I scripts/paleta-empreendimento.py "<cor base>" <slug>
```

- **Saída 0** → seguir. Guardar a tabela de troca e o texto do CTA que ele imprimiu. Os
  ícones recoloridos já ficam em `saida/<slug>/imagens/icones/`.
- **Saída 1** → **parar.** Contraste reprovado ou cor sem matiz (preto, cinza). Dizer em
  português comum: *"essa cor não dá leitura suficiente no e-mail; preciso de outra cor
  base do empreendimento"* — ou, para cor neutra, que o padrão ainda não cobre esse caso e
  é preciso avisar quem cuida dele. Não ajustar a cor por conta própria.

Nunca calcular a paleta à mão, nem "corrigir" um valor que o script devolveu.

## 2. Mapear imagem → componente

O nome do arquivo carrega a intenção (ver `docs/como-enviar-conteudo.md`):

| Nome | Significado | Componente |
|---|---|---|
| `capa.*` | Abertura da edição | `00-hero-podi-news` (Podi News) ou `03-hero-image` |
| `NN-nome.*` | Notícia NN, imagem no topo em largura inteira | `11-card-noticia` |
| `NN-nome-1x1.*` | Notícia NN, imagem ao lado do texto | `07-artigos-alternados` ou `12-card-noticia-compacta` |

O `NN` casa com o número do bloco no documento. Se o texto e a imagem não fecharem,
**perguntar** — associação errada é pior que pergunta a mais.

## 3. Conferir a proporção antes de montar

E-mail não recorta imagem: o arquivo entra com a forma que tem.

- Sem sufixo / `capa` → **16:9 ou mais panorâmica**, mínimo 1072px de largura
- `-1x1` → **quadrada**, tolerância de 2%, mínimo 496×496
- Galeria dentro do card (`13a`, modo empreendimento) → **quadrada**, mínimo 448×448

Quando não bater, **não distorça e não corte por conta própria**. Monte o resto do
e-mail e relate no fim: qual arquivo, qual proporção veio, qual era esperada.

Exceção: se a imagem estiver só acima do tamanho mínimo (proporção certa, sobra de
pixel), pode usar — o `width` do HTML resolve.

Formato fora de JPG/PNG (WebP, AVIF, HEIC, SVG) é bloqueio: converter com
`sips -s format jpeg` e avisar, ou pedir o arquivo certo.

## 4. Montar

1. Frente `cliente` ou `interno` (`brand/README.md`) — decide rodapé e tom.
   **Nenhuma peça leva link de descadastro:** o servidor de envio não suporta a variável e
   ela derruba a campanha (`design-system/newsletter/guidelines/variaveis-envio.md`).
2. Edição do **Podi News** → header obrigatório `00-hero-podi-news.html`
   (`design-system/newsletter/components/README.md`).
3. Copiar `templates/newsletter/base.html` para **`saida/<slug>/index.html`** e colar os
   blocos de `design-system/newsletter/components/` no lugar marcado. Os comentários dos
   blocos podem ficar — o `conferir` não os lê. **Nunca apagar** os condicionais do Outlook
   (`<!--[if mso]>`, `<!--[if !mso]><!-->`, `<!--<![endif]-->`): sem eles o botão some.
   Nunca gravar em `examples/` — aquilo é acervo curado, gravado só por quem cuida do padrão.
4. Máximo de **4 blocos de conteúdo**. Passou disso, cortar ou propor dois envios.
5. Ativos e links fixos de `brand/links-oficiais.md` — imagem do fecho, URLs sociais,
   CTA fixo — **não se inventa**.
6. **Nunca escrever cor solta.** Toda cor sai de `design-system/newsletter/tokens.md`.
7. **Campos personalizados** (`{{nome}}`, `{{economia_total}}`…): só ficam se o briefing
   disser que o disparo é **por outro sistema**, e escritos exatamente como o briefing os
   define. Se o briefing traz os campos e não diz por onde sai, **perguntar antes de
   montar**. Sem essa confirmação, só as três variáveis
   (`design-system/newsletter/guidelines/variaveis-envio.md`).

**No modo empreendimento**, os passos 2 e 3 mudam:

- Copiar `templates/newsletter/base-empreendimento.html` (não o `base.html`). Um arquivo
  por e-mail quando a campanha tem vários.
- Blocos nesta ordem: `01b-header-empreendimento` → `03-hero-image` → `08-destaque-numeros`
  variante B → `13-card-conteudo` (com os itens do `13`, `13a` e `13b`) → `90b-social-logo`
  variante B → `91-footer-legal` com o texto legal antes do `©`.
- Depois de colar: trocar o grupo verde pela tabela do script, trocar o texto do CTA nas
  duas metades do botão se ele mandou, tirar todas as classes `dm-*` e apontar os ícones
  para `imagens/icones/<rede>-campanha.png`.
- O card único é **uma** seção: um CTA só, no fim, com a linha fina antes.

## 5. Quando falta algo no sistema

Se o conteúdo pede um bloco, uma cor ou um layout que não existe:

1. **Não invente.** Não crie uma cor nova, não improvise um bloco com CSS solto.
2. Verifique se um componente existente resolve com outro conteúdo.
3. Se realmente não resolve, monte o resto do e-mail e **relate a ausência no fim**,
   marcada explicitamente como **proposta**: o que falta, onde seria usado, e o que você
   sugere.
4. Proposta não vira padrão sozinha. Quem decide é o maintainer (`docs/governanca.md`).

Se o briefing pedir uma **fotografia que ainda não existe**, a direção visual não se
inventa: ela está no Style Lock (`brand/photography/STYLE-LOCK-PODI.md`). Relate o que falta e
aponte o Style Lock como referência para quem for produzir a imagem.

Isso vale **só para fotografia**. As imagens que chegam em `_inbox/` não passam por
avaliação de estilo fotográfico — muitas são print de tela, montagem gráfica ou arte, e
para elas o único critério continua sendo formato e proporção (§3).

Se o pedido do usuário conflita com o brand — outra cor, texto branco sobre o verde,
outro logo — **sinalize o conflito** em vez de alterar a identidade. Explique a regra em
uma frase e ofereça a alternativa que respeita o sistema.

## 6. QA e entrega

Rodar `design-system/newsletter/guidelines/qa-checklist.md` inteiro antes de dizer que
está pronto. Os itens verificáveis por comando:

```bash
python3 -I scripts/conferir.py saida/<slug>/index.html   # saída 0
```

Ele lê a peça sem os comentários e confere, de uma vez: peso abaixo de 100 KB, nada de
`<script>`, `<form>`, `<iframe>`, flex, `calc()` ou `var(--)`, toda tabela com
`role="presentation"`, toda imagem com `alt`, todo link com `target="_blank"`, botão VML
inteiro, cor só da paleta, o verde nunca como cor de texto, nenhum "a Podi" — e as
variáveis.

As variáveis são o mais caro de errar: `{{MAIUSCULA}}` que sobrou é placeholder não
preenchido, e qualquer variável fora das três permitidas **derruba o envio inteiro**
(`design-system/newsletter/guidelines/variaveis-envio.md`). Em disparo por outro sistema,
passar os campos do briefing — e nenhum outro:

```bash
python3 -I scripts/conferir.py --campos nome,economia_total saida/<slug>/index.html
```

**No modo empreendimento**, o `conferir.py` não se aplica (a paleta é derivada da cor do
shopping). No lugar dele:

```bash
python3 -I scripts/paleta-empreendimento.py "<cor base>" --conferir saida/<slug>/*.html   # saída 0
```

Ele acusa cor do Podi sobrando, classe `dm-*`, falta do `light only`, ícone ou rede do Podi
e texto do CTA errado. Pendência aqui é correção antes de entregar, não item de relatório.

Relatar sempre: caminho do arquivo, **subject** (≤45 caracteres), **preheader** (60–90),
peso do HTML, componentes usados, imagens a hospedar com dimensão final, e o que ficou
de fora e por quê.

No modo empreendimento, relatar também: a cor base e os tokens que o script gerou, os
ícones recoloridos a hospedar e o aviso de que o modo é sempre claro (o app do Gmail e parte
do Outlook podem escurecer a peça por conta própria).


Se a peça tem campos personalizados, a entrega diz, em destaque: **esta peça não pode sair
pelo servidor do Podi** — lá, esses campos derrubam o envio inteiro.
