/* ECOS Medicare Solutions — site analytics (Google Analytics 4)
 *
 * ONE place to configure. Replace MEASUREMENT_ID below with this site's GA4
 * Measurement ID (Google Analytics -> Admin -> Data Streams -> your web stream).
 * Until a real ID is set this file does nothing at all -- no network requests,
 * no broken hits. A placeholder that silently fails looks installed while
 * collecting zero data, so the placeholder is refused explicitly.
 *
 * Tracks, beyond standard pageviews:
 *   click_to_call  -- every tap on a phone number, labelled by placement
 *   generate_lead  -- every lead form submitted, labelled by page and form
 * Mark BOTH as key events (conversions) in GA4: Admin -> Events -> "Mark as key event".
 */
(function () {
  var MEASUREMENT_ID = 'G-XXXXXXXXXX';
  if (!/^G-[A-Z0-9]{8,12}$/.test(MEASUREMENT_ID) || /^G-X+$/.test(MEASUREMENT_ID)) {
    if (window.console && console.info) console.info('[analytics] No GA4 Measurement ID configured yet — tracking is off. Set MEASUREMENT_ID in analytics.js.');
    return;
  }
  var s = document.createElement('script'); s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + MEASUREMENT_ID; document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag; gtag('js', new Date()); gtag('config', MEASUREMENT_ID);
  function placement(el) {
    var map = [['.site-header', 'header'], ['.cta-strip', 'cta strip'], ['.hero', 'hero'], ['.lead-card', 'lead form'],
               ['.faq', 'faq'], ['.site-footer', 'footer'], ['.section', 'body content']];
    for (var i = 0; i < map.length; i++) { try { if (el.closest(map[i][0])) return map[i][1]; } catch (e) {} }
    return 'body';
  }
  function pageInfo() { return { page_path: location.pathname, page_title: (document.title || '').slice(0, 100) }; }
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href^="tel:"]'); if (!a) return;
    var info = pageInfo();
    gtag('event', 'click_to_call', { phone_number: a.getAttribute('href').replace('tel:', ''), link_placement: placement(a), page_path: info.page_path, page_title: info.page_title, transport_type: 'beacon' });
  }, true);
  document.addEventListener('submit', function (e) {
    var f = e.target; if (!f || f.tagName !== 'FORM') return;
    var info = pageInfo(); var topic = f.querySelector('select');
    gtag('event', 'generate_lead', { form_id: f.id || f.getAttribute('name') || 'unnamed', form_placement: placement(f), lead_topic: topic ? topic.value : '', page_path: info.page_path, page_title: info.page_title, transport_type: 'beacon' });
  }, true);
})();
