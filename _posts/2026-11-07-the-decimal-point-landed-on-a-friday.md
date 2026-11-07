---
layout: post
title: "The Decimal Point Landed on a Friday"
dek: "A 1960 Science paper fitted world population to a hyperbola and got a singularity next Friday. It was off by half a percent in 1993, which is the part worth explaining."
description: "A 1960 Science paper fitted world population to a hyperbola and got a singularity next Friday. It was off by half a percent in 1993, which is the part worth explaining."
date: 2026-11-07
tags: ["demography", "curve fitting", "economic growth", "forecasting"]
accent: "#4A2E9C"
accent_dark: "#B0A0F5"
sources:
  - title: "Doomsday: Friday, 13 November, A.D. 2026 — von Foerster, Mora & Amiot, Science 132(3436), 1291-1295 (1960)"
    url: "https://www.science.org/doi/10.1126/science.132.3436.1291"
  - title: "Doomsday: Friday, 13 November, A.D. 2026 — full text (PDF mirror)"
    url: "https://www2.bioinfo.rpi.edu/bystrc/courses/biol4520/Doomsday.pdf"
  - title: "People, Skills, and Resources: An Interaction Model for World Population Growth — Taagepera, Technological Forecasting and Social Change 13, 13-30 (1979)"
    url: "https://escholarship.org/content/qt8dg7k25r/qt8dg7k25r.pdf"
  - title: "Papers on world population (incl. Umpleby 1987, Serrin 1975, the 1961 letters and the 1962 reply) — Stuart Umpleby"
    url: "https://blogs.gwu.edu/umpleby/papers-on-world-population"
  - title: "The scientific revolution in demography — Umpleby, Population and Environment 11(3), 159-174 (1990)"
    url: "https://link.springer.com/article/10.1007/BF01254115"
  - title: "In 1960, scientists predicted the world would end on November 13, 2026 — Popular Science"
    url: "https://www.popsci.com/science/world-end-overpopulation-doomsday-november-2026/"
  - title: "Scientists once calculated the date of doomsday — MacEachern, The Conversation / Gizmodo"
    url: "https://gizmodo.com/scientists-once-calculated-the-date-of-doomsday-and-its-next-month-2000820261"
  - title: "World Population Prospects 2024: Ten key messages — UN Population Division"
    url: "https://population.un.org/wpp/assets/Files/WPP2024_Key-Messages.pdf"
  - title: "World population, historical series and 2026 estimate (UN WPP 2024) — StatisticsTimes"
    url: "https://statisticstimes.com/demographics/world-population.php"
  - title: "Population growth — Our World in Data"
    url: "https://ourworldindata.org/population-growth"
  - title: "Estimates of historical world population — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Estimates_of_historical_world_population"
  - title: "Law of hyperbolic growth of the human population (von Foerster, Kapitsa, Kremer, Korotayev) — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Law_of_hyperbolic_growth_of_the_human_population"
  - title: "The End of Economic Growth? Unintended Consequences of a Declining Population — Jones, AER 112(11), 3489-3527 (2022)"
    url: "https://www.aeaweb.org/articles?id=10.1257%2Faer.20201605"
---

Next Friday is the thirteenth. According to a paper in *Science* dated 4 November 1960, it is also the day the human population becomes infinite.

I went to the paper expecting a joke, because the title reads like one: "Doomsday: Friday, 13 November, A.D. 2026. At this date human population will approach infinity if it grows as it has grown in the last two millenia." Misspelling included. The authors were Heinz von Foerster, Patricia M. Mora and Lawrence W. Amiot, working at the University of Illinois, and the thing underneath the title is not a joke at all. It is a short, careful, entirely conventional curve-fitting paper. That gap — between how the paper is remembered and what it actually does — turned out to be the interesting part, and so did the fact that for thirty-three years after publication the curve was very nearly right.

## What they actually fitted

Start with the ordinary model of a growing population: `dN/dt = αN`, where α is the net per-head rate of increase. If α is a constant you get exponential growth. If α falls as the population gets denser — the standard assumption, competition for a fixed pie — you get a logistic curve that flattens out at a carrying capacity.

Von Foerster and his co-authors proposed the opposite. People communicate. People who communicate can form coalitions, and a coalition acts as one player against nature rather than as many players against each other. So α might *rise* with N. They wrote it in the simplest possible way, `α = α₀N^(1/k)`, and solved it. The solution is not exponential and not logistic. It is a hyperbola:

> N = K / τ^k, where τ = t₀ − t

τ is the time remaining until the curve goes vertical. The paper calls it "dooms-time," which I enjoy more than I should. Then they took 24 independent estimates of world population spanning about a hundred generations, from roughly the time of Christ to the late 1950s, threw out duplicates, excluded 1958, and ran least squares.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">2026.87</div><div class="sl mono">fitted singularity</div><div class="sn">±5.50 years</div></div><div class="stat"><div class="sv">0.990</div><div class="sl mono">exponent k</div><div class="sn">1.000 is the pure hyperbola, dN/dt ∝ N²</div></div><div class="stat"><div class="sv">7%</div><div class="sl mono">RMS deviation of the fit</div><div class="sn">across 24 estimates, A.D. 1 to the 1950s</div></div><div class="stat"><div class="sv">9.6 trillion</div><div class="sl mono">people alive today, per their equation</div><div class="sn">actual: 8.30 billion</div></div></figure>


The fitted date, 2026.87, is a decimal point. Point eight seven of a year lands in the second week of November, and in 2026 the 13th of November is a Friday. The title is that coincidence, cashed in. One historian who has written about the paper this year, Alan MacEachern, reads it as deliberate stagecraft — an ordinary scientific article wrapped in an extraordinary title — and I think that is right. It worked: the paper drew letters to *Science* calling it ridiculous and manifestly absurd, a reply from the authors in 1962 distinguishing "projections" from "forecasts," a *Time* write-up, and three *Pogo* strips.

Two things about that fit deserve more attention than the title.

The first is that k came out as 0.990 ± 0.009 — indistinguishable from 1. With k = 1 the model collapses to `dN/dt ∝ N²`, the cleanest possible statement that every person's productive capacity scales with the number of other people they can reach. The data picked the simplest member of the family on its own. A separate fit by Meyer and Vallée, which simply assumed the pure hyperbola `P = 200 × 10⁹ / (2026 − t)`, landed on the same year.

The second is that this is not Malthus, and it is not *The Population Bomb*, which came eight years later. Von Foerster explicitly rejected famine as the constraint; the whole point of the coalition mechanism is that technology keeps pace, that it has kept pace for a hundred generations and will keep pace for three more. The danger in the paper is geometric, not agricultural. Their line is that our great-great-grandchildren will not starve to death — they will be squeezed to death. The recommendation at the end is a two-child norm enforced through tax policy, plus, in a flourish I had to read twice, emigration by spacecraft with no re-entry permit issued.

## The part I didn't expect

I assumed a 1960 extrapolation to 2026 would have been obviously dead by 1975. It wasn't. In 1987, Stuart Umpleby published a note in *Science* with the title "World Population: Still Ahead of Schedule" — population was running *above* the doomsday curve, not below it. Running the published equation forward myself: in 1987 it gives 4.72 billion against an actual 5.05 billion, so it was 7% low. In 1993 it gives 5.56 billion against an actual 5.59 billion. That is an error of six parts in a thousand, thirty-three years out of sample.

Then it comes apart, and it comes apart completely, because that is what hyperbolas do. The entire character of the curve lives in its last few percent of τ. By mid-2026 the equation is over by a factor of 58; by this morning, by a factor of 1,151.


<figure class="fig bars"><figcaption class="mono">Predicted ÷ actual population, before the curve ran away</figcaption><div class="rows"><div class="brow"><div class="blabel">1960</div><div class="btrack"><div class="bfill" style="width:58.13%" title="1960 · 0.93×"></div></div><div class="bval mono">0.93×</div></div><div class="brow"><div class="blabel">1970</div><div class="btrack"><div class="bfill" style="width:56.25%" title="1970 · 0.90×"></div></div><div class="bval mono">0.90×</div></div><div class="brow"><div class="blabel">1987</div><div class="btrack"><div class="bfill" style="width:58.13%" title="1987 · 0.93×"></div></div><div class="bval mono">0.93×</div></div><div class="brow"><div class="blabel">1993</div><div class="btrack"><div class="bfill" style="width:61.87%" title="1993 · 0.99×"></div></div><div class="bval mono">0.99×</div></div><div class="brow"><div class="blabel">2000</div><div class="btrack"><div class="bfill" style="width:71.25%" title="2000 · 1.14×"></div></div><div class="bval mono">1.14×</div></div><div class="brow"><div class="blabel">2010</div><div class="btrack"><div class="bfill" style="width:100.00%" title="2010 · 1.60×"></div></div><div class="bval mono">1.60×</div></div></div></figure>


Today the equation calls for 9.6 trillion people and a growth rate of 5,500% per year. The measured figures are 8.30 billion and 0.83%. The model's own relation for doubling time, `Δt₂ ≈ τ/2`, puts the current doubling time at about three days.

## Where the fit was weaker than it looked

The ±5.50 years is the honest output of a least-squares routine and a dishonest description of what anyone knew. It is a standard error computed over 24 numbers that have no standard errors of their own. Published estimates for world population at A.D. 1 run from about 170 million (McEvedy and Jones) to about 330 million (the top of Durand's range) — uncertainty on the order of 50% in the oldest and most leveraged points in the series. A 7% RMS deviation against inputs like that is not a measure of how well the model describes the world. It is a measure of how well a two-parameter curve can thread a scatter of educated guesses, which is very well indeed, and tells you much less.

Worse, in the sense that matters most: the data could not distinguish a singularity from no singularity. Rein Taagepera went through this carefully in 1979 and showed that a doubly exponential form — no singularity anywhere, ever — fits the post-1850 data about as well as the hyperbola does, and he was explicit that the singularity is an artifact of the chosen functional form rather than a claim about infinite people. So "the world ends in 2026" and "the world never ends" were, on the evidence available in 1960, the same evidence.

And the mechanism was wrong exactly where the curve was right. The acceleration that von Foerster read as rising per-head productivity was mostly mortality decline: children stopped dying, and families took decades to adjust. That is a bounded, one-way transition — death rates can fall to near zero and no further — whereas `α = α₀N^(1/k)` has no ceiling in it anywhere. The curve was fitting the steep middle of a sigmoid and reporting it as a hyperbola. Joel Cohen's summary, quoted in recent coverage, is that von Foerster was right about the past and wrong about the future; Dean Spears notes that demographers at the time already had reasons to doubt sustained acceleration, which is some of what the angry letters were about.


<aside class="fig note"><span class="mono">Note</span><p>I could not read the criticism directly. Serrin&#x27;s &quot;Is &#x27;Doomsday&#x27; on Target?&quot; (<em>Science</em>, 1975), the 1961 letters and the authors&#x27; 1962 reply are all behind the paywall; I am working from Taagepera&#x27;s citations and from this year&#x27;s secondary coverage for their content. One claim in that coverage I would not repeat: that the world fell off the curve because it took the paper&#x27;s advice. Fertility fell for reasons that owe nothing to a 1960 <em>Science</em> article.</p></aside>


## What survived

The equation did not get thrown away. Michael Kremer gave it microfoundations in 1993: ideas are non-rival, so the stock of technology grows with the number of people thinking, and population grows with technology — which multiplies out to `dN/dt ∝ N²` again, from economics rather than cybernetics. That scale effect is still the load-bearing assumption in idea-based growth theory.

What changed is the sign. In Charles Jones's 2022 version, knowledge accumulates as `Ȧ/A = αN^λA^(−β)` and long-run income growth comes out proportional to population growth. Feed in the actual number — a world where total fertility is 2.3 and falling, where more than half of all countries are already below replacement, where the UN's central projection peaks near 10.3 billion in the mid-2080s and declines after — and the same machinery that once ran to infinity in 66 years now runs to zero. Jones calls the outcome the Empty Planet: living standards stagnating for a population that vanishes. He is careful to say it is not a forecast, which is the lesson von Foerster taught the field the hard way.

So the thing I keep turning over is not that the 1960 paper was wrong. It is that the paper was wrong in a way its own data could not have revealed, using a functional form that had no way to represent what was about to happen, and that this was invisible for three more decades because a hyperbola and a sigmoid look identical until the moment they don't. On Friday the curve will be off by a factor of a thousand. In 1993 it was off by half a percent. Those are the same curve.
