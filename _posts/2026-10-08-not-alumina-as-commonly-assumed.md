---
layout: post
title: "Not Alumina, As Commonly Assumed"
dek: "Two years of headlines about megaconstellations eating the ozone layer rest on a compound that lab ablation work now suggests is mostly not being produced. The only global model that has simulated it left the chemistry out and got the opposite sign."
description: "Two years of headlines about megaconstellations eating the ozone layer rest on a compound that lab ablation work now suggests is mostly not being produced. The only global model that has simulated it left the chemistry out and got the opposite sign."
date: 2026-10-08
tags: ["ozone", "satellite reentry", "atmospheric chemistry", "space debris"]
accent: "#17703F"
accent_dark: "#63DB8A"
sources:
  - title: "Potential Ozone Depletion From Satellite Demise During Atmospheric Reentry in the Era of Mega-Constellations (Ferreira et al., 2024) — Geophysical Research Letters"
    url: "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024GL109280"
  - title: "The same paper, full text as filed in FAA docket FAA-2024-1395 — regulations.gov"
    url: "https://downloads.regulations.gov/FAA-2024-1395-0037/attachment_1.pdf"
  - title: "Metals from spacecraft reentry in stratospheric aerosol particles (Murphy et al., 2023) — PNAS"
    url: "https://www.pnas.org/doi/10.1073/pnas.2313374120"
  - title: "The same paper, open-access copy — White Rose Research Online"
    url: "https://eprints.whiterose.ac.uk/id/eprint/203372/7/murphy-et-al-2023-metals-from-spacecraft-reentry-in-stratospheric-aerosol-particles.pdf"
  - title: "Investigating the Potential Atmospheric Accumulation and Radiative Impact of the Coming Increase in Satellite Reentry Frequency (Maloney et al., 2025) — Journal of Geophysical Research: Atmospheres"
    url: "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JD042442"
  - title: "The same paper, open copy — NOAA Institutional Repository"
    url: "https://repository.library.noaa.gov/view/noaa/71517/noaa_71517_DS1.pdf"
  - title: "Space waste: An update of the anthropogenic matter injection into Earth (Schulz et al., 2025 preprint) — arXiv"
    url: "https://arxiv.org/abs/2510.21328"
  - title: "The Space Materials Ablation Simulator (SMASI): first results on the thermal ablation of aluminium alloys (Gomez Martin et al.) — 2nd Workshop on Atmospheric Impacts of Spacecraft Launch and Re-entry, ESA/ESTEC"
    url: "https://indico.esa.int/event/579/contributions/11325/"
  - title: "Programme, 2nd Workshop on Atmospheric Impacts of Spacecraft Launch and Re-entry — Indico, ESA/ESTEC"
    url: "https://indico.esa.int/event/579/timetable/"
  - title: "Impact of Spaceflight on Earth's Atmosphere, NASA/TM-20240013276 — NASA Technical Reports Server"
    url: "https://ntrs.nasa.gov/api/citations/20240013276/downloads/NASA-TM-20240013276-V6.pdf"
---

A 250-kilogram satellite ends its working life by falling into air thick enough to take it apart, and what it leaves behind is roughly thirty kilograms of extremely fine powder hanging between 60 and 70 kilometres up. That figure — "around 30 kg of aluminum oxide nanoparticles" — is from Ferreira and colleagues' 2024 paper in *Geophysical Research Letters*, and it is the number that launched two years of headlines about megaconstellations quietly undoing the Montreal Protocol.

I went after this one because the claim has a shape I find hard to resist. A specific molecule. A known catalytic mechanism. A recovering ozone layer with a well-measured baseline. A source growing faster than almost anything else in the atmosphere. Every link in the chain is the kind of thing you can go and check. What I did not expect, reading down the chain, was that the molecule is the link in doubt.

## What the mechanism actually requires

Aluminium oxide does not destroy ozone the way a CFC does. It is not consumed and it does not carry chlorine. What it provides is a *surface* — a place where the stable chlorine reservoir species that the stratosphere keeps locked away can be converted into forms that sunlight breaks apart in minutes. This is the same class of chemistry that makes polar stratospheric clouds the hinge of the Antarctic ozone hole: the clouds themselves are inert, and what matters is that they offer a few square micrometres of the right kind of surface at the right temperature.

So the ozone claim is not really a claim about aluminium. It is a claim about a particular solid phase, with a particular surface, present in a particular size distribution, in a particular place. Ferreira's paper does not simulate any of that. What it simulates is the ablation: a reactive molecular-dynamics run at 2,200 K with oxygen atoms arriving at 2 km/s, meant to represent a generic reentry at 86 km, held at a constant angle of attack for ninety seconds. From that it gets a conversion yield — about 32 per cent of the aluminium in a satellite oxidises — and extrapolates to an inventory. The ozone-destruction step is not modelled at all. It is carried by a citation to the existing literature giving a reaction probability of roughly two per cent on aluminium oxide surfaces, and by the historical body of work on solid rocket motor exhaust.

That is a perfectly respectable thing for a four-page letter to do. It is not what the coverage describes. The paper's own title says "potential," and the potential is doing a great deal of work.

## The measurement that exists

There is real observational evidence here, and it is better than I expected. In February and March 2023, NASA's WB-57 flew out of Fairbanks with a single-particle mass spectrometer aboard and sampled the high-latitude stratosphere up to about 19 kilometres. Murphy and colleagues reported the results in *PNAS* later that year: more than half a million single-particle spectra, over twenty elements traceable to spacecraft alloys, in ratios matching the alloys rather than meteoritic material. Roughly ten per cent — 10 ± 7 — of the sulfuric acid droplets larger than about 120 nanometres carried reentry metals. They found niobium in about one particle in a thousand, with a niobium-to-hafnium ratio matching C-103, a specific alloy used in rocket nozzles. That is a remarkably clean fingerprint.

Note what it establishes and what it does not. It establishes that the material arrives, survives, and distributes itself through the stratospheric aerosol layer. On the question of what phase it is in, the paper is explicit and unhelpful in the most honest way: a few particles resemble the alumina that solid rocket motors emit, but whether the metals "remain oxides after weeks or months in concentrated sulfuric acid is uncertain." The instrument sees metal ions, not molecules. And on ozone, the paper declines the invitation entirely, noting only that at these concentrations there would need to be a catalytic cycle for any significant effect on chlorine partitioning.

An aluminium atom dissolved inside a sulfuric acid droplet and an α-alumina nanoparticle with a bare crystalline face are, for the purpose of heterogeneous chlorine chemistry, almost unrelated objects. The measurement cannot tell them apart. That is not a criticism of the measurement; it is the measurement's own stated limit.

## The only global model that has run it

Last year a NOAA group did the thing everyone was asking for: a three-dimensional simulation with a real middle-atmosphere model. Maloney and colleagues put 10 gigagrams a year of aluminium oxide into WACCM6 coupled to the CARMA aerosol model, emitted between 60 and 70 kilometres, across five scenarios for where reentries happen and how large the particles are. They got 20 to 40 gigagrams accumulating poleward of about 30° in each hemisphere, temperature anomalies up to about 1.5 K, and roughly a ten per cent weakening of the Southern Hemisphere polar vortex.

And the ozone result went the other way. In their scenarios the Southern Hemisphere springtime column ozone *increases* — by as much as about 7 Dobson units in one case and 9 in another — while the Northern Hemisphere loses up to around 5.5. The mechanism is dynamical: the particles absorb and emit, the temperature structure shifts, the vortex loosens, polar stratospheric clouds decrease in the south.

The reason that is not reassuring is the reason it happened. In this model the alumina is chemically inert. It talks only to the radiative transfer code, because CARMA cannot yet hand its particle surface area to WACCM6's heterogeneous chemistry module. The one effect everybody is worried about is the one effect the simulation does not contain. The authors say so plainly, and say the capability is being built. NASA's 2024 technical memorandum on spaceflight and the atmosphere, written while this work was still under review, puts the general situation more bluntly still: simulations of reentry emissions and far-field plume evolution "have not been done at all," and the emissions data to drive them "do not yet exist."

So the published state of the art is a model whose ozone answer has the opposite sign to the headline, for reasons unrelated to the headline's mechanism.

## The denominator

The inventory numbers are worth laying side by side, because the percentages built on them are quoted far more often than the tonnages.


<figure class="fig bars"><figcaption class="mono">Aluminium reaching the atmosphere each year, tonnes · log scale</figcaption><div class="rows"><div class="brow"><div class="blabel">Micrometeoroid influx, arriving (Murphy 2023)</div><div class="btrack"><div class="bfill" style="width:71.42%" title="Micrometeoroid influx, arriving (Murphy 2023) · 130 t"></div></div><div class="bval mono">130 t</div></div><div class="brow"><div class="blabel">Micrometeoroid influx, actually ablated</div><div class="btrack"><div class="bfill" style="width:43.95%" title="Micrometeoroid influx, actually ablated · 20 t"></div></div><div class="bval mono">20 t</div></div><div class="brow"><div class="blabel">Satellites, 2022 (Ferreira 2024)</div><div class="btrack"><div class="bfill" style="width:54.73%" title="Satellites, 2022 (Ferreira 2024) · 41.7 t"></div></div><div class="bval mono">41.7 t</div></div><div class="brow"><div class="blabel">Spacecraft, present day (Murphy 2023)</div><div class="btrack"><div class="bfill" style="width:78.45%" title="Spacecraft, present day (Murphy 2023) · 210 t"></div></div><div class="bval mono">210 t</div></div><div class="brow"><div class="blabel">All space waste, 2024 (Schulz 2025)</div><div class="btrack"><div class="bfill" style="width:87.80%" title="All space waste, 2024 (Schulz 2025) · 397 t"></div></div><div class="bval mono">397 t</div></div><div class="brow"><div class="blabel">Worst-case mega-constellation case (Ferreira 2024)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Worst-case mega-constellation case (Ferreira 2024) · 912 t"></div></div><div class="bval mono">912 t</div></div><div class="brow"><div class="blabel">Of any of it, confirmed to be Al₂O₃</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Of any of it, confirmed to be Al₂O₃ · not determined"></div></div><div class="bval mono muted">not determined</div></div></div></figure>


Ferreira's much-repeated line is that 2022's reentries pushed stratospheric aluminium 29.5 per cent above its natural level, rising to more than 640 per cent in the worst case. Murphy's paper gives about 210 tonnes a year of aluminium ablating from spacecraft against about 20 tonnes a year from meteoroids — which is not a thirty per cent increase but something closer to a thousand. I did the division myself: back out Ferreira's baseline from their own two figures and you get about 141 tonnes a year of natural aluminium, almost exactly Murphy's figure for how much micrometeoroid aluminium *arrives* rather than how much vaporises. The gap between a famous "+29.5%" and an equally sourceable "+1,000%" is mostly a choice about which denominator counts, and neither paper is wrong on its own terms.

That is an arithmetic observation, not a finding, and the honest version of it is that this field does not yet have agreed definitions for its simplest quantity. Schulz and colleagues' October preprint, which is the most careful inventory I found, puts 2024's injected mass at 887 ± 123 tonnes with about 397 tonnes of that aluminium, against a natural injection of roughly 12,300 tonnes of all material — and identifies differential ablation, the fact that different metals boil off at different temperatures and altitudes, as probably the largest source of error in the whole exercise, unmodelled.

## And then the molecule

Which brings me to the part I actually sat up at. At an ESA workshop last September, a group running a new table-top ablation rig called SMASI reported first results on aluminium alloys, and the abstract states that the main atmospheric product is aluminium hydroxide — "not alumina, as commonly assumed." Schulz's preprint, from an overlapping set of people, says the same thing from the modelling side: equilibrium chemistry favours Al₂O₃, but meteoroid ablation models give AlOH and Al(OH)₂ dominating below 80 kilometres, with preliminary lab work supporting the hydroxides. They note that this "could imply different pathways" for ozone, and that those pathways have not been determined.


<aside class="fig note"><span class="mono">Note</span><p>The hydroxide result is a conference abstract and lab work in progress, not a peer-reviewed measurement, and the two lines of evidence for it are not independent — John Plane is a co-author on both the SMASI work and the Schulz inventory. I am treating it as a serious reason for doubt, not as a settled correction.</p></aside>


If that holds up, then the inventory papers, the global model, the FAA docket submission and effectively all of the press coverage are about a compound that is not the one principally being made. Hydroxides are not harmless; they are simply not the thing whose surface chemistry the two per cent reaction probability was measured on. The mechanism would have to be worked out again from the start.

What I find genuinely interesting here is not that anyone has been careless. Ferreira's paper says "potential." Murphy's says "uncertain" and "unknown." Maloney's says the chemistry is absent and being built. Every individual paper is appropriately hedged. The confident claim exists only in the space between them, assembled by readers — me included, until this week — who took the molecule from one paper, the magnitude from another, the mechanism from the solid-rocket-motor literature of the 1990s, and the ozone sign from nowhere in particular.

The schedule is the uncomfortable part. ESA has a reentry measurement campaign planned around the CLUSTER-II satellites, a monitoring initiative is sketched for 2028 through 2038, lab experiments on how these metals behave in sulfuric acid are still running, and the chemistry module for the global model does not exist yet. Meanwhile the NASA memorandum projects reentry vaporisation rising from roughly a thousand tonnes a year now to over thirty thousand by around 2040. The fleet that would produce that is being launched now, and the measurements that could tell us whether it matters are mostly scheduled for after it is up there. I do not know which way this goes. I have stopped being confident that anyone does.
