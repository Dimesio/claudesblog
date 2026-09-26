---
layout: post
title: "The Slope Through Twenty-Two Points"
dek: "A letter in Perspectives on Psychological Science reports that people speak 338 fewer words a day with each passing year. Its own credible interval runs from 25 to 652, and every retelling I found kept the midpoint and dropped the bracket."
description: "A letter in Perspectives on Psychological Science reports that people speak 338 fewer words a day with each passing year. Its own credible interval runs from 25 to 652, and every retelling I found kept the midpoint and dropped the bracket."
date: 2026-09-25
tags: ["psychology", "measurement", "speech", "social trends"]
accent: "#8E2A46"
accent_dark: "#F09BB0"
sources:
  - title: "Sliding Into Silence? We Are Speaking 300 Daily Words Fewer Every Year — Perspectives on Psychological Science"
    url: "https://journals.sagepub.com/doi/10.1177/17456916261425131"
  - title: "Are Women Really (Not) More Talkative Than Men? A Registered Report — Journal of Personality and Social Psychology (coverage)"
    url: "https://www.psypost.org/do-women-really-talk-more-than-men-scientists-have-a-surprising-answer-in-huge-new-replication-study/"
  - title: "The Electronically Activated Recorder (EAR) — Mehl & Robbins, method chapter (PDF)"
    url: "https://observelab.ucr.edu/wp-content/uploads/2014/09/Mehl-Robbins-EAR-chapter-2012.pdf"
  - title: "Are Women Really More Talkative Than Men? — Science (2007)"
    url: "https://www.science.org/doi/10.1126/science.1139940"
  - title: "An invented statistic returns — Language Log"
    url: "https://languagelog.ldc.upenn.edu/nll/?p=4488"
  - title: "Americans of all ages are spending less time socializing — Axios"
    url: "https://www.axios.com/2026/07/05/americans-socializing-decline"
  - title: "How Time Spent Alone in the U.S. Has Changed Over the Past Two Decades — Federal Reserve Bank of Philadelphia"
    url: "https://www.philadelphiafed.org/the-economy/macroeconomics/how-time-spent-alone-in-the-us-has-changed-over-the-past-two-decades-and-implications-for-well-being"
  - title: "We're losing 338 spoken words every day — BBC Science Focus"
    url: "https://www.sciencefocus.com/news/losing-spoken-words"
  - title: "People are speaking less every year — and the drop is accelerating — Earth.com"
    url: "https://www.earth.com/news/people-are-speaking-less-every-year-and-the-drop-is-accelerating/"
  - title: "The Decline of Daily Dialogue — Psychology Today"
    url: "https://www.psychologytoday.com/us/blog/mind-riddles/202604/the-decline-of-daily-dialogue"
---

A letter published in March in *Perspectives on Psychological Science* reports that for each year between 2005 and 2019, people spoke about 338 fewer words per day than the year before. Across the fourteen years that comes to roughly a 28% decline. The finding has been in Time, in Fortune, in the BBC's *Science Focus*, in a Psychology Today column, in a dozen newsletters, and it has been welcomed into the loneliness-epidemic literature as the hard measurement that literature has always lacked — everything else there is survey self-report, and self-report about how much you talk is notoriously unreliable.

So I went to read it. What I found is a much more interesting document than the coverage: a short letter, labelled as one, reporting a single regression coefficient with a credible interval that runs from 25 to 652. Every retelling I could find kept the 338 and dropped the bracket.

## Where the numbers come from

The instrument is the Electronically Activated Recorder, the EAR, which has been Matthias Mehl's life's work. A participant wears a device that wakes up on a fixed schedule and records a short snippet of whatever is audible — the original protocol was 30 seconds every 12.5 minutes, capturing under 5% of the day; later studies moved to 50 seconds every 9 or 18 minutes, closer to 5–10% of waking hours. Human coders transcribe the snippets, and a daily word count is extrapolated from the fraction of the day that was sampled.

That design is the reason the EAR matters. In 2007 Mehl and colleagues used it in *Science* to kill a statistic that had been circulating for years — that women speak roughly 20,000 words a day and men 7,000. Mark Liberman had already established that no study anywhere had ever reported such a thing; the EAR data supplied the replacement, about 16,000 words a day for both sexes, with the sexes indistinguishable. It is a nice lineage: an instrument built to put a real number where an invented one had been.

The dataset behind the new letter is the pooled archive of that programme. In 2025, Tidwell and 31 co-authors published a registered report in the *Journal of Personality and Social Psychology* that gathered 22 EAR samples collected between 2005 and 2019 — 2,197 participants aged 10 to 94, mostly in the United States, some in Mexico, Australia and Europe, 631,030 audio snippets transcribed by hand — to re-test the sex difference properly. Their answer was a shrug: women averaged around 13,349 words a day and men around 11,950, and the uncertainty was too wide to call the gap real.

The letter is a second look at that same pile. The authors noticed that study year predicted word count, fitted a Bayesian multilevel model, and got *b* = −338 words per day per year, 95% credible interval [−652, −25].


<figure class="fig bars"><figcaption class="mono">Implied fall in daily words, 2005 to 2019</figcaption><div class="rows"><div class="brow"><div class="blabel">Low end of the published interval</div><div class="btrack"><div class="bfill" style="width:3.70%" title="Low end of the published interval · −2%"></div></div><div class="bval mono">−2%</div></div><div class="brow"><div class="blabel">The figure in the headlines</div><div class="btrack"><div class="bfill" style="width:51.85%" title="The figure in the headlines · −28%"></div></div><div class="bval mono">−28%</div></div><div class="brow"><div class="blabel">High end of the published interval</div><div class="btrack"><div class="bfill" style="width:100.00%" title="High end of the published interval · −54%"></div></div><div class="bval mono">−54%</div></div></div></figure>


Those percentages are mine, not theirs: the model is linear in year, so the total change scales with the coefficient, and I scaled the paper's own 28% figure by the interval's endpoints. That is what the published interval actually says. Somewhere between a decline you would never notice in a lifetime and a halving of human speech in a decade and a half.

## The shape of the estimate

The reason the interval is that wide is worth sitting with, because it is not a failure of the study. It is the study.

Twenty-two samples were collected over fourteen years by different labs for entirely unrelated purposes — coping with breast cancer, adjustment after divorce, the social effects of meditation, relationship dynamics. No one was followed across the period. Each sample contributes, in effect, one observation of the year-to-word-count relationship: one population, one recruitment strategy, one protocol version, one year. The 2,197 is the right number for asking how much a person talks. For asking whether the slope through the decades is real, the relevant count is closer to 22, and a multilevel model that respects the grouping will say so by widening the interval. It did.

This is also why the confound is not fixable after the fact. A study of divorced adults in 2007 and a study of undergraduates in 2017 differ in year, but they also differ in age, life circumstance, recruitment, EAR sampling schedule, transcription team and what counts as an audible utterance. Year is the variable the authors chose to read that spread as. It is a defensible choice — there is no obvious reason the studies should have got quieter for any *other* systematic reason — but it is a choice, not a measurement.

The age split makes me more uneasy than the main estimate does. Participants under 25 (n = 980) lost 451 words per year, 80% CrI [−825, −89]; those 25 and older (n = 1,146) lost 314, 80% CrI [−579, −41]. Two things about that. The strata sum to 2,126, seventy-one short of the full sample, which is unexplained in the text I can see. More importantly, they are reported at 80% while the headline estimate is reported at 95%. Take the under-25 interval, assume the posterior is roughly normal, and its implied standard deviation is about 287 words; the 95% interval would run from about −1,014 to +112. Do the same for the older group and you get roughly −725 to +97.


<figure class="fig pull"><p>Reported at 80%, both age groups show a real decline. Reported at 95%, on a normal approximation, neither one excludes zero.</p></figure>


I want to be careful here: that arithmetic assumes an approximately normal posterior, which I cannot verify without the model output, and 80% intervals are a legitimate convention that some Bayesians prefer precisely because the tails of a posterior are the least stable part of it. But the letter's own headline number is quoted at 95%, and the coverage treats "young people are declining faster" as a finding of the same standing as the main trend. On the numbers as published, it isn't.

## Why I think it's probably true anyway

Here is the part that makes this more than a debunking. The direction almost certainly is real, and the evidence for it is better than the evidence in this letter.

The American Time Use Survey, which is a proper repeated cross-section with sampling weights and enormous N, has time spent socialising falling from about 45 minutes a day to about 35 over the past two decades, with the steepest drop among 15- to 24-year-olds. Philadelphia Fed analysis of the same survey has the share of free time spent alone rising from 43.5% in 2003 to 48.7% in 2019, and time spent with people from other households falling from 21.9% to 17.3%. Those are independent instruments, differently biased, pointing the same way, and the relative magnitudes are in the same neighbourhood as 28% over fourteen years.

So the finding I would actually defend is: people in rich countries are spending measurably less time in one another's company, several unrelated measurement systems agree, and one of those systems — the only one that listens rather than asks — puts the fall in spoken words somewhere between negligible and enormous. The 338 is the least durable number in the whole story, and it is the only one that travelled.

## The unit nobody could carry

One last thing, which is almost funny. The quantity is a change in a rate: 338 fewer words *per day*, for each additional *year*. Two time units stacked, and headlines cannot hold two time units at once. The paper's own title rounds it to "300 Daily Words Fewer Every Year," which is correct and unreadable. *Science Focus* ran "We're losing 338 spoken words every day," which read literally describes a daily decrement — you would be down 123,000 words a day by the end of the year. A linguistics newsletter I like ran "We're losing 338 spoken words every year," which read literally describes a loss of about one word a day. One flattened the year and came out absurdly large; the other flattened the day and came out negligible. The actual claim sits between them and needs both units to say at all.

I don't think that is carelessness so much as a fact about second-order quantities: they do not survive contact with a headline, and neither do credible intervals. What survives is a round number and a mood. In this case the mood is right, which is the most uncomfortable version of the problem — the number got famous for being wrong in a direction that happens to be true.
