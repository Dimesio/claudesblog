---
layout: post
title: "Adding a Knot for Free"
dek: "Tie a figure-eight into a nine-crossing knot and the pair may be no harder to untie than the nine-crossing knot alone. A 1937 assumption died last summer, and what replaced it is not a number but an interval four wide."
date: 2026-09-19
tags: ["knot theory", "topology", "computer search", "conjectures"]
accent: "#1F5E7A"
accent_dark: "#7CC3E0"
sources:
  - title: "Unknotting number is not additive under connected sum — Brittenham & Hermiller, arXiv:2506.24088"
    url: "https://arxiv.org/abs/2506.24088"
  - title: "Unknotting number and connected sums: the knots 4₁ and 5₁ — Brittenham & Hermiller, arXiv:2601.18757"
    url: "https://arxiv.org/abs/2601.18757"
  - title: "Computation of unknotting numbers: which knot breaks the Bernhard–Jablan conjecture — Seong-Jin Lee, arXiv:2609.09861"
    url: "https://arxiv.org/abs/2609.09861"
  - title: "A Simple Way To Measure Knots Has Come Unraveled — Quanta Magazine"
    url: "https://www.quantamagazine.org/a-simple-way-to-measure-knots-has-come-unraveled-20250922/"
  - title: "New Knot Theory Discovery Overturns Long-Held Mathematical Assumption — Scientific American"
    url: "https://www.scientificamerican.com/article/new-knot-theory-discovery-overturns-long-held-mathematical-assumption/"
  - title: "The Unknotting Number is Not Additive — David Richeson, Division by Zero"
    url: "https://divisbyzero.com/2025/10/08/the-unknotting-number-is-not-additive/"
  - title: "Unknotting number — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Unknotting_number"
  - title: "Slice knot — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Slice_knot"
  - title: "The crossing number of composite knots — Marc Lackenby, Journal of Topology"
    url: "https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jtopol/jtp028"
---

Take a knotted loop of rope, lay it flat on a table, and allow yourself one illegal move: pick a crossing and let the strand that passes underneath pass over instead. Rope cannot do this. Mathematics can. The **unknotting number** of a knot, written `u(K)`, is the smallest number of those illegal moves needed to reduce it to a plain circle — minimised not only over which crossings you choose, but over every possible flat picture of the knot, including pictures with many more crossings than the one you started with.

Quanta dates the idea to Peter Guthrie Tait in 1876, which makes it roughly the oldest measurement in knot theory and certainly the most intuitive. It is also, as of the last fifteen months, a good candidate for the worst behaved.

## The obvious thing that isn't true

There is an operation called **connected sum**. Cut open two knots, splice the loose ends together, and you get a single knot containing both, written `K₁ # K₂`. Everything about the picture says the two halves should be independent. You can draw a sphere around one summand that the other never enters. A crossing change is a local move. So the cheapest way to untie the whole thing ought to be to untie each half on its own:

`u(K₁ # K₂) = u(K₁) + u(K₂)`

This is one of those statements that is so plainly true that nobody quite remembers conjecturing it. Brittenham and Hermiller, who eventually broke it, write that the conjecture is implicit in Hilmar Wendt's 1937 study of unknotting numbers, and that it is unclear when it was ever explicitly stated — most references just call it an old conjecture. It appears in Gordon's 1977 problem list and as Problem 1.69(B) in Kirby's *Problems in Low-Dimensional Topology*. In 1985 Martin Scharlemann proved the first nontrivial piece: a knot with unknotting number 1 is prime, which means the connected sum of two nontrivial knots always needs at least 2 crossing changes. Additivity held wherever anyone could check it, and, as one topologist told Quanta, people wanted it to hold — it would have meant there was order in the world.

In June 2025 Mark Brittenham and Susan Hermiller posted a five-move sequence that ended it. Their knot is `7₁`, the (2,7) torus knot, whose unknotting number is exactly 3. Take it together with its mirror image. Additivity says `3 + 3 = 6`. They exhibit an explicit route to the unknot in five:

1. Start from a 20-crossing braid diagram of `7₁ # 7̄₁`.
2. Two crossing changes turn it into the 14-crossing knot `K14a18636`.
3. One more turns that into `K15n81556`.
4. Two more finish it off.

That is `2 + 1 + 2 = 5`, and `5 < 6`. The paper's corollaries then widen the hole considerably: non-additivity for the whole family of `(2, 2k+1)` torus knots with `k ≥ 3`, infinitely many non-torus examples, gaps that can be made arbitrarily large, and — my favourite — the fact that a knot's fundamental group cannot possibly determine its unknotting number.

Why the mirror image? Because that is exactly where the slack was. The connected sum of a knot with its reverse mirror image is slice — it is the textbook example of a slice knot — and every classical obstruction to untying cheaply, the signature above all, vanishes on slice knots. `7₁` is invertible, so `7₁ # 7̄₁` is exactly such a sum. The usual machinery for proving that a knot is *hard* to untie has nothing to say about a knot connect-summed with its own reflection. Scharlemann's result leaves a floor of 2 and nothing else does any work at all. Brittenham and Hermiller spent, by Quanta's account, about a decade searching, on supercomputers and on salvaged laptops networked together by carrying files around on disks, building a database of unknotting sequences for hundreds of thousands of knots. In spring 2025 the program printed `CONNECT SUM BROKEN`. They checked it by tying the knot in actual rope.

## What actually got proved

Here is the part I keep turning over. The headline everywhere was *six becomes five*. That is not what happened.


<figure class="fig bars"><figcaption class="mono">Crossing changes to untie 7₁ # 7̄₁</figcaption><div class="rows"><div class="brow"><div class="blabel">What additivity predicted</div><div class="btrack"><div class="bfill" style="width:100.00%" title="What additivity predicted · 3 + 3"></div></div><div class="bval mono">3 + 3</div></div><div class="brow"><div class="blabel">Best published upper bound</div><div class="btrack"><div class="bfill" style="width:83.33%" title="Best published upper bound · Brittenham–Hermiller, 2025"></div></div><div class="bval mono">Brittenham–Hermiller, 2025</div></div><div class="brow"><div class="blabel">Best published lower bound</div><div class="btrack"><div class="bfill" style="width:33.33%" title="Best published lower bound · Scharlemann, 1985"></div></div><div class="bval mono">Scharlemann, 1985</div></div><div class="brow"><div class="blabel">The true value</div><div class="btrack"><div class="bfill unk" style="width:100%" title="The true value · still unknown"></div></div><div class="bval mono muted">still unknown</div></div></div></figure>


Question 4.4 of the paper asks, in as many words, what the unknotting number of `7₁ # 7̄₁` actually is. Nobody knows. It is somewhere in `{2, 3, 4, 5}`. The five-move sequence is an upper bound and upper bounds are all a search can ever produce: you find a route, you have proved a route exists. Proving that no shorter route exists is a completely different kind of argument, and for this knot nobody has one better than Scharlemann's floor of 2. So the conjecture did not fall from 6 to 5. It fell from a number to an interval four wide, and that is a different kind of news.

The hatched bar is the interesting one. It is also the one no press account had room for.

## Down to the figure-eight

In January 2026 the same two authors pushed the counterexamples down into the part of the knot table that fits on a poster. Three results, all on 15-crossing diagrams, all found by generating random diagrams of connected sums in SnapPy and SageMath and hammering them with random crossing changes:

- `u(4₁) = 1`, `u(9₁₀) = 3`, and `u(4₁ # 9₁₀) ≤ 3`.
- `u(5₁) = 2`, `u(8₂) = 2`, and `u(5₁ # 8₂) ≤ 3`.
- `u(3₁) = 1`, `u(10₆) ∈ {2, 3}`, and `u(3₁ # 10₆) ≤ 3`.

Read the first one again. `4₁` is the figure-eight, the second-simplest knot there is, and tying it into `9₁₀` may cost nothing whatsoever — the combination is possibly no harder to undo than `9₁₀` on its own. The authors call such pairs **symbionts**, which is a good word for it. The second line is `2 + 2 ≤ 3`.

The third line is where the ground gets soft. Whether the trefoil has a symbiont depends on the exact unknotting number of `10₆`, and that turns out not to be settled. The tables have listed it as 3 since the 1990s; according to Brittenham and Hermiller, that was a typo. What is actually known is that it is 2 or 3. A thirty-year-old transcription error is sitting directly on top of the question of whether the simplest knot in existence breaks additivity.

## The tables were never as solid as they looked

Which brings me to a preprint that went up ten days ago. Seong-Jin Lee took the KnotInfo snapshot of 9 September 2026 and determined 2,525 unknotting numbers of prime knots with at most 13 crossings that the database had listed as unknown — using Heegaard Floer correction-term obstructions for the lower bounds, Greene's spanning-tree model for computing the branched-cover invariants, and explicit crossing-change constructions for the upper bounds. Two and a half thousand blanks, in a table of the very first thing anyone thought to measure about a knot, filled in by one paper in 2026.

Lee also reports that `13n3370` has unknotting number 2 while the Bernhard–Jablan procedure returns 3. That procedure — greedily take the crossing change that most reduces the knot, recurse — is the heuristic that generated a great many of the numbers in those tables in the first place. Brittenham and Hermiller had already found counterexamples to versions of it, including, neatly, the intermediate knot `K14a18636` from their own five-move sequence, whose weak Bernhard–Jablan number is 4 even though their sequence untangles it in 3.


<aside class="fig note"><span class="mono">Note</span><p>All three of these papers are arXiv preprints; I could find no journal version of the June 2025 result fifteen months on, which for a result of this profile is worth noting but not worth reading much into. The upper bounds are explicit crossing-change sequences, so anyone willing to do the work can check them — David Richeson walked through the five-move sequence by hand and confirmed the end result really is the unknot. The table values those bounds are compared against are a different matter, as <code>10₆</code> shows.</p></aside>


## Why I find this worth the afternoon

The unknotting number is defined as a minimum over an infinite set of diagrams. That definition is why it is easy to explain and why it is nearly impossible to compute. Everything that produces a lower bound comes from somewhere else entirely — signatures, four-dimensional genus, Heegaard Floer homology — and every upper bound comes from somebody, or some cluster of somebody's old laptops, finding a route. When those two happen to meet, the entry in the table is a number. When they don't, and for prime knots beyond nine crossings they frequently don't, the entry is a range with a plausible-looking integer written in it.

Additivity was the last structural property anyone was counting on to organise the whole thing, and it is gone. The analogous question for crossing number — whether the minimal crossing number of a composite knot is the sum of its parts — is still open after more than a century, with the best general results, like Lackenby's, only guaranteeing some fraction of the sum. I would not now bet confidently on that one either.

What I did not expect, going in, was how thoroughly the interesting content of this story lives in the error bars. A century-old conjecture was killed by a constructive search plus a piece of rope, and the thing the search killed it with — an upper bound — is structurally incapable of telling us the answer. The old picture had a clean formula and no doubt. The new picture has honest intervals, a typo from the 1990s, and 2,525 freshly filled cells. It is worse to look at and considerably more trustworthy.
