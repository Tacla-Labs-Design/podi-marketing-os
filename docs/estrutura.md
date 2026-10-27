# Estrutura do repositório

Mapa comentado. Visão para quem usa está no [README](../README.md).

```
brand/                                   IDENTIDADE — camada mais alta
├── README.md                            Regras comuns às marcas, qual marca é a peça, marca nova
├── photography/README.md                Como ler um Style Lock (vale para as duas marcas)
├── podi/
│   ├── README.md                        Marca, cor, roxo de detalhe, contraste, as duas frentes, empreendimento
│   ├── links-oficiais.md                Link do app, rodapé legal, redes, textos fixos do deck
│   ├── marca.json                       Os mesmos valores, para máquina (paleta por papel, links, envio)
│   ├── photography/
│   │   ├── STYLE-LOCK-PODI.md           Direção fotográfica oficial — blocos copiados byte a byte
│   │   └── refs/                        As referências que originaram o Style Lock
│   └── assets/
│       ├── header/                      Logos Podi e Tacla Labs; logo-podi.svg é o vetor monocromático
│       ├── icones/                      Ícones sociais — 4 redes × 3 variantes
│       ├── end-news-img.jpg             Imagem fixa do fecho "Podi e você"
│       └── hero-podi-news.png           Arte do hero do Podi News
└── optimall/                            Marca B2B, aprovada em 2026-09-30
    ├── README.md                        Cor, tipografia (Halyard), logo tricolor, grafismos
    ├── mensagens.md                     O que dizer: módulos, números oficiais, voz, frases aprovadas
    ├── links-oficiais.md                CTA, contato, rodapé legal, redes, textos fixos
    ├── marca.json                       Fonte de máquina: cores, paleta_extra, logo, links, contato
    ├── assets/
    │   ├── header/                      Logo positivo, negativo, símbolo (SVG) e PNG 2x do e-mail
    │   ├── icones/                      Ícones sociais roxos, gerados pelo script
    │   ├── icones-ui/                   Ícones HugeIcons bulk (currentColor) dos chips
    │   ├── clientes/                    Logos dos shoppings clientes (roxo do deck e cinza do site)
    │   ├── parceiros/                   Logos das integrações
    │   ├── produto/                     Telas do painel e do app (deck-*, post-*)
    │   ├── fotos/                       Fotos aprovadas dos posts
    │   └── grafismos/                   Símbolo gigante, vidros, elipse e demais grafismos do Figma
    └── photography/STYLE-LOCK-OPTIMALL.md   Mesma luz e lente do Podi, roxo e cenas B2B

design-system/newsletter/                DESIGN SYSTEM do material "newsletter"
├── README.md                            O que é reutilizável e o que é só de e-mail
├── tokens.md                            Cor, tipografia, espaçamento, dark mode, imagens
├── components/                          23 blocos de HTML de e-mail + o botão VML
│   └── README.md                        Catálogo + regras do header do Podi News
└── guidelines/
    ├── email-compat.md                  Regras técnicas de HTML de e-mail
    ├── layout-ritmo.md                  Hierarquia, ritmo, limites de CTA e de seções
    ├── variaveis-envio.md               Variáveis por sistema de envio; as 3 do servidor do Podi
    ├── marcas.md                        Peça do Optimall: blocos, recolorir, conferir
    ├── marca-empreendimento.md          Modo empreendimento: paleta derivada, estrutura, sempre claro
    ├── qa-checklist.md                  Checklist obrigatório antes de entregar
    └── refs/                            Referências visuais (leitura humana, não são ativos)

design-system/apresentacao/              DESIGN SYSTEM do material "apresentação"
├── README.md                            O que é reutilizável e o que é só de slide
├── tokens.md                            Cor, cor secundária, tipografia de projeção, imagens
├── slides/                              Os 16 tipos de slide + o shell `_slide.html`
│   └── README.md                        Catálogo + como escolher o tipo
└── guidelines/
    ├── canvas-16-9.md                   Canvas fixo 1920×1080, preview e export em PDF
    ├── uso-do-roxo.md                   Os 5 usos permitidos do #9934FF
    ├── layout-ritmo.md                  Hierarquia no slide, ritmo do deck, limites
    └── qa-checklist.md                  Checklist obrigatório antes de entregar
design-system/apresentacao/optimall/     Biblioteca própria do deck do Optimall (modelos do Figma)
├── README.md                            Catálogo + como escolher o tipo
├── tokens.md                            Cor, degradês, vidro, Halyard, grafismos
└── slides/                              Os 14 tipos de slide do Optimall

design-system/post/                      DESIGN SYSTEM do material "post" (feed 4:5, 1080×1350)
├── README.md                            Uma biblioteca por marca, regras comuns
├── guidelines/                          canvas, carrossel, legenda, qa-checklist
└── optimall/                            tokens.md + posts/ — os 7 modelos do Optimall

templates/newsletter/
├── base.html                            Shell canônico. NUNCA editar por campanha
└── base-empreendimento.html             Shell do modo empreendimento: sempre claro, sem dark mode

templates/apresentacao/
├── base.html                            Shell do deck do Podi: tokens, canvas, escala e PDF
└── base-optimall.html                   Shell do deck do Optimall: tokens, logos, Halyard

templates/post/
└── base-optimall.html                   Shell do post do Optimall: canvas 1080×1350 e prévia

scripts/exportar.py                      PNG de post e PDF de deck pelo Chrome; confere a fonte antes

.claude/
├── skills/newsletter-podi/SKILL.md      Skill oficial — monta o e-mail
├── skills/apresentacao-podi/SKILL.md    Skill oficial — monta o deck 16:9
├── skills/post-podi/SKILL.md            Skill oficial — monta post/carrossel, PNG e legenda
├── skills/foto-podi/SKILL.md            Skill oficial — escreve o prompt de foto de marca
├── skills/*-optimall/SKILL.md           Atalhos: mesmo procedimento das -podi, marca Optimall
└── launch.json                          Config do servidor de preview local

skills/README.md                         Índice das skills (elas moram em .claude/skills/)

examples/newsletter/                     ACERVO CURADO — só o maintainer grava
├── 2026-08-podi-atualizacoes-app/       Frente cliente — envio real
├── 2026-08-interno-podi-por-dentro/     Frente interno — demonstrativo (placeholders)
├── 2026-08-podi-news-eventos-julho/     Podi News — envio real
└── 2026-09-empreendimento-save-win/     Modo empreendimento — recorte curado de campanha real

projects/
├── README.md                            Como preparar um envio
└── _inbox/<slug>/                       ENTRADA: briefing + imagens. Fora do Git

saida/<slug>/index.html                  SAÍDA: o material montado. Fora do Git
saida/<slug>/assets/                     Imagens do deck — o material precisa abrir sozinho

docs/
├── como-enviar-conteudo.md              Guia de quem escreve: documento e nome das imagens
├── governanca.md                        Quem altera o quê, como propor mudança
└── estrutura.md                         Este arquivo

scripts/check-atualizacao.sh             Verifica/atualiza a cópia local do padrão
scripts/paleta-empreendimento.py         Paleta derivada da cor base, contrastes, ícones e conferência
scripts/aplicar-marca.py                 Marca da peça: validar, derivar (maintainer), aplicar e conferir
scripts/_cor.py                          Conta de cor (OKLab, contraste) e PNG, comum aos dois scripts

CLAUDE.md                                Contexto global para agentes de IA
README.md                                Porta de entrada, linguagem não técnica
CHANGELOG.md                             Mudanças no padrão, com o porquê
```

## Por que assim

**Fotografia dentro de `brand/`.** Direção fotográfica é identidade, como a cor e o logo —
vale para e-mail, post e impresso. Não virou `design-system/photography/` porque a camada de
"como se constrói" seria uma skill de produção de imagem, que ainda não existe.

**Uma marca por pasta, um sistema só.** Podi e Optimall são irmãos: mesma estrutura, mesmos
procedimentos, mesmas regras de qualidade. No **e-mail**, duplicar blocos por marca faria as
duas divergirem na primeira correção: os blocos são escritos **uma vez**, com os valores do
Podi (a marca de referência), e o e-mail de outra marca é recolorido no fim por
`scripts/aplicar-marca.py`, papel por papel, a partir de `brand/<marca>/marca.json`.

**Deck e post do Optimall têm biblioteca própria.** A linguagem visual do Optimall — degradê
roxo, vidro, pattern de pontos, Halyard, logo tricolor — não sai de recolorir os slides do
Podi. Os modelos vêm do Figma aprovado pelo Optimall, escritos já nos tokens dele, e passam só
pelo `conferir`. O procedimento continua um só: as skills mudam a pasta de onde os modelos
saem, não os passos.

**`scripts/exportar.py`.** PNG de post e PDF de deck saem do Chrome da máquina, sem instalar
nada. O script confere a fonte antes: a Halyard é licenciada e vive no computador, não na web.

**`brand/` separado de `design-system/`.** A cor de marca e a regra de contraste valem para
qualquer material — e-mail, post, impresso. As regras de tabela e VML valem só para e-mail.
Misturar as duas faria todo material novo herdar limitação de Outlook.

**`design-system/<material>/`.** O segundo material chegou: `apresentacao/` nasceu ao lado
de `newsletter/`, sem herdar nada de e-mail. O que é comum aos dois — paleta, regras de
contraste, papéis tipográficos — continua em `brand/` ou repetido em cada `tokens.md` com o
valor certo para aquele suporte. `page` é o exemplo: `#EDF7F1` no e-mail, `#48DB84` no
slide, mesmo nome porque é o mesmo papel.

**Apresentação pode usar CSS moderno.** Flex, grid e `var()` são proibidos na newsletter por
causa do Outlook e obrigatórios na apresentação, que abre num navegador. Foi exatamente para
isso que as duas camadas ficaram separadas.

**Componentes fora de `templates/`.** O template é só o shell. Os 23 blocos são
componentes do design system: se copiam para dentro do template, não são templates.

**`projects/` e `saida/` fora do Git.** O trabalho de cada pessoa é local. Ninguém
sobrescreve ninguém, e material bruto não infla o histórico do repositório.

**Skills com sufixo de marca.** A ferramenta de IA traz dezenas de comandos próprios. Sem o
sufixo, na hora de digitar não dá para saber qual comando é o padrão da marca. As `-optimall`
são atalhos que seguem a `-podi` do mesmo material: um procedimento, dois nomes.

**Skills em `.claude/skills/`.** É a pasta que o Claude Code descobre sozinho. Uma segunda
cópia em `skills/` criaria duas versões divergindo — por isso `skills/` é só o índice.
