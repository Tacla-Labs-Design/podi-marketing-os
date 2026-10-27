---
name: apresentacao-podi
description: Monta uma apresentação, deck ou slide do Podi em 16:9 a partir de um briefing em projects/_inbox/<slug>/, seguindo o design system de apresentação. Use quando pedirem para gerar, montar ou criar uma apresentação, um deck, um pitch, um slide ou um PowerPoint do Podi.
---

# Montar uma apresentação Podi

Argumento: o slug da pasta em `projects/_inbox/`. Sem argumento, listar as pastas
disponíveis e perguntar qual. Se não houver briefing em pasta nenhuma, o assunto pode vir
direto da conversa — mas o roteiro (§2) continua obrigatório.

Esta skill é o **procedimento**. As regras que ela obedece estão em outros lugares e valem
integralmente:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/README.md`, `brand/links-oficiais.md`, `brand/marca.json` | Identidade, contraste, o roxo de detalhe, CTA e textos fixos |
| Brand | `brand/photography/STYLE-LOCK-PODI.md` | Direção fotográfica — só quando a peça pedir **foto nova** |
| Design System | `design-system/apresentacao/` | Tokens, os 16 tipos de slide, canvas, roxo, ritmo, QA |
| Template | `templates/apresentacao/base.html` | O shell |

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
  Se não atualizou nada, não comente.
- **Saída 1** → houve alteração local conflitante. **Parar.** Dizer que esta cópia do
  padrão está diferente da oficial e que é preciso avisar quem cuida do repositório.

## 1. Ler tudo antes de decidir qualquer coisa

```bash
ls -R projects/_inbox/<slug>/
```

- `.docx` → `textutil -convert txt -stdout arquivo.docx`
- `.pdf` → `pdftotext arquivo.pdf -`
- `.pptx` → `textutil -convert txt -stdout arquivo.pptx`, e **abrir as imagens** que vierem
- `.zip` → `unzip -o arquivo.zip -d projects/_inbox/<slug>/imagens/`
- Imagens → **abrir de fato** com a tool Read. Nome de arquivo não é prova de conteúdo, e
  você precisa da proporção real para escolher o slide.

Antes de montar, saber três coisas. Se o briefing não disser, **perguntar**:

1. **Para quem** — cliente/prospect, shopping parceiro, ou time interno.
2. **Quanto tempo** — 5 minutos são ~8 slides; 20 minutos, ~20. É o teto de slides.
3. **Qual é o pedido** — o que a plateia deve fazer no fim. É o `15-encerramento`.

## 2. Definir o roteiro — e confirmar antes de montar

Escreva o roteiro como uma lista: **número, tipo de slide, o que ele diz em uma frase.**

```
01  00-capa               Podi para o Shopping X
02  01-agenda             o que vamos ver
03  03-titulo-texto       o problema: o shopping não sabe quem entra
04  08-numeros            105 mil cadastros no último ano
...
```

O tipo se escolhe pelo **formato da informação**, não pela vontade de variar — a tabela de
decisão está em `design-system/apresentacao/slides/README.md`.

**Mostre o roteiro e espere a pessoa confirmar antes de montar.** Deck errado é caro:
refazer 18 slides depois de prontos é o dobro do trabalho de discordar de uma lista.

Respeite os limites de `guidelines/layout-ritmo.md` — 20 slides, ~60 palavras por slide,
4 cards por grade, um divisor de seção a cada 4 a 6 slides.

## 3. Montar

1. Copiar `templates/apresentacao/base.html` para **`saida/<slug>/index.html`** e trocar o
   `{{TITULO_DA_APRESENTACAO}}` do `<title>`.
2. Copiar os slides escolhidos de `design-system/apresentacao/slides/` para dentro do
   `<div class="deck">`, na ordem do roteiro, e preencher os `{{PLACEHOLDER}}`.
   Os fixos saem de `brand/marca.json`: `{{TAGLINE}}` ← `textos.tagline`,
   `{{CTA_URL}}` ← `links.cta`, `{{CTA_TEXTO}}` ← `textos.cta_deck`, `{{REDE}}` ← `textos.rede_deck`.
   `{{SEM_MARCA}}`/`{{COM_MARCA}}` do `11-comparativo` levam "Podi".
   Nunca gravar em `examples/` — aquilo é acervo curado.
3. Criar `saida/<slug>/assets/` e colocar ali **todas** as imagens, inclusive as fixas
   copiadas de `brand/assets/`. O deck precisa abrir sozinho se alguém mandar a pasta.
4. Trocar os `<svg>` genéricos dos chips pelo glifo certo do assunto, mantendo
   `fill="currentColor"`.
   O **logo Podi não é imagem**: é o `<symbol>` que já vem no template, usado por
   `<use href="#logo-marca">`. A cor sai do CSS — branco sobre o verde e sobre o preto,
   `logo--marca` sobre fundo claro. Nunca trocar por PNG, nunca recolorir por `filter`.
5. **Nunca escrever cor solta.** Toda cor sai de `design-system/apresentacao/tokens.md`,
   por `var(--token)`.
6. **O roxo é só detalhe** — `guidelines/uso-do-roxo.md`. No máximo 3 por slide, nunca em
   texto, nunca sobre o verde.
7. Numerar os slides no rodapé e conferir se o link do app é o oficial (`links.cta`).

Proporção de imagem fora do esperado: **não distorça e não corte por conta própria.**
Monte o resto e relate no fim — qual arquivo, qual proporção veio, qual era esperada.

## 4. A rota `/design`

Quando a pessoa quiser **editar o visual à mão** em vez de receber o HTML pronto, o mesmo
conteúdo vai para o comando `/design` do Claude, como artboards de **1920 × 1080**.

O que não pode escapar: **o `/design` não decide nada de identidade.** Ele recebe as
decisões prontas. Ao chamar, passe no briefing do canvas, explicitamente:

- Os tokens de `design-system/apresentacao/tokens.md` — os hex, não os nomes.
- Canvas 1920 × 1080, margem de segurança de 96px.
- Inter, dois pesos, e a escala tipográfica inteira.
- As duas regras de contraste: texto sobre o verde é `#101010`, **nunca branco**; o roxo
  `#9934FF` é **só detalhe gráfico**, nunca texto, nunca sobre o verde.
- O logo do Podi, em SVG (`brand/assets/header/logo-podi.svg`).
- O roteiro do §2, com o tipo de slide de cada artboard.

Se o canvas voltar com cor, fonte ou uso de roxo fora do sistema, **é o canvas que se
corrige**, não o design system.

As duas rotas convivem: o HTML em `saida/<slug>/index.html` continua sendo a versão
canônica e a que vira PDF. Rodar as duas para o mesmo deck é normal.

## 5. Quando falta algo no sistema

Se o conteúdo pede um tipo de slide, uma cor ou um layout que não existe:

1. **Não invente.** Não crie uma cor nova, não improvise um slide com CSS solto.
2. Verifique se um dos 16 tipos resolve com outro conteúdo.
3. Se realmente não resolve, monte o resto do deck e **relate a ausência no fim**, marcada
   explicitamente como **proposta**: o que falta, em qual slide seria usado, o que sugere.
4. Proposta não vira padrão sozinha. Quem decide é o maintainer (`docs/governanca.md`).

Se o briefing pedir uma **fotografia que ainda não existe**, a direção visual não se
inventa: ela está em `brand/photography/STYLE-LOCK-PODI.md`. Relate o que falta e aponte o
Style Lock — ou monte o prompt com `/foto-podi`.

Se o pedido conflita com o brand — outra cor, texto branco sobre o verde, título roxo,
outro logo — **sinalize o conflito** em vez de alterar a identidade. Explique a regra em
uma frase e ofereça a alternativa que respeita o sistema. Se a pessoa reafirmar, é decisão
dela: diga que a peça sai fora do padrão e siga.

## 6. QA e entrega

Rodar `design-system/apresentacao/guidelines/qa-checklist.md` inteiro antes de dizer que
está pronto. Os itens verificáveis por comando:

```bash
f=saida/<slug>/index.html
python3 -I scripts/conferir.py $f                   # saída 0, e "N slides" = o roteiro
grep -c 'color:var(--accent-2)' $f                  # só chip de ícone e aspas do 10
grep -c 'podi.com.br/app' $f                        # 0 — endereço não existe
```

O `conferir` lê a peça sem os comentários e confere: nenhum `{{...}}`, toda imagem com `alt`
e dentro de `assets/`, cor só da paleta do Podi, nada de verde ou `var(--accent)` como cor de
texto (fora do `.logo--marca`), nenhum "a Podi" — e diz quantos slides há.

Gerar o PDF:

```bash
python3 -I scripts/exportar.py pdf saida/<slug>/index.html   # → saida/<slug>/<slug>.pdf
```

Se ele disser que a fonte não carregou, dizer em português comum: *"a fonte do deck (Inter)
não carregou — ela vem da internet; confira a conexão e me avise para gerar de novo"*. Não
gerar com outra fonte.

Depois abrir o PDF (ou a peça no navegador) e conferir de olho: nenhum slide cortado, nada
fora da margem, o PDF sai em paisagem com um slide por página.

Relatar sempre: caminho do arquivo, **quantos slides e quais tipos**, imagens a hospedar
ou a substituir com a dimensão final, onde está o PDF, e **o que do briefing não coube no
padrão** — dizendo explicitamente o que ficou de fora e por quê.
