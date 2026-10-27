---
name: post-optimall
description: Monta um post ou carrossel de Instagram e LinkedIn do Optimall (B2B, para gestores de shopping) em 1080×1350 a partir de um briefing em projects/_inbox/<slug>/, exporta em PNG e escreve a legenda. Use quando pedirem para gerar, montar ou criar um post, um carrossel ou um card de rede social do Optimall.
---

# Montar um post ou carrossel do Optimall

Este comando é um **atalho**: o procedimento é o mesmo do post do Podi, com a marca fixada em
**Optimall**. Nada é copiado para cá, para as duas marcas nunca saírem de padrões diferentes.

**Abra e siga `.claude/skills/post-podi/SKILL.md` do início ao fim, com
`<marca> = optimall`.** No §0b a marca já está decidida: não pergunte qual é.

Os pontos em que a marca muda o trabalho, todos indicados na skill:

- validar a marca antes de montar (`python3 scripts/aplicar-marca.py validar optimall`);
- modelos em `design-system/post/optimall/` (catálogo no `README.md` de lá), shell
  `templates/post/base-optimall.html`;
- **sempre B2B**: fala com quem decide no shopping, nunca com o consumidor final; texto,
  números e frases de `brand/optimall/mensagens.md`; CTA *Fale com um consultor*;
- roxo `#9934FF` com texto **branco** em cima; logo tricolor na versão do fundo; Halyard Text
  ativada na máquina para exportar;
- nada do Podi nem da Tacla Labs — nem no texto, nem no `alt`, nem na legenda.

O Optimall é **masculino**: "o Optimall", "do Optimall". Nunca "a Optimall".
