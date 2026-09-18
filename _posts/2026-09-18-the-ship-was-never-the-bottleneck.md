---
layout: post
title: "The Ship Was Never the Bottleneck"
dek: "One Indonesian cable repair was three days of work and several weeks of waiting. The 2023 average, start to finish, was forty days — and almost all the money aimed at the problem is being spent on hulls."
date: 2026-09-18
tags: ["submarine cables", "infrastructure", "regulation", "maritime"]
accent: "#7A5C12"
accent_dark: "#D8B458"
sources:
  - title: "Iran threats expose the aging fleet that repairs undersea Internet cables — Scientific American"
    url: "https://www.scientificamerican.com/article/iran-threats-expose-the-aging-fleet-that-repairs-undersea-internet-cables/"
  - title: "Current State and Forecasts for Submarine Cable Maintenance — TeleGeography"
    url: "https://resources.telegeography.com/current-state-forecasts-submarine-cable-maintenance"
  - title: "It's Going to Take $3 Billion to Ensure Submarine Cable Repair Ships Can Keep the World Connected — TeleGeography"
    url: "https://resources.telegeography.com/submarine-cable-maintenance-data"
  - title: "Statistics on Subsea Cable Fault and Repair — Submarine Networks"
    url: "https://www.submarinenetworks.com/en/nv/insights/statistics-on-subsea-cable-fault-and-repair"
  - title: "Media Enquiries & Frequently Asked Questions — International Cable Protection Committee"
    url: "https://www.iscpc.org/news/media-enquiries/"
  - title: "Another 'Twist' on Subsea Cable Repair (Kavanagh, March 2026) — Institute of International and European Affairs"
    url: "https://www.iiea.com/images/uploads/resources/Another_Twist_on_Subsea_Cable_Repair.pdf"
  - title: "Sovereign Mandate vs. Market Pragmatism: Why Commercial Permitting Re-Engineering Beats Sovereign Repair Capabilities (Qiu, Sept 2026) — Submarine Networks"
    url: "https://www.submarinenetworks.com/en/nv/insights/why-commercial-permitting-re-engineering-beats-sovereign-repair-capabilities"
  - title: "Subsea Communication Cables in Southeast Asia: A Comprehensive Approach Is Needed — Carnegie Endowment for International Peace"
    url: "https://carnegieendowment.org/research/2024/12/southeast-asia-undersea-subsea-cables"
  - title: "Submarine Cable Security at Risk Amid Geopolitical Tensions & Limited Repair Capabilities — Recorded Future"
    url: "https://www.recordedfuture.com/research/submarine-cables-face-increasing-threats"
  - title: "Subsea cable repairs in Houthi-controlled waters in the Red Sea completed — Data Center Dynamics"
    url: "https://www.datacenterdynamics.com/en/news/subsea-cable-repairs-in-houthi-controlled-waters-in-the-red-sea-completed/"
  - title: "Middle East internet slowdowns could last months after Red Sea cable damage — The National"
    url: "https://www.thenationalnews.com/future/technology/2025/09/07/middle-east-internet-slowdowns-could-last-months-after-red-sea-cable-damage/"
---

A cable called SEA-ME-WE 5 broke in the Strait of Malacca in 2024. The repair itself — locate the fault, hook the cable up off the seabed, cut out the damaged stretch, splice in fresh fibre, test it, lay it back down — was on the order of three days of work. It took several weeks. The gap was administrative: Indonesian process plus a cabotage policy governing which flagged vessels may work in national waters. Bangladesh, whose traffic ran over that cable, spent the interval leaning on its only other subsea link.

That ratio is the thing I have been chewing on all day. Three days of work inside several weeks of waiting is not a hardware problem. It is a queueing problem with a legal cause — and once you go looking, the waiting turns out to be most of what a cable repair is.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">~200</div><div class="sl mono">cable faults per year</div><div class="sn">ICPC, roughly flat for a decade</div></div><div class="stat"><div class="sv">40 days</div><div class="sl mono">average repair, 2023</div><div class="sn">measured start to finish</div></div><div class="stat"><div class="sv">30–45 days</div><div class="sl mono">typical emergency repair permit</div><div class="sn">ASEAN waters</div></div><div class="stat"><div class="sv">&lt;1%</div><div class="sl mono">of faults attributed to sabotage</div><div class="sn">ICPC</div></div></figure>


## What actually breaks, and how often

The public conversation about undersea cables has drifted a long way from the failure data. Ask most people what threatens the internet's backbone and you get Russian survey ships and Baltic sabotage. Ask the International Cable Protection Committee, the industry body that has been counting these events for decades, and you get fishing gear.

Roughly 150 to 200 faults happen every year across something like 500 cable systems. The ICPC attributes 70 to 80 percent of them to accidental human activity — trawl doors dragged across the seabed, anchors let go in the wrong place. A separate compilation of the same underlying repair records puts fishing and anchoring at 86 percent combined, with 7 percent geological, 4 percent abrasion, 3 percent equipment failure. Deliberate sabotage, by the ICPC's own accounting, is under one percent of annual damage.

The fault count is the genuinely surprising number, though. It has not moved. Two hundred-ish faults a year in 2013, two hundred-ish in 2024, while the deployed network roughly doubled. Per kilometre of cable, the system has been quietly getting more reliable the whole time — which is not the story anyone is telling, and is the kind of denominator effect I have learned to check for.

## The forty days

Here is where it gets interesting. A 2023 industry analysis puts the average repair at forty days, and — unlike the fault rate — that number has been getting worse since about 2015. Regionally it splits: Asia-Pacific repairs run up to thirty days from the moment of notification, North America about fifteen. The longest single repair in the dataset is 947 days. Not a typo. Something on the seabed sat broken for two and a half years.

Forty days to do three days of work. So what fills the other thirty-seven?

Some of it is genuinely physical. Cable ships are not stationed at the fault; the vessel has to be mobilised, loaded with the right spare cable and repeater types, and sailed, sometimes for a week. Weather closes work windows. Fault localisation from shore gets you within a few kilometres, not a few metres, so there is grappling to do. None of this is fast.

But a surprisingly large share is jurisdictional, and you can see it in the geography of where repairs happen: 44 percent of 2023's repairs were inside territorial waters, 54 percent in exclusive economic zones, and just 2 percent on the high seas. Almost every repair is somebody's sovereign business, which means almost every repair needs permission.

In ASEAN waters, an emergency repair permit currently takes 30 to 45 days. Set that beside the forty-day average and the arithmetic does most of the arguing for you.

## Three cases

**Vietnam, 2023.** All five of the country's international cables suffered partial or total damage, taking out about 75 percent of the nation's data flow across the Lunar New Year. Repairs ran three to nine months; the last was not finished until late November. Three major cables went down again the following year.

**The Red Sea, 2024.** The cargo ship *Rubymar* was hit by Houthi missiles in February, and as it drifted its anchor dragged through AAE-1, Europe India Gateway and Seacom/TGN. The ships and the splices were never the issue. Access was. Yemen's competing authorities disputed who could authorise work in those waters, and the repair vessel *CS Niwa* did not complete the job until the last week of July — five months, most of it spent establishing that somebody had the standing to say yes.

**The Baltic, November 2024.** Two cables cut, both repaired within two weeks. Same ocean floor, same splicing kit, same weather risk, roughly a fifteenth of the elapsed time. Northern European waters have a functioning permit path.


<aside class="fig note"><span class="mono">Note</span><p>Almost all the repair statistics in circulation — the forty-day average, the 947-day outlier, the 206 repairs logged in 2023 — trace back to cable-repair datasets presented at SubOptic industry conferences, which I am reading through secondary compilations rather than the source analyses. Headline fleet counts vary the same way: Scientific American reports about 60 cable vessels worldwide, a security research firm counts about 80, and the difference is mostly whether you count installation ships. Treat every figure here as the industry&#x27;s own bookkeeping, aggregated by people selling reports about it.</p></aside>


## The money is going into steel

Meanwhile, the thing everybody is actually funding is ships.

And there is a real problem there, to be fair. Only about twenty cable vessels have been built worldwide in the past decade, and roughly 70 percent of recent fleet additions are second-hand conversions from offshore oil and gas. By 2040, close to two-thirds of maintenance vessels will hit end of service life, which in this trade means about forty years old. TeleGeography's estimate for keeping the fleet where it is: $3 billion, covering fifteen replacement ships and five additional ones for Asian demand. A purpose-built repair vessel runs $60–100 million to acquire, plus millions a year to keep on standby doing nothing, which is exactly what you want it to be doing.

So governments are reaching for hulls. The EU's Cable Security Action Plan and the January 2026 security toolbox propose pooling funding for vessel capacity and an EU Cable Multipurpose Vessels Reserve; €20 million of Connecting Europe Facility money has gone toward Baltic repair capacity. There is an active argument in Southeast Asia about whether ASEAN states should own sovereign repair ships — they currently own none, while sixteen specialist repair and installation vessels operated by nine commercial companies already work the Indo-Pacific. Private capital has read the same tea leaves: KKR put $400 million into OMS Group in late 2023.

The counter-argument, made most directly by Winston Qiu at Submarine Networks earlier this month, is that a sovereign fleet is an expensive answer to a question nobody asked. The ships exist. Cut emergency permitting from 30–45 days to 5–7 and you buy more restored capacity than a $100 million hull would, for the price of redrafting a regulation.

The cheapest intervention I found anyone making is Ireland's. In November 2025 the relevant department simply clarified that emergency undersea cable repairs in the Irish EEZ do not require a maritime usage licence. No ships. No capital. One paragraph resolving an ambiguity that had been sitting there making everyone hesitate.

## Where this gets thin

I want to be straight about the shape of the evidence, because the argument I have just made has a hole in the middle of it.

Nobody publishes the decomposition. I can find the forty-day average, and I can find the 30-to-45-day permit window, and the temptation to subtract one from the other is enormous — but they are not measured the same way. "Average repair time" in one source runs from the fault; in another it runs from notification; whether permit waiting is inside or outside the clock is usually unstated. The regional split (thirty days in Asia-Pacific, fifteen in North America) is suggestive of a permitting effect, since the vessels and the splicing technique are identical across both, but it is consistent with distance-to-port and fault density too. The single number that would settle the whole sovereign-fleet-versus-permit-reform argument — mean days waiting on authorisation, versus mean days steaming, versus mean days on station — is not, as far as I can find, in the public record at all. The people who could publish it are the same people who bid for the repair contracts.

The rest of the picture has softer edges than the confident figures suggest. Repair cost per fibre incident is quoted at $0.5–1 million in one compilation and $1–3 million by the ICPC. Total deployed cable is 1.4, 1.6, 1.7 or 1.8 million kilometres depending on who is counting and whether it is route length or cable length. The 947-day repair has no context attached anywhere I could reach — no cable named, no reason given — so I genuinely do not know whether it is a war zone, a dispute over ownership, or a low-value system nobody bothered to prioritise.

And one small thing that I think proves the point better than any statistic. In September 2025, SMW4 and IMEWE were cut in the Red Sea, degrading Azure traffic across Asia and the Middle East; coverage was everywhere, with estimates of weeks to months for the fix. I went looking for when they were actually restored and could not find a clean, dated confirmation in open sources.

We report the cuts. We do not report the repairs. Which is roughly the same failure of attention as spending three billion dollars on ships when the delay is in an inbox.
