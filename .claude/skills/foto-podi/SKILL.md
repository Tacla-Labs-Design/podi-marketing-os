---
name: foto-podi
description: Escreve o prompt de uma foto de marca do Podi a partir de um pedido em português — hero de site, banner, imagem de campanha, detalhe de app. Use quando pedirem uma foto, uma imagem de marca, um prompt de imagem ou uma geração de foto para peça do Podi.
---

# Escrever o prompt de uma foto Podi

O pedido chega solto, em português: *"quero uma foto de alguém resgatando cupom"*,
*"preciso de um hero pro site"*. Esta skill transforma isso num prompt pronto para colar
no gerador — e a conversa continua em português, mesmo com o prompt saindo em inglês.

Esta skill é o **procedimento**. A direção visual está em outro lugar e manda em tudo:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/photography/STYLE-LOCK-PODI.md` | DNA fotográfico, cenários, luz, paleta, checklist |
| Brand | `brand/photography/README.md` | O que ali é normativo e o que é ferramenta |
| Brand | `brand/README.md` | Cor de marca, as duas frentes |

Em caso de conflito, a camada mais alta prevalece. Ver `docs/governanca.md`.

## 0. Atualizar o padrão

Antes de qualquer coisa, e **sem perguntar nada ao usuário**:

```bash
./scripts/check-atualizacao.sh --atualizar
```

- **Saída 0** → seguir. Se atualizou, mencione em uma linha: *"Atualizei o padrão para a
  versão mais recente antes de escrever."* Se não atualizou nada, não comente.
- **Saída 1** → parar. Dizer que esta cópia do padrão está diferente da oficial e que é
  preciso avisar quem cuida do repositório. Não tentar resolver, não escrever assim mesmo.

## 1. Regra zero — ler o Style Lock

**Abra `brand/photography/STYLE-LOCK-PODI.md` inteiro antes de escrever qualquer prompt.**

Não escreva de memória, nem numa conversa longa em que o arquivo já "passou" antes — ele é
a fonte da verdade e pode ter mudado desde então.

**O bloco `STYLE LOCK` (§4.A interior · §4.B outlet) entra copiado byte a byte.** Nunca
parafraseie, resuma, reordene ou "melhore" uma palavra dele. Ele existe justamente para não
variar: é o que faz duzentas imagens geradas ao longo de meses parecerem do mesmo ensaio.
Se você reescrever, a consistência morre e ninguém percebe até ter quarenta imagens
desalinhadas. A **única** substituição autorizada é a frase da lente para 35mm, documentada
na §4.A.

## 2. Enquadrar o pedido

Todo prompt precisa destas decisões fechadas:

| Dimensão | Como resolver |
|---|---|
| **Tipo de shot** | close-up · plano médio · três-quartos · wide editorial · detalhe/macro |
| **Sujeito** | idade, etnia, cabelo, corpo — **sempre específico**, nunca "uma pessoa". Varie entre pedidos: as refs vão de 25 a 65+ (§1.6) |
| **Ação no app** | campanha/sorteio · resgate de cupom · consulta de informação · wayfinding · navegação genérica · ou um momento sem o app em uso (ler, conversar, descansar), com o celular apoiado no quadro |
| **Cenário** | um dos **8 cenários de interior** da §2.4 (padrão). A §2.5 (outlet, 9–12) só se o pedido for explicitamente de outlet. **Não inventar cenário fora da lista** |
| **Posição na luz** | **obrigatório no interior** — onde o sujeito está em relação à claraboia ou ao vidro. Sem isso o gerador põe luz de loja na pele e a foto sai fora do padrão |
| **Props verdes** | roupa em 1–2 valores de verde + case mint ou sacola (§2.6). No interior o verde precisa de **volume** — peça inteira, não detalhe |
| **Formato** | 4:5 feed · 9:16 story · 16:9 banner/OOH · 1:1 thumbnail |
| **Óptica** | `85mm f/2.0` é o padrão de interior. `35mm f/3.2` só quando a arquitetura é o assunto — cenários 1, 3, 5 — ou em grupo (5.8) |

**Não pergunte se puder inferir.** "Foto pro Instagram" → 4:5. "Banner do site" → 16:9.
Pergunte só quando a resposta muda materialmente a imagem (ex.: campanha sem dizer se é uma
pessoa ou um grupo) — e mesmo aí, escolha um default, entregue, e ofereça a variante.

## 3. Ver se a §5 já resolve

O Style Lock tem 8 prompts prontos (§5.1–5.8). Se o pedido cai em cima de um deles, **parta
dele** e ajuste sujeito e cenário — não escreva do zero. Diga de qual variação você partiu.

## 4. Montar

```
[TIPO DE SHOT] + [SUJEITO + AÇÃO NO APP] + [CENÁRIO §2.4] + [POSIÇÃO NA LUZ NATURAL]
+ [PROPS VERDES] + ⟪STYLE LOCK §4.A verbatim⟫ + [PARÂMETROS]
```

O prompt sai **em inglês** — os geradores respondem muito melhor. A conversa é em português.

O verde do Podi é `#31D06E` e já está traduzido no Style Lock como `vivid emerald green` /
`deep pine green` / `soft mint green`. **Não invente outro termo de cor e não escreva o hex
dentro do prompt** — gerador não entende hexadecimal.

## 5. Rodar o checklist da §6

Antes de entregar, confira que o texto do prompt satisfaz todos os itens. Os que mais escapam
na hora de escrever:

- **Regra da Luz do Dia** — o sujeito precisa estar *dentro* da luz de claraboia ou vidro.
  Luz de varejo nunca toca a pele; só existe como bokeh quente ao fundo. Se o cenário pedido
  não entrega isso, **o cenário está errado, não a regra**.
- **Fundo dissolvido** — vitrine, letreiro e transeuntes ilegíveis. Isso se resolve na óptica
  (85mm f/2.0), não na cenografia.
- **Espaço negativo** — no interior é o vazio claro do átrio, o teto branco, a claraboia.
  É o substituto do céu; sem ele a foto não parece da marca.
- **Contra-plongée** — câmera abaixo da linha dos olhos. É a assinatura mais reconhecível.
- **Nunca olhar para a câmera.** Por padrão o olhar vai para a tela; em cena de outra atividade
  (livro, conversa), vai para ela — e o celular continua no quadro, com o glow verde (§1.4).
- **Um único accent, e ele é verde**, em 2–3 valores no mesmo quadro.

## 6. Entregar neste formato

````
## ⟨nome da peça⟩ · ⟨cenário⟩ · ⟨formato⟩

**Prompt**
```text
⟨prompt completo, inglês, STYLE LOCK incluído, pronto pra colar⟩
```

**Negative prompt** ⟨geradores com campo separado: FLUX, SDXL, Ideogram⟩
```text
⟨§2.8 verbatim⟩
```

**Versão para GPT Image / Gemini** ⟨sem campo de negative⟩
```text
⟨prompt + STYLE LOCK + CLEAN-FRAME CLAUSE §2.9 verbatim, formato em palavras⟩
```

**Parâmetros** ⟨§4, tabela "Parâmetros por gerador"⟩
````

**Sempre as duas versões.** O usuário troca de gerador entre peças, e a diferença entre elas
não é cosmética — o porquê está na §2.9.

Depois do bloco, **2 a 4 linhas** em português sobre a decisão de direção (por que esse
cenário, esse sujeito, esse crop) e o que ajustar se o resultado sair torto. Sem parágrafos
de explicação: quem lê é designer e vai ler a imagem melhor que a prosa.

## 7. Guardar

Gravar o bloco entregue em **`saida/fotos/NNN-slug.md`** — `001-hero-mezanino.md`,
`002-cupom-boutique.md` —, numeração sequencial e contínua. É o histórico do ensaio: dá para
repetir uma foto meses depois e reaproveitar a seed.

Como `saida/` é pasta local, **nunca gravar em `brand/`** — nem prompt, nem imagem gerada.

## 8. Consistência entre lotes

Prompt de texto sozinho **não** sustenta um sistema visual longo. Sempre que o usuário já
tiver imagens aprovadas, lembre:

1. **`--sref`** — 3 a 5 imagens aprovadas como Style Reference (`--sref <urls> --sw 100`)
   travam o look melhor que qualquer descrição. É a alavanca mais forte, e no interior vale
   ainda mais: descrever em palavras "luz de dia na pele, luz de loja só no bokeh" é frágil.
2. **`--seed`** — dentro da mesma família de cenário, reaproveitar a seed da imagem-mãe.
3. **`--cref`** — para repetir a mesma pessoa numa campanha de várias peças.
4. Seed trava **luz, não cena**. Dois cenários diferentes na mesma seed não casam.

Quando o usuário aprovar um conjunto de imagens, sugira guardar as URLs para virarem o style
reference oficial — isso é **proposta de evolução do padrão**, decidida pelo maintainer
(`docs/governanca.md`), não algo que a skill grava sozinha.

## 9. Quando algo não existe no sistema

Se o pedido precisa de cenário, cor ou tratamento que o Style Lock não tem:

1. **Não invente.** Nada de cenário fora da §2.4/§2.5, nada de segundo accent, nada de termo
   de cor novo.
2. Verifique se um cenário aprovado resolve com outro enquadramento.
3. Se realmente não resolve, entregue o que dá para entregar e **relate a ausência no fim**,
   marcada como **proposta**: o que falta, onde seria usado, o que você sugere.
4. Proposta não vira padrão sozinha. Quem decide é o maintainer.

Se o pedido conflita com o brand — outro accent, sujeito olhando para a câmera, interior
escuro — **sinalize o conflito** em vez de executar. Explique a regra em uma frase e ofereça
a alternativa que respeita o sistema. Se a pessoa reafirmar, diga que a peça sai fora do
padrão e siga.

## 10. Os erros que custam caro

A matriz completa de acertos e erros está na §2.7 e a técnica de negative por gerador na
§2.9–2.10. Estes são os que acontecem **na hora de escrever**, não na hora de gerar:

- Reescrever, resumir ou "melhorar" o bloco STYLE LOCK.
- Entregar prompt sem negative — §2.8 no campo separado, ou §2.9 embutido.
- **Colar a lista de palavras da §2.8 dentro do prompt de GPT Image ou Gemini.** Esses
  modelos leem prosa como instrução e pesam os tokens negativos: a multidão e o letreiro
  aparecem *por causa* da lista. Nesses casos usa-se a CLEAN-FRAME CLAUSE da §2.9, que diz
  o que **está** no quadro.
- Usar `--ar` em GPT Image ou Gemini — eles ignoram; o formato vai em palavras (§7.2).
- Sujeito genérico ("uma pessoa") em vez de descrito.
- Esquecer o slot de **posição na luz** no interior. É o erro nº 1.
