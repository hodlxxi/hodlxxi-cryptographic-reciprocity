# CRT Canon Claim Registry

This file is the central registry of stable CRT Canon claim IDs.

Claim IDs are not doctrine. They are addressable, falsifiable research claims that help
chapters, runtime surfaces, mechanisms, and tests refer to the same bounded claim without
expanding its meaning. Runtime mechanisms may cite these IDs, but must not claim stronger
meaning than the registered claim supports.

| Claim ID | Source chapter | Claim | Runtime relevance | Status |
| --- | --- | --- | --- | --- |
| `CRT-RECEIPT-001` | [Receipts as Event Proofs](chapters/receipts-as-event-proofs.md) | A receipt is evidence that a bounded runtime event occurred; it is not evidence of obligation fulfillment, human satisfaction, or trustworthiness. | Signed receipts, `/agent/verify`, and event memory must expose receipt boundaries and avoid satisfaction or obligation claims without additional context. | active |
| `CRT-IDENTITY-001` | [Identity Is Not Key Control](chapters/identity-is-not-key-control.md) | Key control is evidence of control over a cryptographic capability; it is not full identity. | Operator keys, agent keys, requester keys, and Human Proof need continuity, role, recovery, and non-claim context before identity claims are strengthened. | active |
| `CRT-OBLIGATION-001` | [Obligation Is Not Payment](chapters/obligation-is-not-payment.md) | Payment is cost evidence; it is not obligation. | Lightning invoices, paid jobs, and receipts need obligation objects, acceptance criteria, and settlement context before fulfillment or satisfaction claims are made. | active |
| `CRT-REPUTATION-001` | [Reputation Is Not a Score](chapters/reputation-is-not-a-score.md) | Reputation is compressed memory; a score is only one possible compression and often a dangerous one. | Reputation endpoints, attestations, marketplace listings, and job history must preserve context, uncertainty, and non-score presentation. | active |
| `CRT-COMMITMENT-001` | [Commitment Is Not Lockup](chapters/commitment-is-not-lockup.md) | A lockup is a constraint proof; it is not a complete commitment proof. | Covenants, time locks, proof-of-funds surfaces, and participant keys need purpose, consent, release, dispute, and non-claim context. | active |
| `CRT-AGENT-AUTHORITY-001` | [Bounded Authority for AI Agents](chapters/bounded-authority-for-ai-agents.md) | AI agents should operate only within visible, scoped, revocable, and accountable authority; capability is not authority. | Agent capabilities, requests, and messages need delegation records, authority scope, expiry, revocation, and accountability before authority claims are made. | active |
| `CRT-FORGIVENESS-001` | [Memory Before Forgiveness](chapters/memory-before-forgiveness.md) | Forgiveness requires memory: without preserved memory of harm, repair, and changed behavior, forgiveness collapses into forgetting or erasure. | Event chains and trust events need repair, dispute, correction, and audit context before supporting forgiveness or restored-trust claims. | active |
| `CRT-RECIPROCITY-001` | [Reciprocity Is Not Transaction](chapters/reciprocity-is-not-transaction.md) | Reciprocity is not a transaction; it is a pattern across events, actors, memory, expectation, and time. | Marketplace interactions, receipts, repeated interactions, and covenants need relationship memory, counterparty context, expectations, asymmetry, and repair links before reciprocity claims are made. | active |
