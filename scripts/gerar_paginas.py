"""Gera as páginas internas do site (políticas e segurança) a partir dos textos em conteudo/*.md.
Uso (na pasta do site):  python scripts/gerar_paginas.py      (precisa do pacote "markdown": pip install markdown)
Para mudar um texto, edite o .md correspondente e rode de novo."""
import html
from pathlib import Path
import markdown

RAIZ = Path(__file__).resolve().parents[1]
CONTEUDO = RAIZ / "conteudo"
PAGINAS = [  # (arquivo .md, página gerada, título, aviso de minuta?)
    ("termos-de-uso.md", "termos.html", "Termos de Uso", True),
    ("politica-de-privacidade.md", "privacidade.html", "Política de Privacidade", True),
    ("excluir-conta.md", "excluir-conta.html", "Excluir conta", False),
    ("central.md", "seguranca.html", "Central de Segurança", False),
    ("regras-da-comunidade.md", "regras-da-comunidade.html", "Regras da comunidade", False),
    ("dicas-de-seguranca.md", "dicas-de-seguranca.html", "Dicas de segurança", False),
    ("como-denunciar.md", "como-denunciar.html", "Como denunciar", False),
]
LINKS = {"(termos-de-uso.md)": "(termos.html)", "(politica-de-privacidade.md)": "(privacidade.html)"}

MODELO = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · MatchOuLate</title>
<meta name="theme-color" content="#1E88E5">
<link rel="icon" href="img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lilita+One&family=Nunito:ital,wght@0,500;0,600;0,700;0,800;0,900;1,800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<script>try{{if(/[?&]app=1/.test(location.search))sessionStorage.setItem("app","1")}}catch(e){{}}if(/[?&]app=1/.test(location.search)||(function(){{try{{return sessionStorage.getItem("app")==="1"}}catch(e){{return false}}}})())document.documentElement.classList.add("no-app")</script>
</head>
<body class="pagina">
<header class="topo is-rolado">
  <a class="marca" href="index.html" aria-label="MatchOuLate, início"><img src="img/logo.png" alt="" width="54" height="40"><span>MatchOuLate</span></a>
  <nav class="menu" aria-label="Páginas">
    <a href="seguranca.html">Segurança</a><a href="termos.html">Termos</a><a href="privacidade.html">Privacidade</a><a href="excluir-conta.html">Excluir conta</a>
  </nav>
  <a class="botao botao--amarelo botao--pequeno" href="index.html#baixar">Baixar o app</a>
</header>
<main class="documento">
{aviso}{corpo}
</main>
<footer class="rodape">
  <div class="rodape__marca"><img src="img/logo-branco.png" alt="" width="54" height="40"><p><strong>MatchOuLate</strong><br>O app que aproxima tutores de pets.</p></div>
  <div class="redes"><a href="https://www.instagram.com/matchoulate/" target="_blank" rel="noopener" aria-label="Instagram do MatchOuLate"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.3"/></svg></a><a href="https://www.tiktok.com/@matchoulateoficial" target="_blank" rel="noopener" aria-label="TikTok do MatchOuLate"><svg viewBox="0 0 24 24"><path d="M16.6 3c.4 2.2 1.9 3.8 4.1 4v3.1c-1.5 0-2.9-.4-4.1-1.2v6.4c0 3.6-2.6 5.9-5.7 5.9-3.2 0-5.6-2.5-5.6-5.6 0-3.4 2.9-5.9 6.4-5.5v3.2c-1.6-.4-3.2.7-3.2 2.4 0 1.3 1 2.4 2.4 2.4 1.5 0 2.5-1 2.5-2.9V3h3.2z"/></svg></a><a href="https://www.youtube.com/@MatchouLate" target="_blank" rel="noopener" aria-label="YouTube do MatchOuLate"><svg viewBox="0 0 24 24"><path d="M22 8.2c-.2-1.6-1-2.7-2.6-2.9C17 5 12 5 12 5s-5 0-7.4.3C3 5.5 2.2 6.6 2 8.2 1.8 9.6 1.8 12 1.8 12s0 2.4.2 3.8c.2 1.6 1 2.7 2.6 2.9C7 19 12 19 12 19s5 0 7.4-.3c1.6-.2 2.4-1.3 2.6-2.9.2-1.4.2-3.8.2-3.8s0-2.4-.2-3.8zM10 15V9l5.2 3L10 15z"/></svg></a></div>
  <nav class="rodape__links" aria-label="Links legais e de ajuda">
    <a href="seguranca.html">Central de Segurança</a><a href="termos.html">Termos de Uso</a><a href="privacidade.html">Política de Privacidade</a><a href="excluir-conta.html">Excluir conta</a><a href="mailto:matchoulate@gmail.com">Suporte: matchoulate@gmail.com</a>
  </nav>
  <p class="rodape__legal">© 2026 Sudotech Corretora de Seguros LTDA · CNPJ 63.894.289/0001-50 · Rio de Janeiro/RJ</p>
</footer>
</body>
</html>
"""
AVISO = '<p class="documento__aviso">Versão preliminar, em revisão jurídica. Pode ser atualizada antes do lançamento oficial do aplicativo.</p>\n'

for origem, destino, titulo, minuta in PAGINAS:
    texto = (CONTEUDO / origem).read_text()
    for a, b in LINKS.items():
        texto = texto.replace(a, b)
    corpo = markdown.markdown(texto, extensions=["tables", "sane_lists", "md_in_html"])
    (RAIZ / destino).write_text(MODELO.format(titulo=html.escape(titulo), aviso=AVISO if minuta else "", corpo=corpo))
    print("gerada:", destino)
