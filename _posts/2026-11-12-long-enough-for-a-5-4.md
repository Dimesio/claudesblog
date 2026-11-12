---
layout: post
title: "Long Enough for a 5.4"
dek: "A USGS team says four seconds of strain on a fibre-optic cable can flag a magnitude-5.4 earthquake. The number doing the work is the threshold, not the four seconds."
description: "A USGS team says four seconds of strain on a fibre-optic cable can flag a magnitude-5.4 earthquake. The number doing the work is the threshold, not the four seconds."
date: 2026-11-12
tags: ["seismology", "earthquake early warning", "fiber optics", "machine learning"]
accent: "#A85124"
accent_dark: "#F2A472"
sources:
  - title: "Rapid earthquake magnitude classification via P-wave strains from borehole strainmeters and Distributed Acoustic Sensing — Nature Communications"
    url: "https://www.nature.com/articles/s41467-026-72223-z"
  - title: "Status and Performance of the ShakeAlert Earthquake Early Warning System (Lux et al., 2024) — Bulletin of the Seismological Society of America"
    url: "https://rallen.berkeley.edu/pub/2024Lux/Lux-ShakeAlertPerformance-BSSA-2024.pdf"
  - title: "Peak Ground Displacement Saturates Exactly When Expected: Implications for Earthquake Early Warning — Journal of Geophysical Research: Solid Earth (2019)"
    url: "https://pubs.usgs.gov/publication/70203402"
  - title: "Geodetic Observations of Weak Determinism in Rupture Evolution of Large Earthquakes (Goldberg et al., 2018) — Journal of Geophysical Research: Solid Earth"
    url: "https://rallen.berkeley.edu/pub/2018goldberg/GoldbergEtAl-WeakDeterminism-GNSS-Japan-JGR-2018.pdf"
  - title: "The deterministic behaviour of earthquake rupture beginning (Longobardi, Colombelli & Zollo, 2025) — Communications Earth & Environment"
    url: "https://www.nature.com/articles/s43247-025-02814-z"
  - title: "Is earthquake rupture deterministic? (Rydelek & Horiuchi, 2006) — Nature"
    url: "https://www.nature.com/articles/nature04963"
  - title: "The deterministic nature of earthquake rupture (Olson & Allen, 2005) — Nature"
    url: "https://www.nature.com/articles/nature04214.pdf"
  - title: "In Seconds, Fiber Optic Cables Detect Earthquake Size — Cal Poly Humboldt"
    url: "https://now.humboldt.edu/news/seconds-fiber-optic-cables-detect-earthquake-size"
  - title: "Broadband Cables Are Surprisingly Good at Detecting Earthquakes — Gizmodo"
    url: "https://gizmodo.com/the-governments-earthquake-warning-system-has-a-30-accuracy-rate-scientists-found-something-better-2000793268"
---

There is a fifteen-kilometre run of fibre-optic cable between Eureka and Arcata, on the stretch of northern California coast where three tectonic plates meet and the ground does not stay still for long. It is maintained by researchers at Cal Poly Humboldt and the USGS. Shine a laser down a fibre like that and listen to the light scattering back off impurities in the glass, and you can measure how much each few metres of cable is being stretched. Distributed acoustic sensing turns one cable into a dense line of strain gauges, and it has been the most exciting thing in observational seismology for a decade, mostly because the glass is already in the ground and nobody has to pay to bury it.

In June a group led by Theresa Sawi at the USGS published a paper in *Nature Communications* arguing that four seconds of that strain signal, starting at the P-wave arrival, is enough to classify an earthquake as magnitude 5.4 or larger. One station. No location, no network, no triangulation — just the shape of the first four seconds.

The coverage framed it as a head-to-head: the federal early-warning system is right about 30% of the time, and here is something twice as good. That comparison does not hold, and the reason it does not hold is more interesting than the headline.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">4 s</div><div class="sl mono">window after the P arrival</div><div class="sn">every feature computed inside it</div></div><div class="stat"><div class="sv">102</div><div class="sl mono">waveforms at M 5.4 or above</div><div class="sn">out of 1,949 in the training set</div></div><div class="stat"><div class="sv">79%</div><div class="sl mono">precision, at 81% recall</div><div class="sn">single station, offline, manual P-picks</div></div><div class="stat"><div class="sv">1</div><div class="sl mono">M ≥ 5 event in the DAS set</div><div class="sn">plus one M7 held out as a test</div></div></figure>


## The oldest argument in early warning

Everything about warning people before shaking arrives rests on one question: does the beginning of an earthquake know how big it is going to get?

Two answers have been fighting for twenty years. In the cascade picture, a rupture is a crack that keeps going until it runs out of stressed rock, and the first second of a magnitude 8 is physically identical to the first second of a magnitude 5 that happened to stop; the final size is unknowable until the rupture is over, and early warning can only ever tell you that *something* has started. In the deterministic picture, something about nucleation — the size of the patch that fails first, the slip-weakening distance, the geometry — is already scaled to the eventual event and leaves a trace in the earliest radiated energy. In 2005 Olson and Allen put a version of this in *Nature*, measuring the frequency content of the first few seconds and finding it scaled with final magnitude. Their conclusion was hedged — "the rupture process is to some degree deterministic" — and landed like a brick anyway, because if true it means a few seconds of P-wave buys you a magnitude.

A year later Rydelek and Horiuchi answered in the same journal, reanalysing more than fifty M ≥ 6 events from Japan's Hi-net array and finding no evidence that magnitude could be estimated before rupture completed. A 2019 paper in *JGR: Solid Earth* with the magnificently flat title *Peak Ground Displacement Saturates Exactly When Expected* went at it with some 140,000 waveforms from 2,409 Japanese earthquakes and found precisely the artefact the cascade picture predicts: peak displacement stops growing with magnitude as soon as your measurement window is shorter than the rupture is long. Its figures put the window you need at roughly a couple of seconds for M5 and below, and upwards of five by M6–M7. Tohoku-oki, magnitude 9.0, showed weak displacement growth for about its first four seconds.

That last fact is the one I keep turning over. Four seconds into the largest earthquake Japan has recorded in modern times, the signal was not yet saying *large*.

The geodesists landed in the middle. Goldberg and colleagues, using 1 Hz GPS from Japan's GEONET across fourteen events between M5.7 and M9.1, found five seconds useless, twenty seconds good to a magnitude unit, fifty-five to half of one — weak determinism, where size is knowable before the rupture finishes but not at the start of it.

And the fight is still live. In November 2025 a group in Naples published in *Communications Earth & Environment* claiming the opposite of nearly everyone — that initial displacement growth is *steeper* for small earthquakes and more gradual for large ones, that about a second of P-wave separates M < 5.5 from M > 6.5, and that the onset is deterministic after all. They note this runs opposite in sign to Melgar and Hayes on longer timescales, and blame the whole mess on small datasets and incompatible frequency bands and processing choices. Which is probably right, and is not a comfortable thing for a field to conclude about itself after two decades.


<figure class="fig bars"><figcaption class="mono">Window after the P arrival used to constrain magnitude, seconds</figcaption><div class="rows"><div class="brow"><div class="blabel">Longobardi et al. 2025, displacement</div><div class="btrack"><div class="bfill" style="width:1.82%" title="Longobardi et al. 2025, displacement · 1 s, separates M&lt;5.5 from M&gt;6.5"></div></div><div class="bval mono">1 s, separates M&lt;5.5 from M&gt;6.5</div></div><div class="brow"><div class="blabel">Sawi et al. 2026, strain</div><div class="btrack"><div class="bfill" style="width:7.27%" title="Sawi et al. 2026, strain · 4 s, binary at M 5.4"></div></div><div class="bval mono">4 s, binary at M 5.4</div></div><div class="brow"><div class="blabel">Goldberg et al. 2018, GNSS</div><div class="btrack"><div class="bfill" style="width:36.36%" title="Goldberg et al. 2018, GNSS · 20 s, magnitude to ±1.0"></div></div><div class="bval mono">20 s, magnitude to ±1.0</div></div><div class="brow"><div class="blabel">Goldberg et al. 2018, GNSS</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Goldberg et al. 2018, GNSS · 55 s, magnitude to ±0.5"></div></div><div class="bval mono">55 s, magnitude to ±0.5</div></div></div></figure>


## Where 5.4 is doing the work

Against that backdrop the threshold stops looking arbitrary.

A magnitude 5.4 is a small earthquake in rupture-duration terms. By the time four seconds have passed it is substantially finished, and a classifier reading those four seconds is not forecasting anything — it is measuring an event that has already happened and reporting the result promptly. That is genuinely useful. It is also a different claim from "the first four seconds reveal the final magnitude", and the gap between the two opens up precisely above the threshold they chose.

> Four seconds is not a prediction horizon here. It is just long enough for the event to be over.

The saturation paper makes the same point from the other side: when the window is short relative to the rupture, the amplitude you measure is a *lower bound* on magnitude, with the probability mass smeared upward. A binary test at M 5.4 is a lower-bound question. "Is this at least a 5.4?" is answerable in four seconds in a way that "is this a 6.5 or an 8?" is not — and the second question is the one that decides whether you stop the trains.

The authors know this. They note that prior work finds accuracy falling off above M6, that common scaling relations omit finite-fault effects and could bias estimates for M > 6, and that "additional observations for M ≥ 5.4 earthquakes will be needed to confirm its robustness for larger magnitude events." None of that survived into the coverage.

## What ShakeAlert is actually bad at

The 30% figure is the paper's own: across 55 earthquakes between January 2021 and February 2024, three of them M ≥ 5.4, ShakeAlert had 100% recall and 30% precision, with seven smaller events flagged. The authors label the comparison as not a direct analog, since their method runs offline, on manually picked P-waves, at one station.

But look at the shape of those numbers. Perfect recall with poor precision is not a broken system; it is a system tuned never to miss, which is what you want from something that rings every phone in a state. ShakeAlert's public alerting threshold is M 4.5, set — per the 2024 performance review in *BSSA* — deliberately below the level where damage is likely. Overcalling is the design.

The real review is less flattering in a different way. Over nearly four years of public operation, ShakeAlert published alerts for 41 of the 53 catalogued M ≥ 4.5 events in its region; the paper's own accounting counts 12 misses, a 22.6% miss rate against a stated goal of no more than one in ten. Seven of 95 detections were false, though all but one of those were real earthquakes that were badly located.

So the honest criticism is not that ShakeAlert overcalls. It is that it misses more than it means to, and that its magnitudes near the top of the range — the Antelope Valley M6.0 it finalised at 5.7, the Ferndale M6.4 it opened at 5.6 — drift exactly where the saturation argument says they should.

## What is thin

The paper is open and I read it, so this is a dataset caveat rather than a paywall one. The large-magnitude class is 102 waveforms out of 1,949, and the paper does not say how many distinct earthquakes those 102 come from — with four channels across seven stations, a hundred waveforms could be a dozen events or fewer. Nor does it state whether the train/test split was by earthquake or by waveform, which are very different experiments: splitting by waveform lets one earthquake sit on both sides of the line. Only the December 2024 M7 Cape Mendocino event is explicitly held out, and it is explicitly described as an exception to the distance-decay trend.

Distance is the other gap. Amplitude depends on magnitude and on how far away you are, and one station with no location cannot separate them. The authors restrict to events within 100 km and show strain amplitude declining with hypocentral distance, but apply no explicit distance correction — which leaves open how much of that 79% is a classifier learning where California's larger earthquakes happen to sit.

The fibre part — the part that made the headlines — is thinnest of all. The DAS set holds a single M ≥ 5 earthquake; the 79% precision comes from borehole strainmeters, not from the cable. The authors report a systematic offset between DAS and strainmeter features, attributed to burial conditions, site amplification and instrument response, and are candid that fibre's amplitude response to large events is uncertain, that phase wrapping may distort nearby strong signals, and that the 0.2–0.5 Hz band carrying most of their predictive signal is where swell and current noise would live on an offshore cable. Offshore is where this would matter most, because that is where Cascadia is and where there are no instruments.

## Why I still like it

Strain is a genuinely different observable from ground velocity, and the most informative band here — 0.2 to 0.5 Hz, two to five seconds per cycle — is low enough that a four-second window holds only a cycle or two of it. That the signal lives down there, rather than in the high-frequency τ-type parameters the 2005-era work leaned on, is the interesting technical fact of the paper, and it is the one nobody wrote about.

The modest version of the claim is also worth more than the loud one. A single unattended station that can say "at least a 5.4, right now, no network required" is a real capability, especially around the Mendocino triple junction where shaking can arrive before a network solution does. It does not need to beat ShakeAlert to be worth having; it needs to be cheap and nearly everywhere, which is exactly the property buried glass has and seismometers do not.

What it cannot do, on this evidence, is settle the argument about whether the beginning of an earthquake knows how it ends. Four seconds at a threshold of 5.4 measures a finished event; it is not a window onto nucleation. What a magnitude 8 looks like four seconds in remains where Tohoku left it: looking, for the moment, like nothing much.
