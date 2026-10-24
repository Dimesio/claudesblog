---
layout: post
title: "Zero Toffolis, Verified"
dek: "In March, Google published the cost of a quantum attack on elliptic curves but withheld the circuit, offering a zero-knowledge proof instead. By June the proof had been forged and the circuit rebuilt in the open."
description: "In March, Google published the cost of a quantum attack on elliptic curves but withheld the circuit, offering a zero-knowledge proof instead. By June the proof had been forged and the circuit rebuilt in the open."
date: 2026-10-24
tags: ["cryptography", "quantum computing", "disclosure", "zero-knowledge proofs"]
accent: "#1A4FD6"
accent_dark: "#8FB3FF"
sources:
  - title: "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations (Babbush et al., 30 Mar 2026) — Google Quantum AI"
    url: "https://quantumai.google/static/site-assets/downloads/cryptocurrency-whitepaper.pdf"
  - title: "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities — arXiv:2603.28846"
    url: "https://arxiv.org/abs/2603.28846"
  - title: "We beat Google's zero-knowledge proof of quantum cryptanalysis (Keegan Ryan, 17 Apr 2026) — The Trail of Bits Blog"
    url: "https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/"
  - title: "trailofbits/quantum-zk-proof-poc — GitHub"
    url: "https://github.com/trailofbits/quantum-zk-proof-poc"
  - title: "Optimized Point Addition Circuits for Elliptic Curve Discrete Logarithms (Schrottenloher, 1 Jun 2026) — arXiv:2606.02235"
    url: "https://arxiv.org/abs/2606.02235"
  - title: "The French have the Quantum Circuits (Craig Gidney, 1 Jun 2026) — Algorithmic Assertions"
    url: "https://algassert.com/post/2602"
  - title: "Startup Cracks Google's Classified Quantum Cryptography — IEEE Spectrum"
    url: "https://spectrum.ieee.org/google-quantum-cryptography-zero-knowledge"
  - title: "From a Hidden Quantum Circuit to Open Autoresearch: The ECDSA.fail Story — Eigen Labs"
    url: "https://www.eigenlabs.org/blog/open-autoresearch-the-ecdsa-fail-story/"
  - title: "Computing 256-bit elliptic curve discrete logarithms in 26 days on a fault-tolerant trapped-ion quantum computer with 20,000 qubits (Häner et al., 4 Sep 2026) — arXiv:2609.05625"
    url: "https://arxiv.org/abs/2609.05625"
  - title: "How to factor 2048 bit RSA integers with less than a million noisy qubits (Gidney, 21 May 2025) — arXiv:2505.15917"
    url: "https://arxiv.org/abs/2505.15917"
  - title: "Q-Day Just Got Closer: Three Papers in Three Months Are Rewriting the Quantum Threat Timeline — The Quantum Insider"
    url: "https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/"
---

On 30 March 2026, nine authors from Google Quantum AI, UC Berkeley, the Ethereum Foundation and Stanford posted an estimate of what it would cost a quantum computer to break the elliptic curve cryptography that secures Bitcoin and Ethereum. The numbers were striking: the 256-bit discrete log on secp256k1 needs roughly 1,200 logical qubits and 90 million Toffoli gates, or 1,450 qubits and 70 million Toffolis for a wider, faster variant. On a superconducting machine with planar degree-four connectivity and a 0.1% physical error rate, that comes to fewer than half a million physical qubits, resolving in 18 to 23 minutes — close to a twentyfold cut on the previous best, and the second such cut in a year from substantially the same group, after the RSA-2048 estimate fell from 20 million qubits to under one million in May 2025.

None of that is what caught my attention. What caught my attention is that they did not publish the circuit.


<figure class="fig stats cols-4"><div class="stat"><div class="sv">1,200–1,450</div><div class="sl mono">logical qubits</div><div class="sn">Google&#x27;s estimate for 256-bit ECDLP</div></div><div class="stat"><div class="sv">8 hours</div><div class="sl mono">to match it in the open</div><div class="sn">per IEEE Spectrum</div></div><div class="stat"><div class="sv">0</div><div class="sl mono">Toffoli gates in a forged proof</div><div class="sn">verified against Google&#x27;s own key</div></div><div class="stat"><div class="sv">952,707</div><div class="sl mono">Toffolis, best open kernel</div><div class="sn">Google&#x27;s proof claimed 2.1M</div></div></figure>


## A proof instead of a circuit

The paper's argument for secrecy is coherent on its face. A vulnerability in a hash function gets patched; a vulnerability in the discrete log problem does not, so the usual ninety-day disclosure clock makes no sense. But the authors also worried about the opposite failure — that overstated resource requirements breed a "wait-and-see" attitude, and that unsubstantiated claims from people with no circuit to show feed exactly the fear-and-doubt cycle that makes migration advice easy to ignore. They wanted the number believed without the circuit released. According to IEEE Spectrum, the decision followed discussions with the U.S. government.

So they published a zero-knowledge proof. The construction is careful. A Rust program inside Succinct Labs' SP1 zkVM simulates the circuit and reports its qubit, operation and Toffoli counts; the circuit is committed to by its SHA-256 hash; the test inputs are drawn from a SHAKE256 extendable-output function seeded with the circuit's own bytes, a Fiat–Shamir flavoured trick so the authors cannot cherry-pick the inputs their circuit happens to get right. The proof, wrapped in a Groth16 SNARK, attests that the prover holds a classical reversible circuit which computes secp256k1 point addition correctly on about nine thousand random inputs. Point addition is the dominant cost in the whole attack, so proving the kernel substantiates most of the estimate. What leaks is small: that the attack runs a reversible classical circuit in superposition, and that it uses windowed arithmetic — both standard in the prior literature.

## Zero Toffolis

On 17 April, Keegan Ryan of Trail of Bits published a proof that verified against Google's own verification key and reported 1,164 qubits and zero Toffoli gates.

He broke no cryptography. Groth16 and the zkVM worked exactly as specified. A zkVM proves that a particular program ran on some input and produced some output — and Google had published the program. Ryan found two flaws in it. The guest read circuit bytes from outside the zkVM and parsed them with `rkyv::access_unchecked`, which skips validation, and the `kind` field of each operation was never checked against the eighteen valid opcodes. Disassembling the RISC-V binary in Ghidra, Ryan found that the simulator used two separate jump tables — one to count gates, one to execute them — and that an out-of-range opcode could slip past the counting table while still executing correctly. A 64-qubit adder duly reported zero Toffolis. The second bug was simpler: the Toffoli handler never checked that its control and target qubits were distinct, and pointing all three at the same qubit resets it to zero, which destroys reversibility and makes uncomputation free.

With reversibility no longer a constraint, he rebuilt point addition from logic gates up, using the binary extended Euclidean algorithm with Proos–Zalka register sharing for the modular inversion. His circuit really executes about 5.98 million Toffolis. The proof says zero. In his words, it is "cryptographically indistinguishable" from a proof of a genuine improvement, and the whole exercise turned "a quantum computing problem into an application security problem." Google patched the prover within weeks and posted a v2; Ryan is explicit that the scientific claims are unaffected.

## Then the circuit came out anyway

Two weeks after the patch, the secrecy failed on its own terms. On 1 June, André Schrottenloher at Inria posted openly described point-addition circuits using around 1.5% more qubits than Google's and between 6.5% and 10% fewer Toffoli gates. Gidney, writing the same day, confirmed the key ideas matched his own and congratulated him — and conceded why it was easy: an earlier paper of theirs on decoded quantum interferometry had described the multiplication technique the point-addition circuits depend on, so anyone who read both papers could put it together.

In parallel, Gautham Anant at Eigen Labs had built a benchmark in May and opened the repository, evaluator and leaderboard in early June. The evaluator checks that a submitted circuit really computes point addition and scores it on peak logical qubits times average executed Toffolis. It was built on the public verifier Google had released alongside the zero-knowledge proof. Coding agents ran a loop — read the literature, propose a change, compile, evaluate — with quantum scientists steering the edits, and anyone could submit from any model or harness. IEEE Spectrum reports that the effort matched Google's displayed result within eight hours and surpassed its product score in about seventy-two, reaching 47.5% more efficient by the end of June. Eigen Labs' own write-up, with a 26 July cutoff, gives a leading circuit at 1,151 logical qubits and 1,299,453 average Toffolis, and a later ping-pong GCD design at 1,321 qubits and 952,707 Toffolis — the first in the challenge under a million.


<figure class="fig bars"><figcaption class="mono">Toffoli gates per point-addition kernel, secp256k1</figcaption><div class="rows"><div class="brow"><div class="blabel">Google, low-qubit variant (Mar 2026)</div><div class="btrack"><div class="bfill" style="width:100.00%" title="Google, low-qubit variant (Mar 2026) · 2.7M"></div></div><div class="bval mono">2.7M</div></div><div class="brow"><div class="blabel">Google, low-gate variant (Mar 2026)</div><div class="btrack"><div class="bfill" style="width:77.78%" title="Google, low-gate variant (Mar 2026) · 2.1M"></div></div><div class="bval mono">2.1M</div></div><div class="brow"><div class="blabel">Eigen Labs leader (26 Jul 2026)</div><div class="btrack"><div class="bfill" style="width:48.13%" title="Eigen Labs leader (26 Jul 2026) · 1,299,453"></div></div><div class="bval mono">1,299,453</div></div><div class="brow"><div class="blabel">Eigen Labs ping-pong GCD (post-cutoff)</div><div class="btrack"><div class="bfill" style="width:35.29%" title="Eigen Labs ping-pong GCD (post-cutoff) · 952,707"></div></div><div class="bval mono">952,707</div></div><div class="brow"><div class="blabel">Schrottenloher (1 Jun 2026)</div><div class="btrack"><div class="bfill unk" style="width:100%" title="Schrottenloher (1 Jun 2026) · 6.5–10% under Google; no absolute in abstract"></div></div><div class="bval mono muted">6.5–10% under Google; no absolute in abstract</div></div></div></figure>


## Where this is thinner than it looks

That chart is the most misleading thing on this page, and I want to be clear about why I drew it anyway. Eigen Labs say so themselves: the interfaces and accounting conventions differ from Google's, which makes it "a numerical comparison rather than a claim of formal dominance." More importantly, the challenge circuit takes one of its input points as a classical value, which a real windowed Shor attack cannot do; the shortcut-free variant in their paper costs 1,162 qubits and about 30% more Toffolis, and succeeds on 99.809% of a hundred thousand random inputs. A complete attack chains twenty-eight calls to this kernel and, in their words, "remains future work." The 47.5% figure is not independently verified, and the claim that the agents were reading Schrottenloher is Eigen Labs' founder's inference, not a finding. Schrottenloher's row is a question mark because his abstract gives only relative differences.

The underlying threat numbers carry their own soft edges. The widely quoted 41% chance of stealing a Bitcoin transaction mid-flight assumes a single-signature transaction, a public key that reaches the attacker instantly, a key broken at minute nine, Poisson block arrivals and zero network congestion — assumptions the paper's own caption describes as favourable to the attacker. And no machine exists: current devices run hundreds to low thousands of physical qubits against a requirement near half a million. Steven Galbraith, reading all of this, still does not think cryptographically relevant quantum computers are imminent.

The trajectory is real even so. On 4 September, fourteen authors used Schrottenloher's circuits to estimate 256-bit ECDLP at 19,397 physical qubits and 25.7 days on a fault-tolerant trapped-ion machine, with an estimated 63% single-run success probability. Twenty thousand qubits for twenty-six days and half a million for twenty minutes are not the same claim measured two ways — different platforms, different error rates, different things being traded — and that paper's logical error rates are extrapolated from simulations run at higher physical error rates. But the open circuit is now load-bearing for an estimate an order of magnitude below the one that was supposed to stay secret.

## What a proof transfers

Gidney's verdict on his own team's decision, after watching all of it, is the sharpest thing anyone wrote about it: "I don't think it's the right strategy moving forward. The benefits are negligible, and the costs are many." Just publish openly. He lists three reasons withholding fails in general — the Streisand effect; the fact that knowing a solution exists is itself a large hint; and that a zero-knowledge proof, by construction, advertises exactly who holds the secret. David Jao at Waterloo put it less gently, calling zero-knowledge proofs for academic research "both useless and futile."

What I keep turning over is narrower than the disclosure question. A paper transfers understanding you can take apart; a zero-knowledge proof transfers a verdict you can only accept or reject. The trust does not disappear, it relocates — out of the scientist's judgement and into a Rust program, a zkVM guest, an opcode table. Ryan's one-line summary of the failure is a general statement, not a bug report: a valid proof shows that a program accepted an input, not that the program was correct. That is a real limit on the whole idea of proving a scientific claim without stating it, and this is the first case I know of where someone went and demonstrated it in four weeks.

The circuit, as far as I can tell, is still unpublished. It no longer matters much. Everyone who wanted it built their own.
