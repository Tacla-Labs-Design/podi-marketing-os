# Design System — Post

Posts de rede social: **feed 4:5, 1080 × 1350**, sozinhos ou em carrossel. Saem em PNG, um por
card, prontos para subir no Instagram e no LinkedIn.

```
guidelines/
  ├── canvas.md        O canvas fixo, a margem de segurança, o export em PNG
  ├── carrossel.md     Como um carrossel se organiza: capa, miolo, fecho
  ├── legenda.md       O texto que acompanha o post (legenda, CTA, hashtags)
  └── qa-checklist.md  Checklist obrigatório antes de entregar
optimall/
  ├── README.md        Catálogo dos modelos do Optimall e como escolher
  ├── tokens.md        Cor, tipografia, grafismos do post do Optimall
  └── posts/           Os modelos, um <section class="post"> por arquivo
podi/                  (pendente — os modelos de post do Podi ainda não foram carregados)
```

Shell de montagem: `templates/post/base-<marca>.html`. Procedimento: `/post-podi` e
`/post-optimall` (`.claude/skills/post-podi/SKILL.md`).

## Autoridade

Obedece ao [`brand/`](../../brand/README.md) e não pode contradizê-lo. Cor, logo, fonte e voz
são da marca; aqui só são aplicados a um canvas de 1080 × 1350.

## Uma biblioteca por marca

Post é o material mais "de marca" que existe — a pessoa reconhece a peça no feed antes de ler.
Por isso cada marca tem **os próprios modelos**, tirados dos arquivos de Figma aprovados por
ela, e as regras de canvas, carrossel, legenda e QA são comuns.

| Marca | Modelos | Estado |
|---|---|---|
| Optimall | [`optimall/`](optimall/README.md) — 7 modelos do Figma *Social Media – Optimall* | Pronto |
| Podi | — | **Pendente.** Sem modelo aprovado, o `/post-podi` não monta: avisa quem cuida do repositório |

## O que é específico de post

- **O canvas é fixo** e pequeno na tela do celular. Um post tem uma mensagem; o que não cabe
  vira outro card do carrossel — nunca fonte menor.
- **A leitura é de passagem.** A pessoa decide em um segundo se para. Título grande, pouca
  palavra, imagem de produto ou pessoa que se entende sem legenda.
- **Pode usar CSS moderno** (flex, grid, `var()`, degradê, `backdrop-filter`). Abre no Chrome
  para exportar, não num cliente de e-mail.
- **O texto longo mora na legenda**, não na arte (`guidelines/legenda.md`).

## Alterar isto

Só maintainer. Ver [`docs/governanca.md`](../../docs/governanca.md).
