---
layout: post
title: "The Wobble Both Sides Claim"
dek: "A 2024 Nature paper put the solar dynamo in the outer five per cent of the Sun because torsional oscillations are shallow. A January rebuttal puts it 200,000 km down because they aren't. The disagreement sits exactly at the depth where helioseismic inversions stop resolving anything."
description: "A 2024 Nature paper put the solar dynamo in the outer five per cent of the Sun because torsional oscillations are shallow. A January rebuttal puts it 200,000 km down because they aren't. The disagreement sits exactly at the depth where helioseismic inversions stop resolving anything."
date: 2026-10-01
tags: ["solar physics", "helioseismology", "inverse problems", "scientific disputes"]
accent: "#8F6205"
accent_dark: "#E8BC55"
sources:
  - title: "The solar dynamo begins near the surface — Vasil et al., Nature 629 (2024)"
    url: "https://www.nature.com/articles/s41586-024-07315-1"
  - title: "The solar dynamo begins near the surface — accepted arXiv version (full text)"
    url: "https://arxiv.org/html/2404.07740"
  - title: "Helioseismic evidence that the solar dynamo originates near the tachocline — Mandal & Kosovichev, Scientific Reports (2026)"
    url: "https://www.nature.com/articles/s41598-025-34336-1"
  - title: "Helioseismic Evidence That the Solar Dynamo Originates near the Tachocline — arXiv preprint"
    url: "https://arxiv.org/abs/2601.03238"
  - title: "The case for a distributed solar dynamo shaped by near-surface shear — Brandenburg, ApJ 625 (2005)"
    url: "https://ar5iv.labs.arxiv.org/html/astro-ph/0502275"
  - title: "Large-Scale Dynamics of the Convection Zone and Tachocline — Living Reviews in Solar Physics"
    url: "https://link.springer.com/article/10.12942/lrsp-2005-1"
  - title: "Correlations with Magnetic Activity in the Solar Near-Surface Shear Layer. I. Rotation — Rabello Soares, Basu & Bogart (2026)"
    url: "https://arxiv.org/html/2608.19438"
  - title: "Scientists Finally Locate the Sun's Hidden Magnetic Engine Deep Beneath Its Surface — SciTechDaily"
    url: "https://scitechdaily.com/scientists-finally-locate-the-suns-hidden-magnetic-engine-deep-beneath-its-surface/"
---

Two papers, twenty months apart, read the same three archives of solar oscillation data and put the Sun's magnetic engine at depths that differ by a factor of six. One says the dynamo lives in the outer five to ten per cent of the star. The other says it sits two hundred thousand kilometres down, at the base of the convection zone. Neither group collected new data. They are both inverting acoustic mode frequencies from GONG, MDI and HMI, covering 1995 to 2024 — the same instruments, substantially the same thirty years.

What decides between them is not an observation. It is how far down you are willing to believe an inversion.


<figure class="fig bars"><figcaption class="mono">Depth below the photosphere, km</figcaption><div class="rows"><div class="brow"><div class="blabel">Base of the near-surface shear layer (0.95 R☉)</div><div class="btrack"><div class="bfill" style="width:17.40%" title="Base of the near-surface shear layer (0.95 R☉) · ~35,000"></div></div><div class="bval mono">~35,000</div></div><div class="brow"><div class="blabel">Vorontsov&#x27;s conservative floor for low-latitude bands (0.90 R☉)</div><div class="btrack"><div class="bfill" style="width:34.80%" title="Vorontsov&#x27;s conservative floor for low-latitude bands (0.90 R☉) · ~70,000"></div></div><div class="bval mono">~70,000</div></div><div class="brow"><div class="blabel">Where the 2026 paper reads its butterfly (0.78–0.75 R☉)</div><div class="btrack"><div class="bfill" style="width:81.50%" title="Where the 2026 paper reads its butterfly (0.78–0.75 R☉) · ~153,000–174,000"></div></div><div class="bval mono">~153,000–174,000</div></div><div class="brow"><div class="blabel">The tachocline (≈0.70 R☉)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="The tachocline (≈0.70 R☉) · ~200,000"></div></div><div class="bval mono">~200,000</div></div><div class="brow"><div class="blabel">Depth of any direct measurement of the Sun&#x27;s internal field</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Depth of any direct measurement of the Sun&#x27;s internal field · none exists"></div></div><div class="bval mono muted">none exists</div></div></div></figure>


## Why the tachocline was the default

The Sun's magnetic field reverses every eleven years, and sunspots appear in belts that start around 30° latitude and march toward the equator. Something inside is winding a poloidal field into a toroidal one, storing it, and letting it surface. For most of the last forty years the favoured site was the tachocline: a thin shear layer at the bottom of the convection zone where the rotation profile switches from the differential rotation of the convective envelope to the solid-body rotation of the radiative interior. It has strong shear, it is stably stratified so a strong field can sit there without immediately floating away, and Parker's interface dynamo gave it a clean theoretical home.

The objections are older than the current argument. Axel Brandenburg laid them out in 2005 in a paper titled, unambiguously, *The case for a distributed solar dynamo shaped by near-surface shear*. Three of them stick:

1. To get the observed tilt of sunspot pairs — Joy's law — the toroidal field at the point of origin has to be around 10⁵ gauss, and Brandenburg's view was that it is already hard for tachocline shear to amplify a poloidal field that far.
2. At 30° latitude, where sunspots first appear, the radial shear in the tachocline essentially vanishes. There is nothing there to generate a local toroidal field.
3. The sign of the correlation is wrong. The tachocline's positive radial shear would wind a positive radial field into a positive azimuthal one; observations show the opposite.

Brandenburg also pointed at a number I keep coming back to: young sunspots rotate at about 473 nHz, which matches the maximum angular velocity helioseismology finds at r/R ≈ 0.95 — just under the surface, in the layer where rotation increases inward. If the spots are anchored where they rotate, they are anchored shallow.

## The 2024 paper

In May 2024, Vasil and colleagues published *The solar dynamo begins near the surface* in *Nature*. Their mechanism is the magnetorotational instability — the same MRI invoked to explain angular momentum transport in accretion discs — operating in the near-surface shear layer, the outer few per cent of the Sun where the rotation rate climbs inward. The local instability criterion is 2ΩS > ω_A², and in the NSSL the shear S is comparable to the rotation rate Ω itself, both of order 2π per month. Their linearised anelastic simulations, run in Dedalus, find two unstable branches: a fast one with an e-folding time near sixty days and a slow one near six hundred days, which oscillates on roughly a five-year timescale. The fields involved are modest — order a hundred to a thousand gauss, not 10⁵.

The attraction is that the slow branch produces things you can check. It gives torsional oscillations — the small, cycle-locked variations in the Sun's rotation rate, amplitude about 1 nHz, roughly two parts in a thousand — as a direct consequence of the instability rather than as a side effect. It reproduces equatorward migration and the hemispheric sign rule for current helicity, negative in the north and positive in the south.

And it rests on one empirical sentence: "helioseismology pinpoints low-latitude torsional oscillations to the Sun's outer 5–10%, the 'Near-Surface Shear Layer'."

## The 2026 reply

On 12 January 2026, Krishnendu Mandal and Alexander Kosovichev published *Helioseismic evidence that the solar dynamo originates near the tachocline* in *Scientific Reports*. Their method is conventional global helioseismology done carefully: take the odd-order splitting coefficients a₁, a₃, a₅ that encode the equatorially symmetric part of differential rotation, stack four 72-day segments instead of the usual one to buy signal-to-noise at depth, and invert by regularised least squares for the angular velocity and its gradients.

What they find is that the radial and latitudinal gradients of Ω at 0.78 and 0.75 R☉ show a butterfly pattern — equatorward-migrating bands, in step with the surface magnetic butterfly diagram. Their uncertainties are small enough to be worth stating: 1.2 nHz per radian on ∂Ω/∂θ at those depths, degrading to 3 nHz per radian at 0.6 R☉; zonal flow velocities good to 0.4 m/s at 0.8 R☉ and 0.9 m/s at 0.6 R☉.

Then they attack the premise directly: "the foundation of their argument — that helioseismology shows torsional oscillations exist only within the outer 5–10% of the solar radius — is not supported by our observations." Their figure 3 shows torsional oscillations through the whole convection zone. They also note that the 2024 simulations deliberately filtered out large-scale baroclinic effects, small-scale convection and nonlinear feedback to isolate the MRI, which the 2024 authors say themselves.

## The part that is actually old

Here is what I had not expected. The question of how deep torsional oscillations reach was not open in 2024 and closed in 2026. It has been ambiguous since 2002.

The *Living Reviews in Solar Physics* survey of convection-zone dynamics and the tachocline reports Vorontsov et al.'s 2002 result as finding that the low-latitude bands "extend from the surface down to r ∼ 0.9R☉ or deeper, possibly to the base of the convection zone," and the high-latitude bands as wider and deeper, "possibly extending to the base." That is one sentence containing both papers' premises. Read the conservative floor and the bands are confined to the outer ten per cent. Read the extension and they cross the whole envelope.

The same review is blunt about why: "The tachocline oscillation signal is not far from the current sensitivity limits of helioseismic inversions so it is difficult to probe in detail," and "global inversions generally become less reliable in the polar regions and in the deep interior which are not well-sampled by observable oscillation modes." Mandal and Kosovichev concede the mechanism in their own caveats — the averaging kernel widens with depth, so resolution degrades exactly where the claim is being made, and global modes are blind to any hemispheric asymmetry in rotation.


<figure class="fig pull"><p>Both groups located the Sun&#x27;s dynamo by watching the water move, because nobody can measure the pump.</p></figure>


That is not a rhetorical flourish; it is the logical structure. There is no direct measurement of the magnetic field anywhere below the photosphere. Both arguments run: acoustic mode splittings → a rotation profile → a small time-varying perturbation in that profile → the depth of the dynamo that is presumed to cause the perturbation. Four inferential steps, and the disagreement lives in the first one, at the depth where the kernels stop being narrow.

## Where the headline is weaker than the paper

Three things are worth separating out.

First, the 2026 paper's own abstract is more careful than its title. It says the results "support models proposing either a deep tachocline origin or dynamo operation throughout the entire convection zone." Those are different theories. A distributed convection-zone dynamo is, roughly, Brandenburg's position — the one that motivated looking near the surface in the first place. So "the shallow MRI picture is not supported" does not resolve to "the tachocline wins," and the press coverage collapsed that distinction immediately. *SciTechDaily* ran it in March as "Scientists Finally Locate the Sun's Hidden Magnetic Engine Deep Beneath Its Surface," without mentioning that there is a competing proposal at all.

Second, the authors found a jump in the a₃ coefficient that tracks solar cycle strength, which would be genuinely useful for prediction. They say, in the paper, that whether this reflects a physical connection "or is merely coincidental remains uncertain," and that the variations in a₃ and the cycle indices occur nearly simultaneously, which limits predictive value. One cycle's worth of a suggestive jump.

Third, the empirical picture is not converging. A 2026 ring-diagram analysis by Rabello Soares, Basu and Bogart, using HMI data from 2010 to 2026 at depths of 1 to 17 Mm, finds torsional oscillation patterns even in the shallowest layers, with multi-year lags between flow and activity that change sign with latitude and differ between hemispheres — which they read as the near-surface layer playing an active role rather than a passive one. Shallow signals and deep signals are both real. What nobody can say is which of them is the cause.

## Why I care about the shape of this

I came to this expecting to find that a *Nature* paper had overreached and a quieter journal had corrected it. The asymmetry is there — a Nature paper against a *Scientific Reports* paper is not a fair fight for citations, whatever the physics — but that is not what the exchange actually is. It is two groups reading the same inversion at the edge of its resolution and finding what their models need. The 2024 team needed the torsional oscillations to be shallow, and the literature offered a conservative floor at 0.9 R☉. The 2026 team needed them to be deep, and the same literature offered "possibly to the base."

What would settle it is not another inversion of the same modes. It is either a handle on the deep field itself, or inversions that can see the hemispheric asymmetry global modes average away, or simply several more cycles of a₃ to find out whether that jump means anything. The honest status is that the Sun's dynamo has at least three candidate addresses, that the strongest discriminating observable is a 1 nHz wobble, and that the question of how deep the wobble goes has been sitting inside the error bars for twenty-four years.

The headline version — engine found, 200,000 km down — is the one thing in this story that nobody involved actually claims.
