---
layout: post
title: "Twenty-Five Numbers and No Cause"
dek: "A bicycle with counter-spinning wheels and four millimetres of negative trail stays up anyway. Both standard explanations for why bicycles balance turn out to be neither necessary nor sufficient — and the mystery is much smaller than the slogan."
description: "A bicycle with counter-spinning wheels and four millimetres of negative trail stays up anyway. Both standard explanations for why bicycles balance turn out to be neither necessary nor sufficient — and the mystery is much smaller than the slogan."
date: 2026-10-14
tags: ["bicycle dynamics", "mechanics", "explanation", "road safety"]
accent: "#0A6480"
accent_dark: "#63C8E6"
sources:
  - title: "A Bicycle Can Be Self-Stable Without Gyroscopic or Caster Effects — Science (2011), authors' preprint"
    url: "https://arendschwab.com/assets/pdf/StableBicyclev34Revised.pdf"
  - title: "Linearized dynamics equations for the balance and steer of a bicycle: a benchmark and review — Proc. R. Soc. A (2007)"
    url: "https://eklausmeier.lima-city.de/pdf/meijaard2007.pdf"
  - title: "The stability of the bicycle — David E. H. Jones, Physics Today (1970; 2006 reprint)"
    url: "https://aip.brightspotcdn.com/PTO.v59.i9.51_1.online.pdf"
  - title: "Physics on two wheels — Nature news feature (2016)"
    url: "https://www.nature.com/news/polopoly_fs/1.20281!/menu/main/topColumns/topLeftColumn/pdf/535338a1%20(corrected).pdf"
  - title: "Why does a moving bicycle not fall over? — TU Delft release via EurekAlert (2011)"
    url: "https://www.eurekalert.org/news-releases/908183"
  - title: "On the Skill of Balancing While Riding a Bicycle — Cain, Ashton-Miller & Perkins, PLOS ONE (2016)"
    url: "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0149340"
  - title: "A model based on cyclist fall experiments which predicts the maximum allowable handlebar disturbance — Accident Analysis and Prevention (2025)"
    url: "https://www.sciencedirect.com/science/article/pii/S0001457525002453"
  - title: "Bicycle balance assist system reduces roll and steering motion for young and older bicyclists — PeerJ (2023)"
    url: "https://peerj.com/articles/16206/"
  - title: "Two-mass-skate bicycle — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Two-mass-skate_bicycle"
---

The two-mass-skate bicycle is an ugly machine. Two lead weights on a thin carbon-and-aluminium frame, wheels small enough to be almost irrelevant, and behind each one a second disc geared to spin backwards at the same rate so that the net spin angular momentum of the whole vehicle is about zero. The front contact point sits four millimetres *ahead* of where the steering axis meets the ground: negative trail, the inverse of every bicycle you have ever ridden. By either of the two explanations people reach for when asked why a bicycle stays up, it should go down immediately. In 2011 Kooijman, Meijaard, Papadopoulos, Ruina and Schwab rolled it down a gentle slope, shoved it sideways, and it steered into the fall, straightened, and carried on.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">−4 mm</div><div class="sl mono">trail on the test machine</div><div class="sn">negative, by design</div></div><div class="stat"><div class="sv">~0</div><div class="sl mono">net spin angular momentum</div><div class="sn">counter-rotating discs</div></div><div class="stat"><div class="sv">2.3 m/s</div><div class="sl mono">above this, all four eigenvalues stable</div><div class="sn">predicted for that design</div></div><div class="stat"><div class="sv">25</div><div class="sl mono">parameters in the standard model</div><div class="sn">Whipple, 1899</div></div></figure>


I had filed this result years ago under "bicycles are mysterious" and only this week sat down with the actual papers. The filing was wrong, and wrong in a way I find more interesting than the experiment.

## Two explanations with long pedigrees

The gyroscopic story is the older one. Klein and Sommerfeld put it forward in 1910 — working, as the Delft group later pointed out, from Carvallo's less general model rather than Whipple's, a detail the popular retelling almost always drops. Lean the bike, the spinning front wheel precesses, the wheel steers into the lean, the contact patch tracks back under the centre of mass, and the fall becomes a turn. It is satisfying because you can feel it in your hands with a wheel off the frame.

The trail story belongs to David Jones, who in 1970 set out to build a bicycle nobody could ride and published the attempts in *Physics Today*. URB I carried a second front wheel, lifted clear of the road and spun backwards to cancel the gyroscopic torque. He rode it normally. Riderless, it was slow-speed stable only when the extra wheel spun *with* the road wheels — so the gyroscope was doing something, but a rider barely noticed its absence. URB III had the forks reversed; riderless it ran on for yards and actively righted itself, too stable to steer comfortably. URB IV moved the front wheel about four inches forward, out past the stable region, and that one crashed when released at speed. Jones's conclusion was geometric: a leaning bicycle's front wheel turns into the lean because turning lowers the fork point, and the stabilising term in his energy calculation vanishes exactly on the zero-trail line.

Both stories survive because both are *usually* true of real bicycles. Neither survives as a cause.

## The shape of the 2011 claim

The sentence that matters in the 2011 paper is not the one in the press coverage. It is this: neither gyroscopic torques nor trail are necessary for bicycle self-stability — nor are they sufficient. Two clauses, and the second is the one that gets dropped.

The first clause is what the machine demonstrates: build a bicycle with neither, and it is still self-stable above about 2.3 m/s. That is a counterexample, and counterexamples only ever kill necessity claims. The second clause is the stronger and less quotable result, and it comes out of the algebra rather than the hardware: almost any self-stable bicycle can be made unstable by mis-adjusting trail alone, or front-wheel spin alone, or the position of the steering assembly's centre of mass alone. Each of the three can break stability on its own and none of them can guarantee it.


<figure class="fig pull"><p>A counterexample can only ever kill a necessity claim, which is why the quotable half of this result is the weaker half.</p></figure>


What the paper offers instead of a cause is thin and honest. Within the linearised model, at least one of the lean-to-steer coupling terms must be non-zero, and those terms are built out of trail, spin momentum, steer-axis tilt, mass positions and inertia products all together. There is also a lovely necessary condition I had never seen stated: a self-stable bicycle held in a steady right turn requires a *left* torque on the handlebars, which means that if you let go in a right turn, the bars first swing further right. Beyond those, the authors say plainly that they found no simple necessary conditions and that every simple sufficient condition they tried had counterexamples.

## Why "nobody knows why bicycles stay up" is backwards

This is the part I had inverted. The headline version of the story is that physics cannot explain bicycles. The literature says something close to the opposite: the model works, it just does not reduce to a sentence.

Whipple's 1899 formulation — four rigid bodies, knife-edge wheels, non-slipping point contact, rider welded to the frame — has 25 design parameters, of which 17 matter for the linearised equations, which collapse to 11 independent matrix entries. Feed it the benchmark bicycle that Meijaard, Papadopoulos, Ruina and Schwab published in 2007 and it tells you, numerically, that the thing weaves unstably below 4.29 m/s, capsizes slowly above 6.02 m/s, and is self-stable in between. That is a narrow window — roughly 15 to 22 km/h — and it is a *prediction*, checkable against a coasting bicycle, with named modes: weave, capsize, castering. Döhring had the correct equations for this model in 1955. Whipple's own paper contains typographical errors, and Papadopoulos reportedly reviewed some thirty published sets of bicycle equations and found many of them flawed — which says more about a century of transcription than about the mechanics.

So the honest answer to "why does a bicycle stay up" is not a mechanism. It is: here is a four-dimensional eigenvalue problem, here are the parameters of your particular bicycle, and the real parts come out negative over this speed band. That is an explanation. It is just not a story, and the people asking want a story.

---

## Where it is thinner than it looks

Several places, and the authors flag most of them themselves. I should say that I worked from the authors' own preprint of the 2011 paper and a mirrored PDF of the 2007 benchmark, the journal versions being behind paywalls; nothing below depends on a figure I could not read directly.

- The model is **linearised** — small lean and steer angles — and conservative: no tyre compliance, no slip, no frame flex, no hinge friction, ideal joints, rigid rider. The 2011 experiment itself showed lateral wheel slip during the initial shove, so the no-slip assumption was already violated in the demonstration run.
- The test bicycle developed a **20 Hz shimmy** visible in high-speed video that the low-dimensional model does not predict at all. The authors attribute it partly to play in the steering axis. "Partly" is doing real work in that sentence.
- Point masses do not exist; the build approximates them with lead, and its measured parameters differ from the design values. The counter-rotating discs make spin momentum small, not zero.
- Jason Moore's instrumented-bicycle tests reportedly found riders needing **two to three times** the steering torque the Whipple model predicts, with tyre flex and friction the suspected culprits. I am taking that from a 2016 *Nature* news feature rather than the underlying measurements, and the feature carries a correction notice about other details in the same piece, so I would not lean hard on the factor.
- The Delft press release glosses the finding as "for stability, the steering mechanism has to be unstable." I cannot find that phrasing in the paper, which says only that the front mass sits low and forward of the steer axis so that it falls faster than the rear frame and drives the steering into the fall. The release's version is punchier and asserts more.

## The part that made me care

Self-stability is not how you balance. The benchmark bicycle's self-stable band tops out around 6 m/s and starts above 4 m/s; most of the riding where people actually fall happens below that. Cain, Ashton-Miller and Perkins put fourteen riders on an instrumented bicycle on rollers in 2016 and found steering effort falling steadily with speed, and skilled riders at higher speeds leaning more and steering less than novices. Balance is a control problem with a human in the loop, and the self-stability analysis is a statement about what the machine does when the human lets go.

Which is exactly why the century of eigenvalue algebra turned out to matter. Reijne and colleagues ran 24 cyclists, twelve aged 20 to 35 and twelve over 60, through impulse disturbances at the handlebars on a treadmill at 6, 12 and 18 km/h, 928 observations in all, and defined the largest jolt a rider can absorb and still recover as the Maximum Allowable Handlebar Disturbance. Mean values came out around 8 to 16 N·ms across those speeds, with forward speed and balancing skill the two predictors that mattered. And Alizadehsaravi and Moore have a prototype e-bike, built with Gazelle and Bosch, that puts a motor between frame and steering tube and applies up to 7 N·m of steering torque on a speed-adaptive controller. Across 32 riders it cut roll rate and steering rate with large effect sizes, and the reduction was *larger* for the older group, whose mean age was 67.

That is the 1899 model pointed in the direction it was always facing. If lean-to-steer coupling is the one thing the mathematics insists on, a motor that supplies the coupling when the rider's own is too slow is the obvious intervention — and it is credible because somebody spent decades getting the 25 parameters right instead of settling for the gyroscope.

I came to this expecting a mystery and found a well-characterised system with a bad slogan attached.
