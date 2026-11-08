---
layout: post
title: "Five Thousandths of a Mach Number"
dek: "The FAA has proposed letting aircraft fly supersonic over the United States so long as the boom reaching the ground stays under 0.11 pounds per square foot. That number came from what one trick can achieve, and the trick balances on a margin thinner than the weather."
description: "The FAA has proposed letting aircraft fly supersonic over the United States so long as the boom reaching the ground stays under 0.11 pounds per square foot. That number came from what one trick can achieve, and the trick balances on a margin thinner than the weather."
date: 2026-11-08
tags: ["sonic booms", "aviation regulation", "acoustics", "atmospheric uncertainty"]
accent: "#3C7A1E"
accent_dark: "#9BD96A"
sources:
  - title: "Enabling Supersonic Overland Flight, FAA NPRM at 91 FR 40470 — Federal Register"
    url: "https://www.federalregister.gov/documents/2026/07/02/2026-13440/enabling-supersonic-overland-flight"
  - title: "Mach Cutoff Analysis and Results from NASA's Farfield Investigation of No-boom Thresholds — NASA NTRS"
    url: "https://ntrs.nasa.gov/api/citations/20160007348/downloads/20160007348.pdf"
  - title: "Oklahoma City sonic boom study, NORC Report No. 101 — National Opinion Research Center"
    url: "https://www.norc.org/PDFs/publications/NORCRpt_101.pdf"
  - title: "Quantifying the Speed Advantage of Mach-Cutoff Flight — DLR"
    url: "https://elib.dlr.de/143260/1/Supersonic%20Overland%20Without%20a%20Sonic%20Boom.pdf"
  - title: "Concorde Booms and the Mysterious East Coast Noises — Acoustics Today"
    url: "https://acousticstoday.org/wp-content/uploads/2015/06/Concorde-Booms-and-the-Mysterious-East-Coast-Noises-Peter-H-Rogers-and-Domenic-J.-Maglieri.pdf"
  - title: "X-59 sonic boom simulation and case study (Doebler) — NASA NTRS"
    url: "https://ntrs.nasa.gov/api/citations/20210019951/downloads/Doebler_X59_simulation_and_case_study_POMA_022004_1.pdf"
  - title: "ASCENT Project 042: Acoustical Model of Mach Cut-off Flight, final report"
    url: "https://s3.wp.wsu.edu/uploads/sites/2479/2023/07/ASCENT-Project-042_GT_Final-Report.pdf"
  - title: "Comments on the supersonic NPRM, docket FAA-2026-6935 — Earthjustice et al."
    url: "https://earthjustice.org/wp-content/uploads/2026/08/for-filing-2026.08.14-comments-on-supersonic-nprm_with-exhibit-list-1.pdf"
  - title: "Lockheed Martin X-59 Quesst — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Lockheed_Martin_X-59_Quesst"
  - title: "Boom or No Boom could determine overland operations — AirInsight"
    url: "https://airinsight.com/boom-or-no-boom-could-determine-overland-operations/"
---

In July the FAA proposed to undo something I had quietly assumed was permanent. Since 1973, 14 CFR 91.817 has banned civil flight above Mach 1 over the United States, and it does it the simple way: by speed. Not by how loud you are — by how fast. The proposed rule, published on 2 July 2026 at 91 FR 40470, would replace that with a performance test. Fly as fast as you like over Kansas, provided the sonic boom overpressure that arrives at the ground stays at or below **0.11 pounds per square foot**.

I spent an afternoon trying to find out where 0.11 came from, and the answer turned out to be more interesting, and considerably thinner, than I expected.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">0.11 psf</div><div class="sl mono">proposed surface limit</div><div class="sn">about 5.3 pascals</div></div><div class="stat"><div class="sv">0.005</div><div class="sl mono">Mach error that swings ground level 15 dB</div><div class="sn">NASA FaINT</div></div><div class="stat"><div class="sv">0.05</div><div class="sl mono">cutoff Mach shift over six hours</div><div class="sn">same location, DLR</div></div><div class="stat"><div class="sv">36</div><div class="sl mono">cutoff passes in the key dataset</div><div class="sn">three days, one aircraft</div></div></figure>


## The trick the rule is built around

The proposal expects early operations to work by **Mach cutoff**, and the physics is lovely. The speed of sound in air depends on temperature, and the effective speed along a ray depends on the wind it is travelling through. Both normally fall with altitude. A shock wave leaving an aircraft at Mach 1.1 therefore propagates downward into air that carries it more slowly, and its rays bend — the same refraction that makes a hot road shimmer, turned on its side. Below some cutoff Mach number the rays never make it to the surface at all. They flatten out at a caustic some thousands of feet up and curl back skyward, leaving a shadow zone underneath.

What reaches the ground in that shadow zone is not silence and is not a boom. It is the exponentially decaying tail of a wave that turned around overhead: an **evanescent wave**, a low rumble that NASA has compared to background street noise. The rule's own language is careful here in a way the press coverage is not — "Boomless Cruise", Boom Supersonic's name for this, describes a boom that gets refracted away, not a boom that was never made.

The speeds involved are modest. A German Aerospace Center (DLR) study simulating cutoff missions across a year of atmospheres found a mean cutoff Mach of about 1.11, with a maximum around 1.37. On the routes modelled that bought 12.5 to 13 percent off a Mach 0.95 cruise — roughly 38 minutes — for a fuel penalty of 8 to 34 percent. Worth having. Not transformative.

## The knife edge

The flight test the FAA leans on is NASA's Farfield Investigation of No-boom Thresholds, FaINT, flown at Rogers Dry Lakebed at Edwards in November 2012. An F-18B made supersonic passes between 34,400 and 39,300 feet at Mach 1.128 to 1.174, over a line of sixty microphones spaced 125 feet apart, with an instrumented motorglider loitering in the shadow zone to catch the residual from inside it. Six flights, three days, 36 cutoff passes. Flight 6 was dropped from the analysis because the winds were too high.

Measured overpressures across those passes ran from 0.01 to 0.62 psf, with perceived sound exposure levels from 55 to 91 dB. When the computed cutoff altitude sat comfortably above the ground — more than one safe-altitude margin, in the paper's terms — the loudest thing the array recorded was 0.09 psf at 68 dB.

Then come the two sentences in that paper that reframed the whole rule for me. Perturbing the radiosonde profile by 3 knots of wind speed, 10 degrees of wind direction and 3 °C of temperature produced more than 20 dB of dispersion in ground level above the mean. And an error of roughly **0.005** in the difference between the cutoff Mach number and the aircraft's actual Mach number moves ground level by 15 dB or more.

Five thousandths of a Mach number is about three knots of true airspeed up there. That is the precision with which you have to know a quantity computed from a forecast atmosphere.

Now set that beside the DLR paper's measurement of how still the atmosphere holds. Taking atmospheric data six hours apart, they found the cutoff Mach number at the *same positions* differed by at least 0.05. Their own simulation flew with a safety buffer of 0.005 Mach — exactly the margin FaINT says matters, and one tenth of the drift they measured between snapshots.

The rule's answer to this is that an operator "must account for the uncertainty in the terrain, actual weather, and atmospheric parameters", possibly monitoring real-time winds, with speed limits validated against a tool like NASA's PCBoom. It does not say how much margin that requires. That is the part I would want written down, because it is the only part that determines whether the 0.11 ever gets exceeded.

## Where 0.11 actually comes from

The FAA says it set the threshold "based on the FaINT and NTSC datasets" — FaINT plus a 1980 DOT Transportation Systems Center study of Concorde secondary booms over New England. Neither of those identifies 0.11 psf as anything. The closest number in FaINT is the 0.09 psf residual above; the paper also reproduces a prior author's bands of 0.00–0.08 psf for well-cutoff cases and 0.04–0.21 psf for marginal ones, while noting that author never defined what "relatively small intensity" meant. And 0.11 psf is 5.3 pascals, which sits squarely in the middle of the 1–10 Pa range typical of the stratospheric secondary booms the New England study was chasing.

To the agency's credit, it says why in plain words: "due to the lack of integrated metric data available to determine a tolerable level of sonic boom at the surface", it adopted the level at which Mach cutoff had been shown to abate a boom, and made that the limit. Then it asks the public for data supporting any other number.

Read that again, because it is the whole thing. The limit is not a finding about people. It is a finding about a technique — the level the mitigation happened to achieve in one campaign — promoted to a legal ceiling because nothing better was available. Commenters opposing the rule call it technology-driven rather than health-driven, and on this point I think they are simply describing it accurately.


<figure class="fig bars"><figcaption class="mono">Peak overpressure, psf · log scale</figcaption><div class="rows"><div class="brow"><div class="blabel">FaINT, loudest residual when well cut off</div><div class="btrack"><div class="bfill" style="width:1.50%" title="FaINT, loudest residual when well cut off · 0.09 psf"></div></div><div class="bval mono">0.09 psf</div></div><div class="brow"><div class="blabel">Proposed FAA surface limit</div><div class="btrack"><div class="bfill" style="width:1.50%" title="Proposed FAA surface limit · 0.11 psf"></div></div><div class="bval mono">0.11 psf</div></div><div class="brow"><div class="blabel">FaINT, loudest measured pass</div><div class="btrack"><div class="bfill" style="width:1.50%" title="FaINT, loudest measured pass · 0.62 psf"></div></div><div class="bval mono">0.62 psf</div></div><div class="brow"><div class="blabel">Oklahoma City 1964, median, final period</div><div class="btrack"><div class="bfill" style="width:63.35%" title="Oklahoma City 1964, median, final period · 1.60 psf"></div></div><div class="bval mono">1.60 psf</div></div><div class="brow"><div class="blabel">Concorde primary boom, typical</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Concorde primary boom, typical · about 100 Pa"></div></div><div class="bval mono">about 100 Pa</div></div><div class="brow"><div class="blabel">Level where community response measured near the limit</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Level where community response measured near the limit · never run"></div></div><div class="bval mono muted">never run</div></div></div></figure>


## The one time anybody asked

There is exactly one large dose-response dataset for sonic booms over a populated place, and it is 62 years old. From February to July 1964 the FAA ran eight booms a day over Oklahoma City — 1,253 in all — and had NORC interview nearly 3,000 adults three times. Median overpressures under the track were 1.13 psf for the first eleven weeks, 1.23 for the next eight, and 1.60 for the final seven. The share reporting more than a little annoyance climbed from 37 to 44 to 56 percent. By the last round, 27 percent said they could not learn to live with it. The FAA logged about 12,400 calls.

Those levels are more than ten times the proposed limit, from a population that knew the booms were scheduled. Nobody has run the equivalent study anywhere near 0.11 psf, which is why one bar in the chart above is hatched rather than guessed. It is the bar I would most want filled in.

## The metric is the deeper problem

Pounds per square foot is a peak pressure, and peak pressure is a poor predictor of how a boom is experienced. What a listener responds to is rise time and spectrum. NASA's X-59 — which first flew in October 2025 and went supersonic on 5 June 2026 — is designed to a target of 75 dB on the Stevens Perceived Level scale, computed from one-third-octave band loudness in sones, precisely because overpressure alone doesn't capture the thing being regulated. The FaINT paper says as much directly, and proposed perceived level, not overpressure, as the metric worth using.

The clearest illustration is in the secondary booms themselves. Their energy is confined below about 50 Hz; they are generally inaudible, yet they rattle buildings, which is how they became "mysterious East Coast noises" in 1977 and got blamed on Concorde before being mostly absolved. A primary N-wave at the same overpressure carries energy above 1 kHz and sounds like a gunshot. One number, two unrelated experiences. A rule written in psf cannot tell them apart, and the FAA's proposal applies the same 0.11 to primary booms, direct secondaries and indirect secondaries alike.

## What else is missing

Focus booms — the amplified kind from steep turns and push-overs — are left out, on the grounds that they are "limited in area and duration". Evanescent waves below the limit are explicitly permitted, with regulation possibly to follow. The FAA-sponsored research project built to produce an acoustical model of Mach cutoff flight published sensitivity trends without error bounds, called its results preliminary and likely to change, and recorded that the relevant task was not continuing into the next period. And the proposal's list of references includes a company press release about a February 2025 demonstration flight, whose underlying measurements I could not find published anywhere.

My own reading has gaps I should own. The 1980 New England report is on DTIC and DTIC would not serve it to me, so its numbers here come through a review article by two of the acousticians involved in that era and through a comment filed in the docket; the filing is an advocacy document and I have used it for pointers to sources rather than for conclusions. The claim that ICAO rejected overpressure as a regulatory metric in 2014, and the Penn State finding that a 1 percent change in cruise speed can produce a focused boom, both reach me that way and I have not seen the originals.

## Why I keep thinking about it

This is a very clean example of a number acquiring authority by being written down. Within a year, 0.11 psf will be quoted as "the FAA's sonic boom limit" in the tone reserved for findings about human hearing. It is nothing of the kind. It is an engineering waypoint derived from 36 passes of one F-18 over a dry lakebed on three days in 2012, bridged to a 46-year-old Concorde study by a judgement the agency chose not to show, and the agency says so itself if you read to the middle of the preamble.

That is not a scandal. It is what you do when you are told to regulate and have no dose-response curve. The 1973 rule's reasoning, as quoted in the docket, was that there was "no basis for establishing an 'acceptable' overpressure limit" — and the honest reading of the new proposal is not that the basis arrived, but that the agency decided a provisional number beats a speed ban while the real metric is still being built. The X-59's community overflights are supposed to supply that curve, with results going to ICAO around 2027 and the international en route standard not expected until roughly 2031.

The study I actually want, though, is cheaper than any of that. Take a year of real forecasts and real routes, compute the cutoff plan six hours out the way an operator would, then check against the analysis atmosphere how often the ground would have seen more than 0.11 psf. It is a retrospective calculation with existing data and existing models. As far as I can tell, nobody has published it — and until somebody does, the number in the rule is a limit whose probability of being exceeded is unknown by construction.
