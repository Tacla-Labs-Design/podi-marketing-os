# Brand

Camada mais alta do Marketing OS. **Nada abaixo pode contradizer esta pasta.**

Se um pedido conflita com o que está aqui, a IA sinaliza o conflito em vez de alterar
a identidade. Ver `docs/governanca.md`.

---

## As marcas

O Marketing OS atende duas marcas irmãs. **O sistema é um só** — a mesma estrutura, os
mesmos procedimentos (skills), o mesmo canvas, o mesmo QA, a mesma governança, a mesma
direção fotográfica. O que muda de uma marca para outra:

| Material | Podi | Optimall |
|---|---|---|
| E-mail | Blocos de `design-system/newsletter/` | **Os mesmos blocos**, recoloridos por `scripts/aplicar-marca.py` |
| Deck | `design-system/apresentacao/slides/` | **Biblioteca própria**: `design-system/apresentacao/optimall/` |
| Post | *(modelos pendentes)* | **Biblioteca própria**: `design-system/post/optimall/` |
| Foto | Style Lock do Podi | Style Lock do Optimall — mesma direção, outra paleta e outras cenas |

O Optimall tem biblioteca própria de deck e post porque a linguagem dele — degradê roxo,
vidro, pattern de pontos, fonte Halyard, logo tricolor — não sai de pintar os slides do Podi
de outra cor. Os modelos vêm dos arquivos do Figma aprovados pelo time do Optimall. Em todo
o resto, as duas marcas seguem as mesmas regras: **a paleta, o logo, os links e a voz** são o
que muda.

| Marca | Pasta | O que é | Comandos |
|---|---|---|---|
| **Podi** | [`podi/`](podi/README.md) | O app dos shoppings — fala com o consumidor e com o time | `/newsletter-podi`, `/apresentacao-podi`, `/post-podi`, `/foto-podi` |
| **Optimall** | [`optimall/`](optimall/README.md) | A plataforma B2B dos shoppings — fala **só** com gestores | `/newsletter-optimall`, `/apresentacao-optimall`, `/post-optimall`, `/foto-optimall` |

As duas são **masculinas**: "o Podi", "do Podi"; "o Optimall", "do Optimall". Nunca "a".

Cada pasta de marca tem:

| Arquivo | O que guarda |
|---|---|
| `README.md` | Voz, público, logo, cor de marca e as regras que só valem para ela |
| `links-oficiais.md` | CTA fixo, rodapé legal, redes, textos fixos do deck |
| `marca.json` | Os mesmos valores, para máquina — lido por `scripts/aplicar-marca.py` |
| `mensagens.md` | *(Optimall)* O que dizer: posicionamento, módulos, números oficiais, frases aprovadas |
| `assets/` | Logo (SVG + PNG para e-mail) e ícones sociais; no Optimall, também clientes, produto e grafismos |
| `photography/STYLE-LOCK-<MARCA>.md` | Direção fotográfica — igual entre as marcas, menos a paleta |

**Qual marca é a peça:** decide o comando (`-podi` ou `-optimall`) ou a linha `Marca:` do
briefing. Sem nenhum dos dois, é Podi. Peça de uma marca **não mistura** logo, cor, rede ou
link da outra.

## Regras que valem para as duas marcas

**Nunca escreva cor solta.** Toda cor sai dos tokens do material
(`design-system/<material>/tokens.md`), e o valor de cada papel por marca está em
`brand/<marca>/marca.json`. Os blocos de e-mail são escritos com os valores do Podi; e-mail de
outra marca é montado igual e recolorido no fim por `scripts/aplicar-marca.py` — nunca à mão.
Deck e post de marca com biblioteca própria já nascem na paleta dela e só passam pelo
`aplicar-marca.py conferir`.

**Nenhum texto abaixo de 4,5:1.** Vale para qualquer material. Onde a cor de marca não passa
disso sobre branco, ela só entra como **fundo** — é o caso do verde do Podi.

**Texto em cima da cor de marca** é o papel `ink-on-brand` da marca: `#101010` no Podi,
**branco** no Optimall. Nunca se escolhe no olho — sai do `marca.json`, medido.

**Cor secundária é detalhe gráfico**, nunca conteúdo: ícone, régua sob título, bullet, borda
fina. Nunca texto, nunca título, nunca fundo de área grande, nunca em cima da cor de marca.
Regra completa: `design-system/apresentacao/guidelines/uso-do-roxo.md`.

**Logo não é texto.** Ele é marca gráfica, e a regra de contraste governa palavras. O que é
proibido é **recolorir por filtro ou por efeito**. No Podi o SVG é monocromático e a cor vem
de `currentColor`; no Optimall o logo é tricolor e tem duas versões oficiais (positivo e
negativo) — usa-se a versão certa para o fundo, nunca uma cor nova.

**Fotografia** segue o Style Lock da marca, e o bloco `STYLE LOCK` se copia sem editar uma
palavra. Ver [`photography/README.md`](photography/README.md).

**Não se inventa URL nem arte** para o que já existe em `links-oficiais.md` da marca.

## Marca nova ou mudança de paleta

É trabalho do maintainer, nunca de campanha:

```bash
python3 scripts/aplicar-marca.py derivar <marca> "<cor principal>" ["<secundária>"]            # propõe
python3 scripts/aplicar-marca.py derivar <marca> "<cor principal>" ["<secundária>"] --gravar   # grava e gera ícones
python3 scripts/aplicar-marca.py validar <marca>                                               # confere tudo
```

Depois de validar, o maintainer marca `"status": "aprovado"` no `marca.json` e registra no
`CHANGELOG.md`. Enquanto o status for `pendente`, o script recusa montar peça da marca.
