import os,datetime
B='https://djunekz.github.io'
NAV=[('index.html','home'),('about.html','about'),('projects.html','projects'),('stack.html','stack'),('principles.html','principles'),('handles.html','handles'),('faq.html','faq'),('contact.html','contact')]
EMAIL='gab288.gab288@passinbox.com'
TODAY=datetime.date.today().isoformat()
P=[ # name, url, tagline, desc, tags
('AURA','https://github.com/djunekz/aura','Automation & Release Assistant','Memory, not speed. A release assistant that remembers what happened so you do not have to.',['automation','release','CLI']),
('PMCLI','https://github.com/djunekz/pmcli','Project Management CLI','No meetings. Pure signal. Project management that lives where you already work: the terminal.',['CLI','workflow']),
('TDOC','https://github.com/djunekz/tdoc','Documentation as a System','Documentation treated as part of the system, not an afterthought.',['docs','tooling']),
('Termux App Store','https://djunekz.github.io/termux-app-store','CLI / TUI app store for Termux','Interfaces that do not beg. Browse and install Termux packages from a terminal UI.',['TUI','Termux','Android']),
('termux-sync','https://github.com/djunekz/termux-sync','Back up & restore Termux','Back up and restore an entire Termux environment between devices.',['Termux','backup','shell'])]
PR=[('Prefer deletion over addition','Every feature is something to maintain. The best change is often a removed line.'),
('Build for the moment you are not there','Tools should keep working, and keep telling the truth, when nobody is watching.'),
('If it needs constant attention, it is already broken','Automation that demands babysitting has only moved the work somewhere else.'),
('Tools should feel inevitable','The right tool looks obvious in hindsight, with nothing to learn twice.'),
('Interfaces exist to hide complexity, not expose it','A good interface answers the question without making you read the machinery.'),
('Trust is a system property','Trust comes from behavior that is predictable under failure, not from promises.'),
('Complexity is debt with interest','Every shortcut and extra layer is borrowed time, and the bill grows.')]
FAQ=[('Who is Djunekz?','A software developer and tooling architect (GitHub: djunekz) building open-source CLI/TUI tools, automation and release systems, and minimal infrastructure.'),
('Are RedHat, mrxXx, Hmei7 and Anonymous the same person?','Yes. They are handles used by the same developer behind the GitHub account @djunekz.'),
('What has Djunekz built?','AURA, PMCLI, TDOC, Termux App Store and termux-sync. See the projects page.'),
('What languages and platforms does Djunekz use?','Python, Shell, Rust, C/C++ and JavaScript, on Linux, Termux (Android) and GitHub Actions.'),
('Are the tools open source?','Yes. Source code lives on github.com/djunekz, and each project has its own repository.'),
('How can I report a bug or ask a question?','Open an issue on the relevant GitHub repository, or send an email. See the contact page.'),
('Does Djunekz work on hardware or embedded projects?','Yes. Embedded systems and hardware-to-software interfaces are a secondary area of interest.')]
FJ=',\n'.join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'%(q,a) for q,a in FAQ)

def page(fn,title,desc,body,head='',kind='WebPage',path=None):
    url=B+'/'+('' if fn=='index.html' else fn)
    nav=''.join('<a href="%s"%s>%s</a>'%(f,' aria-current="page"' if f==fn else '',n) for f,n in NAV)
    ld='''<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"%s","@id":"%s#page","url":"%s","name":"%s","isPartOf":{"@id":"%s/#website"},"about":{"@id":"%s/#person"}},{"@type":"WebSite","@id":"%s/#website","url":"%s/","name":"Djunekz","publisher":{"@id":"%s/#person"}},{"@type":"Person","@id":"%s/#person","name":"Djunekz","alternateName":["RedHat","mrxXx","Hmei7","Anonymous"],"url":"%s/","image":"%s/assets/icon-512.png","jobTitle":"Tooling Architect & Automation Engineer","sameAs":["https://github.com/djunekz"]}%s]}</script>'''%(kind,url,url,title,B,B,B,B,B,B,B,B,head)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}">
<meta name="author" content="Djunekz"><meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#070405"><meta name="color-scheme" content="dark">
<meta name="google-site-verification" content="L2LF5Ftv92tqqaCWyxE9_-hPjeDS5_4-hMFbNJsKNMc">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png"><link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon-16.png"><link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="website"><meta property="og:site_name" content="Djunekz"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{B}/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{B}/og-image.png">
{ld}
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css"></head>
<body><nav class="bar" aria-label="Main"><div class="wrap in"><a class="brand" href="/"><img src="/assets/logo.png" alt="" width="32" height="32">djunekz</a><div class="links" id="menu">{nav}</div><button class="mbtn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Toggle menu"><span></span><span></span><span></span><b>menu</b></button></div></nav>
<main>{body}</main>
<footer><div class="wrap in"><span>No roadmap. No promises. Only systems that converge. ∎</span><span><a href="https://github.com/djunekz">GitHub</a> · <a href="mailto:{EMAIL}">Email</a> · <a href="/sitemap.xml">Sitemap</a></span></div></footer>
<script src="/assets/app.js" defer></script></body></html>'''
def head(t,d,cmd): return f'<div class="wrap"><div class="page-head"><p class="cmd"><b>$</b> {cmd}</p><h1>{t}</h1><p>{d}</p></div></div>'
def card(p): return f'<article class="card"><h3><a href="{p[1]}">{p[0]}</a></h3><p><b>{p[2]}.</b> {p[3]}</p><div class="tags">'+''.join(f'<span class="tag">{t}</span>' for t in p[4])+'</div></article>'
W=lambda s:f'<div class="wrap">{s}</div>'
out={}
# HOME
out['index.html']=page('index.html','Djunekz — Tooling Architect & Automation Engineer (CLI/TUI) | Portfolio','Djunekz (RedHat, mrxXx, Hmei7, Anonymous) is a software developer building open-source CLI/TUI tools, release automation and minimal infrastructure. Projects: AURA, PMCLI, TDOC, Termux App Store, termux-sync.',
f'''<div class="wrap hero"><p class="cmd"><b>$</b> whoami</p><h1 class="cursor">djunekz</h1>
<p class="lead">Tooling Architect &amp; Automation Engineer</p><p class="cmd">RedHat · mrxXx · Hmei7 · Anonymous</p>
<p>Open-source CLI/TUI tools, release automation and minimal infrastructure, built for the moment you are not there.</p>
<div class="btns"><a class="btn p" href="projects.html">View projects</a><a class="btn" href="https://github.com/djunekz">GitHub profile</a><a class="btn" href="contact.html">Get in touch</a></div>
<div class="term"><div class="tb"><i></i><i></i><i></i><span>djunekz@github.io: ~</span></div><div id="out" aria-live="polite"></div><div class="tin"><b>$</b><input id="cmd" aria-label="Terminal command" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="try: projects"></div></div></div>
<div class="wrap"><section><h2>Projects</h2><div class="grid">{''.join(card(p) for p in P)}</div></section>
<section><h2>Principles</h2><ul class="rules">{''.join(f'<li><div><b>{a}</b><span>{b}</span></div></li>' for a,b in PR[:3])}</ul><p style="margin-top:16px"><a href="principles.html">Read all seven principles</a></p></section></div>''')
# ABOUT
out['about.html']=page('about.html','About Djunekz — Tooling Architect & Automation Engineer','About Djunekz: a software developer focused on CLI/TUI tooling, automation and release systems, failure-oriented design and minimal infrastructure.',
head('About','One idea, repeated: build for the moment you are not there.','cat about.md')+W('''<section class="first"><p><strong>Djunekz</strong> is a software developer who builds open-source command-line (CLI) and terminal UI (TUI) tools, automation and release systems, and minimal infrastructure.</p><p>Tools should keep working, and keep telling the truth, when nobody is watching. That is the test every project is held to.</p>
<dl class="facts"><dt>Focus</dt><dd>CLI/TUI tooling · automation &amp; release · workflow reduction · failure-oriented design</dd><dt>Also works in</dt><dd>embedded systems · hardware ↔ software interfaces · minimal infrastructure</dd><dt>Languages</dt><dd>Python · Shell · Rust · C/C++ · JavaScript</dd><dt>Platforms</dt><dd>Linux · Termux (Android) · GitHub Actions</dd><dt>Handles</dt><dd>RedHat · mrxXx · Hmei7 · Anonymous</dd></dl></section>
<section><h2>How the work is approached</h2><div class="tl"><div><b>Reduce the workflow</b><span>Find the steps a person repeats and remove them.</span></div><div><b>Design for failure first</b><span>Decide what happens when it breaks, then build the happy path.</span></div><div><b>Ship it as a tool</b><span>A small CLI or TUI that does one job and is easy to automate.</span></div><div><b>Release it automatically</b><span>Versioning, packaging and publishing handled by pipelines, not people.</span></div></div></section>
<section><h2>Keep reading</h2><div class="btns"><a class="btn" href="projects.html">Projects</a><a class="btn" href="stack.html">Stack</a><a class="btn" href="principles.html">Principles</a></div></section>'''))
# PROJECTS
out['projects.html']=page('projects.html','Projects — AURA, PMCLI, TDOC, Termux App Store, termux-sync | Djunekz','Open-source projects by Djunekz: AURA, PMCLI, TDOC, Termux App Store and termux-sync.',
head('Projects','Five open-source tools. Each one removes a workflow.','ls projects/')+W(f'<section class="first"><div class="grid">{"".join(card(p) for p in P)}</div></section><section><h2>More on GitHub</h2><p>Everything else, including experiments and older work, is on <a href="https://github.com/djunekz?tab=repositories">github.com/djunekz</a>.</p></section>'),
kind='CollectionPage',
)
# STACK
bars=[('Python',90),('Shell',92),('Rust',65),('C / C++',70),('JavaScript',68)]
out['stack.html']=page('stack.html','Stack — Languages, platforms and tools | Djunekz','The languages, platforms and tools Djunekz uses: Python, Shell, Rust, C/C++, JavaScript, Linux, Termux and GitHub Actions.',
head('Stack','What the tools are built with, and where they run.','cat stack.txt')+W('<section class="first"><h2>Languages</h2><p style="color:var(--mute);font-size:13px">Self-assessed comfort, not a benchmark.</p><div class="bars">'+''.join(f'<div><span>{n}</span><i style="width:{v}%"></i></div>' for n,v in bars)+'</div></section><section><h2>Platforms</h2><div class="grid"><div class="card"><h3>Linux</h3><p>Daily environment and primary target for CLI tools.</p></div><div class="card"><h3>Termux (Android)</h3><p>A full terminal on a phone, and the target of several projects.</p></div><div class="card"><h3>GitHub Actions</h3><p>Release automation, testing and publishing.</p></div></div></section><section><h2>Interests</h2><div class="tags" style="margin:0">'+''.join(f'<span class="tag">{t}</span>' for t in ['CLI','TUI','release automation','workflow automation','embedded systems','hardware interfaces','minimal infrastructure','failure-oriented design'])+'</div></section>'))
# PRINCIPLES
out['principles.html']=page('principles.html','Principles — How Djunekz designs tools','Seven principles behind Djunekz tools: prefer deletion, build for absence, design for failure, and keep complexity low.',
head('Principles','Seven rules that decide what gets built, and what gets deleted.','cat principles.txt')+W('<section class="first"><ul class="rules">'+''.join(f'<li><div><b>{a}</b><span>{b}</span></div></li>' for a,b in PR)+'</ul></section>'))
# HANDLES
out['handles.html']=page('handles.html','Handles — RedHat, mrxXx, Hmei7, Anonymous | Djunekz','RedHat, mrxXx, Hmei7 and Anonymous are handles used by the same developer, Djunekz (GitHub: djunekz).',
head('Handles','One developer, several names.','id djunekz')+W('<section class="first"><p>If you found one of these names elsewhere, it points here.</p><dl class="facts"><dt>djunekz</dt><dd>Main handle and GitHub account (@djunekz)</dd><dt>RedHat</dt><dd>Alias of Djunekz</dd><dt>mrxXx</dt><dd>Alias of Djunekz</dd><dt>Hmei7</dt><dd>Alias of Djunekz</dd><dt>Anonymous</dt><dd>Alias of Djunekz</dd></dl></section><section><h2>Verify</h2><p>The official source is <a href="https://github.com/djunekz">github.com/djunekz</a>. Email or links that do not match it are not from Djunekz.</p></section>'))
# FAQ
out['faq.html']=page('faq.html','FAQ — Questions about Djunekz','Frequently asked questions about Djunekz, the projects, handles, languages and how to get in touch.',
head('FAQ','Short answers to common questions.','man djunekz')+W('<section class="first">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)+'</section>'),
head=',{"@type":"FAQPage","mainEntity":['+FJ+']}',kind='FAQPage')
# CONTACT
out['contact.html']=page('contact.html','Contact Djunekz','Contact Djunekz by email or through GitHub issues.',
head('Contact','The fastest way is a GitHub issue or an email.','contact --open')+W(f'<section class="first"><dl class="facts"><dt>GitHub</dt><dd><a href="https://github.com/djunekz">github.com/djunekz</a></dd><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></dl></section><section><h2>Before you write</h2><p>For bugs, open an issue in the project repository so others can find the answer. For anything else, email works.</p></section>'),kind='ContactPage')
# 404
out['404.html']=page('404.html','404 — Page not found | Djunekz','Page not found.',
head('404','No such file or directory.','cd '+'/missing')+W('<section class="first"><p>That page does not exist or was moved.</p><div class="btns"><a class="btn p" href="/">Go home</a><a class="btn" href="/projects.html">Projects</a></div></section>'))
for f,h in out.items(): open(f,'w').write(h)
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{B}/{"" if f=="index.html" else f}</loc><lastmod>{TODAY}</lastmod><priority>{1.0 if f=="index.html" else 0.7}</priority></url>\n' for f,_ in NAV)+'</urlset>\n')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {B}/sitemap.xml\n')
open('site.webmanifest','w').write('{"name":"Djunekz","short_name":"djunekz","description":"Tooling Architect & Automation Engineer","start_url":"/","display":"standalone","background_color":"#070405","theme_color":"#070405","icons":[{"src":"/assets/icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"/assets/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"}]}')
open('humans.txt','w').write('/* TEAM */\nDeveloper: Djunekz (RedHat, mrxXx, Hmei7, Anonymous)\nGitHub: https://github.com/djunekz\n')
open('.nojekyll','w').write('')
