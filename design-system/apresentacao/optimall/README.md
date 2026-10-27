# Slides — apresentação do Optimall

A biblioteca de slides do Optimall: os 12 modelos da *Apresentação Comercial 2026* (Figma),
mais dois derivados das mesmas peças. Cada arquivo é um `<style>` + um `<section class="slide">`
completo — **se copia** para dentro de `templates/apresentacao/base-optimall.html`, não se edita
aqui. Tokens: [`tokens.md`](tokens.md). Canvas, ritmo e QA: [`../guidelines/`](../guidelines/).

Os modelos já vêm com o **texto aprovado** do deck comercial (números oficiais, "o Optimall").
Num deck comercial padrão, boa parte fica como está; num deck sob medida, troca-se o texto
mantendo o formato. Os únicos `{{PLACEHOLDER}}` são os de depoimento — depoimento só entra real.

| Arquivo | O que é | Fundo |
|---|---|---|
| `00-capa.html` | Abertura: logo, a frase da marca, a linha dos módulos | Roxo |
| `01-numeros-clientes.html` | Os 4 números oficiais em pílulas + grade de logos de clientes | Roxo + disco claro |
| `02-problema.html` | A dor: título com destaque, texto, nuvem de ícones, faixa com o logo | Claro |
| `03-plataforma-modulos.html` | A plataforma: 4 módulos em cards ao redor do símbolo + White Label | Roxo |
| `04-modulo-notebooks.html` | Um módulo com 4 itens e três notebooks (Campanhas) | Claro |
| `05-modulo-celular-painel.html` | Um módulo com lista e painel + celular (Clube de Benefícios) | Claro |
| `06-modulo-cards-painel.html` | Um módulo com 5 cards em zigue-zague e painel (CRM & Dados) | Claro |
| `07-app-integracoes.html` | App: grade de recursos, celular na mão, coluna de integrações | Claro |
| `08-white-label.html` | White label: canais, lista e a tela com a marca do shopping | Claro 2 |
| `09-cards-complementares.html` | 3 cards de peso igual, com imagem (módulos complementares) | Claro 2 |
| `10-seguranca.html` | LGPD: título centralizado, ícones de vidro, 2 cards | Branco |
| `11-encerramento.html` | Fecho: logo, a frase da marca, contatos comerciais | Roxo |
| `12-titulo-texto.html` | *Derivado.* Uma ideia só; `titulo-texto--roxo` vira divisor de seção | Claro 2 / roxo |
| `13-citacao.html` | *Derivado.* Depoimento real de cliente | Roxo |

## Como escolher

Pelo **formato da informação**, não pela vontade de variar:

| A informação é… | Slide |
|---|---|
| A abertura | `00-capa` |
| Prova em número e em logo de cliente | `01-numeros-clientes` |
| O problema do shopping | `02-problema` |
| A plataforma inteira em uma tela | `03-plataforma-modulos` |
| Um módulo com poucos itens e o produto em tela grande | `04-modulo-notebooks` |
| Um módulo com lista e painel + app | `05-modulo-celular-painel` |
| Um módulo com 5 recursos que merecem card | `06-modulo-cards-painel` |
| O app e o que ele integra | `07-app-integracoes` |
| A marca do cliente no produto | `08-white-label` |
| Três coisas de peso igual | `09-cards-complementares` |
| Segurança, conformidade, confiança | `10-seguranca` |
| Uma frase que precisa pousar / mudança de assunto | `12-titulo-texto` (roxo = divisor) |
| Uma prova em pessoa | `13-citacao` |
| O pedido e o contato | `11-encerramento` |

Os slides de módulo (`04`–`07`) servem para **qualquer** módulo: troca-se a tag, o título, o
texto, os itens e a imagem de produto. Dois seguidos do mesmo tipo são aceitáveis; cinco não.

**Não existe no Optimall** (ainda): agenda, timeline, tabela e comparativo. Se o conteúdo pedir,
é proposta — ver `/apresentacao-podi` §5. Nunca usar um slide do Podi num deck do Optimall.

## Imagens

Os modelos referenciam `assets/<arquivo>`. Na montagem, copiar de `brand/optimall/assets/`
(`produto/`, `clientes/`, `parceiros/`, `grafismos/`, `fotos/`) para `saida/<slug>/assets/` —
achatado, só o nome do arquivo. O deck precisa abrir sozinho se alguém mandar a pasta.

## Logo e ícones

- Logo: os `<symbol>` do template — negativo sobre roxo, positivo sobre claro. Nunca PNG, nunca
  `filter`, nunca recolorir.
- Ícones: HugeIcons bulk, inline, em `currentColor`. Biblioteca em `brand/optimall/assets/icones-ui/`;
  trocar pelo glifo do assunto mantendo `currentColor`.
