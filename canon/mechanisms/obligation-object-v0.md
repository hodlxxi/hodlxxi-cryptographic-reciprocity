# Minimum Obligation Object v0

## Purpose

This document defines the minimum conceptual object needed to represent an obligation in
HODLXXI.

An obligation is not created by payment alone. An obligation is not proven by receipt
alone. An obligation is not satisfied by execution alone. A receipt is not fulfillment,
and a timestamp is not obligation order by itself.

An obligation requires a bounded relation among actors, an explicit counterparty,
promise or expectation, acceptance criteria, time horizon, breach condition, and remedy
or repair path. Evidence may support interpretation of those fields, but evidence does
not settle the obligation by itself.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract,
legal contract template, or implementation claim.

## Canon claims and mechanism dependency

This mechanism cites existing Canon claims without changing their meanings.

| Claim ID | Source | Boundary used by this mechanism |
| --- | --- | --- |
| `CRT-OBLIGATION-001` | [Obligation Is Not Payment](../chapters/obligation-is-not-payment.md) | Payment, execution, or receipt evidence does not create or fulfill an obligation by itself. |
| `CRT-EVIDENCE-001` | [Evidence Is Not Truth](../chapters/evidence-is-not-truth.md) | Evidence supports obligation interpretation, but it does not settle truth, satisfaction, legitimacy, or breach. |
| `CRT-TIME-001` | [Time Is Not Timestamp](../chapters/time-is-not-timestamp.md) | Obligation order needs acceptance, horizon, execution, verification, and sequence context; a timestamp alone is not enough. |
| `CRT-RECEIPT-001` | [Receipts as Event Proofs](../chapters/receipts-as-event-proofs.md) | A receipt proves a bounded event, not fulfillment, satisfaction, repair, or obligation closure. |

Minimum Obligation Object v0 explicitly depends on
[`evidence-boundary-metadata-v0`](evidence-boundary-metadata-v0.md). Evidence linked to
an obligation should carry boundary metadata or be treated as incomplete evidence. The
obligation object should reference evidence boundary records through
`evidence_boundary_refs` rather than treating raw evidence as settled meaning.

Related Canon and runtime documents include the [Canon map](../MAP.md), the
[Runtime claims matrix](../runtime/claims-matrix.md), [Runtime non-claims](../runtime/non-claims.md),
and the [Canon / Runtime Gap Register](../runtime/gap-register.md).

## Problem

HODLXXI has payments, requests, receipts, verification, attestations, reputation
telemetry, event memory, Human Proof surfaces, covenant lockups, and marketplace
interactions.

These surfaces are useful, but users may infer stronger claims than the system
preserved:

- paid -> owed;
- paid -> fulfilled;
- executed -> fulfilled;
- receipt verified -> satisfied;
- timestamped first -> accepted first;
- Human Proof requested -> consent or authority proven;
- lockup present -> committed;
- marketplace interaction -> durable reciprocal obligation;
- attestation present -> settled.

The obligation object exists to prevent those false inference chains. It makes the
missing structure visible before HODLXXI presents stronger claims about promise,
acceptance, order, breach, repair, or closure.

## Non-goals

This document does not:

- create a legal contract system;
- define enforceable law;
- require every small paid job to become heavy bureaucracy;
- prove human satisfaction;
- prove moral legitimacy;
- resolve all disputes;
- require all obligation details to be public;
- convert evidence boundary metadata into truth;
- convert timestamps into acceptance order;
- implement runtime code.

## Required fields

A minimum obligation object needs the following fields before HODLXXI can honestly model
an obligation.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `obligation_id` | A stable identifier for this obligation object. | Without a stable identifier, later evidence, disputes, remedies, repairs, and closure records cannot refer to the same bounded object. | It does not prove correctness, legitimacy, or enforceability. |
| `parties` | Actors, keys, organizations, agents, or humans involved in the obligation, including the explicit counterparty when known. | Obligation requires declared counterparties; payment or execution without counterparty context is not enough. | It does not prove full human identity, authority, consent, or legal status. |
| `roles` | Requester, performer, payer, beneficiary, verifier, mediator, agent, custodian, or other role. | Parties need role context so payment, performance, verification, benefit, and agency are not collapsed into one vague relation. | It does not prove delegated authority unless authority evidence exists. |
| `promise_or_expectation` | The bounded promise, requested performance, expected conduct, or relationship expectation. | Without a declared promise or expectation, the system cannot distinguish payment, request, preference, aspiration, duty, or courtesy. | It does not prove that the promise was accepted, performed, or legitimate. |
| `acceptance_criteria` | Conditions under which performance is considered acceptable. | Acceptance criteria make fulfillment testable enough to discuss without treating execution, receipt, or payment as satisfaction. | It does not prove that criteria were actually met or accepted by all parties. |
| `evidence_refs` | Receipts, payments, attestations, messages, Human Proof records, covenant references, marketplace events, verification records, or other evidence. | Evidence must be attached explicitly so observers can see what the obligation object depends on. | It does not transform evidence into truth, satisfaction, legitimacy, or settlement. |
| `evidence_boundary_refs` | References to Evidence Boundary Metadata v0 records for the evidence in `evidence_refs`. | Obligation interpretation depends on evidence type, issuer, verification rule, non-claims, missing context, dispute path, repair path, and time semantics. | It does not settle interpretation; it only exposes evidence boundaries. |
| `created_time` | Time the obligation object was created or first represented. | Creation time distinguishes representation from acceptance, execution, verification, breach, and closure. | It does not prove that the obligation existed before acceptance or that the creation order is meaningful by itself. |
| `accepted_time` | Time or interval when relevant parties accepted the bounded obligation terms, if acceptance occurred. | Obligation order depends on acceptance context, not merely the earliest timestamp attached to payment, request, receipt, or execution. | It does not prove valid consent, authority, or absence of coercion. |
| `due_time_or_horizon` | Deadline, review window, expiry, block range, relationship horizon, or other temporal boundary for performance and breach. | Obligations need temporal boundaries so delay, expiry, review, and breach are not inferred from payment time alone. | It does not prove long-term commitment or continuing duty outside the stated horizon. |
| `execution_time` | Time or interval when performance was attempted, delivered, run, or reported. | Execution time helps distinguish doing from proposing, accepting, verifying, or closing. | It does not prove acceptance, satisfaction, or fulfillment. |
| `verification_time` | Time or interval when a verifier, rule, receipt check, or review process evaluated a bounded claim. | Verification time prevents later checks from being confused with event time, acceptance time, or satisfaction time. | It does not prove final meaning, truth, or human satisfaction. |
| `breach_condition` | What would count as failure, non-performance, late performance, unacceptable performance, misuse, or invalid closure. | Breach cannot be assessed honestly unless the failure condition is stated before or during the obligation lifecycle. | It does not prove breach occurred or assign blame. |
| `dispute_path` | Where parties can contest meaning, authority, quality, acceptance, breach, repair, or closure. | A valid event record can still be contested in interpretation; dispute must not be hidden behind receipts or timestamps. | It does not prove justice or guarantee a fair process. |
| `remedy_path` | Refund, correction, re-performance, restitution, escalation, mediation, replacement, or closure process. | Obligation modeling should expose what happens after failure rather than only marking a counterparty as bad. | It does not prove remedy happened or was sufficient. |
| `repair_path` | Apology, explanation, changed behavior, restored access, relationship repair, repair attestation, or post-remedy review. | Repair may be broader than remedy; the object must not collapse technical correction into human repair. | It does not prove forgiveness, restored trust, or erased harm. |
| `status` | Current conceptual state, such as `proposed`, `accepted`, `active`, `performed`, `verified`, `disputed`, `breached`, `remedy_pending`, `repair_pending`, `repaired`, `forgiven`, `closed`, `expired`, `cancelled`, or `unknown`. | Observers need to know whether the object is proposed, active, contested, repaired, closed, or unresolved. | It does not prove moral settlement, legal status, or human satisfaction. |
| `explicit_non_claims` | Explicit statements about what this obligation object does not prove. | Non-claims prevent the object from becoming a laundering surface for legitimacy, satisfaction, identity, truth, justice, or trust. | It prevents overclaim, but it does not ensure users will read or honor the limits. |
| `human_interpretation_required` | Whether human review is required before stronger claims about acceptance, fulfillment, breach, repair, or closure are displayed or acted on. | Some obligations cannot be safely interpreted by agents or UI state alone, especially when evidence is incomplete, disputed, relational, or high-stakes. | It does not guarantee correct human judgment. |

## Optional fields

Optional fields may help specific contexts without making every obligation object heavy:

- `privacy_scope`
- `disclosure_policy`
- `verifier`
- `mediator`
- `confidence_level`
- `related_reputation_context`
- `related_covenant`
- `related_agent_delegation`
- `repair_history`
- `version`

These fields should remain optional because obligations vary in size, risk, privacy,
jurisdictional context, counterparty familiarity, and evidence needs. A tiny paid job
may need only a lightweight obligation profile, while a durable relationship may need
mediator, disclosure, delegation, covenant, and repair context.

Optional fields must not become hidden mandatory bureaucracy. They should add precision
where needed without implying that a small interaction is illegitimate merely because it
omits heavyweight context.

## Time and order semantics

Obligation time must be modeled as ordered context, not a single timestamp. The object
must distinguish at least:

- `created_time`: when the object was represented;
- `accepted_time`: when terms were accepted, if they were accepted;
- `due_time_or_horizon`: when performance, review, expiry, or breach matters;
- `execution_time`: when performance was attempted or reported;
- `verification_time`: when a rule, verifier, or review checked a bounded claim.

A payment timestamp, receipt timestamp, block height, signature time, or verification
time must not be treated as obligation order by itself. Ordering requires sequence
context, acceptance context, and evidence boundaries. If these are missing, the object
should say `unknown` or require human interpretation rather than implying settlement.

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names
states that may be useful when discussing obligations, evidence, disputes, repair, and
closure.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `proposed` | An obligation has been described but not accepted. | Proposal means consent or duty. |
| `accepted` | Relevant parties have accepted the bounded obligation terms. | Acceptance proves full authority, valid consent, or legal enforceability. |
| `active` | The obligation is currently within its performance or review horizon. | Active means performance is happening correctly. |
| `performed` | The expected action or delivery has been reported as done. | Performed means accepted or satisfying. |
| `verified` | Some evidence or verifier has checked a bounded claim. | Verified means true in every relevant human sense. |
| `disputed` | A party or authorized process contests meaning, quality, acceptance, authority, breach, or closure. | Disputed means the accused party is guilty. |
| `breached` | The object records that a breach condition was reached or declared. | Breached means blame is settled or justice occurred. |
| `remedy_pending` | A refund, correction, restitution, re-performance, mediation, or other remedy path is pending. | Remedy pending means remedy will happen or will be enough. |
| `repair_pending` | An apology, explanation, changed behavior, relationship repair, or other repair path is pending. | Repair pending means repair will happen. |
| `repaired` | A repair path has been recorded as completed or accepted. | Repaired means all harm is gone. |
| `forgiven` | A party or process records forgiveness or re-entry after memory and repair context. | Forgiven means memory is erased. |
| `closed` | The obligation is no longer active under the recorded object. | Closed means morally settled. |
| `expired` | The time horizon ended without continued active obligation. | Expired means no consequences or memory remain. |
| `cancelled` | The obligation was withdrawn or terminated before ordinary completion. | Cancelled means no reliance, harm, or record matters. |

## Runtime surfaces

The obligation object may refer to existing or expected runtime surfaces, but none of
these surfaces proves obligation by itself. Each evidence reference should be paired
with evidence boundary metadata when possible.

| Runtime surface | Possible role in obligation object | What it does not prove alone |
| --- | --- | --- |
| `/agent/request` | Request content, declared requester, requested performance, or initial proposal. | It does not prove acceptance, authority, or obligation. |
| Lightning invoice | Payment path, amount, invoice metadata, or cost evidence. | It does not prove promise, consent, obligation, fulfillment, or satisfaction. |
| Paid job status | Evidence that a job entered or completed a runtime execution path. | It does not prove fulfillment, acceptance, or human satisfaction. |
| Signed receipt | Event proof linked to request, payment, execution, or verification. | It does not prove obligation, fulfillment, breach, repair, satisfaction, or legitimacy. |
| `/agent/verify/<job_id>` | Verification surface for a bounded job or receipt claim. | It does not prove final meaning or settled obligation. |
| `/agent/attestations` | Statements by an actor, agent, verifier, or system surface. | It does not prove truth, justice, or settlement. |
| `/agent/trust/events` | Event memory that may support chronology, continuity, or later review. | It does not prove fairness, consent, or complete context. |
| `/agent/reputation` | Contextual memory that may be affected by performance, dispute, repair, or closure. | It does not prove global trustworthiness or moral worth. |
| Covenant lockup | Evidence of value constraint, time constraint, or commitment-adjacent context. | It does not prove love, loyalty, legitimacy, obligation, or full commitment. |
| Human Proof | Evidence relevant to human presence, continuity, request context, or identity context. | It does not prove full identity, consent, authority, or satisfaction. |
| Marketplace interaction | Trade context, offer, acceptance signal, counterparty relation, or repeated interaction. | It does not prove durable reciprocity, settled obligation, trust, or satisfaction. |
| Future dispute/repair endpoints | Dispute state, remedy path, repair records, mediation, or closure updates. | They do not prove justice or erase memory. |

## Example mappings

These examples show how the object should bound common HODLXXI-adjacent interactions.
They are not runtime schema examples.

| Scenario | Minimum obligation fields to expose | Evidence boundary requirement | Unsafe claim to avoid |
| --- | --- | --- | --- |
| Paid 21-sat job | `parties`, `roles`, `promise_or_expectation`, `acceptance_criteria`, `accepted_time`, `due_time_or_horizon`, `execution_time`, `breach_condition`, `remedy_path`, `status`, `explicit_non_claims`. | Invoice, payment, job status, receipt, and verification records should link through `evidence_refs` and `evidence_boundary_refs`. | Paid job means obligation fulfilled or human satisfied. |
| Signed receipt | `promise_or_expectation` and `acceptance_criteria` must be present before the receipt can support fulfillment interpretation. | Receipt metadata should expose issuer, subject, event time, verification time, bounded claim, non-claims, dispute path, and repair path. | Receipt means satisfaction, acceptance, fulfillment, or closure. |
| Human Proof request | `parties`, `roles`, counterparty context, purpose, acceptance criteria, privacy scope if present, `human_interpretation_required`, and explicit non-claims. | Human Proof evidence should expose subject, related keys, event and observation times, verification rule, missing identity context, and dispute path. | Human Proof request or response means full identity, consent, authority, or obligation acceptance. |
| Covenant lockup | `promise_or_expectation`, `due_time_or_horizon`, related covenant reference, breach condition, release or remedy path, and non-claims. | Lockup evidence should expose constraint rule, block or time context, subject, verification rule, missing purpose context, and counter-evidence path. | Lockup means commitment, loyalty, legitimacy, obligation, or reciprocity. |
| Marketplace interaction | Offer/request context, counterparties, roles, acceptance criteria, acceptance time, due horizon, dispute path, remedy path, repair path, and status. | Listing, message, payment, receipt, fulfillment, review, and reputation evidence should each carry boundary metadata. | Marketplace interaction means durable trust, reciprocal relationship, satisfaction, or settled obligation. |

## What it can prove

A well-formed obligation object can prove or support only bounded claims:

- that an obligation was represented;
- that parties, counterparties, and roles were declared;
- that a promise or expectation was stated;
- that acceptance criteria were stated;
- that evidence links and evidence boundary references were attached;
- that time fields were distinguished rather than collapsed into one timestamp;
- that breach, dispute, remedy, or repair paths were recorded;
- that status and explicit non-claims were visible;
- that human interpretation was required or not required according to the object.

It still does not prove truth, satisfaction, legitimacy, justice, valid consent, authority,
full identity, or moral settlement by itself.

## What it must not prove

The existence or state of an obligation object must not be used for these overclaims:

- obligation object exists -> obligation is morally legitimate;
- payment exists -> obligation exists or is fulfilled;
- signed receipt exists -> obligation is satisfied;
- execution recorded -> outcome was accepted;
- earliest timestamp -> first accepted obligation;
- `status: verified` -> human satisfied;
- `status: closed` -> human meaning settled;
- breach recorded -> guilty party known;
- `remedy_path` exists -> remedy happened;
- `repair_path` exists -> relationship repaired;
- parties listed -> identity fully known;
- evidence linked -> evidence interpreted correctly;
- evidence boundary metadata linked -> interpretation settled;
- forgiven -> memory erased.

## Failure modes

- paid job treated as obligation fulfilled;
- receipt treated as satisfaction;
- timestamp order confused with acceptance order;
- missing counterparty context;
- missing remedy path;
- agent execution mistaken for accepted outcome;
- fake obligation object;
- vague promise or expectation;
- missing acceptance criteria;
- hidden counterparty;
- coercive obligation;
- impossible remedy;
- missing repair path where relational harm is possible;
- disputed state shown as final;
- closure laundering;
- obligation spam;
- private context leaked publicly;
- legal overclaim;
- agent-created obligation without authority;
- raw evidence linked without evidence boundary metadata;
- wealthy actor buying obligation theater.

## Falsification tests

- Do users make fewer mistaken trust decisions when obligation object fields are shown beside receipts and evidence boundary metadata?
- Do disputes decrease when acceptance criteria are explicit?
- Do users still overread paid job or fulfilled status as human satisfaction?
- Do users confuse receipt time, payment time, execution time, verification time, and acceptance time?
- Do agents create obligations beyond delegated authority?
- Does the object become too heavy for small paid jobs?
- Do people avoid honest repair because closure states are too rigid?
- Does `human_interpretation_required` prevent unsafe automated settlement, or does it become ignored decoration?

## Open questions

- What is the minimum obligation object that remains useful?
- Which fields must be machine-readable?
- Which fields should remain human-readable?
- Which fields should be private or selectively disclosed?
- Should every paid job have an obligation object?
- Should tiny 21-sat jobs use a lightweight obligation profile?
- How should obligations interact with reputation?
- How should obligations interact with agent delegation?
- How should repair and forgiveness modify closure state without erasing memory?
- How should old obligation-like records without evidence boundary metadata be displayed?
