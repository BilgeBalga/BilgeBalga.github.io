'use strict';

/* ================================================================
   BILGE BALGA — PORTFOLIO
   Minimal, purposeful JavaScript.
   No libraries. No side effects.
   ================================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ============================================================
     SCROLL PROGRESS BAR
  ============================================================ */
  const scrollBar = document.getElementById('scrollBar');

  function updateScrollBar() {
    if (!scrollBar) return;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    scrollBar.style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
  }

  /* ============================================================
     NAVIGATION
     – Glass blur on scroll
     – Active link tracking
     – Mobile drawer
  ============================================================ */
  const nav      = document.getElementById('nav');
  const burger   = document.getElementById('navBurger');
  const navLinks = document.getElementById('navLinks');
  const allLinks = document.querySelectorAll('.nav__link');

  function updateNav() {
    if (!nav) return;
    nav.classList.toggle('is-scrolled', window.scrollY > 40);
  }

  function updateActiveLink() {
    const sections  = document.querySelectorAll('section[id]');
    const threshold = window.innerHeight * 0.38;
    let current = '';

    sections.forEach(sec => {
      if (window.scrollY >= sec.offsetTop - threshold) current = sec.id;
    });

    allLinks.forEach(link => {
      const href = link.getAttribute('href').replace('#', '');
      link.classList.toggle('is-active', href === current);
    });
  }

  // Mobile menu
  if (burger && navLinks) {
    burger.addEventListener('click', () => {
      const open = navLinks.classList.toggle('is-open');
      burger.classList.toggle('is-open', open);
      burger.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    });

    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('is-open');
        burger.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });

    document.addEventListener('click', e => {
      if (!nav.contains(e.target) && navLinks.classList.contains('is-open')) {
        navLinks.classList.remove('is-open');
        burger.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  /* ============================================================
     SCROLL-REVEAL — IntersectionObserver
     Stagger delay for sibling .reveal-item elements.
  ============================================================ */
  function getStaggerDelay(el) {
    const siblings = [...el.parentElement.children].filter(c =>
      c.classList.contains('reveal-item')
    );
    return siblings.indexOf(el) * 85;
  }

  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;

      const el    = entry.target;
      const delay = el.classList.contains('reveal-item') ? getStaggerDelay(el) : 0;

      setTimeout(() => el.classList.add('is-visible'), delay);
      revealObs.unobserve(el);
    });
  }, {
    threshold: 0.07,
    rootMargin: '0px 0px -48px 0px'
  });

  document.querySelectorAll('.reveal, .reveal-item').forEach(el => revealObs.observe(el));

  /* ============================================================
     ANIMATED STAT COUNTERS
  ============================================================ */
  const counterObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      animateCounter(entry.target);
      counterObs.unobserve(entry.target);
    });
  }, { threshold: 0.6 });

  document.querySelectorAll('.bento__stat-num[data-target]').forEach(el => {
    counterObs.observe(el);
  });

  function animateCounter(el) {
    const target   = parseInt(el.dataset.target, 10);
    const suffix   = el.dataset.suffix || '+';
    const duration = 1200;
    const start    = performance.now();

    const tick = now => {
      const progress = Math.min((now - start) / duration, 1);
      const eased    = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(eased * target) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  }

  /* ============================================================
     POINTER DEVICE DETECTION
     Parallax and tilt are meaningless on touch-only devices —
     skip them entirely to save battery and avoid jank.
  ============================================================ */
  const isPointerDevice = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ============================================================
     HERO MOUSE PARALLAX — subtle glow movement
  ============================================================ */
  const glow1 = document.querySelector('.hero__glow--1');
  const glow2 = document.querySelector('.hero__glow--2');

  if (isPointerDevice && glow1 && glow2) {
    let rafId = null;
    let targetX = 0, targetY = 0;
    let currentX = 0, currentY = 0;

    document.getElementById('hero')?.addEventListener('mousemove', e => {
      const { innerWidth: w, innerHeight: h } = window;
      targetX = (e.clientX / w - 0.5) * 28;
      targetY = (e.clientY / h - 0.5) * 18;

      if (!rafId) {
        rafId = requestAnimationFrame(function loop() {
          currentX += (targetX - currentX) * 0.06;
          currentY += (targetY - currentY) * 0.06;

          glow1.style.transform = `translate(${currentX * -0.6}px, ${currentY * -0.6}px)`;
          glow2.style.transform = `translate(${currentX * 0.4}px, ${currentY * 0.4}px)`;

          rafId = requestAnimationFrame(loop);
        });
      }
    });

    document.getElementById('hero')?.addEventListener('mouseleave', () => {
      if (rafId) {
        cancelAnimationFrame(rafId);
        rafId = null;
      }
      glow1.style.transform = '';
      glow2.style.transform = '';
    });
  }

  /* ============================================================
     PROJECT CARD — subtle tilt on hover (pointer devices only)
  ============================================================ */
  if (isPointerDevice) {
    document.querySelectorAll('.project-card').forEach(card => {
      card.addEventListener('mousemove', e => {
        const rect   = card.getBoundingClientRect();
        const x      = (e.clientX - rect.left) / rect.width  - 0.5;
        const y      = (e.clientY - rect.top)  / rect.height - 0.5;
        const tiltX  = y * -4;
        const tiltY  = x *  4;

        card.style.transform = `perspective(600px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateZ(2px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });
  }

  /* ============================================================
     CONTACT FORM — Visual feedback
  ============================================================ */
  const form   = document.getElementById('contactForm');
  const submit = document.getElementById('formSubmit');

  if (form && submit) {
    form.querySelectorAll('.field__input').forEach(input => {
      input.addEventListener('blur', () => {
        if (!input.value.trim()) return;
        input.classList.toggle('is-valid',   input.checkValidity());
        input.classList.toggle('is-invalid', !input.checkValidity());
      });

      input.addEventListener('input', () => {
        input.classList.remove('is-valid', 'is-invalid');
      });
    });

    form.addEventListener('submit', e => {
      e.preventDefault();

      const original = submit.textContent;
      submit.textContent = 'Message sent ✓';
      submit.disabled    = true;
      submit.style.background   = '#1a4d10';
      submit.style.borderColor  = '#2a6a18';
      submit.style.color        = '#c8ff6e';

      setTimeout(() => {
        submit.textContent  = original;
        submit.disabled     = false;
        submit.style.background  = '';
        submit.style.borderColor = '';
        submit.style.color       = '';
        form.reset();
        form.querySelectorAll('.field__input').forEach(i => i.classList.remove('is-valid'));
      }, 3500);
    });
  }

  /* ============================================================
     MASTER SCROLL HANDLER — rAF-throttled
  ============================================================ */
  let ticking = false;

  window.addEventListener('scroll', () => {
    if (ticking) return;
    requestAnimationFrame(() => {
      updateScrollBar();
      updateNav();
      updateActiveLink();
      ticking = false;
    });
    ticking = true;
  }, { passive: true });

  // Initial run
  updateScrollBar();
  updateNav();
  updateActiveLink();

});
