# Marcas — e-mail do Podi ou do Optimall

O Marketing OS tem duas marcas irmãs e **um** design system de e-mail. A peça do Optimall tem
a mesma estrutura, os mesmos blocos e o mesmo estilo da do Podi; muda a paleta, o logo, as
redes, os links e o rodapé. Regras de marca: [`brand/README.md`](../../../brand/README.md).

Isto **não é** o modo empreendimento ([`marca-empreendimento.md`](marca-empreendimento.md)):
lá a cor vem do briefing do shopping, cada campanha é derivada na hora e o modo é sempre
claro. Aqui a marca é fixa, a paleta foi aprovada uma vez pelo maintainer e **o dark mode
fica**.

## Qual marca é a peça

| Sinal | Marca |
|---|---|
| Comando `/newsletter-optimall`, ou `Marca: Optimall` no briefing | Optimall |
| Comando `/newsletter-podi`, `Marca: Podi`, ou nada dito | Podi |

Se o briefing fala de gestor de shopping, venda B2B ou do Optimall e não diz a marca,
**perguntar**. O modo empreendimento é só do Podi.

## Antes de montar

```bash
python3 scripts/aplicar-marca.py validar optimall
```

- **Saída 0** → seguir.
- **Saída 1** → **parar**. A marca está pendente ou incompleta. Dizer em português comum:
  *"a identidade do Optimall ainda não está completa no padrão — avise quem cuida do
  repositório"*. Não montar com as cores do Podi "por enquanto".

## Blocos

| Parte | Podi | Optimall |
|---|---|---|
| Header | `00-hero-podi-news` ou `01-header` (Podi + Tacla Labs) | `01b-header-empreendimento`, com logo e nome do Optimall |
| Conteúdo | `02` a `13b` | `02` a `13b` — os mesmos |
| Rodapé social | `90-social` ou `90b` variante A | `90b-social-logo` variante B, com as redes do Optimall |
| Rodapé legal | `91-footer-legal` | `91-footer-legal` — o script troca assinatura e links |
| Shell | `templates/newsletter/base.html` | `templates/newsletter/base.html` — o mesmo, com dark mode |

A peça do Optimall **não cita o Podi nem a Tacla Labs** — nem no texto, nem no `alt`, nem na
imagem do fecho (`end-news-img.jpg` é do Podi). O Podi News é uma publicação do Podi: não
existe edição do Podi News assinada pelo Optimall.

Preencher a partir de `brand/optimall/marca.json`:

| Placeholder | Campo |
|---|---|
| `{{URL_LOGO_EMPREENDIMENTO}}` | `logo.png` (caminho relativo `../../brand/optimall/…` a partir de `saida/<slug>/`) |
| `{{LARGURA_LOGO}}` | `logo.png_largura` — largura exibida a 24px de altura |
| `{{NOME_EMPREENDIMENTO}}` | `nome` |
| `{{URL_INSTAGRAM}}`, `{{URL_FACEBOOK}}`, `{{URL_LINKEDIN}}` | `redes.*` — rede sem URL sai da peça (apagar a `<td>`) |
| `{{URL_CTA}}` do CTA principal | `links.cta` |
| `{{LABEL_CTA}}` do CTA principal | `textos.cta_deck` — *Fale com um consultor* |

Texto — manchete, corpo, números, frases — sai de
[`brand/optimall/mensagens.md`](../../../brand/optimall/mensagens.md): B2B, números oficiais,
um CTA. O Optimall não tem Facebook: a `<td>` do Facebook sai do `90b`.

## Depois de montar: recolorir

Monte a peça inteira com os blocos como estão — valores do Podi — e rode:

```bash
python3 scripts/aplicar-marca.py aplicar optimall saida/<slug>/index.html
```

O script troca, numa passada só:

- cada cor do Podi pelo **mesmo papel** do Optimall — fundo, card, tag, linha, link de marca,
  dark mode — em `style`, `bgcolor`, `fillcolor` do VML e no `<style>` do dark mode;
- o texto do botão, **só nas duas metades do CTA**, se o `ink-on-brand` do Optimall for outro
  — e é: no Optimall o botão é roxo `#9934FF` com texto **branco**;
- os ícones sociais (`-green.png` do Podi → `-marca.png` do Optimall);
- os links legais, o CTA e as redes que ainda forem do Podi — e, como o Optimall **não tem
  Termos de Uso** (`"termos": false`), tira o link de termos e o separador do rodapé legal;
- `© <ano> - Podi App` → `© <ano> - Optimall`;
- a classe `.logo-tacla` do `<style>`, que não tem uso sem a Tacla Labs.

Nunca trocar cor à mão, nem "corrigir" um valor que o script gravou.

## Conferir

O `aplicar` já confere no fim; para conferir de novo, só leitura:

```bash
python3 scripts/aplicar-marca.py conferir optimall saida/<slug>/index.html   # saída 0
```

Ele acusa:

- cor do Podi sobrando, ou cor fora da paleta do Optimall;
- qualquer menção a Podi, Tacla Labs, `podiapp`, `podibr`, `podinews` ou asset de `brand/podi/`
  (fora de comentário);
- `{{...}}` fora das variáveis que o sistema de envio do Optimall aceita. **Enquanto a regra
  de envio estiver pendente, nenhuma é aceita** — tirar o `{{email}}` do rodapé ("Você
  recebeu este e-mail porque …") e avisar na entrega.

Pendência aqui é correção antes de entregar, não item de relatório.

## Na entrega

Além do relatório de sempre (`qa-checklist.md`): a marca, a saída do `conferir`, os ícones e o
logo do Optimall a hospedar, e — enquanto valer — o aviso de que **a regra de envio do Optimall
está pendente** e a peça não pode sair pelo servidor do Podi.
