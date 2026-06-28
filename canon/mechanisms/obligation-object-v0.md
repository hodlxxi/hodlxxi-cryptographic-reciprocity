# Minimum Obligation Object v0

## Purpose

This document defines the minimum conceptual object needed to represent an obligation in
HODLXXI.

An obligation is not created by payment alone. An obligation is not proven by receipt
alone. An obligation is not satisfied by execution alone.

An obligation requires a bounded relation among actors, a promise or expected
performance, acceptance criteria, time horizon, breach condition, and remedy or repair
path.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract,
legal contract template, or implementation claim.

## Problem

HODLXXI has payments, requests, receipts, verification, attestations, reputation
telemetry, event memory, and covenant lockups.

These surfaces are useful, but users may infer stronger claims than the system
preserved:

- paid -> owed;
- executed -> fulfilled;
- receipt verified -> satisfied;
- lockup present -> committed;
- attestation present -> settled.

The obligation object exists to prevent those false inference chains. It makes the
missing structure visible before HODLXXI presents stronger claims about promise,
acceptance, breach, repair, or closure.

## Non-goals

This document does not:

- create a legal contract system;
- define enforceable law;
- require every small paid job to become heavy bureaucracy;
- prove human satisfaction;
- prove moral legitimacy;
- resolve all disputes;
- require all obligation details to be public;
- implement runtime code.

## Required fields

A minimum obligation object needs the following fields before HODLXXI can honestly model
an obligation.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `obligation_id` | A stable identifier for this obligation object. | Without a stable identifier, later evidence, disputes, remedies, and closure records cannot refer to the same bounded object. | It does not prove correctness or legitimacy. |
| `parties` | Actors or keys involved in the obligation. | Obligation requires at least a declared relation among participants, even when some identities are partial or pseudonymous. | It does not prove full human identity. |
| `roles` | Requester, performer, verifier, beneficiary, mediator, or other role. | Parties need role context so payment, performance, verification, and benefit are not collapsed into one vague counterparty relation. | It does not prove authority unless authority evidence exists. |
| `promise` | The bounded thing expected or offered. | Without a declared promise, the system cannot distinguish payment, request, preference, aspiration, or duty. | It does not prove satisfaction. |
| `acceptance_criteria` | Conditions under which performance is considered acceptable. | Acceptance criteria make fulfillment testable enough to discuss without treating execution as satisfaction. | It does not prove that criteria were actually met. |
| `time_horizon` | When performance, breach, review, or expiry matters. | Obligations need temporal boundaries so delay, expiry, review, and breach are not inferred from payment time alone. | It does not prove long-term commitment. |
| `evidence_links` | Receipts, payments, attestations, messages, covenant references, or verification records. | Evidence must be attached explicitly so observers can see what the obligation object depends on. | It does not transform evidence into truth. |
| `breach_condition` | What would count as failure. | Breach cannot be assessed honestly unless the failure condition is stated before or during the obligation lifecycle. | It does not prove breach occurred. |
| `remedy_path` | Refund, correction, repair, re-performance, apology, escalation, mediation, or closure. | Obligation modeling should expose what happens after failure rather than only marking a counterparty as bad. | It does not prove repair happened. |
| `dispute_state` | `none`, `disputed`, `under_review`, `resolved`, `abandoned`, or `unknown`. | A valid event record can still be contested in meaning, quality, authority, or acceptance. | It does not prove justice. |
| `closure_state` | `open`, `fulfilled`, `breached`, `repaired`, `forgiven`, `expired`, `cancelled`, or `unknown`. | Observers need to know whether the object is still active, closed, unresolved, repaired, or expired. | It does not erase memory. |
| `non_claims` | Explicit statements about what this obligation object does not prove. | Non-claims prevent the object from becoming a laundering surface for legitimacy, satisfaction, identity, or justice. | It prevents overclaim, but it does not ensure users will read or honor the limits. |

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

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names
states that may be useful when discussing obligations, evidence, disputes, repair, and
closure.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `proposed` | An obligation has been described but not accepted. | Proposal means consent or duty. |
| `accepted` | Relevant parties have accepted the bounded obligation terms. | Acceptance proves full authority or legal enforceability. |
| `active` | The obligation is currently within its performance or review horizon. | Active means performance is happening correctly. |
| `performed` | The expected action or delivery has been reported as done. | Performed means accepted or satisfying. |
| `verified` | Some evidence or verifier has checked a bounded claim. | Verified means true in every relevant human sense. |
| `disputed` | A party or authorized process contests meaning, quality, acceptance, authority, breach, or closure. | Disputed means the accused party is guilty. |
| `breached` | The object records that a breach condition was reached or declared. | Breached means blame is settled or justice occurred. |
| `repair_pending` | A remedy, correction, restitution, re-performance, apology, mediation, or other repair path is pending. | Repair pending means repair will happen. |
| `repaired` | A repair path has been recorded as completed or accepted. | Repaired means all harm is gone. |
| `forgiven` | A party or process records forgiveness or re-entry after memory and repair context. | Forgiven means memory is erased. |
| `closed` | The obligation is no longer active under the recorded object. | Closed means morally settled. |
| `expired` | The time horizon ended without continued active obligation. | Expired means no consequences or memory remain. |
| `cancelled` | The obligation was withdrawn or terminated before ordinary completion. | Cancelled means no reliance, harm, or record matters. |

## Runtime surfaces

The obligation object may refer to existing or expected runtime surfaces, but none of
these surfaces proves obligation by itself.

| Runtime surface | Possible role in obligation object | What it does not prove alone |
| --- | --- | --- |
| `/agent/request` | Request content, declared requester, requested performance, or initial proposal. | It does not prove acceptance, authority, or obligation. |
| Lightning invoice | Payment path, amount, invoice metadata, or cost evidence. | It does not prove promise, consent, obligation, or satisfaction. |
| Paid job status | Evidence that a job entered or completed a runtime execution path. | It does not prove fulfillment, acceptance, or human satisfaction. |
| Signed receipt | Event proof linked to request, payment, execution, or verification. | It does not prove obligation, breach, repair, or legitimacy. |
| `/agent/verify/<job_id>` | Verification surface for a bounded job or receipt claim. | It does not prove final meaning or settled obligation. |
| `/agent/attestations` | Statements by an actor, agent, verifier, or system surface. | It does not prove truth, justice, or settlement. |
| `/agent/trust/events` | Event memory that may support chronology, continuity, or later review. | It does not prove fairness, consent, or complete context. |
| `/agent/reputation` | Contextual memory that may be affected by performance, dispute, repair, or closure. | It does not prove global trustworthiness or moral worth. |
| Covenant lockup | Evidence of value constraint, time constraint, or commitment-adjacent context. | It does not prove love, loyalty, legitimacy, or full commitment. |
| Human Proof | Evidence relevant to human presence or identity context. | It does not prove full identity, authority, or satisfaction. |
| Marketplace interaction | Trade context, offer, acceptance signal, counterparty relation, or repeated interaction. | It does not prove durable reciprocity or settled obligation. |
| Future dispute/repair endpoints | Dispute state, remedy path, repair records, mediation, or closure updates. | They do not prove justice or erase memory. |

## What it can prove

A well-formed obligation object can prove or support only bounded claims:

- that an obligation was represented;
- that parties and roles were declared;
- that evidence links were attached;
- that acceptance criteria were stated;
- that dispute or closure state was recorded;
- that non-claims were visible.

It still does not prove truth, satisfaction, legitimacy, justice, or full identity by
itself.

## What it must not prove

The existence or state of an obligation object must not be used for these overclaims:

- obligation object exists -> obligation is morally legitimate;
- `closure_state: fulfilled` -> human satisfied;
- breach recorded -> guilty party known;
- `remedy_path` exists -> repair happened;
- parties listed -> identity fully known;
- evidence linked -> evidence interpreted correctly;
- forgiven -> memory erased.

## Failure modes

- fake obligation object;
- vague promise;
- missing acceptance criteria;
- hidden counterparty;
- coercive obligation;
- impossible remedy;
- disputed state shown as final;
- closure laundering;
- obligation spam;
- private context leaked publicly;
- legal overclaim;
- agent-created obligation without authority;
- wealthy actor buying obligation theater.

## Falsification tests

- Do users make fewer mistaken trust decisions when obligation object fields are shown beside receipts?
- Do disputes decrease when acceptance criteria are explicit?
- Do users still overread fulfilled state as human satisfaction?
- Do agents create obligations beyond delegated authority?
- Does the object become too heavy for small paid jobs?
- Do people avoid honest repair because closure states are too rigid?

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
