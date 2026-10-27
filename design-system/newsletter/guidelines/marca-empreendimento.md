# Modo empreendimento — e-mail com a marca do shopping

A estrutura de e-mail do Podi, com as mesmas regras técnicas, mas com o **logo, as cores e
as redes do empreendimento** no lugar das do Podi. Serve para peças em que o remetente é o
empreendimento (shopping, outlet) ou uma campanha dele.

Origem: campanha **SAVE & WIN** do City Center Outlet Premium (setembro de 2026), sete
e-mails de gatilho montados à mão. O que foi decidido nela virou esta regra.

Exemplo curado: [`examples/newsletter/2026-09-empreendimento-save-win/`](../../../examples/newsletter/2026-09-empreendimento-save-win/)
— dois dos sete e-mails, remontados com os componentes deste modo.

Autoridade: a permissão para tirar o verde Podi nasce em
[`brand/podi/README.md`](../../../brand/podi/README.md#peças-com-marca-do-empreendimento). Este arquivo
só diz como aplicar.

---

## Quando é este modo

**O remetente não é o Podi.** O briefing diz `Remetente: <empreendimento>`, ou a campanha é
assinada pelo shopping. Se o remetente for o Podi — mesmo falando de um shopping —, a peça é
Podi normal, com `01-header`, verde e dark mode.

Na dúvida, perguntar. É a única pergunta sobre o formato: cabeçalho, rodapé e modo claro o
modo já decide.

## O que muda

| | Podi | Modo empreendimento |
|---|---|---|
| Template | `templates/newsletter/base.html` | `templates/newsletter/base-empreendimento.html` |
| Cabeçalho | `01-header` (Podi + Tacla Labs) | `01b-header-empreendimento` |
| Rodapé social | `90-social` ou `90b` variante A | `90b-social-logo` **variante B** |
| Grupo verde da paleta | tokens do Podi | derivado da cor base (abaixo) |
| Ícones sociais | `brand/podi/assets/icones/*-green.png` | recoloridos para a cor base, em `saida/<slug>/imagens/icones/` |
| Dark mode | bloco `prefers-color-scheme` + classes `dm-*` | **sempre claro**, sem bloco e sem `dm-*` |
| Roxo de detalhe `#9934FF` | permitido como detalhe | não entra — é cor da Tacla Labs |

- **Cabeçalho:** logo do empreendimento centralizado numa placa branca de raio 20px, padding
  32px 28px. Logo colorido para fundo claro, 24px de altura, até 150px de largura,
  exportado em 2x (arquivo 300 × 48 para 150 × 24).
- **Rodapé social:** `90b` variante B, com o mesmo arquivo de logo do cabeçalho e as redes
  **do empreendimento**, vindas do briefing. Nunca misturar com as do Podi.
- **Ícones sociais:** a mesma forma dos `-green.png`, pintada com a cor base a partir do
  canal alfa. Quem gera é o script; o PNG fica na pasta do envio e **nunca é gravado em
  `brand/`**. Só existem ícones para as redes que têm `-green.png` oficial (Instagram,
  Facebook, LinkedIn, Spotify).

## O que não muda

Vale integralmente, como em qualquer peça do Podi:

- [`email-compat.md`](email-compat.md): tabelas, CSS inline, CTA em VML, imagens JPG/PNG em 2x.
  A única seção que não se aplica é a de dark mode.
- Tipografia, espaçamento e raios de [`tokens.md`](../tokens.md), os limites de
  [`layout-ritmo.md`](layout-ritmo.md) e o [`qa-checklist.md`](qa-checklist.md).
- Rodapé legal `91-footer-legal`: `© <ano> - Podi App`, motivo do recebimento, Política de
  Privacidade e Termos de Uso. O **texto legal da promoção** entra antes do `©`, dentro do
  mesmo bloco, em 12/18 na cor `muted` — o lugar está marcado no componente.
- **Nenhum link de descadastro** ([`variaveis-envio.md`](variaveis-envio.md)).
- O link do app (`https://podi.podiapp.com.br/podi-e931a`), "o Podi" no masculino e a
  hierarquia de autoridade.

---

## Estrutura da peça

Nesta ordem — é a estrutura que o SAVE & WIN validou:

| # | Bloco | Componente |
|---|---|---|
| 1 | Cabeçalho do empreendimento | `01b-header-empreendimento` |
| 2 | Imagem hero da campanha | `03-hero-image` (536 × auto, arquivo mínimo 1072) |
| — | espaçador 32px | `99-spacer` |
| 3 | Destaque: o número principal | `08-destaque-numeros` **variante B · 1 coluna** — rótulo 16px em cima, número 32px embaixo |
| — | espaçador 16px | `99-spacer` |
| 4 | Card de conteúdo único | `13-card-conteudo` com os itens dentro |
| — | espaçador 40px | `99-spacer` |
| 5 | Rodapé social | `90b-social-logo` variante B |
| 6 | Texto legal + rodapé legal | `91-footer-legal` |

**Dentro do card único** (itens do `13`, `13a` e `13b`, na ordem do conteúdo):

- texto de abertura;
- título de grupo, card title 20/26;
- lista com marcador `&bull;` na cor `accent-ink`;
- galeria de 2 colunas (`13a`): imagem 1:1 exibida a 224px (arquivo mínimo 448 × 448),
  texto embaixo e etiqueta opcional; empilha no mobile;
- extrato de dados (`13b`): rótulo à esquerda, valor à direita, linha fina entre linhas;
- **linha fina** entre grupos e **sempre antes do botão**;
- **um CTA**, no fim.

O card único conta como **uma** seção no limite de quatro do `layout-ritmo.md`.

---

## Paleta derivada da cor base

Só o grupo verde muda. `ink` `#101010`, `body` `#4A4A4A`, `muted` `#6E6E6E` e o branco
`#FFFFFF` ficam como estão.

| Token Podi | Papel | No modo empreendimento |
|---|---|---|
| `#48DB84` brand | fundo do CTA, ícones | a cor base |
| `#0C6E3B` accent-ink | número de destaque, marcador, texto de etiqueta, link de marca | a cor base; se não passar 4,5:1, escurecida em OKLab até passar |
| `#EDF7F1` page/canvas | fundo | derivado |
| `#D4F0DF` accent-soft | faixa do destaque, fundo de etiqueta | derivado |
| `#D2E7DA` hairline | linhas finas | derivado |

**Derivado** = mesma claridade OKLab (L) do token original do Podi, matiz (H) da cor base e
**60% da saturação (C) do token original do Podi**. Se a cor sair do sRGB, a saturação é
reduzida até caber (gamut clamp), mantendo L e H.

**accent-ink escurecido:** mantém matiz e saturação da base e baixa a claridade OKLab até
passar 4,5:1 sobre `page` **e** sobre `accent-soft` — os dois fundos em que ele aparece.
`accent-soft` é o mais escuro, então é ele que decide.

**Texto do CTA:** `#FFFFFF` se der ≥ 4,5:1 sobre a base; senão `#101010`. Aqui quem decide é
o contraste medido. A regra "nunca texto branco sobre o verde" continua valendo para o
`#48DB84` — ele simplesmente não está nesta peça.

### Contrastes obrigatórios — bloqueiam a montagem

| Par | Mínimo |
|---|---|
| `muted` sobre `page` | 4,5:1 |
| `accent-ink` sobre `page` | 4,5:1 |
| `accent-ink` sobre `accent-soft` | 4,5:1 |
| texto do CTA sobre a base | 4,5:1 |

Reprovou: não montar. Pedir outra cor base ao empreendimento.

**Base neutra** (preto, cinza, branco — saturação OKLab abaixo de 0,02) também bloqueia: sem
matiz não há de onde derivar a paleta, e ainda não existe regra para esse caso. Avisar o
maintainer.

### O script — a conta nunca é refeita à mão

```bash
python3 scripts/paleta-empreendimento.py "#173B2A" <slug>
```

Imprime os tokens, os contrastes e a tabela de troca; sai com erro se algum contraste
reprovar; gera os ícones em `saida/<slug>/imagens/icones/<rede>-campanha.png`. Sem o
`<slug>`, só calcula. Só biblioteca padrão do Python — nada para instalar.

Depois de montar, a conferência (só leitura):

```bash
python3 scripts/paleta-empreendimento.py "#173B2A" --conferir saida/<slug>/*.html
```

Ela acusa cor do Podi sobrando, cor fora da paleta derivada, falta do `light only`, bloco de
dark mode, classe `dm-*`, ícone apontando para `brand/`, rede ou logo do Podi, e texto do CTA
diferente do que o contraste decidiu.

### Conferência de referência — SAVE & WIN, base `#173B2A`

| Token | Hex | Contraste |
|---|---|---|
| brand / accent-ink | `#173B2A` | 11,3:1 sobre page · 10,2:1 sobre accent-soft |
| page | `#F0F6F2` | muted 4,65:1 |
| accent-soft | `#DCEDE3` | |
| hairline | `#D8E5DD` | |
| texto do CTA | `#FFFFFF` | 12,4:1 sobre a base |

Se o script um dia devolver outra coisa para `#173B2A`, é o script que está errado.

---

## Como montar

1. Rodar o script com a cor base e o slug. Reprovou → parar.
2. Copiar `templates/newsletter/base-empreendimento.html` para `saida/<slug>/<arquivo>.html`.
3. Colar os blocos na ordem da tabela acima. Os componentes vêm com os tokens e as classes
   do Podi, porque também servem às peças do Podi.
4. **Trocar as cores** do grupo verde pela tabela de troca que o script imprimiu — em todo
   o arquivo, inclusive o fundo da página. Se o texto do CTA for branco, trocar
   `color:#101010` por `color:#FFFFFF` **só nas duas metades do botão** (`<center>` do VML e
   `<a>`): o `#101010` também é a cor dos títulos.
5. **Tirar todas as classes `dm-*`.**
6. Trocar o `src` dos ícones do `90b` por `imagens/icones/<rede>-campanha.png`.
7. Rodar o `--conferir` e o `qa-checklist.md`.

---

## Limitação: sempre modo claro

Os tokens de dark mode do Podi (`#1A1A1A`, `#6FE9A2`, `#16281E`…) são derivados do verde
Podi, e ainda não existe regra para derivá-los de outra cor. Por isso a peça declara
`color-scheme: light only` e não tem bloco de dark mode nem classes `dm-*`.

O que isso **não** garante: o app do Gmail e parte das versões do Outlook ignoram o aviso e
invertem as cores por conta própria. Nesses clientes a peça pode aparecer escurecida, com a
cor base e a placa branca do logo recalculadas por eles. Não há como impedir isso em HTML
de e-mail — é o custo conhecido do modo, até existir uma regra de dark mode derivada.
