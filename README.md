# caerjar.github.io

The Caerjar landing page, served by GitHub Pages at https://caerjar.github.io/.

One self-contained page: `index.html` (inline CSS, no build, no script) and `assets/favicon.svg`.

## Content

- **Terrain**: the six areas (Intelligence, Networks, Archives, Tools, Medicine, Stewardship).
  The hexagon map links to each. Every work listed under a terrain is a real work with a page on
  eonmeridian.github.io; its one line is copied from that work's `work.md` (`sub:`). Add one by
  copying an `<li>` in the terrain.

House rules from eonmeridian.github.io apply: no em-dashes, no machine-intelligence vocabulary or
vendor names, no real name.

## Preview

    python3 -m http.server 8124 --bind 127.0.0.1    # then open http://localhost:8124/
