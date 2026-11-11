---
layout: post
title: "Seventeen Is Not the Problem"
dek: "Every colour space you have ever used resolves to the eyes of seventeen people in 1920s London. The sample size turns out to be the most defensible thing about it."
description: "Every colour space you have ever used resolves to the eyes of seventeen people in 1920s London. The sample size turns out to be the most defensible thing about it."
date: 2026-11-11
tags: ["colorimetry", "metrology", "standards", "vision science"]
accent: "#B9121B"
accent_dark: "#FF9A90"
sources:
  - title: "ISO/CIE 11664-1:2019, Colorimetry - Part 1: CIE standard colorimetric observers (sample)"
    url: "https://cdn.standards.iteh.ai/samples/74164/75588be4062b4baabb6854ab0c6461b2/ISO-CIE-11664-1-2019.pdf"
  - title: "How the CIE 1931 Color-Matching Functions Were Derived from Wright-Guild Data - Fairman, Brill & Hemmendinger, with Brill's 1998 erratum"
    url: "https://silo.tips/download/how-the-cie-1931-color-matching-functions-were-derived-from-wright-guild-data"
  - title: "Evaluating the 1931 CIE Color Matching Functions - Mark Q. Shaw, RIT Munsell Color Science Laboratory"
    url: "https://www.rit-mcsl.org/StudentResearch/mshaw/CMF_Thesis.pdf"
  - title: "Cone fundamentals and CIE standards - Andrew Stockman, UCL Discovery"
    url: "https://discovery.ucl.ac.uk/id/eprint/10079410/1/Cone%20fundamentals%20and%20CIE.pdf"
  - title: "Observer Variability in Metameric Color Matches Using Color Reproduction Media - Alfvin & Fairchild"
    url: "http://markfairchild.org/PDFs/PAP19.pdf"
  - title: "Individual differences in colour matches and cone spectral sensitivities in 51 young adults - UCL Discovery"
    url: "https://discovery.ucl.ac.uk/10194578/1/2024%20LEDMax2%2051%20observers%20SLRSHS.pdf"
  - title: "A compact visual colorimeter for measuring individual colour-matching functions - Ragoo et al., Optics Express"
    url: "https://ivarfa.folk.ntnu.no/publications/journal/Ragoo_24_oe.pdf"
  - title: "CIE 1931 color space - Wikipedia"
    url: "https://en.wikipedia.org/wiki/CIE_1931_color_space"
  - title: "Luminous efficiency function - Wikipedia"
    url: "https://en.wikipedia.org/wiki/Luminous_efficiency_function"
  - title: "How 17 People Defined Modern Color Spaces - Fstoppers"
    url: "https://fstoppers.com/education/every-color-space-edit-was-defined-eyes-17-people-1920s-england-904135"
---

There is a story that goes around every year or so: every colour space you have ever used — sRGB, Display P3, Rec. 2020, the ICC profile inside your printer driver, the ΔE number your calibration software prints — traces back to the eyes of seventeen people in 1920s London. I saw a careful version of it this week and went looking for the primary documents, because a claim like that is usually either trivially true and meaningless, or true and worse than it sounds.

It is the second one. But not for the reason the story tells you.

## What the standard actually says

The document in force is ISO/CIE 11664-1:2019, *Colorimetry — Part 1: CIE standard colorimetric observers*. It is a minor revision of a 2006 standard, which was a restatement of a 1931 decision. It tabulates the colour-matching functions x̄, ȳ, z̄ from 360 nm to 830 nm at 1 nm intervals and defines the CIE 1931 standard colorimetric observer as representative of normal colour vision for fields subtending roughly 1° to 4°.

The standard does not hide its provenance. Its own text says the 1931 functions were derived from experiments on **17 observers** using 2° fields — ten at Imperial College under W. D. Wright, seven at the National Physical Laboratory under John Guild. It also notes, quietly, that the tabulated values from 360–400 nm and 700–830 nm are *extrapolations*. There was never data there.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">1931</div><div class="sl mono">the observer still in force</div><div class="sn">reaffirmed as ISO/CIE 11664-1:2019</div></div><div class="stat"><div class="sv">17</div><div class="sl mono">observers it was derived from</div><div class="sn">the standard&#x27;s own wording</div></div><div class="stat"><div class="sv">360–400</div><div class="sl mono">nm where the values are extrapolated</div><div class="sn">no measurements at all</div></div><div class="stat"><div class="sv">2.5</div><div class="sl mono">mean ΔE between two real viewers</div><div class="sn">20 observers, 14 metameric stimuli</div></div></figure>


## Why seventeen is the least of it

Colour matching is not an opinion poll, and this is where the viral version of the story goes soft. The task Wright and Guild set is a null match: a circular field split down the middle, a test light on one side, three adjustable primaries on the other, and the observer turns the knobs until the seam disappears. There is no judgement of pleasantness, no scale to anchor, no response bias to speak of. The answer is set almost entirely by three cone photopigments and the stuff in front of them — the lens, the macular pigment — and among screened trichromats the *shape* of that answer varies much less than a social scientist's intuition about n=17 would suggest.

Better than that: the two labs used incompatible methods. Wright matched against monochromatic primaries; Guild used broadband filtered ones. Transformed to a common set of primaries, the two datasets agreed closely. Cross-method agreement between independent apparatus is a far stronger warrant than sample size, and it is the thing the "seventeen people" framing throws away.


<figure class="fig pull"><p>The seventeen pairs of eyes are the most defensible thing about the 1931 observer.</p></figure>


## The part that was actually a mistake

Fairman, Brill and Hemmendinger reconstructed the 1931 derivation step by step in the 1990s, and their account is where the real problem lives.

The CIE wanted one more thing from the new system: it wanted the ȳ function to be *exactly* V(λ), the 1924 photopic luminous efficiency function, so that the Y tristimulus value would be luminance and photometry and colorimetry would become one arithmetic instead of two. This is an enormously useful property. It is also not something the data supports, because no exact linear combination of the Wright–Guild functions equals V(λ). The committee got as close as least squares allowed — fixing the luminance coefficients at 1 : 4.5907 : 0.0601 — and then did the thing that matters: it **rescaled all three functions, at every wavelength, by the ratio V(λ)/ȳ₀(λ)**.

That ratio is very nearly unity across most of the spectrum, and it leaves the spectrum locus on the chromaticity diagram untouched, which is why the move looks harmless. It is not harmless. Fairman and his co-authors are explicit that the rescaling changes colour-match predictions for non-monochromatic lights — and every light anyone actually measures is non-monochromatic. Wherever V(λ) is small, the ratio stops being nearly unity, and V(λ) is smallest exactly where the 1924 curve is known to be worst: the violet end.

So the 1931 observer is not a measurement. It is seventeen people's chromaticity data multiplied through, wavelength by wavelength, by a brightness curve that came from different observers in a different experiment, extrapolated past 400 nm where neither dataset reached. The numbers the seventeen produced are fine. The 1924 curve bolted onto them is the defect, and the rescaling is what propagated it into every XYZ value computed since.

Judd proposed a correction in 1951; Vos refined it in 1978, lowering Judd's function below 410 nm by 0.2 log units and truncating at 380 nm on the grounds that everything below was extrapolation anyway. Stockman's assessment is blunt — he calls the reconstruction "entirely unsuitable", on the grounds that it was both unnecessary and speculative. Estévez went further and argued that *no* photometric function can be a linear combination of colour-matching functions, which would make some error structural rather than fixable.

I could not pin down the size of the violet-end error to my satisfaction. Secondary coverage puts it at nearly an order of magnitude at the short-wavelength limit, which is plausible and which I have seen repeated in several places; the primary accounts I could reach describe it qualitatively, plus Vos's specific 0.2 log units relative to Judd. That is a smaller and more careful claim than the one in circulation, and since I could not get to the tabulated comparison myself, the careful one is the one I will stand behind.

## Does it bite?

Alfvin and Fairchild ran the experiment that answers this properly: 20 observers matching 14 metameric stimuli — seven prints and seven transparencies — against a CRT. Inter-observer disagreement came to about 2.6–2.7 CIELAB units as a mean colour difference from the mean, against intra-observer repeatability of 1.3–1.4. Roughly: two different people disagree about twice as much as one person disagrees with themselves. The largest gap between two observers on a single stimulus was 19.7 units, which is not a subtle mismatch.

The standard observer came out of this better than I expected. Its predicted match fell inside the 95% confidence region of the inter-observer distribution for *every* stimulus. As a description of the population mean, 1931 holds up.

What fails is the spread. The CIE Standard Deviate Observer — the official tool for predicting how much observers will disagree — underpredicted the measured mismatch by factors of 3.2 to 10.7, with no meaningful correlation to the actual values. The average is modelled; the variance is not.

A 2024 study put 51 young adults through an LED trichromator and found the same shape of result: mean matching errors of 7.3–7.7 ΔE00 at 2° and 4.2–5.5 at 10°, inter-observer variability between 2.6 and 5.8 ΔE00 depending on the control method, and an M-cone photopigment shift about 2.8 nm longer than the CIE physiological model predicts. Worth noting what that cohort is, though: ages 19 to 31, mean 24.3. It is a better dataset than 1931's and it is still not a sample of the people who look at screens.


<figure class="fig bars"><figcaption class="mono">Observers in each colour-matching dataset</figcaption><div class="rows"><div class="brow"><div class="blabel">Wright, 1928–29, 2°</div><div class="btrack"><div class="bfill" style="width:20.41%" title="Wright, 1928–29, 2° · 10"></div></div><div class="bval mono">10</div></div><div class="brow"><div class="blabel">Guild, 1931, 2°</div><div class="btrack"><div class="bfill" style="width:14.29%" title="Guild, 1931, 2° · 7"></div></div><div class="bval mono">7</div></div><div class="brow"><div class="blabel">CIE 1931 standard observer</div><div class="btrack"><div class="bfill" style="width:34.69%" title="CIE 1931 standard observer · 17, the two pooled"></div></div><div class="bval mono">17, the two pooled</div></div><div class="brow"><div class="blabel">Stiles &amp; Burch, 1955, 2°</div><div class="btrack"><div class="bfill" style="width:20.41%" title="Stiles &amp; Burch, 1955, 2° · 10"></div></div><div class="bval mono">10</div></div><div class="brow"><div class="blabel">Speranskaya, 1959, 10°</div><div class="btrack"><div class="bfill" style="width:55.10%" title="Speranskaya, 1959, 10° · 27"></div></div><div class="bval mono">27</div></div><div class="brow"><div class="blabel">Stiles &amp; Burch, 1959, 10°</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Stiles &amp; Burch, 1959, 10° · 49, some tabulations use 47"></div></div><div class="bval mono">49, some tabulations use 47</div></div><div class="brow"><div class="blabel">CIE 2006 fundamentals, genotyped</div><div class="btrack"><div class="bfill" style="width:69.39%" title="CIE 2006 fundamentals, genotyped · 34, on top of Stiles &amp; Burch"></div></div><div class="bval mono">34, on top of Stiles &amp; Burch</div></div></div></figure>


That last pair of rows is a small lesson in provenance. The Stiles & Burch 10° set is described as 49 observers in one 2024 paper and 47 in another from the same year — a two-observer discrepancy in the foundational dataset of the 10° standard observer, which neither paper remarks on and which I cannot resolve from secondary sources. It is not consequential. It is a decent proxy for how thin the citation chain under all of this gets once you start pulling.

## The replacement exists

CIE 170-1 (2006) defines physiologically based cone fundamentals, derived by Stockman and Sharpe from observers of *known genotype* — nine protanopes, twenty-two deuteranopes, three S-cone monochromats — with the luminous efficiency functions taken from 40 genotyped observers. CIE 170-2 (2015) adds the chromaticity diagrams. This is the thing the 1931 observer should have been and could not have been, since nobody could sequence an opsin gene in 1931.

Industry adoption is close to nonexistent. Not because anyone defends the 1924 curve, but because the 1931 observer's errors are not the kind that cost money at the scale most colour work happens, and swapping the observer would re-denominate every primary coordinate, every ICC profile, and every contractual ΔE tolerance in the world simultaneously. A standard's durability has very little to do with whether it is right.

That is the part I keep turning over. There is a live instrumentation thread here — Ragoo and colleagues built a visual colorimeter out of 3D-printed parts and LED engines, cheap enough that measuring an individual's colour-matching functions stops being a national-laboratory undertaking, though their pilot ran on three observers. If per-viewer colorimetry is becoming practical, the obstacle is no longer measurement. It is that nobody has a population-representative CMF dataset to compare anyone against. Every set we have is small, young, and screened for normality — the 1931 one included, and it has had ninety-five years to be replaced.
