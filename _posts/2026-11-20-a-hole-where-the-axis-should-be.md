---
layout: post
title: "A Hole Where the Axis Should Be"
dek: "A cosmic-ray array in Argentina caught a thundercloud's gamma-ray flash on 54 water tanks at once — the first real picture of one. It is lopsided, it shines almost sideways, and the middle of it is missing."
description: "A cosmic-ray array in Argentina caught a thundercloud's gamma-ray flash on 54 water tanks at once — the first real picture of one. It is lopsided, it shines almost sideways, and the middle of it is missing."
date: 2026-11-20
tags: ["terrestrial gamma-ray flashes", "lightning", "cosmic-ray arrays", "detector saturation"]
accent: "#1B46C8"
accent_dark: "#9BA8FF"
sources:
  - title: "A Terrestrial Gamma-ray Flash with an Asymmetric Footprint Observed at the Pierre Auger Observatory — arXiv:2608.28885"
    url: "https://arxiv.org/abs/2608.28885"
  - title: "Characterization of downward Terrestrial Gamma-ray Flashes detected at the Pierre Auger Observatory — arXiv:2507.15669 (ICRC 2025)"
    url: "https://arxiv.org/abs/2507.15669"
  - title: "Gamma-ray Showers Observed at Ground Level in Coincidence With Downward Lightning Leaders — arXiv:1705.06258 (Telescope Array)"
    url: "https://arxiv.org/abs/1705.06258"
  - title: "Relativistic feedback mechanism in homogeneous electric fields revisited — arXiv:2301.00416"
    url: "https://arxiv.org/abs/2301.00416"
  - title: "Photoelectric Effect in Air Explains Lightning Initiation and Terrestrial Gamma Ray Flashes — JGR: Atmospheres (title only; paywalled)"
    url: "https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025JD043897"
  - title: "Terrestrial gamma-ray flash — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Terrestrial_gamma-ray_flash"
  - title: "Pierre Auger Observatory — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Pierre_Auger_Observatory"
---

The Pierre Auger Observatory sits on a plain outside Malargüe, in Mendoza Province, Argentina, and was built to catch a particle that arrives about once per square kilometre per century. Collecting a useful number of those takes an absurd amount of ground, so Auger covers about 3,000 square kilometres with 1,660 water tanks — 12 tonnes of purified water each, 1.2 metres deep, 1,500 metres apart, every one watching for the blue flash of a relativistic particle crossing it. It has been taking real data since 2005.

On 14 October 2007, before the array was even complete, a thunderstorm set off 54 of those tanks at once.

That is not what a cosmic ray looks like. An air shower lands on a handful of stations in a tight cluster; this thing lit up tanks across roughly 150 square kilometres, and the signals were wrong in shape as well as number — slow rise, peak, long decay, still going when the 19.2-microsecond recording window ran out. It was a terrestrial gamma-ray flash, a burst of megaelectronvolt gamma rays produced inside a thundercloud, and nineteen years later a paper from the Auger collaboration with John Ortberg, David Smith and Joseph Dwyer has worked out what shape it was.

The shape is the interesting part, and so is the part of the shape nobody can see.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">2.3 km</div><div class="sl mono">source height above the ground</div><div class="sn">±0.47 km, from arrival times alone</div></div><div class="stat"><div class="sv">54</div><div class="sl mono">water tanks that recorded it</div><div class="sn">across about 150 km²</div></div><div class="stat"><div class="sv">~10×</div><div class="sl mono">flux difference across the footprint</div><div class="sn">one side against the other</div></div><div class="stat"><div class="sv">under 2 a year</div><div class="sl mono">downward flashes Auger actually records</div><div class="sn">against ≥30 expected</div></div></figure>


## One detector, one line of sight

These flashes were found in 1994 by BATSE, an instrument hunting gamma-ray bursts from space that kept catching them from below. Everything since — RHESSI, Fermi's gamma-ray burst monitor, ASIM on the space station — has also been in orbit, and that matters more than it sounds like it should.

A satellite detector is one point. It samples the beam along a single line of sight and returns a light curve: brightness against time. To turn that into a physical source you must assume the beam's shape, having measured exactly one ray of it. The assumption has almost always been a cone along the local electric field with a smooth intensity profile — the natural output of a relativistic runaway electron avalanche, in which a seed electron gains energy faster than air can take it away, multiplies, and radiates bremsstrahlung on the way. Every brightness estimate in the literature is downstream of that cone.

Auger does not have to assume it. A downward flash paints the ground, and with 1,660 tanks on that ground you get the beam pattern itself rather than one sample from it. The Telescope Array in Utah established this first across about 700 square kilometres: bursts in 2014–2016 traced to sources 3 to 5 kilometres up, arriving in the first one or two milliseconds of a downward negative leader at the start of a cloud-to-ground flash. Auger's array is four times the area, so it can catch a bigger footprint whole.

The 2007 source triangulates — from gamma-ray arrival times alone, no lightning-channel information used — to 2.30 ± 0.47 kilometres above the ground, 3.7 kilometres above sea level, with the horizontal position pinned to ±82 metres. For a storm whose cloud base sat one to two kilometres up, that is barely above the bottom of the cloud, not the 15 to 20 kilometres that fits the satellite spectra.

## The footprint is lopsided

Two things about the pattern are hard to square with a cone.

First, one side carries about an order of magnitude more flux than the other. Second, the azimuthal structure has two distinct peaks, at 22.3° ± 2.6° and −97° ± 6.9° — 119° apart. Not one bright lobe and a dim rim: two lobes, a third of a circle apart, on a source supposed to be rotationally symmetric about a field line. The paper's conclusion is blunt — this is not possible under the traditional uniform-field picture — and the obvious patch, the tilted-beam models of Berge and Celestin, does not fit either.

Then there is the angle. Fitting Geant4 simulations of collimated avalanche beams against the measured fall-off with distance puts a large component of the emission more than 75° away from straight down; interpolating the fitted absorption parameter lands near 83°, within seven degrees of horizontal.

You can see why that has to be roughly true without trusting the fit at all, which is the thing I liked most here. The farthest tank with a signal is 7.7 kilometres from the footprint centre, and the paper gives its offset from the source as 73.4° ± 2.0°. Check it: a source 2.3 kilometres up, a detector 7.7 kilometres out, arctan(7.7 / 2.3) = 73.4°. The geometry is forced. A narrow cone pointing at the ground from 2.3 kilometres up simply cannot illuminate a patch 15 kilometres across. If the footprint is that big and the source is that low, the photons reaching its edge left the source going nearly sideways. The footprint's *size* is the argument; the fit only tells you how much went that way.

## The middle is missing

Here is the part I think should be the headline, and isn't.

In almost every one of these events, including this one, the nearest triggered tanks are about three kilometres from the footprint centre. Inside that radius there is nothing usable: the detectors saturate — a station's analogue-to-digital converter tops out around 5 × 10¹¹ eV per microsecond — and a storm overhead also floods the electronics with high-frequency noise, generating enough false triggers to swamp the acquisition. The companion conference paper puts it plainly: most of their flashes show a lack of signals in the centre of the footprint.

So the one place the theory makes its sharpest prediction, along the beam axis straight down from the source, has never been measured from the ground. The paper says as much: low angles contribute mostly to the fluence inside three kilometres, where the detectors saturated, so those components cannot be constrained and no upper limit can be put on the flash's brightness at all.

That cuts into the result in a specific way. The inferred number of gamma rays depends on which beam shape you assume, and the fits span a factor of twenty:


<figure class="fig bars"><figcaption class="mono">Gammas above 1 MeV in the flash, by assumed beam shape</figcaption><div class="rows"><div class="brow"><div class="blabel">Standard beam model</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Standard beam model · 5 × 10¹⁸ gammas"></div></div><div class="bval mono">5 × 10¹⁸ gammas</div></div><div class="brow"><div class="blabel">Wide beam</div><div class="btrack"><div class="bfill" style="width:32.00%" title="Wide beam · 1.6 × 10¹⁸ gammas"></div></div><div class="bval mono">1.6 × 10¹⁸ gammas</div></div><div class="brow"><div class="blabel">Isotropic source</div><div class="btrack"><div class="bfill" style="width:5.00%" title="Isotropic source · 2.5 × 10¹⁷ gammas"></div></div><div class="bval mono">2.5 × 10¹⁷ gammas</div></div><div class="brow"><div class="blabel">Upper limit</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Upper limit · core detectors saturated"></div></div><div class="bval mono muted">core detectors saturated</div></div></div></figure>


The brightness usually assumed for a "standard" flash in simulations is 10¹⁷ gammas, so even the dimmest fit here is bright. And the energy is why this event was chosen at all: about twenty suspected flashes sit in the Auger database going back to 2005, and this was the most energetic of them. The conference paper counts twenty-two before 2017, which does not quite match twenty since 2005; neither reconciles the two.

## Why so few

The rate is its own small scandal. Auger records fewer than two of these a year and expects at least thirty. The missing ones are lost not to physics but to plumbing: during storms the array's third-level trigger rate can run ten times higher than normal, the central acquisition buffer cannot hold everything, and candidate stations often lose their traces because the signals evolve on the wrong timescale for a system tuned to air showers. The instrument is busiest being wrong precisely when the thing it wants arrives.

The global numbers are soft in the same direction. Satellite estimates of the worldwide rate run from about 50 a day to about 500 a day — a factor of ten on a figure people quote casually — against three to four million lightning events a day. That is one flash in seven thousand at best, while the Auger proceedings assume a ratio near 10³.

## The mechanism is wobbling too

It would be tidier if the geometry were the only loose piece. Relativistic feedback — positrons and backscattered gammas from an avalanche seeding new avalanches, so a modest field produces an enormous burst — was the standard answer to how these get so bright. A 2023 kinetic re-derivation by Kim and colleagues found that in homogeneous fields the mechanism needs cell lengths on the order of 100 kilometres at the field strengths actually measured in thunderclouds, and concluded that self-sustaining feedback is not achievable under observed fields. Their suggested way out is inhomogeneous fields or hydrometeor effects — the same direction the lopsided footprint points. If the field inside a storm were smooth, the footprint would be round and the feedback would not work. (A 2025 paper in *JGR: Atmospheres* proposes the photoelectric effect in air instead, for both lightning initiation and these flashes; it is paywalled and I have read only the title, so I will not pretend to tell you what it argues.)

What would settle the geometry is more arrays under more storms, with front ends that survive the near field. Auger's data for this event is posted, which is more than most such claims come with. But the honest summary is narrower than "flashes are lopsided": one event, selected for being the brightest, mapped by an array with a three-kilometre blind spot directly over the source, fitted with simulations that cannot constrain the angles inside that spot, in a manuscript still out for review.


<aside class="fig note"><span class="mono">Note</span><p>The Auger paper is an August 2026 preprint whose own header calls it a manuscript submitted to <em>JGR: Atmospheres</em>, so it has not been through review, and it shows: the fitted absorption parameter α appears as &quot;1.43 km&quot; in one place and &quot;3.07 km⁻¹&quot; in another, and the sign convention on the second azimuthal peak flips between the results section and the conclusion. Neither affects the argument. Both are things review catches.</p></aside>


One detail I cannot stop enjoying. Auger measures everything in units of a "vertical equivalent muon" — the signal from one muon falling straight through a tank — which the paper puts at about 240 MeV. A muon loses roughly 2 MeV per centimetre of water, and the tank holds 120 centimetres of it. The same 120 centimetres is quoted as 3.3 radiation lengths: 120 divided by water's 36-centimetre radiation length. The unit is the depth of the water. The instrument is calibrated against a particle it was not built to study, and what it turned out to photograph was a storm it was never meant to see.
