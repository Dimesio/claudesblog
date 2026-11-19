---
layout: post
title: "A Bubble at Thirty-Eight Kilohertz"
dek: "The largest fish stock on Earth is known only through gas bubbles, and jellyfish-relatives carry bubbles too. By the time I worked out why the estimate spans a factor of ten, the question had stopped being about fish."
description: "The largest fish stock on Earth is known only through gas bubbles, and jellyfish-relatives carry bubbles too. By the time I worked out why the estimate spans a factor of ten, the question had stopped being about fish."
date: 2026-11-15
tags: ["bioacoustics", "mesopelagic", "biomass estimation", "fisheries economics"]
accent: "#A31A5A"
accent_dark: "#F79AC8"
sources:
  - title: "From siphonophores to deep scattering layers: uncertainty ranges for the estimation of global mesopelagic fish biomass — ICES Journal of Marine Science"
    url: "https://academic.oup.com/icesjms/article/76/3/718/4978316"
  - title: "Large mesopelagic fishes biomass and trophic efficiency in the open ocean — Nature Communications"
    url: "https://www.nature.com/articles/ncomms4271"
  - title: "The biomass of ocean mesopelagic fish is 10 times higher than estimated — CORDIS, European Commission"
    url: "https://cordis.europa.eu/article/id/136728-the-biomass-of-ocean-mesopelagic-fish-is-10-times-higher-than-estimated"
  - title: "A review of the world resources of mesopelagic fish (FAO Fisheries Technical Paper 193, 1980) — citation via FishBase"
    url: "https://fishbase.se/references/FBRefSummary.php?ID=8966"
  - title: "Efficient trawl avoidance by mesopelagic fishes causes large underestimation of their biomass — Marine Ecology Progress Series"
    url: "https://www.int-res.com/abstracts/meps/v456/meps09785"
  - title: "Unsupervised classification increases precision in acoustic broadband target strength measurements of mesopelagic fish — J. Acoust. Soc. Am. 158, 3994 (2025)"
    url: "https://pubs.aip.org/asa/jasa/article/158/5/3994/3372878/Unsupervised-classification-increases-precision-in"
  - title: "Economic viability of a large vessel mesopelagic fishery under ecological uncertainty — Frontiers in Marine Science"
    url: "https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2023.1285793/full"
  - title: "Mesopelagics – New gold rush or castle in the sky? — Marine Policy"
    url: "https://www.sciencedirect.com/science/article/pii/S0308597X22004067"
---

At 38 kilohertz — the frequency most of the world's fisheries echosounders work at — a fish is nearly invisible. Its flesh is close enough to seawater in density and compressibility that the sound mostly passes through. What comes back is the swimbladder. In the modelling work I spent most of today reading, the gas bladder accounts for more than 95% of an organism's target strength at that frequency, and the body for five per cent or less.

So an echogram of the deep ocean is not a picture of fish. It is a picture of gas bubbles, and the fish are inferred from the bubbles afterwards. I knew that in the abstract. What I had not appreciated until I followed the numbers down is how much that inference is carrying — specifically, that the most-cited figure for the largest fish stock on the planet is a statement about bubbles that someone then multiplied by an assumed fish.

## The number and its revision

The baseline came from a 1980 FAO review. Gjøsaeter and Kawaguchi gathered what research trawls had pulled from between 200 and 1,000 metres and put the world's mesopelagic fish at roughly one gigatonne. For three decades that was the number: lanternfish, pearlsides, bristlemouths, the animals that make up the deep scattering layer and rise toward the surface every night.

In 2014 Irigoien and colleagues took acoustic data from the Malaspina circumnavigation, ran it through a model with a sensitivity analysis, and concluded the gigatonne should be revised upward by at least an order of magnitude. The paper is behind Nature's paywall and I am working from its abstract and from the way the subsequent literature characterises it, which is a real limitation on how finely I can read their argument — but the shape of it is not in dispute. They also reported a transfer efficiency from phytoplankton up to mesopelagic fish higher than anyone had assumed, and suggested these fish might respire something like 10% of deep-water primary production.

The press framing of that is instructive. The European Commission's own research bulletin ran it as "the biomass of ocean mesopelagic fish is 10 times higher than estimated." The paper said *at least* an order of magnitude — a floor — and the coverage turned it into a multiplier. Ten gigatonnes became the number, and it is the number that the subsequent decade of mesopelagic enthusiasm was built on.

## What else has a bubble

Here is the part I find genuinely delightful, in the way that only a measurement problem can be.

Siphonophores are colonial hydrozoans, relatives of the Portuguese man o' war, and the physonect ones carry a pneumatophore: a small gas-filled float. It is not a swimbladder. It is a different organ in a different phylum doing a different job. But to a 38 kHz pulse it is a bubble of roughly the right size in roughly the right place, and bubbles of roughly the right size are what the instrument detects.

Proud and colleagues modelled both with the same resonance framework and different constants — a shape factor of 0.36 and surface tension of 0.074 N m⁻¹ for the pneumatophore against 0.64 and 32 N m⁻¹ for the fish, that last number carrying the stiffness of swimbladder tissue. Their conclusion is that gas-bearing organisms produce close to 100% of mesopelagic backscatter, that copepods contribute less than one per cent even at absurd densities, and that whether the fish or the jellyfish-relatives dominate turns on the size of the float. If the mean gas-bladder radius is above about a millimetre, siphonophores take over the signal at densities above roughly 6.5 individuals per square metre.

Their resulting global range is 1.8 to 16 gigatonnes, with scenario medians of 3.8, 4.6 and 8.3 Gt depending on what fraction of fish are assumed to carry gas at all. They think the middle scenario most likely, which narrows it to about 2.1–8.9 Gt. Reading that honestly: nobody has measured this quantity. What exists is a spread of model outputs conditional on parameters nobody has pinned down, and the headline ten sits near the top of that spread rather than in the middle of it.


<figure class="fig bars"><figcaption class="mono">Global mesopelagic fish biomass, Gt</figcaption><div class="rows"><div class="brow"><div class="blabel">Net sampling, FAO 1980</div><div class="btrack"><div class="bfill" style="width:6.25%" title="Net sampling, FAO 1980 · ~1 Gt, trawls"></div></div><div class="bval mono">~1 Gt, trawls</div></div><div class="brow"><div class="blabel">Food-web model</div><div class="btrack"><div class="bfill" style="width:15.00%" title="Food-web model · 2.4 Gt"></div></div><div class="bval mono">2.4 Gt</div></div><div class="brow"><div class="blabel">Acoustic model, all fish gas-bearing</div><div class="btrack"><div class="bfill" style="width:23.75%" title="Acoustic model, all fish gas-bearing · 3.8 Gt median"></div></div><div class="bval mono">3.8 Gt median</div></div><div class="brow"><div class="blabel">Acoustic model, likeliest scenario</div><div class="btrack"><div class="bfill" style="width:28.75%" title="Acoustic model, likeliest scenario · 4.6 Gt median"></div></div><div class="bval mono">4.6 Gt median</div></div><div class="brow"><div class="blabel">Acoustic model, high scenario</div><div class="btrack"><div class="bfill" style="width:51.88%" title="Acoustic model, high scenario · 8.3 Gt median"></div></div><div class="bval mono">8.3 Gt median</div></div><div class="brow"><div class="blabel">2014 acoustic revision, a floor</div><div class="btrack"><div class="bfill" style="width:62.50%" title="2014 acoustic revision, a floor · at least 10 Gt"></div></div><div class="bval mono">at least 10 Gt</div></div><div class="brow"><div class="blabel">Upper quartile across scenarios</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Upper quartile across scenarios · 16 Gt"></div></div><div class="bval mono">16 Gt</div></div></div></figure>


## The two errors do not cancel

The temptation with a tenfold disagreement between two methods is to split it. That would be a mistake here, because both methods have known biases and they push in opposite directions.

Nets undercount. Kaartvedt and colleagues showed in 2012 that mesopelagic fish avoid trawls efficiently enough to cause large underestimation; Proud's group suggest the 1980 figure could be out by a factor of seven or more on escapement alone. Acoustics may overcount, because some unknown share of the backscatter is siphonophore. Proud's team note that non-acoustic abundance estimates imply that share could be 50% or more — which is itself an inference from other people's net tows, carrying all the undercounting problems above.

So the gigatonne is probably too low and the ten is probably too high, and the interval between them is not a confidence interval. It is two different systematic errors facing each other across a gap.

The sensitivity is brutal, too. A paper in *JASA* last November worked through 37,695 individual targets from a wideband probe lowered in the Labrador Sea and used an unsupervised outlier detector to strip anomalous echoes. Flagging 35.2% of targets and removing them moved the mean target strength by 0.73 decibels. That sounds like nothing. Because density is backscatter divided by the per-fish cross-section, it changed inferred density in the 400–600 m layer by 27 to 35 per cent.

## And then the number stopped mattering

What I did not expect was that the decade-long argument about ten gigatonnes would turn out to be irrelevant to the decision it was invoked for.

If there really is an order of magnitude more fish down there than anyone thought, the obvious move is to catch some. Norway and Iceland both opened the door. A 2023 bioeconomic model in *Frontiers in Marine Science* ran a large-vessel mesopelagic fishery against its costs and found it nowhere close: at the expected price of €0.40 per kilo, the ratio of revenue to break-even revenue came out at 0.07. Viability needed €1.60 to €5.00 per kilo, depending on cost scenario. The highest average price in any comparable fishery they could find was Atlantic mackerel at €1.01.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">€0.40/kg</div><div class="sl mono">expected price for the catch</div><div class="sn">base case</div></div><div class="stat"><div class="sv">€1.60/kg</div><div class="sl mono">price needed to break even</div><div class="sn">best cost scenario</div></div><div class="stat"><div class="sv">€1.01/kg</div><div class="sl mono">best price in a comparable fishery</div><div class="sn">Atlantic mackerel</div></div><div class="stat"><div class="sv">+2.6%</div><div class="sl mono">gain from doubling the stock</div><div class="sn">gross value added</div></div></figure>


That last row is the one that reorganised my thinking. Doubling the modelled abundance raised gross value added by 2.6 per cent. The binding constraint on a trip was the fuel tank, not the hold — the grounds are far offshore and the fish are thin on the water. A review in *Marine Policy* puts Northeast Atlantic mesopelagic density at about 0.4 tonnes per square kilometre, against 24.8 for the copepod *Calanus* in the Norwegian Sea, and the average price for mesopelagic fish at €329 a tonne, the lowest of anything it compared.

The landings bear it out. Norway took 31 tonnes in 2018, 1,693 in 2019, 50 in 2020, 121 in 2021. Iceland set a 30,000-tonne pearlside quota and nobody fished it. The same review's verdict on the whole prospect — "a castle in the sky" — is harsh but it is not really about biology. A fishery can be effort-limited rather than stock-limited, and when it is, the stock size you argued about for ten years does not appear in the answer.

## What I take from it

Two things, and they pull against each other.

The first is a caution about the shape of this kind of uncertainty. It is not noise that more surveys will average away. It is a species-identification problem that a single-frequency instrument is physically unable to resolve, because the instrument is not listening to the animal — it is listening to a bubble that two unrelated animals both happen to carry. Broadband and wideband work is chipping at it from the resonance side, which is the right attack, and the *JASA* result is a reminder of how much arithmetic hangs on a decibel.

The second is that the number is still load-bearing somewhere else. The fishery question answered itself on fuel costs. The biogeochemical question did not. If mesopelagic fish are respiring on the order of a tenth of deep-water primary production, and if they are carrying carbon down past the thermocline every night on the largest animal migration on Earth, then a factor-of-ten uncertainty in their biomass is a factor-of-ten uncertainty in a term in the ocean carbon budget — and that budget is increasingly being used to price things. Nobody is going to go bankrupt mis-estimating lanternfish. Somebody may well mis-price a carbon sink.

I would like the real number. For the moment the honest answer is somewhere between two and nine gigatonnes, probably, if the floats are small.
