# PODI — Photography Style Lock
### Direção de fotografia de marca · App de shopping centers · Accent verde

> **Diretriz oficial de Brand do Marketing OS, marca Podi.** Nenhuma camada abaixo de `brand/`
> — design system, template, skill ou pedido de campanha — redefine o que está aqui.
> Contexto e o que é normativo: [`brand/photography/README.md`](../../photography/README.md).
>
> Documento gerado com a skill `brand-consistent-photography`.
> Fonte: 5 referências em `refs/` (Motorola-like, PicPay-like, Apple-like lifestyle mobile).
> **Ambiente padrão: interior de shopping center.** Outlet a céu aberto existe como trilha secundária (§4.B).
> **Como usar:** monte a cena e cole o bloco `STYLE LOCK` de §4.A sem alterar uma palavra.

---

## 1. Fase 1 — DNA Fotográfico extraído das referências

As 5 refs compartilham um mesmo sistema. Isto é o que precisa ser replicado:

### 1.1 Iluminação (Lighting DNA)
| Atributo | Leitura das refs |
| :--- | :--- |
| **Fonte** | Sol natural real, **direto ou semi-difuso**, vindo de **cima e ligeiramente atrás/lateral** (contraluz alta 3/4). Zero flash, zero luz de estúdio. |
| **Hora do dia** | Meio da manhã a fim de tarde (não golden hour extremo, não meio-dia a pino). Sol entre 30° e 55° de altura. |
| **Contraste** | **Médio-alto**, mas **high-key global** — o quadro inteiro é claro porque o fundo é céu/concreto claro. |
| **Sombras** | **Definidas, com borda semi-nítida** (não borradas de softbox, não recortadas a laser). Preenchidas por bounce natural do piso/parede clara → nunca chegam a preto. Sombras longas de arquitetura projetadas na parede aparecem como *gobo natural* (ver `a0658801`). |
| **Pele** | Guarda **brilho especular sutil** em testa, maçã do rosto e nariz. Pele **não** é matificada nem retocada em plástico. Poros e fios soltos de cabelo visíveis. |
| **Temperatura** | Split quente/frio: **pele neutra-quente ~5400K** contra **céu / vidro / metal frios ~6800K**. Essa separação é a assinatura mais forte do conjunto. |

### 1.2 Câmera & Óptica (Optical Setup)
- **Ângulo dominante: contra-plongée (low angle).** 4 das 5 refs colocam a câmera na altura do peito/cintura do sujeito, apontando levemente para cima. É isso que joga a pessoa **contra o alto** e cria a sensação de otimismo/altura.
- **Focais:** `50mm` e `85mm` nos closes de rosto+celular (`ref-1`, `b7471`); `35mm` nos planos médios com contexto arquitetônico (`5dbdff`, `a0658801`).
- **Abertura:** `f/2.0–f/2.8` nos closes (fundo limpo e cremoso, celular em foco), `f/4–f/5.6` nos planos com cenário legível.
- **Plano de foco:** sempre no **rosto + celular**. O celular frequentemente entra no quadro pela borda, em primeiro plano, e permanece nítido.
- **Sensor/textura:** digital limpo, alta resolução, **sem grão de filme, sem vignette, sem aberração cromática, sem halation**. Nitidez natural de lente boa, não sharpening artificial.

### 1.3 Cenário & Superfícies (Environment)
- **O fundo é céu** — gradiente azul quase sólido, ocupando 40–70% do quadro. É o elemento estrutural do sistema.
- Superfícies secundárias: **concreto claro cru**, **metal branco pintado**, **vidro**. Todas de baixa saturação e textura discreta.
- **Cenário sempre despoluído.** Nenhum ref tem multidão, cartaz competindo, lixo visual ou objeto solto atrás do sujeito.

### 1.4 Composição & Geometria
- Sujeito **descentralizado**, com bloco generoso de **espaço negativo** para entrada de headline/logo.
- **Crop decidido e confiante:** braços, ombros e topo da cabeça são cortados pela borda sem cerimônia. O celular entra pela lateral.
- **Diagonais fortes** de arquitetura atravessando o quadro (viga inclinada em `a0658801`, cabos/guarda-corpo em `5dbdff`).
- Linha do horizonte **baixa ou inexistente**.
- **Regra de olhar (invariável):** o sujeito **nunca olha para a câmera**. Por padrão o olhar vai para a **tela do celular**, com a cabeça levemente inclinada para baixo e expressão de reação genuína ao que vê. Quando a cena é sobre outra atividade (ler um livro, conversar, observar o shopping), o olhar vai para essa atividade — mas o **celular continua no quadro**, na mão ou apoiado perto, com o glow verde. É o celular que amarra a foto ao app; a pessoa está vivendo o momento, não posando.

### 1.5 Colorimetria & Paleta
- **Fórmula:** ambiente dessaturado (azul-céu pálido + concreto bege-cinza) **+ um único accent saturado** no vestuário/objeto. Nas refs esse accent é verde, mint, oliva ou laranja.
- **Saturação:** média-alta nos accents, **baixa no resto**. Não é um look "vibrance no talo" — é seletivo.
- **Curva:** **blacks levantados com viés ciano/azul** (nunca preto puro), highlights com rolloff suave, sem estouro.
- **Pele:** tons naturais. Nunca laranja, nunca amarelada.
- **Leitura de referência:** `a0658801` mostra o caso extremo e é o mais próximo do que a PODI precisa — **monocromia verde em camadas** (verde-escuro, verde-médio, verde-mint) contra concreto claro e céu azul.

### 1.6 Mood & Sensação
Jovem, solar, otimista, acessível, urbano. **Genuíno, não corporativo** — micro-expressões reais (sorriso contido, olho semicerrado pelo sol, boca fazendo bico de selfie). Diversidade real de idade, etnia, corpo e gênero é parte do sistema, não uma cota: as refs vão de mulher 25 a homem 65+.

---

## 2. Fase 2 — Tradução para o interior do shopping center

Aqui está o problema central, dito sem rodeio: **as refs foram feitas contra o céu, e dentro de um shopping não existe céu.** Copiar o prompt de exterior para dentro produz uma foto que não parece da mesma marca — fica escura, de luz mista amarelada, com fundo poluído.

A tradução honesta troca **o material do céu**, mantendo intactas as três coisas que realmente carregam a assinatura: o **contra-plongée**, o **split quente/frio de temperatura** e o **espaço negativo claro**.

### 2.1 As três substituições

| Nas refs (exterior) | No interior do shopping | Por quê funciona |
| :--- | :--- | :--- |
| **Céu** como fundo | **Claraboia + vazio claro do átrio** (teto branco, parede pálida cega, profundidade do corredor desfocada) | Entrega a mesma massa clara de espaço negativo; e a claraboia frequentemente deixa **o céu real aparecer** através do vidro |
| **Sol direto** no sujeito | **Feixe/mancha de sol descendo da claraboia**, com o sujeito posicionado *dentro* dele | Preserva a sombra de borda semi-nítida. Luz de claraboia difusa demais mata o contraste e o look inteiro |
| **Bounce do piso de concreto** | **Bounce do piso de pedra polida** | Piso polido de mall é um refletor melhor que concreto: levanta as sombras e ainda dá um reflexo claro no quadro |

> ### 🔒 REGRA DA LUZ DO DIA (substitui a Regra do Céu — não negociável)
> **O sujeito precisa estar iluminado por luz natural: claraboia, átrio envidraçado ou fachada de vidro full-height.**
> A luz artificial do shopping **nunca** ilumina o sujeito. Ela só pode existir como pequenos pontos de bokeh quente ao fundo.

### 2.2 O problema da luz mista (a armadilha nº 1 do interior)

Corredor de shopping é banhado em LED e halógena de varejo a **~3000K**. Isso destrói o split 5400K/6800K que é a assinatura mais forte das refs — a pele fica amarelada e a imagem perde a limpeza.

**Solução, nesta ordem:**
1. **Balanço de branco travado na luz do dia.** A luz de varejo cai naturalmente para o quente, e não o contrário.
2. **Sujeito posicionado dentro da luz natural**, nunca sob os spots de teto.
3. As lâmpadas de loja viram **bokeh quente pequeno e profundo no fundo** — isso não é defeito, é ganho: dá profundidade e faz o verde do sujeito saltar.

### 2.3 O problema do fundo poluído (armadilha nº 2)

Interior de mall é visualmente caótico: letreiro, vitrine, promoção, gente. As refs não têm nenhum ruído desses.

**Solução óptica, não de cenografia:** abrir a lente e comprimir.
- **Interior:** `85mm @ f/1.8–f/2.2` como padrão. Vitrine e multidão dissolvem em formas cremosas ilegíveis.
- Só descer para `35mm @ f/2.8–f/4` quando a arquitetura **precisa** ser lida (átrio, escada rolante, claraboia como assunto).
- Isso é uma diferença real em relação ao exterior, onde `50mm @ f/2.2` bastava — lá o fundo já era limpo.

### 2.4 Cenários aprovados — INTERIOR (padrão)

Todos entregam a Regra da Luz do Dia. Não inventar cenário fora desta lista.

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

### 2.5 Cenários aprovados — OUTLET A CÉU ABERTO (secundário)

Para peças de outlet. Usar o STYLE LOCK **§4.B**.

| # | Cenário |
| :-- | :--- |
| 9 | Rua de lojas do outlet com fachadas claras |
| 10 | Terraço / rooftop deck do mall |
| 11 | Porte-cochère / entrada coberta com pilares claros |
| 12 | Paisagismo do outlet — palmeiras, canteiro, *gobo* de folhas |

### 2.6 Paleta PODI

O verde oficial do Podi é **`#48DB84`** (`brand/podi/README.md`). Os nomes em inglês abaixo são a tradução
desse verde para o vocabulário que os geradores entendem — **não** hexadecimais alternativos.

```
ACCENT PRIMÁRIO   PODI Green      "vivid emerald green"        (dominante: camiseta, sacola, tela)
ACCENT ESCURO     PODI Deep       "deep pine green"            (jaqueta, calça, apoio)
ACCENT CLARO      PODI Mint       "soft mint green"            (case do celular, detalhe leve)
BASE 1 (interior) Vazio do átrio  "bright pale grey-white void, warm white ceiling"
BASE 2 (interior) Piso/parede     "pale polished stone, warm light travertine"
BASE 3            Estrutura       "off-white painted steel, clear glass, brushed aluminium"
BASE 4 (exterior) Céu             "pale desaturated sky blue"
NEUTRO            Sacolas/props   "cream, sand, warm white"
FUNDO PERMITIDO   Luz de loja     "small warm out-of-focus highlights, deep background only"
```

**Uso:** o verde entra em **até 3 camadas de valor diferentes** no mesmo quadro (escuro/médio/claro) — é o truque de `a0658801`. O resto do frame fica dessaturado. **Nunca** mais de um accent não-verde por imagem.

### 2.7 Matriz de Consistência (Do's & Don'ts)

| Elemento | ✅ Obrigatório (On-Brand) | ❌ Proibido (Off-Brand) |
| :--- | :--- | :--- |
| **Iluminação** | Sujeito **dentro** da luz de claraboia/vidro; feixe de sol definido; sombras com borda semi-nítida e fill de piso polido | Sujeito sob spot de teto de loja, LED/halógena de varejo na pele, luz mista, flash, HDR chapado sem sombra |
| **Temperatura** | WB travado na luz do dia; pele 5400K contra vidro/aço 6800K; loja caindo para o quente ao fundo | Pele amarelada por tungstênio, quadro inteiro morno, dominante verde de fluorescente |
| **Exposição** | Exposto para a luz do dia, high-key global, quadro claro | Interior escuro, abafado, subexposto, "foto de celular no corredor" |
| **Ângulo** | Contra-plongée da altura do peito; nível do olho como exceção | Plongée de cima, olho de peixe, dutch angle exagerado |
| **Fundo** | Vitrine e gente **dissolvidas** em bokeh cremoso ilegível; teto branco; parede pálida cega; claraboia | Letreiro legível, logo de terceiro, multidão em foco, painel de LED, corredor sem luz natural, poluição visual |
| **Óptica** | 85mm f/1.8–2.2 padrão; 35mm f/2.8–4 só quando a arquitetura é o assunto | Grande-angular com fundo todo nítido e legível |
| **Cor** | Verde em 3 valores + ambiente dessaturado | Segundo accent forte (vermelho/roxo/laranja), teal-and-orange, pele laranja |
| **Sombra** | Borda semi-nítida, base levantada e azulada | Preto puro esmagado, sombra dupla de flash, sombra borrada de softbox |
| **Sujeito** | Olhando a tela ou a atividade da cena, expressão real, pele com textura | Olhando para a câmera, sorriso forçado de banco de imagem, pele plastificada, pose corporativa |
| **Celular** | Sempre no quadro — segurado naturalmente ou apoiado perto —, nítido, case mint ou preto; tela com **glow verde suave e ilegível** | UI inventada e legível, texto/ícone falso, marca de celular reconhecível |
| **Enquadramento** | Espaço negativo generoso, crop confiante nas bordas | Sujeito centralizado com margem igual, quadro apertado sem respiro |

### 2.8 Negative prompt — modelos COM campo separado

```
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

**Só funciona em modelos com campo separado:** FLUX, SDXL, Ideogram, Stable Diffusion, Leonardo.
Para GPT Image, Gemini/Nano Banana e Midjourney, use §2.9.

### 2.9 CLEAN-FRAME CLAUSE — negative para modelos sem campo separado

GPT Image (ChatGPT / `gpt-image-1`), Gemini / Nano Banana e Midjourney não têm caixa de negative prompt. E aqui está a parte contra-intuitiva:

> **Colar a lista de §2.8 dentro do prompt desses modelos é pior que não colar nada.**
> Eles leem o prompt como instrução em prosa, não como vetor a subtrair. Escrever `crowd, busy signage, red accent` faz o modelo **pesar esses tokens** — e é comum a multidão e o letreiro aparecerem justamente por causa da lista. É o efeito "não pense em um elefante".

A técnica correta é **reformulação positiva**: cada proibição vira uma afirmação sobre o que *está* no quadro. O modelo não tem o que subtrair, então descreve a cena limpa.

Cole este bloco **depois** do STYLE LOCK. É uma unidade fechada, como o STYLE LOCK — não edite.

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

**Backstop opcional (só GPT Image).** Modelos instruction-tuned obedecem negação explícita em prosa, mas a obediência **cai conforme a lista cresce**. Se algo escapar, acrescente **uma** linha curta com no máximo 4 itens — os que falharam, não a lista toda:

```text
Do not include: readable text, crowds, retail lighting on the subject, a second accent colour.
```

**Midjourney.** Tem o parâmetro `--no`, que aceita poucos termos com eficácia real. Use a versão condensada, não a lista inteira:

```
--no text, signage, crowd, flash, orange skin, red, purple
```

### 2.10 Qual técnica por modelo

| Modelo | Negative | Como aplicar |
| :--- | :--- | :--- |
| **FLUX · SDXL · Ideogram · SD · Leonardo** | Campo separado | §2.8 na caixa de negative prompt. Não colar §2.9. |
| **GPT Image / ChatGPT** | Não tem | STYLE LOCK + **§2.9**. `Do not include:` só se algo escapar. |
| **Gemini / Nano Banana** | Não tem | STYLE LOCK + **§2.9** + 1–2 imagens de `refs/`. A imagem de referência vale mais que qualquer negative. |
| **Midjourney** | `--no` limitado | STYLE LOCK + `--no` condensado acima. §2.9 é opcional e deixa o prompt longo — prefira `--sref`. |

---

## 3. Fase 3 — Fórmula de slots

```
[TIPO DE SHOT] + [SUJEITO + AÇÃO NO APP] + [CENÁRIO INTERIOR §2.4] + [POSIÇÃO NA LUZ NATURAL]
+ [PROPS VERDES] + ⟪STYLE LOCK §4.A⟫ + ⟪CLEAN-FRAME CLAUSE §2.9 — só se o modelo não tiver campo de negative⟫
+ [PARÂMETROS]
```

O slot **[POSIÇÃO NA LUZ NATURAL]** é novo e é o mais importante do interior — é ele que impede a foto de cair na luz de varejo. Sempre diga onde o sujeito está em relação à claraboia ou ao vidro.

O `STYLE LOCK` é a parte que **nunca muda**. É ele que garante que 200 imagens geradas em 6 meses casem entre si.

---

## 4.A 🔒 STYLE LOCK — INTERIOR (padrão)

Cole este bloco **integralmente e sem edição** no fim de todo prompt de interior.

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

> **Ao usar 35mm** (cenários 1, 3, 5 — quando a arquitetura é o assunto), troque a frase da lente para:
> `Shot on Sony A7R V, 35mm lens at f/3.2, focus locked on face and phone, architecture legible but subordinate.`
> Essa é a **única** substituição autorizada dentro do bloco.

## 4.B 🔒 STYLE LOCK — OUTLET A CÉU ABERTO (secundário)

Para os cenários 9–12 de §2.5.

```text
STYLE LOCK — shot from a low camera angle looking slightly upward, subject placed off-center
with generous clean negative space above and to one side, confident crop where limbs and the
phone run off the frame edge, strong architectural diagonal crossing the background, low or
absent horizon line. Real natural sunlight from high three-quarter back, mid-morning to
late-afternoon sun, no artificial or flash lighting, crisp semi-hard shadows with soft edges
filled by bounce off pale concrete so shadows never reach pure black, natural gobo shadows of
pillars and foliage, subtle specular sheen on skin. Neutral-warm skin at 5400K against cooler
6800K sky, glass and metal. Medium-high contrast on an overall high-key frame, lifted
cyan-leaning shadows, gentle highlight rolloff, no clipping. Selective saturation: a
desaturated pale sky-blue and warm light-concrete environment carrying a single dominant
saturated green accent layered across three values — deep pine, vivid emerald, soft mint.
Natural skin tones, never orange. Natural unretouched skin texture with visible pores and
loose strands of hair. Subject is absorbed in the moment — eyes on their phone screen, or on what they are doing in
the scene such as a book, a companion or the mall itself — never on the camera, head slightly
tilted, genuine unposed micro-expression; the phone is always in frame, held in hand or resting
close by, its screen emitting a soft green glow, screen content indistinct and unreadable.
Clean high-resolution
digital capture, no film grain, no vignette, no chromatic aberration. Shot on Sony A7R V,
50mm lens at f/2.2, focus locked on face and phone. Editorial commercial advertising
photography, optimistic, youthful, sunlit, unpolished-real.
```

### Parâmetros por gerador

| Gerador | Sufixo |
| :--- | :--- |
| **Midjourney v6.1 / v7** | `--ar 4:5 --style raw --stylize 250 --v 6.1` (feed) · `--ar 9:16` (story) · `--ar 16:9` (banner/OOH) · `--ar 1:1` (thumb) · `--no` condensado de §2.9 |
| **FLUX.1 [dev/pro]** | `guidance 3.0–3.5`, `steps 30–40`, `1080×1350`. Sem `--` params; §2.8 na caixa de negative prompt. |
| **GPT Image / ChatGPT** | Sem parâmetros. Prompt + **CLEAN-FRAME CLAUSE §2.9** no mesmo bloco. Peça o aspect ratio em palavras (`vertical 4:5 portrait format`). |
| **Nano Banana / Gemini Image** | Envie **1–2 refs de `refs/` como imagem de entrada** + prompt + **§2.9**. Adicione: `match the lighting, color grading and low camera angle of the reference image exactly, but relocate the scene indoors under a mall skylight`. |
| **Ideogram / SDXL** | `style: photographic`, §2.8 na caixa de negative, CFG 4–6. |

### 🎯 Consistência entre lotes (importante)
1. **Seed fixa por família de imagem.** No Midjourney, gere uma imagem-mãe aprovada, pegue o `--seed` e reutilize nas variações do mesmo cenário.
2. **Style Reference.** Depois de aprovar 3–5 imagens da marca, use-as como `--sref <urls> --sw 100` em toda geração seguinte. Isso trava o look melhor que qualquer texto — **e no interior isso vale ainda mais**, porque descrever luz mista em palavras é frágil.
3. **Character Reference.** Para reaproveitar a mesma pessoa (ex.: uma campanha com 6 peças), use `--cref <url> --cw 100`.
4. **Nunca** rode dois cenários diferentes na mesma seed esperando coerência — a seed trava a luz, não a cena.

---

## 5. Fase 4 — Suíte de variações prontas (interior)

Todos já estão no formato final. **Concatene o bloco `STYLE LOCK` de §4.A no fim de cada um** e acrescente os parâmetros.
Se o modelo **não tiver campo de negative** (GPT Image, Gemini), acrescente também a **CLEAN-FRAME CLAUSE de §2.9**.

### 5.1 HERO — a imagem principal da marca
> Uso: home do site, capa de app store, abertura de deck. · Cenário 2

```text
Low-angle medium close-up portrait of a woman in her late twenties with natural curly hair,
wearing a vivid emerald green sweatshirt, holding a phone with a soft mint green case up in
her right hand and smiling as she looks down at the screen. She stands at the glass balustrade
of a shopping mall upper mezzanine, standing directly inside the pool of daylight falling from
the atrium skylight above her, the bright pale void of the atrium and the glass roof filling
the top two thirds of the frame.
+ ⟪STYLE LOCK §4.A⟫ --ar 4:5 --style raw --stylize 250 --v 6.1
```

### 5.2 CAMPANHA PROMOCIONAL — participação / sorteio
> Uso: banner de campanha, push, feed. · Cenário 1

```text
Low-angle three-quarter shot of two friends in their early twenties standing side by side in
the central atrium of a shopping mall, both standing inside a bright shaft of sunlight
descending from the glass skylight, one in a deep pine green jacket and one in a soft mint
green windbreaker, both leaning in to look at one phone screen together, one laughing with an
open mouth. Cream paper shopping bags in their free hands. Pale polished stone floor bouncing
light back onto them, off-white steel skylight mullions casting long diagonal gobo shadows on
the wall behind, blue sky visible through the glass roof above.
+ ⟪STYLE LOCK §4.A⟫ 35mm lens at f/3.2 --ar 4:5 --style raw --stylize 250 --v 6.1
```

### 5.3 RESGATE DE DESCONTO / CUPOM
> Uso: fluxo de cupom, tela de onboarding, ilustração de feature. · Cenário 8

```text
Low-angle close-up of a man in his thirties with a short beard, wearing a vivid emerald green
t-shirt, holding his phone forward at chest height with the screen turned slightly toward a
blurred store counter, his other hand holding a cream shopping bag, eyes down on the screen
with a small satisfied smile. He stands just outside a boutique entrance in a mall concourse,
lit by the daylight spilling from the skylight above him and not by the store lighting, the
glass storefront behind him dissolved into creamy out-of-focus shapes with small warm
highlights deep in the background.
+ ⟪STYLE LOCK §4.A⟫ --ar 4:5 --style raw --stylize 250 --v 6.1
```

### 5.4 INFORMAÇÃO / MAPA DO SHOPPING
> Uso: feature de wayfinding, horários, "onde fica". · Cenário 3

```text
Low-angle medium shot of a woman in her fifties with silver-grey hair, wearing a soft mint
green linen shirt, standing at the top of an escalator inside a mall atrium, one hand on the
glass balustrade and the other holding her phone up as she reads the screen and looks slightly
off to the side as if locating a store. A full-height glazed atrium wall behind her floods the
frame with daylight, a sliver of pale blue sky and a distant treetop visible through the
glass, the strong diagonal of the escalator handrail crossing the lower frame.
+ ⟪STYLE LOCK §4.A⟫ 35mm lens at f/3.2 --ar 4:5 --style raw --stylize 250 --v 6.1
```

### 5.5 DETALHE / MACRO — mãos e celular
> Uso: seção de features, divisor de página, thumbnail. · Cenário 5

```text
Low-angle tight detail shot of two hands holding a phone with a soft mint green case, thumb
mid-scroll, a vivid emerald green sleeve cuff and a cream shopping bag handle visible at the
frame edge, the hands sitting inside a bright band of sunlight from a linear skylight
overhead, sharp focus on the knuckles and the phone body, the phone screen glowing soft green
and unreadable. Background is the deeply blurred pale stone concourse of a shopping mall with
a few small warm store highlights and the bright white ceiling in the upper corner.
+ ⟪STYLE LOCK §4.A⟫ 85mm lens at f/1.8 --ar 1:1 --style raw --stylize 250 --v 6.1
```

### 5.6 EDITORIAL / OOH — máximo espaço negativo
> Uso: outdoor, capa, hero com headline grande. · Cenário 1

```text
Extreme low-angle wide shot of a young man in a deep pine green tracksuit standing alone in
the middle of a vast empty shopping mall atrium, small in the lower right of the frame,
standing inside a single bright patch of sunlight on the pale polished stone floor, looking
down at his phone and grinning. The upper three quarters of the image is the clean bright void
of the atrium and its glass skylight, with pale blue sky beyond the glass. A single off-white
steel balustrade runs as a diagonal across the bottom edge.
+ ⟪STYLE LOCK §4.A⟫ 35mm lens at f/4 --ar 16:9 --style raw --stylize 250 --v 6.1
```

### 5.7 SOCIAL / STORY — vertical
> Uso: Reels, Stories, TikTok cover. · Cenário 7

```text
Low-angle vertical portrait of a teenage girl with braided hair, wearing a vivid emerald green
cropped hoodie over a warm white top, walking through the indoor garden lounge of a shopping
mall while looking down at her phone and smiling. Large planter foliage lit by the skylight
above casts crisp gobo shadows across her shoulder and the pale stone paving. The bright white
atrium ceiling and glass roof occupy the top third of the frame, the concourse behind her
dissolved into soft out-of-focus shapes.
+ ⟪STYLE LOCK §4.A⟫ --ar 9:16 --style raw --stylize 250 --v 6.1
```

### 5.8 FAMÍLIA / MULTI-PESSOA
> Uso: comunicação institucional, campanha de datas comemorativas. · Cenário 4

```text
Low-angle group shot of a family of three — a father in a deep pine green polo, a mother in a
soft mint green blouse and a child of about eight — sitting at a pale stone table in a mall
food court beside a full-height glazed wall, the mother holding her phone so all three can
look at the screen together, all three smiling down at it. Cream shopping bags at their feet.
Late-afternoon daylight rakes across them from the glass wall on the left, off-white steel
window mullions casting long diagonal shadows over the table, bright pale sky visible through
the glazing.
+ ⟪STYLE LOCK §4.A⟫ 35mm lens at f/3.2 --ar 4:5 --style raw --stylize 250 --v 6.1
```

---

## 6. Checklist de validação (antes de aprovar qualquer imagem)

Rejeite a imagem se qualquer item falhar.

**Invariantes de marca**
- [ ] A câmera está **abaixo** da linha dos olhos do sujeito?
- [ ] O sujeito está olhando **a tela ou a atividade da cena**, e não a câmera? O **celular está no quadro**?
- [ ] As sombras têm **borda definida** e **base azulada não-preta**?
- [ ] Existe **um único accent**, e ele é **verde**?
- [ ] O verde aparece em **mais de um valor** (escuro/médio/claro)?
- [ ] A tela do celular está **ilegível** (só glow verde), sem UI inventada?
- [ ] A pele tem **textura e brilho especular** — não está plastificada?
- [ ] Há **espaço negativo** suficiente para entrar headline/logo?
- [ ] As **mãos** estão corretas (5 dedos, celular sem deformação)?

**Específicos de interior** *(onde a maioria das gerações falha)*
- [ ] O sujeito está **dentro da luz natural** (claraboia/vidro) — e não sob spot de loja? *(Regra da Luz do Dia)*
- [ ] A **pele está neutra**, sem dominante amarela de tungstênio? Existe o split quente/frio?
- [ ] O quadro está **claro e high-key** — não escuro, abafado ou "corredor de shopping"?
- [ ] A luz de varejo aparece **só como bokeh quente ao fundo**, sem tocar o sujeito?
- [ ] Vitrine, letreiro e transeuntes estão **dissolvidos e ilegíveis**? Zero logo de terceiro?
- [ ] O **teto branco / vazio do átrio / claraboia** está fazendo o papel que o céu fazia nas refs?

---

## 7. Prompt único (versão "copy-paste total" — interior)

Para quem quer um bloco só, sem montar slots. Troque apenas o texto entre `⟨ ⟩`.

### 7.1 Para modelos COM campo de negative (Midjourney, FLUX, SDXL, Ideogram)

O negative vai separado — use §2.8 na caixa própria.

```text
Low-angle ⟨medium close-up⟩ of ⟨a woman in her late twenties with natural curly hair⟩ wearing
⟨a vivid emerald green sweatshirt⟩, holding a phone with a soft mint green case and looking
down at the screen with a genuine ⟨smile⟩, standing ⟨at the glass balustrade of a shopping mall
upper mezzanine⟩ and positioned directly inside the pool of daylight falling from the atrium
skylight above, the bright pale void of the atrium filling the upper portion of the frame.
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
--ar 4:5 --style raw --stylize 250 --v 6.1
```

### 7.2 Para modelos SEM campo de negative (GPT Image / ChatGPT, Gemini / Nano Banana)

Bloco único e autossuficiente: cena + STYLE LOCK + CLEAN-FRAME CLAUSE, com o formato pedido em
palavras em vez de `--ar`. **Nada de lista de keywords negativas aqui** — o motivo está em §2.9.

```text
A vertical 4:5 portrait-format photograph. Low-angle ⟨medium close-up⟩ of ⟨a woman in her late
twenties with natural curly hair⟩ wearing ⟨a vivid emerald green sweatshirt⟩, holding a phone
with a soft mint green case and looking down at the screen with a genuine ⟨smile⟩, standing ⟨at
the glass balustrade of a shopping mall upper mezzanine⟩ and positioned directly inside the
pool of daylight falling from the atrium skylight above, the bright pale void of the atrium
filling the upper portion of the frame.

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

**Formato em palavras** — esses modelos ignoram `--ar`:

| Peça | Escrever no início do prompt |
| :--- | :--- |
| Feed | `A vertical 4:5 portrait-format photograph.` |
| Story | `A tall vertical 9:16 photograph.` |
| Banner / OOH | `A wide 16:9 landscape photograph.` |
| Thumbnail | `A square 1:1 photograph.` |

---

## 8. Nota sobre o verde

**Decidido:** o verde oficial do Podi é **`#48DB84`** — matiz ~145°, dentro da faixa emerald.
Os três valores padrão abaixo ficam **confirmados** como a tradução dele; as variantes lime e
jade seguem documentadas apenas como registro do que foi descartado.

Os prompts usam **"vivid emerald green" / "deep pine green" / "soft mint green"** como valores padrão, escolhidos por serem os que mais se aproximam da monocromia verde de `refs/a0658801`. Se o verde oficial do Podi fosse mais **amarelado** (lime/spring), os termos seriam `vivid spring green` / `deep olive green` / `pale pistachio green`; se fosse mais **azulado** (teal/jade), seriam `vivid jade green` / `deep teal green` / `pale seafoam green`. Mantenha sempre a estrutura de **três valores** — é ela que dá profundidade sem quebrar a monocromia.

**No interior o verde importa mais.** O ambiente de mall é cinza-pedra e branco, muito mais neutro que o azul-céu do exterior — então o accent verde é praticamente a única cor do quadro. Isso é bom para a marca, mas exige que o verde apareça em **volume suficiente** (peça de roupa inteira, não detalhe) para o frame não ler como uma foto dessaturada por acidente.
