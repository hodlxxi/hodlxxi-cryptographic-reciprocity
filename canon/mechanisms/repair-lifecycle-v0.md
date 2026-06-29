# Repair Lifecycle v0

## Purpose

This document defines the minimum conceptual lifecycle needed to represent what happens
after failure, dispute, breach, misuse, or harm in HODLXXI.

Repair is not erasure. Refund is not repair by itself. Apology is not forgiveness.
Closure is not justice. Evidence of repair is not a repaired relationship. Repair is
not reputational laundering or punishment by another name.

Repair requires bounded memory of the original event, a declared failure or harm
context, affected parties, responsible parties, evidence boundary metadata, relevant
obligation context, relevant delegation context when authority was delegated or misused,
time and order semantics, remedy and repair records, changed behavior over time,
dispute and counter-evidence paths, and explicit non-claims about justice, forgiveness,
closure, and restored trust.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract,
legal remedy process, mediation protocol, or implementation claim.

## Canon claims and mechanism dependency

This mechanism cites existing Canon claims without changing their meanings.

| Claim ID | Source | Boundary used by this mechanism |
| --- | --- | --- |
| `CRT-FORGIVENESS-001` | [Memory Before Forgiveness](../chapters/memory-before-forgiveness.md) | Forgiveness requires preserved memory of harm, repair context, and changed behavior over time; it is not apology, closure, erasure, or reputation restoration. |
| `CRT-EVIDENCE-001` | [Evidence Is Not Truth](../chapters/evidence-is-not-truth.md) | Evidence of harm, acknowledgement, refund, apology, remedy, correction, or repair is not truth, justice, forgiveness, or a restored relationship by itself. |
| `CRT-TIME-001` | [Time Is Not Timestamp](../chapters/time-is-not-timestamp.md) | Repair and changed behavior need sequence, horizon, review, and recurrence context; a timestamp alone does not prove repair order, maturation, or transformation. |
| `CRT-OBLIGATION-001` | [Obligation Is Not Payment](../chapters/obligation-is-not-payment.md) | Payment, refund, receipt, or execution is not obligation creation, fulfillment, satisfaction, or repair by itself. |
| `CRT-AGENT-AUTHORITY-001` | [Bounded Authority for AI Agents](../chapters/bounded-authority-for-ai-agents.md) | Agent capability, fluency, key control, or paid execution is not delegated authority; repair after delegated-agent misuse needs delegation and accountability context. |

Repair Lifecycle v0 explicitly depends on
[`evidence-boundary-metadata-v0`](evidence-boundary-metadata-v0.md). Every evidence item
used to support failure, harm, acknowledgement, remedy, repair, counter-evidence,
correction, revocation, forgiveness, or closure should have boundary metadata or be
treated as incomplete evidence. A repair lifecycle should reference these records
through `evidence_boundary_refs` rather than treating raw receipts, messages,
attestations, payments, logs, lockups, or reputation updates as settled meaning.

When repair involves a paid job, promise, acceptance criteria, breach, remedy,
satisfaction, or obligation closure, the record should link to
[`obligation-object-v0`](obligation-object-v0.md) through `related_obligation_refs`.
Refund or payment evidence may be part of a remedy, but it does not by itself repair the
relationship, satisfy the obligation, or prove justice.

When failure or misuse involves delegated authority, AI agents, operators, capabilities,
keys, scopes, revocations, or accountability paths, the record should link to
[`delegation-record-v0`](delegation-record-v0.md) through `related_delegation_refs`.
Delegated-agent misuse cannot be repaired honestly without preserving who delegated what,
what scope was claimed, what authority boundary was exceeded or contested, what
revocation or accountability path exists, and what human interpretation remains.

Related Canon and runtime documents include the [Canon map](../MAP.md), the
[Runtime claims matrix](../runtime/claims-matrix.md), [Runtime non-claims](../runtime/non-claims.md),
and the [Canon / Runtime Gap Register](../runtime/gap-register.md).

## Problem

HODLXXI has receipts, obligations, delegation records, trust events, attestations,
verification surfaces, paid jobs, covenant-adjacent evidence, marketplace interactions,
and reputation memory.

These surfaces can preserve that something happened, but they do not by themselves
explain what should happen after a relationship fails or causes harm. Users may infer
stronger claims than the system preserved:

- failure recorded -> blame is settled;
- dispute opened -> accused party is guilty;
- breach declared -> justice occurred;
- apology sent -> repair happened or forgiveness was granted;
- refund paid -> repair happened or an obligation is morally closed;
- repair receipt exists -> the relationship is repaired;
- closure recorded -> justice occurred;
- forgiveness recorded -> memory should be erased;
- reputation improved -> trust has been restored;
- mediator attested -> harm is resolved;
- agent corrected output -> delegated misuse was accountable;
- lockup performed -> commitment was real;
- marketplace dispute closed -> affected party had a fair path to contest.

The repair lifecycle exists to prevent those false inference chains. It makes visible
the difference between event memory, contested meaning, obligation context, delegated
authority context, remedy attempt, affected-party response, changed behavior, forgiveness,
re-entry, reputation effects, and closure.

## Non-goals

This document does not:

- create a court system;
- define enforceable law;
- guarantee justice;
- force forgiveness;
- erase legitimate memory of harm;
- turn every disagreement into a formal dispute;
- prove moral transformation;
- require all repair details to be public;
- implement runtime code;
- authorize reputational punishment without context;
- treat refund, apology, closure, or receipt evidence as repair by itself;
- treat delegated-agent remediation as adequate without delegation and accountability context.

## Required fields

A minimum repair lifecycle record needs the following fields before HODLXXI can honestly
represent repair after failure, dispute, breach, misuse, or harm.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `repair_id` | A stable identifier for this repair lifecycle record. | Without a stable identifier, evidence, updates, acceptance, rejection, correction, review, and later reputation context cannot refer to the same repair process. | It does not prove repair is valid or fair. |
| `affected_parties` | Parties who claim harm, reliance loss, breach, misuse, or other injury. | Repair cannot be modeled honestly without naming whose interests are at stake, even if identities remain private, selective, or pseudonymous. | It does not prove every affected party has been identified. |
| `responsible_parties` | Parties alleged, admitted, delegated, operationally responsible, or determined within the record to have responsibility to answer, correct, compensate, apologize, revoke, mediate, or otherwise participate. | Repair requires a declared accountability surface rather than vague blame, anonymous system failure, or agent-only responsibility. | It does not prove fault, legal liability, or moral responsibility is settled. |
| `related_obligation_refs` | References to obligation objects when the failure, remedy, refund, restitution, acceptance criteria, breach, satisfaction, or closure depends on obligation context. | Repair involving obligations must preserve the promise, acceptance criteria, remedy path, dispute state, and closure boundary rather than treating payment or receipt evidence as the obligation. | It does not prove an obligation existed, was breached, was fulfilled, or was satisfied. |
| `related_delegation_refs` | References to delegation records when an agent, operator, delegate, capability, key, scope, revocation, or accountability path is relevant. | Delegated-agent misuse requires delegation and accountability context, including scope and authority boundaries, before repair can be interpreted. | It does not prove authority was valid, exceeded, revoked, or repaired. |
| `failure_or_harm_claim` | A bounded statement of the harm, failure, breach, misuse, disputed effect, or alleged harm being raised. | The lifecycle must preserve what is being repaired or contested so repair is not reduced to generic apology, refund, closure, or reputation update. | It does not prove the claim is true, complete, uncontested, or justly framed. |
| `evidence_refs` | Receipts, signatures, messages, attestations, payment proofs, revocation records, verification outputs, logs, lockups, mediator statements, or other evidence relevant to the lifecycle. | Repair claims need evidence links so observers can see what was alleged, acknowledged, attempted, paid, corrected, revoked, or attested. | It does not prove truth, adequacy, justice, sincerity, forgiveness, or restored trust. |
| `evidence_boundary_refs` | References to Evidence Boundary Metadata v0 records for every material evidence item. | Evidence must expose issuer or recorder, subject, verification rule, missing context, non-claims, contradiction, revocation, dispute, counter-evidence, privacy, retention, and human interpretation boundaries. | It does not turn evidence into truth or remove the need for judgment. |
| `event_time` | Time or ordering context for the underlying failure, harm, breach, misuse, dispute, or alleged event. | Repair depends on sequence and horizon; the original event must not be collapsed into later acknowledgement, remedy, or closure timestamps. | It does not prove the event happened as described or that timestamp order is meaningful by itself. |
| `acknowledgement_time` | Time or ordering context for acknowledgement, denial, partial acknowledgement, or awareness of the concern. | Repair needs to distinguish occurrence, awareness, admission, and response order. | It does not prove admission of fault, apology, or repair. |
| `remedy_time` | Time or ordering context for proposed or attempted remedy such as refund, correction, restitution, disclosure, revocation, mediation, or apology. | Observers need to distinguish remedy proposal or attempt from repair over time. | It does not prove the remedy was adequate, accepted, or repaired the relationship. |
| `repair_time` | Time or ordering context for accepted, rejected, partial, abandoned, expired, corrected, or reviewed repair state changes. | Repair status must remain sequence-aware so closure is not inferred from a single timestamp. | It does not prove moral closure, justice, or restored trust. |
| `review_horizon` | Future time, sequence, recurrence window, or review condition used to evaluate changed behavior, repeat failure, re-entry, or reputation effects. | Forgiveness and reputation restoration require changed behavior over time, not only an immediate apology, refund, or attestation. | It does not guarantee behavior will change or that the horizon is sufficient. |
| `acknowledgement` | Current acknowledgement position, such as ignored, noticed, denied, partially acknowledged, acknowledged as process, acknowledged as harm, or admitted responsibility. | Repair needs to separate awareness, process participation, apology, and responsibility. | It does not prove apology, fault, truth, or repair. |
| `remedy` | Proposed or attempted remedy, such as correction, re-performance, refund, restitution, apology, revocation, key rotation, mediation, disclosure, changed practice, or access restoration. | Repair must expose what action is supposed to address the failure rather than merely recording shame, payment, or closure. | It does not prove repair, adequacy, acceptance, justice, or forgiveness. |
| `repair_action` | Actions taken or required to repair, distinct from remedy evidence and including process changes, accountability steps, restitution, correction, revocation, or relationship-specific repair. | Repair must be represented as more than the fact that evidence exists or money moved. | It does not prove the affected relationship is restored. |
| `changed_behavior_evidence` | Evidence and boundary references relevant to behavior after the remedy across the review horizon. | Forgiveness and reputation restoration require memory plus repair context plus changed behavior over time. | It does not prove moral transformation, permanent trustworthiness, or that all affected parties forgive. |
| `dispute_path` | Path for affected parties, responsible parties, or accepted processes to dispute facts, interpretation, authority, obligation, remedy, repair, closure, or reputation effect. | A repair lifecycle without a dispute path risks closure laundering and coerced meaning. | It does not prove the dispute path is fair, accessible, or sufficient. |
| `counter_evidence_path` | Path to attach contradictory evidence, missing context, affected-party response, third-party evidence, or later correction. | Evidence of repair must remain contestable and revisable. | It does not prove counter-evidence exists or will be evaluated fairly. |
| `revocation_or_correction_path` | Path to revoke, correct, amend, qualify, or supersede evidence, repair claims, delegation effects, obligation closure, or reputation effects. | Repair records can themselves be wrong, overbroad, coerced, outdated, or reputation-laundering. | It does not prove revocation or correction will be accepted. |
| `forgiveness_signal` | Optional, bounded signal of forgiveness, non-forgiveness, conditional re-entry, no statement, unknown, or unavailable context. | Forgiveness must be separated from apology, remedy, repair attempt, closure, and reputation so memory is not erased by implication. | It does not prove memory should be erased, trust is automatic, or all affected parties forgive. |
| `status` | Current lifecycle state, such as `opened`, `acknowledged`, `under_review`, `contested`, `remedy_proposed`, `remedy_attempted`, `repair_pending`, `repair_attempted`, `accepted`, `partially_accepted`, `rejected`, `forgiven`, `closed`, `abandoned`, `expired`, `corrected`, or `revoked`. | Observers need to distinguish unresolved, contested, pending, attempted, accepted, rejected, forgiven, corrected, revoked, and closed contexts. | It does not prove justice, restored trust, moral closure, or full context. |
| `explicit_non_claims` | Explicit statements about what this repair lifecycle does not prove. | Non-claims prevent repair records from laundering truth, justice, forgiveness, restored trust, obligation satisfaction, delegated authority, or legitimacy. | It prevents overclaim, but it does not ensure users will read or honor the limits. |
| `human_interpretation_required` | Whether human, affected-party, mediator, operator, or community interpretation is required before stronger claims can be made. | Repair, forgiveness, obligation closure, authority misuse, and reputation restoration often involve human meaning beyond machine verification. | It does not prove the human interpretation is fair, available, or final. |

## Compatibility notes

Earlier drafts and runtime discussions may use names such as `related_event`,
`trigger_event`, `related_objects`, `harm_or_failure_claim`, `dispute_position`,
`acknowledgement_state`, `remedy_plan`, `remedy_evidence`, `affected_response`,
`repair_state`, `forgiveness_state`, `acceptance_criteria`, `reputation_effect`,
`memory_policy`, or `non_claims`. Those names may remain useful as aliases or local
views, but a hardened lifecycle should expose the required fields above when making
repair, forgiveness, closure, obligation, delegation, or reputation claims.

## Optional fields

Optional fields may help specific contexts without making every repair lifecycle heavy:

- `privacy_scope`
- `disclosure_policy`
- `mediator`
- `reviewer`
- `appeal_path`
- `acceptance_criteria`
- `affected_response`
- `dispute_position`
- `memory_policy`
- `reputation_effect`
- `partial_repair_terms`
- `forgiveness_statement`
- `re_entry_conditions`
- `repeat_failure_policy`
- `retaliation_risk`
- `related_delegation_revocation`
- `related_obligation_closure`
- `version`

These fields should remain optional because repair contexts vary by severity, privacy,
reversibility, counterparty familiarity, jurisdictional context, and evidentiary needs.
A small correction may need only a lightweight record, while a serious delegation misuse
or obligation breach may need mediator, appeal, disclosure, revocation, restitution, and
re-entry context.

Optional fields must not become hidden mandatory bureaucracy. They should add precision
where needed without implying that a low-risk repair is illegitimate merely because it
omits heavyweight context.

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names
states that may be useful when discussing failure, dispute, breach, misuse, harm,
repair, forgiveness, and closure.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `opened` | A failure, dispute, breach, misuse, harm, or alleged harm has been recorded as needing review or response. | Opened means wrongdoing is proven. |
| `acknowledged` | A party acknowledges the record, concern, or process. | Acknowledgment means admission of fault or apology. |
| `under_review` | Evidence, claims, authority, consent, quality, impact, obligation context, delegation context, or remedy options are being examined. | Review means neutrality, fairness, or completeness. |
| `contested` | One or more parties dispute facts, interpretation, responsibility, harm, authority, obligation, or remedy. | Contested means bad faith. |
| `remedy_proposed` | A remedy path has been offered. | Proposed remedy means repair happened. |
| `remedy_attempted` | A refund, correction, apology, restitution, revocation, mediation, or other remedy has been attempted. | Attempted remedy means repair succeeded. |
| `repair_pending` | Repair action or review of changed behavior is expected or in progress. | Pending repair means repair will occur. |
| `repair_attempted` | A party records that it attempted relationship-specific or context-specific repair beyond bare remedy evidence. | Attempted repair means the relationship is repaired. |
| `accepted` | Affected parties or an authorized process accept the repair under recorded criteria. | Accepted means all harm is gone or trust is fully restored. |
| `partially_accepted` | Some repair was accepted while some harm, dispute, obligation, delegation, or remedy remains unresolved. | Partial acceptance means full closure. |
| `rejected` | Affected parties or an authorized process reject the proposed or attempted remedy or repair. | Rejection means the responding party is permanently illegitimate. |
| `forgiven` | Forgiveness or re-entry has been recorded by a party or accepted process after preserved memory, repair context, and changed behavior over time. | Forgiveness means memory is erased or trust is automatic. |
| `closed` | The repair lifecycle is no longer active under the recorded object. | Closed means morally settled, just, or forgotten. |
| `abandoned` | The process ended without accepted repair or ordinary closure. | Abandoned means no harm occurred. |
| `expired` | A review or remedy window ended. | Expired means no memory, accountability, dispute, or reputation context remains. |
| `corrected` | A prior repair record, evidence item, obligation closure, delegation interpretation, or reputation effect was corrected. | Corrected means the new interpretation is complete or final. |
| `revoked` | A prior claim, signal, attestation, delegation effect, closure, or reputation effect was revoked or superseded. | Revoked means all downstream harm has been undone. |

## Runtime surfaces

The repair lifecycle may refer to existing or expected runtime surfaces, but none of
these surfaces proves repair by itself.

| Runtime surface | Possible role in repair lifecycle | What it does not prove alone |
| --- | --- | --- |
| Signed receipt | Event proof linked to request, payment, execution, verification, failure, remedy, or repair attempt, with evidence boundary metadata. | It does not prove obligation, harm, repair, forgiveness, justice, or restored relationship. |
| `/agent/verify/<job_id>` | Bounded verification of a job, receipt, or repair-related claim. | It does not prove final meaning, acceptance, satisfaction, or changed behavior. |
| `/agent/attestations` | Statements by a party, agent, verifier, mediator, operator, or system surface. | It does not prove truth, sincerity, legitimacy, settlement, or forgiveness. |
| `/agent/trust/events` | Event memory for chronology, continuity, dispute, repair attempt, acceptance, rejection, correction, revocation, or closure. | It does not prove fairness, complete context, moral resolution, or restored trust. |
| `/agent/reputation` | Contextual memory that may distinguish unresolved failure, accepted repair, forgiveness, re-entry, and repeated behavior. | It does not prove global trustworthiness, moral worth, or that trust should be restored. |
| Evidence Boundary Metadata v0 | Boundary records for evidence used in harm, acknowledgement, remedy, repair, counter-evidence, forgiveness, closure, and reputation claims. | It does not make evidence true or interpretation automatic. |
| Minimum Obligation Object v0 | Related promise, acceptance criteria, breach condition, remedy path, dispute state, or closure state. | It does not prove breach, repair, satisfaction, or justice by itself. |
| Minimum Delegation Record v0 | Related grant, scope, misuse, revocation, accountability path, or repair obligation after misuse. | It does not prove authority was valid or misuse was repaired by itself. |
| Lightning invoice or payment proof | Refund, restitution, compensation, or cost evidence. | It does not prove repair, apology, acceptance, closure, obligation satisfaction, or restored trust. |
| Human Proof | Evidence relevant to human presence or identity context. | It does not prove full identity, consent, harm, authority, or forgiveness. |
| Covenant lockup | Evidence of value constraint, time constraint, or repair-adjacent commitment context. | It does not prove remorse, legitimacy, completed repair, or authentic commitment. |
| Future dispute endpoint | Opening, update, evidence, challenge, mediation, or outcome publication. | It would not prove justice, fairness, or full context by itself. |
| Future repair endpoint | Proposed remedy, repair action, acceptance, rejection, forgiveness signal, correction, revocation, or closure publication. | It would not prove that harm disappeared, forgiveness occurred, or trust was restored. |

## Example mappings

These examples are mappings, not normative outcomes. They show what context the lifecycle
should preserve before stronger interpretations are made.

| Scenario | Required repair lifecycle emphasis | Unsafe inference to avoid |
| --- | --- | --- |
| Failed paid 21-sat job | Link `related_obligation_refs` to the relevant obligation context if the paid job created or touched an obligation; attach receipt, invoice, verification, failure, refund, re-performance, and boundary records through `evidence_refs` and `evidence_boundary_refs`; preserve `event_time`, `acknowledgement_time`, `remedy_time`, and `repair_time`. | Refund paid means the obligation was satisfied, the customer is satisfied, or the relationship is repaired. |
| Incorrect signed receipt | Preserve the original receipt as evidence, attach correction or revocation through `revocation_or_correction_path`, expose counter-evidence, and avoid deleting the memory of the mistaken receipt. | Corrected receipt means the original error never happened or no downstream harm remains. |
| Agent acted beyond delegated authority | Link `related_delegation_refs`; preserve scope, prohibited actions, authority source, revocation, accountability, and affected-party paths; link obligations if the agent created, changed, fulfilled, breached, or disputed an obligation. | Agent apologized, corrected output, or refunded payment means delegated misuse was repaired. |
| Marketplace dispute | Preserve marketplace event evidence with boundary metadata, affected and responsible parties, dispute and counter-evidence paths, remedy path, and review horizon before reputation effects. | Dispute closure means justice occurred or marketplace reputation should reset. |
| Covenant lockup used as commitment theater | Treat the lockup as constraint evidence with boundary metadata; link any obligation or reciprocity context separately; require failure or harm claim, affected-party response, and non-claims about commitment. | Locked sats prove commitment, sincerity, or repair. |
| Reputation restoration after repair | Require preserved memory, repair context, changed behavior evidence across the review horizon, affected-party or accepted-process response where available, and explicit non-claims. | Reputation restoration means forgiveness, erased harm, global trustworthiness, or restored relationship. |

## What it can prove

A well-formed repair lifecycle can prove or support only bounded claims:

- that a repair process was represented;
- that a failure or harm claim was declared;
- that affected and responsible parties were recorded;
- that relevant obligation references were attached when obligation context mattered;
- that relevant delegation references were attached when delegated authority mattered;
- that evidence references and evidence boundary references were attached;
- that event, acknowledgement, remedy, repair, and review horizon time semantics were recorded;
- that acknowledgement, remedy, repair action, dispute path, counter-evidence path, and revocation or correction path were represented;
- that changed behavior evidence and a forgiveness signal, if any, were recorded with boundaries;
- that status, explicit non-claims, and human interpretation requirements were visible.

It still does not prove truth, blame, adequacy, satisfaction, forgiveness, justice,
restored trust, obligation closure, delegated authority validity, or full identity by
itself.

## What it must not prove

The existence or state of a repair lifecycle must not be used for these overclaims:

- repair lifecycle exists -> wrongdoing is proven;
- dispute exists -> accused party is guilty;
- remedy proposed -> repair happened;
- refund paid -> repair happened;
- refund paid -> obligation is morally satisfied;
- apology recorded -> harm is repaired;
- apology recorded -> forgiveness was granted;
- repair evidence exists -> relationship is repaired;
- accepted repair -> all harm is gone;
- forgiven -> memory is erased;
- closed -> justice occurred;
- reputation recovered -> trust is restored;
- mediator attested -> settlement is legitimate in every sense;
- agent corrected action -> delegated misuse had valid authority or was repaired;
- lockup observed -> commitment was sincere.

## Failure modes

- fake repair lifecycle;
- vague failure or harm claim;
- missing affected parties;
- hidden responsible party;
- missing evidence boundary metadata;
- raw evidence treated as truth;
- refund treated as repair;
- apology treated as forgiveness;
- repair receipt treated as restored trust;
- harm erased from memory;
- closure laundering;
- coercive forgiveness;
- mediator capture;
- reputation restored without changed behavior;
- reputation restored without preserved memory;
- repair used as reputation laundering;
- permanent punishment disguised as memory;
- private harm exposed publicly;
- retaliation against a disputing party;
- obligation breach closed without obligation-object context;
- obligation breach closed without affected-party acceptance or dispute path;
- agent misuse repaired without delegation/accountability context;
- agent-created repair without authority;
- delegated authority scope ignored during repair;
- affected party has no dispute or counter-evidence path;
- revocation or correction unavailable for mistaken repair records;
- covenant lockup used as commitment or repair theater;
- marketplace dispute closure treated as justice.

## Falsification tests

- Do users distinguish event proof from accepted repair when both are shown together?
- Do users distinguish refund, remedy, repair action, and relationship restoration?
- Do users distinguish apology from forgiveness?
- Do users still infer guilt from a dispute state?
- Do users still infer justice from a closed repair lifecycle?
- Do affected parties report better understanding when dispute paths, counter-evidence paths, acceptance criteria, and non-claims are visible?
- Do repair records preserve evidence boundary metadata for every material evidence reference?
- Do obligation-related repairs link to obligation-object context before satisfaction or closure language appears?
- Do delegated-agent misuse repairs link to delegation records, scope, revocation, and accountability context?
- Do repair records reduce repeated disputes or merely create closure theater?
- Do agents or operators use repair lifecycle records to launder reputation after misuse?
- Does reputation restoration depend on changed behavior over a review horizon rather than a single refund, apology, or receipt?
- Does privacy-aware memory preserve accountability without creating permanent public punishment?
- Does the lifecycle become too heavy for small failures and corrections?

## Open questions

- What is the minimum useful repair lifecycle record?
- Which states must be machine-readable?
- Which states should remain human-readable?
- Which repair details should be private or selectively disclosed?
- Who can open a repair lifecycle?
- Who can accept or reject repair?
- How should forgiveness be represented without erasing memory?
- How should changed behavior over time be measured without becoming surveillance or a score?
- How should repair affect reputation without becoming a score reset?
- How should repair interact with obligation closure?
- How should repair interact with delegation revocation, suspension, or misuse?
- When should abandoned, corrected, revoked, or expired repair remain visible?
