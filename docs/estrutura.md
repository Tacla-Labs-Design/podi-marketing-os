# Estrutura do repositório

Mapa comentado. Visão para quem usa está no [README](../README.md).

```
brand/                                   IDENTIDADE — camada mais alta
├── README.md                            Marca, cor, roxo de detalhe, contraste, as duas frentes, empreendimento
├── links-oficiais.md                    Link do app, rodapé legal, redes, textos fixos do deck
├── marca.json                           Os mesmos valores, para máquina (paleta por papel, links, envio)
├── photography/
│   ├── README.md                        O que é normativo no Style Lock, e o verde
│   ├── STYLE-LOCK-PODI.md               Direção fotográfica oficial — blocos copiados byte a byte
│   └── refs/                            As referências que originaram o Style Lock
└── assets/
    ├── header/                          Logos Podi e Tacla Labs; logo-podi.svg é o vetor monocromático
    ├── icones/                          Ícones sociais — 4 redes × 3 variantes
    ├── end-news-img.jpg                 Imagem fixa do fecho "Podi e você"
    └── hero-podi-news.png               Arte do hero do Podi News

design-system/newsletter/                DESIGN SYSTEM do material "newsletter"
├── README.md                            O que é reutilizável e o que é só de e-mail
├── tokens.md                            Cor, tipografia, espaçamento, dark mode, imagens
├── components/                          23 blocos de HTML de e-mail + o botão VML
│   └── README.md                        Catálogo + regras do header do Podi News
└── guidelines/
    ├── email-compat.md                  Regras técnicas de HTML de e-mail
    ├── layout-ritmo.md                  Hierarquia, ritmo, limites de CTA e de seções
    ├── variaveis-envio.md               As 3 variáveis do servidor do Podi; disparo por outro sistema
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

design-system/post/                      DESIGN SYSTEM do material "post" (feed 4:5, 1080×1350)
├── README.md                            Regras do material; modelos do Podi pendentes
└── guidelines/                          canvas, carrossel, legenda, qa-checklist

templates/newsletter/
├── base.html                            Shell canônico. NUNCA editar por campanha
└── base-empreendimento.html             Shell do modo empreendimento: sempre claro, sem dark mode

templates/apresentacao/
└── base.html                            Shell do deck: tokens, canvas, escala e PDF

.claude/
├── skills/newsletter-podi/SKILL.md      Skill oficial — monta o e-mail
├── skills/apresentacao-podi/SKILL.md    Skill oficial — monta o deck 16:9
├── skills/post-podi/SKILL.md            Skill oficial — post/carrossel; para enquanto não há modelos
├── skills/foto-podi/SKILL.md            Skill oficial — escreve o prompt de foto de marca
└── launch.json                          Config do servidor de preview local

skills/README.md                         Índice das skills (elas moram em .claude/skills/)

examples/                                ACERVO CURADO — só o maintainer grava
├── briefing-demo/                       Briefing de exemplo, com imagens de teste
└── newsletter/
    ├── 2026-08-podi-atualizacoes-app/       Frente cliente — envio real
    ├── 2026-08-interno-podi-por-dentro/     Frente interno — demonstrativo (placeholders)
    ├── 2026-08-podi-news-eventos-julho/     Podi News — envio real
    └── 2026-09-empreendimento-save-win/     Modo empreendimento — recorte curado de campanha real

projects/
├── README.md                            Como preparar um envio
└── _inbox/<slug>/                       ENTRADA: briefing + imagens. Fora do Git (todo projects/, menos o README)

saida/<slug>/index.html                  SAÍDA: o material montado. Fora do Git
saida/<slug>/assets/                     Imagens do deck — o material precisa abrir sozinho

docs/
├── como-usar.md                         Do zero: abrir, pedir, conferir
├── como-enviar-conteudo.md              Guia de quem escreve: documento e nome das imagens
├── governanca.md                        Quem altera o quê, como propor mudança
└── estrutura.md                         Este arquivo

scripts/check-atualizacao.sh             Verifica/atualiza a cópia local do padrão
scripts/publicar                         Publica a marca no hub de marcas (só maintainer)

hub/BRAND.md, hub/guias/, hub/modelos/   A marca no hub: regras curtas, um guia por peça, modelos com data-slot
scripts/conferir.py                      Confere a peça montada: paleta, verde como texto, variáveis, alt, e-mail
scripts/exportar.py                      PDF do deck (e PNG de post) pelo Chrome; confere a fonte antes
scripts/paleta-empreendimento.py         Paleta derivada da cor base, contrastes, ícones e conferência
scripts/_cor.py                          Conta de cor (OKLab, contraste) e PNG, usada pela paleta

CLAUDE.md                                Contexto global para agentes de IA
README.md                                Porta de entrada, linguagem não técnica
CHANGELOG.md                             Mudanças no padrão, com o porquê
```

## Por que assim

**Fotografia dentro de `brand/`.** Direção fotográfica é identidade, como a cor e o logo —
vale para e-mail, post e impresso. Não virou `design-system/photography/` porque a camada de
"como se constrói" seria uma skill de produção de imagem, que ainda não existe.

**`brand/` separado de `design-system/`.** A cor de marca e a regra de contraste valem para
qualquer material — e-mail, post, impresso. As regras de tabela e VML valem só para e-mail.
Misturar as duas faria todo material novo herdar limitação de Outlook.

**`design-system/<material>/`.** `apresentacao/` nasceu ao lado de `newsletter/`, sem herdar
nada de e-mail. O que é comum aos dois — paleta, regras de contraste, papéis tipográficos —
continua em `brand/` ou repetido em cada `tokens.md` com o valor certo para aquele suporte.
`page` é o exemplo: `#EDF7F1` no e-mail, `#48DB84` no slide, mesmo nome porque é o mesmo papel.

**`design-system/post/` sem modelos.** O canvas, o carrossel, a legenda e o QA de post não
dependem do layout e já estão escritos. Os modelos do Podi ainda não foram aprovados: até
chegarem, o `/post-podi` para e avisa, em vez de improvisar um layout.

**`scripts/conferir.py`.** Lê a peça sem os comentários do HTML e confere o que um `grep`
solto erraria: cor fora da paleta, o verde como cor de texto, variável fora das três do
servidor, imagem sem `alt`, peso e CSS proibido no e-mail, e botão sem a metade de fora do
Outlook. O modo empreendimento tem paleta derivada e se confere pelo próprio
`paleta-empreendimento.py --conferir`.

**`scripts/exportar.py`.** O PDF do deck sai do Chrome da máquina, sem instalar nada. O
script confere antes se a fonte carregou, para a peça não sair com outra letra em silêncio.

**Apresentação pode usar CSS moderno.** Flex, grid e `var()` são proibidos na newsletter por
causa do Outlook e obrigatórios na apresentação, que abre num navegador. Foi exatamente para
isso que as duas camadas ficaram separadas.

**Componentes fora de `templates/`.** O template é só o shell. Os 23 blocos são
componentes do design system: se copiam para dentro do template, não são templates.

**`projects/` e `saida/` fora do Git.** O trabalho de cada pessoa é local. Ninguém
sobrescreve ninguém, e material bruto — briefing e imagem de cliente — não vai para o
histórico do repositório.

**Skills com sufixo `-podi`.** A ferramenta de IA traz dezenas de comandos próprios. Sem o
sufixo, na hora de digitar não dá para saber qual comando é o padrão da marca.

**Skills em `.claude/skills/`.** É a pasta que o Claude Code descobre sozinho. Uma segunda
cópia em `skills/` criaria duas versões divergindo — por isso `skills/` é só o índice.

**`hub/` e `scripts/publicar`.** O time também usa a marca fora deste repositório, pelo hub de
marcas (`https://marcas.taclalabs.workers.dev/podi/manifest.json`), que qualquer ferramenta lê sem
clonar nada. O hub tem uma versão curta do padrão: `BRAND.md`, um guia por peça e modelos HTML com
`data-slot`, que puxam logos e imagens pelo endereço do hub. A fonte dessa versão é a pasta
`hub/`; o `scripts/publicar` monta a pasta da marca, confere que todo endereço citado existe e
envia ao bucket, com o manifesto por último. Mudou uma regra aqui que o hub repete? Mude também em
`hub/` e publique de novo.

