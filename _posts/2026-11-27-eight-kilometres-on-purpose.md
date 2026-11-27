---
layout: post
title: "Eight Kilometres, On Purpose"
dek: "To find out whether tropical cyclones are getting stronger, you have to build a satellite record deliberately worse than the one forecasters use. NOAA now ships one, with a label saying not to use it on any actual storm."
description: "To find out whether tropical cyclones are getting stronger, you have to build a satellite record deliberately worse than the one forecasters use. NOAA now ships one, with a label saying not to use it on any actual storm."
date: 2026-11-27
tags: ["tropical cyclones", "satellite records", "homogenization", "climate trends"]
accent: "#8A1E9E"
accent_dark: "#DFA2F0"
sources:
  - title: "Global increase in major tropical cyclone exceedance probability over the past four decades — Kossin, Knapp, Olander & Velden, PNAS (2020)"
    url: "https://www.pnas.org/doi/10.1073/pnas.1920849117"
  - title: "Correction for Kossin et al. — PNAS (2020)"
    url: "https://www.pnas.org/doi/10.1073/pnas.2021573117"
  - title: "Advanced Dvorak Technique-Hurricane Satellite (ADT-HURSAT) — NOAA NCEI product page"
    url: "https://www.ncei.noaa.gov/products/advanced-dvorak-technique-hurricane-satellite"
  - title: "ADT-HURSAT Technical Documentation (February 2026) — NOAA NCEI"
    url: "https://www.ncei.noaa.gov/sites/default/files/2026-02/ADTHURSAT%20Technical%20Documentation%20-%202.3.26.pdf"
  - title: "Typhoon intensity ReAnalysis (TyRA) — Ito, Aizawa, Shimada, Kawabata & Yamaguchi, arXiv preprint (July 2026)"
    url: "https://arxiv.org/abs/2607.11220"
  - title: "Basin-Specific Changes and Intensity of Tropical Cyclones — Welch, arXiv preprint v3 (October 2026)"
    url: "https://arxiv.org/abs/2606.22518"
  - title: "Aircraft Reconnaissance — Hurricanes: Science and Society, University of Rhode Island"
    url: "https://hurricanescience.org/science/observation/aircraftrecon/index.html"
---

In February this year, NOAA's National Centers for Environmental Information published a new archived dataset of tropical cyclone intensities: ADT-HURSAT version 1, global, every storm from May 1978 to December 2024. Under "Known Issues," the product page says this:

> This dataset should not be used to determine actual storm intensities.

And a little further down: for an individual storm, use IBTrACS instead.

I find that a remarkable thing for a government data archive to say about its own flagship release, and the reason it says it is the most interesting thing I have read this week. ADT-HURSAT is not a worse attempt at the thing IBTrACS does well. It is a deliberately degraded record, built by taking satellite imagery that has improved enormously since 1978 and throwing away the improvements on purpose, because the improvements are exactly what makes the good record useless for the one question people most want to ask: are tropical cyclones getting stronger?

## The ladder down

The raw material is HURSAT-B1, geostationary infrared imagery centred on historical storm positions, drawn from the International Satellite Cloud Climatology Project. The satellite list is a forty-six-year archaeology of orbital hardware: SMS-2, GOES-1 through 18, Meteosat-2 through 11, GMS-1 through 5, MTSAT-1R, FY-2C and 2E, Himawari-8 and 9. Each of those instruments sees a storm differently — pixel size, calibration, viewing angle.

So the imagery is resampled to a single common grid: **8 km spatial resolution, 3-hourly**, with cross-satellite recalibration on top. Only infrared is used; the visible and other channels in HURSAT-B1 are left aside. Kossin and colleagues, whose 2020 PNAS paper is the methodological parent of the NOAA product, went further and used only the primary synoptic hours — 00, 06, 12, 18 UTC — to match the 6-hourly cadence of the operational best-track files. They also removed data from geostationary satellites sitting near 60°E, because in 1998 new coverage appeared over a previously unwatched stretch of the Indian Ocean and introduced a viewing-angle discontinuity in the middle of the record.

Then the Advanced Dvorak Technique — a regression scheme that reads intensity off infrared cloud patterns, descended from Vernon Dvorak's 1970s pattern-matching method — runs over that deliberately coarsened imagery. NOAA's technical documentation notes in passing that operational ADT normally works from 30-minute imagery. The climate record is six times coarser in time than what forecasters use, and the gap in space is wider still.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">8 km</div><div class="sl mono">resampled pixel</div><div class="sn">all satellites, 1978–2024</div></div><div class="stat"><div class="sv">3 h</div><div class="sl mono">image interval</div><div class="sn">operational ADT uses 30 min</div></div><div class="stat"><div class="sv">8%</div><div class="sl mono">per decade</div><div class="sn">major-hurricane exceedance, 95% CI 2–15%</div></div><div class="stat"><div class="sv">225,000</div><div class="sl mono">intensity estimates</div><div class="sn">across about 4,000 storms</div></div></figure>


## Why anyone would do this

Because the obvious alternative is worse in a way that is harder to see. The operational best-track archives are the best available estimate of what each storm actually did, and that is precisely the problem: what the best estimate is made *of* has changed. Routine aircraft reconnaissance of western North Pacific typhoons ended in 1987; Atlantic reconnaissance continues to this day. Geostationary coverage, microwave sounders, scatterometers and the analysts' own techniques have all improved unevenly across basins and decades. A record assembled from the best information available at each moment will show storms getting better-measured, and some fraction of that will look exactly like storms getting stronger.

Kossin et al. ran their analysis on 1979–2017 — about 225,000 ADT-HURSAT intensity estimates across roughly 4,000 storms, with 1978 and 1980 dropped for missing eastern-hemisphere coverage — and restricted it to estimates at hurricane strength or above, because below about 65 kt an eye can form under cirrus that infrared cannot see through. Comparing the first half of the record to the second, the probability that a given hurricane-or-stronger observation was at major-hurricane intensity rose from 0.27 to 0.31: a 15% relative increase over the period, about 8% per decade, with a 95% confidence interval of 2 to 15% per decade after they allowed for serial correlation by assuming an 18-hour decorrelation time and cutting their degrees of freedom by a factor of three. A different cut of the same data — three-year bins, Theil-Sen slope, Mann-Kendall test — gives about 6% per decade at p = 0.02.

The same calculation on the best-track data gives roughly 17% per decade. The authors' inference from that gap is the load-bearing claim of the paper: that the trends in the best track "are about equally split between actual physical trends and spurious technology-based trends." It is an elegant argument, and it is a subtraction between two imperfect records, which is a fragile kind of arithmetic.


<figure class="fig bars"><figcaption class="mono">Change in major-hurricane exceedance probability, % per decade (1979–2017)</figcaption><div class="rows"><div class="brow"><div class="blabel">ADT-HURSAT, global</div><div class="btrack"><div class="bfill" style="width:16.33%" title="ADT-HURSAT, global · 8%, 95% CI 2–15"></div></div><div class="bval mono">8%, 95% CI 2–15</div></div><div class="brow"><div class="blabel">Best track, global</div><div class="btrack"><div class="bfill" style="width:34.69%" title="Best track, global · 17%, &gt;99% conf."></div></div><div class="bval mono">17%, &gt;99% conf.</div></div><div class="brow"><div class="blabel">ADT-HURSAT, Southern Indian</div><div class="btrack"><div class="bfill" style="width:36.73%" title="ADT-HURSAT, Southern Indian · 18%, &gt;90% conf. only"></div></div><div class="bval mono">18%, &gt;90% conf. only</div></div><div class="brow"><div class="blabel">ADT-HURSAT, North Atlantic</div><div class="btrack"><div class="bfill" style="width:100.00%" title="ADT-HURSAT, North Atlantic · 49%, &gt;99% conf."></div></div><div class="bval mono">49%, &gt;99% conf.</div></div></div></figure>


## Where it gets thinner than the headline

The global number is not evenly distributed, and the paper is candid about it. The North Atlantic trend is 49% per decade at better than 99% confidence. The Southern Indian Ocean reaches 18% per decade but clears only the 90% bar. Everything else fails to reach significance: the eastern North Pacific at 4%, the South Pacific at 8%, the western North Pacific at *minus* 1%, the northern Indian Ocean at zero and based, as the authors say, on a small sample. So it is a global trend in the sense that the global pool shows it, but the signal lives mostly in the one basin where everybody agrees large multidecadal swings exist — a point the authors make themselves, attributing the Atlantic behaviour to quasi-oscillatory internal factors and to external ones, natural and anthropogenic, without separating them.

Then there is the question of which direction the homogenized record is biased, where I found the literature pulling against itself.

Kossin et al. flag one direction: at 8 km, eyes smaller than about 20 km are hard to resolve, so the technique misses the most intense storms, which would make the trend they report *too small*. They call this difficult to quantify and leave it an open question — honest, and a reminder that the stated interval is not the whole uncertainty.

A typhoon reanalysis posted in July this year by Kosuke Ito and colleagues, submitted to *Journal of Climate*, pushes the other way. They rebuilt western North Pacific intensities for 1987–2024 by fitting Dvorak CI numbers to 873 aircraft pressure observations from 51 typhoons flown in 1981–86, back when the aircraft were still going. Checked against those direct measurements, they report that ADT-HURSAT "tends to overestimate the intensity of very intense typhoons and underestimate the intensity of weak-to-moderate typhoons" — because its pressure conversion is essentially Dvorak's 1984 table, which they find assigns central pressures about 20 hPa lower than the aircraft actually measured in the 890–930 hPa range — that is, it makes the strongest storms look stronger than they were. Their own basin-wide result is a slight decrease in intense typhoons that is not statistically significant, with weakening in the eastern part of the basin that does carry some significance and that they attribute to storms being born further northwest and so dying younger.

These two concerns are not simply additive, and I cannot tell you which dominates. One says the record flattens the top end; the other says its top end is miscalibrated upward in the basin with the longest aircraft baseline. I would like to have read the supplement where Kossin et al. put their point-by-point comparison against the best track; the main text only calls the fit "far-from-perfect" and gives no mean bias in knots, and the supplement was not reachable. A published correction to the paper exists as well, which I could not open — PNAS turned away every route I tried — so everything above comes from the original text, and I cannot tell you whether the correction touched any of it.

The sharpest test I found is simply running the method on more years. Ivo Welch, in a preprint revised last month, rebuilt the ratio from ADT version 9.0 through 2024 and found that Kossin's half-sample difference was no longer statistically significant over the very same 1979–2017 window, with the rise between halves about half as large; that the worldwide trend over 1990–2024 is not significant; and that the North Atlantic remains the clearest case, at 5.4 percentage points per decade and a p-value of 0.063. He also notes that the 1997 split date coincides with a discrete jump in the Atlantic ratio. The detail I enjoyed most is the least glamorous: the newer ADT version classifies winds at exactly 64 and 96 kt, where the original record's 5-kt grid effectively cut at 65 and 100, and that bookkeeping difference alone shifts the mean ratio. Category boundaries are not facts about the atmosphere.

## What I take from it

Not that the result is wrong. The direction is physically expected, the Atlantic signal is robust across every version I read, and Welch's own framing is that an insignificant worldwide trend does not establish the absence of one. What I take is a method I had not properly understood before: when the instrument improves faster than the signal, the only way to measure the signal is to build an instrument that has not improved — and then to accept that the resulting series is meaningful only in differences, and meaningless in levels.

That is what NOAA's warning label actually says, stripped of the bureaucratic phrasing. The dataset is wrong about every individual storm, consistently, on purpose, which is the entire source of its value.


<figure class="fig pull"><p>A dataset built to be wrong the same way every year is the only honest way to ask whether something changed.</p></figure>


The risk is not in the archive. It is that the label stays attached to the dataset while the number detaches and travels — an 8%-per-decade figure arriving somewhere downstream without the 2-to-15 interval, without the basin table showing that four of six basins contribute nothing significant, and without the sentence explaining that the number exists only because someone deliberately degraded forty-six years of satellite imagery to the quality of its worst year.
