# SAVE & WIN — e-mail com marca do empreendimento

Exemplo curado do **modo empreendimento**
([`marca-empreendimento.md`](../../../design-system/newsletter/guidelines/marca-empreendimento.md)).
Origem: a campanha SAVE & WIN do City Center Outlet Premium, setembro de 2026, sete e-mails
de gatilho. Daqui ficam dois, que juntos usam todos os blocos do modo.

| Arquivo | O que mostra |
|---|---|
| [`01-boas-vindas.html`](01-boas-vindas.html) | O card único completo: texto, título de grupo, galeria 1:1 sem etiqueta, nota, lista, extrato de uma linha e CTA |
| [`07-balanco-final.html`](07-balanco-final.html) | O extrato longo (quatro linhas) e texto de fechamento depois dele |
| [`brief.md`](brief.md) | O briefing, com o cabeçalho que o modo precisa (remetente, disparo, cor base, redes) |

Montados do zero com o `base-empreendimento.html` e os componentes oficiais
(`01b`, `03`, `08` B, `13`, `13a`, `13b`, `90b` B, `91`), paleta de
`scripts/paleta-empreendimento.py "#173B2A"`. Não são as peças enviadas: aquelas foram
montadas à mão, antes de existir o padrão.

## Paleta

| Token | Hex |
|---|---|
| brand / accent-ink | `#173B2A` |
| page / canvas | `#F0F6F2` |
| accent-soft | `#DCEDE3` |
| hairline | `#D8E5DD` |
| texto do CTA | `#FFFFFF` (12,4:1 sobre a base) |

`python3 scripts/paleta-empreendimento.py "#173B2A" --conferir examples/newsletter/2026-09-empreendimento-save-win/*.html`
passa nos dois.

## Envio

**Estas peças não podem sair pelo servidor do Podi.** Os campos `{{nome}}`,
`{{economia_total}}` e os outros do briefing são preenchidos pelo sistema da campanha, que
dispara por gatilho. Pelo servidor do Podi, qualquer um deles derruba o envio inteiro
([`variaveis-envio.md`](../../../design-system/newsletter/guidelines/variaveis-envio.md)).

## Decisões registradas

- **Assuntos acima de 45 caracteres.** O do e-mail 1 tem 56 e o do 7 tem 54, e o do 7 ainda
  cresce com o valor. Os assuntos são do cliente e ficaram como o briefing definiu. Numa
  peça nova, a entrega aponta o limite, mas o texto do cliente não se reescreve por conta própria.
- **Preheaders refeitos para 60–90 caracteres.** Os originais tinham 58 e 48. Os novos
  dizem o mesmo, com o nome do outlet (e-mail 1) e o período da campanha (e-mail 7).
- **Sem pedido de descadastro no rodapé.** O briefing pedia "clique em cancelar
  recebimento ou escreva para marketing@citycenteroutlet.com.br". Pela regra atual, nenhuma
  peça leva descadastro, então a frase saiu. Se o maintainer decidir permitir opt-out por
  e-mail do empreendimento (sem variável), ela volta.
- **Ordem do rodapé.** Texto legal da promoção e endereço antes do `©`, e depois o
  `91-footer-legal` sem mudança: `©`, motivo, Privacidade e Termos. Na peça enviada, o `©`
  vinha depois do motivo.

## Pendência

**`assets/hero-mail.jpg` tem 600 × 300.** O mínimo do padrão é 1072 de largura (2x), e a
arte só existe nesse tamanho. Ampliar só borraria, então o arquivo ficou como veio. Quando o
City Center enviar a arte em 1072 × 536 ou maior, basta trocar o arquivo: o HTML não muda.

## Imagens

| Arquivo | Exibição | Arquivo |
|---|---|---|
| `assets/logo-city-center-color.png` | 150 × 24 (cabeçalho e rodapé) | 300 × 48 |
| `assets/hero-mail.jpg` | 536 × 268 | 600 × 300 — abaixo do mínimo |
| `assets/guarda-chuva.jpg`, `assets/vale-compras.jpg` | 224 × 224 | 512 × 512 |
| `assets/icones/<rede>-campanha.png` | 24 × 24 | 24 × 24, gerados pelo script |

Os ícones herdam o tamanho dos `-green.png` oficiais, que também são 24 × 24.
