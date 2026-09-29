// Heart Bridge site — shared behaviour (mega menu / hamburger)
document.addEventListener('DOMContentLoaded', function () {
  // Desktop mega menu (click to open, click outside to close)
  document.querySelectorAll('.gnav-item').forEach(function (item) {
    var btn = item.querySelector('button');
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var wasOpen = item.classList.contains('open');
      document.querySelectorAll('.gnav-item.open').forEach(function (o) { o.classList.remove('open'); });
      if (!wasOpen) item.classList.add('open');
    });
  });
  document.addEventListener('click', function () {
    document.querySelectorAll('.gnav-item.open').forEach(function (o) { o.classList.remove('open'); });
  });

  // Mobile hamburger
  var burger = document.querySelector('.hamburger');
  var mnav = document.querySelector('.mobile-nav');
  if (burger && mnav) {
    burger.addEventListener('click', function () {
      var open = burger.classList.toggle('open');
      mnav.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    mnav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        burger.classList.remove('open');
        mnav.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  // Auto-crossfade image carousels (e.g. sponsor card with multiple photos)
  document.querySelectorAll('.carousel').forEach(function (car) {
    var imgs = car.querySelectorAll('img');
    if (imgs.length < 2) return;
    var idx = 0;
    setInterval(function () {
      imgs[idx].classList.remove('active');
      idx = (idx + 1) % imgs.length;
      imgs[idx].classList.add('active');
    }, 3000);
  });

  // Contact form: static demo submit -> thanks page
  var form = document.querySelector('#contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var target = form.getAttribute('data-thanks') || '/contact/thanks/';
      window.location.href = target;
    });
  }
});
