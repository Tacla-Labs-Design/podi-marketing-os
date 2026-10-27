---
name: post-podi
description: Monta um post ou carrossel de rede social (Instagram, LinkedIn) do Podi em 1080×1350 a partir de um briefing em projects/_inbox/<slug>/, exporta em PNG e escreve a legenda. É também o procedimento do /post-optimall. Use quando pedirem para gerar, montar ou criar um post, um carrossel, um card de Instagram ou LinkedIn do Podi.
---

# Montar um post ou carrossel (Podi ou Optimall)

Argumento: o slug da pasta em `projects/_inbox/`. Sem argumento, listar as pastas
disponíveis e perguntar qual. Se não houver briefing em pasta nenhuma, o assunto pode vir
direto da conversa — mas o roteiro (§2) continua obrigatório.

Esta skill é o **procedimento**. As regras que ela obedece estão em outros lugares e valem
integralmente:

| Camada | Onde | O que manda |
|---|---|---|
| Brand | `brand/README.md` | Regras comuns às marcas, e qual marca é a peça |
| Brand | `brand/<marca>/README.md`, `links-oficiais.md`, `marca.json` | Identidade, contraste, logo, CTA, redes |
| Brand | `brand/optimall/mensagens.md` | *(Optimall)* O que dizer: números oficiais, módulos, voz, frases aprovadas |
| Brand | `brand/<marca>/photography/STYLE-LOCK-<MARCA>.md` | Direção fotográfica — só quando o post pedir **foto nova** |
| Design System | `design-system/post/` | Canvas, carrossel, legenda, QA |
| Design System | `design-system/post/<marca>/` | Tokens e modelos de post da marca |
| Template | `templates/post/base-<marca>.html` | O shell |

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

## 0b. Qual marca

- Chamado por **`/post-optimall`**, ou briefing com `Marca: Optimall` → **Optimall**.
- Qualquer outro caso → **Podi**. Se o post fala com gestor de shopping (B2B) e não diz a
  marca, perguntar.

Daqui em diante, `<marca>` é `podi` ou `optimall`, e **tudo que é de marca sai de
`brand/<marca>/`**.

```bash
python3 scripts/aplicar-marca.py validar <marca>
ls design-system/post/<marca>/posts/ templates/post/base-<marca>.html
```

- `validar` com saída diferente de 0 → **parar**: *"a identidade do <Marca> ainda não está
  completa no padrão — avise quem cuida do repositório"*.
- **Sem modelos de post da marca** (hoje é o caso do **Podi**) → **parar**: *"os modelos de
  post do Podi ainda não foram carregados no padrão — avise quem cuida do repositório"*.
  Nunca montar post do Podi com os modelos de outra marca, nem improvisar um layout.

**Optimall:** o post é **B2B** — fala com quem decide no shopping, nunca com o consumidor
final. Todo texto sai de `brand/optimall/mensagens.md`. Não cita o Podi nem a Tacla Labs —
nem no texto, nem no `alt`, nem na legenda. Sempre "o Optimall", nunca "a Optimall".

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
01  01-foto-titulo        capa: Sistema de gestão para ações promocionais
02  02-grade-recursos     3 modalidades de campanha
03  03-mockup-painel      o painel: tudo em tempo real
04  06-foto-faixa-cta     fecho: Seja cliente Optimall
```

O modelo se escolhe pelo **formato da informação** — tabela em
`design-system/post/<marca>/README.md`. Estrutura de carrossel em
`design-system/post/guidelines/carrossel.md`: 3 a 10 cards, capa, miolo com um ponto por card,
fecho com o CTA.

**Mostre o roteiro com o texto de cada card e espere a pessoa confirmar antes de montar.**

## 3. Montar

1. Copiar `templates/post/base-<marca>.html` para **`saida/<slug>/index.html`**.
2. Copiar os modelos escolhidos de `design-system/post/<marca>/posts/` para dentro do
   `<div class="grade">`, na ordem do roteiro, e preencher os `{{PLACEHOLDER}}`.
   Nunca gravar em `examples/`.
3. Criar `saida/<slug>/assets/` e colocar ali **todas** as imagens — as do briefing e as fixas
   copiadas de `brand/<marca>/assets/` (produto, clientes, grafismos). O post precisa abrir
   sozinho se alguém mandar a pasta.
4. Trocar os ícones genéricos dos chips pelo glifo certo do assunto, mantendo
   `fill="currentColor"` ou `stroke="currentColor"`.
5. O **logo não é imagem**: é o `<symbol>` que vem no template, usado por `<use href="#…">`,
   na versão certa para o fundo (`tokens.md` da marca). Nunca PNG, nunca `filter`.
6. **Nunca escrever cor solta.** Toda cor sai de `design-system/post/<marca>/tokens.md`, por
   `var(--token)`.
7. **O que não cabe vira outro card** — nunca fonte menor que o mínimo do `tokens.md`.
8. Escrever `saida/<slug>/legenda.txt` conforme `design-system/post/guidelines/legenda.md`
   (Instagram, LinkedIn e ALT de cada card).

Imagem com proporção fora do slot: **não distorça e não corte por conta própria.** Monte o
resto e relate no fim — qual arquivo, qual proporção veio, qual era esperada.

Foto que não existe: a direção visual não se inventa — está no Style Lock da marca. Monte com
a imagem de produto mais próxima de `brand/<marca>/assets/produto/`, relate, e ofereça o
prompt com `/foto-<marca>`.

## 4. Exportar

```bash
python3 scripts/exportar.py png saida/<slug>/index.html
```

- Saída 0 → um PNG por card em `saida/<slug>/png/`, na ordem do roteiro.
- *"A fonte … não está instalada"* → dizer em português comum: *"a fonte do <Marca> (Halyard
  Text) não está ativada neste computador — ative pelo Creative Cloud, em Fontes, e me avise
  para exportar de novo"*. Não exportar com outra fonte.

## 5. Quando falta algo no sistema

Se o conteúdo pede um modelo, uma cor ou um formato que não existe (story 9:16, quadrado,
um layout novo):

1. **Não invente.** Nada de cor nova nem layout improvisado com CSS solto.
2. Verifique se um dos modelos resolve com outro conteúdo.
3. Se realmente não resolve, monte o resto e **relate a ausência no fim**, marcada
   explicitamente como **proposta**.
4. Proposta não vira padrão sozinha. Quem decide é o maintainer (`docs/governanca.md`).

Se o pedido conflita com o brand — outra cor, texto escuro sobre o roxo do Optimall, logo
recolorido, falar com o consumidor num post do Optimall — **sinalize o conflito** em uma frase
e ofereça a alternativa que respeita o sistema. Se a pessoa reafirmar, é decisão dela: diga
que a peça sai fora do padrão e siga.

## 6. QA e entrega

Rodar `design-system/post/guidelines/qa-checklist.md` inteiro. Os itens verificáveis por comando:

```bash
f=saida/<slug>/index.html
grep -c '{{' $f                                     # 0 — nenhum placeholder
grep -o '<img[^>]*>' $f | grep -cv 'alt='           # 0
grep -o 'src="[^"]*"' $f | grep -v '^src="assets/'  # nada
grep -c 'class="post' $f                            # = número de cards do roteiro
python3 scripts/aplicar-marca.py conferir <marca> $f   # saída 0
python3 scripts/exportar.py png $f                     # saída 0
```

No Optimall, também: `grep -ci 'podi\|tacla' $f saida/<slug>/legenda.txt` → 0, e nenhum "a
Optimall".

Depois **abrir cada PNG** com a tool Read e conferir de olho: texto cortado, imagem que não
carregou, fonte trocada, nada fora da margem.

Relatar sempre, em português comum: onde estão os PNGs e a legenda, **a marca**, **quantos
cards e quais modelos**, imagens que precisam ser trocadas por versão final (com a dimensão),
e **o que do briefing não coube no padrão** — dizendo explicitamente o que ficou de fora e por quê.
