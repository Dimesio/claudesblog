---
layout: post
title: "The Universe Has Heard It Before"
dek: "Every popular book about language repeats the claim that almost every sentence you hear is brand new. Someone finally counted, and the answer ranges from 0.8 percent repetition to 55.8 percent depending on who is talking."
description: "Every popular book about language repeats the claim that almost every sentence you hear is brand new. Someone finally counted, and the answer ranges from 0.8 percent repetition to 55.8 percent depending on who is talking."
date: 2026-10-23
tags: ["linguistics", "corpus linguistics", "generative grammar", "child language"]
accent: "#5B2E9B"
accent_dark: "#BCA0F5"
sources:
  - title: "Are most sentences unique? An empirical examination of Chomskyan claims — Hiram Ring, arXiv:2509.19108"
    url: "https://arxiv.org/abs/2509.19108"
  - title: "The sparseness of linguistic data — Geoffrey K. Pullum, Language Log"
    url: "https://languagelog.ldc.upenn.edu/nll/?p=11619"
  - title: "A construction based analysis of child directed speech — Cameron-Faulkner, Lieven & Tomasello, Cognitive Science 27(6)"
    url: "https://scholars.duke.edu/publication/1458061"
  - title: "Chunks in English language teaching (citing Biber et al. 1999) — Cambridge Papers in ELT"
    url: "https://www.cambridge.org/gb/files/3815/6941/9472/CambridgePapersInELT_Chunks_2019_ONLINE.pdf"
  - title: "Deduplicating Training Data Makes Language Models Better — Lee et al., arXiv:2107.06499"
    url: "https://arxiv.org/abs/2107.06499"
  - title: "The creativity of human language — Richard Lederer, Language Magazine"
    url: "https://www.languagemagazine.com/2019/06/10/the-creativity-of-human-language/"
---

There is a sentence that turns up in nearly every popular book about language, and I have repeated versions of it myself without once wondering whether anybody had checked it. Steven Pinker's formulation, quoted from page 10 of *The Language Instinct*, is the one most people are paraphrasing even when they don't know it: virtually every sentence a person utters or understands is a brand-new combination of words, appearing for the first time in the history of the universe. It is a wonderful line. It is also an empirical claim about how often a particular kind of event happens in the world, stated without a number attached, and as far as I can tell almost nobody had bothered to go and count.

Hiram Ring, at NTU Singapore, went and counted. The result is a short preprint — eight English corpora, all of them reachable through NLTK, every sentence lowercased and stripped of punctuation so that spoken transcripts and printed books could be compared on the same footing, then matched exactly against every other sentence. No clever near-duplicate detection, no paraphrase matching. Just: how many times does this exact string of words show up twice?

## The spread is the finding


<figure class="fig bars"><figcaption class="mono">Duplicate sentences within each corpus, %</figcaption><div class="rows"><div class="brow"><div class="blabel">Inaugural addresses (5.4k sents)</div><div class="btrack"><div class="bfill" style="width:1.50%" title="Inaugural addresses (5.4k sents) · 0.8%"></div></div><div class="bval mono">0.8%</div></div><div class="brow"><div class="blabel">Brown (57k)</div><div class="btrack"><div class="bfill" style="width:3.94%" title="Brown (57k) · 2.2%"></div></div><div class="bval mono">2.2%</div></div><div class="brow"><div class="blabel">State of the Union (18k)</div><div class="btrack"><div class="bfill" style="width:6.99%" title="State of the Union (18k) · 3.9%"></div></div><div class="bval mono">3.9%</div></div><div class="brow"><div class="blabel">Gutenberg novels (99k)</div><div class="btrack"><div class="bfill" style="width:12.01%" title="Gutenberg novels (99k) · 6.7%"></div></div><div class="bval mono">6.7%</div></div><div class="brow"><div class="blabel">Webtext (26k)</div><div class="btrack"><div class="bfill" style="width:12.72%" title="Webtext (26k) · 7.1%"></div></div><div class="bval mono">7.1%</div></div><div class="brow"><div class="blabel">Movie reviews (72k)</div><div class="btrack"><div class="bfill" style="width:15.95%" title="Movie reviews (72k) · 8.9%"></div></div><div class="bval mono">8.9%</div></div><div class="brow"><div class="blabel">British National Corpus (6.0M)</div><div class="btrack"><div class="bfill" style="width:22.40%" title="British National Corpus (6.0M) · 12.5%"></div></div><div class="bval mono">12.5%</div></div><div class="brow"><div class="blabel">CHILDES, child-directed speech (2.2M)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="CHILDES, child-directed speech (2.2M) · 55.8%"></div></div><div class="bval mono">55.8%</div></div></div></figure>


Read the top of that chart and Pinker is basically right. Presidential inaugurals repeat themselves 0.8% of the time; the Brown corpus, a deliberately balanced slice of 1960s American printed English, comes in at 2.2%. Ninety-eight percent of the sentences in a general-purpose written corpus occur exactly once, which is a remarkable thing about a system built from a few tens of thousands of words.

Read the bottom of the chart and the claim falls over. In CHILDES — transcribed speech between adults and small children — more than half of all sentences are duplicates. Whatever "virtually every sentence is brand new" describes, it is not what a two-year-old hears.

That gap is doing all the work in this paper, and it is worth being careful about what causes it, because there are at least three candidates and the paper separates none of them.

### Sample size

The first is just arithmetic. Duplicate rate is not a property of a language; it is a property of a sample. Draw more sentences and the chance that any two of them collide goes up, so a corpus of six million sentences will always look more repetitive than a corpus of five thousand, even if the underlying speakers are behaving identically. Inaugural addresses sit at the bottom of that chart partly because there are only 5,395 of them. Ring notes this possibility in his discussion and then compares the corpora anyway.

But size can't be the whole story, and the table says so itself. The BNC has 6.0 million sentences and duplicates 12.5% of the time. CHILDES has 2.2 million — a third as much data — and duplicates 55.8% of the time. Less material, four times the repetition. Something about the register, not the sample, is responsible.

### What counts as a sentence

The second candidate is the one that bothers me most, and the paper does not address it at all: there is no analysis by sentence length, and no mean sentence length reported for any corpus.

This matters enormously. "No." is a sentence. So is "What?" and "Mhm" and "Give me that." Child-directed speech is overwhelmingly made of short utterances; inaugural addresses are made of long periodic ones. Two sentences of three words each have a decent chance of colliding by accident; two sentences of twenty words essentially never do. If you don't condition on length, the duplicate rate you measure is mostly a measurement of your corpus's length distribution wearing the costume of a claim about linguistic creativity.

The popular version of the claim was always explicitly about long sentences. Richard Lederer's rendition in *Language Magazine* cites computer studies finding it would take ten trillion years — two thousand times the age of the Earth — to utter every possible twenty-word English sentence, and concludes that any particular twenty-word sentence is almost certainly new. That is a statement about twenty-word sentences. The corpus test answers a different question, about sentences of any length at all, and the two answers are not comparable.

### The two columns don't line up

There is a third thing in the table I can't make work. Ring reports duplicates two ways: within each text, averaged across texts, and within the whole corpus. For six of the eight corpora the within-text number is *higher* — Brown is 4.3% within-text against 2.2% within-corpus, inaugurals 3.8% against 0.8%.

Under the obvious reading, that's impossible. Pooling a corpus can only add opportunities for two sentences to match, so a pooled rate should never fall below the rate you get looking inside individual texts. Brown's texts are all roughly 115 sentences long, so uneven averaging can't explain a gap that size either.

The reading that would make it consistent is that the "within-corpus" column counts only *cross-text* matches — sentences repeated between documents rather than inside one. That would make the two columns complementary instead of nested, and it would explain the pattern neatly: inaugural addresses repeat themselves internally but rarely echo each other, while caregivers across seven thousand CHILDES transcripts say the same handful of things constantly. I think that's what the numbers mean. The paper doesn't say.


<aside class="fig note"><span class="mono">Note</span><p>Ring&#x27;s paper is an arXiv preprint — submitted September 2025, revised in December, filed under cs.CL, with no journal reference I could find. It also never states whether its percentages count sentence tokens or sentence types: whether a line appearing three times contributes two duplicates or one. That single ambiguity moves every figure in the table, and I could not resolve it from the text.</p></aside>


## The repetition was never in doubt

What makes me think the CHILDES result is real rather than an artifact is that the sub-sentence version of it has been documented for decades by people who were not arguing with Chomsky.

Cameron-Faulkner, Lieven and Tomasello, working on twelve English-speaking mothers in 2003, found that 51% of maternal utterances began with one of just 52 item-based phrases — "Are you…", "I'll…", "Let's…" — and 45% began with one of only 17 words. Biber and colleagues, counting recurrent multi-word bundles in 1999, found that 45% of the words in their conversational corpus occurred inside one, against 21% in academic prose. (I'm taking both figures at second hand — the Cognitive Science paper is paywalled and the Biber number comes via a Cambridge teaching paper that cites it — so treat the decimal places lightly; the direction is what I'd defend.)

So the finding that speech is formulaic is old and well-attested. Ring's contribution is to run it at the whole-sentence level, which is where the famous claim actually lives, and which — astonishingly, for a claim this widely repeated — nobody seems to have done.

## Both things are true at once

Here is the part that reorganised my thinking. Ten years before this preprint, Geoffrey Pullum used the same corpora to argue the exact opposite direction: that linguistic data is desperately *sparse*. Most grammatical word sequences have never occurred anywhere, he wrote — not even most grammatical trigrams — and the probability that any given well-formed string has appeared somewhere in the trillion words of text on the web is approximately zero.

Pullum and Ring are both right, because they are counting different things. The space of possible sentences is so vast that almost all of it is empty. The stream of sentences people actually produce is drawn from a tiny, heavily reused corner of that space. "Virtually every sentence is new" quietly slides between the two: it sounds like a claim about what comes out of people's mouths, and it is argued for with a fact about combinatorics.

The engineers, as usual, ended up measuring this far more carefully than the linguists did, and for entirely unsentimental reasons. When Lee and colleagues deduplicated standard language-model training sets, they found that 4.86% of examples in the One Billion Word Benchmark — which is sentence-level news text — had a near-duplicate elsewhere in the training data, and that one 61-word sentence appeared in C4 over 60,000 times. Their motivation was that duplicated text inflates memorisation and contaminates test sets: 4.60% of C4's validation examples had a near-duplicate in training. Nobody in that paper was thinking about Chomsky. They just needed to know how often English repeats itself, and so they measured it.

What I'd want now is the boring version of Ring's study: one register at a time, sampling frames held constant, duplicate rate plotted against sentence length. My guess is that the curve drops off a cliff somewhere around six or seven words and is indistinguishable from zero past twelve, and that every interesting thing about this question lives on the left-hand side of that graph. Until someone draws it, the honest summary is that the most quoted empirical claim in popular linguistics has one crude test behind it, and that test says: depends who's talking.
