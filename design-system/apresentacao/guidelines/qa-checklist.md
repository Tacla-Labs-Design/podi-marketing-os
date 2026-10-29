# QA — rodar antes de entregar qualquer apresentação

## Canvas

- [ ] Todo slide tem 1920 × 1080 e nada foi cortado por `overflow:hidden`
- [ ] Nenhum texto fora da margem de segurança de 64px
- [ ] Nenhuma barra de rolagem horizontal no navegador
- [ ] O último slide é o `15-encerramento` (ou uma variação dele)

## Cor

- [ ] Nenhuma cor escrita direto no slide — tudo por `var(--token)`
- [ ] `#31D06E` não aparece como `color:` em lugar nenhum
- [ ] `#9934FF` não aparece como `color:` de texto em lugar nenhum
- [ ] Nenhum detalhe roxo solto sobre o verde
- [ ] Texto sobre o verde é `#101010` (a tagline, `#074A21`), nunca branco
- [ ] No máximo 3 tipos de detalhe roxo por slide (repetição numa grade conta uma vez)

## Tipografia

- [ ] Só DM Sans: 600 nos títulos, 400 no texto, 700 só em `<strong>` e número
- [ ] Nenhum texto de leitura abaixo de 24px
- [ ] O título de cada slide cabe em duas linhas

## Imagens

- [ ] Todas em `assets/` da própria pasta, com caminho relativo
- [ ] Todas com `alt` descrevendo o que a imagem mostra
- [ ] Exportadas em 2x da exibição (ver `../tokens.md`)
- [ ] Nenhuma distorcida ou cortada para caber
- [ ] Logo do Podi pelo `<use href="#logo-marca">`, nunca por PNG nem `filter`
- [ ] Logo branco sobre a cor de marca, o preto e foto; `logo--marca` sobre fundo claro
- [ ] Ícones do pack Bulk (`brand/assets/icones-bulk/`), soltos, com `currentColor`; ícone novo desenhado pela regra de `brand/README.md` → Ícones
- [ ] Ripple, mão e telas do app copiados de `brand/assets/deck/`, sem redesenho
- [ ] Rodapé assinado pelo logo, nunca pelo nome da marca escrito
- [ ] Logo de cliente na versão light mode

## Conteúdo

- [ ] Nenhum `{{PLACEHOLDER}}` sobrou
- [ ] Todo número tem label e fonte do dado
- [ ] O CTA do encerramento é o link do app, `https://podi.podiapp.com.br/podi-e931a` (`links.cta`)
- [ ] Uma ideia por slide, nenhum slide acima de ~60 palavras

## Export

- [ ] PDF gerado em paisagem, margens nenhuma, fundos ligados
- [ ] Um slide por página no PDF, nada cortado, nenhum fundo faltando
- [ ] O deck abre sozinho a partir da pasta, sem depender de nada externo

## Comandos

```bash
f=saida/<slug>/index.html
python3 -I scripts/conferir.py $f                   # saída 0 — placeholders, alt, assets/, paleta, verde como texto; "N slides"
grep -c 'color:var(--accent-2)' $f                  # só o .ico do template e as aspas do 10
grep -c 'podi.com.br/app' $f                        # 0 — endereço não existe
python3 -I scripts/exportar.py pdf $f               # saída 0 — uma página por slide
```

O `conferir` lê a peça sem os comentários e acusa o verde ou `var(--accent)` como cor de texto
(fora da regra `.logo--marca`), cor fora da paleta e "a Podi".
