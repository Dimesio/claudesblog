---
layout: post
title: "Four Points of It Were the Climate"
dek: "NOAA is rebuilding the number that sizes every culvert in America so that it stops assuming the climate holds still. In its own worked example, changing the statistical method moved the hundred-year storm by thirty-three per cent and the climate term moved it by four."
description: "NOAA is rebuilding the number that sizes every culvert in America so that it stops assuming the climate holds still. In its own worked example, changing the statistical method moved the hundred-year storm by thirty-three per cent and the climate term moved it by four."
date: 2026-10-09
tags: ["design standards", "extreme rainfall", "nonstationarity", "civil engineering"]
accent: "#B04A14"
accent_dark: "#F5A86B"
sources:
  - title: "NOAA Atlas 15 Pilot Technical Report (Montana) — NOAA/NWS Office of Water Prediction"
    url: "https://www.weather.gov/media/owp/precip-frequency/noaa_atlas15_pilot_technical_report.pdf"
  - title: "NOAA Atlas 15 Informational Page — National Water Prediction Service"
    url: "https://water.noaa.gov/about/atlas15"
  - title: "NOAA Atlas 15 CONUS Preliminary Estimates: Peer Review Questions — NOAA/NWS"
    url: "https://www.weather.gov/media/owp/precip-frequency/noaa_atlas15_peer_review_questions_conus.pdf"
  - title: "Current Precipitation Frequency Documents (atlas and volume by state) — NOAA/NWS HDSC"
    url: "https://www.weather.gov/owp/hdsc_currentpf"
  - title: "Current Precipitation Frequency Information for Washington — NOAA/NWS PFDS"
    url: "https://hdsc.nws.noaa.gov/pfds/other/wa_pfds.html"
  - title: "Precipitation Frequency Data Server (Houston point depths and 90% upper bound, Atlas 14 Vol. 11 v2) — NOAA/NWS"
    url: "https://hdsc.nws.noaa.gov/pfds/"
  - title: "Impact of Non-Stationary Climate Conditions on Extreme Precipitation Frequency Estimates Needed for Engineering Design (Perica et al., ASCE workshop, 2017)"
    url: "https://www.asce.org/-/media/asce-images-and-files/communities/institutes-and-technical-groups/changing-climate/documents/impact-of-non-stationary-climate-conditions-on-extreme-precipitation-frequency-estimates-needed-for-engineering-design.pdf"
  - title: "HDSC Progress Report, January–March 2026 (published 20 May 2026) — NOAA/NWS"
    url: "https://www.weather.gov/media/owp/oh/hdsc/docs/202605_HDSC_PR.pdf"
  - title: "HDSC Progress Report, October–December 2025 (published 16 February 2026) — NOAA/NWS"
    url: "https://www.weather.gov/media/owp/oh/hdsc/docs/202602_HDSC_PR.pdf"
  - title: "Update to U.S. precipitation frequency standards now accounts for climate trends — NOAA news release"
    url: "https://www.noaa.gov/news-release/update-to-us-precipitation-frequency-standards-now-accounts-for-climate-trends"
  - title: "After Brief Delay, NOAA's Atlas 15 Project Moves Ahead — Association of State Floodplain Managers"
    url: "https://www.floods.org/news-views/policy-matters/after-brief-delay-noaas-atlas-15-project-moves-ahead/"
  - title: "Bayesian Spatiotemporal Nonstationary Model Quantifies Robust Increases in Daily Extreme Rainfall Across the Western Gulf Coast (Lu, Lee & Doss-Gollin, 2025) — arXiv"
    url: "https://arxiv.org/abs/2502.02000"
  - title: "Assessment of the standard precipitation frequency estimates in the United States (Kim et al., J. Hydrol. Reg. Stud. 44, 101276, 2022) — DOAJ record"
    url: "https://doaj.org/article/97c7ac167f50478985704df4f83bae70"
  - title: "Extreme floods occurring more frequently than federal estimates — Insurance Business"
    url: "https://www.insurancebusinessmag.com/us/news/catastrophe/extreme-floods-occurring-more-frequently-than-federal-estimates--report-450706.aspx"
  - title: "Examining Atlas 14's Impact on Future Development in the Houston Area — Halff"
    url: "https://halff.com/?p=2883"
---

If you are sizing a culvert in Washington State this week, the rainfall you design it against comes from three documents. For storm durations between one and twenty-four hours, it is NOAA Atlas 2, Volume 9, published in 1973. For anything longer than a day, Technical Paper 49, published in 1964. For bursts shorter than an hour, a 1986 paper by Arkell and Richards. Oregon is identical, with Atlas 2's Volume 10 in place of Volume 9. These are not legacy citations kept around for comparison. They are what the National Weather Service's Hydrometeorological Design Studies Center lists, today, under *current* precipitation frequency documents.

Everywhere else has been moved onto NOAA Atlas 14, which is better and still not new. Volume 1 — Arizona, Nevada, New Mexico, Utah — is from 2004. Volume 2, which governs Maryland, Virginia, Pennsylvania and the Carolinas, is also from 2004. Texas got Volume 11 in 2018. Idaho, Montana and Wyoming got Volume 12 in 2024. Every one of those volumes assumes that extreme rainfall is statistically stationary: that the thing you are estimating does not move while you estimate it.

NOAA is now replacing all of it with Atlas 15, which drops that assumption. This is the first atlas update to get direct federal funding, through the Bipartisan Infrastructure Law, and it is the most consequential piece of statistics most civil engineers will never read. I went looking for how much the numbers move once stationarity goes, and found something I did not expect: in NOAA's own worked example, most of the movement wasn't the climate.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">+33%</div><div class="sl mono">from changing the estimator</div><div class="sn">L-moments to maximum likelihood</div></div><div class="stat"><div class="sv">+4%</div><div class="sl mono">from the time-varying term</div><div class="sn">same site, same storm</div></div><div class="stat"><div class="sv">1964</div><div class="sl mono">oldest source still listed as current</div><div class="sn">Technical Paper 49, durations over a day</div></div><div class="stat"><div class="sv">1.5–5 °C</div><div class="sl mono">warming levels the engineer chooses between</div><div class="sn">Atlas 15 Volume 2</div></div></figure>


## What Atlas 15 actually does

Volume 1 fits a nonstationary Generalized Extreme Value distribution by regional maximum likelihood. The location and scale parameters get two covariates: mean annual maximum rainfall, which handles space, and a Global Temperature Index, which handles time. The shape parameter is held fixed, because letting it float produced unreasonable values.

That Global Temperature Index is the interesting part. It is a thirty-year moving average of global mean temperature anomaly relative to 1851–1900. In 2023 it sits at 1.1 °C. So the hundred-year storm is no longer a number attached to a place; it is a function evaluated at a global average temperature. The pilot report notes that global CO₂ works nearly as well as a covariate and gives almost identical present-day estimates — GTI was chosen for consistency with Volume 2 rather than because it fit better.

Volume 2 is where it gets uncomfortable in a way I find genuinely novel. It takes Volume 1's estimates and multiplies them by adjustment factors derived from downscaled climate models, indexed not by year and not by emissions scenario but by warming level. The CONUS peer-review questionnaire asks reviewers, in a multiple-choice question, which Global Temperature Index levels they would use: 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, or 5 °C. A separate question asks whether an emissions-scenario framing — SSP2-4.5, SSP3-7.0, SSP5-8.5 — would also be useful.

Read that as an engineer and it is a dial. The deliverable for a storm sewer is one depth in inches, and the standard is about to hand you eight of them and ask which future you are building for. That is not a flaw in the method; it is an honest representation of what is actually known. But it relocates a climate-policy judgment into a drainage calculation performed by someone with no mandate to make it, and the questionnaire's framing — *which would you use?* — suggests NOAA knows it and has decided to let the profession sort it out.

## The part that surprised me

In 2015 the Federal Highway Administration asked the Hydrometeorological Design Studies Center to run a pilot on exactly this question. Sanja Perica and colleagues presented the results at an ASCE workshop in Reston in May 2017, and one slide decomposes a single site's 24-hour, 100-year estimate three ways.

Fitting by L-moments, the way Atlas 14 does it, gives 15.0 inches. Refitting the same data by stationary maximum likelihood gives 20.0 inches — a 33 per cent increase with no climate in it at all. Adding the time-varying term gives 20.7 inches. The two compound to the 38 per cent headline, and about four points of it are the nonstationarity.

I want to be careful about how much weight that carries. The slide names no station. The deck's own summary line is "preliminary findings are inconclusive." A single site is a single site, and the method Atlas 15 ended up with — regional MLE with a GTI covariate and AICc model selection — is not the MLE(t) experiment of 2017. But the mechanism is not in dispute: L-moments and maximum likelihood are different estimators with different tail behaviour, and swapping them changes your answer whether or not the climate has moved.

Which makes the Montana pilot's own comparison harder to read than it looks. The pilot reports that Atlas 15 and Atlas 14 differ by generally within about 20 per cent for the 1 per cent annual exceedance probability at 60 minutes and 24 hours, with no apparent geographic pattern, and attributes the differences largely to the nonstationary framework. But the baseline it is differencing against is Atlas 14 Volume 12, an L-moments product, and the pilot's input is Volume 12's own quality-controlled annual maximum series. The estimator changed too. I could not find, in the pilot's text, the decomposition that the 2017 deck did on one site — the figures may carry it, but the prose does not.


<aside class="fig note"><span class="mono">Note</span><p>The pilot technical report says plainly that it has not completed peer review and that final values &quot;may significantly differ.&quot; It covers Montana only, and its applicability beyond the pilot domain is untested. Everything above about magnitudes is provisional by NOAA&#x27;s own label.</p></aside>


## The band nobody designs to

There is a second thing both atlases already tell you and nobody uses. Atlas 14 publishes 90 per cent confidence intervals alongside every point estimate. Pull the Texas numbers for a point in downtown Houston from the Precipitation Frequency Data Server — Volume 11, version 2 — and the 24-hour depths come out like this.


<figure class="fig bars"><figcaption class="mono">Houston, 24-hour rainfall depth, inches</figcaption><div class="rows"><div class="brow"><div class="blabel">25-year estimate</div><div class="btrack"><div class="bfill" style="width:45.49%" title="25-year estimate · 11.6"></div></div><div class="bval mono">11.6</div></div><div class="brow"><div class="blabel">100-year estimate</div><div class="btrack"><div class="bfill" style="width:66.67%" title="100-year estimate · 17.0"></div></div><div class="bval mono">17.0</div></div><div class="brow"><div class="blabel">200-year estimate</div><div class="btrack"><div class="bfill" style="width:80.00%" title="200-year estimate · 20.4"></div></div><div class="bval mono">20.4</div></div><div class="brow"><div class="blabel">100-year, upper bound of its 90% interval</div><div class="btrack"><div class="bfill" style="width:93.73%" title="100-year, upper bound of its 90% interval · 23.9"></div></div><div class="bval mono">23.9</div></div><div class="brow"><div class="blabel">500-year estimate</div><div class="btrack"><div class="bfill" style="width:100.00%" title="500-year estimate · 25.5"></div></div><div class="bval mono">25.5</div></div></div></figure>


The upper bound on the hundred-year storm sits above the two-hundred-year point estimate and most of the way to the five-hundred-year. I pulled the upper bound directly; the server's lower-bound file would not return for me, so I am not quoting it. The shape of the problem is visible without it: the quantity a county writes into an ordinance is the midpoint of a band wide enough to contain several other design storms.

Houston is also the clearest illustration of what a revision does in practice. When Volume 11 landed in 2018, engineering write-ups of the Harris County impact put the previous 100-year depths at an average near 13 inches and the new ones three to five inches higher, close to the old 500-year values. The county rewrote its development regulations the following year. Nothing about the climate changed in 2018; the atlas did.

Atlas 15's answer to this is better communication. The first three questions on the peer-review form ask reviewers to agree or disagree that the preliminary estimates communicate uncertainty better than Atlas 14 did, enable better-informed decisions, and give improved guidance on necessary actions. Question nine asks whether they would want intervals other than the default 90 per cent — 80, or 95. It is a reasonable thing to ask. It is also asking a profession whose output is a single number which flavour of range it prefers.

## What the independent work says

The outside literature does find real trends, and it does not agree with itself about where. Lu, Lee and Doss-Gollin's 2025 Bayesian spatiotemporal model, fit to 181 long-record gauges on the western Gulf Coast, estimates that 10-year and 100-year daily return levels rose roughly 10 to 35 per cent between 1940 and 2022, largest in coastal southeast Texas and southeastern Louisiana. But their fit has Atlas 14 *overestimating* Houston while underestimating New Orleans, Galveston and Mobile — and their own cross-validation reports the pooled stationary model scoring slightly better on two proper scoring rules, LogS and CRPS. A nonstationary model that loses to a stationary one on out-of-sample skill, while still showing a robust trend in its parameters, is a more interesting result than the abstract lets on.

Pointing the other way, Kim and colleagues' 2022 assessment in *Journal of Hydrology: Regional Studies* benchmarks the atlases against estimates built from airport observing stations and finds that they generally underestimate, with the gap widening at longer return periods and shorter durations, and correlating with the atlas's age. That is the result that gets cited when someone says the federal numbers are too low. The work came out of the First Street Foundation — its lead author is First Street's senior hydrologist — a non-profit that builds and licenses its own property-level flood-risk dataset. That does not make the finding wrong; the age correlation is exactly what you would predict. But it is worth knowing who ran the comparison against the federal standard, and I could not verify every author's affiliation independently.

## Why I keep thinking about it

Because the timeline is itself the argument. NOAA published Atlas 14 Volume 12 — a stationary product — in 2024, the same year it released the nonstationary Montana pilot that uses Volume 12's data as input. Volume 13, covering the mid-Atlantic and Carolinas and replacing a 2004 volume, finished peer review and was expected this past summer, also stationary. Meanwhile the Atlas 15 schedule has slid from preliminary CONUS estimates in the first quarter of 2026, to "by September 2026," to an informational page that today still reads "no earlier than September 2026" for the preliminary release and no earlier than September 2027 for publication — with a roughly month-long contract pause somewhere in 2025 that nobody has explained in print. The CONUS peer-review questionnaire is posted. I could not confirm, from anything I could reach, that the estimates it refers to are public yet.

So the number is going to change, probably a lot, and the honest account of why will be three things at once: a longer record, a different estimator, and a moving climate — in roughly that order of effect size, if the one decomposition anyone has published generalises. The ordinance that eventually cites the new depth will say none of that. It will say a number of inches.
