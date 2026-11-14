# Djunekz - Personal Engineering Portfolio

A lightweight, multi-page portfolio for [Djunekz](https://github.com/djunekz), focused on independent software development, terminal tooling, automation and reliability-oriented engineering.

## Design direction

- Dark, restrained visual system with a warm red accent.
- Terminal-inspired details without turning the entire interface into a terminal gimmick.
- Content-first project cards with direct repository links.
- Responsive navigation and layouts for desktop, tablet and mobile.
- Reduced-motion support, visible keyboard focus and a skip-to-content link.
- No framework, build dependency, analytics script or third-party runtime JavaScript.

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Introduction, selected work and engineering approach |
| `about.html` | Profile and working domains |
| `projects.html` | Curated open-source projects |
| `stack.html` | Languages, platforms and engineering interests |
| `principles.html` | Seven engineering principles |
| `handles.html` | Canonical identity and associated handles |
| `faq.html` | Frequently asked questions |
| `contact.html` | GitHub and email contact |
| `404.html` | Custom not-found page |

## Build

The generated HTML pages are committed to the repository and can be served directly by GitHub Pages. To regenerate them after editing the content/template in `tools/build.py`:

```bash
python tools/build.py
```

Python 3.8+ is sufficient. There are no external Python packages to install.

## Deployment

1. Extract the repository contents into the root of `djunekz.github.io`.
2. Review the generated pages and verify every project URL and public contact detail.
3. Commit and push to the branch configured for GitHub Pages.
4. After deployment, test the homepage, navigation, all project links, canonical URLs, sitemap and the 404 page on the live domain.

## Content accuracy

Project descriptions are concise summaries of public repository information, not claims of independent certification or performance. Repository READMEs, releases, licenses and issue trackers remain the authoritative sources for current implementation details. No live GitHub metrics or activity counters are hard-coded into the site.

## Maintainer

Djunekz - <https://github.com/djunekz>
