# Reciprocity Pattern v0

## Purpose

This document defines the minimum conceptual structure needed to represent reciprocity in HODLXXI.

Reciprocity is not a transaction.
Reciprocity is not payment history.
Reciprocity is not transaction count.
Reciprocity is not a trust score.
Reciprocity is not symmetry at every moment.
Reciprocity is not immediate exchange.
Reciprocity is not guaranteed by friendship, kinship, covenant, or agent interaction.

Reciprocity requires repeated interaction, remembered context, recognizable counterparties, expectation, asymmetry tolerance, time horizon, repair path, and evidence of response across time.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract, relationship classifier, legal claim, or implementation claim.

## Problem

HODLXXI has receipts, payments, obligations, delegation records, repair records, covenants, reputation memory, marketplace interactions, agent messages, and trust events.

These surfaces can preserve events and evidence, but they do not by themselves preserve reciprocal meaning. Users may infer false claims:

- many transactions -> reciprocity;
- payment returned -> reciprocity restored;
- equal exchange -> trustworthy relationship;
- locked value -> reciprocal commitment;
- repeated interaction -> cooperation;
- reputation score -> reciprocal trust;
- repair completed -> reciprocity restored;
- agent interaction -> relationship exists.

The reciprocity pattern exists to prevent those false inference chains. It makes visible the difference between event sequence, counterparties, expectation, asymmetry, memory, repair, and bounded evidence over time.

## Non-goals

This document does not:

- create a universal trust score;
- reduce human relationship to transactions;
- require perfect symmetry;
- require immediate repayment;
- require all relationship context to be public;
- prove friendship, loyalty, love, or legitimacy;
- guarantee cooperation;
- replace human judgment;
- implement runtime code.

## Required fields

A minimum reciprocity pattern needs the following fields before HODLXXI can honestly represent reciprocal cooperation as a pattern across time rather than a single transaction, payment, receipt, or exchange.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `pattern_id` | Stable identifier for this reciprocity pattern. | Without a stable identifier, events, obligations, repairs, reputation context, and evidence cannot refer to the same pattern over time. | It does not prove cooperation exists. |
| `counterparties` | Actors, keys, agents, or groups involved. | Reciprocity requires recognizable counterparties so response, delay, asymmetry, and repair are not free-floating event claims. | It does not prove full identity or stable loyalty. |
| `relationship_context` | Family, friend, marketplace, agent delegation, covenant, service, community, or unknown context. | The same event sequence can mean different things in different contexts; interpretation needs a declared relationship frame. | It does not prove legitimacy or affection. |
| `event_sequence` | Ordered events such as payments, receipts, requests, obligations, repairs, messages, attestations, covenant actions, or marketplace interactions. | Reciprocity is interpreted across events, so chronology and event type must be visible. | It does not transform repeated events into reciprocity. |
| `time_horizon` | The period over which reciprocity is interpreted. | Delayed response, durable support, breach, exit, and repair cannot be evaluated without time boundaries. | It does not prove long-term commitment. |
| `expectation_model` | What each party appears to expect from the pattern. | Reciprocity depends on expectation; without this field, observers may confuse gift, payment, debt, service, obligation, and care. | It does not prove expectations were legitimate, shared, or understood. |
| `asymmetry_tolerance` | How much delay, imbalance, gift, debt, one-way support, or unequal timing can exist without treating the pattern as failed. | Reciprocal cooperation can be asymmetric over time, but asymmetry needs bounded interpretation to avoid both false breach and exploitation laundering. | It does not excuse exploitation. |
| `obligation_links` | Related obligation objects. | Obligations may anchor promises, acceptance criteria, breach conditions, remedy paths, and closure states relevant to the pattern. | It does not prove obligations were fulfilled. |
| `repair_links` | Related repair lifecycles. | Reciprocal patterns may survive failure only through visible repair context, affected response, memory, and non-erasure. | It does not prove trust was restored. |
| `reputation_context` | Relevant reputation memory or context. | Reputation may inform how a pattern is interpreted, especially after repeated behavior, repair, dispute, or re-entry. | It does not reduce reciprocity to a score. |
| `evidence_links` | Receipts, payments, attestations, messages, proofs, covenant references, delegation records, repair records, or trust events. | Pattern claims need evidence anchors so observers can inspect what was actually preserved. | It does not transform evidence into meaning. |
| `current_state` | Current conceptual state, such as `emerging`, `active`, `strained`, `broken`, `repaired`, `dormant`, `exited`, or `unknown`. | Observers need to distinguish tentative, active, damaged, repaired, inactive, ended, and uncertain patterns. | It does not prove moral truth. |
| `non_claims` | Explicit statements about what this reciprocity pattern does not prove. | Non-claims prevent transaction count, repair, reputation, covenant, or agent interaction from laundering stronger relationship claims. | It prevents overclaim, but it does not ensure users will read or honor the limits. |

## Optional fields

Optional fields may add precision in contexts where reciprocity patterns are privacy-sensitive, high-stakes, mediated, contested, agentic, or marketplace-adjacent:

- `privacy_scope`
- `disclosure_policy`
- `mediator`
- `verifier`
- `related_covenant`
- `related_delegation`
- `related_marketplace`
- `gratitude_markers`
- `resentment_markers`
- `dependency_risk`
- `coercion_risk`
- `sybil_risk`
- `cartel_risk`
- `re_entry_conditions`
- `exit_conditions`
- `version`

These fields should remain optional because reciprocal patterns vary by relationship, severity, privacy, power asymmetry, evidentiary need, and time horizon. A casual marketplace pattern should not require the same disclosure as a long-running covenant, family support pattern, delegation relationship, or contested repair process.

Optional fields must not become hidden mandatory bureaucracy. They should add context where needed without implying that an omitted emotion marker, mediator, verifier, or risk field makes a low-stakes pattern invalid.

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names states that may be useful when discussing reciprocal patterns across events, actors, memory, expectation, asymmetry, repair, and time.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `observed` | Events involving recognizable counterparties have been observed, but reciprocity has not been established or claimed. | Observation means relationship. |
| `emerging` | Repeated interaction and early expectations are visible, but the pattern remains tentative. | Emerging means cooperation is reliable. |
| `active` | The pattern is currently represented as ongoing, with evidence of response across time. | Active means future cooperation is guaranteed. |
| `asymmetric` | The pattern includes delay, imbalance, gift, debt, one-way support, or unequal timing within declared tolerance. | Asymmetry means exploitation is acceptable. |
| `strained` | Expectations, timing, balance, conduct, or response have become concerning but not conclusively broken. | Strain means bad faith or final breach. |
| `disputed` | Parties or observers contest facts, meaning, expectation, obligation, repair, or state. | Dispute means one side is lying or guilty. |
| `repair_pending` | A repair path is expected, proposed, underway, or awaiting affected response. | Pending repair means repair will occur. |
| `repaired` | A repair lifecycle or accepted process records that a failure was addressed under stated criteria. | Repaired means trust is restored. |
| `forgiven` | Forgiveness, non-retaliation, or re-entry has been recorded with memory preserved. | Forgiven means memory is erased. |
| `dormant` | The pattern is inactive but not necessarily ended or broken. | Dormant means abandoned, safe, or resolved. |
| `exited` | A party or accepted process records exit from the pattern. | Exit means no obligation, memory, harm, or consequence remains. |
| `broken` | The pattern is represented as failed, breached, or no longer sustaining reciprocal cooperation. | Broken means permanent moral judgment. |
| `unknown` | Available evidence is insufficient to assign a more specific state. | Unknown means safe, unsafe, cooperative, or non-cooperative. |

## Runtime surfaces

The reciprocity pattern may refer to existing or expected runtime surfaces, but none of these surfaces proves reciprocity by itself.

| Runtime surface | Possible role in reciprocity pattern | What it does not prove alone |
| --- | --- | --- |
| Signed receipts | Event proof for work, payment, request, delivery, verification, or response. | It does not prove obligation, relationship, commitment, or reciprocity. |
| `/agent/verify/<job_id>` | Verification output for a job or evidence item in the event sequence. | It does not prove shared meaning, satisfaction, or reciprocal cooperation. |
| `/agent/request` | Request surface that may begin or continue an interaction sequence. | It does not prove acceptance, obligation, or relationship. |
| Lightning invoices | Payment request or settlement evidence linked to an event. | It does not prove care, trust, obligation, or reciprocity. |
| Paid job status | Evidence that a job reached a paid state. | It does not prove satisfaction, commitment, or future cooperation. |
| `/agent/trust/events` | Chronological memory for interactions, disputes, repairs, attestations, and state changes. | It does not prove complete context or moral meaning. |
| `/agent/reputation` | Contextual memory that may inform interpretation of repeated behavior. | It does not prove reciprocal trust or reduce reciprocity to a score. |
| `/agent/attestations` | Statements by parties, agents, verifiers, mediators, or observers. | It does not prove truth, legitimacy, consent, or stable relationship. |
| Minimum Obligation Object v0 | Linked promises, acceptance criteria, breach conditions, remedy paths, and closure states. | It does not prove fulfillment, affection, loyalty, or reciprocity by itself. |
| Minimum Delegation Record v0 | Linked authority, scope, duration, permitted actions, consent evidence, revocation, and accountability. | It does not prove loyalty, wisdom, legitimacy, or relationship depth. |
| Repair Lifecycle v0 | Linked failure, remedy, affected response, forgiveness, memory, and re-entry context. | It does not prove trust was restored or reciprocity resumed. |
| Covenant lockup | Evidence of value constraint, time constraint, or covenant-adjacent commitment context. | It does not prove reciprocal loyalty or legitimate commitment. |
| Covenant participant keys | Evidence of declared key participation in a covenant context. | It does not prove full identity, kinship, affection, or future cooperation. |
| Human Proof | Human-presence or identity-context evidence relevant to a pattern. | It does not prove consent, character, legitimacy, or reciprocity. |
| Marketplace listing | Public or semi-public offer context that may anchor repeated marketplace interaction. | It does not prove trustworthiness or relationship. |
| Marketplace interaction | Purchase, service, fulfillment, dispute, or review-adjacent evidence. | It does not prove cooperation beyond the bounded interaction. |
| Inter-agent message | Message evidence between agents or humans using agents. | It does not prove intimacy, authority, consent, or relationship. |
| Future reciprocity endpoint | Possible publication or query surface for reciprocity pattern records. | It would not prove moral truth or future cooperation by itself. |
| Future relationship memory endpoint | Possible selective memory surface for relationship context over time. | It would not prove friendship, love, loyalty, or legitimacy by itself. |

## What it can prove

A well-formed reciprocity pattern can prove or support only bounded claims:

- that a pattern was represented;
- that counterparties were declared;
- that events were ordered;
- that time horizon and relationship context were stated;
- that expectations, asymmetry, obligations, repairs, and reputation context were recorded;
- that evidence links were attached;
- that non-claims were visible.

It still does not prove friendship, loyalty, love, legitimacy, stable cooperation, restored trust, or moral worth by itself.

## What it must not prove

The existence or state of a reciprocity pattern must not be used for these overclaims:

- pattern exists -> relationship is trustworthy;
- many transactions -> reciprocity;
- equal exchange -> trust;
- one-sided support -> exploitation;
- asymmetry tolerated -> abuse is acceptable;
- repair link exists -> reciprocity restored;
- reputation context positive -> reciprocal trust exists;
- covenant exists -> reciprocal commitment exists;
- agent messages repeated -> relationship exists;
- current_state active -> future cooperation guaranteed.

## Failure modes

- transaction-count laundering;
- reputation-score laundering;
- fake reciprocal pattern;
- sybil-created reciprocity;
- cartel reciprocity;
- coercive dependency;
- gift turned into obligation trap;
- one-sided extraction hidden as asymmetry;
- repair used to reset pattern too easily;
- memory used as permanent punishment;
- privacy leakage of relationship context;
- marketplace activity misread as trust;
- agent-generated relationship theater;
- covenant lockup misread as reciprocal loyalty;
- family or friendship context exploited;
- delayed reciprocity mistaken for default;
- default mistaken for delayed reciprocity.

## Falsification tests

- Do users make better trust decisions with pattern context than with transaction count alone?
- Does explicit asymmetry tolerance reduce false breach accusations?
- Does it also increase tolerance of exploitation?
- Do repair links help distinguish restored relationships from reputation laundering?
- Do users overread active patterns as future guarantees?
- Can sybil actors manufacture convincing reciprocal patterns cheaply?
- Can cartels use reciprocal patterns to launder legitimacy?
- Does privacy-aware disclosure preserve meaning without leaking sensitive relationships?
- Does the mechanism become too heavy for casual interactions?

## Open questions

- What is the minimum useful reciprocity pattern?
- Which parts must be machine-readable?
- Which parts should remain human-readable?
- Which parts should be private or selectively disclosed?
- How should delayed reciprocity be distinguished from default?
- How should asymmetry be distinguished from exploitation?
- How should gratitude, resentment, shame, loyalty, and obligation be represented without reducing them to scores?
- How should reciprocity interact with reputation?
- How should reciprocity interact with obligations?
- How should reciprocity interact with repair and forgiveness?
- How should AI agents participate in reciprocal patterns without simulating false intimacy?
- What patterns should be impossible or discouraged?
