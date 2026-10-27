# Links e ativos oficiais — Optimall

> Fonte: o site publicado [optimall.com.br](https://www.optimall.com.br). Não se inventa URL.
> Os mesmos valores ficam em `marca.json`, que é o que os scripts leem — os dois se
> atualizam juntos.

## CTA principal

O destino fixo do botão principal do e-mail, do fecho do deck e da chamada dos posts. É a
conversa com o time comercial — o Optimall não tem "baixar o app".

```
https://www.optimall.com.br/fale-conosco
```

Texto do botão: **Fale com um consultor**. Em post, onde não há link clicável: *"Fale com um
consultor: link na bio"* ou o site escrito, `www.optimall.com.br`.

## Contato comercial

| | |
|---|---|
| E-mail | `comercial@optimall.com.br` |
| Telefone | `(41) 93500-4514` — link `tel:+5541935004514` |
| Site | `www.optimall.com.br` |

O fecho do deck (`11-encerramento`) leva os três. WhatsApp **não existe** ainda: não usar.

## Rodapé legal

```
© <ano> - Optimall
```

| Documento | URL |
|---|---|
| Política de Privacidade | `https://www.optimall.com.br/politica-de-privacidade` |
| Termos de Uso | **não existe** — `marca.json` marca `"termos": false` e o `aplicar` tira o link do rodapé |

## Redes sociais

Entram no `90b-social-logo` variante B. Só as redes com URL aqui entram na peça.

| Rede | URL | @ |
|---|---|---|
| Instagram | `https://www.instagram.com/optimall.br/` | `@optimall.br` |
| LinkedIn | `https://www.linkedin.com/company/optimall-sistemas/about/` | Optimall Sistemas |

O Optimall **não tem** Facebook nem Spotify: a `<td>` dessas redes sai da peça.

## Ícones sociais

A mesma forma dos ícones do Podi, na cor principal do Optimall:
`assets/icones/<rede>-marca.png`. Gerados por `scripts/aplicar-marca.py derivar … --gravar`,
nunca desenhados à mão.

## Textos fixos

| Campo em `marca.json` | Texto | Onde entra |
|---|---|---|
| `textos.tagline` | Mais clientes. Mais engajamento. Melhor relacionamento. | Capa e fecho do deck, post de marca |
| `textos.cta_deck` | Fale com um consultor | Botão do e-mail, fecho do deck, chamada do post |
| `textos.rede_deck` | @optimall.br | Fecho do deck, legenda do post |

A frase de apoio da capa, do site: *"Campanhas, Aplicativo, Clube de Benefícios e CRM, tudo em
uma plataforma White Label."* Mais frases aprovadas em [`mensagens.md`](mensagens.md).
