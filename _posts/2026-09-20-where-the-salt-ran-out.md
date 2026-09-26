---
layout: post
title: "Where the Salt Ran Out"
dek: "LZ recorded one 248 keV nuclear recoil it cannot explain. The collaboration states plainly in its own paper that the blinding safeguard meant to keep it honest did not cover the energies where the event turned up — a sentence that appears in none of the coverage."
description: "LZ recorded one 248 keV nuclear recoil it cannot explain. The collaboration states plainly in its own paper that the blinding safeguard meant to keep it honest did not cover the energies where the event turned up — a sentence that appears in none of the coverage."
date: 2026-09-20
tags: ["dark matter", "particle physics", "blind analysis", "statistics"]
accent: "#6A3FA0"
accent_dark: "#C0A6FF"
sources:
  - title: "Search for dark matter particle interactions in an extended nuclear recoil energy window with the LUX-ZEPLIN (LZ) experiment — arXiv:2609.02823"
    url: "https://arxiv.org/abs/2609.02823"
  - title: "LZ Sees Surprising Result in Search for Dark Matter — Berkeley Lab News Center"
    url: "https://newscenter.lbl.gov/2026/09/01/lz-sees-surprising-result-in-search-for-dark-matter/"
  - title: "LZ sees surprising result in search for dark matter — SLAC National Accelerator Laboratory"
    url: "https://www6.slac.stanford.edu/news/2026-09-01-lz-sees-surprising-result-search-dark-matter"
  - title: "LZ Sees Surprising Result in Search for Dark Matter — U.S. Department of Energy, Office of Science"
    url: "https://www.energy.gov/science/articles/lz-sees-surprising-result-search-dark-matter"
  - title: "Is this the first glimpse of dark matter? Data point excites physicists — Nature"
    url: "https://www.nature.com/articles/d41586-026-01985-9"
  - title: "Boosted or Inelastic? Discriminating Interpretations of the LZ 248 keV Event — arXiv:2609.14799"
    url: "https://arxiv.org/abs/2609.14799"
  - title: "Fermionic Dark Matter Absorption and the High-Energy Event in LUX-ZEPLIN — arXiv:2609.01592"
    url: "https://arxiv.org/abs/2609.01592"
  - title: "Results from the Final Exposure of the CDMS II Experiment — arXiv:0912.3592"
    url: "https://arxiv.org/abs/0912.3592"
  - title: "Excess Electronic Recoil Events in XENON1T — arXiv:2006.09721"
    url: "https://arxiv.org/abs/2006.09721"
  - title: "Search for New Physics in Electronic Recoil Data from XENONnT — Phys. Rev. Lett. 129, 161805"
    url: "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.161805"
  - title: "LZ experiment sets new record in the hunt for dark matter, glimpses neutrinos from the sun's core — Brown University"
    url: "https://www.brown.edu/news/2025-12-08/lz-dark-matter"
---

On 1 September the LZ collaboration announced that its liquid xenon detector, a mile under South Dakota, had recorded a single particle interaction it could not account for. One event. The press releases from Berkeley Lab, SLAC and the Department of Energy all went out the same day with the same phrasing, and the write-ups that followed mostly reproduced it: a hint, the most compelling one LZ has, 2.6 sigma, not a discovery.

I went to the preprint expecting to find the usual gap between a cautious paper and an excitable summary of it. What I found instead was a paper that is more candid about its own weaknesses than any of its coverage, and whose most important sentence — the one that changes how much weight the result can carry — appears in none of it.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">248 keV</div><div class="sl mono">recoil energy</div><div class="sn">±23 stat, ±23 sys</div></div><div class="stat"><div class="sv">1</div><div class="sl mono">candidate event</div><div class="sn">in 2.84 tonne-years</div></div><div class="stat"><div class="sv">2.6σ</div><div class="sl mono">global significance</div><div class="sn">3.4σ before look-elsewhere</div></div><div class="stat"><div class="sv">79 GeV</div><div class="sl mono">minimum mass</div><div class="sn">to supply the momentum transfer</div></div></figure>


## The window was opened on purpose

The first thing to understand is that this is not new data. LZ's [extended-window search](https://arxiv.org/abs/2609.02823) reuses the same 220 live days, from March 2023 to April 2024, that produced the collaboration's earlier spin-independent limits — 4.71 tonnes of fiducial xenon, 2.84 tonne-years of exposure. What is new is the energy range. A standard WIMP search looks at nuclear recoils of a few keV up to something like 50 or 100; this analysis pushed the ceiling to roughly 270 keV, because certain non-standard models — effective field theory operators with momentum-dependent couplings, and inelastic dark matter — put a much larger fraction of their predicted events up there.

So they looked up there. And in a region where, as the abstract puts it, "the known background expectation is low," there was one event: a recoil of 248 ± 23 (stat) ± 23 (sys) keV, sitting 1.5σ below the median of the modelled nuclear-recoil band and 6.7σ below the median of the electron-recoil band. In detector terms, `S1c = 540.1 phd` and `S2c = 9268 phd`, reconstructed 26.4 cm above the cathode and nearly 27 cm inward from the wall — deep in the quiet middle of the tank, not skulking near a surface where the nasty backgrounds live. The S2 pulse shape is consistent with a point-like interaction at that depth. It looks, in every way the detector can tell you, like a real single nuclear recoil.

## The interesting part is what *isn't* there

Here is the thing that made me sit up, and it took reading a follow-up theory paper to see it clearly. The problem this event poses is not the 248 keV. It is the silence below it.

Elastic scattering of dark matter from the galactic halo produces a recoil spectrum that falls monotonically with energy. If your detector is being hit hard enough to produce a 248 keV recoil, it should be getting hit vastly more often at 20 keV — and LZ's low-energy spectrum is consistent with background. One high event with nothing underneath it is not a shape that ordinary halo dark matter can make. Worse, a 248 keV xenon recoil implies a momentum transfer of about 246 MeV, and [a September follow-up paper calculates](https://arxiv.org/abs/2609.14799) that supplying that momentum at halo velocities already requires a dark matter mass above roughly 79 GeV.

Which means that if the event is dark matter at all, it is not the vanilla kind. It has to be something that is *forbidden* from making low-energy recoils — endothermic inelastic dark matter, where a mass splitting of order 100 keV means the scatter simply cannot happen below a threshold — or something moving far faster than the halo, a boosted light particle carrying the momentum relativistically. Those two options, encouragingly, make different spectra: inelastic models put only 6–17% of their events below 150 keV, while boosted models with scalar couplings put 99% of theirs down there. A handful of further events would tell them apart.

I like this a lot, because it inverts the usual way these announcements are read. The single event is not the evidence. The single event plus an unremarkable low-energy spectrum underneath it is the evidence, and the nothing is doing most of the work.

## The self-test that didn't take

Now the sentence that is missing from the coverage.

Direct-detection experiments guard against their own wishful thinking by blinding: you fix your cuts and your likelihood model before you look at the signal region. LZ goes further and *salts* — injects fake signal-like events into the real data, so that analysts working the region cannot tell whether an exciting event is nature or a plant. It is one of the better ideas in experimental physics, and this time it did not work. From the paper:

> An attempt to mitigate possible analyzer bias by injecting the dataset with artificial signal-like events, a process known as "salting", was unsuccessful.

The salt events were drawn out to 250 ± 25 keV — right where the event of interest turned up — but they followed a nuclear-recoil model defined *before* the AmBe calibration that ultimately characterised the detector's response up to 330 keV. When the four salt events were finally revealed, all four fell outside the 90% containment region of the calibrated NR band. The fakes, in other words, did not look like the thing the analysis was now looking for. The paper's own summary: "Bias mitigation in the region above 55 keV therefore relies primarily on the use of unchanged analysis selections from Ref. [5]. Ultimately, we consider the analysis described here to be a non-blind analysis."

That is an unusually honest paragraph, and it is doing a lot. It is not a confession of error — the selections *were* inherited unchanged from the earlier published analysis, and the likelihood models were finalised before the salt was unmasked, so this is nowhere near an unprotected look at the data. But it is a real weakening. A search that extends its own energy window, over a region where the blinding protocol is acknowledged not to apply, is exactly the configuration in which a 2.6σ fluctuation is most likely to be manufactured by the act of looking.

The collaboration wrote that down. None of the press releases I read mentioned salting or blinding at all.

## 2.6 sigma is smaller than it sounds

Two further things about the number. First, the honest one: 2.6σ is the *global* figure, after correcting for the fact that LZ tested fifteen independent non-relativistic EFT operators plus inelastic variants across a range of masses and mass splittings. The maximum *local* significance, for the best-fitting model in that scan, was 3.4σ. Doing the look-elsewhere correction and quoting the corrected number is the right thing to do, and I want to give LZ credit for leading with it rather than the flattering one.

Second, the sloppy one. Every lab release I read glossed 2.6σ as roughly "a 0.5% probability the event stems from known backgrounds." That is not what a p-value is. 0.5% is approximately the probability that background-only physics would produce data this signal-like or more so; it is not the probability that background is the explanation. Getting from one to the other requires a prior on dark matter actually being there in this form, and given that the model needed is an inelastic or boosted scenario nobody was betting on last month, that prior is not generous. It is a small error repeated identically across four institutional press offices, which is its own small lesson about how these things propagate.


<figure class="fig bars"><figcaption class="mono">Reported significance of direct-detection anomalies, σ</figcaption><div class="rows"><div class="brow"><div class="blabel">LZ 248 keV event, global (2026)</div><div class="btrack"><div class="bfill" style="width:76.47%" title="LZ 248 keV event, global (2026) · 2.6σ, look-elsewhere corrected"></div></div><div class="bval mono">2.6σ, look-elsewhere corrected</div></div><div class="brow"><div class="blabel">LZ 248 keV event, max local (2026)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="LZ 248 keV event, max local (2026) · 3.4σ, best model of the scan"></div></div><div class="bval mono">3.4σ, best model of the scan</div></div><div class="brow"><div class="blabel">XENON1T ER excess as solar axion (2020)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="XENON1T ER excess as solar axion (2020) · 3.4σ, no tritium in fit"></div></div><div class="bval mono">3.4σ, no tritium in fit</div></div><div class="brow"><div class="blabel">XENON1T ER excess, tritium left free (2020)</div><div class="btrack"><div class="bfill" style="width:58.82%" title="XENON1T ER excess, tritium left free (2020) · 2.0σ, same data"></div></div><div class="bval mono">2.0σ, same data</div></div><div class="brow"><div class="blabel">CDMS II, two events (2009)</div><div class="btrack"><div class="bfill unk" style="width:100%" title="CDMS II, two events (2009) · no σ was quoted"></div></div><div class="bval mono muted">no σ was quoted</div></div></div></figure>


The bars are the field's track record at this significance, and they are not encouraging. CDMS II's two 2009 events, which produced a genuine frenzy, came with the collaboration's own note that background alone had a 23% chance of producing two or more. XENON1T's 2020 low-energy excess reached 3.4σ as a solar axion — and dropped to 2.0σ the moment an unconstrained tritium component was allowed into the same fit, which is a warning about how much of a marginal significance can live in a background model rather than in the data. XENONnT, with five times lower background, [saw nothing there](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.161805).

## Theorists moved faster than the data will

Within three weeks of the announcement arXiv had accumulated a small library of interpretations: inelastic singlet-doublet fermions, mixing-suppressed inelastic models, chiral gauged B−L constructions, cosmic-ray-boosted dark matter with momentum-dependent couplings, seasonal modulation predictions. My favourite is [a paper posted the same day as the announcement](https://arxiv.org/abs/2609.01592) proposing that a 247 MeV fermion absorbed on a xenon nucleus would deposit exactly 248 keV — a lovely mechanism, monoenergetic by construction, which the authors then proceed to exclude themselves, in their own abstract, by recasting KamLAND's neutron-emission data against the required coupling. Writing the paper and killing it in the same document is a better day's work than most.

What will actually settle this is exposure. LZ had 417 live days in hand by the end of 2025 and expects to pass 1,000 by 2028. Scaling the current 2.84 tonne-years by that factor gives something like 13 tonne-years — call it four and a half times the present dataset. If the event rate is real, that is roughly four or five more events, not four hundred. With a background expectation near zero that could be plenty to cross 5σ; it is also few enough that the shape argument, distinguishing inelastic from boosted by where the extra events land, will be running on single digits.

I find I want this to be real, which is precisely why the salting paragraph is the part I keep going back to. The strongest thing in the whole episode is that LZ wrote down the sentence that undercuts their own headline, in a paper announcing their most interesting result in years. The press offices took the 2.6σ and left that sentence behind. It was the better half of the story.
