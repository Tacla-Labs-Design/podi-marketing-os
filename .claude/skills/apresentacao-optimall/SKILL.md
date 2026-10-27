---
name: apresentacao-optimall
description: Monta uma apresentação, deck, pitch ou slide do Optimall (B2B, para gestores de shopping) em 16:9 a partir de um briefing em projects/_inbox/<slug>/. Use quando pedirem para gerar, montar ou criar uma apresentação, um deck, um pitch ou um PowerPoint do Optimall.
---

# Montar uma apresentação do Optimall

Este comando é um **atalho**: o procedimento é o mesmo do deck do Podi, com a marca fixada em
**Optimall**. Nada é copiado para cá, para as duas marcas nunca saírem de padrões diferentes.

**Abra e siga `.claude/skills/apresentacao-podi/SKILL.md` do início ao fim, com
`<marca> = optimall`.** No §0b a marca já está decidida: não pergunte qual é.

Os pontos em que a marca muda o trabalho, todos indicados na skill:

- validar a marca antes de montar (`python3 scripts/aplicar-marca.py validar optimall`) — se
  ela estiver pendente, parar e pedir para avisar quem cuida do repositório;
- **biblioteca própria**: slides de `design-system/apresentacao/optimall/slides/` (catálogo no
  `README.md` de lá), tokens de `optimall/tokens.md`, template `base-optimall.html`. Nunca um
  slide do Podi;
- **sempre B2B**: texto de `brand/optimall/mensagens.md`, números só os oficiais, CTA *Fale com
  um consultor*; os slides já trazem o texto aprovado do deck comercial;
- **não recolorir** — o deck já nasce roxo; só o `conferir optimall` no QA;
- logo tricolor pelos `<symbol>` do template (negativo sobre roxo, positivo sobre claro);
- PDF por `python3 scripts/exportar.py pdf`, com a Halyard Text ativada na máquina;
- nada do Podi nem da Tacla Labs no deck — nem no texto, nem no `alt`.

O Optimall é **masculino**: "o Optimall", "do Optimall". Nunca "a Optimall".
