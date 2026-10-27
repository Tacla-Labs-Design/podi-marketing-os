---
name: post-podi
description: Monta um post ou carrossel de rede social (Instagram, LinkedIn) do Podi em 1080×1350 a partir de um briefing em projects/_inbox/<slug>/, exporta em PNG e escreve a legenda. Use quando pedirem para gerar, montar ou criar um post, um carrossel, um card de Instagram ou LinkedIn do Podi.
---

# Montar um post ou carrossel do Podi

Argumento: o slug da pasta em `projects/_inbox/`. Antes de pedir ou ler o briefing, rodar o
§0 e o §0b — sem modelos de post, não há o que perguntar. Sem argumento, listar as pastas
disponíveis e perguntar qual. Se não houver briefing em pasta nenhuma, o assunto pode vir
direto da conversa — mas o roteiro (§2) continua obrigatório.

Esta skill é o **procedimento**. As regras que ela obedece estão em outros lugares e valem
integralmente:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/README.md`, `brand/links-oficiais.md`, `brand/marca.json` | Identidade, contraste, logo, CTA, redes |
| Brand | `brand/photography/STYLE-LOCK-PODI.md` | Direção fotográfica — só quando o post pedir **foto nova** |
| Design System | `design-system/post/` | Canvas, carrossel, legenda, QA — e os tokens e modelos de post |
| Template | `templates/post/base.html` | O shell |

Em caso de conflito, a camada mais alta prevalece. Ver `docs/governanca.md`.

## 0. Atualizar o padrão

Antes de qualquer coisa, e **sem perguntar nada ao usuário**:

```bash
./scripts/check-atualizacao.sh --atualizar
```

Quem usa este comando não é pessoa técnica (`CLAUDE.md`). Não peça para ela rodar Git.

- **Saída 0** → seguir. Se atualizou, dizer em uma linha: *"Atualizei o padrão para a versão
  mais recente antes de montar."* Se não, não comentar.
- **Saída 1** → **parar**. Dizer que esta cópia do padrão está diferente da oficial e que é
  preciso avisar quem cuida do repositório.

## 0b. Os modelos existem?

```bash
ls design-system/post/posts/ design-system/post/tokens.md templates/post/base.html
```

- **Faltando qualquer um** → **parar** e dizer, em português comum: *"os modelos de post do Podi ainda não
  foram carregados no padrão — avise quem cuida do repositório"*. Nunca improvisar um layout,
  nem montar com modelo de deck ou de outra marca.
- Tudo presente → seguir.

## 1. Ler tudo antes de decidir qualquer coisa

```bash
ls -R projects/_inbox/<slug>/
```

- `.docx` → `textutil -convert txt -stdout arquivo.docx` · `.pdf` → `pdftotext arquivo.pdf -`
- `.zip` → `unzip -o arquivo.zip -d projects/_inbox/<slug>/imagens/`
- Imagens → **abrir de fato** com a tool Read. Você precisa ver o que é e a proporção real.

Antes de montar, saber três coisas. Se o briefing não disser, **perguntar**:

1. **Onde sai** — Instagram, LinkedIn ou os dois (muda só a legenda).
2. **Post único ou carrossel** — e, no carrossel, a história em passos.
3. **Qual é o pedido** — o que a pessoa deve fazer depois de ver. É o CTA do fecho e da legenda.

## 2. Definir o roteiro — e confirmar antes de montar

Uma lista: **número do card, modelo, o que ele diz em uma frase.**

```
01  <modelo da capa>   capa: a promessa, em uma frase
02  <modelo do miolo>  um ponto por card
03  <modelo do miolo>  …
04  <modelo do fecho>  fecho: o pedido, com o CTA do Podi
```

O modelo se escolhe pelo **formato da informação** — o catálogo dos modelos fica no
`README.md` de `design-system/post/` quando eles forem carregados. Estrutura de carrossel em `design-system/post/guidelines/carrossel.md`:
3 a 10 cards, capa, miolo com um ponto por card, fecho com o CTA.

**Mostre o roteiro com o texto de cada card e espere a pessoa confirmar antes de montar.**

## 3. Montar

1. Copiar `templates/post/base.html` para **`saida/<slug>/index.html`** e trocar o título do
   `<title>`.
2. Copiar os modelos escolhidos de `design-system/post/posts/` para dentro do
   `<div class="grade">`, na ordem do roteiro, e preencher os `{{PLACEHOLDER}}`.
   Nunca gravar em `examples/`.
3. Criar `saida/<slug>/assets/` e colocar ali **todas** as imagens — as do briefing e as fixas
   copiadas de `brand/assets/`. O post precisa abrir sozinho se alguém mandar a pasta.
4. Trocar os ícones genéricos dos chips pelo glifo certo do assunto, mantendo
   `fill="currentColor"` ou `stroke="currentColor"`.
5. O **logo não é imagem**: é o `<symbol>` que vem no template, usado por `<use href="#…">`.
   A cor sai do CSS; nunca PNG, nunca `filter`.
6. **Nunca escrever cor solta.** Toda cor sai de `design-system/post/tokens.md`, por
   `var(--token)`. O verde `#48DB84` é só fundo — texto em cima dele é `#101010`, nunca branco.
7. **O que não cabe vira outro card** — nunca fonte menor que o mínimo do `tokens.md`.
8. Escrever `saida/<slug>/legenda.txt` conforme `design-system/post/guidelines/legenda.md`
   (Instagram, LinkedIn e ALT de cada card).

Imagem com proporção fora do slot: **não distorça e não corte por conta própria.** Monte o
resto e relate no fim — qual arquivo, qual proporção veio, qual era esperada.

Foto que não existe: a direção visual não se inventa — está no Style Lock do Podi. Relate o
que falta e ofereça o prompt com `/foto-podi`.

## 4. Exportar

```bash
python3 -I scripts/exportar.py png saida/<slug>/index.html
```

- Saída 0 → um PNG por card em `saida/<slug>/png/`, na ordem do roteiro.
- *"A fonte … não carregou"* → dizer em português comum que a fonte do Podi não carregou
  neste computador e que é preciso avisar quem cuida do repositório. Não exportar com outra
  fonte.

## 5. Quando falta algo no sistema

Se o conteúdo pede um modelo, uma cor ou um formato que não existe (story 9:16, quadrado,
um layout novo):

1. **Não invente.** Nada de cor nova nem layout improvisado com CSS solto.
2. Verifique se um dos modelos resolve com outro conteúdo.
3. Se realmente não resolve, monte o resto e **relate a ausência no fim**, marcada
   explicitamente como **proposta**.
4. Proposta não vira padrão sozinha. Quem decide é o maintainer (`docs/governanca.md`).

Se o pedido conflita com o brand — outra cor, texto branco sobre o verde, título roxo, logo
recolorido — **sinalize o conflito** em uma frase e ofereça a alternativa que respeita o
sistema. Se a pessoa reafirmar, é decisão dela: diga que a peça sai fora do padrão e siga.

## 6. QA e entrega

Rodar `design-system/post/guidelines/qa-checklist.md` inteiro. O verificável por comando:

```bash
python3 -I scripts/conferir.py saida/<slug>/index.html saida/<slug>/legenda.txt   # saída 0, "N cards" = o roteiro
```

Ele lê a peça sem os comentários e confere: nenhum `{{...}}`, toda imagem com `alt` e dentro
de `assets/`, cor só da paleta, o verde nunca como cor de texto, nenhum "a Podi" — na arte e
na legenda — e diz quantos cards há. Os PNGs já saíram no §4.

Depois **abrir cada PNG** com a tool Read e conferir de olho: texto cortado, imagem que não
carregou, fonte trocada, nada fora da margem.

Relatar sempre, em português comum: onde estão os PNGs e a legenda, **quantos cards e quais
modelos**, imagens que precisam ser trocadas por versão final (com a dimensão), e **o que do
briefing não coube no padrão** — dizendo explicitamente o que ficou de fora e por quê.
