#!/usr/bin/env python3
"""Build Caerjar's own work pages at work/<slug>/ from works/<slug>.md.

Caerjar owns these works: their text and images live in this repo, and they do not
appear on eonmeridian.github.io. Text is used as written; nothing is added.

Run: python3 tools/build.py
"""
import html
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VAULT = ROOT.parent.parent                       # ~/caerjar/vault
PORTFOLIO = VAULT / "code" / "eonmeridian.github.io"
sys.path.insert(0, str(ROOT / "tools"))
import md

# The works on Caerjar, in the order the Work page lists them.
WORKS = [
    "daimon-agent", "local-models", "research-manager", "vetiver",
    "caer-stack",
    "meridian", "corpusmith",
    "specsmith", "earshot", "training", "fieldkit", "epub-to-pdf", "screenplay-formatter", "drone-cinematographer",
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} · Caerjar</title>
<meta name="description" content="{desc}" />
<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300..600&family=IBM+Plex+Sans:wght@500;600&display=swap" />
<link rel="stylesheet" href="../../assets/site.css" />
</head>
<body>
<div class="wrap">
<header>
  <a class="logo" href="../../"><svg width="22" height="22" viewBox="0 0 22 22" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="9"/><circle cx="11" cy="11" r="3" fill="currentColor"/></svg>Caerjar</a>
  <nav aria-label="Pages"><a href="../../offerings/">What we do</a><a href="../../#selected-work">Selected work</a><a href="../../#write">Get in touch</a></nav>
</header>
"""

FOOT = """
<footer><a href="../../">Caerjar</a><a href="mailto:hi@caerjar.com">hi@caerjar.com</a></footer>
</div>
</body>
</html>
"""


def source(slug):
    """Each work's copy lives here, in works/<slug>.md. Caerjar owns its works."""
    own = ROOT / "works" / f"{slug}.md"
    if not own.exists():
        sys.exit(f"{slug}: no works/{slug}.md")
    return own, ROOT


def image(slug, src, base):
    """Copy one image into assets/img/ and return its path from a work page."""
    f = base / src
    if f.parent == ROOT / "assets" / "img":
        return f"../../assets/img/{f.name}"
    dest = ROOT / "assets" / "img" / f"{slug}-{f.name}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(f, dest)
    return f"../../assets/img/{dest.name}"


def build(slug):
    path, base = source(slug)
    head, body = md.split(path.read_text())
    head["title"] = head["title"][0].upper() + head["title"][1:]  # project names are capitalized on this site
    lead, prose = md.page_parts(body)
    esc = lambda s: html.escape(s, quote=True)

    imgs = [(i["src"], i["caption"]) for i in head.get("images", [])]
    imgs += [(i["src"], i["caption"]) for i in head.get("optional_images", [])
             if (base / i["src"]).exists()]
    own = ROOT / "assets" / "plates" / f"{slug}.svg"  # a plate drawn for this site replaces any other
    if own.exists():
        imgs = [(str(own), imgs[0][1] if imgs else head.get("sub", head["title"]))]
    figs = "\n".join(
        f'  <figure><img src="{image(slug, s, base)}" alt="{esc(c)}" loading="lazy" />'
        f"<figcaption>{c}</figcaption></figure>" for s, c in imgs)

    facts = [("Year", head["year"])] if head.get("year") else []
    facts += [("Medium", head["medium"])] if head.get("medium") else []
    facts += [(s["label"], s["value"]) for s in head.get("side", [])]
    dl = "\n".join(f"    <dt>{k}</dt><dd>{v}</dd>" for k, v in facts)

    links = "\n".join(
        f'    <li><a href="{l["url"]}">{l["label"]}</a></li>' if l.get("url")
        else f'    <li><span>{l["label"]}</span></li>' for l in head.get("links", []))

    blurb = head.get("blurb") or re.split(r"(?<=[.!?])\s", re.sub(r"<[^>]+>", "", lead), maxsplit=1)[0]
    page = HEAD.format(title=esc(head["title"]), desc=esc(blurb)) + f"""
<main class="work">
<div class="col">
  <h1>{head['title']}</h1>
  <p class="lede">{head.get('sub', '')}</p>
</div>

<p class="col">{lead}</p>

{f'<div class="figs">{chr(10)}{figs}{chr(10)}</div>' if figs else ''}

<div class="work-body">
  <div class="prose col">
{prose}
  </div>
  <dl class="facts">
{dl}
  </dl>
</div>

{f'<ul class="work-links">{chr(10)}{links}{chr(10)}</ul>' if links else ''}

</main>
""" + FOOT
    out = ROOT / "work" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    return out, page


def private_terms():
    f = PORTFOLIO / "tools" / ".houserules-private"
    return [t.strip() for t in f.read_text().splitlines() if t.strip() and not t.startswith("#")] if f.exists() else []


if __name__ == "__main__":
    terms = private_terms()
    problems = []
    for slug in WORKS:
        out, text = build(slug)
        visible = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        if chr(0x2014) in visible:
            problems.append(f"{out.relative_to(ROOT)}: em-dash")
        for t in terms:
            if re.search(rf"\b{re.escape(t)}\b", visible, re.I):
                problems.append(f"{out.relative_to(ROOT)}: private term '{t}'")
        print("wrote", out.relative_to(ROOT))
    if problems:
        sys.exit("house rules:\n  " + "\n  ".join(problems))
