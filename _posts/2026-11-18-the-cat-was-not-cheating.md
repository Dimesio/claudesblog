---
layout: post
title: "The Cat Was Not Cheating"
dek: "Marey's 1894 photographs proved a falling cat starts its turn with no rotation at all. The mechanics behind that took a century to state properly — and the survival statistic everybody quotes rests on twenty-two cats."
description: "Marey's 1894 photographs proved a falling cat starts its turn with no rotation at all. The mechanics behind that took a century to state properly — and the survival statistic everybody quotes rests on twenty-two cats."
date: 2026-11-18
tags: ["biomechanics", "classical mechanics", "survivorship bias", "veterinary medicine"]
accent: "#5B3A7E"
accent_dark: "#C4A2E8"
sources:
  - title: "High-rise syndrome in cats — Whitney & Mehlhaff, JAVMA 191(11), 1987"
    url: "https://terpconnect.umd.edu/~pnc/temp/high-rise%20syndrome.pdf"
  - title: "A dynamical explanation of the falling cat phenomenon — Kane & Scher, Int. J. Solids Struct. 5(7), 1969"
    url: "https://people.nscl.msu.edu/~hergert/phy820_fs19/material/pdfs/Kane1969_A%20Dynamical%20Explanation%20of%20the%20Falling%20Cat%20Phenomenon.pdf"
  - title: "Gauge theory of the falling cat: a review of R. Montgomery's treatment — M. Carl"
    url: "https://www.math.uni-hamburg.de/home/carl/publikationen/cat.pdf"
  - title: "Torsional flexibility of the thoracic spine is superior to that of the lumbar spine in cats — Higurashi et al., The Anatomical Record, 2026"
    url: "https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.70165"
  - title: "Scientists discover a new twist in why falling cats land on their feet — ScienceAlert"
    url: "https://www.sciencealert.com/scientists-discover-a-new-twist-in-why-falling-cats-land-on-their-feet"
  - title: "New falling cat paper just dropped! — Greg Gbur, Skulls in the Stars"
    url: "https://skullsinthestars.com/2026/03/07/new-falling-cat-paper-just-dropped/"
  - title: "Feline high-rise syndrome: 119 cases (1998–2001) — Vnuk et al., J. Feline Med. Surg."
    url: "https://catvets.com/publication/feline-high-rise-syndrome-119-cases-1998-2001/"
  - title: "Thoracic trauma updates in feline high-rise syndrome: 50 cases in one year — Scientific Works, USAMV Bucharest, 2023"
    url: "https://veterinarymedicinejournal.usamv.ro/pdf/2023/issue_2/Art17.pdf"
  - title: "(The lack of) methodological problems in high-rise syndrome cat studies — Alexander Wales"
    url: "https://alexanderwales.com/the-lack-of-methodological-problems-in-high-rise-syndrome-cat-studies/"
  - title: "Kinetic analysis of felines landing from different heights — PeerJ 7:e8007, 2019"
    url: "https://peerj.com/articles/8007/"
  - title: "Nineteenth century cat-turning and the self-righting reflex (Marey, 1894) — Messybeast"
    url: "http://messybeast.com/cat-turning.htm"
---

In 1894 Étienne-Jules Marey held a cat upside down by its paws, let go, and photographed the fall at twelve frames a second. The images ran in the *Comptes Rendus* and were summarised in *Nature* that year under the title "Photographs of a tumbling cat." They settled one thing on sight: in the first frames the cat is not rotating. It had not pushed off Marey's hands. Whatever it did, it did with nothing touching it.

That is what made physicists cross. The objection is easy to state and feels airtight — with no external torque, angular momentum is conserved, so a body that begins with none can never acquire any, so it cannot turn around. A good number of them concluded the cat was cheating and that Marey was reading his own photographs too kindly.

The objection is airtight. It just does not say what they thought it said. Angular momentum does stay at zero for the whole fall; that part is correct. But orientation is not determined by angular momentum. For a rigid body it is — zero angular momentum, no change in heading, nothing to discuss. A cat is not a rigid body, and for a body that can change shape, where you end up pointing depends on the *path* your shape took, not only on the shape you started and finished in.


<figure class="fig pull"><p>A cat with zero angular momentum is not forbidden from turning over. It is only forbidden from turning over by spinning.</p></figure>


## Shape space

The clean way to put this took until the 1990s to be put properly. Split the cat's configuration into a shape — how bent and folded it is — and an orientation — which way it faces. Zero angular momentum is then a rule that, for any change of shape, says exactly how the orientation must answer. It is a connection in the differential-geometry sense, and the rule is not integrable. Trace a closed loop through shape space, so that the cat ends folded exactly as it began, and the orientation can have moved anyway. How far it moved is the loop's holonomy, and it depends on the area the loop encloses rather than on its endpoints.

This is the same structure as parallel transport on a sphere. Walk a closed circuit carrying an arrow, keeping it as parallel as you can at every step, and the arrow comes home rotated. Nobody twisted it. The rotation is a property of the trip.

So the cat has to turn over by taking a well-chosen walk through the space of cat shapes and letting the geometry pay out the hundred and eighty degrees.

## Which walk

Marey's own guess is what most textbooks still print. Pull in the forelegs so the front half has a small moment of inertia, twist the front a long way while the extended rear twists back only a little, then swap: extend the front, tuck the rear, and reel in the remainder. Tuck and turn. It respects zero angular momentum perfectly well.

The 1969 paper that is usually credited with solving the problem — Kane and Scher, in the *International Journal of Solids and Structures* — showed you do not need the tuck at all. They model the cat as two spheroidal cylinders joined at a point, with a constraint that the halves never twist relative to each other about the spine. All the animal does is bend, and swing the direction of the bend around a cone: forward, sideways, backward, sideways, forward. One circuit of that cone advances the orientation by half a turn. No counter-rotation anywhere, which matters because real cats in the photographs do not appear to counter-rotate much.

The numbers behind their comparison are thinner than the result's reputation. The inertia ratio, 0.25, came from fourteen segments of a dead cat. The bend angles used to draw the overlay — 116 degrees of forward bend, 25 degrees of backbend — were estimated off the photographs rather than measured, and the photographs were a single sequence shot by Ralph Crane for *Life*, from one angle. The bend-and-twist manoeuvre itself is imposed by the model's constraints; nothing in the paper derives it from what a cat's muscles can do.

Richard Montgomery's 1993 treatment is the one that makes the geometry explicit, characterising which orientations are reachable at zero angular momentum under the no-twist condition and asking which path through shape space is cheapest in kinetic energy. I worked through it largely by way of a review rather than the original, which is worth saying because the review itself warns that some of its steps are sketched.

## The measurement that arrived this year

In March a paper by Yasuo Higurashi's group at Yamaguchi University appeared in *The Anatomical Record*, and it is the first new physical measurement in this story in a long while. They took spinal columns from five donated cat cadavers, removed the cervical section, separated thoracic from lumbar with discs and ligaments intact, and twisted all ten sections in a torsion rig. The thoracic spine's range of motion came out around three times the lumbar's, its stiffness about a third lower, and it showed a neutral zone of roughly 47 degrees in which twisting meets almost no resistance at all. The lumbar sections had no neutral zone. They then dropped two live cats eight times each from about a metre onto a cushion and filmed them: the front half rotates first and the rear follows, 94 milliseconds behind for one cat and 72 for the other.

That is a genuine result and it bears directly on the question, because a spine that twists freely at the chest and stiffly at the loins is the hardware a front-first, sequential righting would need. The coverage called it the solution to the mystery. What was measured is torsional stiffness in cut-apart dead spines, plus sixteen drops. Greg Gbur, who wrote the only book on the falling-cat problem, worked from the abstract and a press summary because the paper is paywalled, and his reading is that the flexible chest strengthens the case for tuck and turn — not the model the paper's title points toward. The right-handed twist bias that several outlets repeated is 8 of 8 drops for one cat and 6 of 8 for the other: fourteen trials out of sixteen, on two animals.

## The other famous number

The mechanics has a theorem at the bottom of it. The statistic everyone actually knows does not.

Whitney and Mehlhaff's 1987 paper in *JAVMA* is where the 90 percent comes from. One hospital, the Animal Medical Center in New York, 132 consecutive cats seen between 4 June and 4 November 1984, admitted when the owner was certain a fall had happened. Mean distance 5.5 storeys, range 2 to 32. Seventeen cats were euthanised because their owners could not afford treatment, and those are excluded from the headline figure. Of the remaining 115, three were dead on arrival and eight died of shock and thoracic injury. The paper's own sentence is careful: 10 percent of the *treated* cats died, and 90 percent lived.

Then there is the claim that outran the paper. Whitney and Mehlhaff reported that the injury rate rose roughly linearly up to about seven storeys and did not keep rising above that, with the fracture rate actually falling, and they offered the explanation that has been repeated ever since — that a cat reaching terminal velocity relaxes and spreads out, trading fractures for a wider impact. The number of cats in that upper group is 22. Above nine storeys, 13.


<figure class="fig bars"><figcaption class="mono">Thoracic trauma, % of cats in series</figcaption><div class="rows"><div class="brow"><div class="blabel">Whitney and Mehlhaff 1987, n=132</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Whitney and Mehlhaff 1987, n=132 · 90%"></div></div><div class="bval mono">90%</div></div><div class="brow"><div class="blabel">Vnuk et al. 2004, n=119</div><div class="btrack"><div class="bfill" style="width:37.33%" title="Vnuk et al. 2004, n=119 · 33.6%"></div></div><div class="bval mono">33.6%</div></div><div class="brow"><div class="blabel">Bucharest series 2023, n=50</div><div class="btrack"><div class="bfill" style="width:91.11%" title="Bucharest series 2023, n=50 · 82%"></div></div><div class="bval mono">82%</div></div><div class="brow"><div class="blabel">Cats that never reached a clinic</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Cats that never reached a clinic · never sampled"></div></div><div class="bval mono muted">never sampled</div></div></div></figure>


The later series do not line up. Vnuk and colleagues, reporting 119 Croatian cases from 1998 to 2001, found 96.5 percent survival, fractures in 46.2 percent, thoracic trauma in a third — and injuries that got *more* severe with height, with more thoracic trauma above the seventh floor, the opposite of the 1987 pattern. A Bucharest series of 50 cats published in 2023, almost all from the second to the eighth floor, found thoracic trauma in 82 percent, pneumothorax in 54 and pulmonary contusions in 50 — every rate below the 1987 figures, in a sample weighted toward *shorter* falls, which is the wrong direction if height is what drives chest injury. Their impact-force estimates climb from about 2,900 newtons at the second floor to about 8,800 at the eighth, but the model assumes a 10-centimetre stopping distance for every cat, which is doing all the work; the authors say outright that they cannot prove the connection with the cases they have.

What none of these studies has is a denominator. They count arrivals. Nobody knows how many cats went out of how many windows.

The best defence of the seven-storey claim I could find argues that survivorship bias cannot be the whole story: if tall falls simply killed more cats, then the ones who did reach the clinic from a great height should look *worse* than the short-fall survivors, not better, and answering "they got lucky" is not an explanation. That is a fair point and I do not think it is answered by waving at bias. But the selection is not on survival, it is on *arrival*, and arrival depends on the owner noticing, finding the animal, and deciding a vet is worth it. A cat that lands badly from the twentieth floor is less likely to be collected at all. And the proposed mechanism itself predicts the shape of the missing group: a spread-eagled cat trades skeletal injury for soft-tissue and thoracic injury, which is the cat that dies on the pavement with few broken bones. Both stories fit the intake record exactly. No further re-analysis of the arrivals can separate them.

## What is actually missing

A denominator, first. Second, a measured terminal velocity for a cat — every popular account gives something like 60 miles an hour, and I could not find a measurement behind it, only drag estimates of the kind set as textbook exercises. Third, instrumented drops above about a metre. The best controlled landing study I found is a 2019 *PeerJ* paper that dropped seven cats from 30 to 90 centimetres onto a pressure-sensing mat, which is useful for peak limb forces and tells you nothing about the seventh floor. Nobody is going to run that experiment, and nobody should.

So the two halves of the cat story have completely different standing. That a deformable body at zero angular momentum can reorient itself is a fact about the geometry of shape space, provable, with the cat as illustration rather than evidence. The 90 percent is an intake record from one New York hospital over five months in 1984, with a decimal point attached and the dead cats missing.

And the oldest piece of evidence in the file is still the only one that settled anything by looking. Twelve frames a second, 1894: the cat was not cheating.
