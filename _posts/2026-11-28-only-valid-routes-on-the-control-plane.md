---
layout: post
title: "Only Valid Routes on the Control Plane"
dek: "Address holders publish signed statements about who may announce their prefixes. A December measurement, taken through strangers' broken tunnels, suggests some big networks filter those routes and forward the packets anyway."
description: "Address holders publish signed statements about who may announce their prefixes. A December measurement, taken through strangers' broken tunnels, suggests some big networks filter those routes and forward the packets anyway."
date: 2026-11-28
tags: ["routing security", "rpki", "bgp", "measurement"]
accent: "#2F5A72"
accent_dark: "#6FB8D8"
sources:
  - title: "TORCH: Characterizing Invalid Route Filtering via Tunnelled Observation — Tian et al., arXiv:2603.29207"
    url: "https://arxiv.org/abs/2603.29207"
  - title: "How we measure: RPKI ROA signing and Route Origination Validation — Geoff Huston, APNIC Blog"
    url: "https://blog.apnic.net/2023/11/09/how-we-measure-rpki-roa-signing-and-route-origination-validation/"
  - title: "Beyond origin validation: Four classes of routing attack nobody is validating — Flavio Luciani, APNIC Blog"
    url: "https://blog.apnic.net/2026/08/26/beyond-origin-validation-four-classes-of-routing-attack-nobody-is-validating/"
  - title: "Helping build a safer Internet by measuring BGP RPKI Route Origin Validation — Cloudflare Blog"
    url: "https://blog.cloudflare.com/rpki-updates-data"
---

To find out whether the internet's networks really discard the routes they claim to discard, a group at Tsinghua University spent eleven days last December sending forged packets through strangers' misconfigured tunnels. The paper is called TORCH, it went up on arXiv at the end of March, and the sentence I just wrote is doing enough work that it's worth taking apart slowly.

The thing being measured is RPKI route origin validation. The internet's routing system has no native idea of who owns what: a network announces "I can reach this block of addresses" and its neighbours believe it. MANRS counted more than 3,000 route leaks and hijacks in 2020 alone, and in June 2019 a leak took Cloudflare's address space away from millions of users for hours. RPKI is the patch. An address holder publishes a cryptographically signed Route Origin Authorisation — a ROA — saying which network number is allowed to originate which prefix. Routers can then check incoming announcements against that and label each one valid, invalid, or unknown.

Labelling is not dropping. The check is called ROV, and whether an invalid route gets thrown in the bin or quietly accepted anyway is a local decision made router by router, by an operator nobody can audit. That gap is the entire subject of this post, and it turns out to be two gaps stacked on top of each other.

## Four numbers, four things

Here is what I find genuinely strange about this field: every few months someone publishes a figure for how far RPKI has been deployed, and the figures do not resemble each other.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">27%</div><div class="sl mono">of networks</div><div class="sn">near-full filtering, Dec 2025</div></div><div class="stat"><div class="sv">20%</div><div class="sl mono">of users</div><div class="sn">on an invalid-dropping path, 2023</div></div><div class="stat"><div class="sv">12.3%</div><div class="sl mono">of networks</div><div class="sn">&quot;full protection&quot;, undated</div></div><div class="stat"><div class="sv">6.5%</div><div class="sl mono">of users</div><div class="sn">ISP drops invalids, Oct 2022</div></div></figure>


None of these contradict each other, because none of them measure the same thing. The 27% is TORCH's: the share of autonomous systems whose forwarding behaviour showed near-complete resilience to invalid routes. The 20% is Geoff Huston's long-running APNIC measurement, which he defines precisely as "the proportion of users that cannot reach a destination if the only viable path to that destination entails following an ROA-invalid route" — and which has sat flat since mid-2020 even as ROA publication climbed. The 12.3% comes from a longitudinal study of 28,000-plus networks cited in a recent survey; the survey quotes it without a date, which is its own small annoyance. The 6.5% is Cloudflare's, from 69.7 million browser probes across 41,531 networks in October 2022, counting only networks that failed to reach an invalid test host at least 95% of the time.

Huston is admirably blunt about what his own method can and cannot say. "So, this is not, in fact, a network measurement but a path measurement," he wrote in 2023. If your ISP does nothing but its transit provider filters, you show up as protected. Cloudflare's version has the mirror-image problem: its probes come from browsers, over short peering-rich paths that often skip the big transit networks entirely, so it sees end-user networks well and upper tiers barely at all. Both are honest about this. Neither headline number carries the caveat when it gets quoted.

## The instrument is itself a security failure

The reason nobody can just measure this directly is that there are almost no invalid routes left to test with. Earlier work on the problem, RoVista, depended on finding prefixes in the wild that were invalid and *only* invalid — and by the time TORCH's authors looked, the usable supply in IPv4 had collapsed to a handful, sometimes two. You cannot characterise 75,000 networks with two probes.

So TORCH went to IPv6 and did something I had to read twice. It scanned for open 6in4 tunnel endpoints — relay points that accept IPv6 packets wrapped inside IPv4 and forward them onward — and found over a million, attributing roughly three-quarters of them to 1,349 networks. The useful ones sit in networks that don't do outbound source-address validation, which means you can send them a packet with a forged source address and they will faithfully inject it into their own network and route it from there. That is a textbook failure of BCP 38, the anti-spoofing hygiene the operator community has been asking networks to implement for a quarter of a century. TORCH turns roughly five thousand of these failures per day into free, globally distributed vantage points, spread across 2,116 networks in 115 countries, 86% of them ISPs.

There is something perfect about measuring the deployment of one routing-security control by exploiting the non-deployment of another.

The second trick is subtler. Normally you'd test reachability by getting a reply from the far end, but an invalid prefix usually has nothing listening. So TORCH runs a traceroute, takes the furthest network that answered as an anchor, and checks whether that anchor appears on a BGP path toward the invalid origin. If it does, the packet was heading there. No cooperative target required.

## Valid in the table, invalid in the wire

Run that across 328 target prefixes — 284 of them exclusively invalid, from 134 origin networks — and 1,685 networks with enough samples to score, and the headline is the abstract's: "about 27% of ASes have achieved nearly full ROV protection." Roughly 30% scored below 0.5, which is a polite way of saying they filter almost nothing.

The transit tier is where it gets uncomfortable. These are the networks whose filtering decisions determine everyone else's exposure, and the spread is enormous.


<figure class="fig bars"><figcaption class="mono">Share of invalid prefixes the network would not reach, Dec 2025</figcaption><div class="rows"><div class="brow"><div class="blabel">Level 3, AS3356</div><div class="btrack"><div class="bfill" style="width:40.57%" title="Level 3, AS3356 · 40.2%"></div></div><div class="bval mono">40.2%</div></div><div class="brow"><div class="blabel">Arelion, AS1299</div><div class="btrack"><div class="bfill" style="width:50.45%" title="Arelion, AS1299 · 50.0%"></div></div><div class="bval mono">50.0%</div></div><div class="brow"><div class="blabel">Hurricane Electric, AS6939</div><div class="btrack"><div class="bfill" style="width:52.88%" title="Hurricane Electric, AS6939 · 52.4%"></div></div><div class="bval mono">52.4%</div></div><div class="brow"><div class="blabel">TATA, AS6453</div><div class="btrack"><div class="bfill" style="width:72.05%" title="TATA, AS6453 · 71.4%"></div></div><div class="bval mono">71.4%</div></div><div class="brow"><div class="blabel">NTT, AS2914</div><div class="btrack"><div class="bfill" style="width:91.62%" title="NTT, AS2914 · 90.8%"></div></div><div class="bval mono">90.8%</div></div><div class="brow"><div class="blabel">Orange, AS5511</div><div class="btrack"><div class="bfill" style="width:97.28%" title="Orange, AS5511 · 96.4%"></div></div><div class="bval mono">96.4%</div></div><div class="brow"><div class="blabel">AT&amp;T, AS7018</div><div class="btrack"><div class="bfill" style="width:99.60%" title="AT&amp;T, AS7018 · 98.7%"></div></div><div class="bval mono">98.7%</div></div><div class="brow"><div class="blabel">Deutsche Telekom, AS3320</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Deutsche Telekom, AS3320 · 99.1%"></div></div><div class="bval mono">99.1%</div></div></div></figure>


Deutsche Telekom at 99.1% and Level 3 at 40.2% are not two points on a gradual adoption curve. They are two different answers to the question of whether this is a thing you do.

And then the finding that actually changed how I think about the problem. In one case study, a prefix announced by two different networks — one authorised, one not — stayed reachable at the invalid origin more than 88% of the time, with about 68% of the observed traffic flowing to the wrong origin through a single Tier-1. Something like 845 downstream networks inherited that path. The part I keep turning over is that several of these transit networks appear to have had only valid routes in their control plane. Their routing table was clean. Their packets went to the invalid origin anyway.

That is a different failure from not deploying ROV. A router that advertises a filtered table while forwarding along an unfiltered path defeats every measurement method built on asking the control plane what it knows — and it means an operator can look at their own BGP table, see nothing invalid, and be wrong about what their network is doing.

### Where I'd push back

The per-network table above is the paper's Table 2, and I should say plainly that I read the abstract, introduction and methodology closely and took the results tables as reported; I ran the extraction twice from two different renderings of the paper and got identical figures, which is reassurance but not the same as having checked the plots myself.

More substantively: TORCH's score measures *resilience*, not deployment. A network can score 1.0 because its own routers filter, or because every upstream it buys from does the filtering for it. Those are very different security postures, and the metric cannot tell them apart — the same conflation Huston flagged in his own method. The authors cross-checked against APNIC's measurement on 686 networks and the two agreed on 85.4%; of the 100 disagreements, 83 were networks APNIC called unprotected that TORCH saw filtering, and in 71 of those the network specifically failed to drop Cloudflare's invalid test prefix. Read charitably, that's TORCH catching networks that filter broadly but miss one route. Read less charitably, it's two methods that disagree one time in seven, and no ground truth to appeal to.

The vantage points are also only where broken tunnels happen to be, which the authors concede leaves Africa and Oceania thin. Attribution depends on prefix-to-network mapping datasets that go stale. And this is IPv6; the method generalises in principle, but the numbers above are not IPv4 numbers.

> Coverage is not enforcement — and enforcement in the table is not enforcement in the wire.

The first half of that is Flavio Luciani's phrase, from a survey arguing that the attacks RPKI was built for are now a minority of the ways routing breaks. The second half is what I take from TORCH, and it's the part that worries me more, because the whole architecture of routing security assumes you can reason about forwarding from the control plane. Mostly you can. Roughly 845 networks spent last December finding out about the exception.
