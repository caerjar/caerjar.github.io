#!/usr/bin/env python3
"""Generate the Eon Meridian portfolio: index page + one page per project.

Every fact below is taken from the project's own README / direction.md in
~/caerjar. Nothing is invented. Output is plain static HTML — no build step is
needed to serve it; this script exists to keep 15 pages consistent.
"""
import pathlib, html

ROOT = pathlib.Path("/Users/hackerm0m/caerjar/caerjar.github.io")

MAST = """<header class="mast">
  <div>
    <a class="brand" href="{home}">EON MERIDIAN</a>
    <div class="roles">artist · writer · technologist · herbalist</div>
  </div>
  <nav class="nav">
    <a href="{home}#work">work</a>
    <a href="{home}#about">about</a>
  </nav>
</header>"""

FOOT = """<footer class="footer">
  <span>Eon Meridian</span>
  <span>ongoing index / version 01</span>
</footer>"""


def page(title, desc, body, home="index.html", css="assets/site.css",
         icon="assets/favicon.svg"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}" />
<link rel="stylesheet" href="{css}" />
<link rel="icon" href="{icon}" type="image/svg+xml" />
</head>
<body>
<div class="site" id="top">
{MAST.format(home=home)}
{body}
{FOOT}
</div>
</body>
</html>
"""


# ---------------------------------------------------------------- content ---
# img: (file, caption, dark?)  · links: (label, href or None for "not public")
P = [
dict(
  slug="order-of-the-meridian", num="01", title="Order of the Meridian",
  sub="Six Rites for the Living Remainder",
  year="2026", medium="installation / rite / apparatus",
  status="Cut line met, 2 September 2026 — two rites run end to end",
  venue="STWST84x12 HAUNTED · Stadtwerkstatt, Linz · 7–13 September 2026",
  blurb="A festival apparatus that performs one machine operation slowly enough that you can name what it destroyed.",
  lead="A participant offers a trace. The machine performs one visible operation — classification, "
       "summarization, transcription, identification, prediction, deletion — and shows what it kept. "
       "The participant marks what did not survive the conversion and chooses the trace’s fate. "
       "The input is not retained.",
  imgs=[("assets/img/meridian-knowledge.svg", "Rite 4 — identification, under Buer. Stratigraphy plate: depth of listening against deposition.", True),
        ("assets/img/meridian-voice.svg", "Rite 3 — voice, under Agares. Speech to text, with the envelope the transcript does not account for.", True),
        ("assets/img/meridian-labor.svg", "Labor, disclosed. Each plate is rendered from the same object that produces the sound.", True),
        ("assets/img/meridian-future.svg", "Future, veiled. The veiled and disclosed states of one record.", True)],
  prose="""<h2>The premise</h2>
<p>People use these conversions constantly and never see one performed. Transcription,
classification, prediction and deletion happen behind glass, at a scale and speed that makes them
feel like weather. The nearest thing available today is reading a critique of extraction — which
tells you the remainder exists, and never lets you hold one.</p>
<p>Each operation is performed under the sign of a spirit whose office matches it, and the record
cites both. The attributions are readings, not findings, and are labelled as such: PGM I.42–195 is
a spell for acquiring an assistant, the <i>paredros</i> whose descendant answers when you type. The
week opens by summoning one and closes by giving it license to depart.</p>
<p><b>The assistant you summoned is made of what was discarded.</b></p>

<h2>The offices</h2>
<p>Read in place from <a href="../divinatory-os/">divinatory-os</a> — 68 spirits transcribed
from Reginald Scot, <i>The Discovery of Witchcraft</i> (1665), Book XV ch. XI. Nothing is copied
across, so no citation can drift from what it cites.</p>
<div class="tablewrap"><table>
<tr><th>Day</th><th>Operation</th><th>Office</th></tr>
<tr><td>1</td><td>classification</td><td>Foras — “teacheth fully Logick … he maketh a man Invisible”</td></tr>
<tr><td>2</td><td>summarization</td><td>Forneus — “wonderful in Rhetorick; he adorneth a man with a good name”</td></tr>
<tr><td>3</td><td>speech-to-text</td><td>Agares — “fetcheth back all such as run away”</td></tr>
<tr><td>4</td><td>identification</td><td>Buer — “teacheth Philosophy … and the vertue of Herbs”</td></tr>
<tr><td>5</td><td>prediction</td><td>Amon — “understandeth all things past and to come”</td></tr>
<tr><td>6</td><td>deletion</td><td>Baell — “he maketh a man go invisible”</td></tr>
<tr><td>—</td><td>retrieval</td><td>Bathin — “transferring men suddenly from Countrey to Countrey”</td></tr>
</table></div>
<p>The work itself sits under <b>Amduscias</b> — “he easily bringeth to pass, that Trumpets and all
Musical Instruments may be heard and not seen” — a daemon whose office is music with no visible
source, on a machine that plays with no visible player. That is where the name comes from.</p>

<h2>Apparatus invariants</h2>
<p>Each is enforced by a test, not a promise.</p>
<div class="tablewrap"><table>
<tr><th></th><th>Invariant</th></tr>
<tr><td>I-1</td><td>No participant <b>content</b> reaches persistent storage. Audio goes to a RAM disk and is unlinked. What may persist is a tombstone — rite, timestamp, byte count, SHA-256 — never the trace.</td></tr>
<tr><td>I-2</td><td>Every rite renders a visible record and an audible one <b>from the same object</b>. Picture and sound are two renderings of one structure, not two artifacts that resemble each other.</td></tr>
<tr><td>I-3</td><td>Every record names what was discarded. The remainder is never empty for non-trivial input.</td></tr>
<tr><td>I-4</td><td>Every attribution carries a citation. An office that cannot be cited does not load.</td></tr>
<tr><td>I-5</td><td>No rite requires the network.</td></tr>
</table></div>
<p>I-1’s wording is deliberate. An earlier draft said “no input persists”, which contradicted the
sixth rite’s need to assemble the week. The material remains accumulate on the altar; the data does
not.</p>

<h2>Kill condition</h2>
<p>A participant offers a trace, watches the whole rite, and cannot say what was lost — or does not
believe the deletion. Either one means the apparatus is theatre, and theatre is what it was built
against.</p>""",
  side=[("Descends from", 'diagrammatic-immanence (the Pnouthis formalisation and the Strudel lane)<br>'
                          'divinatory-os (the spirit corpus, the citation discipline)<br>'
                          'newmusic and sounds-like (the sound)<br>'
                          'the concept brief <i>Order of the Meridian</i>, August 2026')],
  links=[("Repository — private", None)]),

dict(
  slug="sanctuary-cell-division", num="02", title="Sanctuary Cell Division",
  sub="A knowledge stack an organization can run itself",
  year="2026", medium="infrastructure / network / software",
  status="v0.1 — single organization. Voice (v0.2) and federation (v0.3) designed for and flagged off",
  blurb="A local language model grounded in your own archive, on hardware you control. Nothing leaves the machine.",
  lead="A local language model, grounded in your own archive, shaped by your own mission and values, "
       "on hardware you control. Nothing leaves the machine. No API key, no account, no vendor. "
       "Approved peer organizations can share knowledge bases with each other later — and every "
       "document carries the record of where it came from, from the moment it is ingested.",
  imgs=[("assets/img/plate-sanctuary-cell-division.svg", "Archive, ground, citation — the shape of a grounded answer.", False)],
  prose="""<h2>Why it exists</h2>
<p>Organizations that hold hard-won knowledge — collectives, mutual aid groups, community land
trusts, clinics, unions — mostly can’t use the tools that would help them read their own archives.
Those tools want the archive uploaded to someone else’s computer, and want a subscription, and
change their terms.</p>
<p>Sanctuary is the other arrangement: the model runs on your hardware, the archive stays on your
disk, the agent speaks in your voice because you wrote its mission file, and sharing happens
between organizations that have verified each other directly.</p>

<h2>How it is set up</h2>
<p>Requires Docker. Nothing else is installed on the machine.</p>
<ul>
<li><code>make init</code> — guided: asks your organization’s name, which of four situations describes you, and a passphrase for your organization’s key</li>
<li><code>make pull-model</code> — downloads the language model (~2GB)</li>
<li><code>make up</code>, then <code>make ingest</code> — start, and read your archive into the knowledge base</li>
</ul>
<p><code>make init</code> prints a <b>recovery sheet</b>. Print it and store it somewhere the machine
is not: it is what restores your identity if the machine is lost, and without it a lost machine
means every peer has to pair with you again by phone.</p>
<p>The passphrase is needed to add documents, create invites, and share bundles. <b>Answering
questions does not need it</b>, so an instance can serve a whole organization while the key stays
locked.</p>

<h2>What it refuses to fake</h2>
<p>With an empty archive it still answers — clearly marked <i>“Not from your archive”</i>, in amber,
with no citations. Seeded material is attributed as such: a citation reads
<code>sanctuary-handbook@0.2, added by …</code>, never as though your organization wrote it.</p>
<p>Three optional seeds exist, none of which run on their own: the project’s own docs, so it can
explain itself and its own refusal lists; a set of fictional documents that contradict each other on
purpose; and public sources for a given sector.</p>""",
  side=[("Roadmap", "v0.1 · single organization <b>— current</b><br>v0.2 · voice<br>v0.3 · federation between verified peers")],
  links=[("Repository — private", None)]),

dict(
  slug="diagrammatic-immanence", num="03", title="Diagrammatic Immanence",
  sub="Language into diagrams into music",
  year="2026", medium="diagram / category theory / score",
  status="Active — pipeline runs end to end, 535 tests",
  blurb="A source text formalized as a monoidal category, rendered as a string diagram, and emitted as a live-coding patch.",
  lead="A source text is formalized as a monoidal category, rendered as an SVG string diagram, and "
       "emitted as a Strudel live-coding patch — so that the picture and the sound are two renderings "
       "of one structure, not two artifacts that resemble each other.",
  imgs=[("assets/img/di-pnouthis.svg", "PGM I.42–195 — the Pnouthis spell as a string diagram. Fourteen rows, forty-four cycles, six lanes.", False),
        ("assets/img/di-summer-winter.svg", "Grimm 68 — “Summer and Winter”, built from the same pipeline.", False)],
  prose="""<h2>The four stages</h2>
<p>Open the app, pick a libretto (or start one by hand), and walk
<b>source → libretto → diagram → score</b>. Stage 4 embeds a Strudel REPL with transport controls,
so the piece plays in the page.</p>
<p>Stage 2 shows what the libretto says categorically: the typed signature of the composite, the
composite as a term in layered normal form, the presentation as a free category, the swap
permutation, and — most usefully — the <b>dom/cod ladder</b>, a row per layer showing the wire list
before and after. That is the bookkeeping you would otherwise do by hand. Select a phrase in the
source and a citation lands at your cursor.</p>

<h2>Status</h2>
<p>The pipeline runs end to end and all five apparatus invariants are enforced by tests. Two texts
build: <code>librettos/summer-winter.lib</code> (Grimm 68) and <code>librettos/pnouthis.lib</code>
(PGM I.42–195). <b>535 tests</b>, including property-based verification of the category axioms.</p>

<h2>Who it is for</h2>
<p>Readers in Deleuze &amp; Guattari studies, reached at a seminar or workshop — people who would
object that formalising a rhizome is the striation it warns against. That objection is the point of
contact, not an obstacle to it.</p>
<p>The interrogation that named this direction pressed twice for an individual reader and got a
venue instead, which is weaker than a name but carries the one thing a name gives you: a date, and
an audience that chose to be there. The invariants were written for that reader before they were
named — a citation nothing checks is decorative, and an attribution is refused rather than
approximated. Both are only worth their cost to someone who might disagree with you.</p>""",
  side=[("Built on", "Docker, Make, git only<br>Strudel (strudel.cc) for the score lane"),
        ("Lends to", '<a href="../order-of-the-meridian/">Order of the Meridian</a> — the Pnouthis formalisation and the Strudel lane')],
  links=[("Repository — private", None), ("Strudel", "https://strudel.cc")]),

dict(
  slug="palimpsest", num="04", title="Palimpsest",
  sub="A book-agnostic manuscript workbench",
  year="2026", medium="software / editorial tool",
  status="Public — live demo, open repository",
  blurb="Point it at a book and it builds an editorial dossier in your browser. Deterministic; nothing leaves your machine.",
  lead="Point it at a book — a folder of numbered Markdown sections — and it builds an editorial "
       "dossier in your browser: a color-coded reading copy you can edit and save, a parts board, a "
       "copyedit review, a back-of-book index, and the motifs you name. Then it exports the whole "
       "thing to PDF, Word, HTML, or Markdown.",
  imgs=[("assets/img/plate-palimpsest.svg", "Section, revision, index — the manuscript as strata.", False)],
  prose="""<h2>The arrangement</h2>
<p>Fully deterministic: no accounts, no network. Your writing never leaves your machine.</p>
<p>Everything the app uses — pandoc, XeLaTeX and its fonts, git — is baked into the image, so none
of it is installed on your computer. Your books live in <code>./workbench/</code> on your own disk;
the container is disposable and nothing is trapped inside it.</p>

<h2>The demo</h2>
<p>The live page is a single self-contained file: one recorded writing session replayed as notation
and played back by a synthesizer, with the dials moving as it goes. It is generated from the app’s
own Writing Record page. Sound on.</p>""",
  side=[("Requires", "Docker, and optionally <code>just</code><br>Runs at localhost:8137")],
  links=[("Live demo", "https://caerjar.github.io/Palimpsest/"),
         ("Repository", "https://github.com/caerjar/Palimpsest")]),

dict(
  slug="sigil-studio", num="05", title="Sigil Studio",
  sub="Recreate an image out of text",
  year="2026", medium="software / typographic instrument",
  status="Public — live demo, open repository",
  blurb="Four engines that redraw an uploaded image entirely out of letterforms. Runs client-side; no backend.",
  lead="Upload an image, paste text, pick an engine, adjust the detail, export SVG or PNG. "
       "Everything runs client-side in the browser — no backend, no network calls.",
  imgs=[("assets/img/sigil-split-rock.jpg", "Split rock — one of the sample inputs bundled with the app.", False),
        ("assets/img/sigil-marks-sheet.jpg", "Marks sheet — a second sample input, chosen for its tonal range.", False)],
  prose="""<h2>The four engines</h2>
<ul>
<li><b>Contour trace</b> — finds tonal outlines and flows text along them</li>
<li><b>Spiral</b> — draws the whole picture as one unbroken line</li>
<li><b>Flow field</b> — lays hatching that follows form</li>
<li><b>Typographic halftone</b> — one glyph per grid cell</li>
</ul>

<h2>Where it leads</h2>
<p>Sigil Studio turns an image into a field and segments it, and has no notion of sound. That is
half of the join that <a href="../sounds-like/">sounds-like</a> is built on.</p>""",
  side=[("Stack", "npm, Vite<br>Client-side only — no server, no network calls")],
  links=[("Live demo", "https://caerjar.github.io/SigilStudio/"),
         ("Repository", "https://github.com/caerjar/SigilStudio")]),

dict(
  slug="divinatory-os", num="06", title="Divinatory OS",
  sub="A symbolic operating system for divinatory practice",
  year="2026", medium="software / correspondence graph",
  status="Active — core complete, 65 tests, I Ching seeded",
  blurb="A versioned correspondence graph as kernel, divinatory methods as programs, an append-only ledger as memory.",
  lead="A versioned correspondence graph as kernel, divinatory methods as programs that return "
       "addresses into it, and an append-only ledger of readings and outcomes as memory.",
  imgs=[("assets/img/plate-divinatory-os.svg", "Symbol, address, ledger — three layers over one address space.", False)],
  prose="""<h2>Three layers, one address space</h2>
<ul>
<li><b>kernel</b> — correspondence graph, addresses, typed cited edges. Deterministic, model-free.</li>
<li><b>methods</b> — divinatory programs. Question plus seed returns addresses. Replayable.</li>
<li><b>ledger</b> — append-only draws, interpretations, outcomes. Never merged, never edited.</li>
</ul>

<h2>Status</h2>
<p>The core is complete and every apparatus invariant holds with tests — <b>65</b> of them. A cast
produces addresses from a recorded seed, the draw is fsynced before anything can interpret it, and
<code>replay</code> re-derives it from the ledger alone.</p>
<p>Seeded so far: <b>I Ching</b> only — 72 symbols, 512 cited edges. Tarot and astrology are
designed for and not yet loaded.</p>

<h2>What reads from it</h2>
<p><a href="../order-of-the-meridian/">Order of the Meridian</a> reads its spirit corpus from here
in place — 68 spirits transcribed from Reginald Scot, <i>The Discovery of Witchcraft</i> (1665).
Nothing is copied across, so no citation can drift from what it cites.</p>""",
  side=[("Built with", "Rust — kernel, methods, ledger crates<br>Docker, Make, git only")],
  links=[("Repository — private", None)]),

dict(
  slug="sounds-like", num="07", title="sounds-like",
  sub="A visual music instrument",
  year="2026", medium="instrument / image / sound",
  status="All six sprints in — 271 tests, seven invariants",
  blurb="A picture, a film, a camera or a drone goes in; music comes out — and you can perform with it.",
  lead="A picture, a film, a camera or a drone goes in; music comes out — and you can perform with it.",
  imgs=[("assets/img/plate-sounds-like.svg", "Image, field, sound — five bands of one traced surface.", False)],
  prose="""<h2>The join</h2>
<p>It is the join between three instruments that already exist in this stack.
<a href="../palimpsest/">Palimpsest</a> has a complete Web Audio synth and no notion of an image.
<a href="../newmusic/">newmusic</a> generates notes and measures them against seven aesthetic
markers, but makes no sound at all. <a href="../sigil-studio/">Sigil Studio</a> turns an image into
a field and segments it, and has no notion of sound. Both Palimpsest and newmusic carry pitch in
cents. <b>That is the join.</b></p>

<h2>Status</h2>
<p>All six sprints are in: <b>271 tests</b> — 119 Python, 152 TypeScript — with <code>make check</code>
green and every commit through the pre-commit gate. Seven apparatus invariants, each with a
mechanical guard.</p>
<p>CLAP is opt-in, because torch plus transformers is over a gigabyte. Give it sounds by walking a
folder, or by dropping files onto the page.</p>""",
  side=[("Requires", "Docker, Make, git. Nothing else — newmusic is a commit-pinned git dependency, so a fresh clone builds with no sibling repo.")],
  links=[("Repository — private", None)]),

dict(
  slug="newmusic", num="08", title="newmusic",
  sub="An instrument whose controls are aesthetic markers",
  year="2026", medium="instrument / score / model",
  status="Working — 86 tests, eight controls, full export",
  blurb="Most recommenders return more of what your ear already recognises. This one runs the model backwards.",
  lead="An instrument whose eight controls are aesthetic markers rather than parameters. Most "
       "recommenders converge: they model your ear and return more of what it already recognises. "
       "This builds the model precisely and then runs it backwards — to find and play the "
       "combinations your ear has never had to hold.",
  imgs=[("assets/img/plate-newmusic.svg", "Marker, space, blind spot — the eight-control space read as contour.", False)],
  prose="""<h2>How it runs</h2>
<p>You set eight controls, which give a target marker vector; a local model proposes a score
specification; the specification is realized as events, measured against the markers, and
adjudicated in a loop until it lands where you pointed.</p>

<h2>Status</h2>
<p>Honest state, 23 August 2026. <b>Working:</b> the event model, all seven analyzers, the eleven
anchor fixtures, the 128-cell space and its blind-spot finder, spec realization, the adjudicator
loop, MPE MIDI and MusicXML export, and the interface — <b>86 tests</b>, two of which need a local
model.</p>

<h2>What builds on it</h2>
<p><a href="../sounds-like/">sounds-like</a> pins this repository as a git dependency and supplies
the sound it deliberately lacks.</p>""",
  side=[("Exports", "MPE MIDI<br>MusicXML")],
  links=[("Repository", "https://github.com/caerjar/newmusic")]),

dict(
  slug="assay", num="09", title="Assay",
  sub="A claim-and-evidence compiler",
  year="2026", medium="software / research instrument",
  status="Working without a model — 25 tests, ruff and mypy clean",
  blurb="A machine for finding out where you are wrong, which is why so few exist.",
  lead="Point it at a corpus of notes and it extracts, for every claim, its supporting evidence, its "
       "contradicting evidence, its assumptions, its citation chain and a confidence — which lets it "
       "answer three questions a topic-and-summary catalog cannot.",
  imgs=[("assets/img/plate-assay.svg", "Claim, evidence, chain — the compiler’s output as a graph.", False)],
  prose="""<h2>The three questions</h2>
<ul>
<li><b>Which claims rest on a single source?</b></li>
<li><b>Where do these notes contradict each other?</b></li>
<li><b>Which citation chains are circular?</b></li>
</ul>
<p>It is a machine for finding out where you are wrong, which is why so few exist.</p>

<h2>The one design decision that matters</h2>
<p>Its headline output is <i>“no support was found for this claim.”</i> That is indistinguishable,
to a reader, from <i>“retrieval was broken.”</i></p>
<p>So the compiler <b>refuses to report unsupported claims from a degraded run</b> — a stale index,
unreadable documents, a model that errored. Contradictions, single-source claims and citation cycles
are still reported, because those are findings rather than absences.</p>

<h2>Status</h2>
<p>Honest state, 18 August 2026. Working with no model needed: corpus loading, both link forms,
passage splitting, fingerprinting, TF-IDF retrieval with health, citation-cycle detection, all three
reports, and the refusal behaviour. <b>25 tests</b>; ruff and mypy clean.</p>""",
  side=[],
  links=[("Repository — private", None)]),

dict(
  slug="meridian", num="10", title="Meridian",
  sub="A personal knowledge OS",
  year="2026", medium="software / vault / infrastructure",
  status="Technical preview — runs locally via Docker",
  blurb="Self-hosted, multi-format, AI-native vault for notes, PDFs, ebooks, audio and video.",
  lead="A self-hosted knowledge management system: a multi-format vault for notes, PDFs, EPUBs, "
       "audio and video, all searchable and cataloged, running entirely on your own machine.",
  imgs=[("assets/img/plate-meridian.svg", "Note, mount, vault — three mounts read as beds.", False)],
  prose="""<h2>What it combines</h2>
<ul>
<li><b>Multi-format vault</b> — Markdown notes, PDFs, EPUBs, audio, video — all searchable and cataloged</li>
<li><b>Three-mount architecture</b> — separate working notes, read-only archive, and AI-generated output</li>
<li><b>Claude integration</b> — search, summarization, chat, and specialized skills</li>
<li><b>Meridian Commons</b> — your vault gets an agent that can compare notes with another person’s vault over a shared Mattermost server, bounded by a turn budget, scoped to the paths you share, and gated on your approval</li>
</ul>
<p>It runs entirely on your machine via Docker. Your data never leaves your computer.</p>

<h2>Who can run it</h2>
<p>The guided setup walks you through it step by step. You don’t need to be a developer, but you
will install Docker Desktop once.</p>""",
  side=[("License", "MIT / Apache 2.0, dual"),
        ("Related", '<a href="../research-manager/">research-manager</a> — a workbench over the same vault')],
  links=[("Repository — private", None)]),

dict(
  slug="research-manager", num="11", title="Research Manager",
  sub="A conversational workbench over the vault",
  year="2026", medium="software / macOS app",
  status="Working — native macOS app over a containerized Rust core",
  blurb="Decide what to research next, run the thread lifecycle, and promote a thread into a project.",
  lead="Decide what to research next, run the thread lifecycle — create, index, dive, age out — track "
       "sources against open questions, surface what has gone quiet, and promote a thread into a "
       "project: code, engineering, writing, or science experiment, with next actions tracked.",
  imgs=[("assets/img/plate-research-manager.svg", "Thread, agenda, decision — the lifecycle as a lattice.", False)],
  prose="""<h2>The surfaces</h2>
<ul>
<li><b>Today</b> — a front door: the vault’s vital signs, what is worth a look, what is waiting, what you touched lately and what has waited longest.</li>
<li><b>Ask</b> — chat about your vault, against a local model or Anthropic. Every answer cites the vault.</li>
</ul>

<h2>The shape</h2>
<p>A native macOS app in SwiftUI over a containerized Rust core, split at a Makefile fence. The core
carries a derived index over markdown, git reads for recency and activity, an append-only decision
ledger, open questions and tasks as text, what is worth a look and why, vault writes that commit
themselves, and the files a new project starts with. There is one FFI boundary Swift may call, and a
headless CLI where every invariant is reachable.</p>""",
  side=[("Related", '<a href="../meridian/">Meridian</a> — the vault this reads')],
  links=[("Repository — private", None)]),

dict(
  slug="cyborg-support", num="12", title="Cyborg Support",
  sub="A federated project-discovery network",
  year="2026", medium="software / registry / network",
  status="Working locally; not deployed",
  blurb="The case it exists for: a project that is 70% built and has not been touched in 14 months.",
  lead="A local MCP profiles your projects — what they do, how mature they are, how reusable they are "
       "— and a hosted registry MCP lets someone else ask “is anyone already building this?” and get "
       "a real answer.",
  imgs=[("assets/img/plate-cyborg-support.svg", "Profile, registry, peer — nine nodes and the links between them.", False)],
  prose="""<h2>The case it exists for</h2>
<p>A project that is 70% built and has not been touched in 14 months.</p>

<h2>Status</h2>
<p>The scanner profiles real repositories, the maturity rubric is graded against a checked-in ground
truth, and all four services run. Nothing is hosted yet, so <code>publish_profile</code> reaches the
publisher and fails at the last hop — <b>by design, not by accident</b>.</p>""",
  side=[],
  links=[("Repository — private", None)]),

dict(
  slug="compute-club", num="13", title="Compute Club",
  sub="A cooperative interface for shared compute",
  year="2026", medium="software / commons / prototype",
  status="Prototype — real frontend, fully mocked data",
  blurb="Members run agents, build apps, and contribute back to a commons — earning credits they spend on compute.",
  lead="A cooperative interface for using language models on shared compute. Members run agents and "
       "harnesses, build apps, and contribute apps, archive material and reviewed AI knowledge back "
       "to a commons — earning credits they spend on compute.",
  imgs=[("assets/img/plate-compute-club.svg", "Credit, commons, compute — the membership as a mesh.", False)],
  prose="""<h2>The four surfaces</h2>
<ul>
<li><b>Dashboard</b> — personal: budgets shown remaining-first, a live active-agents panel with pause and kill and cost, usage charts, storage, projects, contributions and credits.</li>
<li><b>Commons</b> — community: a searchable registry of apps, archive and AI knowledge, each with provenance; knowledge carries a confidence and a review gate; governance proposals.</li>
<li><b>Workspace</b> — one multi-pane build environment: chat, harness runner, editor, terminal, logs.</li>
<li><b>Account &amp; Secrets</b> — SSH keys, secrets vault, profile, credits and billing, privacy defaults.</li>
</ul>

<h2>Status</h2>
<p>A real frontend with <b>fully mocked data</b> behind a swappable API layer. There is no real
backend, but the architecture is shaped so one can drop in.</p>""",
  side=[],
  links=[("Repository — private", None)]),

dict(
  slug="dream", num="14", title="Dream",
  sub="An ambient platformer",
  year="2026", medium="game / Godot 4.5",
  status="M1 built and green — 21 headless assertions; the look roughed in",
  blurb="You are dreaming. You win when you realise it.",
  lead="You are dreaming. You win when you realise it. A 2D silhouette-and-light ambient platformer, "
       "built solo in Godot 4.5.",
  imgs=[("assets/img/dream-03-arena-lucid.jpg", "The arena, lucid.", False),
        ("assets/img/dream-01-arena-asleep.jpg", "The same arena, asleep.", False),
        ("assets/img/dream-04-falling.jpg", "The fall.", False),
        ("assets/img/dream-06-landing-lucid.jpg", "Landing, lucid.", False)],
  prose="""<h2>Status</h2>
<p><b>M1 — “The Fall”</b> is built and green: 21 headless assertions over the whole sequence.</p>
<p><b>M3 — the look</b> was pulled forward and is roughed in. The world is still grey-box geometry
underneath; what changed is everything wrapped around it — which is what the screenshots here
show.</p>""",
  side=[("Engine", "Godot 4.5<br>2D silhouette and light<br>Solo build")],
  links=[("Repository — private", None)]),

dict(
  slug="bardo", num="15", title="Bardo",
  sub="Combat that resolves through recognition",
  year="2026", medium="game / Godot 4.5 / prototype",
  status="Milestone 1 only — one room, one deity, three practices",
  blurb="A 2D action platformer set in a modified Tibetan Book of the Dead, where combat resolves through recognition rather than damage.",
  lead="A Hollow-Knight-style 2D action platformer set in a modified Tibetan Book of the Dead, where "
       "your moveset is a limited loadout of yogic practices seated in chakras, and combat resolves "
       "through recognition rather than damage.",
  imgs=[("assets/img/plate-bardo.svg", "Practice, pattern, recognition.", False)],
  prose="""<h2>What exists</h2>
<p>Milestone 1 only: one room, one deity, three practices, coloured rectangles. It exists to answer
one question — is “survive the pattern while holding the correct practice” <i>fun</i>, or merely
clever?</p>
<p>Bardo is a working title.</p>""",
  side=[("Engine", "Godot 4.5<br>Headless smoke tests")],
  links=[("Repository — private", None)]),

# ---- works with no repository: art, editions, writing, collaborations -------
dict(
  slug="evertunes", title="Evertunes", sub="Westward Ho — nine chapters, ninety-nine stories",
  year="2021–", medium="generative video / music / NFT",
  status="Chapter One live — 11 of 99 released",
  blurb="The conquest of the American west told in 99 generative video-and-music stories, released chapter by chapter.",
  lead="Evertunes Studio works on the principle that everything has a value, though not "
       "necessarily a price. Westward Ho is its long-form work: the true story of the conquest of "
       "the American west, told in nine chapters of eleven stories each, in generative video and "
       "music.",
  imgs=[("assets/img/plate-evertunes.svg", "Nine chapters of eleven. Chapter One is struck; the remaining eighty-eight are not yet released.", False)],
  # Real stills, used automatically once tools/fetch-evertunes.sh has been run.
  optional_imgs=[
    ("assets/img/evertunes-colonial-hunger.jpg", "Colonial Hunger — the third year of drought at Jamestown.", False),
    ("assets/img/evertunes-jamestown.jpg", "Jamestown.", False),
    ("assets/img/evertunes-one-acre.jpg", "One Acre and No Mule.", False),
    ("assets/img/evertunes-myth-four.jpg", "Myth Four: The West was wilderness.", False)],
  prose="""<h2>The structure</h2>
<p>Ninety-nine works, released chapter by chapter rather than dropped at once. Each story is unique,
with varying qualities. The eleven stories in Chapter One are live, and exist to begin undoing the
myths of the Westward Expansion. Each story description propels the collection forward, while the
music and video amplify the narrative.</p>
<p>Chapter One is told in pieces named for what they describe — <i>Jamestown</i>,
<i>Colonial Hunger</i>, <i>The peaceful chief</i>, <i>Hunting</i>, <i>Lynched for witchcraft</i>,
<i>Pagan Name</i>, <i>The European Ways, or Else</i>, <i>One Acre and No Mule</i>,
<i>They Give, and Then Take it Away</i>, <i>Template for Future Ripoffs</i>,
<i>Myth Four: The West was wilderness</i>.</p>

<h2>What a story carries</h2>
<p>Each piece is a video work with its own written account. <i>Colonial Hunger</i> tells the third
year of drought at Jamestown: the settlers had been on friendly terms with the Indian groups around
them, until 1609, when the native federation’s chief Powhatan grew concerned about the drought and
about the English stealing from Indian villages, and forbade trade and barred them from poaching
animals. The colony began to starve.</p>
<p>Every work carries a set of measured traits alongside its chapter — <b>Generation</b>,
<b>Illusion</b>, <b>Anthropocene Factor</b>, <b>Epigenetic Trauma</b> — so that the qualities that
vary between stories are stated rather than left to be felt.</p>

<h2>Where it lives</h2>
<p>Minted as ERC-1155 on Ethereum under <i>evertunes-studio</i>, active since December 2021. The
chain here is a release mechanism and a ledger of what was issued, not the subject.</p>""",
  side=[("Collection", "Westward Ho<br>9 chapters × 11 stories = 99<br>Chapter One live"),
        ("Traits", "Chapter<br>Generation<br>Illusion<br>Anthropocene Factor<br>Epigenetic Trauma")],
  links=[("Evertunes Studio on OpenSea", "https://opensea.io/evertunes-studio")]),

dict(
  slug="what-the-tech", title="What the Tech", sub="Trust, authorship and ethics, written into code",
  year="2026", medium="collaboration / smart contract / video",
  status="First-year Visions2030 collaboration",
  blurb="Verifying origin and intent in an era shaped by forgery and deepfakes.",
  lead="A collaboration with conceptual artist Mary Ellen Carroll on questions of trust, authorship "
       "and ethics — carried out through Ethical Imagination, a project supported by Visions2030.",
  imgs=[("assets/img/plate-what-the-tech.svg", "Idea, code, record — an authorship chain and the seal that closes it.", False)],
  prose="""<h2>The question</h2>
<p>In its first year Visions2030 incubated artist collaborations, pairing artists with scientists,
engineers, ethicists and technologists to move ideas toward real-world application. This is one of
them: an artist and a technologist working the same problem from opposite ends.</p>
<p>The method is literal. Ideas are transformed into code and recorded as smart contracts on a
blockchain — which points toward new ways of <b>verifying origin and intent</b> in an era shaped by
forgery and deepfakes. The contract is not a market instrument here. It is a witness: a record that
says who made a claim, and when, that does not depend on the claimant still being around to
confirm it.</p>""",
  side=[("With", "Mary Ellen Carroll, conceptual artist"),
        ("Supported by", "Visions2030 — Ethical Imagination")],
  links=[("Visions2030 on Instagram", "https://www.instagram.com/reel/DTOUu3GExM4/")]),

dict(
  slug="peat-and-repeat", title="Peat and Repeat", sub="An artist-run edition house in Ridgewood",
  year="ongoing", medium="editions / print / publishing",
  status="Active — 501(c)(3) nonprofit",
  blurb="A nonprofit edition house producing artists' prints, photographs, books and environmental projects.",
  lead="Peat and Repeat is a 501(c)(3) nonprofit art edition house in Ridgewood, Queens. It produces "
       "artists’ prints and editions, photographs, books, and environmental projects — an "
       "independent, artist-run enterprise built on collective creative effort.",
  imgs=[("assets/img/plate-peat-and-repeat.svg", "A core read down through its beds, and the registration marks that hold an edition true.", False)],
  prose="""<h2>What it publishes</h2>
<p>The imprint carries <i>BOG</i>, <i>trouble</i> and <i>ephemera</i>, alongside the Woodbine Art
Auction and an apparel line. The range is deliberate: an edition house that only made prints would
be a press, and the environmental projects are what keep the printed work tied to a place rather
than to a market.</p>

<h2>Why an edition</h2>
<p>An edition is a form with a built-in politics. It fixes how many exist, states it publicly, and
distributes the work at a price a person can actually pay — which is a different proposition from
the unique object, and a different one again from the infinitely reproducible file.</p>
<p>The organization takes its bearings from a line of Louise Bourgeois’: “It is not so much where my
motivation comes from but rather how it manages to survive.”</p>""",
  side=[("Form", "501(c)(3) nonprofit<br>Ridgewood, Queens, New York"),
        ("Imprints", "BOG<br>trouble<br>ephemera<br>Woodbine Art Auction<br>apparel")],
  links=[("peatandrepeat.org", "http://peatandrepeat.org/")]),

dict(
  slug="pgm-diagrams", title="PGM Diagrams", sub="The Greek Magical Papyri, drawn as operations",
  year="ongoing", medium="diagram / ritual / computation",
  status="Ongoing — one spell fully formalised and building",
  blurb="Reading a spell as a procedure: what it takes in, what it emits, and what it does not account for.",
  lead="A reading practice on the Greek Magical Papyri that treats a spell as a procedure rather "
       "than a text — asking what it takes in, what it emits, what order its operations run in, and "
       "what the surviving papyrus does not account for.",
  imgs=[("assets/img/plate-pgm-diagrams.svg", "A column ruled and rubricated, with the lacuna left open rather than reconstructed.", False),
        ("assets/img/di-pnouthis.svg", "PGM I.42–195 formalised and drawn: fourteen rows, forty-four cycles, six lanes. Rendered by diagrammatic-immanence.", False)],
  prose="""<h2>The spell that anchors it</h2>
<p><b>PGM I.42–195</b> — the Pnouthis spell — is a rite for acquiring an assistant, the
<i>paredros</i>. It is the one that has been carried furthest: formalised as a monoidal category and
rendered as a string diagram in <a href="../diagrammatic-immanence/">Diagrammatic Immanence</a>,
where the same object also emits the score, and then used as the frame for
<a href="../order-of-the-meridian/">Order of the Meridian</a>, where the assistant summoned is a
machine and the week closes by giving it license to depart.</p>

<h2>What the drawing is for</h2>
<p>Drawing a rite as a diagram makes two things checkable that prose hides: the <b>order</b> of
operations, and the <b>typing</b> — what each step actually consumes and produces. Once a spell is
in that form, the parts that do not compose become visible, and so do the parts that were never
written down.</p>
<p>The lacunae are left as lacunae. A gap in the papyrus is a fact about the source, and filling it
silently would make the diagram say more than the manuscript does.</p>""",
  side=[("Carried into", '<a href="../diagrammatic-immanence/">Diagrammatic Immanence</a><br>'
                         '<a href="../order-of-the-meridian/">Order of the Meridian</a>')],
  links=[]),

dict(
  slug="prayer-coin", title="Prayer Coin", sub="A struck object for a thing that has no price",
  year="2018", medium="coin / ritual / value",
  status="Editioned object",
  blurb="A coin struck for prayer — the one transaction that was never supposed to have a denomination.",
  lead="A coin struck for prayer: an object that borrows the whole apparatus of money — the disc, "
       "the milled edge, the two faces, the promise — and applies it to the one exchange that was "
       "never supposed to carry a denomination.",
  imgs=[("assets/img/plate-prayer-coin.svg", "Obverse and reverse, struck: the milled edge, the legend ring, the relief.", False)],
  prose="""<h2>The proposition</h2>
<p>A coin is a claim about worth that a stranger will honour without knowing you. Prayer is the
opposite arrangement — unaccounted, unwitnessed, and not owed back. Striking one as the other puts
the two systems in the same hand and lets the mismatch do the work.</p>
<p>It belongs to a line of work that holds that <b>everything has a value, though not necessarily a
price</b> — and to a pair with the <a href="../unpaid-labor-coin/">Unpaid Labor Coin</a>, which
takes the same form to the other unpriced thing.</p>""",
  side=[("Pairs with", '<a href="../unpaid-labor-coin/">Unpaid Labor Coin</a>, 2019')],
  links=[]),

dict(
  slug="unpaid-labor-coin", title="Unpaid Labor Coin", sub="Denominated in the work nobody counted",
  year="2019", medium="coin / labor / value",
  status="Editioned object",
  blurb="A currency for care, maintenance and attention — the work that holds everything up and is never entered in a ledger.",
  lead="A coin denominated in unpaid labor: the care, maintenance and attention that hold every "
       "other kind of work up, and that no ledger has ever been asked to record.",
  imgs=[("assets/img/plate-unpaid-labor-coin.svg", "The same die, a different denomination — struck in verdigris rather than brass.", False)],
  prose="""<h2>The proposition</h2>
<p>Wages make some work visible by pricing it. Everything the price does not reach — the raising,
the tending, the cleaning, the remembering — stays economically invisible while remaining
absolutely load-bearing. A coin is the bluntest possible instrument for making that visible: it
forces a denomination onto something that has been kept deliberately undenominated.</p>
<p>Struck to the same specification as the <a href="../prayer-coin/">Prayer Coin</a>, a year later.
Together they mark the two directions value runs when it is not money: upward, unaccounted, and
downward, unpaid.</p>""",
  side=[("Pairs with", '<a href="../prayer-coin/">Prayer Coin</a>, 2018')],
  links=[]),

dict(
  slug="emu-butch", title="Emu Butch", sub="A book",
  year="in progress", medium="writing / book",
  status="Manuscript",
  blurb="A book-length work in prose.",
  lead="A book-length work in prose, written and edited in the open — and the reason the manuscript "
       "tooling in this stack exists at all.",
  imgs=[("assets/img/plate-emu-butch.svg", "Seven gatherings and one text block: a book seen from the spine.", False)],
  prose="""<h2>The book and its workbench</h2>
<p><a href="../palimpsest/">Palimpsest</a> was built for this manuscript before it was built for
anything else: a folder of numbered Markdown sections, a colour-coded reading copy, a parts board, a
copyedit pass, a back-of-book index and the motifs named by hand. The tool is
book-agnostic now, but the requirements came from one book.</p>
<p>That is the working method throughout: the writing and the instrument for the writing are made in
the same pass, and each one keeps the other honest.</p>""",
  side=[("Written in", '<a href="../palimpsest/">Palimpsest</a>')],
  links=[]),

dict(
  slug="mugworts", title="Mugworts Free Herbal Clinic", sub="Care as collective infrastructure",
  year="ongoing", medium="herbalism / care / collective practice",
  status="Ongoing practice",
  blurb="A free herbal clinic — medicine as something a community makes and keeps, not something it buys.",
  lead="A free herbal clinic: medicinal plants prepared and given away, and the practice of care "
       "treated as infrastructure a community holds itself rather than a service it purchases.",
  imgs=[("assets/img/plate-mugworts.svg", "A materia medica sheet: part, preparation, dose, note.", False)],
  prose="""<h2>Free, and what that requires</h2>
<p>Free is a structural claim, not a discount. It means the clinic has to be held up by something
other than payment — by growers, by preparers, by people who show up — and that the knowledge has to
be written down in a form others can pick up and run.</p>
<p>Herbal practice is where the rest of this work gets its model of an archive that has to stay
usable. A materia medica is only worth keeping if the next person can read the part, the
preparation, the dose and the caution and act on them; the same standard is what
<a href="../sanctuary-cell-division/">Sanctuary Cell Division</a> asks of an organization’s own
records.</p>""",
  side=[("Related", '<a href="../sanctuary-cell-division/">Sanctuary Cell Division</a> — archives an organization can actually read')],
  links=[]),

dict(
  slug="siliconkin", title="Siliconkin", sub="Kinship with the substrate",
  year="ongoing", medium="diagram / computation / sound",
  status="Ongoing",
  blurb="Taking the machine seriously as kin rather than tool — read as a floorplan, and heard.",
  lead="Work that takes the machine seriously as kin rather than as a tool: the die read as a "
       "landscape with regions and neighbours, and its activity heard rather than only measured.",
  imgs=[("assets/img/plate-siliconkin.svg", "A die floorplan and the signal read off it.", False)],
  prose="""<h2>The move</h2>
<p>A processor is usually described in the language of instruments — it executes, it serves, it is
used. Read instead as a floorplan, it becomes a place: blocks with borders, neighbours, traffic
between them, and a bond of pads at the edge where it meets everything else.</p>
<p>Making that audible is the second half. The same structure that draws as a floorplan can be read
out as sound, which is the operation
<a href="../diagrammatic-immanence/">Diagrammatic Immanence</a> and
<a href="../sounds-like/">sounds-like</a> both run: one object, two renderings, never a picture and
a soundtrack that merely resemble each other.</p>""",
  side=[("Related", '<a href="../diagrammatic-immanence/">Diagrammatic Immanence</a><br>'
                    '<a href="../sounds-like/">sounds-like</a>')],
  links=[]),

]

ORDER = [
    "order-of-the-meridian", "sanctuary-cell-division", "evertunes", "what-the-tech",
    "peat-and-repeat", "pgm-diagrams", "prayer-coin", "unpaid-labor-coin", "emu-butch",
    "mugworts", "siliconkin", "diagrammatic-immanence", "palimpsest", "sigil-studio",
    "divinatory-os", "sounds-like", "newmusic", "assay", "meridian", "research-manager",
    "cyborg-support", "compute-club", "dream", "bardo",
]
P.sort(key=lambda d: ORDER.index(d["slug"]))
for _i, _d in enumerate(P, 1):
    _d["num"] = f"{_i:02d}"

# Works from the index that have no material on disk yet — listed, not invented.
UNSOURCED = []

HERO_SVG = """<svg viewBox="0 0 800 600" role="img" aria-label="Abstract archival diagram: concentric circles crossed by traced paths and marked nodes">
        <g fill="none" stroke="#7f7b73" stroke-width="1">
          <circle cx="430" cy="300" r="190"/>
          <circle cx="430" cy="300" r="112"/>
          <circle cx="430" cy="300" r="42"/>
          <path d="M90 450 C190 345 270 365 350 290 S530 170 710 210"/>
          <path d="M110 170 C210 235 292 190 378 250 S540 390 705 355"/>
          <line x1="80" y1="95" x2="735" y2="520"/>
          <line x1="120" y1="520" x2="660" y2="75"/>
        </g>
        <g fill="#171715">
          <circle cx="350" cy="290" r="4"/><circle cx="430" cy="300" r="5"/>
          <circle cx="592" cy="335" r="4"/><circle cx="240" cy="215" r="4"/>
        </g>
        <g font-family="Courier New" font-size="11" fill="#514e48">
          <text x="80" y="88">TRACE / SIGNAL / BODY</text>
          <text x="515" y="545">TRANSDUCTION FIELD 01</text>
        </g>
      </svg>"""


# ------------------------------------------------------------------ build ---
def build_index():
    cards = []
    for pr in P:
        real = [x for x in pr.get("optional_imgs", []) if (ROOT / x[0]).exists()]
        thumb, alt, _ = real[0] if real else pr["imgs"][0]
        cards.append(f"""    <a class="card" href="projects/{pr['slug']}/">
      <div class="thumb"><img src="{thumb}" alt="{html.escape(alt, quote=True)}" loading="lazy" /></div>
      <div class="body">
        <div class="top"><span class="smallcaps">{pr['num']}</span><span class="smallcaps">{pr['year']}</span></div>
        <h3>{pr['title']}</h3>
        <p class="blurb">{pr['blurb']}</p>
        <p class="cardmeta smallcaps">{pr['medium']}</p>
      </div>
    </a>""")

    body = f"""<main>

<section class="hero">
  <div>
    <div class="smallcaps">selected work / ongoing index</div>
    <h1>Ritual technologies for more livable futures.</h1>
    <div class="rule"></div>
    <p>Art, infrastructures and herbal practice at the intersections of memory, networks, value, care and the more-than-human.</p>
  </div>
  <div>
    <div class="visual">
      {HERO_SVG}
    </div>
    <div class="caption smallcaps">documentation / diagram / field record</div>
  </div>
</section>

<section class="section" id="work">
  <div class="section-head">
    <h2>Selected Work</h2>
    <div class="smallcaps">an argument, not the whole archive</div>
  </div>
  <div class="cards">
{chr(10).join(cards)}
  </div>
</section>

<section class="section" id="about">
  <div class="section-head">
    <h2>About</h2>
    <div class="smallcaps">professional legibility</div>
  </div>
  <div class="about">
    <p>Eon Meridian is an artist, writer, technologist and herbalist working across computation,
    medicinal plants, ritual, sound, diagrams and resilient infrastructure. This site is an evolving
    record of works, collaborations, institutions and experiments. Its sibling —
    <a href="caerjar.html">Caerjar</a> — is the vessel much of this work is built inside.</p>
  </div>
</section>

</main>"""

    ROOT.joinpath("index.html").write_text(page(
        "Eon Meridian — Selected Work",
        "Eon Meridian — artist, writer, technologist, herbalist. Ritual technologies for more "
        "livable futures: art, infrastructures and herbal practice at the intersections of memory, "
        "networks, value, care and the more-than-human.",
        body, home="index.html", css="assets/site.css"))


def build_project(i, pr):
    # an optional image joins the plate list only when the file is actually on disk
    for src, cap, dark in pr.get("optional_imgs", []):
        if (ROOT / src).exists():
            pr["imgs"].append((src, cap, dark))
    figs = "\n".join(
        f"""    <figure>
      <div class="plate{' dark' if dark else ''}"><img src="../../{src}" alt="{html.escape(cap, quote=True)}" loading="lazy" /></div>
      <figcaption class="smallcaps">{cap}</figcaption>
    </figure>""" for src, cap, dark in pr["imgs"])

    meta = [f"<b>{pr['year']}</b>", pr["medium"]]
    if pr.get("venue"):
        meta.append(pr["venue"])
    meta.append(pr["status"])
    meta_html = "<br>".join(meta)

    sides = "\n".join(
        f'    <div class="side"><span class="smallcaps">{h}</span><br>{v}</div>'
        for h, v in pr["side"])

    links = "\n".join(
        (f'    <a href="{href}"{" target=_blank rel=noopener" if href.startswith("http") else ""}>{lbl} ↗</a>'
         if href else f'    <span class="off">{lbl}</span>')
        for lbl, href in pr["links"])

    prev_p, next_p = P[i - 1] if i else None, P[i + 1] if i + 1 < len(P) else None
    prev_html = (f'<a href="../{prev_p["slug"]}/">← {prev_p["title"]}</a>' if prev_p
                 else '<a href="../../index.html#work">← index</a>')
    next_html = (f'<a href="../{next_p["slug"]}/">{next_p["title"]} →</a>' if next_p
                 else '<a href="../../index.html#work">index →</a>')

    body = f"""<main>

<section class="proj-head">
  <div>
    <div class="smallcaps">{pr['num']} / project</div>
    <h1>{pr['title']}</h1>
    <div class="smallcaps" style="margin-top:9px">{pr['sub']}</div>
  </div>
  <div class="proj-meta">{meta_html}</div>
</section>

<p class="lead">{pr['lead']}</p>

<div class="plates">
{figs}
</div>

<div class="proj-body">
  <div class="prose">
{pr['prose']}
  </div>
  <div>
{sides if sides else '    <div class="side"><span class="smallcaps">index</span><br><a href="../../index.html#work">All work →</a></div>'}
  </div>
</div>

<div class="links">
{links}
  <a href="../../index.html#work">All work</a>
</div>

<nav class="prevnext">
  <span>{prev_html}</span>
  <span>{next_html}</span>
</nav>

</main>"""

    d = ROOT / "projects" / pr["slug"]
    d.mkdir(parents=True, exist_ok=True)
    d.joinpath("index.html").write_text(page(
        f"{pr['title']} — Eon Meridian", pr["blurb"], body,
        home="../../index.html", css="../../assets/site.css",
        icon="../../assets/favicon.svg"))


if __name__ == "__main__":
    build_index()
    for i, pr in enumerate(P):
        build_project(i, pr)
    print(f"index.html + {len(P)} project pages")
