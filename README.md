# caerjar.github.io

The Caerjar website, served by GitHub Pages at https://caerjar.github.io/.

Static pages, no build, no script. Shared styles in `assets/site.css`; favicon in `assets/favicon.svg`.

| Page | File | Holds |
|---|---|---|
| Home | `index.html` | Mission, the terrain map, the three offerings in brief, contact |
| Offerings | `offerings/index.html` | Advise, Build, Teach: what each includes, what you leave with, the work that shows it; rates note |
| Work | `work/index.html` | The six terrains (Intelligence, Networks, Archives, Tools, Medicine, Stewardship) and the works in each |

## Content

- **Mission**: "We help communities own the tools they depend on." It appears on Home and Offerings.
- **Offerings**: three. Care (herbal and community health) and commissions (installations, performance,
  editions) are not offered for hire on this site; that work stays on the Work page.
- **Works**: every work listed is a real work with a page on eonmeridian.github.io; its one line is
  copied from that work's `work.md` (`sub:`). Add one by copying an `<li>` in the terrain or offering.
- **Rates**: none published yet. Offerings says "Rates on request" plus a sliding-scale line.

House rules from eonmeridian.github.io apply: no em-dashes, no machine-intelligence vocabulary or
vendor names, no real name.

## Preview

    python3 -m http.server 8124 --bind 127.0.0.1    # then open http://localhost:8124/
