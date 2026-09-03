/* ECOS Medicare Solutions — shared site behavior (no dependencies) */
(function () {
  var ct = document.getElementById('consent_timestamp');
  if (ct) ct.value = new Date().toISOString();
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  // Mobile menu
  var tg = document.querySelector('.nav-toggle'), links = document.getElementById('navLinks');
  if (tg && links) {
    tg.addEventListener('click', function () {
      var open = links.classList.toggle('is-open');
      tg.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && links.classList.contains('is-open')) { links.classList.remove('is-open'); tg.setAttribute('aria-expanded', 'false'); tg.focus(); } });
  }

  // Gentle scroll reveal — skipped when reduced motion is preferred.
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;
  var els = document.querySelectorAll('.section, .stat, .card');
  els.forEach(function (el) { el.classList.add('reveal'); });
  if (!('IntersectionObserver' in window)) { els.forEach(function (el) { el.classList.add('in'); }); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(function (el) { io.observe(el); });
})();
