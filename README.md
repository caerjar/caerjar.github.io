# Caerjar

> A Vessel for Care — a workshop for archives, medicines, local intelligence, resilient networks, and the shared practices that sustain collective life.

Static landing site for **Caerjar**, designed to live on GitHub Pages and grow into a place to publish code and writing. The visual language is a Klein-blue blueprint (cream paper, technical coordinate diagram, survey marks); the content is Caerjar's terrain of care.

## Structure

```
caerjar/
├── index.html     # the whole site — single self-contained file, no build step
├── .nojekyll      # tell GitHub Pages to serve files as-is (no Jekyll processing)
├── .gitignore
└── README.md
```

It is a single hand-written HTML file with inline CSS — no framework, no build, no dependencies. Edit `index.html` directly and refresh.

## Preview locally

Just open the file:

```bash
open index.html
```

Or serve it (handy when you start adding subpages):

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

## Publish on GitHub Pages

1. Create the repo and push:
   ```bash
   gh repo create caerjar --public --source=. --remote=origin --push
   ```
   (or create the repo on github.com and `git remote add origin …` + `git push -u origin main`)

2. Enable Pages: **Settings → Pages → Source: Deploy from a branch → `main` / `(root)`**.

3. Your site goes live at `https://<user>.github.io/caerjar/`.
   For a custom domain (`caerjar.org`), add a `CNAME` file with the domain and configure DNS, then set it under Settings → Pages.

## Publishing code alongside the site

Drop projects in subfolders (e.g. `projects/<name>/`) and link them from the
Current Vessels panel in `index.html`. Anything committed to the repo is served
by Pages, so code, write-ups, and demos can all live here.

## Credit

Layout adapted from a blue-blueprint mockup; language and goals are Caerjar's.
