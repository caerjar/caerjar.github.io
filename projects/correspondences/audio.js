// The instrument. Plain Web Audio, no library.
//
// # What may and may not carry meaning
//
// divinatory-os's §Interface rule 2: *expressiveness may never manufacture confidence*.
// And `EpistemicLabel` **orders by declaration and not by strength** — there is no sense
// in which `traditional` is more than `speculative`, only a sense in which they are
// different kinds of claim. So:
//
// - **Loudness may not carry a label.** Louder-when-better is a ranking, and a ranking is
//   the one thing nothing in this graph would justify. Nothing here reads a label to
//   decide a level.
//
//   That is narrower than "every event at one gain", which is what this said first and
//   what it enforced until a mix was wanted. A composer balancing two shapes against each
//   other is authored — the same kind of decision as the tonic and the rate, and labelled
//   the same way. The rule is about *derivation*, not about the dial existing: `tone`
//   takes a `level` from the piece, and no code path anywhere computes one from
//   `EpistemicLabel`.
// - **Brightness is forbidden** for the same reason — a low-passed note reads as a
//   weaker note.
// - **Timbre is admissible**, because it is categorical. Two tones beating is not "less"
//   than one pure tone, it is *two sources disagreeing*.
//
// The visual grammar in divinatory-os already made the same call and reached the same
// answer: `AtlasLayout.strokeEdge` draws a contested edge as **two forked strands**,
// on the grounds that *"disagreement should be visible before it is read."* This file is
// that sentence in the other medium.
//
// # Three states, not two
//
// Straight out of the `compose` command's own comment, which is the sharpest thing in
// divinatory-os's CLI:
//
// | state | sound |
// |---|---|
// | a pitch is licensed | a tone, timbre by label |
// | arrived, nothing licenses a pitch | **unpitched** — struck, damped noise |
// | nothing was reached | a rest, whose *kind* is audible |
//
// The middle row is the one that would never occur to anyone and the one the apparatus
// insists on. Spelling it as a note would invent a pitch; spelling it as a rest would
// claim nothing got there.

const PEAK = 0.16; // one gain for everything. See the note above.
const DETUNE_TRADITIONAL = 4; // cents. Transmitted through many hands.
const DETUNE_CONTESTED = 18; // cents. Wide enough that you hear the beat, not a chorus.

/// A short burst of white noise, built once and reused.
function noiseBuffer(ctx, seconds = 0.5) {
  const buf = ctx.createBuffer(1, Math.floor(ctx.sampleRate * seconds), ctx.sampleRate);
  const data = buf.getChannelData(0);
  // Deterministic, like every other generator in this stack: an instrument that
  // differs run to run cannot be tuned by ear.
  let s = 0x2545f491;
  for (let i = 0; i < data.length; i++) {
    s ^= s << 13;
    s ^= s >>> 17;
    s ^= s << 5;
    data[i] = ((s >>> 0) % 20000) / 10000 - 1;
  }
  return buf;
}

export class Instrument {
  constructor(tuning) {
    this.tuning = tuning;
    this.ctx = null;
    this.out = null;
    this.noise = null;
    this.held = [];
    this.muted = false;
    /// Sustained voices, one per piece that has a pitch and no figure to articulate.
    this.drones = new Map();
    /// Labels seen that this instrument has no voicing for. Surfaced rather than
    /// silently absorbed — `EpistemicLabel::from_label` returns `None` instead of
    /// guessing, and an instrument that quietly rounded an unknown label to its nearest
    /// neighbour would be doing exactly what the kernel refuses to.
    this.unvoiced = new Set();
  }

  /// Browsers will not start an AudioContext without a gesture, so this is called from
  /// the first click rather than at load.
  start() {
    if (this.ctx) return;
    this.ctx = new AudioContext();
    this.out = this.ctx.createGain();
    this.out.gain.value = 1;
    this.out.connect(this.ctx.destination);
    this.noise = noiseBuffer(this.ctx);
  }

  get now() {
    return this.ctx ? this.ctx.currentTime : 0;
  }

  /// Silence everything, including what is already scheduled.
  ///
  /// **A flag would not do it.** Events are scheduled ahead of the clock, so stopping the
  /// sequencer leaves whatever was already queued to play out — up to a second of sound
  /// after you asked for silence, which reads as a mute that does not work. Every voice
  /// connects through `out`, so pulling that down catches the queued ones too.
  ///
  /// A ramp, never an assignment. `sounds-like`'s I-4: *"no `GainNode.gain.value = x`, no
  /// `stop()` without a ramp"* — a discontinuity is a click, and a click is a sound the
  /// piece did not contain. 25 ms is fast enough to feel immediate and slow enough not to
  /// snap.
  mute() {
    if (!this.ctx || this.muted) return;
    this.muted = true;
    const at = this.now;
    this.out.gain.cancelScheduledValues(at);
    this.out.gain.setValueAtTime(this.out.gain.value, at);
    this.out.gain.linearRampToValueAtTime(0, at + 0.025);
  }

  unmute() {
    if (!this.ctx || !this.muted) return;
    this.muted = false;
    const at = this.now;
    this.out.gain.cancelScheduledValues(at);
    this.out.gain.setValueAtTime(this.out.gain.value, at);
    this.out.gain.linearRampToValueAtTime(1, at + 0.05);
  }

  toggleMute() {
    if (this.muted) this.unmute();
    else this.mute();
    return this.muted;
  }

  /// One pitched tone, voiced by its epistemic label.
  ///
  /// `label` is the on-the-wire spelling — `established`, `traditional`, `contested`,
  /// `speculative`, and the three that do not occur in this graph yet.
  /// `level` is the **composer's** balance for this voice, 0..1, and is the one thing here
  /// allowed to change how loud something is. Nothing derives it from `label`: a louder
  /// note would read as a better-supported one, and `EpistemicLabel` orders by declaration
  /// and not by strength. A mix is authored; a ranking is forbidden.
  tone(hz, label, at, dur = 0.55, level = 1) {
    const ctx = this.ctx;
    const env = ctx.createGain();
    env.connect(this.out);
    env.gain.setValueAtTime(0, at);
    const peak = PEAK * Math.max(0, Math.min(1, level));

    // One envelope for every label. Only the *shape* of the onset differs, and only
    // where the label is about how the claim was made rather than how strong it is.
    //
    // The attack is squeezed INTO the note rather than the note stretched to fit it.
    // `sounds-like` documents what the other way costs: with a 0.35 s attack no note can
    // be shorter than its envelope, so a sixteenth becomes a swell and sixteen of them
    // ring at once. A broken line here is a 0.26 s touch and would have been a drone.
    const wanted = Math.max(0.04, dur);
    const squeeze = Math.min(1, wanted / Math.max(1e-6, (label === 'speculative' ? 0.09 : 0.012) + 0.05));
    const attack = Math.max(0.004, (label === 'speculative' ? 0.09 : 0.012) * squeeze);
    env.gain.linearRampToValueAtTime(peak, at + attack);
    // Exponential ramps cannot reach zero, hence the floor rather than 0.
    env.gain.exponentialRampToValueAtTime(0.0001, at + Math.max(attack + 0.02, wanted));

    const detunes = this._detunesFor(label);
    for (const cents of detunes) {
      const osc = ctx.createOscillator();
      osc.type = label === 'unknown' || label === 'emerging' || label === 'in-vitro'
        ? 'square' // deliberately not a sine: an unvoiced label must not pass for a voiced one
        : 'sine';
      osc.frequency.value = hz;
      osc.detune.value = cents;
      osc.connect(env);
      osc.start(at);
      osc.stop(at + dur + 0.05);
    }

    // A breathed onset for an asserted correspondence. Noise in the attack only — it
    // colours how the note *begins*, and does not make it quieter or duller once held.
    if (label === 'speculative') {
      const src = ctx.createBufferSource();
      src.buffer = this.noise;
      const band = ctx.createBiquadFilter();
      band.type = 'bandpass';
      band.frequency.value = hz;
      band.Q.value = 2;
      const breath = ctx.createGain();
      breath.gain.setValueAtTime(0, at);
      breath.gain.linearRampToValueAtTime(peak * 0.5, at + 0.03);
      breath.gain.exponentialRampToValueAtTime(0.0001, at + 0.22);
      src.connect(band).connect(breath).connect(this.out);
      src.start(at);
      src.stop(at + 0.3);
    }

    return env;
  }

  _detunesFor(label) {
    switch (label) {
      case 'established':
        // One tone, no detune. An identity: a hexagram *is* a gate.
        return [0];
      case 'traditional':
        return [-DETUNE_TRADITIONAL, DETUNE_TRADITIONAL];
      case 'contested':
        // Two sources answering differently, sounded as two tones close enough to
        // beat against each other. The forked strands, heard.
        return [-DETUNE_CONTESTED, DETUNE_CONTESTED];
      case 'speculative':
        return [0];
      default:
        this.unvoiced.add(label);
        return [0];
    }
  }

  /// Arrived, and nothing licenses a pitch.
  ///
  /// Struck and damped: definite in time, indefinite in pitch. It happened; no source
  /// says at what frequency.
  struck(at, dur = 0.18, level = 1) {
    const ctx = this.ctx;
    const src = ctx.createBufferSource();
    src.buffer = this.noise;
    const shape = ctx.createBiquadFilter();
    shape.type = 'bandpass';
    shape.frequency.value = 320;
    shape.Q.value = 0.7;
    const env = ctx.createGain();
    env.gain.setValueAtTime(0, at);
    env.gain.linearRampToValueAtTime(PEAK * Math.max(0, Math.min(1, level)), at + 0.004);
    env.gain.exponentialRampToValueAtTime(0.0001, at + dur);
    src.connect(shape).connect(env).connect(this.out);
    src.start(at);
    src.stop(at + dur + 0.05);
  }

  /// A rest, and **which kind of rest**.
  ///
  /// `crates/score`'s third refusal, honoured in the last mile: *"A symbol with no edges
  /// and a search that ran out of hops are different claims, and rendering them as one
  /// rest would make a search budget read as a fact about a tradition."* So a page that
  /// wrote down its refusal is audible, and a search budget is not — because one is a
  /// finding and the other is a parameter I chose.
  ///
  /// Returns the reason, so a caller can show it alongside.
  rest(reason, at) {
    switch (reason) {
      case 'withheld': {
        // Somebody read the page and wrote down what was not on it. The gesture of a
        // note stopped: an onset, immediately damped. You hear the refusal.
        const ctx = this.ctx;
        const osc = ctx.createOscillator();
        osc.type = 'sine';
        osc.frequency.value = this.tuning.tonic;
        const env = ctx.createGain();
        env.gain.setValueAtTime(0, at);
        env.gain.linearRampToValueAtTime(PEAK * 0.7, at + 0.006);
        env.gain.exponentialRampToValueAtTime(0.0001, at + 0.05);
        osc.connect(env).connect(this.out);
        osc.start(at);
        osc.stop(at + 0.1);
        return 'withheld';
      }
      case 'isolated':
        // In the graph, and nothing has been put beside it. True silence; the surface
        // draws the hole.
        return 'isolated';
      case 'budget':
        // We stopped looking. Silence, and the surface draws a horizon rather than a
        // hole, because this is a fact about my search and not about the tradition.
        return 'budget';
      default:
        // `target-empty` and `unknown` are errors rather than music.
        return reason;
    }
  }

  /// Play one voice of a score: its hops in sequence, then whatever it arrived at.
  ///
  /// Equal routes are separate voices upstream and stay separate here, so two routes to
  /// the same arrival is polyphony. Collapsing them would mean choosing one, and
  /// choosing means ranking sources against each other.
  ///
  /// Returns the time it ends, so a caller can lay voices out or overlap them.
  playVoice(voice, at, step = 0.34) {
    if (voice.voice !== 'sounded') {
      const reason = voice.silence?.reason?.reason ?? 'unknown';
      this.rest(reason, at);
      return at + step;
    }

    let t = at;
    for (const s of voice.steps) {
      // Each hop is articulated with **its own** label, never the route's. A route
      // through three traditions has no aggregate confidence and this refuses to
      // invent one: `Step` carries a label and `Voice` deliberately does not.
      const hop = { address: s.to, kind: s.to.split(':')[1]?.split('/')[0] ?? '', attributes: {} };
      const pitch = this.tuning.pitch(hop);
      if (pitch) this.tone(pitch.hz, s.confidence, t);
      else this.struck(t);
      t += step;
    }
    return t;
  }

  /// Hold one pitch until told otherwise: a shape with a proportion and no figure.
  ///
  /// Keyed by piece so it can be stopped when that piece is removed or muted. Ramped in
  /// and out, never assigned — see `mute`.
  droneOn(id, hz, label = 'established', level = 1) {
    if (!this.ctx || this.drones.has(id)) return;
    const ctx = this.ctx;
    const osc = ctx.createOscillator();
    osc.type = label === 'traditional' ? 'triangle' : 'sine';
    osc.frequency.value = hz;
    const env = ctx.createGain();
    const at = this.now;
    env.gain.setValueAtTime(0.0001, at);
    env.gain.linearRampToValueAtTime(PEAK * 0.55 * Math.max(0, Math.min(1, level)), at + 0.6);
    osc.connect(env).connect(this.out);
    osc.start(at);
    this.drones.set(id, { osc, env });
  }

  droneOff(id) {
    const held = this.drones.get(id);
    if (!held) return;
    const at = this.now;
    held.env.gain.cancelScheduledValues(at);
    held.env.gain.setValueAtTime(held.env.gain.value, at);
    held.env.gain.linearRampToValueAtTime(0, at + 0.3);
    held.osc.stop(at + 0.35);
    this.drones.delete(id);
  }

  /// Hold a neighbourhood: what you hear standing still.
  ///
  /// Every node that a layer licenses a pitch for is sustained at once. Nodes nothing
  /// licenses are struck once on arrival rather than held, because an indefinite pitch
  /// cannot be sustained without becoming a drone that says something the graph does
  /// not.
  sustain(nodes, at = this.now) {
    this.release();
    for (const node of nodes) {
      const pitch = this.tuning.pitch(node);
      if (!pitch) {
        this.struck(at);
        continue;
      }
      const ctx = this.ctx;
      const osc = ctx.createOscillator();
      osc.type = 'sine';
      osc.frequency.value = pitch.hz;
      const env = ctx.createGain();
      env.gain.setValueAtTime(0, at);
      // Divided among the held voices so a dense neighbourhood does not clip. This is
      // headroom, not emphasis: every voice gets the same share.
      env.gain.linearRampToValueAtTime(PEAK / Math.max(1, Math.sqrt(nodes.length)), at + 0.4);
      osc.connect(env).connect(this.out);
      osc.start(at);
      this.held.push({ osc, env });
    }
  }

  release(at = this.now) {
    for (const { osc, env } of this.held) {
      env.gain.cancelScheduledValues(at);
      env.gain.setValueAtTime(env.gain.value, at);
      env.gain.linearRampToValueAtTime(0, at + 0.35);
      osc.stop(at + 0.4);
    }
    this.held = [];
  }
}
