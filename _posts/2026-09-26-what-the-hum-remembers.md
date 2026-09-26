---
layout: post
title: "What the Hum Remembers"
dek: "A dispute over who pays for Kosovo's electricity left every mains-driven clock in continental Europe six minutes slow in 2018. The control loop that fixes that exists to make grid frequency boring — which is exactly what a whole branch of forensics needs it not to be."
description: "A dispute over who pays for Kosovo's electricity left every mains-driven clock in continental Europe six minutes slow in 2018. The control loop that fixes that exists to make grid frequency boring — which is exactly what a whole branch of forensics needs it not to be."
date: 2026-09-26
tags: ["power grids", "forensics", "audio", "control systems"]
accent: "#8F4A1E"
accent_dark: "#E6A16A"
sources:
  - title: "Continuing frequency deviation in the Continental European Power System originating in Serbia/Kosovo — ENTSO-E"
    url: "https://www.entsoe.eu/news/2018/03/06/press-release-continuing-frequency-deviation-in-the-continental-european-power-system-originating-in-serbia-kosovo-political-solution-urgently-needed-in-addition-to-technical/"
  - title: "Frequency deviations in Continental Europe originating from Kosovo started again — ENTSO-E"
    url: "https://www.entsoe.eu/news/2018/07/09/frequency-deviations-in-continental-europe-originating-from-kosovo-started-again-technical-measures-kicked-off-to-keep-time-delay-below-60-seconds/"
  - title: "Frequency and grid time — Swissgrid"
    url: "https://www.swissgrid.ch/en/home/operation/regulation/frequency.html"
  - title: "Time and Frequency from Electrical Power Lines (Lombardi) — NIST"
    url: "https://tf.nist.gov/general/pdf/2895.pdf"
  - title: "Manual Time Error Correction in the Eastern Interconnection (May 2020) — NAESB"
    url: "https://www.naesb.org/pdf4/weq_bps052220w6.pdf"
  - title: "Time Monitoring Reference Document, Version 5 — NAESB WEQ"
    url: "https://naesb.org/pdf4/weq_bps062520w1.pdf"
  - title: "Factors affecting forensic electric network frequency matching — Digital Communications and Networks (2023)"
    url: "https://www.sciencedirect.com/science/article/pii/S2352864823000226"
  - title: "Using the ENF Criterion for Determining the Time of Recording of Short Digital Audio Recordings (Huijbregtse & Geradts)"
    url: "https://link.springer.com/chapter/10.1007/978-3-642-03521-0_11"
  - title: "Electrical network frequency analysis — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Electrical_network_frequency_analysis"
  - title: "The hidden electrical noise that can catch criminals — Crime+Investigation UK"
    url: "https://www.crimeandinvestigation.co.uk/articles/hidden-electrical-noise-can-catch-criminals"
---

In the middle of January 2018, clocks across continental Europe started running slow. Not the ones on phones, which take their time from a satellite or a time server. The slow ones were the cheap ones — oven timers, microwave displays, bedside radio alarms, the little display on a coffee machine. Anything that counts the alternating current itself instead of keeping its own oscillator. By the first week of March they were roughly six minutes behind, everywhere from Lisbon to Ankara.

ENTSO-E, the association of European transmission system operators, put out a press release on 6 March naming the cause with unusual bluntness. The deviations originated in the control block covering Serbia, Macedonia and Montenegro, and specifically in the long-running dispute between Serbian and Kosovar authorities over who pays for electricity consumed in northern Kosovo. Somebody was drawing power that nobody was generating to match. Over roughly seven weeks the synchronous area — 25 countries, one giant interlocked machine — had run 113 GWh short, at an average frequency of about 49.996 Hz against a nominal 50.


<figure class="fig stats cols-3"><div class="stat"><div class="sv">113 GWh</div><div class="sl mono">energy the grid ran short</div><div class="sn">ENTSO-E, mid-Jan to March 2018</div></div><div class="stat"><div class="sv">~6 min</div><div class="sl mono">how far mains clocks fell behind</div><div class="sn">across 25 countries</div></div><div class="stat"><div class="sv">49.996 Hz</div><div class="sl mono">mean frequency over the episode</div><div class="sn">nominal is 50.000</div></div></figure>


Four thousandths of a hertz. That is the whole story: a rounding error in the fourth decimal place, sustained for seven weeks, and the continent's microwaves lost six minutes.

## Why a wall clock is an integral

A synchronous clock motor does not measure time. It counts cycles and divides. Fifty oscillations of the mains is one second of what the industry calls grid time, and the accuracy of that second depends entirely on the grid delivering exactly fifty oscillations in exactly one second of real time. It does not, ever, instant to instant — frequency sags when load exceeds generation and rises when it doesn't, continuously, all day. What makes the clock work is that the errors are made to cancel.

This is a control problem with a peculiar shape. Nobody cares about the instantaneous frequency for timekeeping purposes; what matters is the integral of the deviation, accumulated since the epoch. Grid operators therefore run a second, slower control loop sitting on top of the fast one: when the accumulated error passes a threshold, they deliberately bias the whole synchronous area off-nominal in the opposite direction until the debt is repaid. Swissgrid, which monitors frequency for continental Europe through a network of metering stations from Portugal to Turkey and Denmark to Sicily, sets the threshold at twenty seconds and the correction at 49.990 or 50.010 Hz depending on which way the clocks have drifted.

North America does the same thing with different numbers, and has been doing it since electric clocks became a mass product. Henry Warren patented the synchronous clock motor in 1917 and built a business on it; by 1947, according to a NIST review of the practice, Warren master clocks regulated over 95% of the electric lines in the United States. The tail wagged the dog. Utilities kept their frequency honest because their customers' clocks depended on it, and the correction thresholds — 10 seconds on the Eastern Interconnection, 5 on the Western — were set to keep a bedside alarm within sight of the truth.


<figure class="fig bars"><figcaption class="mono">Grid time error tolerated before correction, seconds</figcaption><div class="rows"><div class="brow"><div class="blabel">Western Interconnection (US)</div><div class="btrack"><div class="bfill" style="width:8.33%" title="Western Interconnection (US) · 5 s"></div></div><div class="bval mono">5 s</div></div><div class="brow"><div class="blabel">Eastern Interconnection (US)</div><div class="btrack"><div class="bfill" style="width:16.67%" title="Eastern Interconnection (US) · 10 s"></div></div><div class="bval mono">10 s</div></div><div class="brow"><div class="blabel">Continental Europe, routine</div><div class="btrack"><div class="bfill" style="width:33.33%" title="Continental Europe, routine · 20 s"></div></div><div class="bval mono">20 s</div></div><div class="brow"><div class="blabel">Continental Europe, 2018 emergency programme</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Continental Europe, 2018 emergency programme · 60 s"></div></div><div class="bval mono">60 s</div></div><div class="brow"><div class="blabel">ERCOT</div><div class="btrack"><div class="bfill unk" style="width:100%" title="ERCOT · not stated in the reference document"></div></div><div class="bval mono muted">not stated in the reference document</div></div></div></figure>


What surprised me is how recently the Americans tried to stop. The argument for stopping is decent: almost nothing important depends on mains-counted time any more, and deliberately biasing an entire interconnection off-nominal for four hours at a stretch is not free. FERC approved the retirement of BAL-004, the NERC reliability standard mandating time error correction, on 18 January 2017. The same NIST review notes, using US Naval Observatory monitoring data, that without corrections the Eastern Interconnection would have drifted about seven and a half minutes between the daylight saving switches of March and November 2016.

Except the practice did not actually end. Time error correction survived as a NAESB business practice standard rather than a reliability standard, and when the question came back around in May 2020 — MISO wanted it gone — the recommendation was to keep it. The stated reason is the part I keep turning over: the Eastern Interconnection was accumulating roughly twenty seconds of time error every three to four days, an inadvertent-energy payback schedule that might have explained it had been eliminated that same month, the error kept accruing anyway, and nobody could say why. *Data does not support the retirement of TEC in the EI at this time.* A continent-scale machine is losing time at a steady, measurable, unexplained rate, and the fix is to keep applying the correction while the root cause stays open.

## The same wobble, read backwards

Here is the turn that made me want to write this up. The correction machinery exists because the deviation is a nuisance. But somewhere else entirely, the deviation is the entire product.

Mains hum leaks into audio recordings — 50 Hz in Europe, 60 in North America, plus harmonics — and it leaks in carrying the frequency's moment-to-moment wobble. That wobble is shared across a whole synchronous area and never repeats. Which means a recording with audible hum carries an unforgeable timestamp, provided somebody has been writing down what the grid was doing. Catalin Grigoras published the criterion in 2005; the Metropolitan Police started keeping a continuous frequency record the same year, Bavarian police in 2010; Alan Cooper published an automated matching approach through the Audio Engineering Society in 2008. The technique is called Electric Network Frequency analysis, and it does more than date a file: because an edit splices two non-adjacent stretches of grid history together, a discontinuity in the recovered ENF trace is evidence of tampering that a forger would have to reconstruct the national grid to fake.

So the clock and the fingerprint want opposite things from the same signal, and — this is the bit I had wrong when I started — they are not actually in conflict. Time error correction drives the *integral* of the deviation toward zero. ENF reads the *shape* of the deviation minute to minute. A four-hour bias at 49.990 Hz doesn't erase the wobble; it adds a distinctive step to it. The correction loop is slow and deliberate, the fingerprint lives in the fast noise, and the two pass through each other. One signal, two customers, no argument.

What could genuinely break the fingerprint is the thing nobody designed either loop around: the generation mix. Synchronous machines give a grid rotational inertia, and inertia is what makes frequency wander smoothly and distinctively. Inverter-based generation supplies none of it natively, and the response is a large and active literature on synthetic inertia and fast frequency response — control schemes whose whole purpose is to make frequency deviate *less*. Whether that has measurably reduced how distinguishable an hour of ENF trace is from any other hour, I could not find out. Plenty of papers on frequency stability under high renewable penetration; none I found that runs the question the forensic direction.

## Where this is thinner than it sounds

The accuracy figures for ENF matching are good and they are also narrower than they look. The most careful study I read, in *Digital Communications and Networks* in 2023, isolates recording length as the dominant factor and signal-to-noise ratio as the dominant external one: at roughly five minutes of usable audio, matching accuracy runs near 90–100%; at one to two minutes it collapses toward 20–50%. The number that matters and gets dropped in retelling is the search space those were measured against — a one-week reference window. Casework does not offer a one-week window. It offers a database going back years, and the failure mode there is self-similarity: with enough history, some other stretch of grid time resembles your recording well enough to compete. Huijbregtse and Geradts flagged exactly this, along with fixed frequency offsets introduced by recording equipment, for recordings under ten minutes. Scaling from a week to a decade is not a detail.

The other absence is bigger. I went looking for a black-box or proficiency study giving an error rate for ENF analysis as practised by examiners on real casework — the kind of study that exists, contested but published, for latent fingerprints and firearms comparison. I did not find one. What I found instead was the same handful of illustrative successes moving between articles: a 2012 South London firearms prosecution in which three men received a combined 33 years and ENF authentication of the recordings was part of the case, and a line calling ENF the most significant development in audio forensics since Watergate, which appears in several places with no attribution I could follow back to a person. That is press coverage, not a validation literature. It may well be that the technique is as sound as its advocates say — the physics is genuinely on its side, more so than for most pattern-matching forensics — but "the physics is sound" and "practitioners applying it get the right answer at a measured rate" are different claims, and only one of them has numbers.

---

One loose end I could not close. ENTSO-E said in March 2018 that ceasing the deviation was step one and repaying the 113 GWh was step two, on a timeline to be decided. The deviations came back in July and a new automatic compensation programme kicked in when grid time drifted past sixty seconds. I could not establish from public material when, or whether, the original six minutes were fully paid back. The grid keeps a running ledger of every second it owes the continent, and as far as I can tell nobody publishes the balance.
