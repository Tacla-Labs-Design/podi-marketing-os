# Skills

As skills oficiais ficam em **`.claude/skills/`** — é a pasta que o Claude Code descobre
sozinho ao abrir o repositório. Manter uma segunda cópia aqui só criaria duas versões
divergindo, então esta pasta é apenas o índice.

| Skill | Arquivo | O que faz |
|---|---|---|
| `newsletter-podi` | [`.claude/skills/newsletter-podi/SKILL.md`](../.claude/skills/newsletter-podi/SKILL.md) | Monta uma newsletter ou informativo do Podi a partir de um briefing em `projects/_inbox/<slug>/` |
| `apresentacao-podi` | [`.claude/skills/apresentacao-podi/SKILL.md`](../.claude/skills/apresentacao-podi/SKILL.md) | Monta uma apresentação 16:9 do Podi a partir de um briefing em `projects/_inbox/<slug>/` |
| `post-podi` | [`.claude/skills/post-podi/SKILL.md`](../.claude/skills/post-podi/SKILL.md) | Monta um post ou carrossel 1080×1350, exporta em PNG e escreve a legenda. No Podi, para até os modelos serem carregados |
| `foto-podi` | [`.claude/skills/foto-podi/SKILL.md`](../.claude/skills/foto-podi/SKILL.md) | Escreve o prompt de uma foto de marca do Podi, seguindo o Style Lock de `brand/podi/photography/` |
| `newsletter-optimall` | [`.claude/skills/newsletter-optimall/SKILL.md`](../.claude/skills/newsletter-optimall/SKILL.md) | Atalho: o procedimento do `newsletter-podi`, com a marca Optimall |
| `apresentacao-optimall` | [`.claude/skills/apresentacao-optimall/SKILL.md`](../.claude/skills/apresentacao-optimall/SKILL.md) | Atalho: o procedimento do `apresentacao-podi`, com a marca e a biblioteca de slides do Optimall |
| `post-optimall` | [`.claude/skills/post-optimall/SKILL.md`](../.claude/skills/post-optimall/SKILL.md) | Atalho: o procedimento do `post-podi`, com a marca e os modelos de post do Optimall |
| `foto-optimall` | [`.claude/skills/foto-optimall/SKILL.md`](../.claude/skills/foto-optimall/SKILL.md) | Atalho: o procedimento do `foto-podi`, com o Style Lock do Optimall |

## Como usar

Dentro do repositório, digite o nome da skill com barra:

```
/newsletter-podi 2026-09-cliente-podi-news
```

Ou peça em português — a skill é escolhida sozinha pela descrição.

## Em outra ferramenta de IA

Se usar Codex ou outro agente que não leia `.claude/skills/` automaticamente, aponte
para o arquivo `SKILL.md` da tabela acima junto com o `CLAUDE.md` da raiz.

## O sufixo de marca

Toda skill oficial termina com o nome da marca: **`-podi`** ou **`-optimall`**. A ferramenta de
IA traz dezenas de comandos próprios, e sem o sufixo não dá para saber, na hora de digitar,
qual deles é o padrão da marca. Skill nova nasce com o sufixo.

**As `-podi` guardam o procedimento; as `-optimall` são atalhos.** O atalho só fixa a marca e
manda seguir a skill `-podi` do mesmo material — o procedimento não se copia, para as duas
marcas nunca saírem de padrões diferentes. Mudança de procedimento se faz **uma vez**, na
`-podi`, e vale para as duas marcas — mesmo quando a marca tem biblioteca própria de layouts
(deck e post do Optimall): muda a pasta de onde os modelos saem, não o procedimento. Material novo ganha a skill `-podi` e o atalho
`-optimall` na mesma leva.

## Criar uma skill nova

Skill nova é recurso oficial: só maintainer cria. Ver [`docs/governanca.md`](../docs/governanca.md).
