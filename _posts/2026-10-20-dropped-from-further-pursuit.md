---
layout: post
title: "Dropped From Further Pursuit"
dek: "Tin extrudes conductive filaments out of solid metal at room temperature, nobody can predict when, and the two communities most exposed to it have read the same missing data in opposite directions."
description: "Tin extrudes conductive filaments out of solid metal at room temperature, nobody can predict when, and the two communities most exposed to it have read the same missing data in opposite directions."
date: 2026-10-20
tags: ["metallurgy", "electronics reliability", "regulation", "risk assessment"]
accent: "#9E2B1B"
accent_dark: "#F0917A"
sources:
  - title: "Basic Info on Tin Whiskers — NASA Goddard NEPP"
    url: "https://nepp.nasa.gov/whisker/background/"
  - title: "Tin Whisker Failures — NASA Goddard NEPP"
    url: "https://nepp.nasa.gov/whisker/failures/"
  - title: "Issue 200: Tin Whiskers (NUREG-0933) — US Nuclear Regulatory Commission"
    url: "https://www.nrc.gov/sr0933/section-3-new-generic-issues/issue-200-tin-whiskers"
  - title: "How the Risk of Tin Whiskers Affects Design Decisions — Pecht, Osterman, Tinsley & Lu, IEEE Access 13 (2025)"
    url: "https://ira.lib.polyu.edu.hk/bitstream/10397/115982/1/Pecht_How_The_Risk.pdf"
  - title: "Assessing the Risk Posed by Tin Whiskers — CALCE, University of Maryland (SMTA)"
    url: "https://web.calce.umd.edu/lead-free/SMTAOnline.pdf"
  - title: "Metal Whiskering: Tin, Zinc, and Cadmium — Leidecker & Brusse, NASA"
    url: "https://nepp.nasa.gov/whisker/reference/tech_papers/2007-Leidecker-Metal-Whiskering.pdf"
  - title: "Surface-Energy-Driven Tin Whisker Growth on Pure Tin — Liu et al., Crystals 13(12):1643 (2023)"
    url: "https://www.mdpi.com/2073-4352/13/12/1643"
  - title: "Dominion Learns Big Lesson From A Tiny 'Tin Whisker' (2005) — hosted by NASA NEPP"
    url: "https://nepp.nasa.gov/whisker/reference/tech_papers/2005-dadonna-nuclear-reactor-shutdown.pdf"
  - title: "Directive 2011/65/EU, Article 2 (Scope) — legislation.gov.uk"
    url: "https://www.legislation.gov.uk/eudr/2011/65/article/2/adopted"
  - title: "Restriction of Hazardous Substances Directive — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Restriction_of_Hazardous_Substances_Directive"
  - title: "Galaxy IV — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Galaxy_IV"
---

A tin-plated surface left alone in a drawer at room temperature will sometimes extrude a single crystal of tin out of itself. The filament is a couple of microns across — occasionally more than ten, rarely under a hundred nanometres — and given a few years it reaches millimetres. Nothing heats it. Nothing applies a field. Nothing is moving. The plating simply grows a conductive wire into the space beside it, and if that wire touches an adjacent conductor you have a short circuit that appears in nobody's schematic.

I knew "tin whiskers" as electronics folklore — the thing experienced engineers mutter about when someone specifies a lead-free finish. What I had not understood until I went through the primary material is how thin the quantitative floor under the whole subject is, and that the thinness cuts both ways. The people who treat whiskers as an unquantifiable existential threat and the people who treat them as a solved non-problem are reasoning from the same missing dataset.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">0.03–9 mm/yr</div><div class="sl mono">reported growth rates</div><div class="sn">same material class</div></div><div class="stat"><div class="sv">4</div><div class="sl mono">satellites written off</div><div class="sn">whiskers on pure-tin relays</div></div><div class="stat"><div class="sv">0.5%</div><div class="sl mono">lead said to stop it</div><div class="sn">other sources say 3%</div></div><div class="stat"><div class="sv">?</div><div class="sl mono">published acceleration factor</div><div class="sn">none exists</div></div></figure>


## The record is real, and it is also a pile of anecdotes

The failures are not hypothetical. NASA Goddard's electronic parts group keeps the field's running ledger, and the satellite section is the part everyone quotes: four commercial communications satellites — Galaxy VII, Galaxy IV, Solidaridad 1 and Galaxy IIIR — written off entirely after both their primary and redundant spacecraft control processors failed, with whiskers on pure-tin relays implicated. Four more lost their redundancy and kept flying on one processor.

Galaxy IV is the famous one. On 19 May 1998 it lost control, and with it roughly 80 per cent of US pager service, a great deal of pay-at-the-pump card authorisation, Reuters' wire feed, and the network feeds of all 600 NPR affiliates. Hughes afterwards moved from pure tin to nickel plating, which the trade coverage of the time says added 100 to 200 pounds per payload — a striking way to see a materials decision priced.

The ledger runs much further back than spaceflight. Cadmium-plated military air capacitors had been failing since about 1942, and H. Cobb identified whiskers as the cause in 1946; when cadmium was replaced with tin and zinc in 1952, Bell Labs found the replacements whiskered too. This is an eighty-year-old failure mode, not a modern regression.

Then the honest part, which NASA prints on the page itself. The list "is NOT ALL ENCOMPASSING". Several entries are private communications with no detail attached; some are zinc or silver rather than tin. The absence of an entry "should NOT be construed as evidence of absence", and the anecdotes section exists precisely because for many incidents the formal publicity is "either unavailable or unwanted". You cannot compute a failure rate from a document like that, and as far as I can tell nobody has. The sources do not even fully agree on the canonical case: NASA's table records Galaxy IV's *first* processor failure as not whisker-caused and the fatal redundant failure in May 1998 as the whisker one, while the general reference account has the primary failing that day and the backup carrying an earlier undetected fault.

## The regulation everyone blames arrived too late to have caused it

The folk explanation is that Europe banned lead and things started falling out of the sky. The dates do not permit it. RoHS 1 was adopted in February 2003 and its restrictions applied from 1 July 2006, capping lead at 0.1 per cent by weight in each homogeneous material. All four satellite write-offs began failing between 1998 and 2001. The whisker-induced reactor protection trip at Dresden was 1987; Duane Arnold scrammed in 1990 and again in 1995; the Air Force attribution on F-15 radar problems dates to 1986.

Worse for the folk explanation, RoHS never applied to the exposed systems in the first place. Article 2(4) of the recast directive excludes equipment necessary for protecting member states' essential security interests, including arms and munitions for specifically military purposes, and — by name — equipment "designed to be sent into space". Satellites and missiles were carved out explicitly.

What actually happened is subtler than a ban. The component market walked off and left high-reliability users standing there: once consumer volume went lead-free, parts stopped being offered with tin-lead finishes at all, so aerospace, defence and medical buyers found themselves purchasing pure-tin parts and then paying to strip and re-plate them. Nor was the drift purely regulatory even before 2006. NASA's own account notes that for Shuttle OV-105, built in 1987–89, OSHA rules had made lead-bearing plating solutions expensive to dispose of, and Honeywell proposed pure tin for the card guides — lead leaving for disposal cost and worker safety a decade and a half before anyone drafted a directive.


<figure class="fig bars"><figcaption class="mono">Whisker length, micrometres · log scale</figcaption><div class="rows"><div class="brow"><div class="blabel">JESD201 pass limit, tightest class</div><div class="btrack"><div class="bfill" style="width:32.53%" title="JESD201 pass limit, tightest class · 20 µm in test"></div></div><div class="bval mono">20 µm in test</div></div><div class="brow"><div class="blabel">JESD201 pass limit, loosest class</div><div class="btrack"><div class="bfill" style="width:45.65%" title="JESD201 pass limit, loosest class · 67 µm in test"></div></div><div class="bval mono">67 µm in test</div></div><div class="brow"><div class="blabel">Typical length seen in the field</div><div class="btrack"><div class="bfill" style="width:82.53%" title="Typical length seen in the field · ~2 mm"></div></div><div class="bval mono">~2 mm</div></div><div class="brow"><div class="blabel">Longest lengths reported</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Longest lengths reported · &gt;10 mm"></div></div><div class="bval mono">&gt;10 mm</div></div><div class="brow"><div class="blabel">Gap bridged at Millstone in 2005</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Gap bridged at Millstone in 2005 · not published"></div></div><div class="bval mono muted">not published</div></div></div></figure>


## What the qualification test can and cannot tell you

There is now a standard test. JESD201 stores parts under fixed conditions and passes them if no whisker exceeds a maximum length — between 20 and 67 microns depending on product class and device type. Set that against the millimetre-scale filaments the field reports and the comparison looks absurd, though it is not quite apples to apples: the threshold is what may grow during a bounded test, not a prediction of end-of-life length. The problem is that nothing converts the one into the other, as the standard says itself — its testing "does not guarantee that whiskers will or will not grow under field life conditions."

The reason is that there are no established acceleration factors. A representative qualification campaign reported in this year's review ran three samples per condition — 4,000 hours at 30 °C and 60 per cent humidity, 4,000 hours at 55 °C and 85 per cent, and 1,500 thermal shocks between −55 and 85 °C. Whatever that demonstrates cannot be extrapolated to twenty years in a different climate, because nobody has published the function that would do the extrapolating. NASA's background page is blunter: results on temperature, humidity and thermal cycling are *contradictory*, and the uncertainties make it "extremely difficult to predict if/when tin whiskers may appear." A University of Maryland survey found only a third of suppliers tested for whiskers at all as part of lead-free qualification.

Underneath the testing problem is a physics problem. Compressive stress relieved by recrystallisation is the leading account, and NASA states plainly that "a single accepted explanation of the mechanisms has NOT been established." A 2023 paper in *Crystals* pushes on exactly that: whiskers form in aluminium–tin and silicon–tin systems with no intermetallic to drive volume expansion, they appear in high vacuum, and in the authors' own samples residual stress was essentially identical — 34.3 MPa against 31.5 — between a specimen that whiskered within a day and one that produced nothing in over a year. Their alternative, excess surface energy driving abnormal recrystallisation, is inferred from a five-degree melting-point depression rather than measured directly. Eighty years in, the mechanism is still an argument.

## Two readings of the same hole in the data

Two serious institutions have looked at that hole and drawn opposite conclusions.

The US nuclear regulator opened tin whiskers as Generic Issue 200 after six events: the Dresden trips of 1987 and 1997, Duane Arnold in 1990 and 1995, a pre-trip alarm at South Texas Project in 1999, and the Millstone Unit 3 trip of 17 April 2005, where a whisker shorted a Westinghouse protection-system logic card about 97 per cent tin. Dominion pulled, photographed, cleaned and inspected 103 cards at that unit, replaced four, extended the sweep to Unit 2, and committed to inspections at every refuelling outage. The NRC then closed the issue without a quantitative risk estimate of any kind — no core damage frequency, no probability, only a qualitative finding that the incidents "have not been safety significant" given no precursor events, no common-cause failures and no increasing trend. The issue was, in the document's own capitals, "DROPPED from further pursuit".

The 2025 review by Pecht and colleagues at Maryland reads the same emptiness the other way and concludes the high-reliability community has overcorrected. It calls the governing aerospace standard "ultra-conservative and not cost effective", judges its strictest control class — stripping lead-free parts and re-plating them with tin-lead — "becoming unrealistic to achieve and fraught with quality issues", and estimates that not refinishing could save up to ten times the cost. Its sharpest argument is not economic: reballing and solder-dipping are themselves damaging processes, so the mitigation can plausibly introduce more defects than the whiskers it prevents. The supporting evidence is also soft, though. One manufacturer's claim of no whisker failures across more than two thousand billion shipped products is a vendor assertion, not an independent audit, and a 2017 model putting whisker-induced failure on a PC motherboard below 0.03 per cent is a result about a motherboard in an office, not a relay in geosynchronous orbit for fifteen years.

### What I would want before believing either side

The thing I keep turning over is the direction of the nuclear failures. Every one of those six events pushed the plant toward shutdown — a spurious scram, a trip, an alarm — rather than away from it. That is the benign direction, and it is a large part of why the issue was closed. But it may also be an artefact of what gets noticed: an unnecessary scram is unmissable and reportable, while a whisker that quietly disables one channel of a redundant system may never announce itself. The conclusion that redundant safety functions were not impaired rests on the events that were found.

The other gap is the suppression threshold, unsettled in the sources themselves. NASA's history says whiskering stops at 0.5 per cent lead or more; this year's review puts meaningful reduction at 1 per cent and elimination at 3. That is a sixfold disagreement about the one intervention everybody agrees works. Even the measured mitigations are conditional: a one-hour anneal at 150 °C cut maximum whisker length on matte tin over copper by 72 per cent, and did nothing at all for the same tin over brass.

Tin whiskers are not a mystery in the sense of being unobserved — there are photographs, databases, microscopy, a regulator's event list and eighty years of literature. They are a mystery in the sense that nobody can tell you the probability. And the two most careful groups in the field have taken that same silence as licence to move in opposite directions.
