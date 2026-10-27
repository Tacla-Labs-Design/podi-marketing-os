# QA — rodar antes de entregar qualquer post

## Canvas

- [ ] Todo post tem 1080 × 1350 e nada foi cortado por `overflow:hidden`
- [ ] Texto e logo dentro da margem de segurança de 64px
- [ ] Nenhum texto abaixo de 24px; título e frase principal a partir de 56px
- [ ] Carrossel entre 3 e 10 cards, com capa e fecho

## Cor e tipografia

- [ ] Nenhuma cor escrita direto no post — tudo por `var(--token)` de `../tokens.md`
- [ ] Texto sobre o verde é `#101010`, **nunca branco**; o verde nunca é cor de texto
- [ ] Só a fonte do Podi, nos pesos do `tokens.md`
- [ ] `python3 -I scripts/conferir.py saida/<slug>/index.html saida/<slug>/legenda.txt` → saída 0

## Imagens

- [ ] Todas em `assets/` da própria pasta, com caminho relativo e `alt`
- [ ] Nenhuma distorcida ou cortada para caber; foto nova segue o Style Lock do Podi
- [ ] Logo pela versão certa do fundo (`<use href="#logo-…">`), nunca PNG nem `filter`

## Conteúdo

- [ ] Nenhum `{{PLACEHOLDER}}` sobrou
- [ ] Uma mensagem por card; o título cabe em até 3 linhas
- [ ] Todo número tem fonte (briefing ou documentação oficial do Podi)
- [ ] Nada de outra marca (texto, logo, @, link); sempre "o Podi"
- [ ] `legenda.txt` com Instagram, LinkedIn e ALT de cada card

## Export

- [ ] `python3 -I scripts/exportar.py png saida/<slug>/index.html` → saída 0
- [ ] Um PNG por card, na ordem, e **abrir cada um** para conferir de olho
