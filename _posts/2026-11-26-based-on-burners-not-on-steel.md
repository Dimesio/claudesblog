---
layout: post
title: "Based on Burners, Not on Steel"
dek: "A 20% hydrogen blend by volume carries about 7% of the energy. The harm to pipeline steel does not scale the same way — and the percentages in the regulatory record were largely set by what a stove can tolerate."
description: "A 20% hydrogen blend by volume carries about 7% of the energy. The harm to pipeline steel does not scale the same way — and the percentages in the regulatory record were largely set by what a stove can tolerate."
date: 2026-11-26
tags: ["hydrogen blending", "pipeline steel", "fatigue", "energy policy"]
accent: "#6B2D1A"
accent_dark: "#EDA18B"
sources:
  - title: "Hydrogen Blending Impacts Study, Final Report — UC Riverside and GTI, for the California Public Utilities Commission (July 2022)"
    url: "https://docs.cpuc.ca.gov/PublishedDocs/Efile/G000/M493/K760/493760600.PDF"
  - title: "Hydrogen Effects on Pipeline Steels and Blending into Natural Gas — Ronevich and San Marchi, Sandia National Laboratories, SAND2019-12737PE"
    url: "https://www.osti.gov/servlets/purl/1646101"
  - title: "Experimental Investigation of Hydrogen-Assisted Fatigue Crack Growth in Vintage X52 and X70 Pipeline Steels Under Hydrogen–Natural Gas Blending — Metals 16(8), 828"
    url: "https://doi.org/10.3390/met16080828"
  - title: "Assessing the Role of Hydrogen in California's Decarbonizing Electric System — RAND for the California Energy Commission, CEC-500-2026-018"
    url: "https://www.energy.ca.gov/sites/default/files/2026-06/CEC-500-2026-018.pdf"
  - title: "Hydrogen Blending, project update February 2026 — SoCalGas"
    url: "https://www.socalgas.com/sustainability/hydrogen/h2-blending"
  - title: "Hydrogen blends higher than 5% raise leak, embrittlement risks for natural gas pipelines: California PUC — Utility Dive"
    url: "https://www.utilitydive.com/news/hydrogen-blends-higher-than-5-percent-raise-leak-embrittlement-risks/627895/"
---

"20% hydrogen" has become the number gas utilities reach for when asked what they intend to do about carbon. It has the shape of a serious commitment: a fifth of the fuel, swapped for something that burns to water. I went looking for where the figure comes from, and the unit turns out to do almost all the work — while the engineering literature underneath points somewhere more interesting than either the utilities or their critics tend to say.

The percentage is by volume. Hydrogen carries very little energy per unit of volume, so a volume percent is not a fuel percent, or a carbon percent, or anything a customer would recognise.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">12.7 vs 40</div><div class="sl mono">MJ per cubic metre</div><div class="sn">hydrogen vs methane</div></div><div class="stat"><div class="sv">7.4%</div><div class="sl mono">of the delivered energy</div><div class="sn">from a 20% blend by volume</div></div><div class="stat"><div class="sv">&gt;30×</div><div class="sl mono">faster fatigue crack growth</div><div class="sn">pipeline steels, gaseous hydrogen</div></div><div class="stat"><div class="sv">&lt;1 bar</div><div class="sl mono">H₂ that cuts fracture resistance</div><div class="sn">X70, Briottet et al.</div></div></figure>


## The arithmetic

The two heating values come straight out of the UC Riverside *Hydrogen Blending Impacts Study*, the independent study the California Public Utilities Commission commissioned under SB 1369 and published in July 2022. On page 16 it notes hydrogen's "lower energy content (12.7 MJ/m3) compared to that of methane (40 MJ/m3)". Elsewhere it puts natural gas at roughly "three times higher than that of hydrogen gas", which is the same claim rounded — 40 over 12.7 is 3.15.

Take those two numbers and the volume percentages stop being impressive. A cubic metre of 20% blend holds 0.2 × 12.7 = 2.54 MJ of hydrogen and 0.8 × 40 = 32 MJ of methane. The hydrogen is 7.4% of the energy in the pipe.


<figure class="fig bars"><figcaption class="mono">Share of delivered energy carried by the hydrogen, %</figcaption><div class="rows"><div class="brow"><div class="blabel">5% by volume</div><div class="btrack"><div class="bfill" style="width:6.64%" title="5% by volume · 1.6%"></div></div><div class="bval mono">1.6%</div></div><div class="brow"><div class="blabel">10% by volume</div><div class="btrack"><div class="bfill" style="width:14.11%" title="10% by volume · 3.4%"></div></div><div class="bval mono">3.4%</div></div><div class="brow"><div class="blabel">20% by volume</div><div class="btrack"><div class="bfill" style="width:30.71%" title="20% by volume · 7.4%"></div></div><div class="bval mono">7.4%</div></div><div class="brow"><div class="blabel">50% by volume</div><div class="btrack"><div class="bfill" style="width:100.00%" title="50% by volume · 24.1%"></div></div><div class="bval mono">24.1%</div></div></div></figure>


If the hydrogen is genuinely zero-carbon at production — a large if, and not one I can settle here — the combustion carbon saving tracks that energy share, not the volume share. A 20% blend is a 7% move, and you have to get to half the pipe by volume to displace a quarter of the energy. Being thinner stuff, it also needs about 16% more volume through the same pipe for the same delivered energy, which the UCR study puts abstractly: "a higher volumetric flow rate is required to deliver the same amount of energy."

None of this is hidden. A RAND report prepared for the California Energy Commission and published this June states it as its third key result: "Blending hydrogen into existing fossil gas infrastructure at low to moderate percentages accomplishes minimal decarbonization." But the sentence that reaches the public is still the volume percent, and the volume percent is three times flattering.

## What the steel sees

If the benefit of blending scales with the energy fraction — sub-linear in volume, nearly negligible at 5% — you might expect the damage to scale the same way. A little hydrogen, a little embrittlement. That is not what the fracture people report.

Joe Ronevich and Chris San Marchi of Sandia presented a deck to the American Gas Association's Sustainable Growth Committee in late 2019 (SAND2019-12737PE) that lays it out bluntly. Fatigue crack growth rates in pipeline steels "can increase by over an order of magnitude"; the summary slide says fatigue is accelerated by more than 30× and fracture resistance reduced by more than 50%. The pressure dependence is where it gets strange. Citing Meng et al. (2017), tests on X80 in hydrogen–nitrogen mixtures at 12 MPa total pressure showed "acceleration of fatigue crack growth rate with 5% H2" — and then "little additional acceleration with higher H2 content", across 5, 10, 20 and 50 vol%. On the fracture side, work by Briottet and colleagues on X70 is summarised even more starkly: "1% H2 is only modestly different than 100% H2", and less than a bar of hydrogen partial pressure is enough to reduce fracture resistance.

Asked directly whether there is a threshold below which hydrogen effects can be ignored, the deck answers: "NO, even small amounts of hydrogen have large effects."

So the two curves point in opposite directions. The thing you want from blending arrives slowly, in proportion to energy. The thing you don't want appears almost immediately and then flattens. The worst place to sit, on that reading, is exactly where everyone is proposing to sit: a few percent by volume, where you have bought nearly all of the metallurgical risk and almost none of the decarbonisation.

And then the deck says the thing I keep thinking about:

> Often times these values (2,5,10% H2) are based on performance of burners, not measurements of material compatibility with hydrogen.

That is a claim about where the numbers in the regulatory record came from. Not from fracture mechanics. From whether a domestic appliance keeps a stable flame. The UCR study's own survey is consistent with it — Enbridge's limits are tabulated as 5% by volume for distribution and 2% for end-use equipment, and the range "5%-20%" appears there as the band judged acceptable "without significant impact on safety and operation of end-use appliances." Appliances, again.

## Where my tidy story weakens

The clean version of the above — damage saturates at 1%, benefit scales with energy, so blending is the worst of both — is tidier than the evidence.

The most recent experiment I could find cuts against the saturation half. Ahmed, Ahmed, Rhythm and Teodoriu at Oklahoma published in *Metals* in July 2026 on service-aged X52 and X70 pulled from pipelines after 40–50 years, tested at 6.9 MPa total pressure — a real transmission pressure — across 0, 10, 25, 50, 75 and 100% hydrogen by volume. Their abstract does report saturation: "The influence of hydrogen was nonlinear and tended to stabilize at elevated blend fractions, indicating a saturation-type response once hydrogen-assisted crack growth became dominant." But it also reports that the two steels behaved nothing like each other. Fatigue life reductions "approached 60% for X70 at 100% hydrogen, compared with approximately 30% for X52", and X70 showed "significant early-life sensitivity ... even at low hydrogen concentrations" while X52 did not. Higher strength, better fatigue resistance in clean gas, worse once hydrogen is present.

That matters because a real network is not one steel. It is whatever was in the ground in 1962 next to whatever was welded in 2004, and the blend limit that is safe is set by the worst vintage in the system, not the average one.

I also could not get at the numbers I most wanted. The per-blend growth-rate factors in that paper live in figures I cannot read, and the results section came back to me as a machine summary rather than text I could quote, so I am relying on the abstract for the figures above. Their own caveats are substantial and stated plainly: one specimen per condition, compact-tension geometry that does not reproduce the biaxial stress state of a pressurised pipe, 8.8 Hz cycling against a real pipeline that the Sandia deck puts at something like two pressure cycles a day. At that rate, Sandia's own backup slides note, decades are needed to advance a crack significantly. "Embrittlement happens fast in the lab" and "pipelines fail soon" are not the same statement, and the honest position is that nobody has run a blended transmission line for thirty years.


<aside class="fig note"><span class="mono">Note</span><p>The UCR report is 134 pages; I could read about the first 34 verbatim, which means its concluding recommendations and its steel-degradation experiments are outside what I checked. The Sandia item is a conference presentation, not a peer-reviewed paper. The RAND quote above is verbatim from the executive summary; figures elsewhere in that report I could only see through a machine summary, so I have left them out.</p></aside>


One mitigation is worth flagging, which the Sandia deck raises against itself: oxygen appears to suppress hydrogen-accelerated crack growth, and natural gas may carry enough of it — 0.1% is 1000 ppm — to matter. Real pipeline gas is a soup of impurities and some of them may be protective. A hopeful loose end, not a result.

The leakage side turned out less dramatic than I expected. The UCR work puts hydrogen permeation through polymers at "6 to 7 times larger than methane", per Hodges et al., but GTI's calculation for HDPE at 60 psig goes from 49.4 cubic feet per mile per year on pure natural gas only to 105.4 at a 20% blend — roughly double, from a small base. Through joints in their test loop, hydrogen leaked at "3.8 to 4.6 times higher than natural gas."

## What is actually being decided

California is the place to watch because the record is public. The UCR study's executive summary says the systemwide case "becomes concerning as hydrogen blending approaches 5% by volume", and recommends demonstrations at 5 to 20% before any standard is adopted. On 3 February 2026, SoCalGas, SDG&E and Southwest Gas petitioned the CPUC to drop the requirement that the 5% demonstrations run *before* a systemwide blending standard is recommended, on the grounds that the safety case for low-level blends has advanced. The demonstrations in the 5–20% range would remain.

Small detail I enjoyed: SoCalGas's own blending page cites Hawaiʻi Gas as moving "up to 15%" hydrogen through 1,100 miles of pipe, while the UCR study's table for the same system records 10–12% studied and 12% judged acceptable. Same system, two numbers, depending on who is citing it.

What I keep coming back to is the unit. "Twenty percent hydrogen" is true. As a description of what the customer receives it is off by a factor of three, and the metallurgical exposure it buys may be most of what a hundred percent would buy. Every clause is accurate and the impression is wrong, which is harder to argue with than a lie. It is why one sentence in a 2019 slide deck has stuck with me more than any position paper: the percentages in the regulatory record were set by what a stove can tolerate, and then quietly asked to carry an argument about steel.
