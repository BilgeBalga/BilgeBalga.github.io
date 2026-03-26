# Bilge Balga - Personal Developer Portfolio

[![Deploy](https://github.com/BilgeBalga/BilgeBalga.github.io/actions/workflows/pages/build.yml/badge.svg)](https://BilgeBalga.github.io)

Welcome to the source code of my personal developer portfolio! This repository holds the frontend codebase for my interactive, responsive, and bilingual portfolio site showcasing my projects, tech stack, and professional experience.

🌐 **Live URL:** [https://BilgeBalga.github.io](https://BilgeBalga.github.io)

## 📌 Features

- **Responsive Bento Grid:** Designed with CSS Grid to deliver a clean, tile-based "Bento Box" layout that elegantly resizes across all mobile, tablet, and desktop viewports.
- **Bilingual Support (i18n):** Includes English and Turkish language options through a lightweight custom `lang.js` script with automatic fallback.
- **Micro-interactions:** Custom CSS-driven scroll animations, hover states, blur effects (glassmorphism), and staggered intersection observers (`script.js`).
- **Dynamic Projects Showcase:** Features interactive image galleries for web design iterations, and links directly to live demos or app distributions.
- **Direct Mailto Contact Form:** Integrates a contact form that dynamically structures user inputs into formatted `mailto:` links to open local clients effortlessly.

## 🛠 Tech Stack

Since this is a performant static site, no complicated build pipelines or frameworks are required.

* **HTML5:** Semantic HTML providing accessibility and structure.
* **Vanilla CSS (CSS3):** Heavy use of CSS variables (tokens), Flexbox, CSS Grid, media queries, and `backdrop-filter` for modern styling and layout logic.
* **Vanilla JavaScript (ES6+):** Utilized for:
  * DOM manipulation & Intersection Observers 
  * Mobile burger menu toggles and fluid navigation styling.
  * i18n Language switching logic (`lang.js`).
  * Contact form auto-fill capabilities.

## 📂 Project Structure

```text
├── assets/             # Contains all optimized images (Dental, Antalya Wings, Law Firm demos)
├── index.html          # Main HTML markup containing the UI components
├── style.css           # Global stylesheet and responsive media queries
├── script.js           # Scroll handlers, animations, layout toggles, form behavior
├── lang.js             # Contains the translation dictionaries for EN/TR support
└── README.md           # You are here!
```

## 🚀 Local Development

Running the site locally is extremely straightforward because it uses purely static files without server-side dependencies.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BilgeBalga/BilgeBalga.github.io.git
   cd BilgeBalga.github.io
   ```
2. **Launch a local server:**
   *Using Python:*
   ```bash
   python -m http.server 8000
   ```
   *Using Node (npx):*
   ```bash
   npx serve .
   ```
3. **Open your browser:**
   Navigate to `http://localhost:8000` (or the port specified by your tool) to view the site.

## 📬 Contact

I am open to freelance projects and interesting collaborations! 
- **Email:** bilbalga@gmail.com
- **LinkedIn:** [Bilge Balga](#)
- **GitHub:** [@BilgeBalga](https://github.com/BilgeBalga)

---

&copy; 2026 — Designed & Built by **Bilge Balga**.