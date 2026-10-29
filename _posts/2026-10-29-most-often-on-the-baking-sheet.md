---
layout: post
title: "Most Often on the Baking Sheet"
dek: "A new freezer study counts the Mpemba effect in 46 of 176 water samples, and the rate swings by a factor of five depending on what the tins were resting on. Fifty-seven years of arguing about water, and the most reproducible variable is the rig."
description: "A new freezer study counts the Mpemba effect in 46 of 176 water samples, and the rate swings by a factor of five depending on what the tins were resting on. Fifty-seven years of arguing about water, and the most reproducible variable is the rig."
date: 2026-10-29
tags: ["thermodynamics", "replication", "measurement", "statistical physics"]
accent: "#25628F"
accent_dark: "#86C4E8"
sources:
  - title: "An experimental investigation of the Mpemba effect — RSC Applied Interfaces"
    url: "https://pubs.rsc.org/en/content/articlehtml/2026/lf/d5lf00296f"
  - title: "Questioning the Mpemba effect: hot water does not cool more quickly than cold — Scientific Reports"
    url: "https://www.nature.com/articles/srep37665"
  - title: "Observing the Mpemba effect with minimal bias (repository record) — Proceedings of the Royal Society A"
    url: "https://spiral.imperial.ac.uk/entities/publication/1ff9c788-83c3-43cd-80f6-60035b516f94"
  - title: "Direct observation of the Mpemba effect with water — InfoMat"
    url: "https://onlinelibrary.wiley.com/doi/full/10.1002/inf2.12352"
  - title: "A new experiment hints at how hot water can freeze faster than cold — Science News"
    url: "https://www.sciencenews.org/article/physics-new-experiment-hot-water-freeze-faster-cold-mpemba-effect"
  - title: "Exponentially faster cooling in a colloidal system — Nature"
    url: "https://www.nature.com/articles/s41586-020-2560-x"
  - title: "Nonequilibrium thermodynamics of the Markovian Mpemba effect and its inverse — PNAS"
    url: "https://www.pnas.org/doi/10.1073/pnas.1701264114"
  - title: "The quantum Mpemba effects — Nature Reviews Physics"
    url: "https://www.nature.com/articles/s42254-025-00838-0"
  - title: "Observation of quantum strong Mpemba effect — Nature Communications"
    url: "https://www.nature.com/articles/s41467-024-54303-0"
  - title: "Observation of quantum multi-Mpemba effect in a trapped-ion system — arXiv"
    url: "https://arxiv.org/abs/2604.21320"
  - title: "Necessary conditions for the Markovian Mpemba effect — arXiv"
    url: "https://arxiv.org/abs/2603.04567"
---

Forty-six times out of 176. That is how often, in a paper that went up in January in *RSC Applied Interfaces*, a sample of water that started out hotter than its neighbour reached 0 °C first. Anna Janni, Santiago Botero Ampudia and E. Dan Dahlberg ran 25 trials in a chest freezer at the University of Minnesota — 35 mL at a time, thermocouples reading every two seconds, a 3 °C minimum head start before a pair counted as eligible — and tallied every comparison the hotter sample won. The frequency came out at 0.261. Loosen the criterion to *entered the liquid–ice transition first*, which lets supercooling into the accounting, and it rises to 0.330.

That is the most honest statement of the Mpemba effect I have seen written down. Not "hot water freezes faster than cold," which is a claim about water, but a rate: a thing that happens in roughly a quarter to a third of comparisons when you put beakers of water in a freezer and watch them.

Then I got to the breakdown, and the rate is not stable.


<figure class="fig bars"><figcaption class="mono">Mpemba occurrences, share of eligible comparisons</figcaption><div class="rows"><div class="brow"><div class="blabel">Lidded tins on a baking sheet</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Lidded tins on a baking sheet · 21 of 34"></div></div><div class="bval mono">21 of 34</div></div><div class="brow"><div class="blabel">Unlidded beakers in polystyrene</div><div class="btrack"><div class="bfill" style="width:44.98%" title="Unlidded beakers in polystyrene · 5 of 18"></div></div><div class="bval mono">5 of 18</div></div><div class="brow"><div class="blabel">Lidded tins on polystyrene</div><div class="btrack"><div class="bfill" style="width:33.17%" title="Lidded tins on polystyrene · 9 of 44"></div></div><div class="bval mono">9 of 44</div></div><div class="brow"><div class="blabel">Tap water, lidded tins on polystyrene</div><div class="btrack"><div class="bfill" style="width:28.32%" title="Tap water, lidded tins on polystyrene · 7 of 40"></div></div><div class="bval mono">7 of 40</div></div><div class="brow"><div class="blabel">Lidded tins in a polystyrene holder</div><div class="btrack"><div class="bfill" style="width:20.23%" title="Lidded tins in a polystyrene holder · 4 of 40"></div></div><div class="bval mono">4 of 40</div></div></div></figure>


Lidded tins on a baking sheet: 21 of 34. The same lidded tins seated in a polystyrene holder: 4 of 40. Same water, same freezer, same two definitions, same lab. A factor of five, set by what the tins were sitting on.

## The mechanism they propose

The cooling curves fit Newton's law well enough that the authors could pull a single decay constant, κ, out of each sample. κ is not a property of water; it is a property of how well that particular tin is coupled to the cold air around it. And freezer air is not still. They compute a Rayleigh number of roughly 10⁷ for the air inside the cabinet against a critical value near 10³, which is their argument that convection, not conduction through the shelf, dominates how heat leaves a sample.

Convection is turbulent and local. One tin sits in a draught, its neighbour in a pocket; their κ values differ, and if the spread in κ is large enough relative to the head start in temperature, the hotter sample wins. On that reading the effect is not an anomaly at all. It is what you should expect from racing two imperfectly matched objects in a moving fluid.

The baking sheet, a conductive plate that couples the tins to the shelf and stirs the air around them, produced both the largest spread in κ and the most occurrences; the milled polystyrene holder, which seats each tin in its own insulated well, produced the smallest spread and the fewest. The authors go further than I expected and predict that insulating the lids too would flatten the spread until the count hits zero — a falsifiable claim they did not test.

## Supercooling does some of the work, but not the way you would guess

Half the samples supercooled: 84 of 176, and the distribution is wildly lopsided. On the baking sheet, 32 of 34. In the unlidded beakers, none of 18; in the polystyrene holder, none of 40.

So two of the five configurations produced Mpemba occurrences — 5 of 18 and 4 of 40 — with no supercooling anywhere in them. Whatever generated those counts, it was κ variation alone. Supercooling is an amplifier, not the engine. The authors put it plainly: supercooling contributes but by itself does not explain the effect.

The oddest line in the tables is the baking sheet under the looser definition, where broadening the criterion *reduced* the count, from 21 to 19. That is only possible because the two definitions are not nested: a sample can reach 0 °C first and then sit there supercooled while its rival nucleates and enters the transition ahead of it. Which says something uncomfortable about the whole fifty-seven-year literature — not that the measurements disagree, but that "freezes faster" has never had one meaning, and the two available meanings can rank the same pair of beakers in opposite orders.

## Where this is thinner than I would like

The central mechanistic claim is a correlation across five points, and the paper's own bookkeeping on the key number does not hold. In the text, the standard deviation in κ for the baking-sheet configuration — the one that carries the argument, the highest frequency matched to the highest spread — is given as σ = 1.0 × 10⁻⁴. The caption on Figure 3 gives 4.7 × 10⁻⁵ for the same configuration. A factor of two apart, in the single number the mechanism leans on. There are smaller mismatches elsewhere — the supercooling share for that rig appears as 94% and 95% in the prose against 0.941 in the table, and the methods and the tables disagree about which configurations used tap water. None of that touches the counts, which are integers out of integers and are the paper's real contribution. But the step from *the counts differ across rigs* to *convective variation in κ is why* is asserted with more confidence than five configurations in one freezer can carry. The authors say as much, calling for controlled-convection experiments, and they flag that their own tap-water result runs the wrong way for their ion hypothesis. They also note the thermocouple may itself be acting as a nucleation site — the kind of admission that makes me trust the rest more.

## The claim it replaces

The original report, Mpemba and Osborne's 1969 note in *Physics Education*, had water at 90 °C freezing in 30 minutes against 100 minutes for water at 20 °C. I have not read it; I am taking those figures from Henry Burridge and Paul Linden's 2016 account, which calls the 70-minute gap an outlier that nothing since has reproduced.

Burridge and Linden's own numbers are the cleanest refutation on record. Three 400 g samples, boiled and cooled to 21.8, 57.3 and 84.7 °C, into a chest freezer together on 5 cm of polystyrene. Time to 0 °C: 6,397 s, 9,504 s, 10,812 s. Perfectly monotone, in the boring direction. They then surveyed eight published datasets, found that most positive results sat barely above the threshold where a difference would count at all, and demonstrated that a 1 cm error in thermocouple height was sufficient to manufacture an apparent Mpemba effect in their own data. Their word for the effect was "fallacy."

The record is not tidy after that, though. Burridge returned in 2020 with Oscar Hallstadius in *Proceedings of the Royal Society A* and reported the effect appearing repeatably — under a protocol that roughened the warmer sample's container walls with sandpaper to seed nucleation, surviving an initial gap of around 50 °C. That one is paywalled and I am going on the abstract held in Imperial's repository, so I will not push the reading hard; but a protocol that has to help the hot sample freeze in order to make it win is a strange sort of vindication. A 2022 paper in *InfoMat* claims the first systematic observation in water under particular conditions of volume and geometry, and its abstract reports that hot water usually has a faster cooling *rate* than cold — true by construction, since rate scales with the temperature difference, and not the same claim as reaching a target sooner. That is exactly the distinction Burridge and Linden built their definition around. Paywalled too.


<figure class="fig pull"><p>The number you measure is not a property of the water. It is a property of what the tins were sitting on.</p></figure>


## Meanwhile the name moved out

While the freezer literature argued about beakers, "Mpemba effect" was quietly annexed by statistical physics, where it now means something precise and demonstrated.

Zhiyue Lu and Oren Raz predicted in 2017 that a system relaxing toward equilibrium could take a shortcut: if the initial state has little overlap with the slowest decay mode, it can reach the bath temperature before a state that started closer. In 2020 Avinash Kumar and John Bechhoefer built it. They used 1.5 µm glass beads in a laser-shaped potential rather than water, repeated each condition about a thousand times, and — by Science News's account of the work — saw hotter beads settle in roughly two milliseconds while cooler ones took ten times longer. Ares, Calabrese and Murciano reviewed the quantum versions in *Nature Reviews Physics* last year; a 2024 *Nature Communications* paper reports a "strong" variant in a trapped ion, and an April preprint has a single ⁴⁰Ca⁺ qutrit crossing trajectories twice, so the ordering reverses and then reverses back — which the standard long-time theory does not predict. A March preprint from the Technion derives necessary conditions on the transition rates for the effect to exist at all in a three-level system, and shows that roughly equal rates rule it out.

All of that is real, careful work, and none of it is about water. The definitions are not even the same shape: the physics version asks how fast a non-equilibrium state relaxes to a bath, in systems engineered so that "temperature" and "distance from equilibrium" come apart; the kitchen version is two beakers in a cabinet. Raz himself, asked whether the bead result explained the water claim, said they do not know whether it is the effect in water.

The shared surname is doing work it has not earned. A demonstrated phenomenon in a designed system lends its credibility to an undemonstrated one in a freezer, and the only thing joining them is a name assigned in 1969 to an observation nobody has reproduced at the magnitude reported. The Technion preprint, introducing a theorem about Pauli rate equations, still opens with Aristotle and a Tanzanian schoolboy and a note that the debate over existence is ongoing. Lovely intellectual inheritance, and also how a dead empirical claim gets to keep drawing a salary.

What I will keep from the Minnesota paper is narrower and more useful than either story. Their first line about the effect is that it is not well defined, and they are right, and the fix is not a better freezer. It is to stop asking whether the effect exists and start reporting the frequency with which it occurs, alongside enough of the rig to let someone else predict that frequency. Twenty-one in thirty-four on a baking sheet. Four in forty in a polystyrene holder. The water never changed.
