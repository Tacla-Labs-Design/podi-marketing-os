# Como usar o Podi Marketing OS

Guia de primeira vez. Você não precisa saber HTML nem mexer em nada técnico — precisa
saber escrever o conteúdo e organizar uma pasta. O resto é um comando.

Este é o documento do vídeo de apresentação. Se você chegou aqui pelo vídeo, siga na ordem:
o passo 1 instala o padrão no seu computador, e o passo 4 monta o primeiro e-mail.

---

> ## Se você é o Claude Code lendo este documento
>
> A pessoa acabou de te dar o link deste repositório e pediu para você prepará-lo. Faça,
> nesta ordem:
>
> 1. **Baixe o repositório** para uma pasta na máquina dela e entre nessa pasta.
> 2. **Leia o [`CLAUDE.md`](../CLAUDE.md) da raiz.** Ele é a camada global: hierarquia de
>    autoridade, regras não negociáveis e como falar com quem usa o repositório — que não
>    é uma pessoa técnica. Nunca peça comando de Git a ela.
> 3. **Reconheça as skills.** Elas já vêm no repositório, em `.claude/skills/`. Não é
>    preciso instalar nada: basta abrir o Claude Code dentro da pasta que
>    `/newsletter-podi`, `/apresentacao-podi`, `/post-podi` e `/foto-podi` ficam disponíveis.
>    Confirme que os quatro aparecem e diga isso em português.
> 4. **Confirme em uma frase** que está pronto e pergunte qual material ela quer montar.
>
> Não altere `brand/`, `design-system/`, `templates/`, `.claude/skills/`, `examples/`,
> `docs/` nem o `CHANGELOG.md`. O trabalho nasce em `saida/`.

---

## O que vamos ver

1. **A primeira vez** — instalar o padrão no seu computador, uma vez só
2. **As três skills** — um comando por tipo de material
3. **Montando um Podi News** — da pasta de briefing ao e-mail pronto
4. **O que ele nunca deixa passar** — as regras que protegem a marca sozinhas

---

## O problema: cada peça recomeçava do zero

Cor escolhida na hora, bloco improvisado, link do app digitado à mão. Nenhuma peça saía
errada o bastante para alguém reclamar — e nenhuma saía igual à anterior.

O Marketing OS existe para que a decisão de padrão seja tomada **uma vez**, e não a cada
envio.

### As quatro camadas

| Camada | O que é |
|---|---|
| **Brand** | A identidade: cor, logo, fotografia, links fixos. Nada abaixo pode contradizer. |
| **Design System** | Como cada material se constrói: tokens, blocos prontos, checklist de QA. |
| **Templates** | O esqueleto da peça. Nunca editado por campanha. |
| **Skills** | O comando que você digita. É ele que executa tudo acima. |

Quando duas camadas discordam, **a de cima ganha** — e o Claude avisa em vez de mudar a
marca por conta própria.

---

## 1. A primeira vez

Instalar o padrão no seu computador. Leva alguns minutos, e você faz isso **uma vez só**.

**1 · Abra o Claude.** O aplicativo do Claude no seu computador. Entre com a sua conta do Podi.

**2 · Vá para o Claude Code.** É a parte do app que trabalha com pastas do seu computador,
e não só com conversa.

**3 · Cole o link e peça.** Cole o endereço do repositório e escreva, com essas palavras
mesmo:

```
https://github.com/Tacla-Labs-Design/podi-marketing-os

Instala esse repositório aqui, lê o docs/como-usar.md e deixa as skills prontas.
```

**4 · Pronto.** Ele baixa a pasta sozinho. Da próxima vez, você só abre essa mesma pasta.

Não estamos instalando um programa — estamos trazendo uma pasta com o padrão da marca
dentro.

### Você nunca mais faz isso

A instalação é **uma vez por computador**. Depois, é só abrir a pasta e pedir.

E antes de montar qualquer coisa, ele traz sozinho a versão mais recente do padrão — você
não precisa atualizar nada, nem saber que existe versão.

---

### Teste antes de ter conteúdo real

O repositório já vem com um briefing fictício em
[`examples/briefing-demo/`](../examples/briefing-demo/) — textos e imagens nos nomes certos.
Para montar o primeiro e-mail agora mesmo, peça:

> Copia o briefing de demonstração para o meu inbox e monta a newsletter

O resultado aparece em `saida/`, e serve para você ver o padrão funcionando antes do
primeiro envio de verdade.

---

## 2. Um comando por material

Todos terminam com o nome da marca — **`-podi`**. O sufixo existe porque a ferramenta tem
dezenas de comandos próprios, e você precisa saber, na hora de digitar, qual é o da marca.

| Comando | O que faz |
|---|---|
| **`/newsletter-podi`** | Monta a newsletter, o Podi News ou o informativo interno a partir da sua pasta de briefing. |
| **`/apresentacao-podi`** | Monta um deck 16:9 como o desta apresentação, pronto para virar PDF. Confirma o roteiro com você antes. |
| **`/post-podi`** | Monta um post ou carrossel 1080×1350, entrega os PNGs e a legenda. *No Podi, os modelos ainda não foram carregados — ele avisa.* |
| **`/foto-podi`** | Escreve o prompt de uma foto de marca seguindo a direção fotográfica oficial. |

### O que ele resolve sozinho, e o que ele pergunta

| Ele pergunta antes de decidir | Ele resolve sem perguntar |
|---|---|
| Qual imagem é de qual notícia, quando o nome do arquivo não diz | Layout, hierarquia e ordem dos blocos |
| Se a edição é para cliente final ou para o time interno | Cor, dark mode e versão mobile |
| O que fazer quando o briefing pede algo que não existe no padrão | Subject, preheader e o QA técnico do e-mail |

A coluna da direita é o que você deixa de fazer. A da esquerda é o que ele **não** adivinha
— e é de propósito: errar a associação entre imagem e notícia é pior que uma pergunta a mais.

---

## 3. Montando um Podi News

Quatro passos, e nenhum deles é técnico.

**1 · Prepare a pasta.** Em `projects/_inbox/`, uma pasta `AAAA-MM-frente-assunto` com o
documento e as imagens dentro.

**2 · Peça.** `/newsletter-podi 2026-09-cliente-podi-news` — ou pede em português mesmo:
*"gera a newsletter de projects/_inbox/2026-09-cliente-podi-news"*.

**3 · Confira.** Ele abre no navegador e conta o que do briefing não caiu no e-mail, e por quê.

**4 · Entregue.** Você recebe o arquivo, o subject, o preheader e a lista de imagens para
hospedar.

### O nome do arquivo é a instrução

Esta é a parte que mais economiza retrabalho. O nome do arquivo diz de qual notícia é a
imagem e como ela vai ser usada.

| Nome do arquivo | Onde aparece | Proporção | Mínimo |
|---|---|---|---|
| `capa.jpg` | Abertura da edição | 16:9 ou mais larga | 1072 × 602 |
| `01-cinema.jpg` | Topo do bloco 01 | 16:9 ou mais larga | 1072 × 604 |
| `03-clube-1x1.jpg` | Ao lado do texto | 1:1 exata | 496 × 496 |
| `foto-legal.jpg` | Sem número, ele não adivinha | — | Ele pergunta |

O guia completo de briefing e nomes está em
[`docs/como-enviar-conteudo.md`](como-enviar-conteudo.md). Leia antes do primeiro envio.

### Ele não inventa padrão

Se o conteúdo pede um bloco, uma cor ou um layout que não existe, ele monta o resto do
e-mail e relata a ausência no fim, marcada como **proposta**.

Proposta não vira padrão sozinha — quem decide é quem cuida do repositório. É isso que
impede o padrão de virar uma coleção de exceções.

---

## 4. As regras que ele nunca quebra

- O verde da marca nunca é cor de texto
- Texto sobre o verde é sempre preto, nunca branco
- Em e-mail do Podi, só `{{email}}`, `{{topicId}}` e `{{campaignId}}` — e nenhum link de descadastro
- O link do app é fixo e não se digita à mão
- No máximo 4 blocos de conteúdo por envio
- Nenhuma cor escrita fora dos tokens
- Imagem fora da proporção ele relata, nunca corta sozinho
- Assinatura Podi + Tacla Labs no topo de toda peça do Podi
- O Podi é masculino: **o Podi**, **do Podi** — nunca "a Podi"

Duas delas valem a explicação: as **variáveis** não são preciosismo — o servidor de envio
resolve só aquelas três, e qualquer outra derruba a campanha inteira (é por isso que não
existe link de descadastro no HTML). E o **verde que nunca é texto** dá 1,79:1 de
contraste — reprova em qualquer leitura.

---

## O que já está pronto para usar

| | |
|---|---|
| **18** | blocos de e-mail prontos, do header ao rodapé legal |
| **16** | tipos de slide de apresentação |
| **3** | comandos — um por tipo de material |

Nada disso precisa ser criado de novo.

---

## Dúvidas que sempre aparecem

**"Preciso instalar alguma coisa além do Claude?"**
Não. Você cola o link e pede — ele resolve o resto.

**"E se eu não gostar do resultado?"**
Você pede a mudança em português. Ele remonta.

**"Posso mudar a cor de uma campanha?"**
Pode pedir — ele vai sinalizar que sai do padrão e explicar a regra. Se você confirmar, ele
faz e avisa que a peça saiu fora do padrão.

**"Como sei que estou com a versão certa do padrão?"**
Ele atualiza sozinho antes de montar. Se não conseguir, ele para e avisa — aí é falar com
quem cuida do repositório.

**"Onde fica o material que eu montei?"**
Em `saida/<nome-da-pasta>/`. É pasta local, no seu computador: não vai para o Git e não
afeta ninguém.

---

## Para continuar

- **Como enviar conteúdo:** [`docs/como-enviar-conteudo.md`](como-enviar-conteudo.md)
- **A marca:** [`brand/README.md`](../brand/README.md)
- **Índice das skills:** [`skills/README.md`](../skills/README.md)
- **O que mudou no padrão:** [`CHANGELOG.md`](../CHANGELOG.md)

O padrão é do time. O comando é seu.
