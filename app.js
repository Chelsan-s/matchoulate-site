// MatchOuLate · comportamentos do site: topo que muda ao rolar e blocos que entram com suavidade.
document.documentElement.classList.add("js");

const topo = document.querySelector("[data-topo]");
const atualizarTopo = () => topo.classList.toggle("is-rolado", window.scrollY > 40);
atualizarTopo();
window.addEventListener("scroll", atualizarTopo, { passive: true });

const blocos = document.querySelectorAll(".revela");
if ("IntersectionObserver" in window) {
  const observador = new IntersectionObserver((entradas) => {
    for (const e of entradas) {
      if (e.isIntersecting) { e.target.classList.add("is-visivel"); observador.unobserve(e.target); }
    }
  }, { rootMargin: "0px 0px -12% 0px" });
  blocos.forEach((b) => observador.observe(b));
} else {
  blocos.forEach((b) => b.classList.add("is-visivel"));
}

// Só uma pergunta aberta por vez nas dúvidas
document.querySelectorAll(".duvidas details").forEach((d, _, todas) => {
  d.addEventListener("toggle", () => { if (d.open) todas.forEach((o) => o !== d && (o.open = false)); });
});
