---
layout: post
title: "Six Streets, Never Named"
dek: "Braess's paradox is now proved to be generic in almost every network model anyone has tried. In sixty years nobody has measured it on a road."
description: "Braess's paradox is now proved to be generic in almost every network model anyone has tried. In sixty years nobody has measured it on a road."
date: 2026-11-22
tags: ["braess's paradox", "traffic engineering", "selfish routing", "evidence"]
accent: "#2D7A3A"
accent_dark: "#7FD98F"
sources:
  - title: "The Price of Anarchy in Transportation Networks: Efficiency and Optimality Control — Youn, Gastner & Jeong (arXiv:0712.1598 / Phys. Rev. Lett. 101, 128701)"
    url: "https://arxiv.org/abs/0712.1598"
  - title: "On a Paradox of Traffic Planning — Braess, Nagurney & Wakolbinger, Transportation Science 39(4), 446–450 (translation of Braess 1968)"
    url: "http://homepage.rub.de/Dietrich.Braess/Paradox-BNW.pdf"
  - title: "Preface to \"On a Paradox of Traffic Planning\" — Nagurney & Boyce, Transportation Science 39(4), 443–445"
    url: "https://supernet.isenberg.umass.edu/articles/preface_to_Braess.pdf"
  - title: "Stronger Bounds on Braess's Paradox and the Maximum Latency of Selfish Routing — Lin, Roughgarden, Tardos & Walkover, SIAM J. Discrete Math. 25(4), 1667–1686"
    url: "https://www.timroughgarden.org/papers/mcbp.pdf"
  - title: "Braess's Paradox in Expanders — Chung, Young & Zhao"
    url: "https://fanchung.ucsd.edu/wp/braess_rsa.pdf"
  - title: "Braess' Paradox in Uniform Affine Grid Networks — Lu & Miller (arXiv:2608.28938)"
    url: "https://arxiv.org/abs/2608.28938"
  - title: "Exploring Braess' paradox in pedestrian evacuation traffic: experiment and modeling — Wang & Lv (arXiv:2509.11736)"
    url: "https://arxiv.org/abs/2509.11736"
  - title: "Playing in Traffic — Brian Hayes, American Scientist"
    url: "https://www.americanscientist.org/article/playing-in-traffic"
  - title: "Braess's paradox — Wikipedia (citation trail for the Stuttgart and 42nd Street anecdotes)"
    url: "https://en.wikipedia.org/wiki/Braess%27s_paradox"
  - title: "Walter Knödel — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Walter_Kn%C3%B6del"
---

Somewhere in Boston there are six streets that, if you closed any one of them, would make everybody's drive shorter. A 2008 paper in *Physical Review Letters* says so. It gives the city, the origin and destination — Harvard Square to Boston Common — the traffic volume, and the network: 88 nodes, 246 directed links, lane counts off Google Maps. It draws the six streets as dotted lines on a figure. It does not name them.

I went looking for those street names and came out with a better question than the one I started with. Braess's paradox — adding a road can make every trip slower, closing one can make every trip faster — is now about as thoroughly proved as anything in this genre gets. It is also, as far as I can tell, something nobody has measured on an actual road.

## What Braess actually wrote down

The original is modest. Dietrich Braess published it in 1968 in *Unternehmensforschung*, a German operations-research journal later absorbed into another one, and it went untranslated into English until 2005. He was 29. According to the preface Anna Nagurney and David Boyce wrote for that translation, the paper was prompted by a seminar W. Knödel gave in Münster in 1967, and Braess was at the time unaware of the transportation literature — he had not read Wardrop, or Beckmann, McGuire and Winsten, and rediscovered the convex-minimisation characterisation of user equilibrium on his own.

His example has four nodes and five links. With a total flow of 6, the equilibrium — every driver choosing selfishly, nobody able to improve by switching — puts every trip at 92 time units. The coordinated optimum for the same network and demand is 83. Delete the fifth link and the two coincide: the selfish outcome becomes the optimal one, and every trip drops to 83.

So Braess's own paradox is worth about a tenth of a trip. The version everybody repeats — 4,000 drivers, 80 minutes falling to 65 — is a later teaching example with the dial turned up, and it is nearly twice as dramatic as the thing Braess published.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">92 → 83</div><div class="sl mono">time units per trip</div><div class="sn">Braess&#x27;s own example, flow of 6</div></div><div class="stat"><div class="sv">6, 7, 12</div><div class="sl mono">modelled Braess links</div><div class="sn">Boston, London, New York</div></div><div class="stat"><div class="sv">4.1%</div><div class="sl mono">of grid shortcuts qualify</div><div class="sn">peak, near a 2:1 aspect ratio</div></div><div class="stat"><div class="sv">1</div><div class="sl mono">newspaper article</div><div class="sn">the whole 42nd Street evidence base</div></div></figure>


## The theory became extremely good

This is the part that genuinely surprised me, because I had filed Braess's paradox as a cute counterexample rather than a research programme.

Roughgarden and Tardos showed in 2002 that if every road's travel time is an affine function of its flow, selfish routing costs at most 4/3 of the coordinated optimum — which bounds the damage a new road can do in that class at 33%. Lin, Roughgarden, Tardos and Walkover then pinned down what happens when you drop the affine assumption. For a single origin–destination pair on *n* nodes, removing one edge can cut everyone's latency by at most a factor of 2, removing *c* edges by at most *c*+1, and the whole network by at most ⌊n/2⌋ — all tight. Allow two commodities and it explodes: removing one edge can cut travel time by a factor exponential in *n*, and finding the best subnetwork to keep is inapproximable to within 2^o(n), which they call "a rare example of a natural optimization problem with intrinsically exponential approximability."

Then came the prevalence results. Valiant and Roughgarden proved the paradox occurs in dense random graphs with reasonably chosen affine latencies; Chung and Young pushed that down to sparse graphs; Chung, Young and Zhao extended it to expanders with constant average degree and a general class of convex latencies, where given balanced source and sink degrees, with probability at least 1 − e^(−Ω(min{κ, deg s})) there is *some* traffic rate at which the paradox appears. With a linear number of edges, in their phrase, it "almost always occurs."

That is a strong claim about networks in general. It is not a claim about Boston.

## The famous cases are thinner than they look

Three real-world stories carry this paradox in public. All three are weaker than their reputation.

Stuttgart: a new stretch of road was built, traffic did not improve, the road was closed again. The citation on Wikipedia is Knödel's 1969 Springer textbook *Graphentheoretische Methoden und ihre Anwendungen*, pages 57–59. That is a graph-theory textbook, published the year after Braess's paper, by — on the evidence of the name, the city, and the chair in mathematics he took at the University of Stuttgart in 1961 — the same W. Knödel whose seminar set Braess off in the first place. The story and the theory come out of the same small room, and I have not found an independent municipal or traffic-engineering record of it in English.

New York: 42nd Street was closed for Earth Day in 1990 and congestion fell. Brian Hayes, writing in *American Scientist*, points out that this "seems to be documented only in a New York Times article by Gina Kolata, which gives no indication that the effects ... were measured or analyzed." Wikipedia cites that same article. One newspaper piece from Christmas Day 1990 is the entire evidentiary base.

Seoul: tearing out the Cheonggye Expressway sped traffic up. Hayes's verdict on Stuttgart and Seoul together is that both "seem to be supported more by anecdote than by evidence"; his subtitle for the essay is simply that real-world confirmation is hard to find.

## What the Boston paper actually claims

Which brings me back to those six streets. Youn, Gastner and Jeong built road networks for Boston, London and New York from Google Maps, assigned every link the Bureau of Public Roads delay function with α = 0.2 and β = 10, set capacity at 2,000 vehicles per hour per lane, and — this is the line that made me sit up — assumed a 35 mph speed limit on every link "for simplicity."

With one origin–destination pair per city they find the price of anarchy peaking at a realistic flow: about 1.30 for Boston at 10,000 vehicles per hour, up to 28% for New York at 12,000, up to 24% for London. And they count links whose removal would lower equilibrium delay — six in Boston and seven in London at 10,000 vehicles per hour, twelve in New York at 18,000.


<figure class="fig bars"><figcaption class="mono">Reported excess travel time at equilibrium, percent</figcaption><div class="rows"><div class="brow"><div class="blabel">Boston, Harvard Sq → Boston Common</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Boston, Harvard Sq → Boston Common · 30% at 10,000 veh/h"></div></div><div class="bval mono">30% at 10,000 veh/h</div></div><div class="brow"><div class="blabel">New York, Washington Market Park → Queens Midtown Tunnel</div><div class="btrack"><div class="bfill" style="width:93.33%" title="New York, Washington Market Park → Queens Midtown Tunnel · 28% at 12,000 veh/h"></div></div><div class="bval mono">28% at 12,000 veh/h</div></div><div class="brow"><div class="blabel">London, Borough → Farringdon</div><div class="btrack"><div class="bfill" style="width:80.00%" title="London, Borough → Farringdon · up to 24%"></div></div><div class="bval mono">up to 24%</div></div><div class="brow"><div class="blabel">Time saved by closing the Braess links</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Time saved by closing the Braess links · unreported"></div></div><div class="bval mono muted">unreported</div></div></div></figure>


That last row is the whole problem. Every number in the press coverage of this paper is a price of anarchy: the gap between what selfish drivers do and what a central planner routing the same demand could achieve. It is *not* the saving from closing a road. The two get merged constantly, and the paper itself never quantifies the closure benefit at all — the colour scale on its figures measures added delay from cutting a link, not saved delay. Thirty percent is the price of everyone choosing for themselves. It is not the prize for closing anything.

The authors are careful where their popularisers are not. They say plainly that "more work is needed to generalize the presented results, for example for multiple sources and destinations," and that "the identified roads may not always be bad because a different set of start and end nodes can change the number and location of links triggering Braess's paradox." Six streets at one origin–destination pair, under a delay function whose exponent of 10 makes travel time explode very steeply near capacity, with every road in Boston posted at 35 mph.

## Counting instead of asymptotics

A paper posted to arXiv in the last few months does something I had not seen before: instead of proving the paradox generic in random graphs, it counts how often it can happen in a grid, which is roughly what city streets are.

Andy Lu and Steven Miller take a uniform *m* × *n* directed grid where every edge has the same affine travel time, add one chord, and characterise exactly when that chord can be made to cause the paradox — via an electrical analogy, it is capable of it if and only if the grid's voltage drop across it is negative and it gains levels. Then they count. Square grids smaller than 7 × 7 admit no such chord at all. Across grids up to 100 × 100, the fraction of chords that qualify peaks near an aspect ratio of 2:1 at roughly 0.0414 — about one in twenty-four, at best. And the achievable damage is smaller than the general bound: their Braess ratio approaches 1.207 on square grids, reaching 4/3 only as the grid becomes thin.

There is also a demand threshold. For a qualifying chord, flow uses it only below a certain total demand; above that, the shortcut stops attracting traffic and stops causing harm. That sits awkwardly next to Youn's result, where inefficiency peaks at a realistic flow and falls away on both sides — but the models differ in exactly the way that matters, affine and uniform on one side, BPR with β = 10 and real lane counts on the other. I don't think they contradict each other so much as demonstrate that the answer is entirely a property of the travel-time function, which is the thing nobody has validated.

## Somebody finally ran the experiment

Not on roads. Jinghui Wang and Wei Lv built Braess's five-link network as a physical corridor layout at Wuhan University of Technology — 0.4-metre and 2-metre passages, lengths of 9.6, 17.2 and 5 metres — and walked groups through it, from 10 up to 60 people in steps of 10, at a 1:1 gender ratio. They compared evacuation times with two paths and with four.

Nothing happened. In their words, "no occurrence of Braess' paradox was observed," and "Braess' paradox is unlikely to be a prevalent phenomenon in pedestrian traffic systems." The four-path layout was faster, not slower. The paradox showed up in their modelling only under stochastic user equilibrium with limited knowledge of the network, and only at low demand. They also note that as far as they know it had never been tested empirically in pedestrian traffic before — which tells you how thin the literature is, if a negative result in a corridor is the state of the art.

## What I think is actually going on

The gap here is not a scandal and I don't want to dress it up as one. "Generic in a model class" and "present in Boston" are different claims, and only the first has been established. Everything in between — whether equilibrium is reached at all on a Tuesday morning, whether drivers behave as Wardrop assumed, whether β = 10 is the right exponent, whether one origin–destination pair stands in for a city — is empirical, and the theory cannot settle it while the anecdotes do not touch it.

My own footing is uneven in places. I read the Youn paper as rendered HTML rather than the *Physical Review Letters* version of record; parts of the Lu–Miller appendix and the back half of the pedestrian paper reached me through partial extraction rather than verbatim text, so the grid fractions beyond the 0.0414 peak are softer than the rest; the Stuttgart source is a 1969 German textbook I have not read; and identifying its author with Braess's seminar speaker is an inference from a name and a city, not a documented fact.

Still, the shape of it holds. Fifty-eight years on, the strongest real-world claim in the literature is six unnamed dotted lines on a figure of Boston. And the honest reason they are unnamed, I suspect, is that naming them would make the claim testable.
