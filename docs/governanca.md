# Governança

## Quem mantém

Neste MVP, o **único maintainer** é **Bruno Pinheiro** — Design, Produto e Marketing.

Futuramente outros colaboradores autorizados poderão ser adicionados. O controle é feito
pelo **Git**: só quem tem permissão de escrita no repositório oficial altera o padrão.
Não existe nem deve existir nenhum sistema de senha, login ou permissionamento dentro do
projeto.

## Oficial vs. projeto

| | O que é | Quem altera |
|---|---|---|
| **Oficial** | `brand/`, `design-system/`, `templates/`, `.claude/skills/`, `examples/`, `docs/`, `CHANGELOG.md` | Só maintainer |
| **Projeto** | `projects/_inbox/`, `saida/` | Qualquer pessoa — é local, fora do Git |

Qualquer pessoa pode **usar** o Marketing OS para criar materiais. Ninguém deve **alterar**
recursos oficiais diretamente.

**Uma campanha nunca altera o design system.** Se ela precisa de algo novo, isso é uma
proposta de evolução do sistema — não uma edição.

## Hierarquia de autoridade

```
Brand Guidelines          brand/
        ↓
Design System             design-system/<material>/
        ↓
Templates                 templates/<material>/
        ↓
Skills                    .claude/skills/<skill>/SKILL.md
        ↓
Projeto / pedido do usuário
```

Em conflito, **a camada superior prevalece**.

Exemplo: se alguém pedir "usa uma cor diferente" e essa cor não pertence ao brand, a IA
deve **sinalizar o conflito** e explicar a regra — não alterar a identidade visual. Se a
pessoa reafirmar depois disso, a decisão é dela: a IA diz que a peça sai fora do padrão e
segue.

## Regra fundamental: não inventar padrão

Se algo não está definido:

1. **Identifique a ausência** e diga qual é.
2. **Não crie arbitrariamente.**
3. Se for necessário para executar a tarefa, **proponha** uma solução.
4. **Marque claramente como proposta.**
5. **Proposta não vira padrão automaticamente.**

## Como propor uma mudança (qualquer pessoa)

1. Monte o material com o que existe hoje.
2. Anote o que faltou — a IA já faz isso no relatório final.
3. Mande ao maintainer em uma frase: **o que faltou, onde seria usado, por quê**.

Não edite arquivo oficial para "resolver rápido". Uma cópia local alterada faz o material
sair com um padrão que ninguém mais tem — e nada no arquivo denuncia isso.

## Como incorporar uma mudança (maintainer)

1. Colocar na camada certa:
   - identidade, cor de marca, tom, link fixo, fotografia → `brand/`
   - regra visual, token, componente, guideline, QA → `design-system/<material>/`
   - shell em branco → `templates/<material>/`
   - procedimento que a IA segue → `.claude/skills/<skill>/SKILL.md`
2. Documentar no README da própria pasta.
3. **Escrever a entrada no `CHANGELOG.md` na mesma leva** — data, o que mudou e **por quê**.
   Marcar `**Ação necessária:**` se algo já montado precisar ser revisto.

O porquê é a única parte que não dá para deduzir do histórico daqui a seis meses.
Changelog não escrito na hora não é escrito nunca.

## Cópia desatualizada

`scripts/check-atualizacao.sh` verifica se a cópia local está atrás do repositório oficial
e, com `--atualizar`, já traz a versão nova. A skill roda isso sozinha antes de montar
qualquer coisa.

Se houver alteração local conflitante, o script para e manda avisar o maintainer — em vez
de montar com o padrão antigo sem ninguém perceber. Sem Git, sem remoto ou offline, ele
não bloqueia o trabalho.
