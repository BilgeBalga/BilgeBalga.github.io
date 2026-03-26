import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

with open("index.html.bak", "w", encoding="utf-8") as f:
    f.write(text)

def replace_first(pattern, replacement, string):
    return string.replace(pattern, replacement, 1)

text = text.replace('<li><a href="#about"      class="nav__link">About</a></li>', '<li><a href="#about"      class="nav__link" data-i18n="nav_about">About</a></li>')
text = text.replace('<li><a href="#stack"      class="nav__link">Stack</a></li>', '<li><a href="#stack"      class="nav__link" data-i18n="nav_stack">Stack</a></li>')
text = text.replace('<li><a href="#experience" class="nav__link">Experience</a></li>', '<li><a href="#experience" class="nav__link" data-i18n="nav_exp">Experience</a></li>')
text = text.replace('<li><a href="#work"       class="nav__link">Projects</a></li>', '<li><a href="#work"       class="nav__link" data-i18n="nav_work">Projects</a></li>')
text = text.replace('<li><a href="#contact"    class="nav__link">Contact</a></li>', '<li><a href="#contact"    class="nav__link" data-i18n="nav_contact">Contact</a></li>')

nav_buttons = """      </nav>

      <div class="lang-switch">
        <button id="btn-en" class="is-active" aria-label="English">EN</button>
        <span class="lang-sep">|</span>
        <button id="btn-tr" aria-label="Türkçe">TR</button>
      </div>

      <button"""
text = text.replace('      </nav>\n\n      <button', nav_buttons)

text = text.replace('Available for new roles\n          </p>', 'Available for new roles\n          </p>').replace('Available for new roles', '<span data-i18n="hero_available">Available for new roles</span>')
text = text.replace('<p class="hero__role">Backend Engineer & AI Integrations</p>', '<p class="hero__role" data-i18n="hero_role">Backend Engineer & AI Integrations</p>')
text = text.replace('<span>Backend Systems</span>', '<span data-i18n="hero_tag1">Backend Systems</span>')
text = text.replace('<span>API Design</span>', '<span data-i18n="hero_tag2">API Design</span>')
text = text.replace('<span>AI & ML Integration</span>', '<span data-i18n="hero_tag3">AI & ML Integration</span>')

text = text.replace('<a href="#work"    class="btn btn--solid">View Projects</a>', '<a href="#work"    class="btn btn--solid" data-i18n="hero_btn_work">View Projects</a>')
text = text.replace('<a href="#contact" class="btn btn--outline">Contact</a>', '<a href="#contact" class="btn btn--outline" data-i18n="hero_btn_contact">Contact</a>')

text = text.replace('<h2 class="service-title">Backend Engineering</h2>', '<h2 class="service-title" data-i18n="svc_title1">Backend Engineering</h2>')
text = text.replace('<p class="service-desc">Developing scalable REST APIs and backend services using Python, FastAPI, Flask, and Go. Building production-ready solutions with JWT-based security, database design (MySQL, MongoDB), and hardware–software integration in Raspberry Pi-based systems</p>', '<p class="service-desc" data-i18n="svc_desc1">Developing scalable REST APIs and backend services using Python, FastAPI, Flask, and Go. Building production-ready solutions with JWT-based security, database design (MySQL, MongoDB), and hardware–software integration in Raspberry Pi-based systems</p>')
text = text.replace('<h2 class="service-title">AI & ML Integration</h2>', '<h2 class="service-title" data-i18n="svc_title2">AI & ML Integration</h2>')
text = text.replace('<p class="service-desc">I got practical experience in machine learning by working on various AI projects. I also worked as a volunteer assistant instructor in this field. In one specific project, I used Natural Language Processing (NLP). I did data cleaning, tokenization, and model integration using tools like Scikit-learn, TensorFlow, and NLTK.</p>', '<p class="service-desc" data-i18n="svc_desc2">I got practical experience in machine learning by working on various AI projects. I also worked as a volunteer assistant instructor in this field. In one specific project, I used Natural Language Processing (NLP). I did data cleaning, tokenization, and model integration using tools like Scikit-learn, TensorFlow, and NLTK.</p>')
text = text.replace('<h2 class="service-title">Data Pipelines & Scraping</h2>', '<h2 class="service-title" data-i18n="svc_title3">Data Pipelines & Scraping</h2>')
text = text.replace('<p class="service-desc">Developing web scraping processes with BeautifulSoup and Pandas for large-scale data collection and processing. Cleaning and optimizing raw data to create high-quality datasets for NLP models.</p>', '<p class="service-desc" data-i18n="svc_desc3">Developing web scraping processes with BeautifulSoup and Pandas for large-scale data collection and processing. Cleaning and optimizing raw data to create high-quality datasets for NLP models.</p>')

text = text.replace('<span>Scroll</span>', '<span data-i18n="hero_scroll">Scroll</span>')

text = text.replace('<h2 class="section__title" id="about-heading">About</h2>', '<h2 class="section__title" id="about-heading" data-i18n="about_title">About</h2>')
text = text.replace('<h2 class="section__title" id="about-heading">About</h2>', '<h2 class="section__title" id="about-heading" data-i18n="about_title">About</h2>')

text = text.replace('<p class="label">Who I am</p>', '<p class="label" data-i18n="about_who">Who I am</p>')

text = text.replace('<p class="bento__bio-text">\n              I am Bilge Balga. I graduated with a degree in <strong> Computer Engineering </strong> in 2024. I am a software developer focusing on backend development and machine learning.\n              Currently, I work in hardware and software integration; I manage the <strong> Python </strong> development processes of  <strong> Raspberry Pi-based </strong> systems. In my previous experiences, I developed full-stack web projects using Go, React, and Vue.js. I also built the backend and APIs of a real estate system with Python Flask, and performed data optimizations for NLP models.\n            </p>', '<p class="bento__bio-text" data-i18n="about_p1">\n              Hi, I\'m Bilge, a 2024 <strong>Computer Engineering</strong> graduate focused on <strong>Backend</strong> and <strong>Machine Learning</strong>. Currently, I manage hardware-software integration and <strong>Python</strong> development for <strong>Raspberry Pi</strong> systems.\n            </p>')

text = text.replace('<p class="bento__bio-text">\n              Outside of my professional work, I constantly keep creating; along with my personal projects, I develop customer automations for clinics and custom web projects for companies. Additionally, I previously contributed to knowledge sharing by working as an assistant instructor at BTK Academy and Tech Istanbul.\n              My goal is to build simple and sustainable systems that solve complex problems with technology.\n            </p>', '<p class="bento__bio-text" data-i18n="about_p2">\n              Previously, I built <strong>full-stack</strong> projects with <strong>Go</strong>, <strong>React</strong>, and <strong>Vue.js</strong>, and developed <strong>Python Flask</strong> APIs with <strong>NLP</strong> optimizations. I also build automations for clinics and mentor in tech communities. My goal: solving complex problems with <strong>simple, sustainable systems</strong>.\n            </p>')
text = text.replace('<p class="label">Currently working on</p>', '<p class="label" data-i18n="about_now">Currently working on</p>')
text = text.replace('Raspberry Pi-based systems\n              </li>', '<span data-i18n="now_li1">Raspberry Pi-based systems</span>\n              </li>')
text = text.replace('FastAPI backends &amp; scalable AI integrations\n              </li>', '<span data-i18n="now_li2">FastAPI backends &amp; scalable AI integrations</span>\n              </li>')
text = text.replace('<p class="label">Education</p>', '<p class="label" data-i18n="edu_label">Education</p>')
text = text.replace('<p class="bento__degree">B.S. Computer Engineering</p>', '<p class="bento__degree" data-i18n="edu_deg">B.S. Computer Engineering</p>')

text = text.replace('<p class="bento__stat-label">Projects shipped</p>', '<p class="bento__stat-label" data-i18n="stat_proj">Projects shipped</p>')
text = text.replace('<p class="bento__stat-label">Internships</p>', '<p class="bento__stat-label" data-i18n="stat_int">Internships</p>')

text = text.replace('<p class="label">Based in</p>', '<p class="label" data-i18n="loc_label">Based in</p>')
text = text.replace('<p class="bento__city">Antalya, Turkey</p>', '<p class="bento__city" data-i18n="loc_val">Antalya, Turkey</p>')

text = text.replace('<p class="label">Leadership &amp; Recognition</p>', '<p class="label" data-i18n="certs_label">Leadership &amp; Recognition</p>')
text = text.replace('<li>AI Expertise Bootcamp Instructor — Tech Istanbul</li>', '<li data-i18n="cert1">AI Expertise Bootcamp Instructor — Tech Istanbul</li>')
text = text.replace('<li>Advanced ML &amp; AI Workshop Instructor — BTK Academy</li>', '<li data-i18n="cert2">Advanced ML &amp; AI Workshop Instructor — BTK Academy</li>')
text = text.replace('<li>GDG Antalya Community Member</li>', '<li data-i18n="cert3">GDG Antalya Community Member</li>')

text = text.replace('<h2 class="section__title" id="stack-heading">Stack</h2>', '<h2 class="section__title" id="stack-heading" data-i18n="stack_title">Stack</h2>')
text = text.replace('<h3 class="stack-col__title">Languages</h3>', '<h3 class="stack-col__title" data-i18n="stack_col1">Languages</h3>')
text = text.replace('<h3 class="stack-col__title">Web &amp; APIs</h3>', '<h3 class="stack-col__title" data-i18n="stack_col2">Web &amp; APIs</h3>')
text = text.replace('<h3 class="stack-col__title">Tools</h3>', '<h3 class="stack-col__title" data-i18n="stack_col3">Tools</h3>')
text = text.replace('<h3 class="stack-col__title">AI & Data Science</h3>', '<h3 class="stack-col__title" data-i18n="stack_col4">AI & Data Science</h3>')
text = text.replace('<h3 class="stack-col__title">Embedded & Vision</h3>', '<h3 class="stack-col__title" data-i18n="stack_col5">Embedded & Vision</h3>')


text = text.replace('<h2 class="section__title" id="exp-heading">Experience</h2>', '<h2 class="section__title" id="exp-heading" data-i18n="exp_title">Experience</h2>')

# Experience months
text = replace_first('<time class="timeline__date">Dec 2025 - Present</time>', '<time class="timeline__date" data-i18n="exp_mth1">Dec 2025 - Present</time>', text)
text = replace_first('<h3 class="timeline__role">Software Developer</h3>', '<h3 class="timeline__role" data-i18n="exp_role1">Software Developer</h3>', text)
text = text.replace('<p class="timeline__desc">\n                Working on hardware–software integration in a <strong>Raspberry Pi–based</strong> system. Managing system control and validation processes for <strong>Python-based</strong> applications. Responsible for testing configuration-based structures in field environments and ensuring system stability.\n              </p>', '<p class="timeline__desc" data-i18n="exp_desc1">\n                Working on hardware–software integration in a <strong>Raspberry Pi–based</strong> system. Managing system control and validation processes for <strong>Python-based</strong> applications. Responsible for testing configuration-based structures in field environments and ensuring system stability.\n              </p>')

text = replace_first('<time class="timeline__date">Oct – Nov 2024</time>', '<time class="timeline__date" data-i18n="exp_mth2">Oct – Nov 2024</time>', text)
text = text.replace('<h3 class="timeline__role">Artificial Intelligence Engineer Intern</h3>', '<h3 class="timeline__role" data-i18n="exp_role2">Artificial Intelligence Engineer Intern</h3>')
text = text.replace('<p class="timeline__desc">\n                Built a Python + BeautifulSoup <strong>web scraping pipeline</strong> that significantly improved data consistency across Turkish NLP datasets, enabling cleaner model training. Engineered full CRUD operations and <strong>REST APIs with Flask and MySQL</strong>, complete with a secure authentication layer — delivering a production-ready backend in a fast-paced AI environment. Also developed a React-based automated rent payment notification system, directly improving end-user experience.\n              </p>', '<p class="timeline__desc" data-i18n="exp_desc2">\n                Built a Python + BeautifulSoup <strong>web scraping pipeline</strong> that significantly improved data consistency across Turkish NLP datasets, enabling cleaner model training. Engineered full CRUD operations and <strong>REST APIs with Flask and MySQL</strong>, complete with a secure authentication layer — delivering a production-ready backend in a fast-paced AI environment. Also developed a React-based automated rent payment notification system, directly improving end-user experience.\n              </p>')

text = replace_first('<time class="timeline__date">Feb – May 2024</time>', '<time class="timeline__date" data-i18n="exp_mth3">Feb – May 2024</time>', text)
text = text.replace('<h3 class="timeline__role">Full Stack Developer Intern</h3>', '<h3 class="timeline__role" data-i18n="exp_role3">Full Stack Developer Intern</h3>')
text = text.replace('<p class="timeline__desc">\n                Spearheaded improvements to the <strong>software testing suite in Go</strong>, raising code quality standards and contributing to more stable, reliable releases. Took ownership of the <strong>localization infrastructure</strong> for a multilingual application, enabling the product to reach wider audiences. Built the full project scaffolding from scratch — folder structure, core components, models, services, handlers, and a Vue.js control panel — while integrating Docker to streamline development workflows.\n              </p>', '<p class="timeline__desc" data-i18n="exp_desc3">\n                Spearheaded improvements to the <strong>software testing suite in Go</strong>, raising code quality standards and contributing to more stable, reliable releases. Took ownership of the <strong>localization infrastructure</strong> for a multilingual application, enabling the product to reach wider audiences. Built the full project scaffolding from scratch — folder structure, core components, models, services, handlers, and a Vue.js control panel — while integrating Docker to streamline development workflows.\n              </p>')

text = replace_first('<time class="timeline__date">Jul – Sep 2023</time>', '<time class="timeline__date" data-i18n="exp_mth4">Jul – Sep 2023</time>', text)
text = text.replace('<h3 class="timeline__role">Software Developer Intern</h3>', '<h3 class="timeline__role" data-i18n="exp_role4">Software Developer Intern</h3>')
text = text.replace('<p class="timeline__desc">\n                Collaborated in a cross-functional team to build a <strong>Food App web application</strong> from concept to delivery. Focused on frontend development with React, Redux, and JavaScript while working in close coordination with the backend team — gaining practical experience in real-world agile collaboration, feature handoffs, and iterative product development.\n              </p>', '<p class="timeline__desc" data-i18n="exp_desc4">\n                Collaborated in a cross-functional team to build a <strong>Food App web application</strong> from concept to delivery. Focused on frontend development with React, Redux, and JavaScript while working in close coordination with the backend team — gaining practical experience in real-world agile collaboration, feature handoffs, and iterative product development.\n              </p>')


text = text.replace('<h2 class="section__title" id="work-heading">Projects</h2>', '<h2 class="section__title" id="work-heading" data-i18n="work_title">Projects</h2>')
text = text.replace('<span class="project-featured__tag">Featured</span>', '<span class="project-featured__tag" data-i18n="proj_feat">Featured</span>')
text = text.replace('<strong>Problem:</strong> Property teams were managing tenant data, lease records, and notifications through scattered spreadsheets and manual emails.', '<span data-i18n="proj_prob1"><strong>Problem:</strong> Property teams were managing tenant data, lease records, and notifications through scattered spreadsheets and manual emails.</span>')
text = text.replace('Built an end-to-end platform with a Flask REST backend and React frontend — JWT-secured endpoints, tenant record management, lease tracking, and automated email notifications via a clean API layer.', '<span data-i18n="proj_sol1">Built an end-to-end platform with a Flask REST backend and React frontend — JWT-secured endpoints, tenant record management, lease tracking, and automated email notifications via a clean API layer.</span>')
text = text.replace('<a href="#" class="btn btn--solid btn--sm">View Code</a>', '<a href="#" class="btn btn--solid btn--sm" data-i18n="btn_code">View Code</a>')
text = text.replace('<a href="#" class="btn btn--outline btn--sm">Live Demo</a>', '<a href="#" class="btn btn--outline btn--sm" data-i18n="btn_demo">Live Demo</a>')

text = text.replace('<p class="project-card__desc">\n              Business-grade stock control system with full CRUD operations, reporting dashboards, and role-based access control. Replaced a manual spreadsheet workflow.\n            </p>', '<p class="project-card__desc" data-i18n="proj_desc2">\n              Business-grade stock control system with full CRUD operations, reporting dashboards, and role-based access control. Replaced a manual spreadsheet workflow.\n            </p>')
text = text.replace('<p class="project-card__desc">\n              Built from scratch — Go web service with models, handlers, and repository layer. Full admin control panel in Vue.js with Docker containerisation and integration tests.\n            </p>', '<p class="project-card__desc" data-i18n="proj_desc3">\n              Built from scratch — Go web service with models, handlers, and repository layer. Full admin control panel in Vue.js with Docker containerisation and integration tests.\n            </p>')
text = text.replace('<p class="project-card__desc">\n              Production-ready food ordering interface with React and Redux — cart management, checkout flow, and clean component architecture using CSS Modules.\n            </p>', '<p class="project-card__desc" data-i18n="proj_desc4">\n              Production-ready food ordering interface with React and Redux — cart management, checkout flow, and clean component architecture using CSS Modules.\n            </p>')
text = text.replace('<p class="project-card__desc">\n              CNN model classifying 7 varieties of date fruit with 95%+ accuracy. Packaged as a Streamlit web app and deployed to Hugging Face Spaces.\n            </p>', '<p class="project-card__desc" data-i18n="proj_desc5">\n              CNN model classifying 7 varieties of date fruit with 95%+ accuracy. Packaged as a Streamlit web app and deployed to Hugging Face Spaces.\n            </p>')
text = text.replace('<p class="project-card__desc">\n              An AI-driven platform designed to detect and interpret human emotional signals through natural language processing. Combines real-time sentiment analysis with a scalable FastAPI backend to power emotionally-aware applications.\n            </p>', '<p class="project-card__desc" data-i18n="proj_desc6">\n              An AI-driven platform designed to detect and interpret human emotional signals through natural language processing. Combines real-time sentiment analysis with a scalable FastAPI backend to power emotionally-aware applications.\n            </p>')


text = text.replace('<h2 class="section__title" id="contact-heading">Let\'s talk</h2>', '<h2 class="section__title" id="contact-heading" data-i18n="contact_title">Let\'s talk</h2>')
text = text.replace('<p class="contact-info__lede">\n              I\'m open to freelance projects, and interesting collaborations. Have a project in mind or just want to say hello — reach out.\n            </p>', '<p class="contact-info__lede" data-i18n="contact_lede">\n              I\'m open to freelance projects, and interesting collaborations. Have a project in mind or just want to say hello — reach out.\n            </p>')
text = text.replace('<span class="contact-info__label">Email</span>', '<span class="contact-info__label" data-i18n="contact_email">Email</span>')
text = text.replace('<span class="contact-info__label">Location</span>', '<span class="contact-info__label" data-i18n="contact_loc">Location</span>')

text = text.replace('<label class="field__label" for="f-name">Name</label>', '<label class="field__label" for="f-name" data-i18n="form_name">Name</label>')
text = text.replace('placeholder="Your name"', 'placeholder="Your name" data-i18n-placeholder="form_name_ph"')
text = replace_first('<label class="field__label" for="f-email">Email</label>', '<label class="field__label" for="f-email" data-i18n="form_email">Email</label>', text)
text = text.replace('placeholder="you@example.com"', 'placeholder="you@example.com" data-i18n-placeholder="form_email_ph"')
text = text.replace('<label class="field__label" for="f-message">Message</label>', '<label class="field__label" for="f-message" data-i18n="form_msg">Message</label>')
text = text.replace('placeholder="Tell me about the project or opportunity…"', 'placeholder="Tell me about the project or opportunity…" data-i18n-placeholder="form_msg_ph"')
text = text.replace('<button type="submit" class="btn btn--solid btn--full" id="formSubmit">Send Message</button>', '<button type="submit" class="btn btn--solid btn--full" id="formSubmit" data-i18n="btn_submit">Send Message</button>')

text = text.replace('<span class="footer__copy">&copy; 2026 — Designed &amp; built by Bilge Balga</span>', '<span class="footer__copy" data-i18n="footer_copy">&copy; 2026 — Designed &amp; built by Bilge Balga</span>')
text = text.replace('<a href="#hero" class="footer__top" aria-label="Back to top">Back to top ↑</a>', '<a href="#hero" class="footer__top" aria-label="Back to top" data-i18n="footer_top">Back to top ↑</a>')

text = text.replace('<script src="script.js"></script>', '<script src="lang.js"></script>\n  <script src="script.js"></script>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Done")
