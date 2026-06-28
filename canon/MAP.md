# CRT Canon Map

## Purpose

This map connects Canon language to chapters, runtime surfaces, missing mechanisms, and
falsification paths.

Its purpose is to prevent HODLXXI from becoming a collection of essays or isolated
documents.

Every major claim should eventually be traceable through this chain:

```text
Lexicon term -> Canon chapter -> runtime surface -> missing mechanism -> falsification test
```

The map is provisional. It should change as runtime evidence changes.

## Map rule

A Canon claim is not complete until it can answer:

1. What term does it define or constrain?
2. Which chapter develops it?
3. Which runtime surface currently touches it?
4. What does the runtime surface prove?
5. What does the runtime surface not prove?
6. What mechanism is missing?
7. What observation would weaken or falsify the claim?

## Current chapter layer

The stable claim IDs in this chapter layer are centrally registered in the [CRT Canon Claim Registry](CLAIMS.md).

| Chapter | Claim ID | Primary boundary | Runtime relevance |
| --- | --- | --- | --- |
| [Receipts as Event Proofs](chapters/receipts-as-event-proofs.md) | `CRT-RECEIPT-001` | Receipt proves event, not obligation. | `/agent/verify`, signed receipts, event memory. |
| [Identity Is Not Key Control](chapters/identity-is-not-key-control.md) | `CRT-IDENTITY-001` | Key control is not full identity. | operator key, agent key, requester key, Human Proof. |
| [Reputation Is Not a Score](chapters/reputation-is-not-a-score.md) | `CRT-REPUTATION-001` | Reputation is compressed memory, not a simple score. | `/agent/reputation`, attestations, job history. |
| [Memory Before Forgiveness](chapters/memory-before-forgiveness.md) | `CRT-FORGIVENESS-001` | Forgiveness needs memory and repair. | event chain, future dispute/correction/repair records. |
| [Bounded Authority for AI Agents](chapters/bounded-authority-for-ai-agents.md) | `CRT-AGENT-AUTHORITY-001` | Capability is not authority. | `/agent/capabilities`, agent messages, future delegation. |
| [Obligation Is Not Payment](chapters/obligation-is-not-payment.md) | `CRT-OBLIGATION-001` | Payment is cost evidence, not obligation. | Lightning invoice, paid jobs, receipts. |
| [Commitment Is Not Lockup](chapters/commitment-is-not-lockup.md) | `CRT-COMMITMENT-001` | Lockup is constraint proof, not complete commitment. | covenants, time locks, proof-of-funds surfaces. |
| [Reciprocity Is Not Transaction](chapters/reciprocity-is-not-transaction.md) | `CRT-RECIPROCITY-001` | Transaction is event; reciprocity is pattern over time. | receipts, repeated interactions, marketplace, covenants. |

## Runtime surface map

| Runtime surface | What it can prove | What it must not be read as | Related chapter | Missing mechanism |
| --- | --- | --- | --- | --- |
| Signed receipt | A bounded runtime event was signed. | Fulfilled obligation or human satisfaction. | Receipts as Event Proofs (`CRT-RECEIPT-001`) | Obligation object. |
| `/agent/verify/<job_id>` | A receipt can be checked. | Final judgment about meaning. | Receipts as Event Proofs (`CRT-RECEIPT-001`) | Verification non-claims. |
| Agent key | A runtime key signed something. | Full agent identity or authority. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Agent continuity record. |
| Operator key | A declared operator anchor exists. | Approval of every runtime action. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Operator-agent relation record. |
| Requester key | A key is associated with a request. | Legal identity, payer identity, or full counterparty. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | First-class requester context. |
| `/agent/reputation` | Aggregated operational memory. | Global social trust score. | Reputation Is Not a Score (`CRT-REPUTATION-001`) | Contextual reputation model. |
| Attestation | A statement was exposed or signed. | Truth, legitimacy, or final judgment. | Reputation Is Not a Score (`CRT-REPUTATION-001`) | Counter-attestation path. |
| Event chain | Local continuity of recorded events. | External anchoring or justice. | Memory Before Forgiveness (`CRT-FORGIVENESS-001`) | Dispute and repair lifecycle. |
| `/agent/capabilities` | What the agent says it can do. | What the agent is allowed to do. | Bounded Authority for AI Agents (`CRT-AGENT-AUTHORITY-001`) | Delegation record. |
| Agent message | A key signed a message. | Authority to represent another actor. | Bounded Authority for AI Agents (`CRT-AGENT-AUTHORITY-001`) | Authority proof. |
| Lightning invoice | A payment path exists. | Promise, consent, or obligation. | Obligation Is Not Payment (`CRT-OBLIGATION-001`) | Acceptance criteria. |
| Paid job | Work entered an execution path. | Durable commitment or satisfaction. | Obligation Is Not Payment (`CRT-OBLIGATION-001`) | Job-level obligation state. |
| Covenant lockup | Value and time constraint are visible. | Love, loyalty, legitimacy, or full commitment. | Commitment Is Not Lockup (`CRT-COMMITMENT-001`) | Covenant purpose and non-claims. |
| Marketplace interaction | A trade context exists. | Durable reciprocal cooperation. | Reciprocity Is Not Transaction (`CRT-RECIPROCITY-001`) | Relationship pattern model. |

## Lexicon coverage

| Term | Current status | Main chapter pressure |
| --- | --- | --- |
| Trust | Defined, but not yet a mechanism. | Needs trust decision model. |
| Reciprocity | Defined and chaptered. | Needs reciprocal pattern model. |
| Promise | Defined, but underdeveloped. | Needs promise lifecycle. |
| Commitment | Defined and chaptered. | Needs commitment evidence model. |
| Obligation | Defined and chaptered. | Needs obligation object. |
| Memory | Defined and chaptered. | Needs durable memory and repair states. |
| Identity | Defined and chaptered. | Needs identity continuity/rotation model. |
| Reputation | Defined and chaptered. | Needs contextual reputation model. |
| Forgiveness | Defined and chaptered. | Needs repair lifecycle. |
| Legitimacy | Defined, but underdeveloped. | Needs legitimacy sources and limits. |
| Evidence | Defined. | Needs evidence taxonomy. |
| Proof | Defined. | Needs proof boundary matrix. |
| Verification | Defined. | Needs verification non-claims. |
| Receipt | Defined and chaptered. | Needs obligation boundary integration. |
| Attestation | Defined. | Needs counter-attestation and dispute path. |
| Counterparty | Defined. | Needs counterparty context model. |
| Authority | Defined and chaptered through agents. | Needs authority scope model. |
| Delegation | Defined and chaptered through agents. | Needs delegation record. |
| Consent | Defined. | Needs consent evidence model. |

## Missing mechanism backlog

These are not immediate runtime tasks. They are Canon-level mechanism candidates.

1. [`obligation-object-v0`](mechanisms/obligation-object-v0.md)
   - counterparty;
   - promise;
   - acceptance criteria;
   - time horizon;
   - breach condition;
   - dispute state;
   - remedy path;
   - repair state;
   - closure state.
2. [`delegation-record-v0`](mechanisms/delegation-record-v0.md)
   - delegator;
   - delegate;
   - scope;
   - duration;
   - permitted actions;
   - evidence of consent;
   - revocation path;
   - accountability path.
3. [`repair-lifecycle-v0`](mechanisms/repair-lifecycle-v0.md)
   - disputed event;
   - acknowledgement;
   - correction;
   - restitution;
   - repair attestation;
   - post-repair behavior;
   - forgiveness annotation;
   - non-erasure rule.
4. [`reciprocity-pattern-v0`](mechanisms/reciprocity-pattern-v0.md)
   - counterparties;
   - repeated events;
   - time horizon;
   - asymmetry;
   - delay;
   - repair;
   - re-entry;
   - non-claims.
5. [`identity-continuity-v0`](mechanisms/identity-continuity-v0.md)
   - key purpose;
   - rotation;
   - revocation;
   - compromise notice;
   - operator-agent relation;
   - continuity evidence.
6. [`contextual-reputation-v0`](mechanisms/contextual-reputation-v0.md)
   - reputation for what;
   - according to whom;
   - over what time period;
   - with what evidence;
   - under what dispute state;
   - after what repair.

## Falsification backlog

CRT should become weaker if evidence shows that its distinctions do not improve
decisions.

Initial falsification tests:

1. Receipt-only vs receipt-plus-obligation context
   - If users make equally good trust decisions from receipt-only views, the obligation boundary may be too strong.
2. Key-only vs key-plus-identity-context
   - If key-only views reliably support correct identity decisions, the identity boundary may be too strong.
3. Score-only vs contextual reputation
   - If a simple global score outperforms contextual reputation across cases, the reputation boundary may be too strong.
4. Capability-only vs scoped agent authority
   - If capability-only agent surfaces produce fewer disputes and better delegation decisions, the agent authority boundary may be too strong.
5. Lockup-only vs lockup-plus-meaning context
   - If locked value alone reliably predicts cooperation and preserved meaning, the commitment boundary may be too strong.
6. Transaction-count vs reciprocal-pattern evidence
   - If transaction count alone predicts durable cooperation better than relationship pattern evidence, the reciprocity boundary may be too strong.

## Next Canon work

The next stage should move from boundary chapters to mechanism specs.

Recommended order:

1. [Runtime claims matrix](runtime/claims-matrix.md)
2. [Canon / Runtime Gap Register](runtime/gap-register.md)
3. [mechanisms/obligation-object-v0.md](mechanisms/obligation-object-v0.md)
4. [mechanisms/delegation-record-v0.md](mechanisms/delegation-record-v0.md)
5. [mechanisms/repair-lifecycle-v0.md](mechanisms/repair-lifecycle-v0.md)
6. [mechanisms/reciprocity-pattern-v0.md](mechanisms/reciprocity-pattern-v0.md)
7. [mechanisms/identity-continuity-v0.md](mechanisms/identity-continuity-v0.md)
8. [mechanisms/contextual-reputation-v0.md](mechanisms/contextual-reputation-v0.md)

## Warning

The greatest danger is not that HODLXXI fails to prove events.

The greater danger is that it proves events, payments, signatures, lockups, and receipts
while users infer meanings the system has not preserved.

This map exists to keep those inferences visible, bounded, and testable.
