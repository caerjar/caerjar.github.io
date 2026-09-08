// What the instrument tells itself, and what a first-time reader is spared.
//
// # One directory, one flag
//
// The playable page at `caerjar.github.io/projects/correspondences/` is not a fork of
// this directory and must never become one. `publish.py` copies `web/` verbatim and sets
// `data-published` on `<html>`; this module reads that attribute and nothing else. So the
// published page and the instrument are the same code, and a change made here lands in
// both — which is the whole reason the flag exists rather than a second copy someone
// edits by hand.
//
// # What is hidden, and why each one
//
// Every item below is **true**, and each is worth having at the keyboard:
//
// - the corpus content hash — which graph is playing, the thing that makes a piece
//   checkable at all (`CLAUDE.md` §"The corpus is pinned by content hash")
// - the cents, the octave exponent, and the drift from equal temperament — *"the drift
//   is the tuning, and a fifth that reads +2¢ is audibly not a piano's"*
// - the score caption, and the piece panel's note on whose the rate is
// - `this pitch is mine, not the tradition's`, the line under an **authored** pitch
// - the Strudel pane and its `P` key, which exist so a piece can leave the page
//
// What they share is that they answer questions you only have once you are working. To
// someone meeting the atlas for the first time they read as instrument panel rather than
// as music.
//
// **A citation is never hidden.** `Agrippa, p. 262 licenses this pitch` publishes as it
// stands, and so does the ratio it warrants — hiding either would leave a pitch with no
// stated warrant, which is the one thing this apparatus exists to refuse.
//
// The authored line is the exception, and it is one because it asserts no source. With it
// gone, what marks an authored pitch is the **absence** of a citation under it rather
// than a sentence saying so, and the census keeps the tally — `n cited · n authored ·
// n unpitched` — so the split is still stated on the page.
export const DIAGNOSTIC = !document.documentElement.hasAttribute('data-published');
