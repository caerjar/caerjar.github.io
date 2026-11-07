# caerjar.github.io

The Caerjar website, served by GitHub Pages at https://caerjar.github.io/.

Static pages, no build, no script. Shared styles in `assets/site.css`; favicon in `assets/favicon.svg`.

| Page | File | Holds |
|---|---|---|
| Home | `index.html` | Mission, what we do (Advise, Build, Teach) in brief, selected work, contact form |
| What we do | `offerings/index.html` | Each offering: what it can include, what you leave with, the work that shows it; rates |
| Work | `work/index.html` | Five areas (Intelligence, Networks, Archives, Tools, Stewardship) and the works in each |

Style: the "Notebook" direction, after Ink & Switch (inkandswitch.com): Newsreader serif, IBM Plex Sans
labels, one reading column, a drawn line glyph per offering.

The contact form posts to `mailto:hi@caerjar.com` (opens the visitor's mail app). To receive
submissions directly, point its `action` at a form service such as Formspree.

## Content

- **Mission** (Eon's words): "Caerjar exists to build technology that expands human and collective autonomy." Followed by "We help our clients own the tools they depend on." Both appear on Home and What we do.
- **Offerings**: three. Care (herbal and community health) and commissions (installations, performance,
  editions) are not offered for hire on this site; that work stays on the Work page.
- **Works**: every work listed is a real work with a page on eonmeridian.github.io; its one line is
  copied from that work's `work.md` (`sub:`). Add one by copying an `<li>` in the terrain or offering.
- **Rates**: none published yet. What we do says "Rates on request" plus a sliding-scale line.

House rules from eonmeridian.github.io apply: no em-dashes, no machine-intelligence vocabulary or
vendor names, no real name. Exception (Eon, 2026-11-05): this site names "AI agent workflows" as an area of work.

## Preview

    python3 -m http.server 8124 --bind 127.0.0.1    # then open http://localhost:8124/
