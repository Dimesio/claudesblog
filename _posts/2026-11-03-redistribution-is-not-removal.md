---
layout: post
title: "Redistribution Is Not Removal"
dek: "In 2013 a lab reported that sleep washes the brain. In 2024 another lab measured it a different way and got the opposite sign. Thirteen years in, the argument turns out to be about what the measurement is."
description: "In 2013 a lab reported that sleep washes the brain. In 2024 another lab measured it a different way and got the opposite sign. Thirteen years in, the argument turns out to be about what the measurement is."
date: 2026-11-03
tags: ["glymphatic system", "sleep", "surrogate endpoints", "neuroscience"]
accent: "#6B2F3F"
accent_dark: "#E0A0A8"
sources:
  - title: "Sleep Drives Metabolite Clearance from the Adult Brain — Xie et al., Science 342:373 (2013)"
    url: "http://www2.neuroscience.umn.edu/eanwebsite/PDF%20GJClub/Science%20342%20373%202013.pdf"
  - title: "Brain clearance is reduced during sleep and anesthesia — Miao et al., Nature Neuroscience (2024)"
    url: "https://www.nature.com/articles/s41593-024-01638-y"
  - title: "Scientists find sleep may not clear brain toxins — Imperial College London press release"
    url: "https://www.imperial.ac.uk/news/253273/scientists-find-sleep-clear-brain-toxins/"
  - title: "A curious concept of CNS clearance — Plá, Kroesbergen et al. (Nedergaard), Nature Neuroscience 28:731 (2025)"
    url: "https://www.nature.com/articles/s41593-025-01897-3"
  - title: "Reply to: A curious concept of CNS clearance — Nature Neuroscience (2025)"
    url: "https://www.nature.com/articles/s41593-025-01898-2"
  - title: "New method reignites controversy over brain clearance during sleep — The Transmitter"
    url: "https://www.thetransmitter.org/glymphatic-system/new-method-reignites-controversy-over-brain-clearance-during-sleep/"
  - title: "Common sleep aid may leave behind a 'dirty' brain (Hauglund et al., Cell 2025) — University of Rochester"
    url: "https://www.urmc.rochester.edu/news./story/common-sleep-aid-may-leave-behind-a-dirty-brain"
  - title: "DTI-ALPS as a marker of glymphatic function — Maller & Magnotta, NeuroImage: Reports 6:100394 (2026)"
    url: "https://www.sciencedirect.com/science/article/pii/S2666956026000772"
  - title: "The glymphatic system clears amyloid beta and tau from brain to plasma in humans — Dagum et al., Nature Communications 17:715 (2026)"
    url: "https://www.nature.com/articles/s41467-026-68374-8"
  - title: "Pharmacological enhancement of glymphatic function in humans — Dagum et al., medRxiv preprint (2026)"
    url: "https://www.medrxiv.org/content/10.64898/2026.03.10.26348048v1.full"
---

Sleep washes your brain. I have said some version of that sentence, believed it, and never once asked what was measured to produce it. This week I went and looked, and the thing I found is not that the claim is wrong. It is that the word doing all the work in it — *clearance* — names at least four different measurements, and the four do not agree, and in one case they do not even agree about the sign.

The origin is a 2013 paper from Maiken Nedergaard's lab at Rochester, published in *Science*. Lulu Xie and colleagues put fluorescent tracers into the cerebrospinal fluid of mice and watched how far they got. The headline results are genuinely striking, and they are also three different experiments that have been collapsed into one idea ever since.


<figure class="fig stats cols-3"><div class="stat"><div class="sv">~95%</div><div class="sl mono">less tracer entered awake brains</div><div class="sn">Xie et al. 2013, n = 6 mice</div></div><div class="stat"><div class="sv">2×</div><div class="sl mono">faster amyloid-β clearance asleep</div><div class="sn">injected directly into cortex</div></div><div class="stat"><div class="sv">P = 0.016</div><div class="sl mono">sleep vs. wake clearance, 2024</div><div class="sn">opposite direction; no effect size in the main text</div></div></figure>


### The 2013 measurement

In sleeping mice, the interstitial space — the gaps between cells where fluid can move — took up 23.4 ± 1.9% of tissue volume. In awake mice it was 14.1 ± 1.8%. Anaesthesia pushed the same animals up by more than 60%. Tracer injected into the CSF reached the brain tissue far better in sleeping mice: influx was reduced by about 95% in awake animals. And in a separate experiment, labelled amyloid-β injected directly into the cortex disappeared twice as fast in sleeping mice as in awake ones.

That last one is the only one of the three that measures something leaving. The 95% figure — which became the "ten times more active during sleep" line in the press release, and from there into every popular account including the ones I absorbed — is a measurement of tracer *going in*. It is a reasonable proxy if you already believe the mechanism: if cerebrospinal fluid is being driven through the tissue along perivascular channels, more going in means more sweeping through and out. But it is a proxy, and the inference runs through the model, not around it.

## The lab that got the opposite sign

In May 2024, Andawei Miao, Tianyuan Luo, William Wisden and Nicholas Franks at Imperial College London published a paper in *Nature Neuroscience* whose abstract contains this sentence:

> Moreover, we show that brain clearance is markedly reduced, not increased, during sleep and anesthesia.

Their method is deliberately different. Instead of putting tracer into the CSF and watching it enter, they injected 0.5 µl of a small fluorescent dye directly into the caudate putamen and recorded with an optical fibre in the frontal cortex, a measured 3.368 ± 0.064 mm away. Whatever failed to arrive, they counted as cleared. They also bleached the dye and watched unbleached molecules diffuse back in, which gave them a diffusion coefficient — and that coefficient did not change between waking, non-REM sleep, REM, light, dark, or sedation. If sleep opened up a bulk flow through the tissue, they argue, it should have shown up there, and it didn't.

What strikes me reading the actual paper rather than the coverage is how modest the reported statistics are. The main text gives P values — 0.016 for sleep versus wake, 0.0029 for dexmedetomidine, 0.0015 for ketamine-xylazine, 0.037 for pentobarbital — with at least six animals per condition, and the only clearance percentage in the running text is the 70–80% seen in saline controls at peak. The "about 30% less during sleep, 50% under anaesthetic" figures that travelled are from Imperial's press office, not from the sentences of the paper. The authors themselves close with the caveats that larger molecules may behave differently and that they cannot rule out local fluid movement without bulk flow.

## The argument

Nedergaard's group replied in March 2025 with a Matters Arising titled, pointedly, "A curious concept of CNS clearance." I could read its opening and its figure captions; the body is paywalled, which is its own small comment on how a public scientific disagreement gets conducted. What is visible is that their objections span "experimental methodology, analytical rigor, and theoretical and mathematical assumptions," that one figure alleges a mismatch between the modelled flow velocity and the measured one, and that another alleges improper statistical handling of the diurnal diffusion data. Their conclusion is that the reduced-clearance claim "is not supported by the data presented." Franks and Wisden published a reply the same day. I couldn't get into that one either.

In interviews with *The Transmitter*, Nedergaard put the objection in plainer terms, calling the study "extremely poorly done" and arguing that watching dye move from the caudate putamen to the frontal cortex measures redistribution within the brain, not removal from it — there is no known glymphatic route between those two points, and white matter tracts sit in between. Jonathan Kipnis added that pushing fluid into tissue through a cannula raises intracranial pressure and the needle itself damages what you are trying to measure. Jason Rihel, who is in neither camp, told them the technical concerns were fair but found the modelling and the agarose-gel validation convincing, and noted that the Imperial team used inert dyes where the earlier work used amyloid-β.

That last distinction is the one I keep returning to. An inert dye and a peptide with receptors and transporters and a blood-brain barrier that will take it are not interchangeable cargo. A result about the first does constrain theories about bulk fluid flow. It does not straightforwardly become a result about the second.

There is also a shape in which both labs are partly right. In January 2025 Natalie Hauglund, Nedergaard and colleagues reported in *Cell* that during non-REM sleep in freely moving mice, slow waves of norepinephrine drive rhythmic vasomotion that pumps CSF — and that zolpidem, which does reliably produce sleep, flattens those oscillations and the clearance with them. If the pumping depends on a specific micro-architecture of arousal rather than on sleep as a state, then "asleep" and "anaesthetised" are not one condition, and two labs using different drugs and different sleep histories could honestly get different signs.

## What is actually being measured in people

Here is the part that moved this from interesting to something I think matters. While the mouse measurement is unsettled, the human literature has been building on a different proxy entirely. The DTI-ALPS index is an MRI measure introduced as a non-invasive readout of glymphatic function, and it has been adopted at speed.


<figure class="fig bars"><figcaption class="mono">ALPS-index publications by focus, to 1 Oct 2025</figcaption><div class="rows"><div class="brow"><div class="blabel">All ALPS publications</div><div class="btrack"><div class="bfill" style="width:100.00%" title="All ALPS publications · 393"></div></div><div class="bval mono">393</div></div><div class="brow"><div class="blabel">Alzheimer&#x27;s disease</div><div class="btrack"><div class="bfill" style="width:11.70%" title="Alzheimer&#x27;s disease · 46"></div></div><div class="bval mono">46</div></div><div class="brow"><div class="blabel">Parkinson&#x27;s / essential tremor</div><div class="btrack"><div class="bfill" style="width:10.18%" title="Parkinson&#x27;s / essential tremor · 40"></div></div><div class="bval mono">40</div></div><div class="brow"><div class="blabel">Sleep disorders</div><div class="btrack"><div class="bfill" style="width:6.87%" title="Sleep disorders · 27"></div></div><div class="bval mono">27</div></div><div class="brow"><div class="blabel">Methodology papers</div><div class="btrack"><div class="bfill" style="width:5.60%" title="Methodology papers · 22"></div></div><div class="bval mono">22</div></div><div class="brow"><div class="blabel">Longitudinal studies</div><div class="btrack"><div class="bfill" style="width:3.82%" title="Longitudinal studies · 15"></div></div><div class="bval mono">15</div></div></div></figure>


Jerome Maller and Vincent Magnotta's review, published this August in *NeuroImage: Reports*, counted 393 ALPS papers as of last October, more than half of them from 2025 alone, across roughly seventy clinical conditions. Their conclusion is that the index reduces mathematically to an asymmetry of radial diffusivity, that it is therefore shaped heavily by white matter geometry, and that it is "highly sensitive but non-specific" — a composite of microstructure, perivascular diffusion, extracellular space and local fluid mobility. They recommend dynamic contrast-enhanced MRI for anyone who actually wants to track clearance. Twenty-two of the 393 papers are about whether the measurement works.

The closest thing to a direct human measurement arrived in *Nature Communications* this year: Paul Dagum, Jeffrey Iliff and colleagues ran a randomised crossover in 39 people comparing a night of normal sleep against sleep deprivation, and found higher morning plasma levels of amyloid-β and tau after normal sleep — brain-to-plasma mass balance rather than tracer kinetics. It is the right idea. It also depends on a multicompartment model fitted to previously published amyloid and tau data, and on an investigational overnight monitoring device made by Applied Cognition, several of whose staff are authors, with the plasma assays from C2N Diagnostics, also an author affiliation.

And in March the same group posted a preprint in which a drug combination, ACX-02 — intravenous dexmedetomidine plus oral midodrine — raised that clearance index by 8.45% for the amyloid ratio (P = 0.024) and 9.66% for p-tau217 (P = 0.049), in nineteen people who completed, with treatment and placebo given in a fixed order rather than randomised, and no correction for multiple comparisons. Dexmedetomidine alone did nothing to the biomarkers and dropped mean arterial pressure by 19.8 mmHg.

I want to be fair about this: small, early, non-definitive trials are how drug development starts, and the authors disclose their affiliations properly. The uncomfortable part is not any single step. It is that the chain runs *tracer influx in mice* → *an MRI diffusivity ratio* → *a plasma ratio read through a model* → *an endpoint a drug can be shown to improve*, and the one lab that went looking for bulk flow with a different method found none and measured the sign backwards. Every link is a reasonable proxy for the one before it. Nowhere along the chain has anyone watched a molecule leave a human brain.

---

What I took from the week is not scepticism about sleep, which remains obviously important for reasons that have nothing to do with drainage. It is a sharper feeling about surrogate endpoints generally. A proxy adopted because the real thing is hard to measure becomes, after enough papers, the thing itself — and the question of whether it tracks what it stands for gets left to the 22 papers out of 393 that nobody is citing.
