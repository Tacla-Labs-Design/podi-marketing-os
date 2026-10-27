# Fotografia

Direção fotográfica oficial das marcas. Faz parte de `brand/`: é a camada mais alta, e
**nada abaixo dela pode contradizê-la** — nem design system, nem template, nem skill,
nem pedido de campanha. Ver `docs/governanca.md`.

Cada marca tem **um** Style Lock, e ele é a fonte única da direção fotográfica dela:

| Marca | Style Lock |
|---|---|
| Podi | [`podi/photography/STYLE-LOCK-PODI.md`](../podi/photography/STYLE-LOCK-PODI.md) |
| Optimall | `optimall/photography/STYLE-LOCK-OPTIMALL.md` — derivado do Podi (mesma luz, lente e composição), roxo em três valores e cenas B2B |

**A direção é a mesma entre as marcas** — luz, lente, cenário, composição, humor. O que
muda é **só a paleta**: as seções de cor, o figurino e as frases de cor dentro dos blocos
travados. Um Style Lock novo nasce como cópia do do Podi, com essas partes reescritas pelo
método da §8 ("uma matiz em três valores"). Este arquivo só diz como ler um Style Lock.

---

## As duas regras que quebram tudo se forem ignoradas

1. **Leia o Style Lock antes de escrever qualquer prompt de imagem.** Não gere de memória,
   nem numa conversa longa em que o arquivo já "passou" antes — ele pode ter mudado.
2. **O bloco `STYLE LOCK` (§4.A interior · §4.B outlet) se copia byte a byte.** Nunca
   parafraseie, resuma, reordene ou "melhore" uma palavra. Ele existe justamente para não
   variar: é o que faz duzentas imagens geradas ao longo de meses parecerem do mesmo ensaio.
   A **única** substituição autorizada é a frase da lente para 35mm, documentada na §4.A.

## O que é normativo e o que é ferramenta

| Seção | Papel |
|---|---|
| §1 DNA fotográfico · §2 Tradução para o interior · §4 blocos STYLE LOCK · §6 Checklist · §8 Verde | **Normativo.** É a diretriz de marca. Só o maintainer altera. |
| §3 Fórmula de slots · §5 Suíte de variações · §7 Prompt único · §2.8–2.10 negative por gerador | **Ferramenta de execução.** Ajuda a montar o prompt; não redefine a direção. |

## A cor da marca dentro da foto

A cor de marca está resolvida dentro de cada Style Lock. No Podi, o verde **`#48DB84`**
(`brand/podi/README.md`) vira `vivid emerald green` / `deep pine green` / `soft mint green` —
a tradução dele para o vocabulário que os geradores entendem. Não são hexadecimais
alternativos e não se trocam por campanha.

**Isto não conflita com a regra de contraste do brand.** Lá, a cor de marca pode não servir
como texto. Aqui, ela é figurino, objeto e props dentro da foto — outro eixo, outra regra.

## `refs/`

Cada marca pode ter `photography/refs/`. As do Podi (`podi/photography/refs/`) são as
referências originais que deram origem ao Style Lock. São **leitura e insumo**, não
ativos de peça: entram como imagem de entrada em Gemini / Nano Banana (§2.10) e servem de
gabarito para julgar uma geração. Nunca sobrescrever, nunca usar direto numa peça.

## Como se usa na prática

O procedimento — enquadrar o pedido, montar o prompt, escolher parâmetros por gerador,
arquivar o que foi entregue — está na skill **`/foto-podi`**
([`.claude/skills/foto-podi/SKILL.md`](../../.claude/skills/foto-podi/SKILL.md)). O
`/foto-optimall` segue o mesmo procedimento, com o Style Lock do Optimall.

A divisão é a de sempre: este arquivo define **o que é permitido visualmente**, a skill
ensina **como executar**. A skill referencia o Style Lock; nunca copia trechos dele.
