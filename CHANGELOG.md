# Changelog

Mudanças no padrão — templates, tokens, regras e assets fixos.

Mantido pelo dono do repositório. Quem escreve newsletter lê para saber o que mudou
desde o último envio; as skills avisam quando o clone está atrás.

**Ação necessária** marca o que exige refazer ou revisar algo já montado. O resto
entra sozinho no próximo e-mail.

---

## 2026-10-29 — Verde #31D06E, DM Sans, ícones Bulk e o deck do Figma

O DS de apresentação passa a seguir os três slides que o time usa nos decks (arquivo
**[DECK] Simple Deck - Podi**, no Figma). Com eles mudam o verde e a fonte da marca inteira.

### Mudado

- **Verde de marca: `#48DB84` → `#31D06E`**, em todos os materiais: tokens, componentes, templates,
  exemplos, `marca.json`, logo pack e hub. Os contrastes mudam pouco: `#101010` sobre o verde dá
  9,4:1, o verde sobre branco dá 2,02:1. Recoloridos: `logo-podi.png`, `logo-podi-transparente.png`,
  os ícones sociais `-green` e o `hero-podi-news.png`.
- **Fonte: Inter → DM Sans**, em todos os materiais. Pesos com papel fixo: 600 nos títulos, 400 no
  texto, 700 só no destaque. O e-mail usa 400 e 600.
- **Deck**: `00-capa`, `04-split-foto-cards` e `07-mockup-app` refeitos medida por medida pelo Figma;
  `05` e `06` herdam o card e a caixa de recursos deles. Margem de segurança de 96 para 64px; card
  com padding 40; régua de 4px que some para a direita (200px sob título, 56px em card); título de
  card 48px. `accent-2-line` vira `#E6CCFF`.
- **Roxo**: o limite é de 3 *tipos* de detalhe por slide; o que se repete numa grade conta uma vez.
- **Logo**: branco também sobre foto, numa área calma. O logo preto fica só para impressão a uma
  cor — o modelo do hub assinava o rodapé de slide verde em preto, e o certo é branco.

### Novo

- **Ícones HugeIcons Bulk** (`brand/assets/icones-bulk/`, 93 ícones, com `index.json` de usos),
  soltos e sem chip, por `currentColor`. Regra para desenhar ícone novo na mesma estética em
  `brand/README.md` → Ícones. `scripts/icones.py` refaz o pack a partir do pacote Pro; o
  `publicar` envia a pasta ao hub em `podi/icones/`.
- **Ativos fixos do deck** (`brand/assets/deck/`): ripple, mão com o celular e duas telas do app.
- Tokens `accent-deep` `#074A21` (tagline sobre o verde), `accent-line` `#2E9054` (ripple) e
  `accent-edge` `#28C463` (borda das telas do app).
- Modelo de deck do hub com 9 tipos: entram o split com foto e o slide da plataforma.

### Removido

- O chip de ícone do deck (`.chip`), trocado pelo ícone solto (`.ico`).
- A linha de cliente e data da capa: a capa do Figma é só logo, tagline e o app.

**Ação necessária:** deck ou e-mail montado antes desta versão sai no verde e na fonte antigos.
Antes de reenviar, monte de novo pela versão atual do padrão.

---

## 2026-10-27 — O Podi no hub de marcas

O time passa a usar a marca também pelo hub (`https://marcas.taclalabs.workers.dev/podi/`), que
qualquer ferramenta lê sem clonar o repositório.

### Novo

- **`hub/`**: `BRAND.md`, guias de e-mail, apresentação e foto, e modelos HTML com `data-slot`
  (Podi News e deck). Post fica fora até os modelos chegarem; o modo empreendimento continua só
  no repositório.
- **`scripts/publicar`**: monta a pasta da marca — com o logo em verde, branco e preto, gerados do
  SVG monocromático —, confere que todo endereço citado existe e envia ao bucket, com o manifesto
  por último.
- **Logo pack** (`scripts/logo-pack.py`, página em `hub/guia/index.html`): o logo em verde, branco e
  preto, em SVG e PNG de 512 a 4096 px, com a página da marca — logo, cores, fonte, onde usar e o
  que não pode. O `publicar` gera o pack e envia a pasta para `podi/guia/` e o zip para
  `podi/podi-logo-pack.zip`; os arquivos de `podi/logos/` passam a sair do pack.

### Mudado

- `scripts/conferir.py` aceita imagem pelo endereço do hub e campo de imagem vazio com
  `data-slot`, e conta os condicionais do Outlook só fora dos comentários.

### Removido

- `examples/newsletter/2026-09-empreendimento-save-win/brief.md`: era o briefing do cliente, e o
  repositório é público. O exemplo continua com as duas peças e o README que explica o modo.

---

## 2026-10-27 — O padrão volta a ser só do Podi

O Optimall passou a ter o próprio padrão, mantido à parte. Manter as duas marcas no mesmo
lugar exigia um passo de escolha de marca em toda skill, uma troca de cor no fim do e-mail e
regras que o time do Podi lia sem precisar. Com o Optimall fora, tudo isso sai daqui.

### Removido

- Tudo o que era só do Optimall: identidade, mensagens e assets, as bibliotecas de slides e
  de posts dele, os templates `base-optimall.html` e os comandos `/newsletter-optimall`,
  `/apresentacao-optimall`, `/post-optimall` e `/foto-optimall`.
- O que existia só por causa das duas marcas: a escolha de marca nas skills (e a linha
  `Marca:` no briefing), `scripts/aplicar-marca.py` (`validar`, `derivar`, `aplicar`) e
  `design-system/newsletter/guidelines/marcas.md`.

### Mudado

- **`brand/podi/` volta a ser `brand/`**: `README.md`, `links-oficiais.md`, `marca.json`,
  `assets/` e `photography/` (Style Lock e refs) sobem um nível. O `marca.json` perde o
  `status`, que só servia para bloquear marca pendente.
- **`scripts/conferir.py`** substitui o `aplicar-marca.py` e é só do Podi. Lê a peça sem os
  comentários do HTML — os `grep` soltos contavam texto de comentário — e confere paleta, o
  verde como cor de texto, as três variáveis do servidor (`--campos` para disparo por outro
  sistema), `alt`, e, no e-mail, peso, CSS proibido, tabela sem `role`, link sem `target` e
  botão sem a metade de fora do Outlook. `--marca` confere o `marca.json` (maintainer).
- **`scripts/paleta-empreendimento.py`** passa a rodar com `python3 -I`, que não punha a pasta
  do script no caminho e quebrava o `import` do `_cor.py`.
- **`projects/` inteiro fica fora do Git**, menos o `README.md` e o `_inbox/`: projeto de
  cliente fora do `_inbox/` estava sendo versionado.
- CLAUDE.md, README, guias, índice de skills e as skills voltam a falar de uma marca só.

**Ação necessária:** peça já montada em `saida/` que aponta para `../../brand/podi/...`
perde as imagens no preview. Troque esses caminhos por `../../brand/...` antes de abrir de
novo — ou monte a peça outra vez.

---

## 2026-10-23 — Foto do Podi: a pessoa não precisa estar olhando o celular

A regra de olhar do Style Lock do Podi dizia que o sujeito **sempre** olha para a tela do
celular. Isso impedia cenas legítimas da marca — alguém lendo um livro na praça de
alimentação, conversando, descansando — que mostram o shopping como lugar de bem-estar, não
só de uso do app. O Optimall já tinha uma regra mais aberta (o olhar vai para o trabalho).

### Mudado

- **Regra de olhar** (`brand/podi/photography/STYLE-LOCK-PODI.md` §1.4): o invariável agora é
  **nunca olhar para a câmera**. Por padrão o olhar vai para a tela; quando a cena é de outra
  atividade, vai para ela. O **celular continua sempre no quadro** (na mão ou apoiado perto,
  com o glow verde) — é ele que amarra a foto ao app.
- **Bloco STYLE LOCK** (§4.A, §4.B e as cópias da §7) e **CLEAN-FRAME CLAUSE** (§2.9 e §7.2):
  a frase do olhar foi reescrita nesse sentido. O resto do bloco não mudou.
- §2.7 (linhas Sujeito e Celular) e checklist da §6 acompanham a regra nova.
- `/foto-podi`: o slot "Ação no app" aceita um momento sem o app em uso, com o celular no
  quadro.

Fotos já geradas continuam válidas — quem olhava o celular segue dentro da regra.

---

## 2026-10-07 — Optimall aprovado: deck, post e e-mail B2B

O Optimall saiu de "pendente" e passou a montar as três peças: **e-mail, deck e post**,
sempre B2B, falando com quem decide no shopping. A identidade veio do site publicado
(optimall.com.br, código do `lp-optimall`) e dos dois arquivos do Figma do time do Optimall:
*Apresentação Comercial 2026* (12 slides) e *Social Media – Optimall* (7 posts aprovados).

**A regra "um design system só" mudou.** O plano de 2026-09-28 era montar o deck do Optimall
com os slides do Podi e recolorir. Os modelos do Figma mostraram que a linguagem do Optimall —
degradê roxo, vidro, pattern de pontos, fonte Halyard, logo tricolor — não sai de pintar os
slides do Podi de outra cor. Agora: **procedimento, canvas, QA e governança continuam comuns;
deck e post do Optimall têm biblioteca própria** e já nascem na paleta dele; o **e-mail
continua** nos mesmos blocos, recolorido pelo script.

### Adicionado

- **Marca Optimall aprovada** (`brand/optimall/`):
  - `marca.json` com `"status": "aprovado"`: roxo `#9934FF`, **texto branco sobre o roxo**
    (`#101010` não passa 4,5:1), roxo de texto `#9025F4`, lavandas e neutros do site, sem
    secundária; `paleta_extra` com os degradês e lilases do Figma; `fonte`, `contato`, logo
    positivo/negativo/símbolo; `links.termos: false` (o Optimall não tem Termos de Uso).
  - `mensagens.md` (novo): público, posicionamento, os 4 módulos, complementares,
    integrações, **números oficiais** (+260 campanhas · +3,8 mi compras · +470 eventos ·
    +R$ 980 mi GMV — os do site, confirmados pelo maintainer; os do deck antigo não valem),
    prova social, voz B2B e frases aprovadas.
  - `README.md` e `links-oficiais.md` reescritos; `photography/STYLE-LOCK-OPTIMALL.md` (novo),
    derivado do Podi: mesma luz e lente, roxo em três valores, cenas B2B.
  - `assets/`: logos (SVG positivo, negativo, símbolo; PNG 2x do e-mail), ícones sociais
    roxos, `icones-ui/` (HugeIcons bulk), `clientes/`, `parceiros/`, `produto/`, `fotos/`,
    `grafismos/`.
- **Deck do Optimall**: `design-system/apresentacao/optimall/` (`README.md`, `tokens.md`,
  14 slides — os 12 do Figma e dois derivados das mesmas peças, `12-titulo-texto` e
  `13-citacao`) e `templates/apresentacao/base-optimall.html`.
- **Material novo: post** — `design-system/post/` (canvas 1080×1350, carrossel, legenda, QA),
  `design-system/post/optimall/` (7 modelos do Figma) e `templates/post/base-optimall.html`.
  Podi: modelos pendentes — o `/post-podi` avisa em vez de improvisar.
- **Skills** `post-podi` (procedimento) e `post-optimall` (atalho).
- **`scripts/exportar.py`** — PNG de post e PDF de deck pelo Chrome da máquina, conferindo
  antes se a fonte da marca está instalada.

### Mudado

- `CLAUDE.md`, `brand/README.md`, `README.md`, `skills/README.md`, `docs/*`: a nova regra
  (biblioteca de deck e post por marca), o Optimall aprovado, o material post.
- `/apresentacao-podi` escolhe biblioteca, tokens e template pela marca; no Optimall **não
  recolore** e gera o PDF pelo `exportar.py`. `/apresentacao-optimall` atualizado.
- `/newsletter-podi` (parte Optimall) e `design-system/newsletter/guidelines/marcas.md`: texto
  de `mensagens.md`, botão roxo com texto branco, rodapé sem Termos, sem Facebook.
- `/foto-podi`: diferenças do Optimall (ação no trabalho, figurino, sem `--sref` das refs do
  Podi, tela de produto nunca gerada).
- `scripts/aplicar-marca.py`: aceita `termos: false`, `paleta_extra` no `conferir`, recusa
  recolorir deck/post de marca com biblioteca própria, e chama de "campo não preenchido" o
  `{{…}}` que sobra em deck e post.
- `design-system/apresentacao/guidelines/`: canvas cita a fonte de cada marca e o export por
  script; QA ganhou a seção do Optimall.

### Decisões a confirmar

- **Fonte dos posts.** O Figma dos posts foi desenhado em **DM Sans**; o padrão usa
  **Halyard Text** (a fonte do site e do deck), com títulos em 400 e corpo em Book para
  compensar o peso. Se o time preferir DM Sans nos posts, é trocar o `--font` do template.
- **Ícones do slide de problema** (`02-problema`): no Figma são multicoloridos; no padrão
  ficaram roxos, porque as outras cores não são da marca.
- **Post 05:** um dos chips do Figma era o símbolo do Podi; virou o ícone de celular.

**Ação necessária:** quem tem cópia local deixa a skill atualizar o padrão antes de montar
peça do Optimall. Peça do Optimall montada antes desta versão não existia (a marca estava
pendente).

---

## 2026-09-28 — Optimall como segunda marca

O Optimall, a plataforma B2B que oferece o Podi aos shoppings, precisa de e-mails e decks com
a mesma estrutura e o mesmo estilo do Podi. O plano antigo era duplicar o repositório e trocar
a paleta — mas duas cópias divergem na primeira correção. Em vez disso, **o design system
continua um só**: componentes e slides são escritos uma vez, com os valores do Podi, e a peça
do Optimall é montada igual e recolorida no fim, papel por papel, por um script. É o mesmo
mecanismo do modo empreendimento, com a paleta fixa e aprovada em vez de derivada na hora.

A identidade do Optimall (cores, logo, links, textos fixos, regra de envio) **ainda não foi
carregada**: `brand/optimall/marca.json` está com `"status": "pendente"`, e nenhuma peça do
Optimall é montada até o maintainer aprovar.

### Adicionado

- **`brand/README.md`** (novo) — regras comuns às duas marcas, como saber de qual marca é a
  peça (comando ou linha `Marca:` do briefing; sem nenhum, Podi) e como carregar uma marca.
- **`brand/optimall/`** — `README.md` (marca B2B, masculina, 100% independente: não cita o
  Podi nem a Tacla Labs), `links-oficiais.md` e `marca.json`, com os campos a preencher.
- **`brand/podi/marca.json`** e **`brand/optimall/marca.json`** — os valores da marca para
  máquina: cor por papel (grupo de marca, secundária, neutros, dark mode), logo, ícones, links,
  rodapé, textos fixos do deck, regra de envio e o que a peça não pode conter.
- **`scripts/aplicar-marca.py`** — `validar` (marca completa e contrastes), `derivar`
  (maintainer: propõe o grupo de marca a partir da cor principal, grava e gera os ícones),
  `aplicar` (recolore a peça montada: cores, texto do CTA, ícones, links, rodapé, `<symbol>` e
  `viewBox` do logo do deck) e `conferir` (cor fora da paleta, sobra de outra marca, variável
  não permitida).
- **`scripts/_cor.py`** — a conta de cor (OKLab, contraste) e o PNG, tirados do
  `paleta-empreendimento.py` para os dois scripts usarem a mesma.
- **`design-system/newsletter/guidelines/marcas.md`** — peça do Optimall: blocos (`01b`,
  `90b` B, `91`), recolorir, conferir, entrega.
- **`.claude/skills/newsletter-optimall`**, **`apresentacao-optimall`**, **`foto-optimall`** —
  atalhos: seguem a skill `-podi` do mesmo material com a marca fixada. O procedimento não é
  copiado.

### Alterado

- **`brand/`** reorganizado: tudo que era do Podi foi para **`brand/podi/`** — `README.md`,
  `links-oficiais.md`, `assets/`, `photography/STYLE-LOCK-PODI.md` e `refs/`.
  `brand/photography/README.md` ficou comum às duas marcas. Nenhum valor do Podi mudou.
- **Caminhos** `brand/assets/…`, `brand/links-oficiais.md`, `brand/README.md` e o Style Lock
  atualizados em skills, componentes, templates, docs, exemplos e scripts.
- **Deck:** o `<symbol id="logo-podi">` virou `logo-marca` e `.logo--verde` virou
  `.logo--marca` (template e 14 slides). Os textos fixos do Podi nos slides viraram
  placeholders preenchidos pelo `marca.json`: `{{TAGLINE}}` no `00-capa`; `{{CTA_URL}}`,
  `{{CTA_TEXTO}}` e `{{REDE}}` no `15-encerramento` (que também trocou `color:#fff` por
  `var(--ink-inverse)`); `{{SEM_MARCA}}`/`{{COM_MARCA}}` no `11-comparativo`.
- **`tokens.md`** de newsletter e apresentação — tabela token × papel da marca, com a coluna
  do Optimall pendente; saiu a nota de duplicação do repositório.
- **`variaveis-envio.md`** — a regra das três variáveis passa a ser do servidor do Podi. O
  Optimall sai por outro sistema, com regra pendente: até lá, nenhuma variável na peça.
- **`/newsletter-podi`**, **`/apresentacao-podi`**, **`/foto-podi`** — ganharam o passo "Qual
  marca" e leem tudo que é de marca de `brand/<marca>/`; os QA passaram a rodar
  `aplicar-marca.py conferir`.
- **`qa-checklist.md`** dos dois materiais, `uso-do-roxo.md`, `slides/README.md`, READMEs de
  design system e de componentes, `CLAUDE.md`, `README.md`, `skills/README.md` e `docs/` —
  descrevem as duas marcas. Contagens corrigidas (23 componentes de e-mail, 16 slides).
- **`scripts/paleta-empreendimento.py`** — importa a conta de cor de `_cor.py` e lê os ícones
  de `brand/podi/assets/icones/`. Saída idêntica à anterior (conferida no exemplo SAVE & WIN).

**Ação necessária:** quem tem a pasta do padrão no computador precisa atualizá-la — os
caminhos de `brand/` mudaram. As skills fazem isso sozinhas no passo 0. Peça já montada em
`saida/` que aponte para `../../brand/assets/…` precisa passar a apontar para
`../../brand/podi/assets/…` para as imagens do Podi voltarem a carregar no preview.

**Pendência:** cores, logo (SVG monocromático + PNG), links, redes, textos do deck e regra de
envio do Optimall; depois, `STYLE-LOCK-OPTIMALL.md` nascido do do Podi com a paleta nova.
Deck com cor de marca escura (texto branco sobre ela) ainda não tem regra — o script trava e
vira proposta se a cor do Optimall pedir isso.

---

## 2026-09-23 — exemplo curado do modo empreendimento

O modo empreendimento nasceu sem um exemplo que mostrasse o resultado esperado. Os sete
e-mails do SAVE & WIN foram montados à mão antes da regra e têm desvios dela, então não
entraram como estão: dois foram remontados com os componentes oficiais.

### Adicionado

- **`examples/newsletter/2026-09-empreendimento-save-win/`** — `01-boas-vindas.html` (o
  card único completo) e `07-balanco-final.html` (o extrato longo), com `brief.md` (o
  briefing com remetente, disparo, cor base e redes) e um `README.md` que registra as
  decisões: assuntos do cliente mantidos acima de 45 caracteres, preheaders refeitos para
  60–90, rodapé sem o pedido de descadastro e na ordem do `91`.
- **Pendência:** o hero só existe em 600 × 300, abaixo do mínimo de 1072. Troca o arquivo
  quando chegar a arte em 2x; o HTML não muda.

### Alterado

- **`README.md`**, **`docs/estrutura.md`**, **`marca-empreendimento.md`** — apontam para o
  exemplo.

---

## 2026-09-23 — e-mail com marca do empreendimento

O SAVE & WIN do City Center Outlet Premium foi o primeiro e-mail em que o remetente é o
empreendimento, não o Podi: sete e-mails de gatilho com o logo, a cor e as redes do outlet.
Ele foi montado à mão, com decisões fora do padrão — header, paleta, ícones, modo claro,
campos personalizados. Sem regra, o próximo sairia diferente, e todo e-mail desse tipo seria
tratado como conflito de marca. As decisões do SAVE & WIN viraram o **modo empreendimento**.

### Adicionado

- **`design-system/newsletter/guidelines/marca-empreendimento.md`** — quando usar, o que
  muda e o que não muda, a estrutura da peça, o algoritmo da paleta, os contrastes que
  bloqueiam a montagem, a conferência de referência e a limitação do modo claro.
- **`scripts/paleta-empreendimento.py`** — recebe a cor base em hex e imprime os tokens
  derivados, os contrastes e a tabela de troca; sai com erro se algum contraste reprovar ou
  se a cor for neutra; gera os ícones sociais recoloridos em `saida/<slug>/imagens/icones/`.
  Com `--conferir`, confere peças montadas (só leitura). Só biblioteca padrão do Python.
  Para `#173B2A` ele devolve exatamente a paleta usada no SAVE & WIN.
- **`templates/newsletter/base-empreendimento.html`** — o shell sempre claro: `light only`,
  sem bloco de dark mode e sem classes `dm-*`. Um arquivo à parte, e não uma instrução de
  adaptação, porque a diferença está no `<head>` — é exatamente o que dá errado quando se
  adapta à mão, e nada no e-mail montado denunciaria o erro.
- **Componentes:** `01b-header-empreendimento` (logo centralizado na placa branca),
  `13-card-conteudo` (card único e seus itens: texto, título de grupo, lista, nota, linha
  fina, CTA), `13a-card-galeria-2col` (galeria 1:1 dentro do card) e `13b-card-extrato`
  (rótulo à esquerda, valor à direita).
- **`08-destaque-numeros`** — variante B, de uma coluna: rótulo 16px em cima, número 32px
  embaixo. A de três colunas virou a variante A, sem mudança.

### Alterado

- **`brand/README.md`** — seção nova "Peças com marca do empreendimento": quando é
  permitido (o remetente é o empreendimento), que o verde Podi sai só nesse caso, e o que
  continua Podi (`© Podi App`, link do app, regras de texto). A assinatura Podi + Tacla Labs
  no topo passa a ter essa única exceção.
- **`brand/links-oficiais.md`** — os ícones recoloridos são exceção aos `-green` e nunca
  são gravados em `brand/`.
- **`variaveis-envio.md`** — a regra das três variáveis vale para o servidor do Podi. Se o
  briefing disser que o disparo é por outro sistema, os campos dele ficam, escritos como o
  briefing define, e a entrega avisa que a peça não pode sair pelo servidor do Podi. Na
  dúvida, a skill pergunta.
- **`email-compat.md`** — a seção de dark mode registra a exceção do modo empreendimento.
- **`tokens.md`** — referência à paleta derivada e ao script; rótulo 16px na variante B do
  `08`; tamanhos do logo do empreendimento e da galeria no card.
- **`qa-checklist.md`** — seção do modo empreendimento, no lugar da de dark mode.
- **`91-footer-legal`** — comentário marcando onde entra o texto legal da promoção (antes
  do `©`). O bloco em si não mudou.
- **`components/README.md`** — os blocos novos no catálogo e uma seção do modo.
- **`/newsletter-podi`** — detecta o modo pelo remetente, pede só o que falta (logo, cor
  base, redes, texto legal, imagens 1:1, por onde sai o disparo), roda o script antes de
  montar e o `--conferir` no QA. Não pergunta cabeçalho, rodapé nem modo claro.
- **`docs/como-enviar-conteudo.md`** — o que o time manda para um e-mail de empreendimento.
- **`CLAUDE.md`** — as regras não negociáveis citam o modo e a exceção das variáveis.
- **`design-system/newsletter/README.md`**, **`docs/estrutura.md`** — contagem de blocos
  (23), a guideline, o template e o script novos.

---

## 2026-09-23 — rodapé social com logo à esquerda

Campanhas em que o remetente é o empreendimento (a primeira foi o SAVE & WIN do City Center
Outlet Premium) precisavam assinar o rodapé com o logo e as redes do próprio empreendimento.
O `90-social` só tinha ícones centralizados, com as URLs fixas do Podi. Agora existe um
segundo modelo, e o atual continua sendo o padrão.

### Adicionado

- **`design-system/newsletter/components/90b-social-logo.html`** — logo à esquerda, ícones à
  direita, numa linha só também no mobile. Variante A com o logo Podi verde e as redes
  oficiais do Podi; variante B com o logo do empreendimento e as redes dele, vindas do
  briefing.

### Alterado

- **`components/README.md`** — o bloco novo no catálogo, a regra de obrigatórios aceita
  `90-social` ou `90b-social-logo`, e uma seção nova explica quando usar cada modelo.
- **`templates/newsletter/base.html`** — o comentário de montagem cita os dois modelos.
- **`brand/links-oficiais.md`** — a variante B do `90b` é a única que troca as URLs das redes.
- **`design-system/newsletter/README.md`**, **`docs/estrutura.md`** — contagem de blocos (19).

---

## 2026-09-04 — proibido JavaScript em newsletter

`email-compat.md` já vetava `<script>`, mas não cobria JS disfarçado em atributo
(`onclick`, `onload`) ou `href="javascript:..."`. Clientes de e-mail podem bloquear a
mensagem inteira ao detectar isso, então a regra ficou explícita.

### Alterado

- **`design-system/newsletter/guidelines/email-compat.md`** — seção "Conteúdo e
  entregabilidade" agora proíbe qualquer forma de JavaScript, não só a tag `<script>`.

---

## 2026-09-03 — só três variáveis em e-mail, e nada de descadastro

O servidor de envio do Podi (AWS) resolve apenas `{{email}}`, `{{topicId}}` e
`{{campaignId}}`. Qualquer outra variável no HTML **derruba o envio inteiro** — não é um
campo vazio, é a campanha que não sai. Como não existe variável de descadastro, o link de
descadastro sai das peças.

### Adicionado

- **`design-system/newsletter/guidelines/variaveis-envio.md`** — a tabela do que é
  suportado, a distinção entre placeholder de montagem (`{{MAIUSCULA}}`, substituído antes
  do envio) e variável de envio (minúscula, resolvida pelo servidor), e o `grep` de
  conferência.

### Alterado

- **`91-footer-legal.html`** — sem link de descadastro. O motivo do recebimento continua,
  e o e-mail do destinatário passa a vir de `{{email}}` em vez de
  `{{EMAIL_DESTINATARIO}}`.
- **`brand/README.md`** — a tabela das duas frentes não diferencia mais rodapé por
  descadastro; a diferença passa a ser tom, motivo do recebimento e contato.
- **`CLAUDE.md`**, **`/newsletter-podi`**, **`qa-checklist.md`**, **`docs/como-usar.md`**,
  **`docs/como-enviar-conteudo.md`**, **`examples/briefing-demo/README.md`** — regra nova
  no lugar da antiga; o QA ganhou o item de conferir as variáveis que sobraram no arquivo.
- **Exemplos** em `examples/newsletter/` — rodapés refeitos sem descadastro.

**Ação necessária:** e-mail montado antes desta data e ainda não enviado precisa ter o
`{{URL_DESCADASTRO}}` removido do rodapé — se for enviado como está, a campanha não sai.

---

## 2026-09-01 — briefing de demonstração no repositório

Quem instalava o Marketing OS pela primeira vez não tinha o que montar: `projects/_inbox/`
nasce vazia e não é versionada. Agora o repositório traz um briefing fictício pronto.

### Adicionado

- **`examples/briefing-demo/`** — `brief.md` com cabeçalho de envio e três notícias
  numeradas, mais `imagens/` com as quatro imagens nos nomes e proporções certos
  (`capa.jpg`, `01-`, `02-`, `03-…-1x1`). As imagens são placas de teste em cores dos
  tokens, não fotografia — a direção fotográfica continua valendo só para foto de verdade.
- **Chamadas para a pasta** no `README.md` e no `docs/como-usar.md`.

### Por quê

O primeiro contato com o padrão não pode depender de haver conteúdo real na mão. Com o
briefing de demonstração, a pessoa monta um e-mail completo no mesmo dia em que instala —
e vê o descadastro, o layout lateral do bloco 1:1 e o relatório final funcionando.

---


## 2026-09-01 — guia "Como usar" em Markdown

A apresentação de introdução ao Marketing OS virou documento. O deck continua servindo à
gravação; o Markdown é o que fica no repositório para quem chegar pelo vídeo.

### Adicionado

- **`docs/como-usar.md`** — o conteúdo dos 16 slides em texto: as quatro camadas, a
  instalação, as três skills, o passo a passo do Podi News, as regras não negociáveis e as
  dúvidas frequentes. Começa com um bloco endereçado ao Claude Code, para que ele saiba o
  que fazer quando alguém colar o link do repositório e pedir para preparar a pasta.
- **Link no `README.md`**, no começo do "Como usar" e na referência rápida.

### Por quê

O vídeo pede um destino: a pessoa cola o link, manda ler um documento e o ambiente fica
pronto. Um deck em HTML não serve para isso — o Claude precisa de texto, e quem assistiu
precisa de um lugar para voltar depois.

---


## 2026-09-01 — Podi é sempre masculino

A marca era tratada ora no masculino, ora no feminino. Fica definido: **o Podi**, **do Podi**,
**no Podi**, **pelo Podi**. Nunca "a Podi".

### Alterado

- **Ocorrências no feminino corrigidas** em `brand/`, `design-system/`, `.claude/skills/`,
  `examples/`, `skills/README.md`, `README.md`, `CLAUDE.md` e nas entradas antigas deste
  changelog.

### Por quê

Nome de marca não tem gênero por si — quem define é o uso. O time fala "o Podi", e material
que diga "a Podi" soa como se fosse de outra empresa. Deixar a regra escrita evita que cada
peça decida sozinha.

**Ação necessária:** material já montado que diga "a Podi" ou "da Podi" precisa ser corrigido
no próximo envio.

---


## 2026-09-01 — hero do Podi News passa a ter dark mode

O card de abertura das edições do Podi News era o único do repositório que ficava branco
no dark mode, com o texto sem classe de tema. Agora ele acompanha os cards de notícia.

### Alterado

- **`00-hero-podi-news.html`** — o card externo troca `.dm-logo` por `.dm-surface`:
  no dark ele vai para `#242424`, igual a `11-card-noticia` e `12-card-noticia-compacta`.
- **Texto do hero** ganha as classes que faltavam: `.dm-ink` na headline, `.dm-body` no
  texto de apoio, e `.dm-tag` + `.dm-accent` no eyebrow. O hero deixa de ser a exceção
  em que o texto ficava sem tema.
- **A topbar dos logos** ganhou placa branca própria (`.dm-logo` com raio
  `20px 20px 0 0`), antes herdada do card inteiro.

### Por quê

O card branco fixo destoava do resto da peça no dark mode: a edição abria com um bloco
claro e seguia com cards escuros. A razão original da trava era só o logo da Tacla Labs,
que tem o "Tacla" em preto — e isso se resolve isolando a topbar, sem prender o card todo.

### Limitação conhecida

A topbar **continua branca nos dois modos**. Não existe no repositório uma arte da Tacla
Labs legível sobre fundo escuro (só `brand/assets/header/logo-tacla-labs.png`, com o
"Tacla" preto), e o `email-compat.md` proíbe trocar arquivo de imagem por CSS — a troca
falha no Gmail e no Outlook. Quando a arte negativa existir, a placa sai e a topbar herda
o `.dm-surface` do card.

**Ação necessária:** edições do Podi News já montadas continuam com o hero branco no dark
mode. Para atualizar uma peça, no bloco do hero: trocar `class="dm-logo"` por
`class="dm-surface"` na tabela do card, envolver a `<td>` da topbar em
`bgcolor="#FFFFFF" class="dm-logo"` com `border-radius:20px 20px 0 0`, e acrescentar
`.dm-ink`, `.dm-body`, `.dm-tag` e `.dm-accent` nos textos. Os exemplos em
`examples/newsletter/` ainda estão no padrão antigo.

---

## 2026-09-01 — rodapé legal da newsletter

O rodapé deixou de pedir razão social e endereço, e os links jurídicos passaram a ser fixos.

### Alterado

- **Linha de copyright** do rodapé passa de `© {{ANO}} {{RAZAO_SOCIAL}} · {{ENDERECO}}`
  para `© {{ANO}} - Podi App`. Os dois placeholders sumiram: eram preenchidos à mão a cada
  envio, e é justamente aí que aparecia divergência entre uma newsletter e outra.
- **Política de Privacidade e Termos de Uso** viram URLs fixas no componente, em vez de
  `{{URL_PRIVACIDADE}}` / `{{URL_TERMOS}}`:
  `https://www.podiapp.com.br/politica-privacidade/` e
  `https://www.podiapp.com.br/termos-de-uso.html`. Registradas em `brand/links-oficiais.md`.
- Atualizados junto: `91-footer-legal.html`, os três exemplos em `examples/newsletter/`,
  `qa-checklist.md`, `email-compat.md` e a tabela de frentes em `brand/README.md`.

**Ação necessária:** newsletter já montada em `saida/` e ainda não enviada — troque o
rodapé pelo componente atualizado. Os links antigos `podi.com.br/privacidade` e
`podi.com.br/termos` não existem.

## 2026-09-01 — apresentações e cor secundária

O repositório deixou de cobrir um material só. **Apresentação** entra ao lado de newsletter,
com design system, template e skill próprios — e o roxo que o time já usava nos slides vira
regra escrita.

### Adicionado

- **Cor secundária de marca `#9934FF`** em `brand/README.md`. Ela já existia de fato — nos
  slides do time e como variante de ícone social — mas sem regra escrita, o que na prática
  significa que cada peça decidia sozinha. Agora está definida como **detalhe gráfico**:
  ícone, régua sob título, bullet, borda fina. Nunca texto, nunca título, nunca fundo de
  área grande, nunca sobre o verde (2,4:1).
  O contraste sobre branco passaria em texto (4,9:1) — a regra é mais restritiva **de
  propósito**: o verde é a marca, o roxo é tempero. Sem esse limite, em três campanhas o
  deck vira roxo e deixa de parecer Podi.
- **`design-system/apresentacao/`** — tokens de projeção (corpo a partir de 28px, título de
  slide a 64px), os quatro tokens do roxo, canvas fixo, uso do roxo, ritmo do deck e QA.
  Nasceu ao lado de `newsletter/` e **não herdou nada de e-mail**: aqui flex, grid e `var()`
  são obrigatórios, e as regras de `email-compat.md` não valem.
- **16 tipos de slide** em `design-system/apresentacao/slides/`, do `00-capa` ao
  `15-encerramento`, mais o shell `_slide.html`. Quatro deles — capa, split foto + cards,
  features em duas colunas e mockup de app — são a formalização dos três layouts que o time
  já vinha usando. O padrão **descreve o que existia**; não inventou direção visual nova.
- **`brand/assets/header/logo-podi.svg`** — o logo Podi sozinho, em vetor **monocromático**.
  Não tem cor gravada: a cor vem de fora, por `currentColor`. Era a peça que faltava — os
  PNGs existentes são verdes, e logo verde sobre fundo verde some, o que obrigava a enfiar o
  logo dentro de uma placa branca em toda capa. Agora ele vai branco direto sobre o verde,
  como nos decks que o time já fazia.
  Junto veio a regra em `brand/README.md`: **logo não é texto**. A regra de contraste do
  verde governa palavras; o logo é marca gráfica, e branco sobre o verde é como o Podi
  assina. O que continua proibido é recolorir por `filter` ou por efeito.
- **O rodapé de todo slide é assinado pelo logo**, não pela palavra "Podi". Assinatura de
  marca é a marca; texto no lugar dela é o tipo de detalhe que ninguém nota no slide 3 e
  incomoda no slide 15. Sobre fundo claro o logo é sempre o verde original `#48DB84`, em
  qualquer tamanho: ali ele é assinatura discreta, não alvo de leitura — o mesmo raciocínio
  já escrito para o ícone social verde do rodapé do e-mail.
- **`templates/apresentacao/base.html`** — shell com os tokens no `:root`, canvas de
  1920 × 1080, escala automática para preview na tela e `@page` configurado para o PDF sair
  em paisagem com um slide por página. O logo entra como `<symbol>` carregado uma vez só;
  os slides o usam por `<use href="#logo-podi">`, para o desenho não ser copiado três vezes
  dentro do mesmo arquivo.
- **Skill `/apresentacao-podi`** — lê o briefing, define o roteiro (número, tipo de slide,
  o que ele diz), **confirma o roteiro antes de montar**, monta em `saida/<slug>/` e roda o
  QA. A confirmação do roteiro é o passo que evita o erro caro do material: refazer 18
  slides prontos custa o dobro de discordar de uma lista.
- **Rota `/design`** documentada na skill (§4) e no `CLAUDE.md`. Quem quiser editar o visual
  à mão leva o mesmo conteúdo para o canvas do `/design` — mas **o `/design` não decide
  identidade**: cor, tipografia e uso do roxo vão no briefing do canvas, prontos. Canvas
  fora do sistema se corrige; design system não.

### Alterado

- **`CLAUDE.md`** — a frase "hoje o único material coberto é newsletter" saiu, e duas regras
  não negociáveis entraram: o roxo de detalhe e o canvas fixo de 1920 × 1080.
- **`brand/README.md`** — nova seção "Cor secundária" e o ponteiro de tokens agora aponta
  para os dois materiais.
- **`docs/estrutura.md`, `skills/README.md`, `saida/README.md`** atualizados com a pasta
  nova, a skill nova e o que fazer com o deck pronto (o PDF, e mandar a pasta inteira —
  o HTML sozinho perde as imagens).

### O que ficou de fora, de propósito

- **Export nativo para `.pptx`.** O PDF cobre o uso real e trava a tipografia; um `.pptx`
  gerado substituiria a Inter na máquina de quem abrisse e desmontaria o espaçamento. Quem
  precisa do PowerPoint importa o PDF como imagem de fundo. Deck que precise ser **editado**
  no PowerPoint depois é um pedido diferente — falar com quem cuida do padrão.
- **Subir tokens comuns de newsletter + apresentação para `brand/`.** Agora existem dois
  casos de uso reais, então a promoção finalmente pode ser discutida — mas ela é uma
  mudança estrutural, e mudança estrutural não entra junto com o material que a motivou.
- **`examples/apresentacao/`.** Acervo é curado a partir de trabalho real entregue. O
  primeiro deck montado com o padrão é o candidato natural.

---

## 2026-09-01 — skill de foto e sufixo `-podi`

### Adicionado

- **Skill `/foto-podi`** — escreve o prompt de uma foto de marca a partir de um pedido em
  português: enquadra o pedido nas dimensões obrigatórias, parte de uma das 8 variações
  prontas quando cabe, monta o prompt em inglês com o bloco `STYLE LOCK` copiado sem edição,
  roda o checklist e entrega as duas versões (com e sem campo de negative). Fecha a lacuna
  aberta na entrada anterior: `brand/photography/` dizia **o que é permitido**, e não havia
  nada dizendo **como executar**.
  A skill **referencia** o Style Lock; não copia trechos dele. Direção visual continua tendo
  uma fonte só.
- **`saida/fotos/NNN-slug.md`** — onde os prompts entregues ficam guardados. É o histórico do
  ensaio: dá para repetir uma foto meses depois e reaproveitar a seed. Como todo `saida/`,
  é local e fora do Git.

### Alterado

- **Toda skill oficial passa a terminar em `-podi`.** `/newsletter` virou **`/newsletter-podi`**;
  a skill nova já nasceu `/foto-podi`. A ferramenta de IA traz dezenas de comandos próprios —
  sem o sufixo, na hora de digitar não dá para saber qual é o padrão da marca.
  **Ação necessária:** quem já usava `/newsletter` passa a digitar `/newsletter-podi`. O
  material montado antes não muda em nada.
- **`skills/README.md`, `README.md`, `projects/README.md`, `docs/como-enviar-conteudo.md`,
  `docs/estrutura.md`, `CLAUDE.md` e `scripts/check-atualizacao.sh`** atualizados com o nome
  novo e com a regra do sufixo escrita, para skill nova já nascer certa.
- **`saida/README.md`** deixou de falar só em newsletter: agora a pasta recebe dois tipos de
  saída.
- **`brand/photography/README.md`** — a seção "o que ainda não existe" virou o ponteiro para
  a `/foto-podi`.

---

## 2026-09-01 — direção fotográfica

### Adicionado

- **`brand/photography/`** — a direção fotográfica do Podi passa a ser diretriz oficial de
  Brand, no mesmo nível da cor e do logo. Contém o `STYLE-LOCK-PODI.md` migrado íntegro do
  repositório de fotografia, as 5 referências que o originaram e um `README.md` dizendo o
  que ali é normativo (DNA, tradução para interior, blocos STYLE LOCK, checklist, verde) e
  o que é ferramenta de execução (fórmula de slots, suíte de prompts, negative por gerador).
  Está em `brand/` e não em `design-system/` porque vale para qualquer material — e-mail,
  post, impresso —, não só para e-mail.
- **Regra não negociável no `CLAUDE.md`** — não se inventa direção visual nova, e o bloco
  `STYLE LOCK` se copia sem editar uma palavra. Parafrasear o bloco é o erro que ninguém
  percebe até ter quarenta imagens desalinhadas entre si.

### Alterado

- **O verde da fotografia ficou decidido: `#48DB84`.** O Style Lock vinha operando com o hex
  oficial "a confirmar" — o Marketing OS já o tinha. Os termos `vivid emerald green` /
  `deep pine green` / `soft mint green` ficam confirmados como a tradução desse verde para o
  vocabulário dos geradores; as variantes lime e jade continuam no §8 só como registro do que
  foi descartado.
- **Skill `/newsletter`** passou a apontar o Style Lock para o caso de o briefing pedir uma
  **foto que ainda não existe**. As imagens que chegam em `_inbox/` **não** ganharam critério
  de aceite fotográfico: muitas são print de tela ou montagem gráfica, e para elas o critério
  continua sendo só formato e proporção.
- **`brand/README.md` e `docs/estrutura.md`** ganharam a seção e a linha correspondentes.

### O que ficou de fora, de propósito

- O `CLAUDE.md` do repositório de origem. Ele é o manual de uma fábrica de prompts — formato
  de entrega, numeração de arquivo, `--sref`/`--seed`/`--cref`. Isso é procedimento de skill,
  não Brand, e colide com a linguagem não técnica deste repositório.
- A pasta `prompts/` de origem: é saída de projeto, equivalente ao `saida/` daqui.
- Uma skill `/foto`. É **proposta**, registrada no `brand/photography/README.md` — não padrão.

---

## 2026-09-01 — Podi Marketing OS

O repositório deixou de ser "as newsletters do Podi" e passou a ser o **Podi Marketing OS**:
a base oficial de padrões para todo material de Marketing, Design e Publicidade. Newsletter
continua sendo o único material coberto — o que mudou foi a arrumação, para que um segundo
tipo de material caiba sem herdar as limitações de e-mail.

**Ação necessária:** todos os caminhos mudaram. Se você tem uma cópia antiga, ela vai ser
atualizada sozinha na próxima montagem. Se você tinha algo salvo fora de `saida/`, confira
antes.

### Adicionado

- **Camada `brand/`** — identidade Podi separada do design system: cor de marca e regra de
  contraste, as duas frentes (cliente/interno) com tom e rodapé, logos e ícones, e
  `links-oficiais.md` com o link do app, as URLs sociais e a imagem do fecho.
  Existe porque a regra do `#48DB84` vale para qualquer material, e as regras de tabela e
  VML valem só para e-mail. Misturadas, todo material novo herdaria limitação de Outlook.
- **`docs/governanca.md`** — quem altera o quê, a hierarquia de autoridade
  (Brand → Design System → Templates → Skills → Projeto), e como propor mudança sem editar
  recurso oficial. No MVP o único maintainer é Bruno Pinheiro.
- **`docs/estrutura.md`** — mapa comentado do repositório, com o porquê de cada separação.
- **READMEs de camada** — `brand/`, `design-system/newsletter/`,
  `design-system/newsletter/components/` (catálogo dos 18 blocos + regras do header do
  Podi News), `projects/`, `skills/`.
- **Regra "não invente padrão"** — quando falta algo no sistema, a IA identifica a ausência,
  monta o resto e relata como **proposta** explicitamente marcada. Proposta não vira padrão
  sozinha.
- **Regra de conflito** — pedido que contraria uma camada superior é **sinalizado**, não
  executado silenciosamente.

### Alterado

- **Estrutura de pastas**, com tudo movido:
  | Antes | Agora |
  |---|---|
  | `assets/header/`, `assets/icones/`, `assets/end-news-img.jpg` | `brand/assets/…` |
  | `templates/tokens.md` | `design-system/newsletter/tokens.md` |
  | `templates/sections/` | `design-system/newsletter/components/` |
  | `templates/base.html` | `templates/newsletter/base.html` |
  | `docs/qa-checklist.md` | `design-system/newsletter/guidelines/qa-checklist.md` |
  | `refs/` | `design-system/newsletter/guidelines/refs/` |
  | `content/_inbox/` | `projects/_inbox/` |
  | `examples/<slug>/` | `examples/newsletter/<slug>/` |
  Os `src` dos três exemplos e dos componentes foram reescritos junto.
- **`CLAUDE.md` reescrito como camada global.** As regras específicas foram para onde
  pertencem: compatibilidade de e-mail (§3) → `design-system/newsletter/guidelines/email-compat.md`;
  ritmo visual (§5) → `layout-ritmo.md`; frentes e contraste (§4) → `brand/README.md`;
  ativos fixos (§4b) → `brand/links-oficiais.md`; fluxo e nome de imagem (§2/§2a) → a skill.
  As não negociáveis ficaram repetidas na raiz de propósito — errar nelas custa caro demais
  para depender de um clique a mais.
- **Comando `/nova-newsletter` virou `/newsletter`.** O "nova" descrevia o momento, não o
  material — e num OS multi-material o nome do material é o que identifica a skill.
- **`README.md` reescrito** para quem não é técnico: o que é o OS, para quem, o que é
  oficial, governança e como propor mudança.
- **`scripts/check-atualizacao.sh`** passou a vigiar `brand/`, `design-system/` e
  `templates/` como caminhos críticos.
- **`.gitignore`** passou a ignorar `projects/_inbox/` e `*.zip` — material bruto do time
  não infla o histórico do repositório.

### Removido

- **`content/31082026_atualizacoes/`** — 3 MB de PNGs de briefing já consumido, fora da
  convenção de nome e duplicando as imagens já convertidas em
  `examples/newsletter/2026-08-podi-atualizacoes-app/assets/`.
- **`refs/exemplo-de-conteudo.html`** — e-mail salvo pelo Apple Mail. Continha caminho
  absoluto da máquina de origem, `<script>` e fontes inline; o padrão que ele
  representava já foi superado pelos três exemplos atuais.
- **`assets/logo-podi.png` e `assets/logo-tacla-labs.png`** da raiz — duplicatas órfãs
  dos arquivos de `assets/header/`, que são os realmente usados.

---

## 2026-09-01 — padrão de newsletter

### Adicionado

- **Bloco `00-hero-podi-news.html`** — header combinado das edições do Podi News:
  card branco único com topbar de logos, imagem da edição e eyebrow + headline +
  texto de apoio. Vindo do Figma `Podi-News-26-27`, node `1:422`.
  **Ação necessária:** toda edição do Podi News passa a usar este bloco. A combinação
  antiga (`01-header` + `02a` + `02` + `03` soltos) só vale para as outras frentes.
- **Pasta `saida/`** — é onde o e-mail montado é gravado a partir de agora, no lugar
  de `examples/`. Fica fora do Git: o trabalho é local de cada pessoa.
  `examples/` vira acervo curado, gravado só pelo dono do repositório.
- **Guia `docs/como-enviar-conteudo.md`** — para quem escreve: formato do documento,
  nomenclatura das imagens e proporções exigidas.
- **Comando `/nova-newsletter <slug>`** — monta a newsletter a partir de
  `content/_inbox/<slug>/`, conferindo antes se o clone está atualizado.
- **Convenção de nome de imagem** (CLAUDE.md §2a): `capa.*`, `NN-nome.*` para imagem
  no topo em largura inteira (16:9 ou mais panorâmica) e `NN-nome-1x1.*` para imagem
  ao lado do texto (quadrada). Fora da proporção, o Claude relata em vez de recortar.
- **Papéis de tipografia faltando** em `tokens.md`: número de destaque (32/38/600) e
  label de número (14/20/400), que o `08-destaque-numeros` já usava sem estar escrito.

### Alterado

- **Ícones sociais agora são os verdes** (`assets/icones/*-green.png`), por decisão de
  marca, no lugar dos roxos. Contraste de 1,63:1 sobre a página clara contra 4,5:1 do
  roxo — no modo claro o ícone é ornamento, e o que sustenta o link é o `alt`.
  **Ação necessária:** newsletters montadas antes desta data ainda apontam para
  `*-roxo.png`. Se for reenviar alguma, trocar o sufixo.
- **Link do botão de baixar o app** é fixo: `https://podi.podiapp.com.br/podi-e931a`.
  Substitui o `podi.com.br/app` que estava nos exemplos e não existia.
  **Ação necessária:** conferir esse `href` em qualquer e-mail ainda não disparado —
  ele aparece em dois lugares no botão, no `<v:roundrect>` e no `<a>`.
- **Imagem do fecho "Podi e você"** é sempre `assets/end-news-img.jpg`, nunca uma arte
  nova nem cópia dentro da pasta do envio.
- **URLs dos ícones sociais** fixadas direto no `90-social.html`, no lugar dos
  placeholders `{{URL_*}}`. Os exemplos estavam com endereços inventados.
- **Piso de 15px** no QA passou a citar as exceções reais — legal 12px, eyebrow 12px,
  label de número 14px. Antes falava em "legendas de 13px", tamanho que não existe
  em nenhum bloco.
- `&display=swap` do Google Fonts escapado como `&amp;` no `base.html`, para o arquivo
  bater com o doctype XHTML que ele declara.

### Removido

- Pasta `design-system/` e o ambiente virtual `.venv-x/`, que não participavam da
  montagem de e-mail.

---

## Como escrever uma entrada

Uma seção por data, com `Adicionado` / `Alterado` / `Removido`. Cada item diz o que
mudou e **por quê** — daqui a seis meses o porquê é a única parte que não dá para
deduzir do diff. Marcar `**Ação necessária:**` quando algo já montado precisar ser
revisto.
