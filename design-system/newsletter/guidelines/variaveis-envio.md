# Variáveis de envio — o que o servidor aceita

**A regra de variáveis é do sistema que dispara.** O valor oficial também está em `envio` de
`brand/marca.json`, e é dali que `scripts/conferir.py` tira a lista que acusa.

Os e-mails do Podi saem por um servidor próprio na **AWS**. Ele resolve apenas três
variáveis. Qualquer outra **derruba o envio inteiro** — não é um e-mail com um campo
vazio, é a campanha que não sai.

## As três permitidas

| Variável | Suportada |
|---|---|
| `{{email}}` | ✅ |
| `{{topicId}}` | ✅ |
| `{{campaignId}}` | ✅ |
| qualquer outra | ❌ derruba o envio inteiro |

Escrever exatamente assim, em minúsculas e camelCase. `{{Email}}`, `{{EMAIL}}` ou
`{{ email }}` não são a mesma coisa e caem na linha de baixo da tabela.

## Campos do briefing em disparo por outro sistema

A regra das três variáveis vale para **envio pelo servidor do Podi**. Há peças que não saem
por ele: e-mails de gatilho de campanha (primeira nota validada, meta atingida…) disparados
pelo sistema da própria campanha, que preenche campos como `{{nome}}` ou
`{{economia_total}}`. A primeira foi o SAVE & WIN do City Center Outlet Premium.

| O briefing diz | O que fazer |
|---|---|
| O disparo é pelo **servidor do Podi**, ou não diz nada | Só as três variáveis. Campo do briefing vira texto fixo ou sai da peça |
| O disparo é por **outro sistema** | Os campos do briefing podem ficar, **escritos exatamente como o briefing define** — mesmo nome, mesma caixa, mesmas chaves |
| Traz campos personalizados, mas não diz por onde sai | **Perguntar antes de montar** |

Quando os campos ficam, a entrega avisa, com todas as letras: **esta peça não pode sair
pelo servidor do Podi** — lá, qualquer um desses campos derruba o envio inteiro.

O resto continua valendo: nada de link de descadastro, e `{{email}}` no rodapé legal
continua sendo o `{{email}}` — se o outro sistema usar outro nome para o e-mail do
destinatário, o briefing precisa dizer.

## Sem link de descadastro

O servidor não gera URL de descadastro, e não existe variável para ela. Então:

- **Nenhuma peça leva link de descadastro** — nem cliente final, nem interno.
- Nunca inventar `{{URL_DESCADASTRO}}`, `{{unsubscribe}}` ou equivalente: cai na
  regra acima e o envio não sai.
- O rodapé continua obrigatório com `© <ano> - Podi App`, o **motivo do recebimento**,
  Política de Privacidade e Termos de Uso. É o que informa o destinatário.
- A saída do descadastro é tratada **fora do HTML**, por quem opera o envio.

## Placeholder de montagem ≠ variável de envio

Os componentes e o template usam `{{MAIUSCULAS_COM_UNDERSCORE}}` — `{{ANO}}`,
`{{PREHEADER}}`, `{{TITULO_INTERNO}}`, `{{MOTIVO_RECEBIMENTO}}`. Esses são
**placeholders de montagem**: existem para serem substituídos por texto no arquivo,
antes do envio.

A regra fica legível na hora do QA:

- `{{MAIUSCULA}}` sobrou no HTML final → **erro de montagem**, falta preencher.
- `{{qualquerOutra}}` minúscula fora das três da tabela → **erro de envio**, derruba tudo.

Antes de entregar, conferir que só sobraram as três permitidas:

```bash
python3 -I scripts/conferir.py saida/<slug>/index.html
```

Ele lê a peça sem os comentários — onde os blocos citam placeholders de exemplo — e acusa
qualquer `{{...}}` que não seja `{{email}}`, `{{topicId}}` ou `{{campaignId}}`. Em disparo
por outro sistema, os campos do briefing entram com `--campos`, e nenhum outro passa:

```bash
python3 -I scripts/conferir.py --campos nome,economia_total saida/<slug>/index.html
```

Campo que não está no briefing é erro de montagem do mesmo jeito.
