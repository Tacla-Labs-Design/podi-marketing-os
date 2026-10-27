# Links e ativos oficiais — Podi

Fixos em todo envio, independentemente da frente. **Copiar do componente, nunca
reescrever à mão.**

## Download do app Podi

```
https://podi.podiapp.com.br/podi-e931a
```

Vale para qualquer rótulo ("Baixar o app", "Baixar o app Podi", "Baixe agora") e para
**as duas metades do botão**: o `href` do `<v:roundrect>` do MSO **e** o `href` do `<a>`.
Nunca `podi.com.br/app` — esse endereço não existe.

## Rodapé legal

Linha de copyright, sem razão social e sem endereço:

```
© <ano> - Podi App
```

| Documento | URL |
|---|---|
| Política de Privacidade | `https://www.podiapp.com.br/politica-privacidade/` |
| Termos de Uso | `https://www.podiapp.com.br/termos-de-uso.html` |

## Redes sociais

Já fixas em `design-system/newsletter/components/90-social.html` e na variante A do
`90b-social-logo.html`. A variante B do `90b` é a única que troca as redes: ela é do
empreendimento, e as URLs vêm do briefing dele.

| Rede | URL |
|---|---|
| Instagram | `https://www.instagram.com/podibr` |
| Facebook | `https://www.facebook.com/podibr` |
| LinkedIn | `https://www.linkedin.com/company/podiapp` |
| Spotify | `https://open.spotify.com/user/31ipyesxy6gxagkbhw3ugdac6fka?si=a0d1d28c642a4abb&nd=1&dlsi=3f8e7ed87ede4cb9` |

O `&` do Spotify vai escapado como `&amp;` no HTML.

## Imagem do fecho "Podi e você, sempre uma parceria perfeita"

Sempre `brand/assets/end-news-img.jpg`. Nunca uma arte nova, nunca uma cópia dentro da
pasta do envio.

## Ícones sociais

Variante **verde** (`brand/assets/icones/*-green.png`, `#48DB84`), por decisão de marca.

No modo claro dá 1,63:1 sobre a página — é **ornamento, não alvo de leitura**. Por isso
o `alt` com o nome da rede é obrigatório em cada ícone, e a área de toque é o que
sustenta o link. Nunca usar o verde para um ícone que precise carregar informação sozinho.

As outras variantes no repositório: `-black` some no dark (1,1:1), `-white` some no claro.

**Exceção — peça com marca do empreendimento:** os ícones são a mesma forma dos `-green`,
recoloridos para a cor base da campanha por `scripts/paleta-empreendimento.py`. Eles ficam
em `saida/<slug>/imagens/icones/` e nunca são gravados em `brand/`
(`design-system/newsletter/guidelines/marca-empreendimento.md`).

## Textos fixos do deck

Entram nos placeholders dos slides `00-capa` e `15-encerramento`
(`design-system/apresentacao/slides/`). Os mesmos valores estão em `marca.json` → `textos`.

| Placeholder | Texto |
|---|---|
| `{{TAGLINE}}` (capa) | `Pensou em Shopping<br>ou Outlet? <strong>Pensou Podi!</strong>` |
| `{{CTA_URL}}` (encerramento) | `https://podi.podiapp.com.br/podi-e931a` |
| `{{CTA_TEXTO}}` (encerramento) | `Baixar o app Podi` |
| `{{REDE}}` (encerramento) | `@podibr` |
