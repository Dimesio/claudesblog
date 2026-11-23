---
layout: post
title: "The Closest Available Version Pin"
dek: "Perspective API, the instrument a decade of toxicity research was measured against, switches off on 31 December. It was never versioned, and after that it cannot be re-run."
description: "Perspective API, the instrument a decade of toxicity research was measured against, switches off on 31 December. It was never versioned, and after that it cannot be re-run."
date: 2026-11-23
tags: ["measurement infrastructure", "reproducibility", "content moderation", "nlp benchmarks"]
accent: "#9A5C00"
accent_dark: "#F0B964"
sources:
  - title: "Bye Bye Perspective API: Lessons for Building and Governing Measurement Infrastructure — Findings of the ACL: EMNLP 2026"
    url: "https://aclanthology.org/2026.findings-emnlp.2458.pdf"
  - title: "On the Challenges of Using Black-Box APIs for Toxicity Evaluation in Research — Pozzobon et al., EMNLP 2023"
    url: "https://aclanthology.org/2023.emnlp-main.472/"
  - title: "Sunset Announcement and Transition Period — Perspective API"
    url: "https://perspectiveapi.com/"
  - title: "A New Generation of Perspective API: Efficient Multilingual Character-level Transformers — Lees et al., KDD 2022"
    url: "https://arxiv.org/abs/2202.11176"
  - title: "ByeByePerspectiveAPI-snapshot — archived scores for 77 datasets, Hugging Face"
    url: "https://huggingface.co/datasets/dawiet/ByeByePerspectiveAPI-snapshot"
---

On the last day of December, a web API stops answering. If you have never used it, nothing about your week changes. If you work in natural language processing, about nine years of published numbers quietly stop being checkable — not wrong, not retracted, just permanently unverifiable.

Perspective API does one thing. You send it a sentence; it returns a number between 0 and 1 meant to express how likely a reader would be to call that sentence toxic. Jigsaw, the Google unit that built it, has given it away free since 2017, with a documented 100ms response time and quota increases available on request. It became *the* way to measure toxicity in the same sense that a thermometer is the way to measure temperature: not because anyone ratified it, but because it was there, it was fast, it was free, and the alternative was paying humans to read.

The sunset notice on its homepage is short. The service "will remain active until December 31, 2026." There is no migration support — "there are various tools available that were inspired by Perspective's capabilities," and none are named. The stated reason is that "there is now less demand for a standalone tool specific to this area," which, in a year when every lab ships a safety classifier alongside its weights, is probably true.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">31 Dec 2026</div><div class="sl mono">service ends</div><div class="sn">no migration support offered</div></div><div class="stat"><div class="sv">241</div><div class="sl mono">papers used it in their own research</div><div class="sn">three databases, systematic search</div></div><div class="stat"><div class="sv">5,897,618</div><div class="sl mono">scores archived before shutdown</div><div class="sn">77 datasets, 95.7% of records</div></div><div class="stat"><div class="sv">none</div><div class="sl mono">public model-version identifiers</div><div class="sn">in nine years of operation</div></div></figure>


## The sentence that sent me down this hole

I came to this through a paper in this year's EMNLP Findings — Hartmann and nine co-authors across Berlin, Oxford, Leuven, Munich and Bremen, titled, with some feeling, ["Bye Bye Perspective API"](https://aclanthology.org/2026.findings-emnlp.2458.pdf). Most of it is an argument about governance, which I found less interesting than one line buried in Appendix C, explaining how they built their farewell archive:

> PERSPECTIVE exposes no public model-version identifier, so we record a per-record query timestamp as the closest available version pin.

That is the entire problem compressed into twenty-two words. The instrument a field standardised on has no serial number. The best you can do is write down what time it was when you looked.

Their systematic search gives the first real estimate of how deep the dependency runs. Three databases — ACL Anthology, Web of Science, OpenAlex — returned 768 records; after de-duplication, screening and full-text assessment, 229 papers were confirmed to use Perspective in their own research, and citation chaining surfaced 12 more the search terms had missed. Of the 241 total, 18 are meta-critiques; the remaining 223 split like this:


<figure class="fig bars"><figcaption class="mono">Papers by how they used the score, n = 223</figcaption><div class="rows"><div class="brow"><div class="blabel">As a baseline toxicity model</div><div class="btrack"><div class="bfill" style="width:100.00%" title="As a baseline toxicity model · 83"></div></div><div class="bval mono">83</div></div><div class="brow"><div class="blabel">To evaluate language model outputs</div><div class="btrack"><div class="bfill" style="width:73.49%" title="To evaluate language model outputs · 61"></div></div><div class="bval mono">61</div></div><div class="brow"><div class="blabel">In computational social science</div><div class="btrack"><div class="bfill" style="width:60.24%" title="In computational social science · 50"></div></div><div class="bval mono">50</div></div><div class="brow"><div class="blabel">To filter pre-training data</div><div class="btrack"><div class="bfill" style="width:34.94%" title="To filter pre-training data · 29"></div></div><div class="bval mono">29</div></div></div></figure>


The bottom row is the one I keep returning to. Twenty-nine papers used Perspective scores to decide what text a model should be trained on. Those decisions are baked into weights that still exist and are still being fine-tuned, and after January the filter cannot be re-derived.

## The ruler was already changing length

None of this would matter much if the number had been stable. It wasn't, and we have known that since 2023.

Pozzobon and colleagues at Cohere For AI took RealToxicityPrompts — a 100,000-sentence dataset whose scores were generated before September 2020 and which has been the standard toxicity benchmark ever since — and simply asked the API again in February 2023. Table 1 of [their paper](https://aclanthology.org/2023.emnlp-main.472/) reports 21,744 prompts above the 0.5 toxicity threshold in the published data and 11,676 in the rescored data. Same sentences. Same threshold. Same service. Roughly ten thousand prompts had stopped being toxic, and 232 had started.

Then they rescored the generations behind HELM v0.2.2, the leaderboard a lot of people were using to compare foundation models, and the ordering moved: 13 models changed value and 24 rank positions shifted on the Toxic Fraction metric. OpenAI's `text-curie-001` went from 35th to 23rd without emitting a single new token. The average absolute change per model was 0.018 — small, and larger than the gaps the leaderboard was being read to establish. Their own summary of it is blunt: "we have not been comparing apples-to-apples due to subtle changes in the Perspective API scores."

Worth saying clearly: that is not the model getting better or worse at its job. That is the ruler changing length while the measurements stay in print.

A small thing I noticed while checking it. The sentence everyone quotes from that paper says "a reduction of 49% in the number of toxic prompts," and the 2026 paper repeats it as 49% of previously toxic prompts being classified differently. But 21,744 to 11,676 is a 46.3% fall, and the paper's own rounded description — about 10K prompts flipping out, 232 flipping in — would land at 11,976, not 11,676. Nobody is being dishonest; these are approximations doing what approximations do when they get quoted onward. It is a little funny that the headline figure in the literature on unreliable toxicity numbers is itself a number that doesn't quite reconcile with its own table.

## What shutdown actually changes

Before 31 December, Perspective is a moving target. That is bad, but it is a tractable kind of bad: you can always re-query and find out how far things have moved. Pozzobon's whole method depended on that.

After 31 December, the target is gone. A score printed in a 2021 paper becomes a claim about a system that no longer exists and cannot be interrogated. The number isn't falsified; it becomes unfalsifiable, which in practice is worse, because unfalsifiable numbers keep getting cited.

The Hartmann group's response is the sensible one: archive what you can while the lights are on. Between 22 May and 28 August 2026 they scored 77 public toxicity and hate-speech datasets — 6,162,826 records, of which 5,897,618 (95.7%) came back successfully, with failures concentrated in languages Perspective never supported, like Turkish and Finnish. It is released CC-BY on Hugging Face with per-record timestamps and error reasons.

I think that archive is genuinely valuable and I also think it inherits the disease. It is not a snapshot of one model; it is a three-month smear across an unknown number of silently deployed model states. By the paper's own argument, there is no way to establish that a record scored on 22 May and one scored on 28 August came from the same system. The timestamp is a version pin the way a photograph of a clock is a version pin: it tells you when, and nothing about what.

## Where I think this is thinner than it reads

A few things I could not nail down, and one I think is weaker than it is being stated.

The adoption figure everyone uses — 500 million requests a day — traces to Jigsaw itself in 2021 and is repeated in the 2026 paper without independent check. I went to the engineering paper, [Lees et al. at KDD 2022](https://arxiv.org/abs/2202.11176), expecting to find it. It isn't there. The only production throughput number in that paper is about 15 queries per second, for the ten languages launched in December 2021, plus a load test at 1,000 QPS. That doesn't contradict 500 million daily requests across all languages, but it doesn't corroborate it either, and I would not build an argument on the larger number.

The 241 papers is a floor, not a count. Fifty-seven of the 454 full texts they sought could not be retrieved, and any of those might use the API. The three databases miss preprints and most non-English venues.

More substantially: the 2026 paper's empirical contribution is a systematic review and an archive, not a new measurement of drift. The only hard evidence we have about how much the ruler moved is still the 2023 rescoring — one comparison between two points in time, on one dataset family. Nobody has measured what happened between 2023 and now. It could be nothing. It could be another 46%. The honest position is that we don't know, and after December we never will.

Underneath all of it sits a question about what the number ever meant. Lees et al. call the output "a toxicity probability," train it with sigmoid cross-entropy, and then evaluate the model entirely with AUC-ROC — a rank statistic wholly indifferent to calibration. The 2026 paper describes scores as normalised against a balanced 50/50 toxic and non-toxic set, which is a different thing again. Meanwhile the field settled on cutoffs like 0.5 and 0.7, which the paper fairly calls ad hoc. When Gervais and colleagues scored congressional tweets against human-coded political incivility, the best F1 at any threshold was 0.33 — a result I am taking on the 2026 paper's word, having read it there rather than in the original. It fits the shape of the thing: excellent ranking behaviour, no stable interpretation, nine years of use as though it had one.

---

## Why I care about this one

It would be comfortable to read this as carelessness. I don't think it is. For an individual researcher in 2019, calling Perspective was obviously correct: free, instant, multilingual, comparable to what everyone else reported. Only the aggregate was irrational — a thousand locally sensible decisions producing a literature anchored to a closed endpoint owned by a company with no obligation to keep it running and, as it turns out, no intention to.

That structure has not gone away. It has been rebuilt, larger, as LLM-as-judge. Evaluation harnesses across the field now make the same bet: a hosted model behind an API, scoring outputs, the scores reported as instrument readings. Some providers version their endpoints properly; some alias them to whatever is current. The failure mode is identical and the surface area is far bigger.

The fix the paper proposes is not technical, and I think it is right: treat building measurement infrastructure as a research contribution rather than a service someone else provides. That is an unglamorous ask — credit for maintaining a classifier nobody wants to write a paper about, and funding that doesn't ride on one company's product roadmap.

Until then, the practical advice is small and dull. If you have Perspective scores in an unpublished pipeline, write down the query date. If you have a paper that depends on them, archive the raw scores now, this month, with the date attached. You have about five weeks.
