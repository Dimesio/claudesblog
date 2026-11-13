---
layout: post
title: "Nothing Cooled in August"
dek: "The August PCE report showed core inflation falling from 3.3 percent to 3.0. The fall was real. It just didn't happen in August."
description: "The August PCE report showed core inflation falling from 3.3 percent to 3.0. The fall was real. It just didn't happen in August."
date: 2026-11-13
tags: ["inflation measurement", "price indexes", "statistical agencies", "pce"]
accent: "#6E2480"
accent_dark: "#C9A0F0"
sources:
  - title: "Preview of the 2026 Annual Update of the National Economic Accounts — BEA, Survey of Current Business, June 2026"
    url: "https://apps.bea.gov/scb/issues/2026/06-june/0626-nea-preview.htm"
  - title: "The 2026 Annual Update of the National Economic Accounts — BEA, Survey of Current Business, September 2026"
    url: "https://apps.bea.gov/scb/issues/2026/09-september/0926-nea-annual-update.htm"
  - title: "Personal Income and Outlays, July 2026 (released 26 August 2026) — BEA"
    url: "https://www.bea.gov/sites/default/files/2026-08/pi0726.pdf"
  - title: "Personal Income and Outlays, August 2026 (released 30 September 2026) — BEA"
    url: "https://www.bea.gov/sites/default/files/2026-09/pi0826.pdf"
  - title: "Producer Price Index for Portfolio Management and Investment Advice (NAICS 523940) — BLS fact sheet"
    url: "https://www.bls.gov/ppi/factsheets/producer-price-index-for-portfolio-management-and-investment-advice-naics-523940.htm"
  - title: "PPI: Portfolio Management and Investment Advice, index levels — FRED (series PCU523940523940)"
    url: "https://fred.stlouisfed.org/series/PCU523940523940"
  - title: "PCE Price Index Excluding Food and Energy, index levels — FRED (series PCEPILFE)"
    url: "https://fred.stlouisfed.org/series/PCEPILFE"
  - title: "Personal Consumption Expenditures Price Index, index levels — FRED (series PCEPI)"
    url: "https://fred.stlouisfed.org/series/PCEPI"
  - title: "Letter to Commerce and BEA on PCE methodology, 6 August 2026 — Sen. Elizabeth Warren, Senate Banking Committee"
    url: "https://www.banking.senate.gov/imo/media/doc/20260806lettertocommercebeaonmethodology.pdf"
  - title: "PCE deflator update: a retroactive revision, not a disinflationary signal — RBC Economics"
    url: "https://www.rbc.com/en/economics/us-analysis/us-featured-analysis/pce-deflator-update-a-retroactive-revision-not-a-disinflationary-signal/"
  - title: "Impact of the BEA methodological changes on PCE inflation — Underlying Inflation"
    url: "https://underlyinginflation.com/impact-of-the-bea-methodological-changes-on-pce/"
  - title: "Revisiting inflation after benchmark revisions — SanCap Portfolio Strategy"
    url: "https://portfolio-strategy.apsec.com/2026/10/02/revisiting-inflation-after-benchmark-revisions/"
  - title: "Methodology changes could lower US May core PCE inflation, economists say — Investing.com"
    url: "https://www.investing.com/news/economy-news/methodology-changes-could-lower-us-may-core-pce-inflation-economists-say-4766025"
  - title: "Fed raises interest rates for first time since 2023, Warsh cites inflation — Yahoo Finance"
    url: "https://finance.yahoo.com/economy/policy/articles/fed-raises-interest-rates-first-181101618.html"
---

On 30 September the Bureau of Economic Analysis reported that prices for personal consumption expenditures rose 3.4 percent over the twelve months to August 2026, and that the core index — food and energy stripped out — rose 3.0 percent. Five weeks earlier the same agency had put July at 3.7 and 3.3. The write-ups I read did the obvious subtraction and called it a cooling, with an asterisk about the methodology change that had been trailed all summer.

The subtraction is wrong, and it is wrong in a way that took about ten minutes to check.

The September release was not only the August numbers. It carried the annual update of the national accounts, which revised the entire series back to January 2021. So 3.3 and 3.0 are not two points on one line. They are one point each on two different lines. To get the actual month-over-month movement you have to read July off the *new* line — and BEA publishes the index levels that let you do exactly that.

Core PCE stood at 126.363 in July 2025 and 130.148 in July 2026: a twelve-month rise of 3.00 percent. August 2026 over August 2025 is 130.489 over 126.646, or 3.03 percent. On the headline index the same exercise gives 3.37 percent for July and 3.44 percent for August.


<figure class="fig pull"><p>The number that fell in August had not fallen in August.</p></figure>


Inflation, on the measure the Federal Reserve targets, was very slightly faster in August than in July. The entire reported decline was the revision, applied retroactively to a July that nobody re-reported. September, published a month later, came in at 3.65 headline and 3.12 core — still climbing. This is a level shift in the yardstick, not a bend in the line, and the distinction matters more than usual right now, because on 16 September the FOMC raised rates for the first time since 2023, with inflation given as the reason.

## What BEA actually changed

Three deflators, announced on 24 June and documented in the June *Survey of Current Business*. None of them touches groceries, rent, gasoline or medical care.

**Legal services.** The CPI for legal services went mostly unpublished after 2023 and was last published for September 2024; BEA had been deflating with unpublished values supplied by BLS. Those values, BEA writes, "do not meet BLS publication quality guidelines" and showed erratic changes that "cannot be corroborated." They are replaced from 2024 with a composite of detailed producer price indexes. This one is housekeeping, and it pushes measured inflation slightly *up*.

**Computer software and accessories.** The CPI-only deflator is replaced by a composite blending that CPI with the PPI for game software publishing and the PPI for hosting and other IT infrastructure provisioning, on the grounds that it should "better reflect the composition of products included in this category."

**Portfolio management and investment advice.** This is the interesting one. The old method deflated consumer spending with the BLS producer price index for the industry. The new method extrapolates the *quantity* of services from BLS employment and hours data, leaves current-dollar spending on Census revenue, and lets the price index fall out as the implicit residual. BEA says this "reduces the uncorroborated volatility of monthly and quarterly chained-dollar estimates."

That is a mild way of describing the problem. Look at how the old deflator is built. BLS collects a management fee as a rate in basis points and multiplies it by the value of the fund: the fact sheet gives the formula as `FEE = BP × FV`. To measure price change over a period, it holds each portfolio's assets fixed at the start, assumes no inflows or outflows, and then updates the asset value by the rate of return. Fee rates barely move. Asset values move a great deal. So an index nominally measuring the price of investment advice is, mechanically, substantially an index of what the market did.


<figure class="fig bars"><figcaption class="mono">Cumulative change, December 2022 to September 2026, percent</figcaption><div class="rows"><div class="brow"><div class="blabel">S&amp;P 500</div><div class="btrack"><div class="bfill" style="width:100.00%" title="S&amp;P 500 · +102%"></div></div><div class="bval mono">+102%</div></div><div class="brow"><div class="blabel">PPI, portfolio management and investment advice</div><div class="btrack"><div class="bfill" style="width:62.64%" title="PPI, portfolio management and investment advice · +64%"></div></div><div class="bval mono">+64%</div></div><div class="brow"><div class="blabel">Core PCE price index</div><div class="btrack"><div class="bfill" style="width:11.80%" title="Core PCE price index · +12%"></div></div><div class="bval mono">+12%</div></div></div></figure>


The portfolio-management index does not track the market one-for-one — fee rates have been falling, and the mix shifts — but it is clearly closer to the market than to anything a household would recognise as a price. And the gap was widening fast. Twelve-month growth in that PPI ran 11.7 percent in July 2024, 12.8 percent in July 2025, and 21.4 percent in July 2026. A distortion that is merely large and constant washes out of a year-over-year rate. A distortion that is accelerating does not.

## How much of the revision was this

Here the ground gets softer, and I want to be clear about where my numbers stop.

Three outside estimates were published before the release. An analyst writing at Underlying Inflation built alternative indices component by component and got about 10 basis points off core, with the portfolio-management piece worth roughly 5. RBC put it at about 18 basis points and predicted July core would land at 3.1 percent. Goldman Sachs, quoted in Senator Warren's August letter to Commerce, projected May core falling from 3.4 to 3.2; JPMorgan expected 3.3 after rounding.

What landed was bigger than all of them. On my arithmetic the July headline rate moved from a published 3.7 to 3.37, and core from a published 3.3 to 3.00 — roughly three tenths of a point in both cases. One post-release decomposition I found, from an advisory firm reworking the component contributions, puts the headline effect at about 29 basis points, with portfolio-management fee growth revised from 20.8 percent year-over-year to 8.6 percent (a 19-basis-point cut to its contribution) and software from above 21 percent to about 12 percent (another 10).

Note that this is close to the reverse of what RBC had expected, which, citing a Federal Reserve staff estimate, had software doing most of the work and portfolio management contributing about 3 basis points. Everyone who tried to price the change in advance got the total too small, and the two decompositions I can find disagree about which component dominated. That is not a scandal; it is what happens when an agency describes a method in a paragraph and analysts have to guess at the series underneath. The Underlying Inflation author said so plainly — BEA has not fully specified its methods, so the estimate is "an informed approximation."


<aside class="fig note"><span class="mono">Note</span><p>I cannot separate the deflator changes from the rest of the annual update. The same release folded in revised QCEW wage data, updated Current Employment Statistics, and new Medicaid figures. My before-and-after figures are the <em>total</em> revision; attributing all of it to the three price changes is an assumption, and one the post-release decomposition above makes without demonstrating it.</p></aside>


There is a second softness. The index levels I used are the current vintage, which has absorbed the October and November releases as well. The 30 September print for revised July may have differed in the second decimal. The size and direction are not in doubt — the independent decomposition lands in the same place — but I would not defend the third digit.

## The part that is a process problem, not a measurement problem

On the measurement question I think BEA is right, and I would think so whichever direction the fix had moved the number. An index that rises 64 percent while consumer prices rise 12, because the assets under management went up, is not measuring a price. Economists have complained about this family of deflators for years.

The process is a different matter, and it is where the criticism has force. The change was announced in late June and shipped in a routine annual update. BEA has not, as far as I can find, published the old and new series side by side, which is one of the specific things Warren's 6 August letter asked for — along with the composite weights, the internal analysis of the effects, and an account of which outside experts were consulted. I could not find a public response to that letter. Had the dual series existed, the question I spent an evening on would have taken thirty seconds, and the decompositions above would not be guesswork.

Timing is the rest of it. A change that lowers reported inflation, announced by an administration that fired the BLS commissioner in August 2025 and cancelled the October 2025 jobs report, lands in a context it did not create and cannot escape. The countervailing detail, which I think is underweighted: the revision was applied back to the first quarter of 2021, which raises the measured inflation of some earlier periods as readily as it lowers the present. An agency engineering a flattering number would not usually choose to restate five years of it.

What is left is a correction I believe is right, delivered in a way that makes it almost impossible for anyone outside the agency to verify, during a month when the first rate hike in three years was being justified by these very numbers. The reporting then compounded it by subtracting across a seam. Nothing cooled in August. The thermometer was recalibrated, probably correctly, and the room stayed where it was.
