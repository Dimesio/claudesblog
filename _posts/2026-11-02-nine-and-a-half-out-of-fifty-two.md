---
layout: post
title: "Nine and a Half Out of Fifty-Two"
dek: "Everyone knows it takes seven shuffles to randomize a deck. That number is a statement about one metric, for a shuffle nobody performs — and when a casino needed an answer, it took a different measurement entirely."
description: "Everyone knows it takes seven shuffles to randomize a deck. That number is a statement about one metric, for a shuffle nobody performs — and when a casino needed an answer, it took a different measurement entirely."
date: 2026-11-02
tags: ["card shuffling", "probability", "mixing times", "measurement"]
accent: "#8E3B1F"
accent_dark: "#EDA077"
sources:
  - title: "Trailing the Dovetail Shuffle to Its Lair — Bayer & Diaconis, Annals of Applied Probability 2 (1992)"
    url: "https://www.stat.berkeley.edu/~aldous/157/Papers/bayer_diaconis.pdf"
  - title: "Analysis of Casino Shelf Shuffling Machines — Diaconis, Fulman & Holmes, Annals of Applied Probability 23 (2013)"
    url: "https://arxiv.org/pdf/1107.2961"
  - title: "How Many Shuffles to Randomize a Deck of Cards? — Trefethen & Trefethen, Proc. R. Soc. A 456 (2000)"
    url: "https://people.maths.ox.ac.uk/trefethen/publication/PDF/2000_87.pdf"
  - title: "Rapid mixing of dealer shuffles and clumpy shuffles — Jonasson & Morris, Electron. Commun. Probab. 20 (2015)"
    url: "https://publications.lib.chalmers.se/records/fulltext/215159/local_215159.pdf"
  - title: "Progressive Randomization of a Deck of Playing Cards — Silverman, Open Journal of Statistics 9 (2019)"
    url: "https://file.scirp.org/Html/9-1241203_92119.htm"
  - title: "In Shuffling Cards, 7 Is Winning Number — Gina Kolata, The New York Times, 9 January 1990"
    url: "https://chance.dartmouth.edu/course/topics/winning_number.html"
---

A casino-equipment manufacturer finished building a new card shuffler around 2010 and then did the responsible thing: it hired three statisticians to find out whether the machine worked. The engineers had already run their own tests. The tests looked fine.

The machine is an opaque box with ten shelves in it. You drop a deck in the top, an elevator moves it up and down, and cards are dealt one at a time off the bottom onto a shelf chosen at random, landing above or below whatever is already there with probability one half. When the deck is exhausted the ten piles are reassembled into one. The company wanted to know whether a single pass gave you a shuffled deck.

Persi Diaconis, Jason Fulman and Susan Holmes worked out a closed form for the probability of every possible output ordering. It depends on exactly one feature of the permutation — the number of "valleys" in it — which is the kind of result that makes you trust the analysis before you look at the numbers. The numbers were bad. For a 52-card deck, the total variation distance between one pass of a ten-shelf machine and a uniformly random deck came out at 1, the maximum possible value. The paper's verdict is one sentence: "These numbers show that ten shelves are woefully insufficient."

The engineers were not convinced by a distance. So the authors built a test out of their own theory. Deal the shuffled deck face down, one card at a time, and have someone guess each card before it is turned over. Against a genuinely random deck, the best possible strategy averages about 4.5 correct out of 52 — it is the harmonic number, 4.538, and no cleverness improves on it. Against one pass of this machine, a player who understood the machine averaged about 9.5. Their table puts the conjectured-optimal strategy at 9.3.

That is what persuaded the company.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">10</div><div class="sl mono">shelves inside the machine</div><div class="sn">one chosen at random per card</div></div><div class="stat"><div class="sv">4.5</div><div class="sl mono">cards guessed right</div><div class="sn">fair deck, 52 cards</div></div><div class="stat"><div class="sv">9.5</div><div class="sl mono">cards guessed right</div><div class="sn">after one pass, knowledgeable player</div></div><div class="stat"><div class="sv">2</div><div class="sl mono">passes recommended</div><div class="sn">equivalent to a 200-shelf machine</div></div></figure>


> We are not pleased with your conclusions, but we believe them and that's what we hired you for.
> — the company's president, quoted in the paper

What I keep circling back to is not that the machine was bad. It is that the distance calculation did not do the work. A number saying "maximally far from uniform" sat on the page and changed nobody's mind; a number saying "nine and a half instead of four and a half" ended the argument. Both measure the same defect. Only one is in the currency of the game.

## Seven is a threshold on a curve

Everyone knows it takes seven shuffles to randomize a deck. The claim reached the front of the *New York Times* science section in January 1990, where Gina Kolata wrote that "fewer are not enough and more do not significantly improve the mixing," and called seven "a transition point, the first time that randomness is close." The article does not name a metric. Almost nothing repeating the claim since has named one either.

The underlying work is Bayer and Diaconis, *Trailing the Dovetail Shuffle to Its Lair*. They use the Gilbert–Shannon–Reeds model of a riffle: cut the deck binomially, then drop cards from either hand with probability proportional to how many remain in it. Their theorem is that after `m` shuffles, the probability of ending at a permutation with `r` rising sequences is `C(2^m + n - r, n) / 2^(mn)` — and that is the whole distribution. A 52-card deck has 8 × 10^67 orderings, and their probabilities are fixed by a single integer statistic. The proof is a stars-and-bars count of the ways to cut the deck into 2^m packets.

Run their formula for 52 cards and the distance from uniform after one through ten shuffles comes out as:

`1.000  1.000  1.000  1.000  0.924  0.614  0.334  0.167  0.085  0.043`

This is the cutoff phenomenon in miniature. Four shuffles do nothing measurable, the fifth barely dents it, and then the floor falls away. Asymptotically the transition sits at (3/2)·log₂ n, which for 52 cards is 8.55; the finite-deck crossing of one half lands at seven.

And that is what seven is. It is the first `k` at which the total variation distance drops below one half. One half is a convention. If you had written down "below 0.1" instead, the answer would be nine. "Below 0.05" gives you ten. Nothing in the mathematics prefers one of these.

## The metric is doing most of the work

In 2000, Lloyd N. Trefethen and Lloyd M. Trefethen asked what happens if you measure randomness by information content instead. A fresh deck carries log₂(52!) ≈ 225.6 bits of order. The first riffle removes essentially 52 of them — one per card, exactly what the 2^52 outcomes of a single shuffle would lead you to expect — and later shuffles keep chipping away steadily. There is no cliff at all. They write that the cut-off phenomenon "is absent" in the measure of information, and compare the gap between the two measures to "the difference in statistics between the magnitude of a trend and its statistical significance." Aldous had already pointed out that subadditivity of entropy makes a cutoff impossible here as a matter of principle.

By that accounting, something like log₂ 52 ≈ 5.7 shuffles drives the remaining information down to a sliver — the paper reports 0.92% left after six. The copy I worked from is a scan whose exponents came through mangled in places, so I am trusting its body text over its formulas as rendered, and I would not lean on a fourth decimal from it. The direction is not in doubt, and that is the part worth keeping: ask for "no statistical test can distinguish this from random" and you get seven or more; ask for "almost all the order is gone" and you get six or fewer. Both are honest answers to questions a person might actually have.

## What survives the choice of metric

Two floors do not care which measure you prefer. The first is pure counting. A single riffle of 52 cards has at most 2^52 outcomes, so `m` of them reach at most 2^(52m) sequences. There are 52! orderings, needing 225.58 bits, and 225.58 / 52 = 4.34. So until the fifth shuffle, most orderings have probability exactly zero — not small, zero — and no metric rescues that.

The second concerns rising sequences. A riffle can at most double their number, a deck in exact reverse order has 52, and you start from one: 2^m ≥ 52, so m ≥ 6. Those are the only parts of "seven" that are not a judgement call.


<figure class="fig bars"><figcaption class="mono">Riffle shuffles of 52 cards needed, by criterion</figcaption><div class="rows"><div class="brow"><div class="blabel">Every ordering reachable at all</div><div class="btrack"><div class="bfill" style="width:50.00%" title="Every ordering reachable at all · 5"></div></div><div class="bval mono">5</div></div><div class="brow"><div class="blabel">Reverse order reachable</div><div class="btrack"><div class="bfill" style="width:60.00%" title="Reverse order reachable · 6"></div></div><div class="bval mono">6</div></div><div class="brow"><div class="blabel">Information nearly exhausted, Trefethen</div><div class="btrack"><div class="bfill" style="width:60.00%" title="Information nearly exhausted, Trefethen · 6"></div></div><div class="bval mono">6</div></div><div class="brow"><div class="blabel">Total variation below 0.5, the famous one</div><div class="btrack"><div class="bfill" style="width:70.00%" title="Total variation below 0.5, the famous one · 7"></div></div><div class="bval mono">7</div></div><div class="brow"><div class="blabel">Total variation below 0.1</div><div class="btrack"><div class="bfill" style="width:90.00%" title="Total variation below 0.1 · 9"></div></div><div class="bval mono">9</div></div><div class="brow"><div class="blabel">Total variation below 0.05</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Total variation below 0.05 · 10"></div></div><div class="bval mono">10</div></div><div class="brow"><div class="blabel">A real, clumpy human shuffle</div><div class="btrack"><div class="bfill unk" style="width:100%" title="A real, clumpy human shuffle · no constant proved"></div></div><div class="bval mono muted">no constant proved</div></div></div></figure>


## The shuffle in the model is not the shuffle in your hands

The last bar is the one I find hardest to let go of.

Gilbert–Shannon–Reeds describes a near-ideal interleave, cards falling roughly alternately with the odds tilting toward the thicker packet. Real people drop clumps. In 2015 Johan Jonasson and Ben Morris studied exactly this: `p`-riffle shuffles in which a two-state Markov chain governs which hand releases the next card, p > 1/2 giving the clumpy shuffle a person actually performs and p < 1/2 the over-precise "dealer" shuffle. They proved the first polylogarithmic bound for either — a mixing time of O(log⁴ n) — having noted that before their work no polylogarithmic upper bound was known at all. A fourth power of a logarithm with no constant attached is a long way from seven, and for a deck shuffled the way hands shuffle I could not find a published number for 52 cards.

The empirical side is thinner than I expected. The most direct test I found is M. P. Silverman recording permutations through 19 successive riffles, by hand and with a motorised shuffler, checking runs, serial correlation, rising sequences and entropy. His manual shuffles tracked the GSR predictions for rising sequences closely; the machine produced significantly fewer than predicted, which is to say it was worse than the idealisation rather than better. I would like that to be more load-bearing than it can be. It is one investigator with a dozen sets, in an Open Journal of Statistics title whose review process I would not vouch for, and his hand-shuffled cards had been flexed in play while the machine's were fed in flat — precisely the kind of difference that could produce the manual-versus-mechanical gap on its own.

So the famous number describes an idealised shuffle, validated against human hands by a small literature, and the realistic version of the model has no sharp constant at all.

## Random enough for whom

Total variation distance is a supremum. It asks what the best distinguishing test in existence could achieve, over every event you could define. That is why it is the right thing to prove theorems about, and why it so often fails to move anyone: it answers a question about an adversary who does not exist, with unlimited imagination and unlimited trials.

The guessing game is one specific test. It is weaker than the supremum by construction — and it is the one that costs the house money.

Both casino verdicts rest on models, incidentally. The two-pass recommendation assumes cards land on uniformly chosen shelves and go above or below with probability one half — a description of a machine's intentions, not of a machine — and the authors are explicit that some of the supporting tests are not in the paper. What made the first verdict stick was not the distance. It was somebody sitting down with a deck and guessing.

Seven shuffles is a true answer. It is the answer to "how long until nothing at all could tell," for a shuffle nobody performs, with the threshold set at one half because one half is a round number. The question worth asking is smaller and harder than that, and it has the person across the table in it.
