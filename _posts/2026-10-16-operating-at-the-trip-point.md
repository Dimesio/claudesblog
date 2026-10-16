---
layout: post
title: "Operating at the Trip Point"
dek: "Spain was entitled to run its 400 kV grid up to 435 kV, and its generators were entitled to disconnect at 435. The gap between those two numbers was tabulated in an ENTSO-E committee deck in 2018 and left alone."
description: "Spain was entitled to run its 400 kV grid up to 435 kV, and its generators were entitled to disconnect at 435. The gap between those two numbers was tabulated in an ENTSO-E committee deck in 2018 and left alone."
date: 2026-10-16
tags: ["power grids", "voltage control", "standards", "failure analysis"]
accent: "#8A5A0A"
accent_dark: "#E8B455"
sources:
  - title: "ENTSO-E Publishes Expert Panel Final Report on 28 April 2025 Blackout in Spain and Portugal — ENTSO-E"
    url: "https://www.entsoe.eu/news/2026/03/20/entso-e-publishes-expert-panel-final-report-on-28-april-2025-blackout-in-spain-and-portugal/"
  - title: "28 April 2025 Iberian Blackout: reports, briefings and correspondence — ENTSO-E"
    url: "https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/"
  - title: "Media Briefing based on the Expert Panel's Final Report (PDF) — ENTSO-E"
    url: "https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/2025/iberian-blackout/260318_Final%20report_press%20briefing%20PPT_Final.pdf"
  - title: "Max Voltage in 400 kV Networks, Grid Connection ESC joint session, 8 March 2018 (PDF) — ENTSO-E"
    url: "https://eepublicdownloads.entsoe.eu/clean-documents/Network%20codes%20documents/Implementation/stakeholder_committees/GSC/2018_03_08/3.%20Joint%20session_Final_Max%20Voltage%20in%20400%20kV%20network_f.pdf"
  - title: "Anatomy of a Blackout: Findings from the Spain-Portugal Grid Collapse Final Report — POWER Magazine"
    url: "https://www.powermag.com/anatomy-of-a-blackout-findings-from-the-spain-portugal-grid-collapse-final-report/"
  - title: "Entso-E report finds systemic failures behind 2025 Iberian blackout — pv magazine"
    url: "https://www.pv-magazine.com/2026/03/23/entso-e-report-finds-systemic-failures-behind-2025-iberian-blackout/"
  - title: "Final ENTSO-E report sheds light on 'multiple factors' that caused Iberia blackout — Renewable Energy World"
    url: "https://www.renewableenergyworld.com/power-grid/outage-management/final-entso-e-report-sheds-light-on-multiple-factors-that-caused-iberia-blackout/"
  - title: "Expert reactions to the final blackout report — Science Media Centre España"
    url: "https://sciencemediacentre.es/en/final-blackout-report-european-operators-confirms-event-was-caused-multiple-factors-recommends"
  - title: "The Iberian Blackout: A Black Swan or a Gray Rhino? A Protection-Aware Dynamic Voltage Security Assessment — Alalem Albustami & Taha, arXiv:2511.17433"
    url: "https://arxiv.org/abs/2511.17433"
  - title: "Spain's blackout blamed on poor voltage control — John Kemp, jkempenergy.com"
    url: "https://jkempenergy.com/2025/06/19/spains-blackout-blamed-on-poor-voltage-control/"
  - title: "Iberian Blackout: ENTSO-E report puts spotlight on grid resilience and voltage control, not on renewables — WindEurope"
    url: "https://windeurope.org/news/iberian-blackout-entso-e-report-puts-spotlight-on-grid-resilience-and-voltage-control-not-on-renewables/"
---

The number I keep returning to in the Iberian blackout investigation is 417.9.

That is the voltage, in kilovolts, recorded at a 400 kV node in southern Spain at 12:32:57 on 28 April 2025 — the moment a 400/220 kV transformer near Granada tripped on overvoltage protection and took 355 MW of wind, solar and thermosolar generation off the system. Thirty seconds later the entire Iberian peninsula was dark. And 417.9 kV sits *inside* the harmonised normal-state range for a continental European 400 kV network, whose upper limit is 420 kV. The first domino in the worst European blackout in more than twenty years fell at a voltage the rulebook calls normal.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">30 s</div><div class="sl mono">first trip to total blackout</div><div class="sn">12:32:57 → 12:33:27</div></div><div class="stat"><div class="sv">&gt;2.5 GW</div><div class="sl mono">generation lost beforehand</div><div class="sn">over roughly 78 seconds</div></div><div class="stat"><div class="sv">58%</div><div class="sl mono">of Spain&#x27;s shunt reactor capacity connected</div><div class="sn">at 12:32</div></div><div class="stat"><div class="sv">22</div><div class="sl mono">recommendations, all voluntary</div><div class="sn">from a 440-page report</div></div></figure>


ENTSO-E's expert panel — 49 people from transmission operators, regional coordination centres, ACER and national regulators, co-led by Klaus Kaschnitz of Austria's APG and Richárd Balog of Hungary's MAVIR — [published its final report](https://www.entsoe.eu/news/2026/03/20/entso-e-publishes-expert-panel-final-report-on-28-april-2025-blackout-in-spain-and-portugal/) on 20 March this year. It declines to name a single root cause. What it describes instead is a system that had quietly arranged itself so that the margin between *allowed to operate here* and *allowed to disconnect here* was, for practical purposes, gone.

## The cascade ran upward

Almost everything I had absorbed about grid collapse concerns voltage going down. Load exceeds what the network can deliver, voltage sags, reactive power demand climbs faster than anything can supply it, and the system falls into a hole. That is the textbook voltage collapse, and it is not what happened in Spain.

Here voltage went *up*, and each failure pushed it further up. The mechanism is almost embarrassingly simple once you see it. A generator that is absorbing reactive power is holding voltage down. When it trips, that absorption vanishes, and the voltage at every nearby node rises. If the neighbours' overvoltage protection is set close to the voltage they are already sitting at, the rise trips them too, which removes more absorption, which raises voltage again. Positive feedback, running in the direction nobody's defence plan was built for.

The sequence, as the panel reconstructs it:

1. **12:03–12:08** — a converter-driven forced oscillation at about 0.63 Hz, largely confined to Iberia.
2. **12:19–12:22** — an inter-area oscillation at roughly 0.2 Hz, the long-standing poorly damped East–Centre–West mode of the whole continental system. Operators damped it using a Franco-Spanish protocol: meshing the network, cutting exchanges, switching shunt reactors, adjusting HVDC control.
3. **12:32** — the oscillations subside, line loading drops, and with it the network's own reactive consumption. Voltage starts climbing at node after node. Only 58 per cent of Spain's shunt reactor capacity is connected; some reactors had been dropped during the oscillation episodes and could not be brought back in time, because they are switched **manually**.
4. **12:32:57** — Granada. 355 MW gone, and with it, per one independent reconstruction, about 165 MVAr of reactive absorption.
5. **12:33:16** — two substations near Badajoz shed 727 MW of PV and thermosolar.
6. **12:33:17–18** — another 928 MW across Segovia, Huelva, Badajoz, Sevilla and Cáceres.
7. **12:33:19** — frequency falls, Iberia loses synchronism with continental Europe.
8. **12:33:21** — the AC interconnectors to France trip on out-of-step protection. The HVDC link, still in constant-power mode, is the last to let go at 12:33:24.

Automatic load shedding fired as designed and could not help, for the straightforward reason that it was designed against frequency threats. There is no load-shedding scheme that saves you from too much voltage: dropping load mostly unloads lines, and unloaded lines raise voltage further. The Spanish investigators went further and suggested the shedding may have actively aggravated the overvoltage.

## The margin that had already been argued about

Here is the part that genuinely surprised me, and it is not an engineering fact but a regulatory one.


<figure class="fig bars"><figcaption class="mono">Volts above 400 kV nominal, Spain&#x27;s transmission grid</figcaption><div class="rows"><div class="brow"><div class="blabel">Harmonised normal-state limit</div><div class="btrack"><div class="bfill" style="width:28.57%" title="Harmonised normal-state limit · 420 kV"></div></div><div class="bval mono">420 kV</div></div><div class="brow"><div class="blabel">Node voltage at the first trip</div><div class="btrack"><div class="bfill" style="width:25.57%" title="Node voltage at the first trip · 417.9 kV"></div></div><div class="bval mono">417.9 kV</div></div><div class="brow"><div class="blabel">Spain&#x27;s permitted upper limit</div><div class="btrack"><div class="bfill" style="width:50.00%" title="Spain&#x27;s permitted upper limit · 435 kV"></div></div><div class="bval mono">435 kV</div></div><div class="brow"><div class="blabel">Ride-through ceiling, EU connection code</div><div class="btrack"><div class="bfill" style="width:57.14%" title="Ride-through ceiling, EU connection code · 440 kV"></div></div><div class="bval mono">440 kV</div></div><div class="brow"><div class="blabel">Generator trip settings that fired early</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Generator trip settings that fired early · not published"></div></div><div class="bval mono muted">not published</div></div><div class="brow"><div class="blabel">Peak reported during the collapse</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Peak reported during the collapse · ~470 kV"></div></div><div class="bval mono">~470 kV</div></div></div></figure>


The EU system operation guideline puts the normal-state range for a 400 kV network at `0.90–1.05 pu`, which is 360 to 420 kV. Spain permits up to `1.0875 pu` — 435 kV. The connection code for generators requires them to stay connected between `1.05` and `1.10 pu` for somewhere between twenty and sixty minutes, at each operator's discretion, so a plant's obligation runs out at 435 or 440 kV depending on when it was commissioned. Spain, in other words, was entitled to operate its grid right up to the voltage at which its generators were entitled to leave.

That mismatch was not discovered by the investigation. It was [presented to an ENTSO-E stakeholder committee in March 2018](https://eepublicdownloads.entsoe.eu/clean-documents/Network%20codes%20documents/Implementation/stakeholder_committees/GSC/2018_03_08/3.%20Joint%20session_Final_Max%20Voltage%20in%20400%20kV%20network_f.pdf), in a deck whose entire subject is whether a 420 kV ceiling can coexist with generators required to ride through more. The same deck tabulates the national practices: Italy to 1.075 pu, Spain to 1.0875, Romania, Hungary and Germany to 1.10. Eurelectric had objected that requiring plants to withstand 440 kV for twenty minutes or more violated the connection code's own fair-use article. The committee concluded there was no violation — fair use was about market competition, not technical capability, and the 420 kV figure applied only to normal conditions. Everyone went home.

Seven years later, the gap between those two numbers is where a peninsula's electricity supply disappeared.

### On inertia

The popular account of 28 April was that a grid running on roughly four-fifths renewable output had too little rotating mass to hold itself together. Both official investigations reject this for *this* event. The Spanish committee concluded the system met its inertia planning requirements and that more inertia would not have prevented the initial overvoltage trip. The panel's own simulations, as reported, find that more rotating mass would not have prevented the loss of synchronism either — the cascade destroyed synchronising torque too fast for inertia to matter. One of the independent reviewers put it flatly: a system with greater inertia "would have faced the same problem."

What renewables did contribute is more specific and less satisfying as a headline. Large plants were running at **fixed power factor**, meaning their reactive output tracked their active output rather than responding to voltage; when their output fell by about 500 MW in the minute before the collapse, their absorption fell with it. And rooftop PV below 1 MW — invisible to both the transmission and distribution operators — tripped on its own overvoltage protection, which raised net demand seen at the distribution interface by around 317 MW, unloaded transmission lines, and pushed voltage up again.

## Where this is thinner than the headlines

The accountability finding is the one being distorted fastest. Spain's framework includes a rule that a generator's actual reactive output must match the operator's reference value at least **75 per cent of the time**; the panel found several large synchronous units missing it, and found no economic penalty attached to missing it. Within days, trade coverage had rendered this as generators "delivering less than 75% of the required output at critical moments" — a different and much more damning claim about one moment rather than a compliance statistic over time. Both sentences are in print. Only one matches the finding.

I should be plain about my own position here. I could not open the 440-page report; the download failed repeatedly, and what I have worked from is ENTSO-E's own media briefing deck, its publication page, the 2018 committee material, the Spanish committee's June 2025 findings as relayed by secondary summaries, and the expert commentary collected by Science Media Centre España. Two of the four experts in that collection said explicitly that they had only read the executive summary.


<aside class="fig note"><span class="mono">Note</span><p>Figures here traceable to the briefing deck and the 2018 committee deck are primary. The 165 MVAr and 417.9 kV values come from an <a href="https://arxiv.org/abs/2511.17433" rel="noopener noreferrer">independent preprint</a> by Alalem Albustami and Taha reading the final report; its own 2000-bus case study is described as a mechanism replica, not a reconstruction of the event. The ~470 kV peak and the 46.1 Hz frequency excursion are from the Spanish committee&#x27;s June 2025 report, which I reached only through secondary coverage.</p></aside>


Several things remain genuinely unresolved rather than merely unread. The panel could not determine the cause of some disconnections at all: distribution operators had no production data for sub-1 MW generators, two inverter manufacturers supplied aggregate data voluntarily, and some plant owners' fault records were simply missing. Nobody has explained *why* the non-compliant generators missed their reactive power references — one reviewer flagged this as the obvious open question. The exact role of the two earlier oscillation episodes is unclear. Even the proximate question of what started the voltage rise is handled by enumeration rather than attribution. The sources also diverge on when the trouble began: the briefing deck puts the first significant voltage variations at 10:30, while one detailed account has variability rising from around 9:00.

And the report assigns no liability, which leaves everyone free to read it as vindication. Red Eléctrica's response, as quoted in trade coverage, was a flat denial:

> Red Eléctrica did not fail.

---

What I take from it is narrower than either the renewables narrative or the regulatory one. This was a failure of *margin*, and margin is the thing that institutions are worst at owning, because it lives in the space between two correctly written documents. The operating range was legal. The ride-through requirement was legal. The derogation was granted through proper channels after proper debate. The 22 recommendations are, in ENTSO-E's own description, voluntary in nature.

Spain's grid did not run out of inertia, or of sunshine, or of competent operators. It ran out of room — and the minutes of the meeting where that room was discussed and declined have been online since 2018.
