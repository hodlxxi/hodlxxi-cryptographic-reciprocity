# Contextual Reputation v0

## Purpose

This document defines the minimum conceptual structure needed to represent contextual reputation in HODLXXI.

Reputation is not a global score.
Reputation is not popularity.
Reputation is not moral worth.
Reputation is not identity.
Reputation is not reciprocity.
Reputation is not a badge.
Reputation is not a final judgment.
Reputation is not erased by forgiveness.
Reputation is not restored by payment alone.

Contextual reputation requires remembered events, role context, domain context, time horizon, evidence links, repair history, dispute status, confidence limits, and explicit non-claims.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract, scoring system, legal process, or implementation claim.

## Problem

HODLXXI has receipts, attestations, trust events, reputation endpoints, obligations, delegations, repair lifecycles, reciprocity patterns, identity continuity records, marketplace interactions, Human Proof, and covenant references.

These surfaces can preserve events and bounded statements, but they can also invite false inference chains if reputation is displayed without context. Users may infer stronger claims than the system preserved:

- high score -> trustworthy;
- many receipts -> good reputation;
- paid jobs -> good actor;
- identity continuity -> reputation;
- repair completed -> reputation restored;
- forgiveness granted -> negative memory erased;
- no disputes -> trustworthy;
- marketplace activity -> reliable actor;
- covenant lockup -> high reputation;
- agent fluency -> agent reputation.

The contextual reputation record exists to prevent those false inference chains. It makes visible the difference between compressed memory, evidence, domain, role, dispute state, repair history, identity context, reciprocity context, and the claims HODLXXI must not make.

## Non-goals

This document does not:

- create a universal trust score;
- rank human worth;
- rank moral value;
- prove identity;
- prove authority;
- prove legitimacy;
- guarantee future behavior;
- erase negative memory;
- require all reputation context to be public;
- replace human judgment;
- implement runtime code.

## Required fields

A minimum contextual reputation record needs the following fields before HODLXXI can honestly represent reputation as contextual compressed memory rather than as a global score, popularity metric, trust badge, or moral rank.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `reputation_id` | Stable identifier for this contextual reputation record. | Without a stable identifier, evidence, summaries, disputes, corrections, and later updates cannot refer to the same contextual record. | It does not prove reputation is true or fair. |
| `subject` | Human, agent, operator, organization, marketplace actor, covenant participant, key, or pseudonymous actor whose reputation is being summarized. | Reputation must have a declared subject so observers know what entity, role, key, or continuity anchor the memory is about. | It does not prove full identity. |
| `context_domain` | Domain where the reputation applies, such as paid jobs, marketplace fulfillment, covenant participation, agent delegation, verification, repair behavior, communication, family context, or unknown. | Reputation is contextual; a record must name the domain before any summary can be interpreted. | It does not generalize to all domains. |
| `role_context` | Requester, performer, verifier, mediator, operator, agent, beneficiary, covenant participant, marketplace seller, marketplace buyer, or unknown. | The same subject may behave differently, carry different obligations, or expose different risks in different roles. | It does not prove role legitimacy. |
| `time_horizon` | Period over which reputation memory is summarized. | Reputation without time bounds collapses old, recent, stale, and changing behavior into one misleading present-tense claim. | It does not prove future behavior. |
| `memory_inputs` | Events, receipts, attestations, trust events, obligations, repairs, disputes, messages, payments, covenants, delegations, or reciprocity patterns being compressed. | Reputation must disclose what memory is being compressed so users can distinguish evidence-backed summaries from free-floating labels. | It does not transform memory into truth. |
| `evidence_links` | References to underlying records or proofs. | Contextual summaries need audit paths to preserved records where privacy and disclosure rules allow. | It does not prove interpretation. |
| `obligation_context` | Related obligation objects and their states. | Reputation about performance, breach, or reliability must distinguish receipts and payments from obligations, acceptance criteria, remedy paths, and closure. | It does not prove obligations were fulfilled. |
| `delegation_context` | Related delegation records and scope. | Reputation about agents, operators, or representatives must show whether actions were linked to bounded delegation. | It does not prove authority was valid. |
| `repair_context` | Related repair lifecycles, forgiveness states, remedy evidence, and memory policy. | Repair and forgiveness must remain visible so reputation is not laundered by closure, refund, apology, or silence. | It does not erase harm. |
| `reciprocity_context` | Related reciprocity patterns. | Reputation may depend on repeated interaction patterns rather than isolated transactions or counts. | It does not prove reciprocal trust. |
| `identity_context` | Related identity continuity records or anchors. | Reputation may need key, operator, agent, pseudonym, rotation, or continuity context to avoid identity laundering or mistaken attribution. | It does not prove full identity. |
| `dispute_context` | Open, resolved, abandoned, contested, unknown, or no known disputes. | Users need to know whether the underlying memory is disputed, settled under recorded criteria, unresolved, hidden, or unknown. | It does not prove guilt or innocence. |
| `confidence_limits` | Limits on certainty, completeness, recency, sample size, privacy, missing data, or adversarial manipulation. | A reputation summary must expose its uncertainty and incompleteness instead of presenting compression as final truth. | It does not prove the summary is reliable. |
| `current_summary` | Human-readable and/or machine-readable contextual summary. | The record needs a bounded summary for use in interfaces, agent reasoning, or human review. | It does not reduce reputation to a universal score. |
| `non_claims` | Explicit statements about what this contextual reputation record does not prove. | Non-claims prevent overclaim and keep reputation from becoming a badge, rank, judgment, or moral label. | It prevents overclaim, but it does not ensure users will read or honor the limits. |

## Optional fields

Optional fields may improve precision in some contexts without making every contextual reputation record too heavy:

- `privacy_scope`
- `disclosure_policy`
- `verifier`
- `mediator`
- `weighting_notes`
- `decay_policy`
- `appeal_path`
- `correction_path`
- `sybil_risk`
- `cartel_risk`
- `coercion_risk`
- `popularity_bias`
- `reputation_laundering_risk`
- `negative_memory_policy`
- `version`

These fields should remain optional because reputation contexts differ by stakes, privacy, reversibility, adversarial pressure, domain, role, and evidentiary burden. A low-stakes marketplace interaction may need a lightweight contextual summary. A long-running delegation relationship, contested repair history, or covenant-adjacent relationship may need richer disclosure, appeal, decay, mediator, correction, and manipulation-risk context.

Optional fields must not become hidden mandatory bureaucracy. They should add precision where needed without implying that a contextual reputation record is illegitimate merely because it omits heavyweight context inappropriate to the domain.

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names states that may be useful when discussing contextual reputation records, updates, disputes, repairs, forgiveness annotations, stale memory, and retirement.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `created` | A contextual reputation record has been created with declared subject, domain, role, time horizon, memory inputs, and non-claims. | Created means the subject is trustworthy. |
| `active` | The record is currently being used or displayed as contextual reputation memory. | Active means current summary is complete or final. |
| `updated` | Memory inputs, evidence links, summary, confidence limits, or context fields have changed. | Updated means the new version is more truthful. |
| `disputed` | One or more claims, inputs, interpretations, or summaries are contested. | Disputed means the subject is guilty or dishonest. |
| `under_review` | Evidence, disputes, corrections, privacy, or interpretation are being examined. | Review means neutrality, fairness, or completeness. |
| `corrected` | An error, omission, misattribution, or misleading summary has been corrected. | Corrected means all problems are resolved. |
| `repaired` | A related repair lifecycle has affected the contextual memory. | Repaired means reputation is fully restored. |
| `forgiveness_noted` | Forgiveness, conditional re-entry, or non-forgiveness has been recorded as context. | Forgiveness noted means negative memory is erased. |
| `degraded` | Confidence, recency, evidence quality, dispute state, or manipulation risk has weakened the record. | Degraded means the subject is bad or unsafe. |
| `restored` | Confidence or usability has improved after correction, review, repair, or new evidence. | Restored means trust is automatic or harm disappeared. |
| `stale` | The time horizon, recency, or evidence base is no longer current enough for ordinary use. | Stale means the memory is false or irrelevant. |
| `sealed` | Some or all details are no longer public or are selectively disclosed under privacy or safety policy. | Sealed means nothing happened or accountability ended. |
| `retired` | The record is no longer used as current contextual reputation. | Retired means memory must be forgotten. |
| `unknown` | State cannot be determined from available context. | Unknown means safe, unsafe, guilty, innocent, or neutral. |

## Runtime surfaces

Contextual reputation may refer to existing or expected runtime surfaces, but none of these surfaces proves contextual reputation by itself.

| Runtime surface | Possible role in contextual reputation | What it does not prove alone |
| --- | --- | --- |
| `/agent/reputation` | Existing or future display surface for compressed operational memory. | It does not prove global trustworthiness, moral worth, or final judgment. |
| `/agent/trust/events` | Event chronology for actions, updates, disputes, repair, attestations, and reputation-relevant memory. | It does not prove interpretation, fairness, or complete context. |
| `/agent/attestations` | Statements by subjects, agents, verifiers, mediators, operators, or counterparties. | It does not prove truth, legitimacy, or absence of counterevidence. |
| Signed receipts | Bounded proof that a recorded event was signed. | It does not prove obligation, satisfaction, reputation, or trustworthiness. |
| `/agent/verify/<job_id>` | Verification surface for job records, receipts, or evidence references. | It does not prove quality, meaning, restored trust, or future behavior. |
| `/agent/request` | Request context that may define roles, expectations, or claimed scope. | It does not prove consent, authority, completion, or satisfaction. |
| Lightning invoices | Payment request or payment evidence relevant to jobs, remedies, or marketplace activity. | It does not prove obligation, morality, repair, or reputation. |
| Paid job status | Execution or completion context for work. | It does not prove the actor is good, reliable in all domains, or free of disputes. |
| Minimum Obligation Object v0 | Context for promise, acceptance criteria, breach condition, remedy path, dispute state, repair state, and closure state. | It does not prove obligations were fulfilled by itself. |
| Minimum Delegation Record v0 | Context for delegated scope, permitted actions, duration, revocation, and accountability path. | It does not prove authority was legitimate or wisely used. |
| Repair Lifecycle v0 | Context for harm, dispute, remedy, acceptance, forgiveness, memory policy, and repair state. | It does not erase harm or prove trust has been restored. |
| Reciprocity Pattern v0 | Context for repeated interaction, asymmetry, delay, repair, re-entry, and non-transactional relationship memory. | It does not prove reciprocal trust or moral worth. |
| Identity Continuity v0 | Context for key purpose, rotation, revocation, compromise notice, operator-agent relation, and continuity evidence. | It does not prove full identity or good reputation. |
| Covenant lockup | Evidence of value or time constraint relevant to commitment-adjacent context. | It does not prove love, loyalty, legitimacy, or high reputation. |
| Human Proof | Evidence relevant to human presence or identity context. | It does not prove full identity, trustworthiness, or moral value. |
| Marketplace listing | Public or semi-public offer context for goods, services, terms, or seller identity. | It does not prove reliability, fulfillment, or safe behavior in other domains. |
| Marketplace interaction | Trade, negotiation, payment, fulfillment, dispute, or review context. | It does not prove durable reciprocity or global reputation. |
| Inter-agent message | Signed or recorded communication between agents. | It does not prove authority, consent, sincerity, or human-like character. |
| Future contextual reputation endpoint | Possible first-class surface for contextual reputation records. | It would not prove final truth, moral worth, or future behavior by itself. |
| Future correction endpoint | Possible surface for correcting errors, omissions, misattribution, or misleading summaries. | It would not prove every correction is complete or accepted. |
| Future dispute endpoint | Possible surface for opening, updating, contesting, mediating, or resolving disputes. | It would not prove guilt, innocence, justice, or complete context by itself. |

## What it can prove

A well-formed contextual reputation record can prove or support only bounded claims:

- that a reputation summary was represented;
- that a subject, domain, role, and time horizon were declared;
- that memory inputs and evidence links were attached;
- that obligation, delegation, repair, reciprocity, identity, and dispute contexts were referenced;
- that confidence limits and non-claims were visible.

It still does not prove moral worth, global trustworthiness, identity, legitimacy, authority, future behavior, or restored trust by itself.

## What it must not prove

The existence or state of a contextual reputation record must not be used for these overclaims:

- reputation exists -> actor is trustworthy;
- high reputation -> moral worth;
- global score -> contextual reliability;
- many receipts -> good reputation;
- no disputes -> no harm;
- repaired -> reputation fully restored;
- forgiven -> negative memory erased;
- positive marketplace history -> safe in all domains;
- agent reputation -> human-like character;
- identity continuity -> good reputation;
- covenant exists -> reputation is high;
- current_summary -> final truth.

## Failure modes

- global-score collapse;
- popularity laundering;
- transaction-count laundering;
- receipt-count laundering;
- repair laundering;
- forgiveness laundering;
- identity laundering;
- sybil reputation farming;
- cartel reputation farming;
- retaliation through negative reputation;
- permanent punishment through memory;
- memory erasure disguised as mercy;
- context collapse across domains;
- privacy leakage;
- hidden disputes;
- mediator capture;
- stale reputation treated as current;
- agent reputation theater;
- wealthy actor buying reputation;
- weak actor unable to repair reputation.

## Falsification tests

- Do users make better decisions with contextual reputation than with a global score?
- Do users still overread contextual summaries as final truth?
- Do contextual records reduce mistaken trust decisions across domains?
- Can sybil actors farm reputation cheaply?
- Can cartels launder legitimacy through mutual attestations?
- Do repair histories prevent reputation laundering or enable it?
- Does negative memory become permanent punishment?
- Does privacy-aware disclosure preserve useful reputation without exposing sensitive context?
- Does the mechanism become too heavy for low-stakes interactions?
- Do users confuse agent reputation with human character?

## Open questions

- What is the minimum useful contextual reputation record?
- Which fields must be machine-readable?
- Which fields should remain human-readable?
- Which parts should be private or selectively disclosed?
- Should HODLXXI ever expose a numeric score?
- How should reputation decay over time?
- How should repair affect reputation without erasing memory?
- How should forgiveness affect reputation?
- How should reputation interact with identity continuity?
- How should reputation interact with reciprocity patterns?
- How should reputation interact with obligations and delegations?
- How should reputation resist sybil and cartel manipulation?
- What reputation claims should HODLXXI never make?
