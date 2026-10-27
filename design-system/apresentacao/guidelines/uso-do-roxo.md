# O roxo `#9934FF` — onde entra e onde não entra

A regra nasce em [`brand/README.md`](../../../brand/README.md). Aqui está o que ela
significa na prática de um slide.

**O verde é a marca. O roxo é tempero.** Um slide bem montado tem entre um e três detalhes
roxos. Quatro já é um slide roxo, e slide roxo não parece Podi.

## Os cinco usos permitidos

| Uso | Token | Onde está |
|---|---|---|
| Glifo de ícone dentro de chip claro | `accent-2` sobre `accent-2-soft` | `04`, `05`, `06` |
| Régua/gradiente sob o título | `accent-2` → `accent-2-mid`, 120 × 6px | quase todos |
| Bullet de lista, ponto de timeline | `accent-2` | `01`, `11`, `12` |
| Borda fina de container | `accent-2-line`, 2px | `06`, `13` |
| Aspas ornamentais | `accent-2` a 35% de opacidade | `10` |

Fora desta lista, **não é uso permitido** — é proposta, e proposta vai para quem cuida do
padrão (`docs/governanca.md`).

## Onde nunca

- **Texto.** Nenhum parágrafo, nenhum título, nenhum rótulo, nenhum número de destaque.
  Passaria em contraste (4,9:1 sobre branco); a regra é de marca, não de acessibilidade.
- **Sobre o verde.** `#9934FF` sobre `#48DB84` dá 2,4:1. Detalhe roxo só existe **dentro
  de card branco** ou sobre `page-light`.
- **Fundo de área grande.** Campo de cor é papel do verde. Card roxo, faixa roxa e slide
  roxo estão fora.
- **Carregando informação sozinho.** Um ícone roxo sem rótulo ao lado não comunica nada
  para quem está no fundo da sala — mesma lógica do ícone social verde do rodapé do e-mail.

## Como conferir

```bash
f=saida/<slug>/index.html
grep -o 'color:[^;"]*\(9934FF\|--accent-2\b\)' $f  # 0 — roxo nunca é hex em texto
grep -n 'color:[^;"]*\(48DB84\|--accent)\)' $f     # só .logo--marca: logo é forma, não texto
grep -c 'color:var(--accent-2)' $f                  # só chip de ícone e aspas do 10
grep -c '9934FF' $f                                 # 1 — só no :root do template
```

Nos slides, o roxo aparece **sempre por token** (`var(--accent-2)`), nunca por hex. Hex de
roxo escrito no meio de um slide é sinal de que alguém copiou de fora do sistema.

Os únicos `color:var(--accent-2)` legítimos são o **chip de ícone** e o **ícone da lista de
features** — ali o `color` existe para o `currentColor` do SVG pegar a cor, não para pintar
texto — e as **aspas ornamentais** do `10-citacao`. Qualquer outro é erro.
