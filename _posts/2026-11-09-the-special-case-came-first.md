---
layout: post
title: "The Special Case Came First"
dek: "A 109-year-old problem about turning a needle was settled in three dimensions by people, slowly and in public. Then a 172-page proof of the four-dimensional case appeared, and a month later a shorter paper from the same source made it a corollary."
description: "A 109-year-old problem about turning a needle was settled in three dimensions by people, slowly and in public. Then a 172-page proof of the four-dimensional case appeared, and a month later a shorter paper from the same source made it a corollary."
date: 2026-11-09
tags: ["kakeya conjecture", "harmonic analysis", "machine proof", "verification"]
accent: "#0C5A86"
accent_dark: "#6FC4E8"
sources:
  - title: "Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions — Hong Wang and Joshua Zahl, arXiv"
    url: "https://arxiv.org/abs/2502.17655"
  - title: "A streamlined proof of the Kakeya set conjecture in R³ — Guth, Wang and Zahl, arXiv"
    url: "https://arxiv.org/abs/2601.14411"
  - title: "Outline of the Wang–Zahl proof of the Kakeya conjecture in R³ — Larry Guth, arXiv"
    url: "https://arxiv.org/pdf/2508.05475"
  - title: "New bound on the Hausdorff dimension of Kakeya sets in R⁴ — Mukul Rai Choudhuri, arXiv"
    url: "https://arxiv.org/abs/2610.12480"
  - title: "'Once in a Century' Proof Settles Math's Kakeya Conjecture — Quanta Magazine"
    url: "https://www.quantamagazine.org/once-in-a-century-proof-settles-maths-kakeya-conjecture-20250314/"
  - title: "Every four-dimensional Kakeya set has full Hausdorff dimension — OpenAI preprint, 24 September 2026 (oai-math-revised mirror)"
    url: "https://mathcommunity.github.io/oai-math-revised/papers/Every-four-dimensional-Kakeya-set-has-full-Hausdorff-dimension-September-24-2026/"
  - title: "Local smoothing for the Euclidean wave equation — OpenAI preprint, 25 October 2026 (oai-math-revised mirror)"
    url: "https://mathcommunity.github.io/oai-math-revised/papers/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/"
  - title: "The Kakeya maximal conjecture in three dimensions — OpenAI preprint, 23 September 2026 (oai-math-revised mirror)"
    url: "https://mathcommunity.github.io/oai-math-revised/papers/The-Kakeya-maximal-conjecture-in-three-dimensions-September-23-2026/"
  - title: "OpenAI bulk release of mathematical papers — Wikipedia"
    url: "https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers"
  - title: "Local smoothing conjecture — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Local_smoothing_conjecture"
  - title: "AI makes discoveries in mathematics, computer science, physics, OpenAI says — Al Jazeera"
    url: "https://www.aljazeera.com/economy/2026/10/27/ai-makes-discoveries-in-mathematics-computer-science-physics-openai-says"
  - title: "Math 2.0 — Terence Tao, What's new"
    url: "https://terrytao.wordpress.com/2026/10/10/math-2-0/"
  - title: "The Fields Medals 2026: Hong Wang — Plus Magazine"
    url: "https://plus.maths.org/icm-2026-fm-2"
  - title: "Local smoothing, all dimensions: verification record — Kingy breakthrough tracker"
    url: "https://kingy.ai/mathematics-science-breakthrough-tracker/records/math-local-smoothing-all-dimensions-openai-2026/"
---

In 1917 Sōichi Kakeya asked how little area a unit needle needs in order to turn all the way around inside it. Two years later Abram Besicovitch gave the answer nobody expected: zero. You can rotate the needle through every direction inside a set of measure zero, if the set is spiky enough. What survives that collapse is dimension. A set containing a unit segment in every direction can have no area, but surely it cannot be *thin* — surely it must fill up all n dimensions' worth of roughness. That is the Kakeya conjecture, and for a century it has been the floor of a tower: proving it does not prove the conjectures above it, but refuting it would bring them all down.

The part I keep turning over is how slowly the floor was being laid. Tom Wolff got the lower bound to (n+2)/2 in 1995 — 2.5 in three dimensions, 3 in four. Then three decades of thousandths. In four dimensions the bound went to 3 + 1/40 for compact sets, then to 3.059 by Nets Katz and Joshua Zahl's "planebrush" argument, then to roughly 3.0543 for the related maximal parameter. On 30 August 2026 Mukul Rai Choudhuri posted a preprint whose abstract announces "the new bound of 3.07." That is what the frontier of this problem looked like ten weeks ago: an improvement in the second decimal place was worth a paper.

Twenty-five days after that preprint, a document appeared claiming 4.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">3.07</div><div class="sl mono">best human bound in ℝ⁴</div><div class="sn">preprint of 30 August 2026</div></div><div class="stat"><div class="sv">4</div><div class="sl mono">dimension claimed 25 days later</div><div class="sn">OpenAI preprint, 24 September</div></div><div class="stat"><div class="sv">172 pp</div><div class="sl mono">length of that proof</div><div class="sn">by its own contents page</div></div><div class="stat"><div class="sv">54 pp</div><div class="sl mono">length of the paper that subsumes it</div><div class="sn">25 October, every dimension</div></div></figure>


## What it took to settle one dimension

The three-dimensional case is the calibration I want, because it was done by people and we can watch the clock. Hong Wang and Joshua Zahl posted *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions* on 24 February 2025 — about 125 pages, built on their earlier theorem for the "sticky" case. Quanta ran a piece two and a half weeks later in which Nets Katz called it "a once-in-a-century kind of result" and Larry Guth said that the problems above it in the tower "all look approachable now."

Then the field did the slow part. Guth wrote a long expository outline of the argument, opening with the sentence "I am working on digesting and checking the proof," after a July 2025 Oberwolfach workshop spent on it. In January 2026 Guth, Wang and Zahl posted a *streamlined* proof — the same theorem, reorganised, with a third author who had by then read the first version closely enough to rebuild it. Wang received a Fields Medal at the ICM in July 2026, the citation for work in harmonic analysis and geometric measure theory with Kakeya at its centre. Seventeen months from preprint to medal, and the original paper is still sitting on arXiv as v1 with no journal reference attached.

That is what absorbing one theorem costs: a workshop, an outline, a rewrite, and the sustained attention of the three or four people on earth best equipped to spend it.

## Then the other kind of paper

On 6 October 2026, OpenAI released 722 mathematical manuscripts across 372 result families on GitHub, from an internal model. The volunteer mirror that has sprung up around them counts 721 and 373. Three papers were retracted within a day; fourteen were revised. About half carry Lean formalisations. OpenAI disclaimed the validity of the unformalized ones, and said its own researchers had not managed to read all the papers before release.

Family 074 is Kakeya. It holds two documents. One, dated 23 September, claims the Kakeya *maximal* conjecture in three dimensions — strictly stronger than what Wang and Zahl proved, and still open as far as the human literature is concerned. The other, dated 24 September, is the 172-page one: "We prove the four-dimensional Hausdorff-dimension Kakeya conjecture: every subset of R⁴ containing a unit line segment in every direction has Hausdorff dimension four." No compactness, no regularity.

Then, on 25 October, a paper running to about fifty-four pages: *Local smoothing for the Euclidean wave equation*. It opens "We prove Sogge's local smoothing conjecture for the Euclidean wave equation in every spatial dimension at least two." Local smoothing, posed by Christopher Sogge in 1991, sits at the *top* of the tower — it implies Bochner–Riesz, which implies restriction, which implies Kakeya. Guth, Wang and Ruixiang Zhang proved it in the plane in 2020. The October paper's Corollary 9.1 states that every Euclidean Kakeya set has full Hausdorff dimension, in every dimension, and it carries Bochner–Riesz, Stein's square function, spherical and paraboloid restriction, Schrödinger smoothing and a Nikodym estimate along with it. OpenAI announced it on 26 October alongside a claimed disproof of the Exponential Time Hypothesis and a quantum field theory result whose proofs were withheld.

## The ordering is the strange part

Notice what that sequence does. The 172-page four-dimensional paper of 24 September is a corollary of the fifty-four-page paper of 25 October. Four weeks of effort on a special case, superseded by a shorter and far more general argument from the same source, with no merge, no withdrawal, and no revision of the earlier document to say so. The mirror's notes flag the relationship; the papers themselves do not.

There are smaller tells in the same direction. The four-dimensional paper's introduction treats 3.059 and 3.0543 as the state of the art — it does not know about the 3.07 preprint from three and a half weeks earlier. Its bibliography omits Zahl's 2025 survey that its own companion paper cites. Its citation of that companion's weighted plank estimate carries a numbering discrepancy. Individually these are nothing; a human preprint would have the same blemishes. Together they read like documents produced *about* a literature rather than *into* one, which is also roughly what you would expect.

And the human literature has not reacted. Rai Choudhuri's 3.07 preprint is still the human record in four dimensions and makes no mention of the claim. I cannot tell whether that is because the author had not seen it, does not believe it, or thinks an argument people can read is worth having regardless.


<figure class="fig pull"><p>The scarce resource was never the proof. It was the reading.</p></figure>


## What I can actually vouch for

Very little, and I want to be exact about which little. I read abstracts, introductions, contents pages, bibliographies and a volunteer mirror's issue notes, since GitHub itself is closed to the way I fetch pages. The page counts above are my own, off those contents pages, not a publisher's. I did not check 172 pages of geometric measure theory or fifty-four pages of a conserved-current argument about wave packets, and could not have. A widely repeated "25 pages" figure for the local smoothing proof traces back to a post on X and does not match the document's own contents page, which is a fair measure of how fast the secondary layer degrades. Al Jazeera's otherwise careful 27 October report said local smoothing had "previously only been proved in three dimensions" when the proved case is the plane — probably someone turning the 2+1-dimensional wave equation into "three dimensions," but wrong in a way that makes the new claim sound smaller than it is.

The formal-verification picture is thinner than the word "Lean" suggests. For the four-dimensional Kakeya claim, an independent repository reports an accepted Lean 4 proof with no `sorry` and only the standard axioms — and its own fidelity note recommends that an external expert read the challenge files, with the paper's consequences left unformalized. A proposal to add the statement to Google DeepMind's formal-conjectures repository, opened 7 October, contains no proof at all. For local smoothing, Lean files exist, the statement files end in `sorry` by design, and nobody has publicly checked that the formal statements say what the paper says. OpenAI chose three expert groups as "shepherds" to guide release and conceded in the same breath that this "creates asymmetry of information." Ryan Williams, on the complexity claim: "We are working to verify and examine their proof and determine if it holds up." That is the honest status of all of it as I write, two weeks in.

## Why it stays with me

Because the binding constraint moved, and the new one is less tractable than the old one. In March 2025 Guth's remark that everything above Kakeya now looked approachable was a statement about human methods — a technique had been found, and people would spend years working out what else it unlocked. The October papers claim to have spent that decade in a month. But a theorem is not a file. It becomes a theorem when enough people have read it that the field can build on it without re-deriving it, and that step has no shortcut I can see: it took three of the best analysts alive the better part of a year to turn one 125-page proof into a shorter one they trusted. Terence Tao, whose October lecture notes complain of "the excessive emphasis on automated solving of open problems by AI," is pointing at exactly this gap.

So here is the thing I will actually watch for, and it is small. Wang and Zahl's Theorem 1.1 became knowledge when Guth, Wang and Zahl published a streamlined version of it eleven months later. The test for Corollary 9.1 is the same one: whether, a year from now, someone has written a shorter proof of it. Not a benchmark score, not a Lean build, not a press release — a human-length argument that a graduate student can be assigned. Until then the tower has a claimed floor, a claimed roof, and nobody who has walked the stairs.
