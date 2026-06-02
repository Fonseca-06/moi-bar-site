# MÔI Bar — Landing Page

> Trabalho prático da disciplina de **Interação Humano-Computador (IHC)**  
> 3º Período · Sistemas de Informação

Site institucional desenvolvido para o **MÔI Bar e Restaurante**, estabelecimento localizado no Setor Bueno, Goiânia - GO.

---

## Sobre o projeto

O MÔI é um bar fundado em 2022 no Setor Bueno, referência na noite goianiense com 44 mil seguidores no Instagram e avaliação 4.3★ no Google. O objetivo do trabalho foi aplicar os princípios de IHC no desenvolvimento de uma interface real, funcional e responsiva para o estabelecimento.

O site foi construído a partir de pesquisa sobre o bar (dados reais de funcionamento, copy baseado na identidade do local) e passou por ciclos de prototipação, análise de usabilidade e refinamento visual.

---

## Tecnologias

- HTML5 semântico
- CSS3 — variáveis, grid, flexbox, media queries, mix-blend-mode
- JavaScript vanilla — scroll behavior, navbar dinâmica
- Fontes: [EB Garamond](https://fonts.google.com/specimen/EB+Garamond) + [DM Sans](https://fonts.google.com/specimen/DM+Sans) via Google Fonts
- Sem frameworks ou bibliotecas externas

---

## Estrutura do projeto

```
moi-bar-site/
├── index.html       # Site completo (single page)
├── server.py        # Servidor local com Cache-Control: no-store
├── imgs/
│   ├── logo.png     # Logo oficial do MÔI (fundo transparente)
│   ├── hero.jpg     # Foto hero — bar escuro com neon laranja
│   ├── crowd.jpg    # Foto ambiente — galera na pista
│   ├── pessoas.jpg  # Foto clientes
│   ├── balcao.jpg   # Foto balcão com Edison bulbs
│   ├── chopp.jpg    # Chopp gelado fundo preto
│   ├── drink.jpg    # Drink autoral fundo escuro
│   ├── interior.jpg # Interior do bar
│   └── petisco.jpg  # Petiscos — batata frita
└── README.md
```

---

## Seções do site

| Seção | Conteúdo |
|---|---|
| **Hero** | Logo, tagline e CTAs sobre foto full-screen |
| **Sobre** | História do bar, quote de avaliação Google, rating |
| **Programação** | Agenda semanal (Qua–Sáb) em layout editorial |
| **Happy Hour** | Promoção de quinta — dobradinha de chopp |
| **Drinks & Petiscos** | Layout assimétrico com 3 itens do cardápio |
| **Galeria** | Grid 2fr/1fr/1fr com fotos do ambiente |
| **Localização** | Endereço real, horários e mapa Google embutido |

---

## Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/Fonseca-06/moi-bar-site.git
cd moi-bar-site

# Inicia o servidor local (sem cache)
python3 server.py
```

Acesse `http://localhost:8000` no navegador.

> O `server.py` serve os arquivos com `Cache-Control: no-store`, evitando cache agressivo do browser durante o desenvolvimento.

---

## Dados reais utilizados

| Campo | Dado |
|---|---|
| Endereço | R. T-59, 166 — Setor Bueno, Goiânia - GO |
| Telefone | (62) 3097-6819 |
| Instagram | [@moigoiania](https://instagram.com/moigoiania) — 44K seguidores |
| Avaliação | 4.3★ no Google · 273 avaliações |
| Horários | Qua 18h–01h · Qui 19h–02h · Sex 19h–03h · Sáb 19h–03h |
| Fundação | Março de 2022 |

---

## Decisões de design

**Paleta:** Preto (`#070707`) com gradiente progressivo para laranja escuro (`#E8610A`), espelhando a identidade visual real do bar no Instagram.

**Tipografia:** EB Garamond para títulos (elegância editorial) + DM Sans para corpo (legibilidade funcional).

**Programação:** Layout de lista editorial em vez de cards simétricos — evita o padrão genérico de "grid de cards iguais" comum em sites gerados automaticamente.

**Imagens:** Unsplash (licença gratuita para uso) + logo oficial fornecida pelo estabelecimento.

---

## Autores

Desenvolvido por **João Pedro Fonseca Moreno** — [@Fonseca-06](https://github.com/Fonseca-06)

Disciplina: Interação Humano-Computador · 3º Período · Sistemas de Informação
