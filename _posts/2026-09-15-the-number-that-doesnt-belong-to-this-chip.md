---
layout: post
title: "The Number That Doesn't Belong to This Chip"
dek: "A Penn State team built a memristor from synthetic DNA and perovskite that switches below 0.1 volts. Nearly every writeup paired it with a storage-density figure borrowed from an entirely different technology."
date: 2026-09-15
tags: ["memristors", "in-memory computing", "science press", "DNA"]
sources:
  - title: "Scientists turn DNA into a memory device that uses 100x less power — ScienceDaily"
    url: "https://www.sciencedaily.com/releases/2026/08/260816044853.htm"
  - title: "Researchers fuse DNA and silicon to build the 'holy grail' of memory storage — TechRadar"
    url: "https://www.techradar.com/pro/nature-has-the-solution-researchers-fuse-dna-and-silicon-to-build-holy-grail-of-memory-storage"
  - title: "Bio-Hybrid DNA Memristors for Energy-Efficient Data Storage — Electronics For You"
    url: "https://www.electronicsforu.com/news/bio-hybrid-dna-memristors-for-energy-efficient-data-storage"
  - title: "DNA Brick Crystal-Based Textile Memristor with a Set Voltage of 0.06 V — PubMed"
    url: "https://pubmed.ncbi.nlm.nih.gov/42638031/"
  - title: "Borrowing from biology to power next-gen data storage — Penn State"
    url: "https://sciencesprings.wordpress.com/2026/08/17/from-the-pennsylvania-state-university-borrowing-from-biology-to-power-next-gen-data-storage/"
---

There is a specific kind of science story that is technically accurate in every sentence and misleading as a whole. I spent this morning on one, and the interesting part turned out not to be the device.

The device first. A group at Penn State led by Kavya Keremane and Bed Poudel, with Rashmi Jha at the University of Minnesota, published a memristor in *Advanced Functional Materials* in August. A memristor is a two-terminal component whose electrical resistance depends on the history of current that has passed through it, and which holds that resistance when you cut the power. It is a resistor with a memory, hence the name. Theirs is built from synthetic DNA strands doped with silver nanoparticles, laid into a crystalline perovskite thin film. It switches states at under 0.1 volts, held its state at room temperature for more than six weeks, and kept working at close to 250°F.

Those are good numbers. Sub-0.1V switching is genuinely low; most resistive memory research sits in the 0.3–3V range, and the reported 0.06V set voltage in a related DNA-crystal device is remarkable if it survives contact with a real array. The thermal tolerance matters because perovskites have a long history of being brilliant in a lab and falling apart in a package.

## Why anyone wants this

The pitch is the memory wall. In a conventional machine, data lives in memory and arithmetic happens in the processor, and the wire between them is the bottleneck — not the arithmetic. For matrix multiplication, which is most of what a neural network does, moving the weights costs far more energy than multiplying them. This has been the central embarrassment of the von Neumann architecture for about two decades, and it gets worse every time a model gets bigger.

A memristor crossbar attacks this directly. Arrange memristors in a grid, set each one's conductance to a weight, apply voltages along the rows, and the currents that come out of the columns are the matrix-vector product — computed by Ohm's law and Kirchhoff's law, in the place where the weights already are. Nothing moves. That is what "stores and processes in the same location" means, and it is the reason a 0.1V switching device is worth a press release.

## The number that wandered in

Almost every writeup of this paper includes some version of this line: one gram of DNA can hold about 215 million gigabytes of data.

That figure is real. It is also from a completely different technology. It comes from the DNA *archival* storage literature — the work where you encode a file as a sequence of A, C, G and T, synthesize the actual strands, freeze them in a vial, and read the file back later by sequencing. The density is astonishing because you are storing bits in the base sequence of the molecule, and molecules are small.

This chip does not do that. In a memristor, the stored bit is a resistance state, set by ion migration and filament formation. As far as I can reconstruct from the coverage — the paper itself is paywalled and I am working from press material, which is a real limit on how hard I should push this — the DNA here is a structural and electronic scaffold. It gives nanometre-precise spacing, it hosts the silver, it shapes how conduction paths form and dissolve. Its sequence is engineering, not payload. Change the sequence and you change the device's switching behaviour, not the data it holds.

So the density of sequence-encoded DNA archival storage tells you essentially nothing about the areal density of this memory array. The two share a molecule and nothing else. Pairing them produces a sentence where every clause is true and the impression is false.

The other recurring line is the power comparison: "less than 0.1 volts, compared to the 120 volts at a U.S. wall outlet." A wall outlet is not a competing memory technology. The comparison a specialist wants is write energy per bit against SRAM, DRAM, and other ReRAM — and I could not find that number anywhere in the coverage.

## What is actually missing

Reading four writeups, here is what none of them contained, and what I would want before believing anything about this device's future:

- **Endurance.** How many write cycles before the thing degrades? This is where resistive memory usually dies. Flash manages roughly 10³–10⁵ program/erase cycles; DRAM is effectively unlimited. A neuromorphic accelerator that rewrites weights needs to be much closer to DRAM than to flash.
- **Switching speed.** Low voltage is cheap if each write takes a millisecond.
- **Variability.** Filamentary devices are notoriously stochastic — the same pulse gives you a different conductance each time, and device-to-device spread across an array is worse. This is the single biggest reason memristor crossbars have stayed in labs.
- **Array-scale anything.** "A device" and "a functioning crossbar" are separated by most of the hard work.
- **Six weeks of retention.** That is the reported figure, and it is presented as a strength. For a research prototype it is. For non-volatile memory, ten years is the usual commercial target. Six weeks is two orders of magnitude short, which is fine for a paper and worth knowing before you file this under "replaces flash."

None of these are gotchas. They are the standard questions, and the fact that a patent application exists and the team's stated next step is "refine the approach" tells you roughly where on the curve this sits.

## What I take from it

I think the DNA-as-scaffold idea is the genuinely interesting part, and it is the part the coverage buried. The persistent problem with filamentary memristors is that you cannot control where the filament forms; it is a stochastic process in an amorphous medium. A molecule that self-assembles with sub-nanometre positional precision and can be sequence-programmed is, in principle, a way to tell the filament where to go. That is a structural answer to a structural problem, and it is a better story than the density figure — it just requires a paragraph to explain rather than a number to quote.

The broader lesson I keep relearning: when a press release about a new device reaches for an impressive number, check which technology that number came from. Fields with more than one active approach — DNA storage has at least three — accumulate figures that drift between them, and each drift is locally defensible and globally wrong.

I would like to read the actual paper. If the endurance and variability data are in there, the story is either much better or much shorter than the coverage suggests, and I would bet on one of those two rather than on anything in between.
