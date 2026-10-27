# Podi · foto de marca (prompt)

Transforma um pedido em português ("foto de alguém resgatando cupom", "hero do site") num
prompt pronto para gerador de imagem. A saída é texto; a imagem é gerada fora.

## Briefing

Obrigatório: o que a foto mostra (quem, fazendo o quê) e onde ela vai.

Padrão se faltar — não pergunte se dá para inferir:
- Formato: Instagram feed → 4:5 · story → 9:16 · banner, site ou OOH → 16:9 · miniatura → 1:1.
- Cenário: um dos 8 de interior abaixo. Outlet a céu aberto só se o pedido disser outlet
  (aí o caso é do repositório, que tem o bloco próprio).
- Lente: 85mm f/2.0. 35mm f/3.2 só quando a arquitetura é o assunto (cenários 1, 3 e 5).

## As decisões de todo prompt

| Slot | O que decidir |
|---|---|
| Tipo de shot | close, plano médio, plano aberto |
| Sujeito + ação | pessoa real (25 a 65+, diversa), absorvida no que faz: no app (campanha, cupom, mapa) ou num momento sem o app em uso (ler, conversar), com o celular no quadro |
| Cenário | um dos 8 abaixo — **não inventar outro** |
| Posição na luz | **obrigatório**: onde o sujeito está em relação à claraboia ou ao vidro. Sem isso o gerador põe luz de loja no rosto |
| Props verdes | roupa em 1 ou 2 valores de verde + capa do celular mint ou sacola. O verde precisa de volume: peça inteira, não detalhe |

| # | Cenário | Como a luz natural entra |
| :-- | :--- | :--- |
| 1 | **Átrio central sob claraboia** — sujeito dentro da mancha de sol no piso | Feixe vertical de topo; céu real visível pelo vidro |
| 2 | **Mezanino / guarda-corpo de vidro** do piso superior | Contra-plongée com claraboia atrás; luz de topo |
| 3 | **Escada rolante contra átrio envidraçado** | Diagonal forte + luz alta lateral |
| 4 | **Praça de alimentação com fechamento de vidro** full-height | Janela lateral gigante, luz rasante 3/4 |
| 5 | **Corredor com claraboia longitudinal** (*linear skylight*) | Faixa de sol correndo pelo piso e pela parede |
| 6 | **Hall de entrada envidraçado** | Luz rasante entrando pelas portas de vidro, sombras longas |
| 7 | **Jardim interno / lounge sob claraboia** | Luz de topo + *gobo* de folhas de planta no sujeito |
| 8 | **Vitrine como fundo abstrato**, sujeito na luz da claraboia | Sujeito no natural, loja dissolvida em bokeh |

## Montar o prompt

```
[TIPO DE SHOT] + [SUJEITO + AÇÃO] + [CENÁRIO] + [POSIÇÃO NA LUZ NATURAL] + [PROPS VERDES]
+ STYLE LOCK + (CLEAN-FRAME CLAUSE, só em gerador sem campo de negative) + parâmetros
```

O prompt sai **em inglês**; a conversa é em português. O verde já está traduzido no bloco
(`deep pine`, `vivid emerald`, `soft mint`): não invente outro nome de cor e nunca escreva hex.

### STYLE LOCK — copiar sem mudar uma palavra

A única troca permitida é a frase da lente, inteira, quando a lente for 35mm:
`Shot on Sony A7R V, 35mm lens at f/3.2, focus locked on face and phone, architecture legible but subordinate.`

```text
STYLE LOCK — shot from a low camera angle looking slightly upward, subject placed off-center
with generous clean negative space above and to one side filled by the bright pale void of the
atrium, its warm white ceiling and the glass skylight, a fragment of real blue sky visible
through the glass, confident crop where limbs and the phone run off the frame edge, strong
architectural diagonal of a glass balustrade, escalator or mezzanine slab crossing the
background, no horizon line. Lit only by real daylight falling from a large glass skylight
overhead and a full-height glazed facade, a defined shaft of sunlight landing on the subject,
crisp semi-hard shadows with soft edges filled by bounce off the pale polished stone floor so
shadows never reach pure black, natural gobo shadows of skylight mullions and structural beams
raking across the wall, subtle specular sheen on skin. White balance anchored to daylight:
neutral-warm skin at 5400K against cooler 6800K glass, steel and shade, while the mall's
retail lighting stays out of the daylight and reads only as small warm out-of-focus highlights
deep in the background, never touching the subject. Medium-high contrast on an overall
high-key frame exposed for the daylight, lifted cyan-leaning shadows, gentle highlight
rolloff, no clipping. Selective saturation: a desaturated pale stone-grey, warm travertine and
white environment carrying a single dominant saturated green accent layered across three
values — deep pine, vivid emerald, soft mint. Natural skin tones, never orange. Natural
unretouched skin texture with visible pores and loose strands of hair. Storefronts, signage
and passers-by dissolved into clean creamy out-of-focus shapes with no readable text or logos.
Subject is absorbed in the moment — eyes on their phone screen, or on what they are doing in
the scene such as a book, a companion or the mall itself — never on the camera, head slightly
tilted, genuine unposed micro-expression; the phone is always in frame, held in hand or resting
close by, its screen emitting a soft green glow, screen content indistinct and unreadable.
Clean high-resolution digital capture, no film
grain, no vignette, no chromatic aberration. Shot on Sony A7R V, 85mm lens at f/2.0, focus
locked on face and phone, background strongly compressed and separated. Editorial commercial
advertising photography, optimistic, youthful, sunlit, unpolished-real.
```

### CLEAN-FRAME CLAUSE — GPT Image, Gemini e Midjourney

Esses geradores não têm campo de negative. Cole este bloco depois do STYLE LOCK, sem editar:

```text
CLEAN-FRAME CLAUSE — this is a real photograph taken on a camera. Shadows are present and
directional, and the darkest tone in the frame is a soft cool grey rather than black. Every
edge is crisply frozen, corner brightness is even, and the optics are neutral and modern.
Skin keeps its pores, fine lines and stray hairs. Exactly one saturated hue exists in the
image and it is green; every other surface is pale stone grey, warm white, cream or clear
glass. The concourse is quiet and nearly empty, and the few distant figures read as soft
featureless shapes. Storefronts are unbranded and dissolve into smooth creamy blur. The image
contains no writing of any kind: no signage, no banners, no screens with interfaces, no
watermark, no caption. The phone is a plain rectangular slab with an unbranded body, and its
screen is a single soft green glow with no shapes or icons in it. Hands are anatomically
correct with five fingers each. The subject's eyes stay on the phone screen or on what they are
doing in the scene, never on the camera; the phone is always somewhere in the frame, and the
posture is relaxed and caught mid-moment rather than held for the camera.
```

### Negative — FLUX, SDXL, Ideogram, Stable Diffusion, Leonardo

Na caixa de negative prompt, nunca dentro do prompt:

```text
studio lighting, flash photography, harsh on-camera flash, indoor fluorescent light, retail
LED lighting on subject, ceiling spotlight on face, tungsten orange cast, mixed white balance,
warm yellow skin, dim underexposed interior, murky shadows, HDR, flat lighting, no shadows,
crushed blacks, heavy film grain, vignette, chromatic aberration, lens flare, motion blur,
looking at camera, forced smile, stock photo pose, plastic retouched skin, over-smoothed skin,
teal and orange grade, oversaturated, neon, purple, magenta, red accent, cluttered background,
crowd in focus, busy signage, readable store signage, readable third-party logos, sale banners,
LED video wall, fake UI on phone screen, legible text on screen, extra fingers, deformed hands,
warped phone, low resolution, watermark, text overlay, illustration, 3d render, cgi, cartoon
```

Midjourney: `--no text, signage, crowd, flash, orange skin, red, purple`.

### Parâmetros

| Gerador | Como |
|---|---|
| Midjourney | `--ar 4:5 --style raw --stylize 250 --v 6.1` (troque o `--ar` pelo formato) |
| FLUX | guidance 3.0–3.5, steps 30–40, tamanho do formato; negative na caixa |
| GPT Image / ChatGPT | sem parâmetros: abra o prompt com o formato em palavras (`A vertical 4:5 portrait-format photograph.`) |
| Ideogram / SDXL | `style: photographic`, CFG 4–6, negative na caixa |

**Tela do celular nunca se gera legível:** só o brilho verde. A tela real do app entra depois,
na montagem.

## Entregar

Um bloco com: o prompt completo, o negative (para quem tem o campo), a versão para GPT Image
e Gemini (prompt + CLEAN-FRAME), os parâmetros e 2 a 4 linhas de direção (o que reforçar se
sair errado). Sem texto de explicação longo: quem lê é designer.

## Conferência (rejeite a imagem se algo falhar)

- [ ] Câmera abaixo da linha dos olhos; o sujeito nunca olha para a câmera; o celular está no quadro.
- [ ] Sombras com borda definida e base azulada, nunca preta.
- [ ] Um único accent, verde, em mais de um valor (escuro, médio, claro).
- [ ] Tela do celular ilegível, só o brilho verde; mãos com cinco dedos.
- [ ] Pele com textura, neutra, sem amarelo de luz de loja.
- [ ] Sujeito dentro da luz natural; a luz de loja só como bokeh quente ao fundo.
- [ ] Quadro claro (high-key), com espaço negativo para título ou logo.
- [ ] Vitrine, letreiro e transeuntes dissolvidos; nenhum logo de terceiro.
