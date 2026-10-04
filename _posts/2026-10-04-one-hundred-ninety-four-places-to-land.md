---
layout: post
title: "One Hundred Ninety-Four Places to Land"
dek: "The FAA is removing a third of America's VOR beacons and keeping the rest as a skeleton sized by one rule: a conventional instrument approach within 100 nautical miles of anywhere in the lower 48. That comes to 194 airports — and the failure mode that has actually grown since isn't the one the network answers."
description: "The FAA is removing a third of America's VOR beacons and keeping the rest as a skeleton sized by one rule: a conventional instrument approach within 100 nautical miles of anywhere in the lower 48. That comes to 194 airports — and the failure mode that has actually grown since isn't the one the network answers."
date: 2026-10-04
tags: ["aviation", "navigation", "gps", "redundancy"]
accent: "#A8172B"
accent_dark: "#F58A96"
sources:
  - title: "Provision of Navigation Services for NextGen: Plan for Establishing a VOR Minimum Operational Network, 81 FR 48694 — Federal Register"
    url: "https://www.federalregister.gov/documents/2016/07/26/2016-17579/provision-of-navigation-services-for-the-next-generation-air-transportation-system-nextgen"
  - title: "VOR MON and NextGen DME Programs, EAA Oshkosh briefing, July 2025 — FAA"
    url: "https://www.faa.gov/about/officeorg/headquartersoffices/ato/navigation-programs/vor-mon-outreach-presentations/2025-oshkosh-vor-mon-nextgen-dme-programs.pdf"
  - title: "Instrument Flight Procedures Inventory Summary — FAA"
    url: "https://www.faa.gov/air_traffic/flight_info/aeronav/procedures/ifp_inventory_summary/"
  - title: "GNSS Interference Resource Guide, March 2026 — FAA"
    url: "https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afx/afs/afs400/afs410/GNSS/GPS_GNSS_Interference_Resource_Guide.pdf"
  - title: "Amendment of Domestic VOR Federal Airways V-16, V-35 and others, Eastern United States — Federal Register"
    url: "https://www.federalregister.gov/documents/2026/03/06/2026-04442/amendment-of-domestic-very-high-frequency-omnidirectional-range-vor-federal-airways-v-16-v-35-v-37"
  - title: "EASA updates aircraft GNSS jamming and spoofing guidance, citing spike — Runway Girl Network"
    url: "https://runwaygirlnetwork.com/2026/07/easa-updates-aircraft-gnss-jamming-and-spoofing-guidance/"
  - title: "VOR MON Program briefing 23-01, Aeronautical Charting Forum — FAA"
    url: "https://www.faa.gov/air_traffic/flight_info/aeronav/acf/media/Presentations/23-01-VOR-MON-Program.pdf"
  - title: "Discontinuation of VOR Services update, Aeronautical Charting Forum 12-01 — FAA"
    url: "https://www.faa.gov/air_traffic/flight_info/aeronav/acf/media/Presentations/12-01_Discon-of-VOR-update.pdf"
  - title: "VOR Minimum Operational Network (VOR MON) program page — FAA"
    url: "https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gbng/vormon"
  - title: "On Instruments: The GPS backup — AOPA"
    url: "https://www.aopa.org/news-and-media/all-news/2021/july/pilot/on-instruments-the-gps-backup"
---

The FAA is two-thirds of the way through taking down a third of the radio beacons that used to define American airspace, and the question of which ones survive comes down to a single sentence of design criteria. I went looking for how that sentence cashes out in practice — how many places you could actually land, under instrument flight rules, if GPS stopped working over the lower 48 — and found the answer in a conference slide deck rather than a regulation.

It is 194.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">896</div><div class="sl mono">VORs at program start</div><div class="sn">contiguous U.S., FY2016</div></div><div class="stat"><div class="sv">200</div><div class="sl mono">discontinued so far</div><div class="sn">as of July 2025</div></div><div class="stat"><div class="sv">594</div><div class="sl mono">planned end state</div><div class="sn">FY2030</div></div><div class="stat"><div class="sv">194</div><div class="sl mono">designated MON airports</div><div class="sn">123 ILS/LOC, 71 VOR</div></div></figure>


## What a VOR does, and why there are fewer of them

A VOR is an unattended ground station radiating a VHF signal encoded so that a receiver can work out its bearing from the station — not distance, just the angle. String enough of them together and you get the Victor airways, the published low-altitude routes that are drawn literally station to station. That is why retiring one beacon means redrawing airways in the *Federal Register*: the notice from March 6, 2026 that takes out Charlotte, Foothills and Holston Mountain this December has to amend fourteen Victor airways to deal with the hole.

Beacons are expensive in the way that a thousand unattended radio sites in fields are expensive. In 2010 the FAA counted 967 of them, 1,018 including non-federal stations, with 80 percent of the fleet between twenty and thirty years old. Satellite navigation had made most of them redundant for their original job, so in 2016 the agency published a final policy — *Provision of Navigation Services for the Next Generation Air Transportation System*, 81 FR 48694 — committing to cut 308 of the 896 in the contiguous states and keep the remainder as a deliberate skeleton: the VOR Minimum Operational Network.

## The sentence

The MON is sized by two criteria, and reading them slowly is most of the work.

1. Retain enough VORs for nearly continuous signal coverage at and above 5,000 feet above ground level — roughly a 70-nautical-mile radius per station at that height.
2. Retain enough VORs that from any point in the contiguous United States, at least one airport with a conventional instrument approach lies within 100 nautical miles.

"Conventional" is carrying real weight there. It means an approach flyable with no GPS, no DME, no ADF and no radar coverage at all: an ILS, a localizer, or a plain VOR approach. The 194 airports are the set that satisfies that criterion. A hundred and twenty-three of them offer an ILS or localizer. The other seventy-one offer only a VOR approach.

Set that against what the country normally has. The FAA's own procedure inventory, as of the August 6, 2026 charting cycle, lists 11,439 published approach charts, 7,119 of them satellite-based. RNAV (GPS) approaches alone serve 2,989 airports. Conventional approaches of every kind serve 1,303. The guaranteed set — the one the network is actually engineered to deliver — is 194.

That is not a scandal. It is the design. The MON was never meant to preserve the airspace system minus GPS; its stated job is to let an aircraft that loses satellite navigation revert to beacon-to-beacon flying, get clear of the outage, and land *somewhere*. The FAA has been reasonably candid that "somewhere" is the operative word — AOPA reported in 2021 that the agency conceded the resulting routing would be inefficient for VOR-only aircraft and in places circuitous. The promise is a floor, not a network.

## The detail that reorganized how I think about it

Buried in the FAA's own outreach briefing, in the list of things pilots are asked to do, is this pair: maintain VOR and ILS proficiency, and do not load VOR approaches into your GPS navigator.

That second one clarified the whole program for me. Nearly every modern cockpit will cheerfully render a VOR approach as a magenta line computed from satellite position, and flying it that way is easier and more accurate than chasing a needle. It is also precisely useless in the only scenario the approach exists for. If GPS is the thing that broke, a procedure you have only ever flown through the GPS is a procedure you have not flown.


<figure class="fig pull"><p>A backup is only a backup if it does not route through the thing that failed.</p></figure>


The same briefing notes that no avionics changes are required, and that equipage, fuel reserve and alternate filing rules are unchanged. So the entire human half of this system — whether the receiver in the panel still works, whether the pilot can intercept and hold a radial under load, whether anyone has flown a raw VOR approach since their instrument checkride — is managed by exhortation. I could not find an FAA figure for what fraction of the general aviation fleet carries a functioning VOR receiver, nor any measurement of proficiency. "Maintain proficiency" is a request, and requests do not have denominators.

## The failure mode moved

This is where I think the design and the popular framing have come apart, and it is less the FAA's framing at fault than everyone else's.

The MON answers *denial*. GPS goes away — jamming, a satellite fault, an outage — the crew knows immediately because the box says so, and they revert. Clean case, well understood, well engineered.

What has grown since 2022 is the other thing. The FAA's GNSS Interference Resource Guide, published this past March, separates them carefully: jamming is emission that stops a receiver acquiring and tracking signals; spoofing is emission of GNSS-*like* signals that the receiver acquires and tracks happily, and then reports a position that is simply wrong. EASA's updated safety bulletin in July says both are growing in severity and sophistication, clustered around the Mediterranean, Black Sea, Middle East, Baltic and Arctic.

Reversion is a response to a *declared* failure. Spoofing's defining property is that nothing in the aircraft declares one. The FAA guide's own detection list is the tell: a position that shifts several miles in seconds, inertial and satellite solutions disagreeing, estimated position uncertainty climbing, the clock changing, the autopilot turning for a course you did not command. Every item on it is a cross-check a human has to notice and then believe. The ground network is the second half of the answer. The first half is a pilot deciding the magenta line is lying to them.

And the complementary half of the backup is arriving slowly. The NextGen DME program — which lets suitably equipped aircraft fix position from two distance-measuring stations instead of satellites — had 17 of 126 planned new sites in service as of July 2025, and its third segment is scheduled to run until 2035. The VOR cuts finish in FY2030.

## What I can't tell you

The gaps here are specific, and a couple of them are more interesting than the headline.

The freshest official status I can find is that July 2025 briefing; the FAA's VOR MON program page was last updated August 19, 2025. So the figure of 200 discontinued is more than a year stale, and three more go in December. Even the program total drifts depending on which document you open: the 2016 policy named 308 candidates, a 2023 briefing said 306, and the 2025 deck's own arithmetic — 200 gone, 102 to go — comes to 302. Small discrepancies, but I cannot reconcile them from public documents, and they are a reminder that the tidy number is a plan, not a census.

Nobody has published, as far as I can tell, an analysis of whether the 194 MON airports are usable in the weather you would actually be diverting in. A VOR approach bottoms out at a higher altitude than an ILS, by an amount that varies airport by airport with terrain and obstacles, and seventy-one of the 194 have nothing better on offer. The 100-nautical-mile criterion is purely geometric. It says nothing about ceilings, and nothing about whether you have the fuel to fly a hundred miles the long way round with a needle.

The threat numbers are weaker than their circulation suggests. The most-quoted statistic, which the FAA guide itself reproduces, is IATA's: loss of GNSS per 1,000 flights up 65 percent in the first half of 2024 against 2023. That is two years old, it lumps every cause of signal loss into one bucket, and it is dominated by conflict-adjacent airspace, where a MON airport in Nebraska helps nobody. I did not find a comparable figure for interference inside the contiguous United States, and I suspect the reason is that a clean one does not exist.

None of which makes the program wrong. What stays with me is the shape of it. A backup was specified in 2016 against the failure mode of 2016, is being built out through 2030 and 2035, and the failure mode that actually grew in the interval is one where the backup engages only after a person has correctly disbelieved an instrument. The engineering is all in the beacons. The single point of failure is the cross-check.
