---
layout: post
title: "The Same Tenth of a Millimetre"
dek: "One set of papers reads the Antikythera mechanism's calendar ring as extraordinary precision; a 2025 preprint reads its gear teeth as errors bad enough to jam. Converted into the same units, both are the same wobble in one craftsman's hand."
description: "One set of papers reads the Antikythera mechanism's calendar ring as extraordinary precision; a 2025 preprint reads its gear teeth as errors bad enough to jam. Converted into the same units, both are the same wobble in one craftsman's hand."
date: 2026-10-07
tags: ["antikythera", "metrology", "inference", "archaeology"]
accent: "#0B5FB0"
accent_dark: "#8FBDF5"
sources:
  - title: "An improved calendar ring hole-count for the Antikythera mechanism — Woan & Bayley, arXiv:2403.00040"
    url: "https://arxiv.org/abs/2403.00040"
  - title: "Woan & Bayley, Horological Journal 2024(July), 282–287 — citation and abstract"
    url: "https://eprints.gla.ac.uk/329337"
  - title: "The Impact of Triangular-Toothed Gears on the Functionality of the Antikythera Mechanism — Szigety & Arenas, arXiv:2504.00327 (preprint)"
    url: "https://arxiv.org/abs/2504.00327"
  - title: "The Antikythera Mechanism: Evidence of a Lunar Calendar, Parts 1&2 — Budiselic et al., Horological Journal (British Horological Institute)"
    url: "https://bhi.co.uk/wp-content/uploads/2020/12/BHI-Antikythera-Mechanism-Evidence-of-a-Lunar-Calendar.pdf"
  - title: "An Initial Assessment of the Accuracy of the Gear Trains in the Antikythera Mechanism — Edmunds, J. Hist. Astron. 42(3), 307–320 (paywalled)"
    url: "https://doi.org/10.1177/002182861104200302"
  - title: "Edmunds (2011) repository record — Cardiff ORCA"
    url: "https://orca.cardiff.ac.uk/id/eprint/46026/"
  - title: "Gravitational wave researchers cast new light on Antikythera mechanism mystery — Phys.org / University of Glasgow"
    url: "https://phys.org/news/2024-06-gravitational-antikythera-mechanism-mystery.html"
  - title: "Antikythera Mechanism's intricate gears: simulations reveal potential jamming issues — Phys.org"
    url: "https://phys.org/news/2025-04-antikythera-mechanism-intricate-gears-simulations.html"
  - title: "Recent Study Sparks Debate on Functionality of the Antikythera Mechanism — Greek Reporter"
    url: "https://greekreporter.com/2025/04/24/antikythera-mechanism-toy/"
  - title: "Mysterious Antikythera Mechanism May Actually Be a Toy, Study Says — Popular Mechanics via Yahoo"
    url: "https://www.yahoo.com/news/mysterious-antikythera-mechanism-may-actually-120010380.html"
  - title: "Antikythera mechanism — Wikipedia (gear tooth pitch, after Freeth et al. 2006)"
    url: "https://en.wikipedia.org/wiki/Antikythera_mechanism"
---

Two claims were made about the same lump of corroded bronze, eighteen months apart.

In June 2024, two gravitational-wave astronomers at Glasgow announced that the holes hidden beneath the Antikythera mechanism's calendar ring had been laid out with an accuracy of 0.028 millimetres. The coverage went where you would expect: extraordinary precision, remarkable craftsmanship, the ancient Greeks were better machinists than we thought. In April 2025 a preprint out of Mar del Plata simulated the same device's gear train using the manufacturing errors that have actually been measured on its teeth, and found that it jammed in 90 per cent of runs. One headline that followed said the mechanism may have been a toy.

I went looking for the contradiction and did not find one. What I found instead is that nobody had converted the two sets of numbers into the same units, and that when you do, they describe one craftsman with one hand, working to about a tenth of a millimetre, in two places where a tenth of a millimetre means completely different things.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">0.028 mm</div><div class="sl mono">radial scatter of the ring&#x27;s holes</div><div class="sn">the figure that got quoted</div></div><div class="stat"><div class="sv">0.13 mm</div><div class="sl mono">scatter along the ring</div><div class="sn">same data, 4.6× larger</div></div><div class="stat"><div class="sv">1.365 mm</div><div class="sl mono">one calendar division</div><div class="sn">measured inter-hole distance</div></div><div class="stat"><div class="sv">4–8%</div><div class="sl mono">gear-tooth position error, of one pitch</div><div class="sn">Edmunds&#x27; range, ≈0.06–0.13 mm</div></div></figure>


## What the ring papers actually did

The calendar ring is the outer scale on the mechanism's front. For most of a century it was assumed to carry 365 divisions, the Egyptian civil year, because that is what a Hellenistic astronomical instrument ought to carry. Then in 2020 Chris Budiselić, Tony Freeth and colleagues put high-resolution X-ray CT through Fragment C and found something nobody had used properly before: a ring of small holes behind the scale, drilled to take the pins of whatever indexed it. Eighty-one of them survive, broken into sections by the fractures that run through the fragment; Woan and Bayley later used 79 of them, from the six sections holding more than a single hole. The largest unbroken run, 37 holes, covers about a tenth of the original circle.

They measured the surviving inter-hole distance at 1.365 mm and ran an equivalence test against the candidate rings. 354 holes — the lunar year — fit; 365 did not. But their interval was wide: 346.8 to 367.2 at 99 per cent, which is another way of saying that from a tenth of a circle you cannot pin a hole count down very far.

Graham Woan and Joseph Bayley's contribution, published in the July 2024 *Horological Journal*, was to notice that this is exactly the shape of problem a gravitational-wave group solves for a living. You have a few disjoint stretches of a periodic signal, each one displaced and rotated by an unknown amount, and you want the period. So they wrote the fragments' displacements and rotations in as nuisance parameters — three per section — put Gaussian priors on the per-hole position errors, split those errors into a radial and a tangential component on the assumption that the ring began as a precisely scribed circle, and sampled the posterior twice over with two different samplers.

Their answer, using all the data: **355.24 holes**, with a 68 per cent credible interval of about ±1.4. 360 strongly disfavoured, 365 not plausible.

### The number the press release picked

Two things got lost on the way to the press release. The first is that the 0.028 mm everyone repeated is the *radial* scatter — how far each hole sits in or out from the scribed circle. The quantity that carries the information, the scatter *along* the circle, came out at 0.129 mm, 4.6 times larger. It is still a small number. It is just not the small number that was quoted, and it is the one that constrains the hole count.

The second is in the abstract, in plain sight. Using all the data, the estimate is 355.24. Drop the holes adjacent to fractures — the ones whose measured positions are most likely to have been moved by the breaking — and it becomes **354.08**. So the clean lunar answer, the one the headlines ran with, is the one you get from the trimmed set; the full set puts 354 at the edge of the 68 per cent interval and 356 just as comfortably inside it. Which number you believe depends on how much you trust bronze at the edge of a crack, after two thousand years in seawater. The paper is open about this. The coverage, which said the ring was "vastly more likely" to have had 354 holes, was not.

## What the gear paper actually said

The 2025 preprint, by Esteban Szigety and Gustavo Arenas, is not the paper its headlines describe. It bolts together two existing models — Alan Thorndike's analytical treatment of the non-uniform motion you get from triangular teeth, and Mike Edmunds' 2011 model of manufacturing error — and simulates the pointers.

The triangular teeth turn out to be nearly free: the shape alone produces negligible pointer error. The errors are what bite. The authors set a failure criterion in terms of the gap between meshing wheels — jam below 10 per cent of nominal separation, disengage above 90 — and allow themselves a 1 per cent failure rate per gear pair. Simulated with Edmunds' error values at optimal separation, 90 per cent of runs jammed.

Their own conclusion is not that the mechanism was a toy. It is this: *either the mechanism never functioned or its actual errors were smaller than those reported by Edmunds* — and they lean hard on the second branch, pointing out that two millennia underwater deform bronze, that CT resolution may not resolve tooth tips and valleys cleanly, and that Edmunds had to work from partially destroyed wheels. Their final estimate is that the device worked somewhere between their best and second-best error cases. The abstract says outright that the inputs are speculative and the results must be read with caution. Somewhere between that and the aggregator headlines, a methodological critique of a fifteen-year-old error measurement turned into an obituary for the machine.

## Putting them in the same units

Here is the part I actually wanted. Edmunds expresses tooth error as a fraction of angular pitch — a standard deviation of 1° on a 60-tooth wheel is 1/6 = 0.16 — and his range is 0.04 to 0.08. The mechanism's teeth have an average circular pitch of about 1.6 mm. So his errors are roughly 0.06 to 0.13 mm of tangential slop in where a tooth flank sits.

The ring holes sit on a 1.365 mm pitch with about 0.13 mm of scatter along the circle.


<figure class="fig bars"><figcaption class="mono">Positional scatter, % of one division</figcaption><div class="rows"><div class="brow"><div class="blabel">Ring holes, radial</div><div class="btrack"><div class="bfill" style="width:22.11%" title="Ring holes, radial · 2.1% — 0.028 mm"></div></div><div class="bval mono">2.1% — 0.028 mm</div></div><div class="brow"><div class="blabel">Ring holes, along the circle</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Ring holes, along the circle · 9.5% — 0.13 mm"></div></div><div class="bval mono">9.5% — 0.13 mm</div></div><div class="brow"><div class="blabel">Ring holes, per hole if the scatter is independent</div><div class="btrack"><div class="bfill" style="width:70.53%" title="Ring holes, per hole if the scatter is independent · 6.7% — 0.09 mm"></div></div><div class="bval mono">6.7% — 0.09 mm</div></div><div class="brow"><div class="blabel">Gear teeth, Edmunds&#x27; low end</div><div class="btrack"><div class="bfill" style="width:42.11%" title="Gear teeth, Edmunds&#x27; low end · 4% — 0.06 mm"></div></div><div class="bval mono">4% — 0.06 mm</div></div><div class="brow"><div class="blabel">Gear teeth, Edmunds&#x27; high end</div><div class="btrack"><div class="bfill" style="width:84.21%" title="Gear teeth, Edmunds&#x27; high end · 8% — 0.13 mm"></div></div><div class="bval mono">8% — 0.13 mm</div></div><div class="brow"><div class="blabel">Gear teeth, Edmunds&#x27; per-gear measured values</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Gear teeth, Edmunds&#x27; per-gear measured values · paywalled, and not restated in the preprint"></div></div><div class="bval mono muted">paywalled, and not restated in the preprint</div></div></div></figure>


The two bodies of work are measuring the same hand. One of them was reported as evidence of extraordinary skill and the other as evidence the thing could not have run.

The difference is not precision, it is consequence. A tenth of a division on a calendar scale is invisible: the pin goes in the hole, the pointer sits a tenth of a day off true, nobody can read that off a bronze dial anyway, and the errors do not compound — each hole's wrongness is its own. A tenth of a pitch inside a train of thirty-odd meshing wheels is a different animal. Meshing is a clearance problem, not an averaging problem; you do not need the average tooth to be good, you need the *worst* tooth pair in the train to stay inside the gap, and the more wheels you chain the more chances you give the tail of the distribution. That asymmetry, not any disagreement about how good the maker was, is the whole story.

## Where this is thinner than I would like

Edmunds' 2011 paper is behind a paywall, so I have his error model second-hand, through how Szigety and Arenas describe and use it, and his conclusion — that the device was better suited to display or education than to practical prediction — through its repository record. I have not seen his per-gear numbers, which is why the most interesting bar in that chart is a question mark.

The comparison itself needs two caveats. Budiselić's 0.13 mm is the standard deviation of the distance *between* adjacent holes; Woan and Bayley's 0.129 mm is the scatter of each hole's own position. If hole errors are independent, those differ by a factor of √2, which is why I have given both readings in the chart — the ring is either slightly worse than Edmunds' worst gears or comfortably inside his range, depending on which convention you take. And some unknown part of all these figures is not the maker at all, but corrosion, deformation, and the limits of a CT scan.

Then there is the assumption of independence, which I think is the real open question. All three analyses treat positional errors as random and uncorrelated. But a ring of 354 holes was almost certainly indexed off something — a dividing plate, a stepped-off chord — and a marking method leaves *correlated* error: a systematic drift or a periodic wobble rather than white noise. The 2025 preprint does model a sinusoidal systematic term, 0° to 2°, separately. Correlated error with the same standard deviation is far more forgiving in a gear train than independent error, because neighbouring teeth are wrong together and the gap between two wheels changes slowly instead of jumping. Nobody has published the autocorrelation of the hole positions, as far as I can find, and the data to do it has been sitting in Budiselić's supplementary measurements since 2020.

The last thing I noticed is the simplest. The 2025 preprint does not cite either ring paper, and the ring papers do not discuss the gear-tooth error literature. The best available evidence about how precisely this object was made is split across two conversations that are not talking to each other, in units that do not match, with the louder claim in each one being the one that made a better headline.
