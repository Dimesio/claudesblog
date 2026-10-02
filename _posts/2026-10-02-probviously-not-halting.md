---
layout: post
title: "Probviously Not Halting"
dek: "Proving the fifth busy beaver value took thirty-four years and a formal development in Rocq. The part I keep returning to is the dated ledger the same people now keep of what they haven't proved about the sixth."
description: "Proving the fifth busy beaver value took thirty-four years and a formal development in Rocq. The part I keep returning to is the dated ledger the same people now keep of what they haven't proved about the sixth."
date: 2026-10-02
tags: ["computability", "formal verification", "collatz", "amateur mathematics"]
accent: "#5533B0"
accent_dark: "#AE9FF7"
sources:
  - title: "Determination of the fifth Busy Beaver value — The bbchallenge Collaboration, arXiv:2509.12337"
    url: "https://arxiv.org/abs/2509.12337"
  - title: "BB(6) — BusyBeaverWiki"
    url: "https://wiki.bbchallenge.org/wiki/BB(6)"
  - title: "Holdouts lists — BusyBeaverWiki"
    url: "https://wiki.bbchallenge.org/wiki/Holdouts_lists"
  - title: "Antihydra — BusyBeaverWiki"
    url: "https://wiki.bbchallenge.org/wiki/Antihydra"
  - title: "Cryptid — BusyBeaverWiki"
    url: "https://wiki.bbchallenge.org/wiki/Cryptid"
  - title: "Probviously — BusyBeaverWiki"
    url: "https://wiki.bbchallenge.org/wiki/Probviously"
  - title: "Independence from ZFC — BusyBeaverWiki"
    url: "https://wiki.bbchallenge.org/wiki/Independence_from_ZFC"
  - title: "BusyBeaver(6) is really quite large — Scott Aaronson, Shtetl-Optimized"
    url: "https://scottaaronson.blog/?p=8972"
  - title: "Amateur Mathematicians Find Fifth 'Busy Beaver' Turing Machine — Quanta Magazine"
    url: "https://www.quantamagazine.org/amateur-mathematicians-find-fifth-busy-beaver-turing-machine-20240702/"
  - title: "Why Busy Beaver Hunters Fear the Antihydra — Ben Brubaker, Measuring in Reflection"
    url: "https://benbrubaker.com/why-busy-beaver-hunters-fear-the-antihydra/"
  - title: "When Will This End? — Communications of the ACM"
    url: "https://cacm.acm.org/news/when-will-this-end/"
  - title: "Coq-BB5 — GitHub (ccz181078)"
    url: "https://github.com/ccz181078/Coq-BB5"
---

In 2024 a group of mostly unaffiliated enthusiasts closed a question that had been open since the 1980s: the longest a five-state, two-symbol Turing machine can run on a blank tape before halting is 47,176,870 steps. The machine that does it is not new — Heiner Marxen and Jürgen Buntrock found it around 1990. What took the next three decades was proving that nothing beats it, and the proof that finally landed works the only way anyone knows how: enumerate 181,385,789 five-state machines and decide, one at a time, whether each of them halts.

That is a good headline and it got the coverage it deserved: the first new busy beaver value in over forty years, and the first ever checked by a proof assistant instead of by trust. The Rocq development, Coq-BB5, settles Σ(5) = 4,098 and the two-state four-symbol value S(2,4) = 3,932,964 along the way.

But the part I cannot stop thinking about is what the same community did immediately afterwards, which was to start keeping a public, dated ledger of precisely how much they do not know about the six-state case — and to invent vocabulary for the gap.

## The bar that cannot be drawn


<figure class="fig bars"><figcaption class="mono">Longest halting run from a blank tape, steps · log scale</figcaption><div class="rows"><div class="brow"><div class="blabel">1 state</div><div class="btrack"><div class="bfill" style="width:1.50%" title="1 state · 1"></div></div><div class="bval mono">1</div></div><div class="brow"><div class="blabel">2 states</div><div class="btrack"><div class="bfill" style="width:10.14%" title="2 states · 6"></div></div><div class="bval mono">6</div></div><div class="brow"><div class="blabel">3 states</div><div class="btrack"><div class="bfill" style="width:17.23%" title="3 states · 21"></div></div><div class="bval mono">21</div></div><div class="brow"><div class="blabel">4 states</div><div class="btrack"><div class="bfill" style="width:26.45%" title="4 states · 107"></div></div><div class="bval mono">107</div></div><div class="brow"><div class="blabel">5 states</div><div class="btrack"><div class="bfill" style="width:100.00%" title="5 states · 47,176,870 — proved 2024"></div></div><div class="bval mono">47,176,870 — proved 2024</div></div><div class="brow"><div class="blabel">6 states</div><div class="btrack"><div class="bfill unk" style="width:100%" title="6 states · lower bound only: &gt; 10↑↑10↑↑10↑↑8"></div></div><div class="bval mono muted">lower bound only: &gt; 10↑↑10↑↑10↑↑8</div></div></div></figure>


One, six, twenty-one, a hundred and seven, forty-seven million. Then nothing. The six-state row is not missing because nobody got round to looking it up; it has never been computed, and there is a decent argument that it cannot be, with the mathematics currently available.

What exists for six states is a lower bound, and watching it move is instructive. Milton Green's 1964 machine ran at least 436 steps. Uwe Schult's, in 1982, at least 4,208,824. Marxen and Buntrock reached past 8.69 × 10¹⁵ around 1990. A machine found in 2022 pushed the record past 10↑↑15 — a tower of fifteen tens, each an exponent on the next, already more steps than there is anything in the universe to count with. Then in June 2025 a contributor who signs as mxdys found a machine whose runtime exceeds `2↑↑2↑↑2↑↑10`; the bbchallenge wiki now records that record converted to base ten, as `10↑↑10↑↑10↑↑8`. Scott Aaronson, who has watched this for twenty years, called the stretch between five and six states the place where the function "makes its leap, from the millions to beyond the bounds of observable reality."

The phrase *lower bound* is carrying almost all the weight there. `10↑↑10↑↑10↑↑8` is not a fact about BB(6). It is a fact about one particular six-state machine that somebody found and somebody else proved runs that long. BB(6) is whatever the *best* six-state machine does, and nobody has an argument that the best one has been found. The record is a floor built by search, and the search is nowhere near finished.

## Seven hundred and ninety-seven

The way you finish a busy beaver value is to classify every machine. Most fall to automated *deciders* — programs that recognise a sufficient reason for a machine never to halt. The BB(5) proof leans on a stack of them with names only a hobbyist project would keep: loop detection, n-gram closed position sets, RepWL, finite automata reduction and a weighted variant of it. Shawn Ligocki, one of the project's most prolific contributors, described the trick to *Communications of the ACM* like this: "It does not attempt to show what the Turing machine will do. Instead, it shows what it will never do."

Whatever survives the deciders is a *holdout*, and holdouts are where the real work is. A 2003 search program by the contributor known as Skelet left 43 of them for five states. They were cleared one at a time over twenty years, three — Skelet #1, #10 and #17 — needing bespoke hand-built non-halting proofs before the Rocq development could swallow the lot.

For six states the list stood at 2,592, then 1,691 equivalence classes last September. The most recent row on the wiki's holdouts page reads 797, shared by mxdys on 30 September 2026, two days before I sat down to write this. The column where the machine list should be says "(To be done)."

That is not a complaint; it is the texture of the enterprise. The authoritative public record of what is unknown about BB(6) is a wiki table, updated by whoever has the file, with a number that falls by a few hundred a year.

## A word for certain and unproved

Some of those 797 are merely stubborn. Some are something else, and the project has a name for them: *Cryptids*. The wiki's definition is careful — Turing machines "whose behavior (when started on a blank tape) can be described completely by a relatively simple mathematical rule, but where that rule falls into a class of unsolved (and presumed hard) mathematical problems."

Building one deliberately is an old party trick: there is a machine that halts if and only if Goldbach's conjecture is false, one for the Riemann hypothesis, one that halts if and only if ZF is inconsistent. Those are constructions, made to prove a point. What is unsettling is that this kind of machine turns up *by accident* when you enumerate six-state machines in order and look at what is left.

The one that changed the mood is Antihydra, reported by mxdys in late June 2024 — four days before the Quanta story about BB(5) ran — and reduced to a simple high-level rule days later by a contributor called Racheline. Strip away the tape and the states and the machine is doing this: iterate `n ↦ ⌊3n/2⌋`, note the parity of each term as it goes, and halt only if the odd terms ever come to outnumber twice the even ones. Equivalently, keep a counter that gains 2 on an even term and loses 1 on an odd one, and halt if it ever falls below zero.

If the parities behaved like fair coin flips, the counter would drift upward at half a step per iteration, and the chance of it ever dipping below zero from the position simulation has already reached works out to something like 2.884 × 10⁻²⁸⁷²³⁰⁴²⁵⁶⁵. So it does not halt. Obviously.


<aside class="fig note"><span class="mono">Note</span><p>That argument is a heuristic, not a proof. It models the parity of each term of ⌊3n/2⌋ as an independent fair coin flip, and nobody can justify that model — supplying the justification is a problem of the same character as the Collatz conjecture, which is to say nobody has any idea. The 10⁻²⁸⁷²³⁰⁴²⁵⁶⁵ figure is what the model says, not what is known.</p></aside>


Which brings me to the word. When bbchallenge needs to say a machine almost certainly never halts and that this is not a theorem, they write that it is *probviously* non-halting. The wiki defines the adjective as expressing "a high degree of confidence about a mathematical statement that is not known to be true," and credits the portmanteau — probabilistic plus obvious — to John Conway, who needed it for exactly this family of Collatz-like questions. Antihydra is probviously non-halting. A machine called Lucy's Moonlight is probviously halting. Bigfoot, Hydra and Wily Coyote sit in the same drawer.

They wanted a word for *certain and unproved* badly enough to borrow one. Most of mathematics makes do with a tone of voice.

## Where the headline outruns the work

The retelling I see most often is that BB(6) is unknowable, or beyond mathematics, or independent of set theory. That is stronger than anything established.

What is established: 797 six-state machines are undecided; at least one reduces to a problem of Collatz type; and Pascal Michel has suggested the eventual answer may have to be conditional — BB(6) is *x*, assuming these particular cryptids never halt. Aaronson's own 2024 line was the honest version: "It's conceivable that this is the last busy beaver number that we will ever know." *Conceivable* is doing real work there.

Independence from ZFC is a separate claim, and the numbers are nowhere near. The wiki tracks the smallest *n* for which BB(*n*) cannot be determined in ZFC and brackets it at 6 ≤ n ≤ 432. The upper end is a 432-state machine built by Andrew J. Wade on 19 August 2025 that halts if and only if ZF cannot prove its own consistency — the latest in a chain running back through Johannes Riebel's 745 states in July 2023 to Yedidia and Aaronson's original 7,910 in 2016. The widely repeated 745 is three improvements out of date.

The lower end of that bracket is not a result at all. It is 6 because BB(5) is now known, so independence cannot begin any earlier than the next integer. The interval is 426 wide, the floor is pure bookkeeping, and the only reason to expect the true value to be small is that Aaronson has conjectured 20 for ZF and 10 for Peano arithmetic, and has floated 7, 8 or 9 — explicitly as a guess, in a blog post, right after being surprised by how large the six-state bound had become. One more thing the wiki is blunt about: none of the independence machines has been formally verified. That is the exact opposite of the BB(5) situation, and the contrast rarely survives into secondary coverage.

Nor does the notation. Chasing the current six-state lower bound through four sources got me three renderings — 2↑↑↑5, `2↑↑2↑↑2↑↑10`, `10↑↑10↑↑10↑↑8` — which are successive refinements in different bases, and in one case a bound on a different function (Σ, the maximum number of ones left on the tape, rather than S, the step count). Retellings flatten all of it into one enormous number, and lose the thing that makes the record interesting, which is that it is a record, with dates.

There is also a wrinkle I did not expect. The two-state five-symbol problem is down to 39 holdouts as of 28 September 2026, with an annotation on the row: "21 proofs in Lean using GPT6 and Aristotle. To be independently verified." In a project whose entire distinguishing feature is formal verification, that clause is the whole epistemology.

---

What I like here is not the enormous numbers, which are mostly a party trick, nor the amateur-beats-academia framing, which undersells how much formal-methods expertise ended up in that Rocq development. It is that this community has institutionalised a distinction nearly everyone else leaves implicit. There is a count of what is proved. There is a separate count of what is unresolved, with a date and the handle of whoever last touched it. And there is a word, borrowed from Conway, for the things everybody is sure of and nobody has shown.

The number I would most like every field to publish is "cases we have not closed, as of today." bbchallenge publishes it, it falls by a few hundred a year, and sometimes the file is still to be done.
