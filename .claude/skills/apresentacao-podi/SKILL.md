---
name: apresentacao-podi
description: Monta uma apresentação, deck ou slide do Podi em 16:9 a partir de um briefing em projects/_inbox/<slug>/, seguindo o design system de apresentação. É também o procedimento do /apresentacao-optimall. Use quando pedirem para gerar, montar ou criar uma apresentação, um deck, um pitch, um slide ou um PowerPoint do Podi.
---

# Montar uma apresentação Podi (ou Optimall)

Argumento: o slug da pasta em `projects/_inbox/`. Sem argumento, listar as pastas
disponíveis e perguntar qual. Se não houver briefing em pasta nenhuma, o assunto pode vir
direto da conversa — mas o roteiro (§2) continua obrigatório.

Esta skill é o **procedimento**. As regras que ela obedece estão em outros lugares e valem
integralmente:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/README.md` | Regras comuns às marcas, e qual marca é a peça |
| Brand | `brand/<marca>/README.md`, `links-oficiais.md`, `marca.json` | Identidade, contraste, secundária de detalhe, CTA e textos fixos |
| Brand | `brand/<marca>/photography/STYLE-LOCK-<MARCA>.md` | Direção fotográfica — só quando a peça pedir **foto nova** |
| Brand | `brand/optimall/mensagens.md` | *(Optimall)* O que dizer: números oficiais, módulos, voz, frases aprovadas |
| Design System | `design-system/apresentacao/` | Canvas, ritmo, QA — comuns às duas marcas |
| Design System | Podi: `tokens.md` + `slides/` · Optimall: `optimall/tokens.md` + `optimall/slides/` | A biblioteca de slides **da marca** |
| Template | Podi: `templates/apresentacao/base.html` · Optimall: `templates/apresentacao/base-optimall.html` | O shell |

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

## 0b. Qual marca

O procedimento é um só e serve a duas marcas — Podi e Optimall (`brand/README.md`). Cada
marca tem a **própria biblioteca de slides**:

| | Podi | Optimall |
|---|---|---|
| Slides | `design-system/apresentacao/slides/` (16 tipos) | `design-system/apresentacao/optimall/slides/` (14 tipos) |
| Tokens | `design-system/apresentacao/tokens.md` | `design-system/apresentacao/optimall/tokens.md` |
| Template | `templates/apresentacao/base.html` | `templates/apresentacao/base-optimall.html` |
| Recolorir no fim | — | **Não.** O deck já nasce na paleta do Optimall |

Nunca misturar: slide do Podi não entra em deck do Optimall, nem o contrário.

- Chamado por **`/apresentacao-optimall`**, ou briefing com `Marca: Optimall` → **Optimall**.
- Qualquer outro caso → **Podi**. Se o deck fala de venda B2B para shopping e não diz a
  marca, perguntar.

Daqui em diante, `<marca>` é `podi` ou `optimall`, e **tudo que é de marca sai de
`brand/<marca>/`**: identidade (`README.md`), CTA e textos fixos (`links-oficiais.md`,
`marca.json`), Style Lock.

**Optimall**, antes de seguir:

```bash
python3 scripts/aplicar-marca.py validar optimall
```

Saída diferente de 0 → **parar** e dizer, em português comum: *"a identidade do Optimall
ainda não está completa no padrão — avise quem cuida do repositório"*. Não montar com as
cores do Podi "por enquanto". Deck do Optimall **não cita o Podi nem a Tacla Labs**.

O deck do Optimall é **sempre B2B**: fala com quem decide no shopping. O texto sai de
`brand/optimall/mensagens.md` — números só os oficiais de lá, CTA *Fale com um consultor*,
sempre "o Optimall". Os slides da biblioteca já vêm com o texto aprovado do deck comercial:
num deck comercial padrão, boa parte fica como está.

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
decisão está em `design-system/apresentacao/slides/README.md` (Podi) ou
`design-system/apresentacao/optimall/README.md` (Optimall). No Optimall o fecho é o
`11-encerramento`.

**Mostre o roteiro e espere a pessoa confirmar antes de montar.** Deck errado é caro:
refazer 18 slides depois de prontos é o dobro do trabalho de discordar de uma lista.

Respeite os limites de `guidelines/layout-ritmo.md` — 20 slides, ~60 palavras por slide,
4 cards por grade, um divisor de seção a cada 4 a 6 slides.

## 3. Montar

1. Copiar o template da marca (`base.html` ou `base-optimall.html`) para
   **`saida/<slug>/index.html`**.
2. Copiar os slides escolhidos da biblioteca da marca para dentro do `<div class="deck">`, na
   ordem do roteiro, e preencher os `{{PLACEHOLDER}}` (no Optimall, trocar o texto aprovado pelo
   do roteiro onde ele mudar, mantendo o formato).
   Os fixos por marca saem de `brand/<marca>/marca.json`: `{{TAGLINE}}` ← `textos.tagline`,
   `{{CTA_URL}}` ← `links.cta`, `{{CTA_TEXTO}}` ← `textos.cta_deck`, `{{REDE}}` ← `textos.rede_deck`.
   `{{SEM_MARCA}}`/`{{COM_MARCA}}` do `11-comparativo` levam o nome da marca.
   Nunca gravar em `examples/` — aquilo é acervo curado.
3. Criar `saida/<slug>/assets/` e colocar ali **todas** as imagens, inclusive as fixas
   copiadas de `brand/<marca>/assets/`. O deck precisa abrir sozinho se alguém mandar a pasta.
4. Trocar os `<svg>` genéricos dos chips pelo glifo certo do assunto, mantendo
   `fill="currentColor"`.
   O **logo não é imagem**: é o `<symbol>` que já vem no template. No Podi,
   `<use href="#logo-marca">`, e a cor sai do CSS — branco sobre a cor de marca e sobre o
   preto, `logo--marca` sobre fundo claro. No Optimall, o logo é tricolor: `#logo-optimall-negativo`
   sobre roxo, `#logo-optimall` sobre claro. Nunca trocar por PNG, nunca recolorir por `filter`.
5. **Nunca escrever cor solta.** Toda cor sai do `tokens.md` da marca, por `var(--token)`.
6. **Podi: o roxo é só detalhe** — `guidelines/uso-do-roxo.md`. No máximo 3 por slide, nunca em
   texto, nunca sobre o verde. **Optimall:** o roxo é a marca; texto sobre ele é sempre branco,
   e roxo como texto sobre claro é `--roxo-texto` (`optimall/tokens.md`).
7. Numerar os slides no rodapé e conferir se o CTA é o `links.cta` da marca.
8. **Optimall:** não recolorir — o deck já nasceu na paleta dele, e o `aplicar` recusa deck do
   Optimall. As imagens fixas saem de `brand/optimall/assets/` (`produto/`, `clientes/`,
   `parceiros/`, `grafismos/`, `fotos/`) e vão **achatadas** para `saida/<slug>/assets/`, com o
   nome que o slide usa. A fonte é a Halyard Text, instalada na máquina.

Proporção de imagem fora do esperado: **não distorça e não corte por conta própria.**
Monte o resto e relate no fim — qual arquivo, qual proporção veio, qual era esperada.

## 4. A rota `/design`

Quando a pessoa quiser **editar o visual à mão** em vez de receber o HTML pronto, o mesmo
conteúdo vai para o comando `/design` do Claude, como artboards de **1920 × 1080**.

O que não pode escapar: **o `/design` não decide nada de identidade.** Ele recebe as
decisões prontas. Ao chamar, passe no briefing do canvas, explicitamente:

- Os tokens do `tokens.md` da marca **com os hex** — Podi em `design-system/apresentacao/tokens.md`,
  Optimall em `design-system/apresentacao/optimall/tokens.md`. Os hex, não os nomes.
- Canvas 1920 × 1080, margem de segurança de 96px (Podi) ou 64px (Optimall).
- A fonte e a escala tipográfica inteira: Inter em dois pesos (Podi); Halyard Text (Optimall).
- As duas regras de contraste: texto sobre a cor de marca é o `ink-on-brand` da marca (no
  Podi, `#101010` — **nunca branco** sobre o verde); a secundária (no Podi, o roxo `#9934FF`)
  é **só detalhe gráfico**, nunca texto, nunca sobre a cor de marca.
- O logo da marca, em SVG (`brand/<marca>/assets/header/`).
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
inventa: ela está no Style Lock da marca (`brand/<marca>/photography/`). Relate o que falta e
aponte o Style Lock — ou monte o prompt com `/foto-podi` (`/foto-optimall`).

Se o pedido conflita com o brand — outra cor, texto branco sobre o verde, título roxo,
outro logo — **sinalize o conflito** em vez de alterar a identidade. Explique a regra em
uma frase e ofereça a alternativa que respeita o sistema. Se a pessoa reafirmar, é decisão
dela: diga que a peça sai fora do padrão e siga.

## 6. QA e entrega

Rodar `design-system/apresentacao/guidelines/qa-checklist.md` inteiro antes de dizer que
está pronto. Os itens verificáveis por comando:

```bash
f=saida/<slug>/index.html
grep -c '{{' $f                                     # 0 — nenhum placeholder
grep -n 'color:[^;"]*\(9934FF\|48DB84\|--accent)\)' $f   # Podi: só a regra .logo--marca
grep -c 'color:var(--accent-2)' $f                  # só chip de ícone e aspas do 10
grep -o '<img[^>]*>' $f | grep -cv 'alt='           # 0
grep -o 'src="[^"]*"' $f | grep -v '^src="assets/'  # nada
grep -c 'podi.com.br/app' $f                        # 0
grep -c 'class="slide' $f                           # = número de slides do roteiro
python3 scripts/aplicar-marca.py conferir <marca> $f   # saída 0
```

Os greps com `9934FF`/`48DB84`/`--accent-2` são do deck do Podi; no do Optimall quem confere a
paleta é o `conferir`, que também acusa qualquer sobra do Podi. No Optimall, também:
`grep -ci 'podi\|tacla' $f` → 0 e nenhum "a Optimall".

Gerar o PDF:

```bash
python3 scripts/exportar.py pdf saida/<slug>/index.html   # → saida/<slug>/<slug>.pdf
```

Se ele disser que a fonte não está instalada, dizer em português comum: *"a fonte do Optimall
(Halyard Text) não está ativada neste computador — ative pelo Creative Cloud, em Fontes, e me
avise para gerar de novo"*.

Depois **abrir no navegador** (`open $f`) e conferir de olho: nenhum slide cortado, nada
fora da margem, o PDF sai em paisagem com um slide por página.

Relatar sempre: caminho do arquivo, **a marca**, **quantos slides e quais tipos**, imagens a hospedar
ou a substituir com a dimensão final, onde está o PDF, e **o que do briefing não coube no
padrão** — dizendo explicitamente o que ficou de fora e por quê.
