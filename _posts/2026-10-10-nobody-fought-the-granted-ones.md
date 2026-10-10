---
layout: post
title: "Nobody Fought the Granted Ones"
dek: "An entropy coder its inventor gave away is now inside zstd, Apple's compressor and the genomics archives. The patent fight people remember was over the one application that got rejected anyway."
description: "An entropy coder its inventor gave away is now inside zstd, Apple's compressor and the genomics archives. The patent fight people remember was over the one application that got rejected anyway."
date: 2026-10-10
tags: ["compression", "software patents", "information theory", "entropy coding"]
accent: "#5C6B10"
accent_dark: "#C2D157"
sources:
  - title: "Asymmetric numeral systems: entropy coding combining speed of Huffman coding with compression rate of arithmetic coding — Jarek Duda, arXiv:1311.2540"
    url: "https://arxiv.org/abs/1311.2540"
  - title: "Interleaved entropy coders — Fabian Giesen, arXiv:1402.3392"
    url: "https://arxiv.org/abs/1402.3392"
  - title: "rANS notes — The ryg blog"
    url: "https://fgiesen.wordpress.com/2014/02/02/rans-notes/"
  - title: "Zstandard Compression and the 'application/zstd' Media Type — RFC 8478"
    url: "https://www.rfc-editor.org/rfc/rfc8478.html"
  - title: "FiniteStateEntropy — benchmark table, Yann Collet"
    url: "https://github.com/Cyan4973/FiniteStateEntropy"
  - title: "US20170164007A1, Mixed boolean-token ANS coefficient coding — Google Patents"
    url: "https://patents.google.com/patent/US20170164007A1/en"
  - title: "US11234023B2, Features of range asymmetric number system encoding and decoding — Google Patents"
    url: "https://patents.google.com/patent/US11234023B2/en"
  - title: "US9595976B1, Folded integer encoding — Google Patents"
    url: "https://patents.google.com/patent/US9595976B1/en"
  - title: "GB2538218A, Compressing data using asymmetric numeral systems with probability distributions — Google Patents"
    url: "https://patents.google.com/patent/GB2538218A/en"
  - title: "After Patent Office Rejection, It is Time For Google To Abandon Its Attempt to Patent Use of Public Domain Algorithm — EFF"
    url: "https://www.eff.org/deeplinks/2018/08/after-patent-office-rejection-it-time-google-abandon-its-attempt-patent-use-public"
  - title: "Alarm raised after Microsoft wins data-encoding patent — The Register"
    url: "https://www.theregister.com/2022/02/17/microsoft_ans_patent/"
  - title: "Asymmetric numeral systems — ESP Wiki (End Software Patents)"
    url: "https://wiki.endsoftwarepatents.org/wiki/Asymmetric_numeral_systems"
  - title: "Hey Google: Stop Trying To Patent A Compression Technique An Inventor Released To The Public Domain — Techdirt"
    url: "https://www.techdirt.com/2018/06/13/hey-google-stop-trying-to-patent-compression-technique-inventor-released-to-public-domain"
  - title: "JPEG XL — Wikipedia (browser support history, entropy coding)"
    url: "https://en.wikipedia.org/wiki/JPEG_XL"
  - title: "Asymmetric numeral systems — Wikipedia (adopters list)"
    url: "https://en.wikipedia.org/wiki/Asymmetric_numeral_systems"
  - title: "Zstd 1.5.6 Released - Celebrating Google Chrome Support For Zstandard Encoding — Phoronix"
    url: "https://www.phoronix.com/news/Zstd-1.5.6-Zstandard"
---

If this page reached you over a connection that negotiated `Content-Encoding: zstd`, part of the unpacking was done by a method a Polish researcher posted to arXiv in November 2013 and deliberately refused to patent. Chrome shipped zstd content encoding in version 123. The format is [RFC 8478](https://www.rfc-editor.org/rfc/rfc8478.html), and section 4 of it is blunt about the internals: "Two types of entropy encoding are used by the Zstandard format: FSE and Huffman coding." FSE is Finite State Entropy, Yann Collet's implementation of the table-driven flavour of Jarek Duda's asymmetric numeral systems.

I went looking into ANS this week to understand the patent fight people remember. I came away much more interested in the patents nobody fought.

## The trick

Huffman coding assigns each symbol a whole number of bits, which means it silently rounds every probability to a power of two. If one symbol has probability 0.8, the best Huffman can do is spend one bit on it, and one bit is about three times what information theory says that symbol is worth (0.32 bits). Arithmetic coding fixes this — it tracks a sub-interval and can spend fractional bits — but it carries two state variables, needs careful renormalisation, and costs real work per symbol.

Duda's idea, in the [2013 paper](https://arxiv.org/abs/1311.2540) whose title is itself the pitch — *entropy coding combining speed of Huffman coding with compression rate of arithmetic coding* — is to keep the state as a **single natural number**. Each symbol's share of that number is proportional to its probability. Because there is only one state value, renormalisation becomes "shift some digits in, shift some out", and for a fixed distribution the entire encoder and decoder behaviour can be precomputed into a lookup table. Duda calls it an entropy coding automaton and notes it runs to a few kilobytes for a 256-symbol alphabet. You get near-exact probabilities at the cost of a table read.

Here is what that buys on a deliberately lopsided source, from the benchmark table in Collet's [FiniteStateEntropy repository](https://github.com/Cyan4973/FiniteStateEntropy):


<figure class="fig bars"><figcaption class="mono">Compression ratio, Proba80 (a heavily skewed synthetic source)</figcaption><div class="rows"><div class="brow"><div class="blabel">Huffman (huff0)</div><div class="btrack"><div class="bfill" style="width:72.17%" title="Huffman (huff0) · 6.38×"></div></div><div class="bval mono">6.38×</div></div><div class="brow"><div class="blabel">Huffman (zlib)</div><div class="btrack"><div class="bfill" style="width:72.17%" title="Huffman (zlib) · 6.38×"></div></div><div class="bval mono">6.38×</div></div><div class="brow"><div class="blabel">tANS (FSE)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="tANS (FSE) · 8.84×"></div></div><div class="bval mono">8.84×</div></div><div class="brow"><div class="blabel">Arithmetic coder, same file</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Arithmetic coder, same file · not benchmarked"></div></div><div class="bval mono muted">not benchmarked</div></div></div></figure>


That gap is the whole argument, and it closes fast: on the repo's near-uniform test file, FSE and Huffman land at 1.13 against 1.13, and Huffman decodes faster. The benchmark is also softer than it looks — synthetic files from the library's own generator, 32 KB blocks, one i7-5600U laptop, GCC 4.8.4 — and the comparison the title promises, against an actual arithmetic coder, is not in the table at all. Duda's own abstract cites roughly 50% faster decoding than Huffman for a 256-symbol alphabet and a ratio close to arithmetic coding, but that figure is his summary of someone else's implementation, with no dataset or machine named. Everyone agrees ANS sits between the two. Nobody in the canonical sources has published the three-way measurement.

### The part that doesn't fit on the slide

Fabian Giesen's [rANS notes](https://fgiesen.wordpress.com/2014/02/02/rans-notes/) are the best plain-language account of the catch. Because the encoder and decoder functions are strict inverses, "the last symbol encoded will be the first symbol returned by the decoder." So the encoder has to run the data backwards. Giesen, who implemented it: "The reverse encoding seems like a total pain at first, and it kind of is." Adaptive modelling is worse — you need a forward pass to build the model and a backward pass to write the bits. There is a further constraint that the total frequency must divide the normalisation bound, which Giesen calls "a serious limitation" and which is why both get chosen as powers of two.

Which makes the division of labour inside zstd read differently to me. Huffman handles the literals; FSE handles literal lengths, match lengths, offset codes, and the Huffman headers themselves. ANS didn't replace Huffman there. It took the jobs with static tables and skewed distributions, where its accuracy actually pays for the awkwardness, and left the rest alone.

It took a lot of jobs. Per Wikipedia's list: zstd (so the Linux kernel, Chrome, Android), Apple's LZFSE, Google's Draco, the CRAM genomics format in samtools, NVIDIA's nvCOMP, Microsoft's DirectStorage BCPack, JPEG XL and JPEG AI.

## The fight people remember

In December 2016, Google filed US application 15/370,840, *Mixed boolean-token ANS coefficient coding*, inventor Alexander Jay Converse, claiming a 2015 priority date. Duda — an assistant professor at Jagiellonian University who had, by his own account, spent time helping Google engineers implement ANS for video compression — found out, and found the collaboration had gone quiet. He called the application "completely ridiculous," said he could not afford a patent lawyer, and filed a third-party submission so the examiner would at least have his papers in front of them. Google's line to Ars Technica was that Duda's work was "a theoretical concept" and its application covered "a specific application of that theory."

In August 2018 the USPTO issued a non-final rejection of every claim. The [EFF's summary](https://www.eff.org/deeplinks/2018/08/after-patent-office-rejection-it-time-google-abandon-its-attempt-patent-use-public) lists three grounds: the broadest claims ineligible as abstract ideas under *Alice*, all claims unclear and functionally described, and all claims obvious over three references — Duda's paper, an arXiv note by Fabian Giesen, and a twenty-year-old patent on data management in a video decoder. Google abandoned it. EFF's closing line: "ANS should belong to all of us."

A good outcome, and the one that got written up. But while it was being fought:

- **GB2538218 / US 9,847,791**, filed February 2015, covering rANS driven by Markov-model probability tables with an escape code and SIMD table lookups, aimed squarely at gene-sequence data. The UK grant published in 2021; the US patent issued in December 2017. Anticipated expiry 2035.
- **US 9,595,976**, *Folded integer encoding*, Google's own, filed September 2016 and granted in March 2017 — six months before the ANS story broke. It cites Duda's arXiv paper and names "asymmetrical number systems" as an alternative to the arithmetic coders it describes.
- **US 11,234,023**, *Features of range asymmetric number system encoding and decoding*, Microsoft, filed June 2019. Final rejection October 2020; Microsoft responded in March 2021; granted January 2022. There is a continuing application filed December 2021 and, per the ESP Wiki, pending filings in Europe, South Korea and China.


<figure class="fig pull"><p>The loud fight was over the application that failed. The ones that were granted went through in near silence.</p></figure>


I read claim 1 of the Microsoft patent, in fragments, through Google Patents. It is not a claim on ANS. It is a computer system with a rANS decoder "configured to perform operations using a two-phase structure," where one phase conditionally merges buffered input into the state and the other conditionally emits a symbol once the state holds enough information — a pipelining arrangement for hardware. Duda's reaction in [The Register](https://www.theregister.com/2022/02/17/microsoft_ans_patent/) was that it "looks like just the description of the standard algorithm." Having read it, I think that overstates it: the claim is narrower than the alarm implied. I also don't think narrow is the same as harmless, because claim scope is settled by litigation, and none of these has been litigated.

## What I can't see

Nearly every status fact above carries a warning label. Google Patents flags its own legal-status fields as assumptions rather than legal conclusions — "Abandoned," "Active," the 2035 expiry, all assumptions. The GB/US genomics pair has an assignee disagreement: Google Patents lists an individual inventor as assignee, the ESP Wiki lists PetaGene Ltd, and at least one of those is stale. The ESP Wiki itself is run by a campaign against software patents; everything on it I could independently check held up, but its selection of what to record is a position, not a register. And I read claims through a rendering layer, not the file history.

The question that actually matters — does any shipping ANS implementation infringe any of these — has no public answer. Jon Sneyers, the JPEG XL spec editor, told The Register that as far as he knows the Microsoft patent doesn't affect JPEG XL, that Microsoft has not declared it to ISO despite participating in the committee, and that he is not a lawyer. Microsoft declined to say whether it would seek royalties. That is the entire record.

## The gate turned out to be somewhere else

The 2022 worry was specific: a patent would chill JPEG XL. Four years on, the obstacle was something else. Chrome pulled JPEG XL in version 110, citing lack of ecosystem interest. In November 2025 the Chrome team said it was open to a **memory-safe** decoder; a Rust implementation was merged into Chromium in January 2026 and restored in 145 behind a flag, with default shipping planned for 155. Firefox switched to a Rust decoder in January 2026 and landed JPEG XL in 152 behind Firefox Labs, default planned for 157. Safari shipped it natively back in version 17.

Chilling effects are unobservable by construction, so I can't say the patent did nothing. But the visible gate was a rewrite in a memory-safe language and three years of browser politics, not a claim chart. The coverage I find most sympathetic was pointing at the wrong door.

The compression numbers in that debate are soft too. ISO's call for proposals *required* a 60% improvement over JPEG — a specification, not a measurement. Duda told The Register roughly 3×. Wikipedia's 20% figure for lossless JPEG recompression traces to a hobbyist write-up. A requirement, a claim, and a blog post, none of them the same quantity.

---

What stays with me is how thin the defence was. ANS is in the kernel, in two browsers' network stacks, in Apple's compressor, in the format genomics archives use. It got there because one person wrote it down in public, gave it away, and then spent a decade reading patent dockets without a lawyer, filing third-party submissions when something showed up. Prior art does not enforce itself; somebody has to notice and say so, in the right venue, before the clock runs out.

That is not a system. That is a person.
