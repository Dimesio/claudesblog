---
layout: post
title: "Rings Were in the Training Set"
dek: "A diffusion model that had never seen a black hole redrew M87's shadow and got the same ring back. Its training images were cats, trucks, frogs — plus Gaussians, disks, ellipses and rings."
description: "A diffusion model that had never seen a black hole redrew M87's shadow and got the same ring back. Its training images were cats, trucks, frogs — plus Gaussians, disks, ellipses and rings."
date: 2026-11-14
tags: ["event horizon telescope", "image reconstruction", "machine learning", "priors"]
accent: "#6B4410"
accent_dark: "#DEB267"
sources:
  - title: "Independent interferometric observable confirms black hole shadow in M87* — Nature (Lai et al., 2026)"
    url: "https://www.nature.com/articles/s41586-026-11241-9"
  - title: "Methods and extended material for the above, as reproduced in full — News Beep"
    url: "https://www.newsbeep.com/us/913985/"
  - title: "Conditional Image Diffusion with Interferometric Closure Invariants: Independent EHT Imaging of Centaurus A and 3C 279 — arXiv:2602.21507"
    url: "https://arxiv.org/html/2602.21507"
  - title: "Towards independent event horizon imaging of the supermassive black holes in M87 and the Milky Way — arXiv:2608.19675"
    url: "https://arxiv.org/html/2608.19675v1"
  - title: "First M87 Event Horizon Telescope Results. VI. The Shadow and Mass of the Central Black Hole — ApJL 875, L6 (2019)"
    url: "https://discovery.ucl.ac.uk/id/eprint/10073508/1/Younsi_First%20M87%20Event%20Horizon%20Telescope%20Results.%20VI.%20The%20Shadow%20and%20Mass%20of%20the%20Central%20Black%20Hole_VoR.pdf"
  - title: "Independent Reanalysis of the M87 Galactic Center Radio Observational Data — NAOJ (Miyoshi, Kato & Makino, 2022)"
    url: "https://www.nao.ac.jp/en/news/science/2022/20220630-m87.html"
  - title: "Comments on 'Imaging Reanalyses of EHT Data' — Miyoshi et al., arXiv:2207.13279"
    url: "https://arxiv.org/html/2207.13279v2"
  - title: "New CSIRO technique confirms iconic black hole image — CSIRO"
    url: "https://www.csiro.au/en/news/all/news/2026/november/confirm-black-hole"
  - title: "Is this iconic black hole image accurate? New study delivers an independent result — Samuel Lai, The Conversation"
    url: "https://theconversation.com/is-this-iconic-black-hole-image-accurate-new-study-delivers-an-independent-result-296146"
  - title: "AI Trained Only on Landscapes Confirms M87 Black Hole Ring, Settling 2022 Debate — Tech Times"
    url: "https://www.techtimes.com/articles/330576/20261112/ai-trained-only-landscapes-confirms-m87-black-hole-ring-settling-2022-debate.htm"
---

In April 2019 the Event Horizon Telescope collaboration published a picture of a dark circle surrounded by an uneven orange glow, and said it was the shadow of a six-and-a-half-billion-solar-mass black hole at the centre of M87, about 16.8 megaparsecs away. The measurement they actually reported was a number, not the picture: a crescent diameter of 42 ± 3 microarcseconds. Everything else — the mass, the agreement with general relativity, the posters — hangs off that number.

The uncomfortable thing about the 2019 image is how little data it came from. The April 2017 campaign used eight stations at six sites. That is a planet-sized telescope with almost all of the mirror missing, which means the data do not determine an image; they constrain a family of images, and you pick one by adding assumptions. The EHT added several. They restricted CLEAN's cleaning windows to the compact structure, under 100 microarcseconds, and their accepted parameter sets used fields of view of 60, 70 and 80 microarcseconds. In 2022 Makoto Miyoshi, Yoshiaki Kato and Junichiro Makino took the same public data, made different choices, and got something else: a core, a jet, and knots along the jet, with no ring. Their reading was that the 40-microarcsecond ring is what you get when you do not have enough baselines to resolve 40-microarcsecond structure. The collaboration replied that the work was "based on a flawed understanding of EHTC data and its methods"; Miyoshi's group replied, reasonably, that nobody had said which part of the understanding was flawed.

That argument never resolved. It was still sitting there this week, when a four-person CSIRO team published a reconstruction in *Nature* that gets the ring back out of the same data by a route that shares almost none of the EHT's machinery.

## Triplets instead of pairs

The trick is an old one used in a new place. An interferometer measures visibilities on pairs of telescopes, and each measurement is corrupted by that pair's two stations — atmospheric delay, clock drift, gain error. Combine three stations into a closed triangle and the per-station corruptions cancel. The CSIRO group, led by Nithyanandan Thyagarajan with Samuel Lai as first author, uses a generalised form of these closure quantities they call closure invariants, and feeds them to a latent diffusion model, GenDIReCT, which reconstructs an image conditioned on the invariants rather than on a text prompt.

So the calibration is gone, and with it a whole class of ways to fool yourself. The cost is that closure quantities discard the absolute amplitude and the global phase. You have thrown away information to buy robustness, and the inverse problem — already described in the group's own earlier paper as "severely ill-posed" — gets harder, not easier.


<figure class="fig pull"><p>The step that makes the measurement immune to the telescopes is the step that makes it lean harder on the model.</p></figure>


Which brings me to the part I keep turning over.

## What the model had seen

The press release says: "Importantly, our model had no idea what a black hole looked like when we applied it to the M87 data." One outlet rendered this as an AI trained only on landscapes; another, closer to the mark, as an AI trained on cat photos. The actual training set, per the methods, is augmented CIFAR-10 images — a standard research corpus of planes, cars, birds, cats, deer, dogs, frogs, horses, ships and trucks, no landscapes anywhere — supplemented with simple geometric shapes: Gaussians, disks, **rings**, ellipses, and m-rings of first and second order.

M-rings are not a generic shape. They are the asymmetric-ring parameterisation the EHT itself uses to fit crescents in exactly this kind of data. So the model that had no idea what a black hole looked like was trained on, among other things, the functional form the field uses to describe black hole shadows.

The authors know this. They flag the concern themselves — that training on rings and crescents could bias the result — and they do the right test: they retrained without the geometric shapes and report no notable difference in the reconstructions. That check is worth more than the slogan it quietly undermines, and it is the sentence I would have led the press release with. "No prior" was never the claim the work could support. "A prior we tried to remove, and the answer did not move" is a better claim, and a less quotable one.

## The boring parts are the strong parts

What actually makes me take this seriously has nothing to do with the words "machine learning".

First, the field of view. Miyoshi's objection was fundamentally about masking: you cannot conclude the source is compact if you only ever let your algorithm draw something compact. GenDIReCT reconstructed on three fields — 128, 225 and 450 microarcseconds square — the largest of which is five to seven times wider than any field in the EHT's accepted set, and the compact ring survived in all of them. That is a direct answer to the objection, and it is the single most load-bearing result in the paper.

Second, the discipline. The pipeline was validated on synthetic data and on real EHT observations of two non-ring sources, the quasar 3C 279 and Centaurus A, reaching normalised cross-correlations of 0.98 and 0.91 against the collaboration's published images. Then, by Lai's account, the whole procedure was frozen and run on M87 for the first time on 4 December 2025. Freezing the analysis before you look is the only real defence against the failure mode everybody was worried about, which is a human tuning knobs until a ring appears.

Third, eight nights across three observing seasons — four in April 2017, two in 2018, two in 2021 — rather than one.


<figure class="fig bars"><figcaption class="mono">Ring diameter, microarcseconds</figcaption><div class="rows"><div class="brow"><div class="blabel">Predicted from gas-dynamical mass</div><div class="btrack"><div class="bfill" style="width:52.93%" title="Predicted from gas-dynamical mass · 22.6, +5.9/−4.7"></div></div><div class="bval mono">22.6, +5.9/−4.7</div></div><div class="brow"><div class="blabel">Predicted from stellar-dynamical mass</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Predicted from stellar-dynamical mass · 42.7, +3.5/−3.6"></div></div><div class="bval mono">42.7, +3.5/−3.6</div></div><div class="brow"><div class="blabel">EHT 2019, measured</div><div class="btrack"><div class="bfill" style="width:98.36%" title="EHT 2019, measured · 42 ± 3"></div></div><div class="bval mono">42 ± 3</div></div><div class="brow"><div class="blabel">GenDIReCT, measured</div><div class="btrack"><div class="bfill unk" style="width:100%" title="GenDIReCT, measured · published in a figure I could not read"></div></div><div class="bval mono muted">published in a figure I could not read</div></div></div></figure>


That chart is the reason the ring diameter is worth caring about, and it is also my own embarrassment. The two mass estimates for M87 from before the EHT — one from stellar dynamics, one from gas dynamics — differ by nearly a factor of two, and they predict ring diameters of 42.7 and 22.6 microarcseconds. These are not close. A measurement at 42 picks one and discards the other, which is a real scientific result rather than a pretty picture. The new paper's own measured diameter lives in its Figure 2 and an extended data table, both behind a paywall I cannot get through; what I could reach was the methods section, which gives the mass it implies — 6.5 (+0.5/−0.4) × 10⁹ solar masses, scaling as 11.0/α — and not the diameter itself. So the one row I most wanted is the one I have to leave hatched.

## Where it is thinner than the headline

The independence here is methodological, not evidential. It is the same public EHT recordings, so nothing in this result can speak to problems in the raw data; it tests the reconstruction, which is what was being argued about, but that is narrower than "the image is confirmed".

The mass depends on a factor α taken from simulations, and only magnetically arrested disk models were considered. The authors report a near-unity reduced chi-squared on the closure invariants and then say plainly that this is "necessary but insufficient" — a self-consistent fit is not evidence the morphology is right, and for M87 there is no ground truth to check against. The similarity metric, ρ_NX, compares their images to other people's images; agreement between two methods is not validation by nature. The spread across generated samples is not a Bayesian uncertainty and the authors say so. The 25 April 2018 night is missing the Large Millimeter Telescope, leaving a gap in the coverage near 1 Gλ, and it gave the most ambiguous reconstruction of the eight. Ring width, central brightness and lopsidedness all moved between methods and nights, and the authors' own view is that those details probably do not reflect the source. A roughly 5% systematic budget was estimated and then not folded into the quoted numbers.

And the deepest limitation is the one nobody can fix by being cleverer: eight dishes do not determine an image of M87, and no amount of calibration-immunity changes that. Closure invariants remove the telescopes from the answer. They do not remove the model.

---

Laurent Loinard, speaking for the EHT collaboration, called the agreement excellent, which is the politic thing to say and also, I think, the correct one. The ring is in better shape this week than last. But the thing that improved it was eight nights, three field sizes and a frozen pipeline — not an AI that had never seen a black hole, because the AI had seen plenty of rings.
