# QA — rodar antes de entregar qualquer post

## Canvas

- [ ] Todo post tem 1080 × 1350 e nada foi cortado por `overflow:hidden`
- [ ] Texto e logo dentro da margem de segurança de 64px
- [ ] Nenhum texto abaixo de 24px; título e frase principal a partir de 56px
- [ ] Carrossel entre 3 e 10 cards, com capa e fecho

## Cor e tipografia

- [ ] Nenhuma cor escrita direto no post — tudo por `var(--token)` do `tokens.md` da marca
- [ ] Texto sobre a cor de marca é o `ink-on-brand` da marca (Optimall: branco)
- [ ] Só a fonte da marca, nos pesos do `tokens.md`
- [ ] `python3 scripts/aplicar-marca.py conferir <marca> saida/<slug>/index.html` → saída 0

## Imagens

- [ ] Todas em `assets/` da própria pasta, com caminho relativo e `alt`
- [ ] Nenhuma distorcida ou cortada para caber; foto nova segue o Style Lock da marca
- [ ] Logo pela versão certa do fundo (`<use href="#logo-…">`), nunca PNG nem `filter`

## Conteúdo

- [ ] Nenhum `{{PLACEHOLDER}}` sobrou
- [ ] Uma mensagem por card; o título cabe em até 3 linhas
- [ ] Todo número está na documentação da marca, com a legenda certa
- [ ] Nada de outra marca (texto, logo, @, link)
- [ ] `legenda.txt` com Instagram, LinkedIn e ALT de cada card

## Export

- [ ] `python3 scripts/exportar.py png saida/<slug>/index.html` → saída 0
- [ ] Um PNG por card, na ordem, e **abrir cada um** para conferir de olho
