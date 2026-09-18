---
layout: post
title: "The Leap Hour Nobody Will Have to Insert"
dek: "In October, sixty-four countries vote to stop correcting UTC for the Earth's rotation and let the two drift apart by up to a full hour. The fix works because the bill does not come due until roughly the year 3000."
date: 2026-09-16
tags: ["timekeeping", "standards", "infrastructure", "earth rotation"]
accent: "#A23B2E"
accent_dark: "#F0A57F"
sources:
  - title: "Draft Resolutions for the 28th meeting of the CGPM (Draft Resolution C) — BIPM"
    url: "https://www.bipm.org/documents/20126/284836054/CGPM-2026-Draft-Resolutions.pdf"
  - title: "Report from the CCTF on Draft Resolution C — BIPM"
    url: "https://www.bipm.org/documents/20126/284836054/CCTF-report-on-Draft-Resolution-C.pdf"
  - title: "Resolution 4 of the 27th CGPM (2022), on the use and future development of UTC — BIPM"
    url: "https://www.bipm.org/en/cgpm-2022/resolution-4"
  - title: "28th meeting of the CGPM, 13–15 October 2026 — BIPM"
    url: "https://www.bipm.org/en/cgpm-2026"
  - title: "A global timekeeping problem postponed by global warming (Agnew, 2024) — Nature"
    url: "https://www.nature.com/articles/s41586-024-07170-0"
  - title: "Bulletin C 72, 6 July 2026 — IERS"
    url: "https://datacenter.iers.org/data/latestVersion/bulletinC.txt"
  - title: "International timekeepers to vote on changing the leap second to a leap hour — Scientific American"
    url: "https://www.scientificamerican.com/article/international-timekeepers-to-vote-on-changing-the-leap-second-to-a-leap-hour/"
  - title: "It's time to leave the leap second in the past — Engineering at Meta"
    url: "https://engineering.fb.com/2022/07/25/production-engineering/its-time-to-leave-the-leap-second-in-the-past/"
  - title: "How Precision Time Protocol handles leap seconds — Engineering at Meta"
    url: "https://engineering.fb.com/2025/02/03/production-engineering/how-precision-time-protocol-ptp-handles-leap-seconds/"
  - title: "Leap Smear — Google Public NTP"
    url: "https://developers.google.com/time/smear"
  - title: "Leap seconds (Markus Kuhn) — University of Cambridge Computer Laboratory"
    url: "https://www.cl.cam.ac.uk/~mgk25/time/leap/"
  - title: "Controversial 'negative' leap seconds to be ditched in favor of a rare leap hour — New Atlas"
    url: "https://newatlas.com/technology/leap-seconds-history/"
  - title: "Earth Rotation Records Spur October Vote to Avert Negative Leap Second — Tech Times"
    url: "https://www.techtimes.com/articles/320185/20260711/earth-rotation-records-spur-october-vote-avert-negative-leap-second.htm"
  - title: "Leap seconds are set to end May 20, 2027 — lilting channel"
    url: "https://lilting.ch/en/articles/leap-second-abolition"
  - title: "Shortest day measured in the atomic-clock era, 1.66 ms — ScienceBlog"
    url: "https://scienceblog.com/m-on-5-july-2024-earth-completed-a-rotation-1-66-milliseconds-short-of-86-400-seconds-the-shortest-day-measured-in-the-atomic-clock-era-breaking-the-previous-record-set-in-june-2022/"
---

For fifty-four years, Coordinated Universal Time has only ever been corrected in one direction. Twenty-seven times since 1972 the world has been told to insert an extra second — 23:59:60, a minute with sixty-one seconds in it — because the Earth had fallen a little behind the atomic clocks. The correction has never once gone the other way. In October, sixty-four countries will vote on a proposal designed to make sure it never does.

The instrument is Draft Resolution C for the 28th General Conference on Weights and Measures, which meets at Versailles from 13 to 15 October. Its title is *On the technical actions needed to ensure the continuity of UTC*, and its operative content is two numbers: the maximum permitted value of the difference between UT1 and UTC becomes 3,600 seconds, and continuous UTC takes effect on 20 May 2027. UT1 is time as told by the Earth's actual rotation. UTC is time as told by caesium. The rule since 1972 has kept them within 0.9 seconds of each other. The new rule keeps them within an hour.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">3600 s</div><div class="sl mono">the new UT1−UTC limit</div><div class="sn">up from 0.9 s</div></div><div class="stat"><div class="sv">20 May 2027</div><div class="sl mono">continuous UTC begins</div><div class="sn">if the vote passes</div></div><div class="stat"><div class="sv">30%</div><div class="sl mono">risk of a negative leap second</div><div class="sn">by 2035, per the CCTF</div></div><div class="stat"><div class="sv">0</div><div class="sl mono">negative leap seconds ever applied</div><div class="sn">in 54 years</div></div></figure>


What I find interesting here is not that the leap second is being retired. That has been coming since at least 2015, when the ITU punted the decision to a later conference, and it was formally scheduled in 2022, when the 27th CGPM resolved that the limit "will be increased in, or before, 2035." What is interesting is that the deadline moved forward by eight years, and the reason it moved is a risk estimate rather than a failure.

## The hurry is about a thing that has not happened

The Earth is currently running fast. Not consistently, and not by much — the shortest day yet measured in the atomic-clock era came in about 1.66 milliseconds under 86,400 seconds, in early July 2024, with more sub-86,400-second days through July 2025. Sources I read disagree about whether the record day was the 4th or the 5th of July, which tells you something about how this gets reported downstream. The direction, though, is not in dispute: for the last few years UT1 has been gaining on UTC rather than losing to it, which is why there has been no leap second since the end of 2016 and why IERS Bulletin C, issued on 6 July this year, again announced none for December.

Keep that up and the difference eventually crosses 0.9 seconds on the wrong side, and the IERS has to announce a *negative* leap second: 23:59:58 followed directly by 00:00:00, a minute with fifty-nine seconds in it.

Duncan Agnew's 2024 paper in *Nature* is the piece of this I most enjoyed. He separated two things pushing on the Earth's spin. The liquid core has been slowing at a steady rate since 1972, which speeds up the rest of the planet — that is the long trend making a negative leap second plausible at all. Working against it, meltwater from Greenland and Antarctica is redistributing mass away from the poles, which slows the planet down. His conclusion is that the melt has pushed the first negative leap second from roughly 2026 out to roughly 2029. Global warming bought timekeeping three years.

I want to be straight about my footing: the full paper is behind Nature's paywall and I am working from the abstract and secondary coverage, so I have the headline result and not the error bars on it.

The CCTF's own report puts the probability of a negative leap second at roughly 30% within the next decade if nothing changes, against about 50% for a positive one. Patrizia Tavella, who runs the BIPM's Time Department, is quoted in *Scientific American* saying they consulted the people who would have to implement it: "We estimated that if we wait till 2035, we have 30 percent risk of a negative leap second…even 10 percent risk is too much."

## Why one second backwards is worse than one second forwards

It is not obvious, from the outside, why subtracting a second should be scarier than adding one. Both are one-second discontinuities in a supposedly uniform time scale.

The answer is that adding one has been done twenty-seven times and subtracting one has been done zero times, and all the code that matters was written by people who had only seen the first case. Meta's engineering team put it plainly when they came out against leap seconds in 2022: "The impact of a negative leap second has never been tested on a large scale; it could have a devastating effect on the software relying on timers or schedulers." The CCTF report itself relays an industry assessment that preparing for one "could be as demanding as preparation for the millennium Y2K bug."

That comparison is doing something specific, and I think it is fair. Y2K was not frightening because the arithmetic was hard. It was frightening because the assumption was everywhere, unlabelled, in code nobody had read in fifteen years. "A minute has sixty seconds, except sometimes sixty-one" is an assumption a lot of systems have been forced to confront. "A minute sometimes has fifty-nine" is an assumption almost nothing has ever been asked about.

## Choosing the ceiling

The committee considered three options for the new limit: one minute, one hour, or no fixed limit at all.


<figure class="fig bars"><figcaption class="mono">Maximum UT1−UTC allowed under each option, seconds · log scale</figcaption><div class="rows"><div class="brow"><div class="blabel">Rule in force since 1972</div><div class="btrack"><div class="bfill" style="width:1.50%" title="Rule in force since 1972 · 0.9 s"></div></div><div class="bval mono">0.9 s</div></div><div class="brow"><div class="blabel">Option considered: one minute</div><div class="btrack"><div class="bfill" style="width:50.00%" title="Option considered: one minute · 60"></div></div><div class="bval mono">60</div></div><div class="brow"><div class="blabel">Draft Resolution C: one hour</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Draft Resolution C: one hour · proposed"></div></div><div class="bval mono">proposed</div></div><div class="brow"><div class="blabel">Option considered: no fixed limit</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Option considered: no fixed limit · no number attached"></div></div><div class="bval mono muted">no number attached</div></div></div></figure>


They landed on an hour, on the grounds that it "will ensure the long-term continuity of UTC for several centuries," and the resolution instructs the BIPM to work with the ITU, IAU, IUGG and IERS on monitoring and on explaining the change. Formal statements of support came from ITU-T, ITU-R Working Party 7A, IEEE-1588 and the IERS. Institutionally, there is not much of a fight here.

## The part I keep turning over

Draft Resolution C sets a ceiling. It does not say what happens when the ceiling is reached.

That is a defensible omission if the ceiling is far enough away, and it probably is. But "several centuries" is a soft phrase for a document whose whole purpose is replacing a soft procedure with a hard number, and the published estimates do not agree with each other.

### A back-of-envelope, clearly labelled as mine

Tidal braking lengthens the day by something like 1.7 milliseconds per century. If you start from roughly zero excess today and let that accumulate, the gap between UT1 and UTC grows as the square of elapsed time, and you get to 3,600 seconds in something like eleven centuries — call it the year 3100. That is my arithmetic from a sourced rate, not a published figure, and it is sensitive to assumptions I am guessing at. Markus Kuhn, who has followed this argument for decades, wrote that the first leap hour would fall in the 27th century. The CCTF says several centuries. Those are all in the same family and none of them is a number you would bet a procedure on.

Kuhn's objection to the leap hour itself is sharper, and I have not seen it answered: a leap hour is "3600 times more disruptive than a leap second," and inserting one would be "a very major discontinuity in what is meant to be a uniform time scale." If a one-second step is dangerous enough to abolish in 2027, a one-hour step is not a solution to it. It is the same problem, scaled up by three and a half orders of magnitude, and handed to people who will have no living memory of anyone doing it.

The honest reading, I think, is that nobody expects the leap hour to ever be inserted. UTC will be redefined again long before the year 3000 — Draft Resolution B at the same conference is already about the future redefinition of the second itself. The hour is not a plan. It is a number large enough to make the limit formally exist while being practically unreachable, which is a reasonable thing for a standards body to do and a slightly strange thing to describe as ensuring continuity.

## What genuinely gets better

One thing I did not expect to find is how much mess this clears up in the meantime.

Because leap seconds break things, the large operators stopped applying them as specified and started smearing instead — spreading the extra second over hours so no clock ever steps. Google smears linearly over 24 hours, noon to noon, a frequency change of about 11.6 parts per million. Others chose different windows and different curves. Meta's engineers note that their NTP path uses a quadratic smear while their PTP path uses a linear one, and that timestamps taken from the two during a smear can disagree by over 100 microseconds. Meta also cannot join the public NTP pools, because the pools do not smear and Meta does.

So the current situation is not one time scale with an occasional discontinuity. It is several mutually inconsistent time scales that agree except during the days when precision matters most. Continuous UTC deletes that whole category of problem. Nobody needs a smear for a correction that never comes.

## What I could not pin down

The 30% figure is the load-bearing number in this entire decision, and I found it stated in the CCTF report and quoted by Tavella but did not find the stochastic model behind it — what data window, what assumptions about core angular momentum, how the ice-melt term from Agnew's work is carried in. A probability that moved an international deadline eight years earlier deserves to be legible, and it may well be, in a document I did not reach.

The other thing I would want, and could not find, is any published account of what a leap hour would actually consist of operationally. Not when — how. Given that the resolution's justification is that abrupt one-second changes endanger critical infrastructure, the absence of a procedure for the abrupt 3,600-second change is the most interesting silence in the document.
