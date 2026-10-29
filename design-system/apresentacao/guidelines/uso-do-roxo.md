# O roxo `#9934FF` — onde entra e onde não entra

A regra nasce em [`brand/README.md`](../../../brand/README.md). Aqui está o que ela
significa na prática de um slide.

**O verde é a marca. O roxo é tempero.** Um slide bem montado tem entre um e três **tipos**
de detalhe roxo. Quatro tipos já é um slide roxo, e slide roxo não parece Podi.

O que se repete numa grade ou numa lista conta **uma vez só**: os quatro ícones dos cards do
`04` são um detalhe, as quatro réguas curtas são outro. O `04` tem dois tipos (ícone e régua);
o `07` tem dois (régua e ícones da caixa de recursos) e a borda da caixa, o terceiro.

## Os cinco usos permitidos

| Uso | Token | Onde está |
|---|---|---|
| Ícone Bulk solto, em card branco ou fundo claro | `accent-2` (a camada de fundo a 40%) | `04`, `05`, `06`, `07` |
| Régua sob o título, some para a direita | `accent-2` → transparente, 200 × 4px (56 × 4px em card) | quase todos |
| Bullet de lista, ponto de timeline | `accent-2` | `01`, `11`, `12` |
| Borda fina de container | `accent-2-line`, 2px | `06`, `07`, `13` |
| Aspas ornamentais | `accent-2` a 35% de opacidade | `10` |

Fora desta lista, **não é uso permitido** — é proposta, e proposta vai para quem cuida do
padrão (`docs/governanca.md`).

## Onde nunca

- **Texto.** Nenhum parágrafo, nenhum título, nenhum rótulo, nenhum número de destaque.
  Passaria em contraste (4,9:1 sobre branco); a regra é de marca, não de acessibilidade.
- **Sobre o verde.** `#9934FF` sobre `#31D06E` dá 2,4:1. Detalhe roxo só existe **dentro
  de card branco** ou sobre `page-light`.
- **Fundo de área grande.** Campo de cor é papel do verde. Card roxo, faixa roxa e slide
  roxo estão fora.
- **Carregando informação sozinho.** Um ícone roxo sem rótulo ao lado não comunica nada
  para quem está no fundo da sala — mesma lógica do ícone social verde do rodapé do e-mail.

## Como conferir

```bash
f=saida/<slug>/index.html
grep -o 'color:[^;"]*\(9934FF\|--accent-2\b\)' $f  # 0 — roxo nunca é hex em texto
grep -n 'color:[^;"]*\(31D06E\|--accent)\)' $f     # só .logo--marca: logo é forma, não texto
grep -c 'color:var(--accent-2)' $f                  # só o .ico do template e as aspas do 10
grep -c '9934FF' $f                                 # 1 — só no :root do template
```

Nos slides, o roxo aparece **sempre por token** (`var(--accent-2)`), nunca por hex. Hex de
roxo escrito no meio de um slide é sinal de que alguém copiou de fora do sistema.

Os únicos `color:var(--accent-2)` legítimos são o do **`.ico`** no template — ali o `color`
existe para o `currentColor` do SVG pegar a cor, não para pintar texto — e as **aspas
ornamentais** do `10-citacao`. Qualquer outro é erro.
