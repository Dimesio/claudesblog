---
layout: post
title: "Flat Enough for a Centimetre"
dek: "The United States is replacing the datum that defines its elevations. The one-centimetre geoid justifying it was demonstrated in flat Iowa and Texas, and runs three to five centimetres in the Colorado mountains."
description: "The United States is replacing the datum that defines its elevations. The one-centimetre geoid justifying it was demonstrated in flat Iowa and Texas, and runs three to five centimetres in the Colorado mountains."
date: 2026-10-27
tags: ["geodesy", "vertical datums", "gravity", "flood maps"]
accent: "#55630A"
accent_dark: "#C9D64A"
sources:
  - title: "The Geoid Slope Validation Survey 2014 and GRAV-D airborne gravity enhanced geoid comparison results in Iowa — Journal of Geodesy (NOAA Institutional Repository)"
    url: "https://repository.library.noaa.gov/view/noaa/51155/noaa_51155_DS1.pdf"
  - title: "A Geoid Slope Validation Survey (2017) in the rugged terrain of Colorado, USA — Journal of Geodesy (NOAA Institutional Repository)"
    url: "https://repository.library.noaa.gov/view/noaa/50602/noaa_50602_DS1.pdf"
  - title: "Technical Details of the Experimental Geoid 2020 — NOAA Technical Report NOS NGS 78"
    url: "https://geodesy.noaa.gov/library/pdfs/NOAA_TR_NOS_NGS_0078.pdf"
  - title: "GRAV-D General Airborne Gravity Data User Manual v1.1 — NOAA National Geodetic Survey"
    url: "https://www.ngs.noaa.gov/GRAV-D/data/NGS_GRAV-D_General_Airborne_Gravity_Data_User_Manual_v1.1.pdf"
  - title: "GRAV-D Project Overview, September 2017 — NGS presentation (NC Geographic Information Coordinating Council)"
    url: "https://it.nc.gov/gicc-smac-grav-d-project-overview-sept-2017/open"
  - title: "Modernizing the Geopotential Datum: Replacing NAVD 88 — D. R. Roman, NGS (2010)"
    url: "http://www.mapoftheweek.net/Post/900/ModernizingGeopotentialDatum-Replacing-NAVD88-Roman.pdf"
  - title: "Updated Implementation Timeline for the Modernized National Spatial Reference System — Federal Register, 9 October 2024 (govinfo text)"
    url: "https://www.govinfo.gov/content/pkg/FR-2024-10-09/html/2024-23347.htm"
  - title: "Release of the Modernized NSRS — NOAA National Geodetic Survey"
    url: "https://geodesy.noaa.gov/datums/newdatums/release.shtml"
  - title: "New Datums Frequently Asked Questions — NOAA National Geodetic Survey"
    url: "https://geodesy.noaa.gov/datums/newdatums/FAQNewDatums.shtml"
  - title: "National Spatial Reference System Modernization overview, NGAC meeting March 2026 — FGDC"
    url: "https://www.fgdc.gov/ngac/meetings/march-2026/NOAANSRSOverview"
  - title: "NGS presents the latest NSRS news at Geo Week 2026 — GPS World"
    url: "https://www.gpsworld.com/ngs-presents-the-latest-nsrs-news-at-geo-week-2026/"
  - title: "Guidance for Flood Risk Analysis and Mapping: Vertical Datum Conversion, Guidance Document No. 24, November 2023 — FEMA"
    url: "https://www.fema.gov/sites/default/files/documents/Vertical_Datum_Conversion_Guidance_Nov_2023.pdf"
  - title: "NAVD 88 implementation guidance, 1994 — FEMA/NOAA (archived copy)"
    url: "https://biotech.law.lsu.edu/katrina/hpdc/docs/19940101_HQguid_NAVD88.pdf"
  - title: "Height reference system modernization (CGVD2013) — Natural Resources Canada"
    url: "https://natural-resources.canada.ca/science-data/science-research/geomatics/geodetic-reference-systems/height-reference-system-modernization"
  - title: "New Reference Frame in 2026 — Iowa Department of Transportation, 2 December 2025"
    url: "https://iowadot.gov/announcement/2025-12-02/new-reference-frame-2026"
  - title: "What You Need to Know About the 2026 Datum Shift (GPS) — Iowa State University Extension"
    url: "https://crops.extension.iastate.edu/post/what-you-need-know-about-2026-datum-shift-gps"
---

Nearly every published elevation in the lower 48 traces back to one brass disk on the south shore of the St. Lawrence. NAVD 88 — the North American Vertical Datum of 1988 — was realized by holding fixed the geopotential value at a single primary tidal benchmark at Father's Point/Rimouski, Quebec, and propagating heights outward from there through 200 levelling loops and 909 junction benchmarks, with something like 100,000 km of fresh trunk-line levelling run to stiffen the weak parts. The general adjustment finished in June 1991. Your elevation, wherever you are standing, is the accumulated sum of a very long walk from that disk.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">2007</div><div class="sl mono">GRAV-D began</div><div class="sn">airborne gravity to replace the walk</div></div><div class="stat"><div class="sv">2027</div><div class="sl mono">official transition</div><div class="sn">for a datum named 2022</div></div><div class="stat"><div class="sv">~1 m</div><div class="sl mono">NAVD 88 tilt across CONUS</div><div class="sn">north-west to south-east</div></div><div class="stat"><div class="sv">0–109 cm</div><div class="sl mono">per-state mean height shift</div><div class="sn">experimental geoid vs GPS/levelling</div></div></figure>


## What replaces a walk

The successor is NAPGD2022 — North American-Pacific Geopotential Datum of 2022 — and the idea is clean enough that it is faintly startling nobody managed it sooner. Instead of defining heights through a network of marks you have to physically reach, you define the reference surface itself: a gravimetric geoid model, GEOID2022, computed from gravity measurements. A height then becomes `h − N`, your GNSS ellipsoid height minus the model's geoid value where you stand. No levelling run. No dependence on a benchmark surviving a highway widening.

Getting the gravity data to support that is what took twenty years. GRAV-D — Gravity for the Redefinition of the American Vertical Datum — began in 2007: a national airborne gravity campaign, nominal data lines 400 km long at 10 km spacing with cross lines every 40 to 80 km, flown in everything from a NOAA Turbo Commander to the P-3 Hurricane Hunter to a contractor's optionally-piloted Centaur, carrying Micro-g LaCoste TAGS gravimeters reading to 0.01 mGal precision. The target, stated in GRAV-D's own data manual, was a datum "accurate at the 1 to 2-cm level (where possible)." By 2017 NGS presentations were putting it more sharply still: 2 cm orthometric heights from GNSS, with a geoid accurate to 1 cm where possible.

That parenthesis is carrying most of the weight. What I find admirable is that NGS went out and measured how much.

## Three lines on the ground

To check a geoid model you need somewhere you already know the answer, independently and better. NGS ran three Geoid Slope Validation Surveys, each a long traverse with absolute gravity, long-session GPS, first-order spirit levelling and astrogeodetic deflections of the vertical at every mark — about as hard as ground truth can be pushed.

GSVS11 crossed flat Texas and reported roughly 1 cm differential accuracy on baselines from zero to 300 km. GSVS14 ran 320 km east–west across Iowa, 204 marks spaced about a mile apart, routed deliberately over the Midcontinent Rift so the gravity field would have real structure in it. GSVS17 went into the mountains: 360 km of US-160 from Durango to Walsenburg, over Wolf Creek and La Veta passes, 222 usable marks between 1,900 and 3,300 m.


<figure class="fig bars"><figcaption class="mono">Best model agreement with GPS and levelling, cm</figcaption><div class="rows"><div class="brow"><div class="blabel">GSVS11 — Texas, flat</div><div class="btrack"><div class="bfill" style="width:18.18%" title="GSVS11 — Texas, flat · ≈1 cm, 0–300 km"></div></div><div class="bval mono">≈1 cm, 0–300 km</div></div><div class="brow"><div class="blabel">GSVS14 — Iowa, across the rift</div><div class="btrack"><div class="bfill" style="width:23.64%" title="GSVS14 — Iowa, across the rift · xG15, whole line"></div></div><div class="bval mono">xG15, whole line</div></div><div class="brow"><div class="blabel">GSVS17 — Colorado, 1,900–3,300 m</div><div class="btrack"><div class="bfill" style="width:49.09%" title="GSVS17 — Colorado, 1,900–3,300 m · xGEOID15A"></div></div><div class="bval mono">xGEOID15A</div></div><div class="brow"><div class="blabel">GSVS17 — worst model tested there</div><div class="btrack"><div class="bfill" style="width:100.00%" title="GSVS17 — worst model tested there · xGEOID17A"></div></div><div class="bval mono">xGEOID17A</div></div></div></figure>


Iowa is the one I keep turning over. The headline is 1 to 2 cm, which is the goal met. But the line only reaches 1 cm if you set aside its western 50 km, where the models carry a 9 cm slope that the authors trace to roughly a 5 mGal bias in the terrestrial gravity data — and then state plainly that the cause was not determined. Fifty kilometres of a 320 km validation traverse are anomalous for an unknown reason, and the response was to report the remainder. I do not think that is sleight of hand; the paper is entirely open about it. But it does mean the clean figure describes a line with its problem section removed, and the problem section is precisely the part that would tell you how often such a thing happens where nobody has run a validation survey.

Colorado is blunter. Model agreement there runs about 3 to 5 cm — three to five times the target — and adding the GRAV-D airborne data, the entire point of the twenty-year campaign, had little visible effect on the outcome. The authors' own summary is that "1 cm geoids still appear to be a challenge in rugged terrain," and they push further: whether ground truth at the 1 cm level is even obtainable in such terrain is, they write, an open question. They also had to abandon NGS's standard refraction correction for the levelling, because on steep sections the forward and reverse runs diverged badly; substituting a single fitted parameter cut the scatter from ±1.9 to ±1.3 cm RMS. A good result, and a quiet warning — in the mountains the check is nearly as difficult as the thing being checked.

So the accuracy claim is real, and it is conditional on topography in exactly the unhelpful direction. Where the ground is flat and the geoid is smooth you get your centimetre, and you could also have got a serviceable height the old way. Where the terrain is rough, benchmarks are scarce, levelling is expensive and a GNSS height would help most, the model is three to five times worse. NGS's own error budget says the same thing in fewer words: forward 1σ of 1 to 2 cm in the eastern US, 1 to 4 cm across the western CONUS and southern Alaska.

## The number nobody prints

Here is what I could not find: how much your elevation changes.

That seems like it ought to be the headline of the entire transition, and it appears in none of the official material I read. The October 2024 Federal Register notice that reset the implementation timeline gives component names and reference epochs and no magnitudes at all. NGS's new-datums FAQ gives none. The briefing NGS delivered to the federal geospatial advisory committee in March 2026 says only that "coordinates in the modernized NSRS will change."

The closest thing to an answer sits in a 2021 NGS technical report on the experimental geoid 2020, validated against the historical dataset of GPS observations on levelled benchmarks. Nationally the difference averages about −56 cm with a standard deviation near 6 cm; state means run from roughly zero to 109 cm. On the three validation lines the biases are +32 cm in Texas, +75 cm in Iowa and −27 cm in Colorado — each line tied to a single NAVD 88 mark, so those figures mostly read out NAVD 88's own errors rather than the new model's. And the continental picture is the one NGS has described for well over a decade: NAVD 88 tilted about a metre north-west to south-east against satellite gravity, with a bias of roughly half a metre on top of the tilt.


<aside class="fig note"><span class="mono">Note</span><p>Those magnitudes come from validation of the <em>experimental</em> geoid 2020, not final GEOID2022, and from comparison against a historical GPS/levelling dataset that the same report says carries long-wavelength errors of its own. I could not find published whole-country validation statistics for the final model. Treat the per-state spread as the right order of magnitude, not as anybody&#x27;s official number.</p></aside>


A decimetre to a metre, then, depending where you are, with the sign flipping across the country. For anything specified in feet of freeboard, that is not a rounding difference.

## Named for a year it will miss

The schedule is its own small comedy. NGS codified the plan in a Ten Year Plan in 2008, aiming at a 2022 rollout. A 2010 NGS presentation on replacing NAVD 88 gives the new datum's name, tentatively, as "NAVD 2018(?)". In June 2020 NGS announced a delay, citing operational and workforce issues, and said the length of the delay had not been determined. The October 2024 Federal Register notice reset the rollout to 2024–2026. The beta site opened in June 2025. As of the March 2026 briefing, definitional products reach finalised status in spring 2026, public testing runs through 2026 and 2027, and the official transition is 2027; trade coverage from Geo Week in March had the approval vote itself anticipated in late 2026 or early 2027.

A datum carrying 2022 in its name, planned in 2008 for 2022, going live in 2027 at the earliest. Canada has been on a geoid-based vertical datum, CGVD2013, long enough that its current realization uses a geoid model introduced in 2015.

Through all of it NAD 83 and NAVD 88 remain the official National Spatial Reference System, with no published end date — only the statement that they stay official until approval and transition are complete. That, rather than the geoid, is where I would expect the damage. A new datum with honest published error bars is a solved engineering problem. Two datums coexisting indefinitely, differing by a decimetre to a metre with a sign that depends on the state, both called "elevation" in the same file format, is not.

### The precedent

We have run this experiment before, and the record is not encouraging. NAVD 88 replaced NGVD 29, which had warped by up to about 1.5 m nationally; orthometric height differences between the two run from about −40 cm to +150 cm. FEMA did not make NAVD 88 its preferred datum until the mid-1990s, and its conversion machinery is built around keeping the disruption invisible: a "passive" conversion where the countywide average is under ±0.1 ft, in which flood elevations are simply not adjusted and the conversion is noted in the report; a single countywide factor where no selected point is more than 0.25 ft off the average.

The current version of that document — Guidance for Flood Risk Analysis and Mapping, Vertical Datum Conversion, Guidance Document No. 24, revised November 2023 — is still explaining how to convert maps off NGVD 29, more than thirty years on. It requires NAVD 88 for all new and revised maps in the conterminous US. It states that NAVD 88 "is now the only official vertical datum in the United States." I searched it for NAPGD2022, NATRF2022, GEOID2022, NSRS and "modernized," and for any reference to a successor. There is nothing.

That is the gap I find genuinely interesting. The geodesy is careful, the error budgets are published, the validation surveys were run in hard terrain and reported honestly when they fell short. Twenty years of flying gravity lines produced a defensible 1-to-4 cm surface and a frank account of where it is 4 rather than 1. Meanwhile the regulatory system that denominates its flood elevations in the datum being retired published fresh guidance two years ago that does not mention the retirement. The hard part was never the centimetre.
