---
layout: post
title: "None of Those Mailboxes Were Monitored"
dek: "At 4:49 one morning in March 2022, one or two people in Hong Kong switched off the London Metal Exchange's price bands and emailed London to say so. The £9.2m fine that arrived three years later was not for switching them off — it was for never having written down when they were allowed to."
description: "At 4:49 one morning in March 2022, one or two people in Hong Kong switched off the London Metal Exchange's price bands and emailed London to say so. The £9.2m fine that arrived three years later was not for switching them off — it was for never having written down when they were allowed to."
date: 2026-10-05
tags: ["market structure", "commodities", "circuit breakers", "financial regulation"]
accent: "#3C5566"
accent_dark: "#9FBDD0"
sources:
  - title: "Final Notice: The London Metal Exchange — Financial Conduct Authority, 20 March 2025"
    url: "https://www.fca.org.uk/publication/final-notices/london-metal-exchange-2025.pdf"
  - title: "First FCA enforcement action and fine against a Recognised Investment Exchange — FCA press release"
    url: "https://www.fca.org.uk/news/press-releases/first-fca-enforcement-action-and-fine-against-recognised-investment-exchange"
  - title: "LME response to FCA Final Notice — London Metal Exchange"
    url: "https://www.lme.com/en/news/press-releases/2025/lme-response-to-fca-final-notice"
  - title: "Independent Review of Events in the Nickel Market in March 2022, Final Report — Oliver Wyman for the LME"
    url: "https://www.lme.com/-/media/Files/Trading/New-initiatives/Nickel-independent-review/Independent-Review-of-Events-in-the-Nickel-Market-in-March-2022---Final-Report.pdf"
  - title: "Bank of England announces supervisory action on LME Clear — Bank of England, 3 March 2023"
    url: "https://www.bankofengland.co.uk/news/2023/march/boe-announces-supervisory-action-on-lme-clear"
  - title: "Central Clearing and Trade Cancellation: The Case of LME Nickel Contracts on March 8, 2022 — Office of Financial Research, working paper 24-09"
    url: "https://www.financialresearch.gov/working-papers/files/OFRwp-24-09_central-clearing-and-trade-cancellation.pdf"
  - title: "The English Court of Appeal upholds dismissal of LME nickel crisis claims — Freshfields"
    url: "https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/the-english-court-of-appeal-upholds-dismissal-of-lme-nickel-crisis-claims-102jm2t"
  - title: "Announcement: claim filed at the UK Competition Appeal Tribunal — HKEX, 8 September 2026"
    url: "https://www1.hkexnews.hk/listedco/listconews/sehk/2026/0908/2026090800216.pdf"
  - title: "FCA LME fine highlights disorderly market control weaknesses — Clifford Chance briefing"
    url: "https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2025/04/fca-lme-fine-highlights-disorderly-market-control-weaknesses.pdf"
  - title: "FCA imposes £9.2 million fine on London Metal Exchange for market disorder — Mishcon de Reya"
    url: "https://www.mishcon.com/news/fca-imposes-92-million-fine-on-london-metal-exchange-for-market-disorder"
  - title: "Systems error triggers fresh chaos as LME suspends nickel trading once again — CNBC, 16 March 2022"
    url: "https://www.cnbc.com/2022/03/16/metals-lme-suspends-nickel-trading-once-again-on-systems-error.html"
---

The clause that made me stop and reread is seven words long: *"none of those mailboxes were monitored overnight."* It sits in the Financial Conduct Authority's final notice to the London Metal Exchange, published in March 2025 — three years after the LME suspended its nickel market, cancelled eight hours of trades, and became the most litigated exchange in Europe.

Here is what the notice says happened. Between 1:00am and 7:30am London time, the LME's electronic order book was watched from Hong Kong by a Trading Operations team that was "usually a team of two, but sometimes a single individual if the other team member was on leave." Their main instrument for keeping the market orderly was a pair of automatic volatility controls called price bands. The dynamic band was a narrow channel around a reference price that adjusted with each new order and simply refused anything outside it; the static band was five times wider, re-anchored hourly, and let price formation continue while blocking bids above its ceiling. Each came in three settings — normal, wide and wider, the last being twice the normal width. For nickel on 7 March, the dynamic band's *widest* available setting was $470, and the static band's, at five times that, $2,350.

On 7 March 2022, between roughly 1:47am and 2:04am, the Hong Kong team pushed nickel's static band past its widest preset, from $2,350 to $6,000. By 7:16am the three-month price was up 28 per cent at $37,000. Through the day the London team suspended and reapplied the bands repeatedly. Nobody called a senior manager, because nobody thought this was the sort of thing you called a senior manager about — suspending the bands was, in the notice's phrase, one of the team's "established practices for aiding price discovery."

At 4:49am on 8 March the Hong Kong team switched both bands off altogether. At 5:04am they sent the standard notification: an email to an internal distribution list. Between 5:44am and 6:08am, with nothing in the order book's way, nickel went from $70,000 to $101,365 — double that morning's opening price, and more than triple Monday's opening price of $29,770. By 6:33am it was back at $80,010. At 8:15am the market was suspended. LME senior management learned that the price bands had been off for three and a half hours at some point on 9 March.


<figure class="fig bars"><figcaption class="mono">Price move the control could absorb, $ per tonne</figcaption><div class="rows"><div class="brow"><div class="blabel">Dynamic band, widest preset</div><div class="btrack"><div class="bfill" style="width:1.50%" title="Dynamic band, widest preset · $470"></div></div><div class="bval mono">$470</div></div><div class="brow"><div class="blabel">Static band, widest preset</div><div class="btrack"><div class="bfill" style="width:7.49%" title="Static band, widest preset · $2,350"></div></div><div class="bval mono">$2,350</div></div><div class="brow"><div class="blabel">Static band as reset on 7 March</div><div class="btrack"><div class="bfill" style="width:19.13%" title="Static band as reset on 7 March · $6,000"></div></div><div class="bval mono">$6,000</div></div><div class="brow"><div class="blabel">Actual move, 5:44–6:08am on 8 March</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Actual move, 5:44–6:08am on 8 March · $70,000 → $101,365"></div></div><div class="bval mono">$70,000 → $101,365</div></div></div></figure>


## Three breaches, all of them paper

What the LME was actually fined for is stranger than that narrative suggests. Not for suspending the bands. Not for the cancellation, which the notice does not criticise at all. Not for failing to see the positions that caused the squeeze; on that point the notice is close to exculpatory, recording that "very large positions held mainly on the Over the Counter (OTC) market were highly material to the extraordinary speed and extent of the price rises" and that the LME "did not have visibility of these positions at the time," and then making no finding of breach about it.

The breaches are three and they are all documentary. Under REC 2.5.1(3), systems and controls that were not "adequate, effective and appropriate to ensure orderly trading under conditions of severe market stress." Under Article 18(3) of RTS 7, a failure to set out internal policies and arrangements for the static bands and for the circumstances in which either band could be suspended. Under Article 18(4), a failure to publish them.

The Relevant Period runs from 3 January 2018 to 8:15am on 8 March 2022, and the start date is not arbitrary. 3 January 2018 is the day MiFID II made automatic volatility mechanisms mandatory for electronic trading venues. On the FCA's account the LME was in breach from the first morning the obligation existed, for four years and two months, and the breach consisted of never having written down the answer to the question *when are we allowed to turn these off?*

An internal LME incident report in October 2021 had already noticed the practice — bands suspended during volatility in tin and copper — and flagged it as an operational risk, on the narrow ground that with the bands off nothing stood between the order book and a fat-finger trade or a runaway algorithm. No corrective action followed. The FCA's sharpest observation is that this framing was the defect: the Trading Operations team held "an unduly narrow view of market disorder," confined to error trades and rogue algorithms, and so could not see that a market may be disorderly while every single order in it is deliberate and correctly entered.

## Four inquiries, four different failures

Four bodies have now produced an account of March 2022, and what strikes me is how little they overlap.

Oliver Wyman's independent review, published in January 2023, puts the cause in position monitoring: two very large short positions fragmented across as many as twelve members and both venues, roughly 52 per cent of the large positions held over the counter where the LME could not see them, and regulatory position limits set at 80,200 lots across prompt dates — high enough that, as the review notes, none of the largest nickel positions in March 2022 would have breached them. Its terms of reference explicitly excluded the LME Group's own decision-making and governance.

The Bank of England, in March 2023, found shortcomings in the governance, management independence and risk management of LME Clear — the clearing house, not the exchange — and appointed a skilled person under section 166 to monitor the remediation.

The FCA took the exchange's systems and controls, and nothing else.

The courts took only the cancellation. The Divisional Court dismissed Elliott's and Jane Street's judicial review in November 2023, the Court of Appeal upheld that in October 2024, and the Supreme Court refused permission to appeal on the ground that it raised no arguable point of law. Elliott had claimed around $456 million, Jane Street about $15 million.

Each answered the question inside its own remit, competently. The question that interests me — whether a market with documented circuit breakers and visible positions would ever have needed either the suspension or the cancellation — sits in the gaps between the four, and nobody had the mandate to ask it.

## What the fine does not establish

Here the story is weaker than its headline, and the LME's own response makes the point better than I can: there is, it notes, "no finding by the FCA that the price bands were capable of preventing the underlying market disorder in March 2022." That is accurate and it matters. The fine establishes that a control was undocumented and misunderstood. It does not establish that the control, correctly operated, would have held. The FCA says so itself — it "did not need to expressly opine" on whether the bands would have been sufficient had they worked as intended.

There is a reason to doubt it. Both bands were anchored to reference prices that moved with the market, so against a sustained squeeze they slow a move rather than cap it — which is presumably why the LME's post-event fix was not better bands but hard daily limits, 12 per cent on aluminium and copper and 15 per cent on everything else, plus mandatory weekly OTC position reporting.

The counterfactual on the other side is weaker still. The case for cancelling rests entirely on the claim that the alternative was a cascade of clearing-member defaults.


<aside class="fig note"><span class="mono">Note</span><p>That cascade — seven members failing, then twelve of forty-five — comes from the LME&#x27;s own filings in the litigation it was defending. The Office of Financial Research paper that works through it says plainly that it cannot be verified, because the intervention is what stopped it happening. I could not find an independent reconstruction anywhere.</p></aside>


The 2024 OFR working paper assembles what can be assembled. LME Clear's margin breach volume in the first quarter of 2022 was $23.3 billion, two orders of magnitude above prior quarters, and one account breached by $2.0 billion against a default fund of $1.1 billion. Those figures are published. The cascade is not: the LME's filings put the unissued intraday call at $19.75 billion, forcing seven of forty-five clearing members into default with losses near $2.6 billion, of which $220 million would have exceeded prefunded resources, and replenishment calls then threatening five more. Against that, the cancellation erased roughly $1.3 billion of profit and loss between the parties to somewhere between five and nine thousand trades. The fine was £9,245,900 — £13.2 million before a 30 per cent settlement discount, itself built up from 10 per cent of LME revenue on the relevant contracts. Set beside $1.3 billion it is well under one per cent, whichever currency you count in.

## The argument is still running

On 3 September 2026, Elliott filed a fresh claim against HKEX and the LME at the UK Competition Appeal Tribunal, this time under Chapter II of the Competition Act 1998: abuse of a dominant position. The conduct alleged, per HKEX's own announcement to the Hong Kong exchange five days later, includes failing to have arrangements in place to prevent disorderly trading and to monitor volatility in nickel futures.

Having lost the argument that the LME had no power to cancel, the claimants are now running the argument that it should never have arrived at a morning where cancelling was the only move left. And the FCA's final notice is, conveniently, a regulator's own finding that something very close to that was true for four years and two months. HKEX says the claim is without merit and will be contested vigorously; no damages figure is stated, and the Tribunal would have to assess one.

Whether a competition claim can be built on top of a systems-and-controls finding, I have no idea, and I would not bet either way. What stays with me is smaller and more concrete: a control whose loosest setting was $470 standing in front of a move of more than $30,000, switched off by one or two people on a night shift whose escalation procedure was an email to a list that nobody read until the following day. Everything downstream of 4:49am — eight days of closed market, a systems error that halted nickel again on the first morning it reopened, $1.3 billion of unwound trades, three courts, two regulators, a consultancy and a claim still live in 2026 — followed from a question that nobody at the exchange had ever been required to write an answer to.
