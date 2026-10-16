# Site do MatchOuLate

Site de divulgação e download do app, em HTML, CSS e JavaScript puros: não precisa de build nem de framework. Qualquer hospedagem de site estático serve (GitHub Pages, Netlify, Vercel, Cloudflare Pages, Hostinger).

## Ver no computador

Abra `index.html` no navegador.

## Estrutura

| Caminho | O que é |
| --- | --- |
| `index.html` | A página principal |
| `styles.css` | Todo o visual (cores da marca no topo do arquivo) |
| `app.js` | Topo que muda ao rolar, entrada suave dos blocos e perguntas frequentes |
| `img/` | Logos e selos das lojas |
| `img/pets/` | Fotos dos pets (Unsplash, uso comercial livre; origem de cada uma em `CREDITOS.md`) |
| `conteudo/*.md` | Textos das políticas e da Central de Segurança |
| `scripts/gerar_paginas.py` | Gera `termos.html`, `privacidade.html`, `excluir-conta.html` e as páginas de segurança a partir de `conteudo/` |
| `*.html` (demais) | Páginas geradas; não edite direto, edite o `.md` e gere de novo |

## Mudar um texto legal ou de segurança

```bash
pip install markdown
python scripts/gerar_paginas.py
```

Os mesmos textos ficam versionados no repositório do app em `docs/juridico` e `docs/seguranca`. Mantenha as duas cópias iguais.

## Antes de lançar

- **Links das lojas:** quando o app for publicado, troque os `href="#"` e `href="#baixar"` dos selos pelos links da App Store e do Google Play, e tire o aviso "Chegando às lojas em breve". Pelas regras da Apple e do Google, os selos só devem apontar para o app publicado.
- **Fotos:** as de `img/pets/` vêm do Unsplash. Quando houver fotos de pets da equipe ou de usuários (com autorização por escrito), troque mantendo o nome do arquivo.
- **Telas do app:** a seção "Por dentro do app" usa prints reais do iPhone (`img/app-inicio.jpg`, `app-explorar.jpg`, `app-perfil.jpg`, sem a engrenagem do Expo Go). Para trocar, salve um print novo com o mesmo nome (proporção 739×1600). `img/tela-*.png` não são mais usadas e podem ser apagadas.
- **Domínio:** com o domínio próprio (ex.: matchoulate.com.br), atualize no app o endereço das páginas legais (`services/links.js`) para este site.
- **Revisão jurídica:** depois do parecer, tire o aviso "Versão preliminar" (`AVISO` em `scripts/gerar_paginas.py`) e preencha a data de publicação nos textos.
