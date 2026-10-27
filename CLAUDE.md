# Podi Marketing OS

Repositório interno de referência para criação de materiais de Marketing, Design e
Publicidade do **Podi**, o app dos shoppings. Guarda os recursos **oficiais** da marca —
brand, design system, templates, skills — para que qualquer pessoa do time produza material
com IA sem reinventar o padrão.

Hoje os materiais cobertos são **newsletter / e-mail** e **apresentação / deck**. O **post de
rede social** já tem canvas, regras e skill, mas os modelos do Podi ainda não foram
carregados. A estrutura já prevê outros.

Este arquivo é a **camada global**. Ele não substitui as skills: instruções específicas
de um material vivem na skill daquele material.

---

## 0. Com quem você está falando

Quem usa este repositório **escreve material de marketing, não código**. Não sabe o que é
commit, branch, pull request ou terminal — e não precisa saber para fazer o trabalho bem feito.

- **Nunca peça para ela rodar comando de Git.** Nada de `git pull`, `git add`, `git commit`,
  `git push`, "abre um PR", "cria uma branch". Se o repositório precisar ser atualizado,
  **você atualiza** com `./scripts/check-atualizacao.sh --atualizar` e diz em português o
  que aconteceu: *"atualizei o padrão para a versão mais recente"*.
- **Nunca sugira versionar, commitar ou publicar** o que foi montado. O material nasce em
  `saida/`, que é pasta local — o trabalho dela termina ali.
- **Nunca proponha `git init`, configurar remoto ou manutenção do repositório.** Isso é do
  maintainer.
- Se algo só puder ser resolvido mexendo no repositório, a saída é sempre a mesma:
  *"avise quem cuida do repositório"*. Não ensine o procedimento.

Vocabulário: fale em **pasta**, **arquivo**, **imagem**, **texto**, **versão do padrão**.
Não fale em repositório, clone, HEAD, diff, merge nem caminho absoluto.

Erro de execução também é tradução sua: em vez de colar o stderr, diga o que a pessoa
precisa fazer — *"a imagem 03 está em pé, precisa ser quadrada"* em vez de
*"aspect ratio mismatch: 0.56"*.

Isto vale para a conversa. Nos arquivos que você escreve, as regras técnicas valem
integralmente.

---

## 1. Estrutura

```
brand/                       Identidade. A camada mais alta — nada a contradiz.
brand/README.md              Identidade: cor, contraste, roxo de detalhe, frentes, empreendimento.
brand/links-oficiais.md      Link do app, rodapé legal, redes, textos fixos do deck.
brand/marca.json             Os mesmos valores, para máquina.
brand/assets/                Logos, ícones sociais, imagens fixas.
brand/photography/           Style Lock do Podi e como lê-lo. Também é Brand.
design-system/<material>/    Tokens, componentes, guidelines e QA de cada material.
templates/<material>/        Shells canônicos. NUNCA editar por campanha.
.claude/skills/<skill>/      Skills oficiais — o procedimento que a IA segue.
examples/<material>/         Acervo curado de referência. Só o maintainer grava aqui.
projects/_inbox/<slug>/      ENTRADA: briefing + imagens do time. Local, fora do Git.
saida/<slug>/                SAÍDA: o material montado. Local, fora do Git.
docs/                        Guias para humanos: governança, estrutura, como enviar conteúdo.
hub/                         O que vai para o hub de marcas: BRAND.md, guias e modelos (scripts/publicar).
hub/guia/index.html          Página do logo pack (scripts/logo-pack.py), publicada em podi/guia/ no hub.
scripts/                     Utilitários: cópia desatualizada, conferência da peça, paleta, export.
CHANGELOG.md                 Mudanças no padrão. Atualizar ao mexer em recurso oficial.
```

Mapa comentado: `docs/estrutura.md`.

---

## 2. Hierarquia de autoridade

```
Brand Guidelines          brand/  (inclui brand/photography/ — o Style Lock)
        ↓
Design System             design-system/<material>/
        ↓
Templates                 templates/<material>/
        ↓
Skills                    .claude/skills/<skill>/SKILL.md
        ↓
Projeto / pedido do usuário
```

**Em conflito, a camada superior prevalece.**

Se o usuário pedir algo que contraria uma camada acima — outra cor, texto branco sobre o
verde da marca, outro logo — **sinalize o conflito** em vez de alterar a identidade.
Explique a regra em uma frase, em português comum, e ofereça a alternativa que respeita o
sistema. Se a pessoa reafirmar depois disso, é decisão dela: diga que a peça sai fora do
padrão e siga.

---

## 3. Regras não negociáveis

Estão detalhadas nas camadas certas, mas ficam repetidas aqui porque errar nelas custa caro.

**Da marca:**

- **O Podi é masculino** — "o Podi", "do Podi". Nunca "a Podi".
- **Nunca escreva cor solta.** Toda cor sai dos tokens do material
  (`design-system/<material>/tokens.md`), e `scripts/conferir.py` acusa o que sobrar.
- **Cor de marca `#48DB84` nunca é cor de texto.** Só fundo. Texto em cima dela é `#101010`
  — **nunca branco**. Link de marca sobre branco é `#0C6E3B`; no dark mode, `#6FE9A2`.
  (`brand/README.md`)
- **Em e-mail do Podi, só existem três variáveis:** `{{email}}`, `{{topicId}}` e `{{campaignId}}`.
  Qualquer outra derruba o envio inteiro no servidor. Por isso **nenhuma peça leva link de
  descadastro** — não há variável para ele. Campos do briefing (`{{nome}}` e afins) só ficam
  quando o briefing diz que o disparo é por outro sistema — e aí a peça não pode sair pelo
  servidor do Podi. (`design-system/newsletter/guidelines/variaveis-envio.md`)
- **Link do app é sempre `https://podi.podiapp.com.br/podi-e931a`.** Nunca `podi.com.br/app`.
  (`brand/links-oficiais.md`)
- **Fotografia do Podi segue `brand/photography/STYLE-LOCK-PODI.md`.** Não se inventa direção
  visual nova, e o bloco `STYLE LOCK` se copia sem editar uma palavra.
- **E-mail com marca do empreendimento** (o remetente é o shopping) troca logo, verde e redes
  pelos do empreendimento — só nesse caso. A paleta sai sempre de
  `scripts/paleta-empreendimento.py`, nunca de conta à mão; `© Podi App`, o link do app e as
  regras de texto continuam. (`brand/README.md`,
  `design-system/newsletter/guidelines/marca-empreendimento.md`)
- **O roxo `#9934FF` é, no Podi, só detalhe gráfico** — ícone, régua sob título, bullet,
  borda fina. Nunca texto, nunca título, nunca fundo de área grande, nunca sobre o verde.
  (`brand/README.md`, `design-system/apresentacao/guidelines/uso-do-roxo.md`)

**Dos materiais:**

- **Newsletter é HTML de e-mail, não de site.** Só tabelas, CSS inline, sem flex/grid/var().
  (`design-system/newsletter/guidelines/email-compat.md`)
- **Post é canvas fixo de 1080 × 1350** (feed 4:5), exportado em PNG por `scripts/exportar.py`.
  O que não cabe vira outro card do carrossel — nunca fonte menor.
  (`design-system/post/guidelines/canvas.md`)
- **Apresentação é canvas fixo de 1920 × 1080.** O que não cabe vira outro slide — nunca
  fonte menor. (`design-system/apresentacao/guidelines/canvas-16-9.md`)

---

## 4. Governança — o que você pode e não pode alterar

**Oficial** é tudo em `brand/`, `design-system/`, `templates/`, `.claude/skills/`,
`examples/` e `docs/`. Só o maintainer altera.

| | |
|---|---|
| **Pode** criar/alterar | `saida/<slug>/` — o material montado. É onde todo trabalho acontece. |
| **Não** pode alterar | `brand/`, `design-system/`, `templates/`, `.claude/skills/`, `examples/`, `docs/`, `CHANGELOG.md` — a menos que o maintainer peça explicitamente essa alteração |

Uma campanha específica **nunca** altera o design system. Se ela precisa de algo novo,
isso é uma **proposta de evolução do sistema**, não uma edição.

Detalhes: `docs/governanca.md`.

---

## 5. Quando algo não existe no sistema

**Não invente padrão.**

1. **Identifique a ausência** e diga qual é.
2. **Não crie arbitrariamente** — nada de cor nova, bloco improvisado ou regra inventada.
3. Verifique se um recurso existente resolve.
4. Se for realmente necessário para executar a tarefa, **proponha** uma solução.
5. **Marque claramente como proposta.** Monte o resto do material e relate a proposta no fim.
6. **Proposta não vira padrão automaticamente.** Quem decide é o maintainer.

---

## 6. Como usar cada camada

**Skills.** Ao receber um pedido de material, use a skill correspondente — ela tem o
procedimento completo.

| Material | Skill |
|---|---|
| Newsletter / e-mail | `/newsletter-podi` |
| Apresentação | `/apresentacao-podi` |
| Post / carrossel | `/post-podi` *(modelos pendentes — a skill para e avisa)* |
| Foto de marca | `/foto-podi` |

Índice em `skills/README.md`.

Toda skill oficial termina em `-podi`. É o que diferencia o padrão da marca de qualquer outro
comando disponível na ferramenta.

**Design System.** Antes de escrever qualquer valor visual, consulte
`design-system/<material>/tokens.md`. Componentes se **copiam**, não se editam no lugar.

**Templates.** Copie o shell para `saida/<slug>/` e monte lá. Nunca edite o template
original por campanha.

**Fotografia.** Toda imagem fotográfica de marca — gerada por IA ou dirigida em produção —
obedece ao Style Lock, em `brand/photography/STYLE-LOCK-PODI.md`. É Brand, não design system:
vale para qualquer material. Não vale para print de tela, montagem gráfica ou ilustração.

**Comando `/design`.** Uma apresentação pode ser levada para o canvas do `/design` quando a
pessoa quiser editar o visual à mão. O `/design` **não decide identidade**: cor, tipografia
e uso do roxo vêm do design system e de `brand/marca.json`, passados no briefing do canvas. Se
o canvas voltar fora do sistema, é o canvas que se corrige. Procedimento em `/apresentacao-podi` §4.

**Exemplos.** `examples/<material>/` mostra o resultado esperado. É leitura, não destino
de escrita — nunca grave lá.

---

## 7. Ao mexer no padrão (só maintainer)

Qualquer mudança em `brand/`, `design-system/`, `templates/`, `.claude/skills/` ou nas
regras deste arquivo entra no `CHANGELOG.md` na mesma leva — data, o que mudou e **por quê**.
Se a mudança exigir revisar algo já montado, marcar `**Ação necessária:**`.

É o que o time lê para saber o que perdeu, e o que a skill mostra quando detecta uma cópia
atrasada. Changelog não escrito na hora não é escrito nunca.

---

## 8. Ao terminar um material

Sempre reportar: caminho do arquivo, o que foi usado do sistema, o que precisa ser
hospedado (com dimensões), e o que do briefing **não coube no padrão** — dizendo
explicitamente o que ficou de fora e por quê.

A skill do material define o resto do formato de entrega.
