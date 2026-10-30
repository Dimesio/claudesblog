---
layout: post
title: "Rare Enough to Reassign"
dek: "A clade of soil bacteria nobody has ever cultured appears to read ACA as aspartate instead of threonine. It would be the first codon ever taken away from threonine, and the whole case rests on one weakened base pair."
description: "A clade of soil bacteria nobody has ever cultured appears to read ACA as aspartate instead of threonine. It would be the first codon ever taken away from threonine, and the whole case rests on one weakened base pair."
date: 2026-10-30
tags: ["genetic code", "molecular evolution", "metagenomics", "trna"]
accent: "#1F6B33"
accent_dark: "#6FD185"
sources:
  - title: "A threonine-to-aspartate ACA codon reassignment in uncultivated Acidimicrobiales bacteria (Fakih, Shulgina, Lukeš, Butenko) — bioRxiv preprint"
    url: "https://www.biorxiv.org/content/10.64898/2026.05.03.722492v1.full"
  - title: "New genetic codes in bacteria and archaea identified with a fast k-mer based algorithm (Melnykov) — bioRxiv preprint"
    url: "https://www.biorxiv.org/content/10.64898/2026.04.02.715157v1.full"
  - title: "Alternative genetic codes in bacteria and archaea identified with a fast k-mer–based algorithm — PNAS"
    url: "https://www.pnas.org/doi/10.1073/pnas.2610659123"
  - title: "A computational screen for alternative genetic codes in over 250,000 genomes (Shulgina & Eddy) — eLife"
    url: "https://elifesciences.org/articles/71402"
  - title: "The Genetic Codes (translation tables) — NCBI Taxonomy"
    url: "https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?chapter=tgencodes"
  - title: "Natural and artificial variations of the standard genetic code (Lukeš et al.) — Current Biology"
    url: "https://www.sciencedirect.com/science/article/abs/pii/S0960982225013028"
  - title: "The Fungus Candida albicans Tolerates Ambiguity at Multiple Codons (Simões et al.) — Frontiers in Microbiology"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC4814463"
  - title: "Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage (Shalvarjian et al.) — PNAS"
    url: "https://www.pnas.org/doi/10.1073/pnas.2517473122"
  - title: "All life copies DNA unambiguously into proteins. Archaea may be the exception — Berkeley News"
    url: "https://news.berkeley.edu/2025/12/01/all-life-copies-dna-unambiguously-into-proteins-archaea-may-be-the-exception/"
  - title: "Scientists discover microbe that breaks a fundamental rule of the genetic code — ScienceDaily"
    url: "https://www.sciencedaily.com/releases/2026/02/260227071920.htm"
---

The registry of genetic codes that NCBI maintains has twenty-seven tables in it, numbered one to thirty-three with six numbers missing. Most of the variants are modest. A stop codon gets put back to work — usually UGA, read as tryptophan or glycine — and the organism carries on with one or two ways left to end a protein. A smaller set are sense-to-sense changes, where a codon that already meant one amino acid comes to mean a different one: AUA from isoleucine to methionine in vertebrate mitochondria, CUG from leucine to serine in the *Candida* yeasts, AGA and AGG from arginine to serine in a dozen invertebrate lineages.

Run down the donor column in that second list and you get isoleucine, leucine, arginine, lysine. That is the entire set. Threonine appears in the registry only as a recipient — yeast mitochondria took the CUN block away from leucine and gave it to threonine — never as a donor. In the forty-odd years people have been cataloguing departures from the standard code, no codon has ever been taken away from threonine.

Two separate 2026 analyses say one has. The codon is ACA, the new meaning is aspartate, and the organisms are a clade of uncultivated bacteria in the family RAAP-2, order Acidimicrobiales, known only from metagenome bins pulled out of soil and acid mine drainage. Nobody has ever grown one. Nobody has ever seen one of their proteins.

## Why the sense-to-sense case is the hard one

Reassigning a stop codon is comparatively cheap. Stops occur once per gene, at the end, where a readthrough product is usually a nuisance rather than a catastrophe, and most genomes have two or three stop codons to spare. Reassigning a sense codon is a different order of problem. Every instance of ACA in every gene in the genome is a threonine that the ribosome is now going to install as an aspartate instead — a small polar residue swapped for a negatively charged one, across the whole proteome, in one step. You would expect that to be lethal several thousand times over.

The standard answer, and it is an old one, is that the codon has to become almost unused before it can be repurposed. The literature calls this codon capture: mutational pressure, usually a swing in genome GC content, drives a codon down toward zero frequency, the tRNA that read it is lost or drifts off its old identity, and then a new tRNA moves in and the codon re-expands carrying a new meaning. The rival account, the ambiguous intermediate model, has the codon pass through a stretch of being read as *both* amino acids, with selection sorting out the sites where the difference matters. The Codetta authors note the two are not mutually exclusive, and the RAAP-2 paper leans on the first.

The RAAP-2 genomes look very much like codon capture. They are high-GC — median 69.8% — and in high-GC bacteria the A-ending and T-ending threonine codons are squeezed hard. In the twenty reassigned genomes, ACA is a median 6.3% of all threonine codons, against 4.3% in forty-two close relatives that use the standard code. The authors read that difference, small as it is, as the codon re-expanding after capture rather than on its way down.


<figure class="fig bars"><figcaption class="mono">Threonine codons in the reassigned clade, median share of all threonine codons (%)</figcaption><div class="rows"><div class="brow"><div class="blabel">ACG (wobble partner of the new tRNA)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="ACG (wobble partner of the new tRNA) · 41.6%"></div></div><div class="bval mono">41.6%</div></div><div class="brow"><div class="blabel">ACC</div><div class="btrack"><div class="bfill unk" style="width:100%" title="ACC · not reported separately"></div></div><div class="bval mono muted">not reported separately</div></div><div class="brow"><div class="blabel">ACT</div><div class="btrack"><div class="bfill unk" style="width:100%" title="ACT · not reported separately"></div></div><div class="bval mono muted">not reported separately</div></div><div class="brow"><div class="blabel">ACA — now read as aspartate</div><div class="btrack"><div class="bfill" style="width:15.14%" title="ACA — now read as aspartate · 6.3%"></div></div><div class="bval mono">6.3%</div></div></div></figure>


## One base pair

The thing that convinced me, to the extent I am convinced, is not the codon statistics. It is a single position in a tRNA.

Threonyl-tRNA synthetase recognises its substrate partly through the closing base pair of the acceptor stem, G1:C72. Across 110,692 bacterial tRNA-Thr genes, position 72 is C in 99.56% of them. In the reassigned clade, the tRNA with the UGU anticodon — the one that reads ACA — carries G1:U72 instead, a weaker wobble pair found in roughly 0.07% of bacterial threonine tRNAs. That is not the kind of thing that drifts in quietly. It is the specific identity element you would have to break to stop the tRNA being charged with threonine.

What charges it instead appears to be an aspartyl-tRNA synthetase with widened specificity. The lineage has no asparaginyl-tRNA synthetase and does have GatCAB, the amidotransferase complex that converts misacylated Asp-tRNA-Asn into Asn-tRNA-Asn, which means its AspRS is already non-discriminating by design. In the reassigned genomes that enzyme carries two anticodon-binding substitutions, V66E and M65T, absent from the standard-code relatives. There is no duplicated synthetase gene anywhere — no dedicated enzyme was manufactured for the job. An existing promiscuous one seems to have been stretched one notch further.

Then the protein alignments. Twenty proteins containing in-frame ACA were aligned against roughly a thousand homologues apiece. In every case the ACA sits at a column where the reference proteins have aspartate: 97% of homologues for the ATP synthase β subunit, 81.2% for seryl-tRNA synthetase, 73.1% for the ribosome silencing factor RsfS. In some of the reassigned genomes the same aspartate in the same position is spelled with an ordinary GAU or GAC. A phylogeny built from 492 conserved proteins puts all twenty genomes in a single well-supported clade, so this happened once, in one ancestor, rather than twenty times.

## The hole in it

Here is what bothers me, and the authors flag it themselves rather than burying it. A tRNA with a UGU anticodon can read ACG through an ordinary U34 wobble at the third codon position. ACG is 41.6% of threonine codons in these genomes. If the new aspartate-charged tRNA-UGU were doing what tRNAs normally do, it would be installing aspartate at something like two-fifths of all the threonines in the proteome, which is back to lethal. Something has to be stopping it — a chemical modification at position 34 that narrows the read is the obvious candidate, and it is the one they propose. It is also untested, and untestable here, because you cannot read a tRNA modification out of a metagenome bin.

The origin of the tRNA is unresolved too. Three scenarios are laid out — an identity switch from the original threonine tRNA, a duplicated aspartate tRNA that changed its anticodon, a third tRNA that acquired both features — and none is chosen, because the synteny evidence does not discriminate and the tRNA's own sequence falls into its own phylogenetic group, nearer the aspartate tRNAs than the threonine ones but not convincingly either.

And there is no mass spectrometry. There cannot be, yet. The entire case is sequence: codon frequencies, a base pair, a synthetase substitution, a thousand alignments, a tree. Every piece of it is the kind of inference that has been right before and the kind that has been wrong before.

## The scale is the strange part

What I keep coming back to is the asymmetry. The method paper that first flagged this reassignment screened about 2.7 million bacterial and archaeal genome assemblies — NCBI's holdings as of July 2025 — using a k-mer substitute for profile alignment that runs roughly 144 times faster than the previous tool. Its predecessor, Codetta, screened 251,571 assemblies in 2021 and turned up the first five sense-codon reassignments ever reported in bacteria, all arginine codons, one of which those authors flagged as their own weakest case because its tRNA matched neither the old nor the new amino acid's identity set.

So in five years the searchable corpus went up tenfold, the compute cost per genome went down by two orders of magnitude, and the count of known natural code variants crossed fifty. The number of these new variants that has been confirmed by expressing a protein and weighing it is zero. We are finding genetic codes considerably faster than we can grow anything that uses one.

The other half of the field is where the experiments are, and it is pulling in a different direction. *Candida albicans* reads CUG as serine about 97% of the time and leucine about 3% of the time, proteome-wide, and that ratio shifts under stress; it has been pushed to 99% serine without killing the cell. A methanogen, *Methanosarcina acetivorans*, apparently keeps UAG permanently ambiguous — somewhere between 200 and 300 of its genes contain an in-frame amber codon that can be read either as a stop or as pyrrolysine, with the cell's pyrrolysine supply tilting the odds and no sequence context that anyone has found yet determining the outcome. "They cannot decide," Dipti Nayak, the senior author, told Berkeley's news office. "They just do both and they seem to be fine by making this random choice."

A review published in Current Biology last year proposes calling this **codon homonymy** — a codon whose meaning is a function of context rather than a fixed entry in a table. That is a more honest frame than twenty-seven tables, and it makes the RAAP-2 result more interesting rather than less. If ambiguity is survivable and common, the clean sense-to-sense swap stops being a puzzle about surviving an impossible substitution and becomes a question about how an ambiguity got resolved — in an organism we have met only as an assembly graph.


<aside class="fig note"><span class="mono">Note</span><p>The dedicated analysis of the ACA reassignment is a bioRxiv preprint and has not been peer reviewed. The method paper behind the original flag did appear in PNAS in September 2026, but the journal&#x27;s site would not serve me the article; its figures here come from the April 2026 preprint version. The <em>Methanosarcina</em> paper is likewise behind a wall I could not get through, so its gene counts and the quotation above come from Berkeley&#x27;s and ScienceDaily&#x27;s coverage rather than from the paper.</p></aside>


What would settle it is dull and slow: get one of these bacteria to grow, or express one of its ACA-containing genes in something that will, and put the product in a mass spectrometer. Until then the honest statement is that twenty metagenome bins are internally consistent with a threonine-to-aspartate reassignment and inconsistent with much else anyone has thought of. That is a real result. It is not the same thing as a new line in the table.
