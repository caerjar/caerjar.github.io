# Eon Meridian

> Ritual technologies for more livable futures — art, infrastructures and herbal practice at the intersections of memory, networks, value, care and the more-than-human.

Portfolio site for **Eon Meridian**, with the **Caerjar** landing page kept alongside it. Designed to live on GitHub Pages and grow into a place to publish code and writing.

Two visual languages live here: the portfolio is editorial (paper, monospace, serif headings, hairline rules); Caerjar is a Klein-blue blueprint (cream paper, technical coordinate diagram, survey marks).

## Structure

```
caerjar/
├── index.html            # Eon Meridian portfolio — hero, work cards, collaborations, about
├── caerjar.html          # Caerjar landing page (a vessel for care), self-contained
├── projects/<slug>/      # one page per work, 24 of them
│   └── index.html
├── assets/
│   ├── site.css          # shared stylesheet for the index and every work page
│   └── img/              # documentation images and generated plates
├── .nojekyll             # tell GitHub Pages to serve files as-is (no Jekyll processing)
├── .gitignore
└── README.md
```

No framework, no build, no dependencies — plain static HTML served as-is. Edit a file directly and
refresh. `caerjar.html` keeps its own inline CSS; the portfolio pages share `assets/site.css`,
because fifteen copies of one stylesheet is fifteen places to forget.

### Where the content comes from

Every project page is written from that project's own `README.md` / `direction.md` in `~/caerjar` —
status, test counts, invariants, venues and dates included. Nothing on those pages is invented, so
when a project's status changes, update the page from the source rather than from memory.

The nine works with no repository are sourced from elsewhere and cited on their pages:

| Work | Source |
|---|---|
| Evertunes | [opensea.io/evertunes-studio](https://opensea.io/evertunes-studio) — collection text, story titles, traits |
| What the Tech | [visions2030.studio reel](https://www.instagram.com/reel/DTOUu3GExM4/) — Ethical Imagination |
| Peat and Repeat | [peatandrepeat.org](http://peatandrepeat.org/) |
| PGM Diagrams | `diagrammatic-immanence` and `machinic-hymns` in `~/caerjar` |

**Prayer Coin, Unpaid Labor Coin, Emu Butch, Mugworts Free Herbal Clinic and Siliconkin have no
source at all.** Their copy is drafted from the medium and the surrounding work, and should be
replaced with the artist's own account. Do not treat it as a record of what those works are.

### Images

`assets/img/` holds two kinds of file:

- **Real documentation** — plates from `machinic-hymns`, string diagrams from
  `diagrammatic-immanence`, screenshots from `dream`, sample inputs from `SigilStudio`.
- **Generated plates** (`plate-<slug>.svg`) — for works with no documentation image. These are
  marks, not photographs: deterministic diagrams drawn in the site's own visual language, seeded
  from the slug. Two generators make them — `tools/plates.py` in ink only, and
  `tools/colorplates.py`, which gives each work one or two spot colors taken from its own subject
  (brass for the coins, rubric red for the papyri, peat and moss for the edition house). Replace any
  of them with real documentation whenever you have it.
- **Fetched on demand** — `bash tools/fetch-evertunes.sh` pulls four Westward Ho stills from the
  OpenSea CDN. `build.py` uses them automatically once they exist and falls back to the generated
  chapter plate when they don't, so the site is never broken by their absence.

### tools/

The HTML in `projects/` and `index.html` is committed static output and is served directly — there
is no build step in the deploy path. `tools/` holds the two scripts that produced it, so fifteen
pages stay consistent when the template or the content changes:

```bash
python3 tools/plates.py       # ink plates      → assets/img/plate-*.svg
python3 tools/colorplates.py  # color plates    → assets/img/plate-*.svg
bash    tools/fetch-evertunes.sh   # optional: real Westward Ho stills
python3 tools/build.py        # index.html and every projects/<slug>/index.html
```

Project copy lives in the `P` table in `tools/build.py`. Editing a generated page by hand works
until the next `build.py` run overwrites it — put the change in the table instead.

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
Selected Work list in `index.html` (or the Current Vessels panel in
`caerjar.html`). Anything committed to the repo is served by Pages, so code,
write-ups, and demos can all live here.

## Credit

Portfolio layout adapted from an editorial mockup; the Caerjar page from a blue-blueprint mockup. Language and goals are Eon's and Caerjar's.
