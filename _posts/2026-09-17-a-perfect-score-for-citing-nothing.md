---
layout: post
title: "A Perfect Score for Citing Nothing"
dek: "The disruption index hands its maximum value to any paper whose reference list is missing from the database. Nearly nine million records in one widely used corpus are exactly that — and the most repeated finding in metascience is built on top of them."
description: "The disruption index hands its maximum value to any paper whose reference list is missing from the database. Nearly nine million records in one widely used corpus are exactly that — and the most repeated finding in metascience is built on top of them."
date: 2026-09-17
tags: ["metascience", "bibliometrics", "measurement", "peer review"]
accent: "#93316E"
accent_dark: "#F0A0CF"
sources:
  - title: "Papers and patents are becoming less disruptive over time (Park, Leahey & Funk, 2023) — Nature"
    url: "https://www.nature.com/articles/s41586-022-05543-x"
  - title: "Papers and patents are becoming less disruptive over time, author manuscript — NSF Public Access Repository"
    url: "https://par.nsf.gov/servlets/purl/10382242"
  - title: "Dataset artefacts can partially drive the measured decline in disruption (Holst et al., 2026) — Nature"
    url: "https://www.nature.com/articles/s41586-026-10787-y"
  - title: "Reply to: Dataset artefacts can partially drive the measured decline in disruption (Park, Leahey & Funk, 2026) — Nature"
    url: "https://www.nature.com/articles/s41586-026-10788-x"
  - title: "The disruption index is biased by citation inflation (Petersen, Arroyave & Pammolli) — Quantitative Science Studies"
    url: "https://direct.mit.edu/qss/article/5/4/936/124788/The-disruption-index-is-biased-by-citation"
  - title: "The disruption index is biased by citation inflation, preprint — arXiv:2306.01949"
    url: "https://arxiv.org/abs/2306.01949"
  - title: "A Dynamic Network Measure of Technological Change (Funk & Owen-Smith, 2017) — Management Science"
    url: "https://pubsonline.informs.org/doi/10.1287/mnsc.2015.2366"
  - title: "VUB research calls the global debate on scientific innovation into question — VUB Press"
    url: "https://press.vub.ac.be/vub-research-calls-the-global-debate-on-scientific-innovation-into-question"
---

Take a paper that cites nothing. Not a paper with a thin bibliography — a paper whose reference list, as far as the database is concerned, is empty. Score it on the disruption index, the metric behind the most repeated claim in metascience of the past decade, and it comes out at exactly 1. The maximum. The same number the index assigns to a paper that rearranged its field so completely that everyone who cited it stopped citing what came before.

That is not a bug in somebody's implementation. It is what the formula says, and the formula is four symbols long.

## What the index actually measures

The CD index, introduced by Russell Funk and Jason Owen-Smith in *Management Science* in 2017, asks a question about a paper's descendants rather than its ancestors. Take a focal paper *p* with a reference list *{r}*. Look at everything that cites *p* within a window — five years in the standard version, hence CD5 — and sort those citing works into three bins. Bin *i* is works that cite *p* but nothing in *{r}*: they took the new thing and dropped its lineage. Bin *j* is works that cite both *p* and *{r}*: they folded the new thing into the existing conversation. Bin *k* is works that cite *{r}* but not *p*: the field carried on as though *p* had not happened.

Then:

`CD = (Ni − Nj) / (Ni + Nj + Nk)`

The result runs from −1, perfectly consolidating, to +1, perfectly disruptive. I find this a genuinely lovely construction. It doesn't try to measure importance or novelty directly, which are hopeless; it measures *eclipse*. Did your paper make its own predecessors unnecessary? That is a real, structural property of a citation network, and it is the sort of thing that only becomes visible in bulk.

Now empty the reference list. Bin *j* requires citing something in *{r}*, and *{r}* is empty, so N*j* = 0. Bin *k* requires the same, so N*k* = 0. Every citing work necessarily lands in bin *i*, and CD = N*i*/N*i* = 1. Exactly 1, no matter who cited the paper or why. To this index, a missing bibliography and total intellectual conquest are the same event.

## The claim

In January 2023, Michael Park, Erin Leahey and Russell Funk put that index on the cover of *Nature*. Working across six databases — 25 million papers from the Web of Science covering 1945 to 2010, and 3.9 million US patents from PatentsView — they reported that average CD5 had collapsed. For papers, the decline between 1945 and 2010 ranged from 91.9% in the social sciences, where mean CD5 fell from 0.52 to 0.04, to 100% in the physical sciences, where it fell from 0.36 to literally 0. For patents between 1980 and 2010 the range was 78.7% to 91.5%. Their proposed cause was "a narrowing in the use of previous knowledge" — researchers drawing on an ever-shallower pool of prior work.

It is hard to overstate how far that finding travelled. "Science is running out of ideas" became a stylised fact, repeated in funding debates, in arguments about the productivity of research spending, in essays about whether the modern academy can still produce an Einstein.

## The correction

On 29 October 2023, a group at the Vrije Universiteit Brussel and KU Leuven — Vincent Holst, Andres Algaba, Floriano Tori, Sylvia Wenmackers and Vincent Ginis — submitted a Matters Arising to *Nature* pointing at the empty-bibliography problem. It was accepted on 9 June 2026 and published on 12 August 2026. Two years and nine months from submission to print.

Their finding is blunt. In SciSciNet, a widely used derivative of Microsoft Academic Graph, 8,861,343 papers score CD5 = 1, and 97% of them have zero references on file. In PatentsView, 142,362 patents score CD5 = 1 and 78% of those have no references. The team then went and looked at the underlying documents, and reports that most of them do in fact contain references. The zeroes are not a fact about the literature. They are a fact about the metadata.

That would be a curiosity if the errors were randomly scattered. They are not. Older records are systematically thinner — reference extraction has improved enormously over the decades, and back-catalogue digitisation is worse the further back you go. So the artefact loads onto exactly the years that anchor the high end of the trend line. Drop the CD5 = 1 entries and, by Holst et al.'s account, most of the decline goes with them.


<figure class="fig bars"><figcaption class="mono">Reduction in measured CD5 decline after removing CD5 = 1 entries, %</figcaption><div class="rows"><div class="brow"><div class="blabel">Papers, SciSciNet</div><div class="btrack"><div class="bfill" style="width:90.65%" title="Papers, SciSciNet · −0.31 → −0.01"></div></div><div class="bval mono">−0.31 → −0.01</div></div><div class="brow"><div class="blabel">Papers, JSTOR</div><div class="btrack"><div class="bfill" style="width:93.46%" title="Papers, JSTOR · −0.16 → −0.00"></div></div><div class="bval mono">−0.16 → −0.00</div></div><div class="brow"><div class="blabel">Papers, APS corpus</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Papers, APS corpus · −0.27 → +0.02"></div></div><div class="bval mono">−0.27 → +0.02</div></div><div class="brow"><div class="blabel">Patents, PatentsView</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Patents, PatentsView · 58–71% across categories"></div></div><div class="bval mono muted">58–71% across categories</div></div></div></figure>


The American Physical Society row is the one that stops you: 107% means the slope crossed zero. On that corpus, with the maximal-score entries removed, measured disruptiveness very slightly *rises*.

## The reply, which is not weak

*Nature* published Park, Leahey and Funk's response alongside it, and they do not concede much. Their central objection is that Holst et al.'s corpus is dirtier than the one it is correcting. It contains, they say, three times as many zero-reference works as the original; at least 2.8 million editorials, obituaries and comments; 1.5 million books and conference proceedings; 254,000 product reviews. Roughly 20% of the sample is not research at all. They name 456 *For Dummies* guides. They name Dr. Seuss.

The share of works scoring CD = 1 tells the same story from the other end: 4.3% of papers and 4.9% of patents in the original data, against 23.1% in Holst et al.'s SciSciNet sample — a 5.4-fold overrepresentation. And they make one more argument that I think is the strongest thing either side says: Holst et al.'s *own* regression, the one designed to handle the zero-reference problem without simply deleting rows, still produces large significant declines at *P* < 0.01. That result sits in their supplementary tables, unaddressed in the main text.

There is also a real methodological objection to the deletion approach. If you remove every work scoring CD5 = 1, you remove the genuinely disruptive papers along with the broken records, because they score the same. You are deleting your outcome variable at its most informative end and then reporting that the outcome got flatter. Of course it did.

## Where I come out

Both sides are correct about each other, which is the least satisfying and most likely conclusion.

But I don't think that leaves the two claims symmetric. An index whose maximum value is returned by a missing field is not purely a measurement instrument; it is partly a coverage detector. You can argue about how much of the 1945–2010 slope is coverage and how much is science, and that argument is now properly joined. What you cannot do is treat the slope as a clean reading and then reason from it about the productivity of research funding.

And the zero-reference problem is not even the deepest objection on the table. In June 2023, four months before Holst et al. submitted, Alexander Petersen, Felber Arroyave and Fabio Pammolli posted a critique — later published in *Quantitative Science Studies* — arguing that the index is biased by citation inflation. Reference lists have grown steadily for a century. As citation networks densify, triadic closure rises mechanically, and CD is a measure of triadic closure, so CD drifts toward 0 whether or not anything about scientific practice has changed. Their conclusion is that the index is "temporally biased, and unsuitable for cross-temporal analysis" — which, if right, means the trend was never measurable on this instrument at all. That critique does not depend on any database being wrong. It survives a perfectly clean dataset.

Park and colleagues note that the decline has been documented in nearly a hundred studies across databases and metrics. That is the argument I trust least, and it is the one most often repeated.


<figure class="fig pull"><p>A hundred studies sharing one index and a handful of overlapping databases is not a hundred replications. It is one measurement, taken many times.</p></figure>


Some of those studies do use non-citation-based measures, and those are the ones worth weighing. But the citation-based majority inherits both the metadata artefact and the densification bias wholesale, and counting them adds confidence without adding evidence.

## What I could not check

The crux of this dispute is a regression in a supplementary table, and I have read both sides' characterisation of it rather than the table. Park et al. say it shows a significant decline; Holst et al. built it and apparently did not foreground the result. Someone should simply publish the arbitration — rerun the index on a hand-verified corpus with reference lists restored rather than rows deleted, research articles only, no obituaries and no Dr. Seuss. That analysis is obvious, it is not very hard, and as far as I can find nobody has put it out.

Which leaves me not knowing whether disruptiveness is declining. The narrower thing I am fairly confident of is that this index, on these databases, over this span, cannot settle it — and that "science is becoming less disruptive" has been carried into policy conversations with a certainty the measurement never had.

The last detail is the one I keep returning to. The critique sat in review for two years and nine months, during which *Nature*'s embargo conventions kept its authors from discussing it publicly, while the claim it disputes hardened into common knowledge. Science self-corrected here. It self-corrected at a speed that made the correction almost irrelevant to the thing it was correcting.
