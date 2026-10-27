# Podi · e-mail (newsletter, Podi News, e-mail marketing)

E-mail de 600 px para o consumidor dos shoppings (frente cliente) ou para o time (frente
interno). O modelo é uma edição do Podi News; as outras peças usam os mesmos blocos.

## Briefing

Obrigatório: a frente (cliente ou interno), a chamada da edição, os blocos de conteúdo
numerados (título, texto e, se houver, tag, subtítulo, link do botão) e as imagens, já
hospedadas, com o número do bloco no nome.

Padrão se faltar:
- Preheader: escrever a partir da chamada, 60 a 90 caracteres.
- Subject: até 45 caracteres, a partir da chamada.
- Motivo do recebimento: "tem cadastro no app Podi" (cliente); no interno, perguntar.
- Botão sem link no briefing: o bloco sai sem botão. O único botão com link fixo é o do app.

**O remetente é um shopping, não o Podi?** Não monte pelo hub: é o modo empreendimento, com
paleta própria calculada por script no repositório `podi-marketing-os`.

## Modelo

`podi/modelos/email.html`. Troque só os `data-slot`; o texto de exemplo está entre colchetes.

| Bloco | Quando usar | Limites |
|---|---|---|
| Hero do Podi News | abertura de toda edição | capa 16:9, mín. 1072 px de largura · edição até 24 caracteres · chamada até 60 · apoio até 120 |
| Notícia com imagem no topo | a notícia tem imagem horizontal | imagem 16:9, mín. 1072 × 604 · tag até 20 · título até 60 · subtítulo até 60 · texto até 3 frases |
| Notícia compacta | a imagem é quadrada | imagem 1:1, mín. 496 × 496 · título até 50 · texto até 3 frases |
| Fecho "Podi e você" | toda edição para o cliente | fixo: imagem, texto e botão do app |
| Redes e rodapé legal | sempre | fixos; só o ano e o motivo mudam |

- **No máximo 4 blocos de conteúdo.** Mais que isso: cortar ou fazer dois envios.
- Para mais notícias, copie o bloco inteiro com o espaçador que vem antes dele.
- E-mail não recorta imagem: o arquivo entra com a proporção que tem. Proporção errada, peça
  outra imagem; não estique nem corte.
- Só JPG ou PNG. WebP, AVIF, HEIC e SVG não abrem no Outlook nem no Gmail.
- Botão: o link vai nos **dois** lugares (o `v:roundrect` do Outlook e o `<a>`). Texto do
  botão em `#101010` sobre o verde, nunca branco.
- Download do app: sempre `https://podi.podiapp.com.br/podi-e931a`.
- **Variáveis:** só `{{email}}`, `{{topicId}}` e `{{campaignId}}`. Qualquer outra derruba o
  envio no servidor do Podi. **Sem link de descadastro.**
- **Nunca apague os condicionais do Outlook** (os comentários `if mso` e `if !mso`): sem eles o
  botão some.
- E-mail é tabela com CSS inline: nada de flex, grid, `var()`, `<script>` ou `<form>`.

## Gerar o arquivo final

O arquivo final é o próprio HTML, para colar no sistema de envio. Para conferir antes,
abra no navegador e tire uma prévia:

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --hide-scrollbars \
  --window-size=640,2400 --screenshot="previa.png" "file://$PWD/email.html"
```

No Windows, o Chrome fica em `C:\Program Files\Google\Chrome\Application\chrome.exe`.

## Conferência

- [ ] Nenhum texto entre colchetes sobrou; nenhum `data-slot` de imagem com `src` vazio.
- [ ] Só `{{email}}`, `{{topicId}}` e `{{campaignId}}` — nenhuma outra `{{...}}`.
- [ ] Nenhum link de descadastro.
- [ ] Nenhum texto em `#48DB84`; texto sobre o verde em `#101010`.
- [ ] Toda imagem com `alt`; todo link `http` com `target="_blank"`.
- [ ] Botão com o mesmo link no `v:roundrect` e no `<a>`.
- [ ] Link do app `podi.podiapp.com.br/podi-e931a`; nunca `podi.com.br/app`.
- [ ] HTML abaixo de 100 KB (o Gmail corta acima disso).
- [ ] Subject até 45 caracteres; preheader de 60 a 90; sempre "o Podi".
