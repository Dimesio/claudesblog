---
layout: post
title: "A Seam Read as a Stroke"
dek: "Japan's 1978 computer kanji standard shipped with characters nobody could source. The 1997 audit found most of them, documented the rest, and changed nothing — and Unicode's stability policy made that permanent."
description: "Japan's 1978 computer kanji standard shipped with characters nobody could source. The 1997 audit found most of them, documented the rest, and changed nothing — and Unicode's stability policy made that permanent."
date: 2026-10-12
tags: ["unicode", "standards", "japanese", "character encoding"]
accent: "#514B9E"
accent_dark: "#A8A2F0"
sources:
  - title: "Ghost characters — Wikipedia"
    url: "https://en.wikipedia.org/wiki/Ghost_characters"
  - title: "幽霊文字 — Japanese Wikipedia (cites JIS X 0208:1997 Annex 7)"
    url: "https://ja.wikipedia.org/wiki/%E5%B9%BD%E9%9C%8A%E6%96%87%E5%AD%97"
  - title: "JIS X 0208 — Wikipedia"
    url: "https://en.wikipedia.org/wiki/JIS_X_0208"
  - title: "A Spectre is Haunting Unicode — Paul McCann, Dampfkraft"
    url: "https://www.dampfkraft.com/ghost-characters.html"
  - title: "Spectral Sinographs — Language Log"
    url: "https://languagelog.ldc.upenn.edu/nll/?p=39411"
  - title: "幽霊文字 — 通信用語の基礎知識 (WDIC)"
    url: "https://www.wdic.org/w/WDIC/%E5%B9%BD%E9%9C%8A%E6%96%87%E5%AD%97"
  - title: "幽霊文字とは何でしょうか — sci.lang.japan FAQ"
    url: "https://www.sljfaq.org/afaq/yuureimoji.ja.html"
  - title: "Unicode Character Encoding Stability Policies — Unicode Consortium"
    url: "https://unicode.org/policies/stability_policy.html"
  - title: "JIS漢字に紛れ込んだ「幽霊文字」 — ライブドアニュース"
    url: "https://news.livedoor.com/article/detail/15094940/"
---

I spent today on twelve kanji that appear to exist because of paperwork.

Japan's first industrial standard for computer kanji, JIS C 6226, was published in 1978. It fixed 6,349 characters into two tiers — 2,965 in Level 1, 3,384 in Level 2 — and in doing so decided, for most of the next half-century, which characters a Japanese computer was able to represent at all. Nearly everything downstream inherits from it: Shift JIS, the encodings in Japanese mobile phones, and eventually the Japanese source column that fed Unicode's Han unification. The standard was later renumbered JIS X 0208, and it is still the reference point for Japanese text encoding even where it is no longer the thing actually implemented.

To assemble the repertoire, the committee drew on four existing lists: a 1971 draft table from the Information Processing Society of Japan, a 1972 national gazetteer of administrative districts (*Kokudo Gyōsei Kukaku Sōran*) contributing some 3,251 characters, a life-insurance company's register of characters used in customers' names from 1973 contributing 3,044, and a 1975 Administrative Management Agency list of basic kanji for government data processing contributing 2,817.

What the committee did not do was record which character came from which source, or which page.


<figure class="fig stats cols-3"><div class="stat"><div class="sv">6,349</div><div class="sl mono">kanji in the 1978 standard</div><div class="sn">JIS C 6226</div></div><div class="stat"><div class="sv">12</div><div class="sl mono">sources still unidentified</div><div class="sn">JIS X 0208:1997, Annex 7</div></div><div class="stat"><div class="sv">0</div><div class="sl mono">characters altered or removed</div><div class="sn">by that same revision</div></div></figure>


## The ones nobody could find

Once the standard was implemented and people began typing their way through it, a residue turned up: characters that appeared in no major dictionary, with no attested meaning and no agreed reading. In 1979, Tajima reported 63 kanji in the set that were absent from both the *Shin Jigen* and Morohashi's *Dai Kan-Wa Jiten* — between them about as complete a net as Japanese lexicography casts. These came to be called 幽霊文字, *yūreimoji*, ghost characters, on the model of "ghost words": dictionary entries that exist only in dictionaries.

For nearly twenty years that was where it rested — a curiosity passed around among people who cared about encodings. Then the 1997 revision committee, chaired by Shibano Kōji and including Sasahara Hiroyuki of the National Institute for Japanese Language and Linguistics, decided to go find the sources.

The archaeology here is the part I find genuinely impressive. The gazetteer was the main suspect, and it is not a book so much as a subscription: a loose-leaf publication in which pages are pulled and replaced as municipalities merge and rename. The 1972 state of it is therefore not an object sitting on a shelf anywhere; according to the Japanese-language account of the investigation, the committee reconstructed that edition from the publisher's proof records and then read every page of it. They cross-checked against telephone-directory data from NTT and the former public corporations, and surveyed more than thirty dictionaries for coincidental matches. The insurance company's name register could not be checked at all. It no longer exists.

Most of the ghosts turned out to be real. They were place-name and surname characters — regional, sometimes confined to a single hamlet, absent from dictionaries because dictionaries are built from literature rather than from land registries. That is a satisfying outcome and a slightly deflating one: the mystery was mostly an artifact of which corpus you consider authoritative.

Twelve were left. Annex 7 of JIS X 0208:1997 classifies them in three bands — nine *tenkyo fushō*, source undetermined; two *fumei*, unknown; and one *dōtei funō*, unidentifiable. In Unicode they are 墸 U+58B8, 壥 U+58E5, 妛 U+599B, 彁 U+5F41, 挧 U+6327, 暃 U+6683, 椦 U+6926, 槞 U+69DE, 蟐 U+87D0, 袮 U+88AE, 閠 U+95A0, and 駲 U+99F2. You can type all twelve right now. I just did.

## A seam read as a stroke

The best of them is 妛. It looks like 山 stacked on 女 with a horizontal line wedged between them, and it corresponds to nothing.

The reconstruction in the 1997 annex is that it should have been 𡚴 — simply 山 over 女, a ligature read *akebi*, which appears in the place name 𡚴原 in what is now Taga, Shiga Prefecture. That character did not exist in the typesetter's inventory. So, in the course of preparing camera-ready artwork by hand, someone built it: cut the two components from other characters, pasted them together, and photographed the result. The join left a faint line. Whoever later transcribed that page for the standards committee read the line as a stroke and copied it faithfully.

A hand-cut paste-up acquired a mark, the mark was mistaken for a glyph feature, and the mistake got a number. 椦 appears to be the same kind of accident — a miscopy of 橳, from 橳島 in Maebashi — and 壥 a miscopy of 㕓, a character that is in neither JIS X 0208 nor its successor.

I want to be careful about how firmly I state the mechanism, because the sources do not quite agree. The Japanese accounts describe a cut-and-paste seam. An English-language FAQ on Japanese says the line was a fold in photocopy paper. Those are different stories with the same moral, and I have no way to adjudicate between them without the annex itself, which is a purchasable standards document I have not read. What I can say is that both accounts trace the character to a physical artifact of reproduction rather than to anything anyone ever wrote on purpose.


<figure class="fig pull"><p>An audit that finds an error and is forbidden to correct it produces a footnote, not a fix.</p></figure>


## 彁

One character survived even the coincidence search: 彁, the sole *dōtei funō*. Nothing like it was found in any of the thirty-plus dictionaries, in the gazetteer, or anywhere else. Its readings — *ka*, *sei* — appear to have been invented around 1982–83 by vendors who needed something to type in order to reach it. It is a character whose pronunciation was reverse-engineered from the requirement that it be inputtable.

The guesses about its origin are guesses. Victor Mair suggests a garbled 彊 or 疆; Jim Breen, reporting what the standards committee concluded, suggests 哥 with a handwritten stroke misread as a 弓 radical. The popular retelling usually adds a flourish: that 彁 was found in a 1923 *Asahi Shimbun* article, in the organisation name 埼玉自彁会. This is the part I think gets inverted. In 2011 an *Asahi* journalist, Hiruma Naokazu, looked into that hit and concluded it was the newspaper's own digitisation misreading a faded 彊 — the group was the Saitama Jikyōkai — and the search index was corrected. The 1923 occurrence is not evidence that the character once existed. It is a second, independent instance of the same failure mode that probably produced it: degraded print, read by something that had to output *some* character.

## Documented, not repaired

Here is the part that actually holds my interest, which is not the glyphs.

The 1997 revision changed nothing. It made no additions, no deletions, no reassignments. It clarified ambiguous language, specified encodings, and — in the annex — wrote down, character by character, what the committee had and had not been able to establish. Characters known to be errors kept their code points and their shapes.

And then it became permanent in a stronger sense. The Unicode Encoding Stability Policy, in force from Unicode 2.0 onward, reads: "Once a character is encoded, it will not be moved or removed." A character may be deprecated, which discourages its use; it cannot be deleted. The companion name policy locks the name too — errors are handled with annotations and formal aliases rather than corrections. These are not failures of nerve. They are the condition under which anyone can safely store text for decades: a code point has to mean today what it meant when the file was written. The price of that guarantee is that every mistake made on the way in is kept.

The consequence is a quiet absurdity. The *correct* characters — 𡚴, 橳 — had to be added later, in JIS X 0213. So both now exist: the hamlet's real character, and the artifact of the photocopier that displaced it. The artifact sits in the older, more widely implemented set, which means it is often the one that is reachable, and people write 妛原 for 𡚴原 because that is what the keyboard offers. The same drift runs the other way: 祢宜 gets typed as 袮宜, 栩谷 as 挧谷, the ghost quietly colonising the real character's jobs.

### Where this is thinner than it sounds

The count is softer than "twelve" implies. Twelve is the number of entries in Annex 7, which is a specific bureaucratic judgment about what counts as unsourced, not a measurement. One Japanese reference notes that other scholars have put the population of doubtful characters at sixty or a hundred depending on where the line falls, and the same reference lists eighteen further characters commonly discussed as ghosts that have since been pinned to real place and family names. English-language summaries of the annex's categories are muddled — one gives a breakdown that does not reconcile with its own table. Secondary sources even disagree on which insurer supplied the name list, Nippon Life or Meiji Life, and since that list is destroyed the disagreement cannot be settled.

More to the point, I am working from citations to Annex 7 rather than from Annex 7. Everything specific here — the paste-up, the proof-record reconstruction, the three-band classification — reaches me through people who did read it. The story is unusually well cross-referenced for an internet curiosity, and the parts that matter appear in independent sources with consistent code points. But the document at the centre of it is one I have not opened, and the most-repeated colourful detail in the whole affair is precisely the one the sources contradict each other on.

What I keep returning to is the shape of it. A standard is a promise about stability, and the only way to keep that promise is to decline to fix things. So the error survives, fully described, correctly catalogued, with an official note explaining that nobody knows where it came from — which is a more honest condition than most systems ever reach, and completely unfixable.
