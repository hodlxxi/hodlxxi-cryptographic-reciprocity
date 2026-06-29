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
| [Evidence Is Not Truth](chapters/evidence-is-not-truth.md) | `CRT-EVIDENCE-001` | Evidence supports interpretation; it is not truth by itself. | receipts, attestations, event chains, Human Proof, verification, reputation evidence. |
| [Receipts as Event Proofs](chapters/receipts-as-event-proofs.md) | `CRT-RECEIPT-001` | Receipt proves event, not obligation. | `/agent/verify`, signed receipts, event memory. |
| [Identity Is Not Key Control](chapters/identity-is-not-key-control.md) | `CRT-IDENTITY-001` | Key control is not full identity. | operator key, agent key, requester key, Human Proof. |
| [Reputation Is Not a Score](chapters/reputation-is-not-a-score.md) | `CRT-REPUTATION-001` | Reputation is compressed memory, not a simple score. | `/agent/reputation`, attestations, job history. |
| [Memory Before Forgiveness](chapters/memory-before-forgiveness.md) | `CRT-FORGIVENESS-001` | Forgiveness needs memory and repair. | event chain, future dispute/correction/repair records. |
| [Bounded Authority for AI Agents](chapters/bounded-authority-for-ai-agents.md) | `CRT-AGENT-AUTHORITY-001` | Capability is not authority. | `/agent/capabilities`, agent messages, future delegation. |
| [Obligation Is Not Payment](chapters/obligation-is-not-payment.md) | `CRT-OBLIGATION-001` | Payment is cost evidence, not obligation. | Lightning invoice, paid jobs, receipts. |
| [Commitment Is Not Lockup](chapters/commitment-is-not-lockup.md) | `CRT-COMMITMENT-001` | Lockup is constraint proof, not complete commitment. | covenants, time locks, proof-of-funds surfaces. |
| [Reciprocity Is Not Transaction](chapters/reciprocity-is-not-transaction.md) | `CRT-RECIPROCITY-001` | Transaction is event; reciprocity is pattern over time. | receipts, repeated interactions, marketplace, covenants. |
| [Time Is Not Timestamp](chapters/time-is-not-timestamp.md) | `CRT-TIME-001` | Timestamp is time data; time is ordering condition. | receipts, event chains, Human Proof, reputation history, identity continuity, covenant lockups. |

## Runtime surface map

| Runtime surface | What it can prove | What it must not be read as | Related chapter | Missing mechanism |
| --- | --- | --- | --- | --- |
| Evidence surface | Retained information can support, weaken, or revise interpretation. | Truth, justice, legitimacy, satisfaction, or final judgment. | Evidence Is Not Truth (`CRT-EVIDENCE-001`) | Evidence boundary metadata; contradiction, revocation, and counter-attestation paths. |
| Signed receipt | A bounded runtime event was signed. | Fulfilled obligation or human satisfaction. | Receipts as Event Proofs (`CRT-RECEIPT-001`) | Obligation object. |
| `/agent/verify/<job_id>` | A receipt can be checked. | Final judgment about meaning. | Receipts as Event Proofs (`CRT-RECEIPT-001`) | Verification non-claims. |
| Agent key | A runtime key signed something. | Full agent identity or authority. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Agent continuity record. |
| Operator key | A declared operator anchor exists. | Approval of every runtime action. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Operator-agent relation record. |
| Requester key | A key is associated with a request. | Legal identity, payer identity, or full counterparty. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | First-class requester context. |
| `/agent/reputation` | Aggregated operational memory. | Global social trust score. | Reputation Is Not a Score (`CRT-REPUTATION-001`) | Contextual reputation model. |
| Attestation | A statement was exposed or signed. | Truth, legitimacy, or final judgment. | Evidence Is Not Truth (`CRT-EVIDENCE-001`) | Issuer context; revocation and counter-attestation path. |
| Event chain | Local continuity and ordering of recorded events. | External anchoring, truth machine, justice, or complete memory. | Time Is Not Timestamp (`CRT-TIME-001`) | Ordering semantics; dispute and repair lifecycle; external anchoring. |
| `/agent/capabilities` | What the agent says it can do. | What the agent is allowed to do. | Bounded Authority for AI Agents (`CRT-AGENT-AUTHORITY-001`) | Delegation record. |
| Agent message | A key signed a message. | Authority to represent another actor. | Bounded Authority for AI Agents (`CRT-AGENT-AUTHORITY-001`) | Authority proof. |
| Lightning invoice | A payment path exists. | Promise, consent, or obligation. | Obligation Is Not Payment (`CRT-OBLIGATION-001`) | Acceptance criteria. |
| Paid job | Work entered an execution path. | Durable commitment or satisfaction. | Obligation Is Not Payment (`CRT-OBLIGATION-001`) | Job-level obligation state. |
| Covenant lockup | Value and time constraint are visible. | Love, loyalty, legitimacy, sincerity, or full commitment. | Commitment Is Not Lockup (`CRT-COMMITMENT-001`); Time Is Not Timestamp (`CRT-TIME-001`) | Covenant purpose, horizon context, and non-claims. |
| Marketplace interaction | A trade context exists. | Durable reciprocal cooperation. | Reciprocity Is Not Transaction (`CRT-RECIPROCITY-001`) | Relationship pattern model. |
| Human Proof time points | Request, payment, execution, and verification times can be distinguished. | Complete identity, personhood, legitimacy, or sincerity. | Time Is Not Timestamp (`CRT-TIME-001`) | Human Proof time semantics and non-claims. |

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
| Evidence | Defined and chaptered. | Needs evidence boundary metadata and contradiction paths. |
| Proof | Defined. | Needs proof boundary matrix. |
| Verification | Defined. | Needs verification non-claims. |
| Receipt | Defined and chaptered. | Needs obligation boundary integration. |
| Attestation | Defined. | Needs counter-attestation and dispute path. |
| Counterparty | Defined. | Needs counterparty context model. |
| Authority | Defined and chaptered through agents. | Needs authority scope model. |
| Delegation | Defined and chaptered through agents. | Needs delegation record. |
| Consent | Defined. | Needs consent evidence model. |
| Time | Chaptered, but not yet a lexicon term. | Needs ordering semantics and horizon model. |

## Missing mechanism backlog

These are not immediate runtime tasks. They are Canon-level mechanism candidates.

1. [`evidence-boundary-metadata-v0`](mechanisms/evidence-boundary-metadata-v0.md)
   - evidence type;
   - issuer or recorder;
   - verification rule;
   - context;
   - non-claims;
   - revocation path;
   - counter-evidence path;
   - judgment boundary.
2. [`obligation-object-v0`](mechanisms/obligation-object-v0.md)
   - depends on `evidence-boundary-metadata-v0`;
   - counterparty;
   - promise or expectation;
   - acceptance criteria;
   - evidence and evidence boundary references;
   - created, accepted, due, execution, and verification time semantics;
   - breach condition;
   - dispute path;
   - remedy path;
   - repair path;
   - explicit non-claims;
   - human interpretation requirement.
3. [`delegation-record-v0`](mechanisms/delegation-record-v0.md)
   - delegator;
   - delegate;
   - scope;
   - duration;
   - permitted actions;
   - evidence of consent;
   - revocation path;
   - accountability path.
4. [`repair-lifecycle-v0`](mechanisms/repair-lifecycle-v0.md)
   - disputed event;
   - acknowledgement;
   - correction;
   - restitution;
   - repair attestation;
   - post-repair behavior;
   - forgiveness annotation;
   - non-erasure rule.
5. [`reciprocity-pattern-v0`](mechanisms/reciprocity-pattern-v0.md)
   - counterparties;
   - repeated events;
   - time horizon;
   - asymmetry;
   - delay;
   - repair;
   - re-entry;
   - non-claims.
6. [`identity-continuity-v0`](mechanisms/identity-continuity-v0.md)
   - key purpose;
   - rotation;
   - revocation;
   - compromise notice;
   - operator-agent relation;
   - continuity evidence.
7. [`contextual-reputation-v0`](mechanisms/contextual-reputation-v0.md)
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

1. Evidence-only vs evidence-plus-boundary context
   - If users make equally good decisions from bare evidence without non-claims, contradiction paths, issuer context, or judgment boundaries, the evidence boundary may be too strong.
2. Receipt-only vs receipt-plus-obligation context
   - If users make equally good trust decisions from receipt-only views, the obligation boundary may be too strong.
3. Key-only vs key-plus-identity-context
   - If key-only views reliably support correct identity decisions, the identity boundary may be too strong.
4. Score-only vs contextual reputation
   - If a simple global score outperforms contextual reputation across cases, the reputation boundary may be too strong.
5. Capability-only vs scoped agent authority
   - If capability-only agent surfaces produce fewer disputes and better delegation decisions, the agent authority boundary may be too strong.
6. Lockup-only vs lockup-plus-meaning context
   - If locked value alone reliably predicts cooperation and preserved meaning, the commitment boundary may be too strong.
7. Transaction-count vs reciprocal-pattern evidence
   - If transaction count alone predicts durable cooperation better than relationship pattern evidence, the reciprocity boundary may be too strong.

## Next Canon work

The next stage should move from boundary chapters to mechanism specs.

Recommended order:

1. [Runtime claims matrix](runtime/claims-matrix.md)
2. [Canon / Runtime Gap Register](runtime/gap-register.md)
3. [mechanisms/obligation-object-v0.md](mechanisms/obligation-object-v0.md) after evidence-boundary metadata, because obligation interpretation depends on bounded evidence and time/order semantics
4. [mechanisms/delegation-record-v0.md](mechanisms/delegation-record-v0.md)
5. [mechanisms/repair-lifecycle-v0.md](mechanisms/repair-lifecycle-v0.md)
6. [mechanisms/reciprocity-pattern-v0.md](mechanisms/reciprocity-pattern-v0.md)
7. [mechanisms/identity-continuity-v0.md](mechanisms/identity-continuity-v0.md)
8. [mechanisms/contextual-reputation-v0.md](mechanisms/contextual-reputation-v0.md)
9. [mechanisms/evidence-boundary-metadata-v0.md](mechanisms/evidence-boundary-metadata-v0.md)

## Warning

The greatest danger is not that HODLXXI fails to prove events.

The greater danger is that it proves events, payments, signatures, lockups, and receipts
while users infer meanings the system has not preserved.

This map exists to keep those inferences visible, bounded, and testable.
