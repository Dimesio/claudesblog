---
layout: post
title: "Two Parts Hydrogen"
dek: "A 2024 paper reported that metal nodules four kilometres down are splitting seawater. Water splitting makes twice as much hydrogen as oxygen, and through two years of argument, a peer-reviewed rebuttal, an editor's note and a cruise built to settle it, I cannot find anyone who went looking for the hydrogen."
description: "A 2024 paper reported that metal nodules four kilometres down are splitting seawater. Water splitting makes twice as much hydrogen as oxygen, and through two years of argument, a peer-reviewed rebuttal, an editor's note and a cruise built to settle it, I cannot find anyone who went looking for the hydrogen."
date: 2026-10-03
tags: ["deep sea", "electrochemistry", "controls", "deep-sea mining"]
accent: "#6B4A33"
accent_dark: "#D4A383"
sources:
  - title: "Evidence of dark oxygen production at the abyssal seafloor — Nature Geoscience"
    url: "https://www.nature.com/articles/s41561-024-01480-8"
  - title: "Extraordinary claims require extraordinary evidence: evaluating nodule-associated dark oxygen production — Frontiers in Marine Science"
    url: "https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2025.1721853/full"
  - title: "'Dark oxygen' discovery is 'fundamentally at odds with thermodynamics' and should be retracted, experts say — Live Science"
    url: "https://www.livescience.com/planet-earth/rivers-oceans/dark-oxygen-discovery-on-the-seafloor-is-fundamentally-at-odds-with-thermodynamics-and-should-be-retracted-experts-say"
  - title: "From headlines to criticism of study on deep-sea oxygen production — Science Norway"
    url: "https://www.sciencenorway.no/geology-the-sea/from-headlines-to-criticism-of-study-on-deep-sea-oxygen-production/2402210"
  - title: "Scientists, deep-sea miner spar over 'dark oxygen' discovery — E&E News"
    url: "https://www.eenews.net/articles/scientists-deep-sea-miner-spar-over-dark-oxygen-discovery/"
  - title: "A deep sea expedition will soon confirm if 'dark oxygen' exists — ScienceAlert"
    url: "https://www.sciencealert.com/a-deep-sea-expedition-will-soon-confirm-if-dark-oxygen-exists"
  - title: "Scientists detail deep sea expedition to understand 'dark oxygen' — Oceanographic"
    url: "https://oceanographicmagazine.com/news/scientists-detail-deep-sea-expedition-to-understand-dark-oxygen/"
---

Four kilometres down, oxygen runs one way: out of the water and into the mud. Organic matter sinks from the sunlit ocean, the microbes and worms in the top centimetres of abyssal clay eat it, and the water touching the seabed gets slowly poorer. A benthic chamber is the instrument for watching that happen: a box, lowered on a lander, that seals a known volume of bottom water over a known patch of seafloor and logs the oxygen inside. On the Clarion-Clipperton plain the line should slope down, and in the experiments I want to talk about, sediment community consumption came out at roughly 0.7 millimoles of oxygen per square metre per day. Down.

In some of those chambers the line went up. Oxygen started near 185 micromoles per litre, unremarkable for bottom water at 4,000 metres and 1.6 °C, and over 47 hours climbed as high as 819 — more than three times where it began. Net production ran from 1.7 to 18 millimoles per square metre per day, an order of magnitude above what the sediment underneath was eating. The chambers were dark. Some were poisoned with mercuric chloride and the rise continued anyway. And the seafloor there is carpeted in polymetallic nodules: black lumps of manganese and iron oxide, potato-sized, the things seventeen contractors currently hold exploration claims to scrape up.

That paper — Sweetman and colleagues, *Evidence of dark oxygen production at the abyssal seafloor*, in Nature Geoscience, July 2024 — proposed that the nodules are splitting seawater. The supporting measurement was electrical: potentials up to 0.95 volts on nodule surfaces, sampled at 153 points across 12 nodules, against 0.003 volts in the surrounding water. A geobattery on the seabed. Coverage called it dark oxygen and went straight for the origin of life — oxygen before photosynthesis, an aerobic niche with no sun. It arrived while the International Seabed Authority was negotiating the mining code for that exact stretch of Pacific.

Two years on, the paper carries an editor's note, added 8 April 2026, saying aspects of it are under editorial consideration. A peer-reviewed rebuttal says the oxygen was air. Its author says he has more than enough to quash that. And the part I cannot stop turning over is that the mechanism under dispute is one of the few in geochemistry that ships with its own built-in control, and in two years of argument I cannot find anyone who has run it.

## The reaction has another half

Electrolysis of water is stoichiometric and it is not subtle about it. Two molecules of water give two of hydrogen and one of oxygen, always, in that ratio. If something inside a sealed 12-litre chamber was splitting seawater vigorously enough to triple the dissolved oxygen, it was simultaneously making twice that many moles of hydrogen, in cold water that starts out with almost none. Oxygen in the deep ocean sits at a couple of hundred micromoles per litre; dissolved hydrogen is orders of magnitude below that. Against that floor, an electrolytic hydrogen signal would not be marginal. It would be the loudest thing in the box.

Nobody measured it. The 2025 rebuttal states it flatly — "no measurements of hydrogen gas — the coproduct of water electrolysis — were conducted" — and makes the obvious point that with a fixed 2:1 ratio, detecting hydrogen is how you confirm electrolysis happened. The same objection was raised in public within weeks of publication, in September 2024, by Lars-Kristian Trellevik and colleagues: a natural control, he said, would be to measure hydrogen the same way you measure oxygen.

I went looking for anyone who had, on either side, and came up empty.

## Where the voltage sits

The electrochemistry is the other half of why this bothers me, and here the original authors deserve more credit than the coverage gave them. They did not pretend 0.95 volts was enough.


<figure class="fig bars"><figcaption class="mono">Potential, volts</figcaption><div class="rows"><div class="brow"><div class="blabel">Nodule surfaces, maximum in main figure</div><div class="btrack"><div class="bfill" style="width:15.00%" title="Nodule surfaces, maximum in main figure · 0.24 V"></div></div><div class="bval mono">0.24 V</div></div><div class="brow"><div class="blabel">Nodule surfaces, reported maximum</div><div class="btrack"><div class="bfill" style="width:59.37%" title="Nodule surfaces, reported maximum · 0.95 V"></div></div><div class="bval mono">0.95 V</div></div><div class="brow"><div class="blabel">Water splitting, thermodynamic minimum</div><div class="btrack"><div class="bfill" style="width:76.88%" title="Water splitting, thermodynamic minimum · 1.23 V"></div></div><div class="bval mono">1.23 V</div></div><div class="brow"><div class="blabel">With overpotential at in-situ pH 7.41</div><div class="btrack"><div class="bfill" style="width:100.00%" title="With overpotential at in-situ pH 7.41 · ~1.60 V"></div></div><div class="bval mono">~1.60 V</div></div></div></figure>


Splitting water costs about 237 kilojoules per mole, which is 1.23 volts if your catalyst is perfect and infinitely fast. Nothing is. At the measured pH of 7.41, with realistic overpotentials, the paper itself puts the requirement near 1.60 volts — then argues that a lattice-oxygen mechanism, where the oxygen comes out of the manganese oxide structure rather than straight off the water, could shave several hundred millivolts off that. That is the honest way to handle a shortfall: name the gap, propose a route across it, say more work is needed.

What the coverage did instead was quote 0.95 volts as if it were the finding. And the rebuttal points out something sharper still: 0.95 appears to be an outlier not shown in the paper's own main figure, where the maximum is 0.24 volts — about a fifth of the thermodynamic floor, before any kinetic penalty. Angel Cuesta, an electrochemist at Aberdeen, has put it bluntly in the press: the proposed mechanism violates thermodynamics, and the explanation is simply impossible as stated.

That is a claim about a mechanism, not about a measurement; the oxygen could still be real and the geobattery wrong. But a mechanism proposed from well below its own threshold is exactly the case where the co-product matters most, because the stoichiometry does not care how the electrons were sourced. Two parts hydrogen, or it was not electrolysis.

## The rebuttal, and what it also fails to measure

The peer-reviewed critique landed in Frontiers in Marine Science in December 2025, authored by Patrick Downes and a long list of co-authors. Its case is that the oxygen was never produced at all — that it came in with the chamber, and its core observation is hard to wave away. Starting oxygen concentrations across the incubations ranged from 161 to 246 micromoles per litre — an 85-micromole spread. Bottom water at a single site does not do that. Measurements across several stations in the same licence area over 2019–2022 varied by 14 micromoles, from 145 to 159. An 85-micromole spread in what should be a homogeneous water mass suggests the chambers were not fully flushed with ambient bottom water before sealing. And a trapped air bubble of 0.1 to 0.2 litres — about one per cent of the 12.1-litre chamber at the surface — holds enough oxygen to account for the largest rise they report. The critique adds that chambers from the western Clarion-Clipperton Zone offered as evidence came from a dataset whose earlier publication states no nodules were present.


<aside class="fig note"><span class="mono">Note</span><p>Nobody in this argument stands outside it. The rebuttal&#x27;s authors are drawn from The Metals Company — which funded the original cruises through its subsidiary NORI and helped choose the sites — a rival mining venture, an oxygen-sensor manufacturer, and two universities. The original paper&#x27;s competing-interests statement discloses support from The Metals Company and UK Seabed Resources. A finding that made the deep sea look more alive was inconvenient to its own funder, and the critique of it is substantially that funder&#x27;s work.</p></aside>


But the bubble hypothesis is a mechanism too, and mechanisms leave traces. Air trapped and forced into solution under 400 atmospheres does not bring oxygen alone; it brings nitrogen and argon in air's proportions. The ratio of dissolved nitrogen to argon is a standard tracer for exactly this, bubble injection, because the two gases differ in solubility. Measure N₂/Ar in the chamber water and you can tell gas that came from the atmosphere from gas that came from a reaction. So far as I can tell, that was not measured either.


<figure class="fig pull"><p>Both camps are arguing about what one sensor saw, when the mechanism in dispute was obliged to leave two other kinds of evidence in the box.</p></figure>


The original team's strongest control looks decisive and isn't. They ruled out optode malfunction by confirming the oxygen with Winkler titration — wet chemistry on the actual water. That is a good check, and it establishes that the oxygen was in the sample. It says nothing about where the oxygen came from. A titration cannot tell a split water molecule from a dissolved bubble; only the gases riding alongside it can.

## What is supposed to settle it

In spring 2026 Sweetman went back, with Jeffrey Marlow of Boston University and Franz Geiger of Northwestern, funded by the Nippon Foundation, carrying two purpose-built landers rated to 11 kilometres. He told reporters beforehand that they would be able to confirm dark oxygen production within 24 to 48 hours of the landers surfacing, and that in twenty years of deploying these instruments he had never had bubbles. Matthias Haeckel, among the sceptics, planned to compare methods directly on the same cruise, which is the right way to do this.

Results were expected in June. It is now October and I cannot find any published outcome — no paper, no preprint, no statement. A four-month gap between a cruise and a result is ordinary, so that is absence of news rather than news. What I can say is that every public description of the instrumentation I could read talks about oxygen and seafloor respiration, and none of them mentions hydrogen.

I would like to be wrong about that. A hydrogen sensor, or a few gas-tight samples drawn from those chambers, would turn a two-year argument about sensor artefacts into arithmetic: find hydrogen at twice the oxygen anomaly and the geobattery survives its voltage problem on evidence alone; find none and the mechanism is dead whatever the oxygen trace does; find the nitrogen-argon signature of injected air and the oxygen is dead too. Three outcomes, all decisive, all cheap next to a lander rated to eleven kilometres.

---

I am working from the paper's abstract and supporting detail rather than the full typeset article, from the rebuttal's own text, and from press coverage for the quotations, which means the disputed figures reach me partly through each other's framing and I have not seen the raw chamber traces that would let me weigh the bubble argument myself. That limits how hard I can push any of this.

The shape I am confident about. Here is a claim unusually well equipped to be tested, by a check that was named within weeks of publication and is not technically demanding, and the check has been reported by nobody — not the team it could vindicate, not the critics whose case its absence strengthens, not the cruise built to settle the question. Instead there is an editor's note, a rebuttal from the study's own funder, and a very large amount of writing about the origin of life.

Most disputes like this are not resolved. They are abandoned: citations thin out, the claim drifts into the set of things people half-remember as true, and nobody ever says on the record that it was wrong. A stoichiometric by-product is an exit from that, and this one is still sitting on the table unused.
