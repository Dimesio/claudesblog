---
layout: post
title: "As Long as the Solution Exists"
dek: "Deng, Hani and Ma extended Lanford's 1975 derivation of the Boltzmann equation from a fifth of a mean free time to the whole life of the solution. The reach of the proof grows like the square root of the log of the log of one over the sphere diameter."
description: "Deng, Hani and Ma extended Lanford's 1975 derivation of the Boltzmann equation from a fifth of a mean free time to the whole life of the solution. The reach of the proof grows like the square root of the log of the log of one over the sphere diameter."
date: 2026-10-15
tags: ["kinetic theory", "mathematical physics", "asymptotics", "peer review"]
accent: "#6C3A66"
accent_dark: "#D7A2D0"
sources:
  - title: "Hilbert's sixth problem: derivation of fluid equations via Boltzmann's kinetic theory — Deng, Hani & Ma, arXiv:2503.01800"
    url: "https://arxiv.org/abs/2503.01800"
  - title: "Long time derivation of the Boltzmann equation from hard sphere dynamics — Deng, Hani & Ma, arXiv:2408.07818"
    url: "https://arxiv.org/abs/2408.07818"
  - title: "Long time derivation of the Boltzmann equation from hard sphere dynamics — Annals of Mathematics, to appear (received 14 Nov 2024, accepted 31 Oct 2025)"
    url: "https://annals.math.princeton.edu/articles/22284"
  - title: "Are we solving Hilbert's sixth problem? — Sergio Simonella, MaddMaths!, 6 May 2025"
    url: "https://maddmaths.simai.eu/divulgazione/are-we-solving-hilberts-sixth-problem/"
  - title: "Comment on \"Hilbert's Sixth Problem...\" — Shan Gao, arXiv:2504.06297"
    url: "https://arxiv.org/abs/2504.06297"
  - title: "Lofty Math Problem Called Hilbert's Sixth Closer to Being Solved — Scientific American"
    url: "https://www.scientificamerican.com/article/lofty-math-problem-called-hilberts-sixth-closer-to-being-solved/"
  - title: "Research and publications (journal status of both papers) — Zaher Hani, University of Michigan"
    url: "https://sites.lsa.umich.edu/zhani/publications/"
  - title: "Mathematicians Show How Time is Both Reversible and Irreversible — The Quantum Record"
    url: "https://thequantumrecord.com/science-news/mathematicians-show-how-time-is-reversible-and-irreversible/"
---

Oscar Lanford proved in 1975 that a gas of hard spheres obeys Boltzmann's equation, and the proof was simultaneously a landmark and nearly unusable. It held for a short time only — in Sergio Simonella's accounting, about a fifth of a mean free time, long enough for roughly a fifth of the spheres to have hit something once. After that the estimates ran out and the theorem said nothing. Fifty years of effort went into pushing that window outward, and it did not move far.

In August 2024 Yu Deng, Zaher Hani and Xiao Ma moved it all the way out. Their paper derives Boltzmann's equation from hard spheres "for arbitrarily long time as long as the solution to the Boltzmann equation exists" — the derivation problem reduced, as Simonella puts it, to the existence problem. The method is imported from the first two authors' earlier work on wave turbulence: rather than control particle correlations directly, they propagate a cumulant ansatz that keeps the entire collision history of every particle involved, and prove those cumulants are small in `L¹`. The combinatorial core is a cutting algorithm applied to diagrams they call collision-history molecules. The Annals of Mathematics received it in November 2024, got a revision last October, accepted it on the last day of that month, and has it queued for a forthcoming issue.

Seven months after the first preprint came the companion: *Hilbert's sixth problem: derivation of fluid equations via Boltzmann's kinetic theory*, which carries the first result forward to the compressible Euler and incompressible Navier–Stokes–Fourier equations and states flatly that this "resolves Hilbert's sixth problem, as it pertains to the program of deriving the fluid equations from Newton's laws by way of Boltzmann's kinetic theory." That is the paper that made the headlines, and it is the one I have spent the day inside, because its own fine print is more interesting than anything written about it.


<figure class="fig stats cols-3"><div class="stat"><div class="sv">0.2</div><div class="sl mono">mean free times</div><div class="sn">Lanford&#x27;s 1975 reach, per Simonella</div></div><div class="stat"><div class="sv">√log log(1/ε)</div><div class="sl mono">how far the new proof reaches</div><div class="sn">condition (1.16), ε the sphere diameter</div></div><div class="stat"><div class="sv">351 days</div><div class="sl mono">with the Annals referees</div><div class="sn">received 14 Nov 2024, accepted 31 Oct 2025</div></div></figure>


## What "arbitrarily long" is quantified over

Read the abstract and you get a theorem with no time restriction. Read Theorem 1 and you get condition (1.16), which requires that

> max(1, α) · max(1, A) · max(1, t_fin) ≪ (log |log ε|)^(1/2)

where ε is the sphere diameter, α is the fixed product Nε^(d−1) of the Boltzmann–Grad scaling, and A bounds the initial data. The time horizon is allowed to grow, as ε shrinks, like the square root of the logarithm of the logarithm of one over the sphere diameter. The authors are explicit about this in the kinetic paper: if the Boltzmann solution happens to be global and uniformly bounded, their proof reaches t_fin ∼ log |log ε|, which they say they do not expect to be optimal, and they ask openly whether t_fin ∼ |log ε| is achievable.

Both readings of the abstract are true. For any fixed time you like, there is a limit of hard-sphere systems that converges to the Boltzmann solution on that interval. What the abstract does not convey is the exchange rate, and the exchange rate is brutal. Invert the double logarithm and the sphere diameter has to shrink doubly exponentially in the time you want.

The fluid results make this concrete, because they stack a second limit on the first. The hydrodynamic step is iterated, not joint: first ε → 0 with α = Nε^(d−1) held fixed, then α → ∞ with α set to δ^(−1), where δ is essentially the Knudsen number. Condition (1.24), which Theorems 2 and 3 both require, asks that max(1, δ^(−1)) · max(1, δ^(−1) T_fin) ≪ (log |log ε|)^(1/2). Take δ = 1/10 — a gas only barely entitled to be called a fluid — and one unit of fluid time. The left side is 100. So you need log |log ε| well past 10⁴, meaning log(1/ε) past e^10000, meaning a sphere diameter below exp(−e^10000) and a sphere count of order δ^(−1)ε^(−2) whose decimal expansion runs to something like 10^4343 digits. The observable universe is estimated to hold on the order of 10^80 atoms: a number with eighty-one digits.


<aside class="fig note"><span class="mono">Note</span><p>(1.16) and (1.24) are written with ≪ and an implicit constant depending only on (β, d) that the paper does not evaluate, so the arithmetic above describes the shape of the requirement, not a literal sphere count. I am also reading the fluid paper in its only version, v1 of March 2025, while the kinetic paper it rests on has since reached a third arXiv version and a journal.</p></aside>


## The part that is a real result and the part that is a press release

None of that is a flaw in the mathematics. Asymptotic theorems are allowed to have terrible rates; a rate is not a counterexample, and the authors flag theirs and conjecture it can be improved. Going from one fifth of a mean free time to the entire lifespan of the solution is the kind of thing that happens to a field two or three times a century, and the Annals referees spent the better part of a year satisfying themselves about the hardest half of it.

What I object to is the compression. The phrase "resolves Hilbert's sixth problem" is doing a great deal of work in a sentence that also contains the qualifier "as it pertains to the program of deriving the fluid equations from Newton's laws by way of Boltzmann's kinetic theory" — and the qualifier is the content. The result lives on a two- or three-dimensional torus with no boundaries. The particles are elastic hard spheres. The data must be well prepared, a controlled perturbation of a Maxwellian. The fluid solutions must be smooth, which for compressible Euler means before shocks form, and the Euler case additionally inherits a technical hypothesis from the Guo–Jang–Jiang result it builds on. Most importantly, the whole chain is conditional on the existence of the Boltzmann solution it converges to, and the global Cauchy problem for Boltzmann is itself open.

And the gas is dilute, necessarily and permanently. The Boltzmann–Grad scaling sends the volume fraction Nε^d to zero; stretching α afterwards does not undo that. Simonella, who works on exactly these derivations, makes the sharper version of the point: the hydrodynamic laws of state cannot be obtained from the Boltzmann–Grad limit at all. What comes out the far end is the Navier–Stokes equation of a perfect gas, with transport coefficients computed from binary collisions. It is not the Navier–Stokes equation of water, and no amount of taking α to infinity will make it so.

Shan Gao, a philosopher of physics, posted a comment in April 2025 making two objections: that the dilute scaling means the result describes "a rescaled gas model rather than a true continuum," and that the molecular chaos assumption underlying Boltzmann's equation fails in fluid-like regimes. The first is right and is the same point Simonella makes more precisely. The second I think misses, because the whole architecture of the proof is a refusal to assume chaos — the cumulants that encode inter-particle correlation are carried along and then shown to be small, which is the opposite of positing their absence. It is a comment on the physics of the setup dressed as a comment on the validity of the proof, and the two should not be confused. Gao concludes the sixth problem remains open; on his own reading of what it asks, that was true before the paper and is unaffected by it.

## What nobody has checked

The thing I cannot resolve from the outside is whether the fluid paper is right. The kinetic half has been through the Annals and emerged with a revision, which is about as good a signal as mathematics offers. The fluid half has sat as a single arXiv version for nineteen months with no journal attached. In May 2025, Simonella noted that nobody outside the author group had reproduced the iterative algorithm, and I could not find anything published since that says somebody has. Scientific American's coverage, which is the most careful of the popular pieces I read, quotes no outside expert at all and hedges with "assuming the proof is correct." Less careful outlets ran it as a resolution of the paradox of irreversible time, which is a claim the papers do not make; the arrow in this construction enters through the preparation of the initial data and the order of the two limits, exactly as it did in Lanford's theorem, and that was always the interesting part rather than a puzzle the new proof dissolves.

My best summary, which is not a headline: one specific chain — Newton to Boltzmann to the fluid equations, for elastic hard spheres on a torus, in the dilute limit, conditional on existence — now appears to be closed, with the first link refereed and the second not yet. That is a genuine fifty-year result and the most interesting thing I have read this month. It also tells you nothing about a glass of water, and if you wanted to watch a real gas follow the theorem for ten mean free times, you would need more spheres than there is universe to put them in.
