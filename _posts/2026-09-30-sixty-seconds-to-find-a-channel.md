---
layout: post
title: "Sixty Seconds to Find a Channel"
dek: "In the FCC's incentive auction, a television station stopped getting cheaper the moment a SAT solver failed to fit it back onto the airwaves. A timeout and a proof of impossibility were deliberately made the same answer — and the difference was paid in cash."
description: "In the FCC's incentive auction, a television station stopped getting cheaper the moment a SAT solver failed to fit it back onto the airwaves. A timeout and a proof of impossibility were deliberately made the same answer — and the difference was paid in cash."
date: 2026-09-30
tags: ["spectrum", "auctions", "sat solvers", "mechanism design"]
accent: "#0E6E8C"
accent_dark: "#66C9E8"
sources:
  - title: "Deep Optimization for Spectrum Repacking — Newman, Fréchette & Leyton-Brown (arXiv preprint of the CACM paper)"
    url: "https://arxiv.org/pdf/1706.03304"
  - title: "Deferred-Acceptance Clock Auctions and Radio Spectrum Reallocation — Milgrom & Segal (JPE working version)"
    url: "https://web.stanford.edu/~isegal/heuristic.pdf"
  - title: "Artificial Intelligence and Market Design: Lessons Learned from Radio Spectrum Reallocation — NBER chapter"
    url: "https://www.nber.org/system/files/chapters/c14942/c14942.pdf"
  - title: "Ownership Concentration and Strategic Supply Reduction — Doraszelski, Seim, Sinkinson & Wang, NBER WP 23034"
    url: "https://www.nber.org/system/files/working_papers/w23034/w23034.pdf"
  - title: "TV Broadcast Incentive Auction: Results and Repacking — Congressional Research Service IF10751"
    url: "https://www.everycrsreport.com/reports/IF10751.html"
  - title: "SATFC source release — FCC GitHub organisation"
    url: "https://github.com/FCC/SATFC"
  - title: "Incentive auction stage 1 fails the final stage rule — RF Venue"
    url: "https://www.rfvenue.com/blog/2016/08/31/incentive-auctions-fail-to-meet-final-stage-rule-reset-to-be-scheduled-at-lower-114-mhz-target"
  - title: "126 MHz clearing target set; reverse auction to begin May 31 — Broadcast Law Blog"
    url: "https://www.broadcastlawblog.com/2016/04/articles/126-mhz-incentive-auction-clearing-target-set-reverse-auction-for-tv-stations-to-bid-to-surrender-their-spectrum-to-wireless-users-to-begin-may-31/"
---

Between May 2016 and January 2017 the FCC ran an auction in which a television station's payout could turn on whether a piece of software found an answer in under a minute. Not on how much the station was worth, not on what its owner bid — on whether a SAT solver, given sixty seconds, could find it a channel to sit on. If the solver found one, the station's price offer kept falling and it had to decide whether to keep declining. If the solver came back empty, the station froze at the price it had reached and became a provisional winner: it would be paid to go dark.

The part that stopped me is that "came back empty" and "ran out of time" were deliberately made the same thing.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">2,990</div><div class="sl mono">stations in the repacking problem</div><div class="sn">UHF and VHF</div></div><div class="stat"><div class="sv">2,575,466</div><div class="sl mono">channel-specific interference constraints</div><div class="sn">in the auction&#x27;s constraint files</div></div><div class="stat"><div class="sv">60 s</div><div class="sl mono">to find a channel</div><div class="sn">per bid-processing check</div></div><div class="stat"><div class="sv">96.03%</div><div class="sl mono">solved inside the limit</div><div class="sn">on the authors&#x27; 10,000-problem test set</div></div></figure>


## The problem underneath

The auction's job was to clear a contiguous block of low-band spectrum — the old UHF television channels — and hand it to mobile carriers. To do that you have to buy some broadcasters off the air and squeeze everyone who stays into a narrower band without anyone interfering with anyone else. That squeezing is the *station repacking problem*: assign every remaining station a channel from its own permitted set such that no pair of stations violates a constraint. It is graph colouring with a very ugly graph, and it is NP-complete.

The graph was not hypothetical. Newman, Fréchette and Leyton-Brown describe roughly 2,990 stations and 2,575,466 channel-specific interference constraints — pairs of the form "station A on channel 38 forbids station B on channel 39." Encoded as a Boolean satisfiability instance for one clearing target, that came to 73,187 variables and 2,917,866 clauses. Not enormous by modern SAT standards. But it had to be re-solved, in a slightly different form, every time the auction considered lowering one station's price — "tens of thousands of times in a single auction," as the paper puts it.

## The rule that made it tractable

The reverse auction was a descending clock. Every participating station started with a large opening offer, and each round the offer to some stations fell. A station that declined an offer *exited* — it kept broadcasting and accepted being repacked. A station whose exit would make the remaining set unpackable could not be allowed to leave, so its clock stopped and it won at that price.

So each check asks: can this station still be fitted in alongside everyone who has already exited? Yes means keep pushing the price down. No means buy it out.

And the third case — the solver neither finding an assignment nor proving that none exists — was collapsed into "no." Milgrom and Segal, who designed the mechanism, state it flatly:

> When the feasibility checker timed out without producing a yes or no answer, the time-out was treated as a no and the price offer for the station was not reduced.

That single convention is what let the FCC put a heuristic, incomplete, best-effort program at the centre of a ten-billion-dollar transfer. Because the checker is only ever allowed to fail in one direction — it can wrongly refuse to lower a price, but it can never wrongly certify a packing that doesn't exist — the auction stays feasible and stays, in their term, *obviously strategy-proof*: a station's best move is to accept any offer above its own value and decline any offer below, and this holds without the owner needing to understand the price rule or trust the FCC to follow it. They also show the mechanism is group strategy-proof, and that winners never have to reveal more about their valuations than the fact that they won.

None of that requires the solver to be good. It requires the solver to be *conservative*. Which means the cost of the solver being bad does not show up as a broken band plan or a gameable auction. It shows up as money.

## Solver performance, denominated in dollars

This is the bit I find genuinely elegant and slightly unnerving. The team built SATFC — a portfolio of eight complementary configured solvers running in parallel on an eight-core box, drawn from a design space of 191 parameters nested up to four levels deep, built on `clasp` and the `SATenstein` local-search framework after screening twenty state-of-the-art SAT solvers.

Two of its tricks are specific to the auction rather than to SAT. The first is that consecutive checks are nearly identical: the previous round's assignment is almost a solution to this round's problem, so SATFC seeds the search with it and only reshuffles the station in question and its interference neighbours. The second is *containment caching*, which exploits a monotonicity that is obvious once stated and powerful in practice: if a set of stations is packable then so is every subset, and if a set is unpackable then so is every superset. Each cached instance therefore answers an exponential family of future queries.

The result: the best single off-the-shelf solver managed 79.96% of a 10,000-instance benchmark within sixty seconds, a naive parallel portfolio of all twenty reached 81.58%, and SATFC got 87.73% in under a second and 96.03% within the minute.

Now translate that. In the FCC's own auction simulations, swapping SATFC for the off-the-shelf `gnovelty+pcl` made the reverse auction cost between 1.22 and 1.45 times more on average, with a comparable increase in economic value destroyed. Over twenty percent, on both counts, from the choice of SAT solver. Somewhere in the accounts of the United States Treasury there is a line item whose size was set by algorithm configuration.

## What the auction actually produced


<figure class="fig bars"><figcaption class="mono">Incentive auction, US$ billions</figcaption><div class="rows"><div class="brow"><div class="blabel">Broadcaster asks, stage 1 at 126 MHz</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Broadcaster asks, stage 1 at 126 MHz · ~$86bn"></div></div><div class="bval mono">~$86bn</div></div><div class="brow"><div class="blabel">Forward-auction bids, stage 1</div><div class="btrack"><div class="bfill" style="width:26.86%" title="Forward-auction bids, stage 1 · 23.1"></div></div><div class="bval mono">23.1</div></div><div class="brow"><div class="blabel">Forward-auction gross, final stage</div><div class="btrack"><div class="bfill" style="width:23.02%" title="Forward-auction gross, final stage · 19.8"></div></div><div class="bval mono">19.8</div></div><div class="brow"><div class="blabel">Paid to broadcasters</div><div class="btrack"><div class="bfill" style="width:11.69%" title="Paid to broadcasters · 10.05"></div></div><div class="bval mono">10.05</div></div><div class="brow"><div class="blabel">Deposited to the Treasury</div><div class="btrack"><div class="bfill" style="width:8.49%" title="Deposited to the Treasury · 7.3"></div></div><div class="bval mono">7.3</div></div><div class="brow"><div class="blabel">Extra paid because checks timed out</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Extra paid because checks timed out · unreported"></div></div><div class="bval mono muted">unreported</div></div></div></figure>


It took four stages to close, with clearing targets descending 126, 114, 108, 84 MHz. Stage 1 is the one worth staring at: at a 126 MHz target, broadcasters collectively wanted about $86 billion to clear out, and the carriers bid $23.1 billion. The gap was roughly the size of the gap between a policy and a fantasy, and the rules required starting over at a lower target. Three stages later, at 84 MHz, 175 stations accepted $10.05 billion, the forward auction grossed $19.8 billion, $7.3 billion went to the Treasury, and nearly a thousand surviving stations were moved to new channels across ten phases over thirty-nine months.

The last bar is the one I wanted most and could not fill. I could not find any published count of how often the live auction's checker hit its sixty-second wall during bid processing, let alone what those particular freezes cost. The FCC released the constraint files and released SATFC itself — it sits in the FCC's own GitHub organisation, last tagged 2.3.1, a fortnight before bidding opened — but the bid-processing logs are a different kind of artefact. The one number that would tell you what the compute budget was worth in dollars appears to be unreported.

## Where this is thinner than it sounds

Almost every quantitative claim about how well the mechanism performed comes from simulations, and the simulations were built by the people who designed the mechanism. The SATFC authors are direct about the limitation: their training instances came from proprietary auction simulations exploring "a very narrow set of answers" about participation and bidder behaviour, and they write that it is "of course impossible to guarantee that variations in the assumptions would not have yielded computationally different problems." The efficiency comparison has a harder ceiling still — the optimal VCG benchmark could only be computed for a restricted 218-station instance around Greater New York, never nationally. The reassuring headline that the clock auction landed within 10% of minimal value loss while costing 24% less than a Vickrey auction is a statement about a model, not a measurement of the event.

And the mechanism's incentive guarantees, real as they are, are guarantees about a single station's single decision. They say nothing about an owner holding twelve stations in one market.


<aside class="fig note"><span class="mono">Note</span><p>Doraszelski, Seim, Sinkinson and Wang estimate that strategic withholding by multi-station owners raised payouts by 13.5% to 42.4% depending on the clearing target. Their own model predicts $2.5 billion at the 84 MHz target against an actual $10.05 billion, partly because they assume full participation where only about 47% of eligible stations took part. Treat the range as a direction, not a size.</p></aside>


That last point matters because it is the failure mode the computer science could not touch. The auction was engineered so that no single bidder could profit by lying about its value, and so that an unsolved SAT instance would cost the public money rather than corrupt the outcome. Both of those are real achievements. Neither of them constrains a group that owns enough of the supply to choose how much of it shows up.

## Why I keep thinking about it

The usual way to describe this auction is that economists designed a clever market and computer scientists made it run fast. I think that gets the relationship backwards. The mechanism was chosen *because* the computation was hopeless: a descending clock with a conservative feasibility oracle was the design that survives having an NP-complete subproblem you cannot solve reliably, and the oracle's failures were routed into the one channel where they do the least damage and the most visible harm — the price.

It is a rare case of a system that is honest about its own incompleteness in a way you can audit, at least in principle. You could, if the logs existed, put a dollar figure on every second of compute the FCC did not buy. I would like to know that number. I suspect nobody computed it, and I am fairly sure nobody published it.
