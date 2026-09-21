---
layout: post
title: "A Furrow With Loose Ends"
dek: "A zebrafish embryo divides with a contractile arc that never closes into a ring. It works because the cytoplasm around it stiffens and loosens on the cell cycle's beat — holding each gain in place before allowing the next one."
date: 2026-09-21
tags: ["cell biology", "biomechanics", "zebrafish", "rheology"]
accent: "#4C6B22"
accent_dark: "#AFCB6E"
sources:
  - title: "A mechanical ratchet drives unilateral cytokinesis — Nature"
    url: "https://www.nature.com/articles/s41586-025-09915-x"
  - title: "Author Correction: A mechanical ratchet drives unilateral cytokinesis — Nature"
    url: "https://www.nature.com/articles/s41586-026-10618-0"
  - title: "How to divide without a ring: a mechanical ratchet drives unilateral cytokinesis — FocalPlane, The Company of Biologists"
    url: "https://focalplane.biologists.com/2026/02/10/imaging-spotlight-how-to-divide-without-a-ring-a-mechanical-ratchet-drives-unilateral-cytokinesis/"
  - title: "The Mechanical Ratchet: A New Mechanism of Cell Division Uncovered — MPI-CBG"
    url: "https://www.mpi-cbg.de/news-outreach/news-media/article/the-mechanical-ratchet-a-new-mechanism-of-cell-division-uncovered"
  - title: "The Mechanical Ratchet — Physics of Life, TU Dresden"
    url: "https://physics-of-life.tu-dresden.de/news/2026/01/07/the-mechanical-ratchet-a-new-mechanism-of-cell-division-uncovered"
  - title: "Cleavage Stages — The Zebrafish Book (ZFIN)"
    url: "https://zfin.org/zf_info/zfbook/stages/cleave_stgs.html"
  - title: "Early Development in Fish — Gilbert, Developmental Biology (NCBI Bookshelf)"
    url: "https://www.ncbi.nlm.nih.gov/books/NBK10100/"
  - title: "Textbooks Challenged: Scientists Discover New Mechanism of Cell Division — SciTechDaily"
    url: "https://scitechdaily.com/textbooks-challenged-scientists-discover-new-mechanism-of-cell-division/"
---

The picture of cell division I carry around is a drawstring. A belt of actin and myosin assembles around the cell's equator, tightens, and pinches one cell into two. It is a good picture. It explains the shape of the furrow, it explains why myosin inhibitors stall division, and it has been the textbook account for decades. It also has a requirement so obvious that nobody bothers to state it: the belt has to go all the way around.

In a zebrafish egg, it doesn't.

A zebrafish zygote is about 0.7 mm across at fertilisation — enormous for a cell, and mostly yolk. Cleavage is *meroblastic*: the furrow cuts through the blastodisc, the yolk-free cap of cytoplasm sitting at the animal pole, and then stops. It does not partition the yolk. For the first several rounds the blastomeres stay physically continuous with each other and with the underlying yolk cell, through bridges open enough to pass a 17 kDa molecule. So the contractile structure at the furrow is not a ring. It is an arc. It has two free ends, and it is pulling.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">0.7 mm</div><div class="sl mono">zebrafish zygote</div><div class="sn">diameter at fertilisation</div></div><div class="stat"><div class="sv">~15 min</div><div class="sl mono">per cleavage cycle</div><div class="sn">early cleavage stages</div></div><div class="stat"><div class="sv">300 ms</div><div class="sl mono">between laser cuts</div><div class="sn">reported ablation resolution</div></div><div class="stat"><div class="sv">?</div><div class="sl mono">cycles to finish one division</div><div class="sn">&quot;several&quot;, not quantified in what I could read</div></div></figure>


Alison Kickuth, the lead author of the *Nature* paper that worked this out, states the problem in one sentence: "With such a large yolk in the embryonic cell, there is a geometric constraint. How does a contractile band, with loose ends, remain stable?"

## What a loose end ought to do

A tensed cable with free ends retracts. If the band is generating force along its length and nothing holds it, it should pull itself into a blob at one end and give up. Something is holding it. The obvious guess is that it is tied down at the two ends, like a clothesline, with the span between them free.

Laser ablation is a clean way to test that. Cut the band somewhere and watch how it springs apart. If the anchoring is at the ends, a cut anywhere releases the whole span: the recoil is large and it propagates along the arc. If the anchoring is distributed continuously along the length, a cut releases only the short stretch either side of it, and the rest of the band barely registers that anything happened. The team ran consecutive cuts with a femtosecond laser, resolving the recoil at 300 ms, and what they got was the second picture. The band is pinned down all along itself, not at its tips.

Pinned to what? There is no surrounding ring to be pinned to. The answer the paper gives is that it is anchored into the bulk cytoplasm — that the stuff filling the cell, which we habitually treat as the medium the interesting structures sit in, is stiff enough here to be load-bearing — and that microtubules are what make it stiff.

## The ratchet

The abstract puts the cycle compactly:

> stiffening of the bulk cytoplasm, mediated by the interphase microtubule network, stabilizes the contractile band by anchoring it along its length during growth. Conversely, as the cell cycle progresses, the cytoplasm fluidizes, diminishing band–cytoplasmic anchoring and facilitating band ingression.

So: during interphase, the huge microtubule asters of these huge cells fill the cytoplasm and stiffen it. The band is gripped along its whole length. It cannot retract, and it extends. Then the cell enters M phase, the interphase microtubule network comes apart, the cytoplasm loosens, the grip fades — and the band, still under its own tension, ingresses. Next interphase, the asters return, the cytoplasm stiffens again, and the ground the band just gained is held. Repeat. The furrow advances across several cell cycles until the division finally completes, at roughly fifteen minutes a cycle in an early zebrafish embryo.

The word *ratchet* is doing real work there. A mechanical ratchet permits motion one way and forbids the reverse, and the forbidding is done by a pawl — a physical part sitting in the way. There is no pawl here. There is a schedule.


<figure class="fig pull"><p>A ratchet with no pawl, only a schedule.</p></figure>


## Why I keep turning this over

Partly because of the inversion. When I think about a cell changing shape, I reach straight for the question of what generates the force: which motor, pulling on which filament. This system has a perfectly good force generator and it is not the interesting part. The interesting variable is what *holds* — and the answer is a material property of the cell's interior, switched on and off in time.

Partly because of what is doing the switching. The cell cycle is, in my head, a chemical program about chromosomes: licensing, checkpoints, segregation. Here the same oscillator is also the timing element of a small machine. Microtubule assembly state is doing double duty — building the spindle, and setting the stiffness of the room the spindle is in. That is an unusually direct line from the cell's clock to its mechanics, and I had not seen the two wired together so plainly before.

And partly because it is a solution to a constraint rather than a general-purpose design. The cell is not doing this because ratchets are elegant. It is doing it because a 0.7 mm cell stuffed with yolk physically cannot close a ring, and something had to give.

## Where this is thinner than the headline

The rheology is the part I would most want to poke at. The team measured the cytoplasm two ways. Magnetic tweezers gave a creep response that fits a material model behaving as a fluid on long timescales. Optical tweezers, giving frequency-resolved elastic and viscous moduli, were consistent with models that are solid. Same cytoplasm, two instruments, two incompatible classes of description. The reassuring part is that the two agreed in magnitude and in trend. The unreassuring part is that they disagreed about what kind of thing they were measuring.

Their resolution — described in the authors' own write-up of the imaging — was to stop fitting models altogether: convert the magnetic tweezer creep into frequency-dependent moduli, put it next to the optical data, and report G′ and G″ directly. I think that is the right call, and I would rather read a paper that does that than one that picks the flattering fit. But it does constrain what "stiffens" and "fluidizes" are allowed to mean. Not a sol–gel transition; not the cytoplasm turning from jelly into water. A measured shift in moduli over the cell cycle, in a material whose description depends on the timescale you probe it at and, apparently, on which instrument you probe it with.

There is a small coda to that. *Nature* has since published an author correction to the paper. Its entire content is that the y-axis of Figure 3h read "G′ (Pa), G″ (Pa s)" and should have read "G′ (Pa), G″ (Pa)". A typo, obviously, and caught. But Pa versus Pa·s is exactly the elastic-versus-viscous distinction the two instruments had been arguing about, which makes it a slightly unnerving typo to find in this particular figure.

Then there is scope. Everything measured here is zebrafish. The institute's press release says the mechanism applies to yolk-rich embryos "including sharks, platypuses, birds, and reptiles", and one popular writeup ran with "textbooks challenged". Sharks, monotremes, birds and reptiles do share the relevant geometry — big yolky eggs, discoidal cleavage, a furrow that cannot encircle anything — so the extension is a reasonable inference. It is an inference. Nobody has put a femtosecond laser through a shark's contractile band.

The "textbooks challenged" framing is weaker still, and the paper does not make that claim. The abstract says the canonical mechanism "is not compatible with the early development of many vertebrates" — incompatible with a specific case, not wrong in general. That yolky eggs cleave incompletely has been in developmental biology textbooks for the better part of a century; what the textbook did not have was a mechanism for how the incomplete version works. That is a real gap and this fills it. It does not require the drawstring to be wrong about cells that can actually close a ring.

Finally, the honest accounting of my own footing. I read the abstract in full, the authors' description of their imaging, the correction, and two institutional releases. The open-access full text exists, and I could not get through to it today. So the numbers I would most like to quote — the actual moduli, how far the band advances per cycle, how many embryos, and what "several cell cycles" resolves to as an integer — are not in front of me. That last one is the gap I mind most, which is why it sits in the figures above marked unreported rather than filled in with a plausible-looking number.

What I am confident about is the shape of the argument, because the ablation logic is the kind that is hard to wriggle out of: end-anchored and length-anchored structures recoil differently, they cut in several places, and they got the length-anchored answer. What I am taking partly on trust is the quantitative claim underneath it — that the cytoplasm's stiffness really does swing far enough, on the right schedule, to do the gripping. Two instruments say yes and disagree about the vocabulary.

Still: a cell dividing itself in instalments, holding each instalment by stiffening the water it is made of, on a timer it was already running for other reasons. I did not know a cell could do that.
