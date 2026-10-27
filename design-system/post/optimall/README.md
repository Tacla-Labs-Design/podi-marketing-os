# Posts — Optimall

Os 7 modelos de post do Optimall, do Figma *Social Media – Optimall* (seção "posts
aprovados"). Cada arquivo é um `<style>` + um `<section class="post">` de 1080 × 1350 —
**se copia** para dentro de `templates/post/base-optimall.html`. Tokens: [`tokens.md`](tokens.md).
Regras comuns: [`../guidelines/`](../guidelines/).

Os modelos vêm com o texto aprovado do Figma (com "o Optimall" e os números oficiais). Os
únicos `{{PLACEHOLDER}}` são os de depoimento — depoimento só entra real, com nome e cargo.

| Arquivo | O que é | Fundo |
|---|---|---|
| `posts/01-foto-titulo.html` | Foto recortada, título e subtítulo no canto, ícones subindo do celular | Lavanda |
| `posts/02-grade-recursos.html` | Título com destaque desenhado + 4 cards de vidro com ícone | Roxo |
| `posts/03-mockup-painel.html` | Logo e site no topo, título, tela do painel sangrando | Roxo em degradê |
| `posts/04-citacao.html` | Depoimento em painel de vidro escuro | Lavanda + vidro |
| `posts/05-modulos-orbita.html` | "Tudo em 1 plataforma": ícones em órbita do símbolo + painel | Claro |
| `posts/06-foto-faixa-cta.html` | Foto grande, faixa roxa com destaque e lista, pílula de CTA | Lavanda |
| `posts/07-depoimento-foto.html` | Foto grande com card roxo de depoimento | Lavanda |

## Como escolher

| A informação é… | Modelo |
|---|---|
| Uma promessa, com gente | `01-foto-titulo` |
| 3 ou 4 coisas de peso igual (modalidades, módulos, benefícios) | `02-grade-recursos` |
| O produto em tela | `03-mockup-painel` |
| Uma prova em pessoa, sem foto | `04-citacao` |
| A plataforma inteira / tudo integrado | `05-modulos-orbita` |
| Um convite (seja cliente, fale com a gente) com lista de benefícios | `06-foto-faixa-cta` |
| Uma prova em pessoa, com foto | `07-depoimento-foto` |

## No carrossel

| Posição | Modelos que funcionam |
|---|---|
| Capa | `01`, `03`, `05` |
| Miolo | `02` (um card por recurso, repetido), `03` (uma tela por passo), `04`/`07` |
| Fecho | `06` (CTA) |

Estrutura e limites em [`../guidelines/carrossel.md`](../guidelines/carrossel.md).

## Imagens

Na montagem, copiar de `brand/optimall/assets/` (`fotos/`, `produto/`, `grafismos/`) para
`saida/<slug>/assets/`, achatado. Foto nova: mesma proporção do slot e Style Lock do Optimall
(`/foto-optimall`). Tela nova de produto: PNG transparente, na proporção da que substitui.

Não existe (ainda): story 9:16 e quadrado 1:1 — proposta.
