---
name: newsletter-optimall
description: Monta uma newsletter, informativo ou e-mail marketing do Optimall (B2B, para gestores de shopping) a partir de um briefing em projects/_inbox/<slug>/. Use quando pedirem para gerar, montar ou criar um e-mail, uma newsletter ou um informativo do Optimall.
---

# Montar uma newsletter do Optimall

Este comando é um **atalho**: o procedimento é o mesmo do e-mail do Podi, com a marca fixada
em **Optimall**. Nada é copiado para cá, para as duas marcas nunca saírem de padrões diferentes.

**Abra e siga `.claude/skills/newsletter-podi/SKILL.md` do início ao fim, com
`<marca> = optimall`.** No §1a a marca já está decidida: não pergunte qual é.

O que muda em relação à peça do Podi está em `design-system/newsletter/guidelines/marcas.md`,
e a skill aponta cada ponto:

- validar a marca antes de montar (`python3 scripts/aplicar-marca.py validar optimall`) — se
  ela estiver pendente, parar e pedir para avisar quem cuida do repositório;
- header `01b` e rodapé social `90b` variante B, com logo e redes do Optimall;
- nada do Podi nem da Tacla Labs na peça;
- recolorir no fim com `aplicar-marca.py aplicar optimall` e conferir com `conferir optimall`;
- enquanto a regra de envio do Optimall estiver pendente, nenhuma variável `{{...}}` e aviso
  na entrega.

O Optimall é **masculino**: "o Optimall", "do Optimall". Nunca "a Optimall".
