# Repair Lifecycle v0

## Purpose

This document defines the minimum conceptual lifecycle needed to represent what happens
after failure, dispute, breach, misuse, or harm in HODLXXI.

Repair is not erasure. Repair is not automatic forgiveness. Repair is not reputational
laundering. Repair is not punishment by another name. Repair is not proven by a receipt
alone.

Repair requires bounded memory of the original event, a declared failure or harm
context, affected parties, proposed remedy, evidence of repair attempt, acceptance or
rejection state, and explicit non-claims about justice, forgiveness, and restored trust.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract,
legal remedy process, mediation protocol, or implementation claim.

## Problem

HODLXXI has receipts, obligations, delegation records, trust events, attestations,
verification surfaces, paid jobs, covenant-adjacent evidence, and reputation memory.

These surfaces can preserve that something happened, but they do not by themselves
explain what should happen after a relationship fails or causes harm. Users may infer
stronger claims than the system preserved:

- failure recorded -> blame is settled;
- dispute opened -> accused party is guilty;
- breach declared -> justice occurred;
- apology sent -> repair happened;
- refund paid -> obligation is morally closed;
- forgiveness recorded -> memory should be erased;
- reputation improved -> trust has been restored;
- mediator attested -> harm is resolved.

The repair lifecycle exists to prevent those false inference chains. It makes visible
the difference between event memory, contested meaning, remedy attempt, acceptance,
forgiveness, re-entry, and closure.

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
- authorize reputational punishment without context.

## Required fields

A minimum repair lifecycle record needs the following fields before HODLXXI can honestly
represent repair after failure, dispute, breach, misuse, or harm.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `repair_id` | A stable identifier for this repair lifecycle record. | Without a stable identifier, evidence, updates, acceptance, rejection, closure, and later reputation context cannot refer to the same repair process. | It does not prove repair is valid or fair. |
| `related_event` | The bounded event, failure, dispute, breach, misuse, harm, or alleged harm that opened the repair lifecycle. | Repair needs a declared event anchor so it is not free-floating reputation theater or punishment without context. | It does not prove the allegation is true or complete. |
| `trigger_event` | A compatibility or human-readable reference to the initiating event, when distinct from `related_event`. | Some records may need to preserve the language of the initiating complaint or system event while still linking to a bounded event reference. | It does not prove causation, fault, or settled interpretation. |
| `related_objects` | Linked obligations, delegation records, receipts, attestations, trust events, payments, messages, or verification records. | Repair must show which preserved events and claims it depends on. | It does not transform linked evidence into complete truth. |
| `affected_parties` | Parties who claim harm, reliance loss, breach, misuse, or other injury. | Repair cannot be modeled honestly without naming whose interests are at stake, even if some identities remain private or pseudonymous. | It does not prove every affected party has been identified. |
| `responsible_parties` | Parties alleged, admitted, or determined within the record to have responsibility to answer, correct, compensate, apologize, mediate, revoke, or otherwise participate. | Repair requires a declared accountability surface rather than vague blame or anonymous system failure. | It does not prove fault, legal liability, or moral responsibility is settled. |
| `harm_or_failure_claim` | A bounded statement of the harm, failure, breach, misuse, or disputed effect being raised. | The lifecycle must preserve what is being repaired or contested so repair is not reduced to generic apology, refund, or reputation update. | It does not prove the claim is true, complete, or uncontested. |
| `dispute_position` | The current position of relevant parties, such as alleged, admitted, denied, contested, partially accepted, unknown, or mediated. | Valid receipts can coexist with contested meaning, quality, authority, consent, or harm. | It does not prove bad faith, guilt, neutrality, or final judgment. |
| `acknowledgement_state` | Whether the record, concern, harm, responsibility, or process has been acknowledged, denied, ignored, partially acknowledged, or left unknown. | Repair needs to distinguish awareness of a claim from admission of responsibility or completed remedy. | It does not prove apology, fault, acceptance, or repair. |
| `remedy_plan` | Correction, re-performance, refund, restitution, apology, revocation, key rotation, mediation, disclosure, changed practice, or other proposed remedy. | Repair must expose what action is supposed to address the failure rather than merely recording shame or blame. | It does not prove the remedy is adequate or accepted. |
| `remedy_evidence` | Receipts, signatures, messages, attestations, payment proofs, revocation records, verification outputs, or mediator statements relevant to a remedy attempt. | Remedy claims need evidence links so observers can see what was attempted, paid, corrected, revoked, or attested. | It does not prove sincerity, adequacy, justice, or restored trust. |
| `affected_response` | The affected party or accepted process response to the remedy, such as pending, accepted, rejected, partially accepted, no response, or unknown. | Repair cannot be honestly represented by the actor attempting repair alone; the affected side or accepted process must be visible where available. | It does not prove all affected parties are satisfied or that silence equals consent. |
| `repair_state` | Current repair lifecycle state, such as `opened`, `under_review`, `repair_proposed`, `repair_pending`, `repair_attempted`, `accepted`, `rejected`, `closed`, `abandoned`, or `expired`. | Observers need to distinguish unresolved, contested, pending, attempted, accepted, rejected, and closed contexts. | It does not prove justice, restored trust, or moral closure. |
| `forgiveness_state` | Whether forgiveness, non-forgiveness, conditional re-entry, no statement, or unknown forgiveness context has been recorded. | Forgiveness must be separated from repair, closure, and reputation so memory is not erased by implication. | It does not prove memory should be erased or trust is automatic. |
| `acceptance_criteria` | Conditions under which the remedy may be treated as accepted, rejected, partially accepted, or expired. | Repair needs testable boundaries so closure is not inferred from payment, apology, or passage of time alone. | It does not prove affected parties are satisfied. |
| `reputation_effect` | Whether and how the repair lifecycle may inform reputation memory. | Reputation should distinguish unresolved harm, accepted repair, rejected repair, forgiveness, and re-entry instead of collapsing them into a score. | It does not prove global trustworthiness or moral worth. |
| `memory_policy` | How the original event, dispute, repair attempt, and closure should remain visible, private, selective, or summarized. | Repair must not become erasure, but memory must also avoid unbounded punishment and unnecessary disclosure. | It does not guarantee every observer will apply the policy correctly. |
| `non_claims` | Explicit statements about what this repair lifecycle does not prove. | Non-claims prevent repair records from laundering justice, forgiveness, restored trust, or legitimacy. | It prevents overclaim, but it does not ensure users will read or honor the limits. |

## Optional fields

Optional fields may help specific contexts without making every repair lifecycle heavy:

- `privacy_scope`
- `disclosure_policy`
- `mediator`
- `reviewer`
- `appeal_path`
- `expiry_or_review_time`
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
| `acknowledged` | A party acknowledges the record, concern, or process. | Acknowledgment means admission of fault. |
| `under_review` | Evidence, claims, authority, consent, quality, impact, or remedy options are being examined. | Review means neutrality, fairness, or completeness. |
| `contested` | One or more parties dispute facts, interpretation, responsibility, harm, authority, or remedy. | Contested means bad faith. |
| `repair_proposed` | A remedy or repair path has been offered. | Proposed repair means the remedy is adequate. |
| `repair_pending` | A remedy is expected or in progress. | Pending repair means repair will occur. |
| `repair_attempted` | A party records that it attempted correction, restitution, apology, revocation, mediation, or other remedy. | Attempted repair means repair succeeded. |
| `accepted` | Affected parties or an authorized process accept the repair under recorded criteria. | Accepted means all harm is gone or trust is fully restored. |
| `partially_accepted` | Some repair was accepted while some harm, dispute, or remedy remains unresolved. | Partial acceptance means full closure. |
| `rejected` | Affected parties or an authorized process reject the proposed or attempted repair. | Rejection means the responding party is permanently illegitimate. |
| `forgiven` | Forgiveness or re-entry has been recorded by a party or accepted process after memory and repair context. | Forgiveness means memory is erased or trust is automatic. |
| `closed` | The repair lifecycle is no longer active under the recorded object. | Closed means morally settled, just, or forgotten. |
| `abandoned` | The process ended without accepted repair or ordinary closure. | Abandoned means no harm occurred. |
| `expired` | A review or remedy window ended. | Expired means no memory, accountability, or reputation context remains. |

## Runtime surfaces

The repair lifecycle may refer to existing or expected runtime surfaces, but none of
these surfaces proves repair by itself.

| Runtime surface | Possible role in repair lifecycle | What it does not prove alone |
| --- | --- | --- |
| Signed receipt | Event proof linked to request, payment, execution, verification, failure, or repair attempt. | It does not prove obligation, harm, repair, forgiveness, or justice. |
| `/agent/verify/<job_id>` | Bounded verification of a job, receipt, or repair-related claim. | It does not prove final meaning, acceptance, or satisfaction. |
| `/agent/attestations` | Statements by a party, agent, verifier, mediator, operator, or system surface. | It does not prove truth, sincerity, legitimacy, or settlement. |
| `/agent/trust/events` | Event memory for chronology, continuity, dispute, repair attempt, acceptance, rejection, or closure. | It does not prove fairness, complete context, or moral resolution. |
| `/agent/reputation` | Contextual memory that may distinguish unresolved failure, accepted repair, forgiveness, and re-entry. | It does not prove global trustworthiness or moral worth. |
| Minimum Obligation Object v0 | Related promise, acceptance criteria, breach condition, remedy path, dispute state, or closure state. | It does not prove breach, repair, satisfaction, or justice by itself. |
| Minimum Delegation Record v0 | Related grant, scope, misuse, revocation, accountability path, or repair obligation after misuse. | It does not prove authority was valid or misuse was repaired by itself. |
| Lightning invoice or payment proof | Refund, restitution, compensation, or cost evidence. | It does not prove apology, acceptance, closure, or restored trust. |
| Human Proof | Evidence relevant to human presence or identity context. | It does not prove full identity, consent, harm, or forgiveness. |
| Covenant lockup | Evidence of value constraint, time constraint, or repair-adjacent commitment context. | It does not prove remorse, legitimacy, or completed repair. |
| Future dispute endpoint | Opening, update, evidence, challenge, mediation, or outcome publication. | It would not prove justice or full context by itself. |
| Future repair endpoint | Proposed remedy, repair attempt, acceptance, rejection, forgiveness, or closure publication. | It would not prove that harm disappeared or trust was restored. |

## What it can prove

A well-formed repair lifecycle can prove or support only bounded claims:

- that a repair process was represented;
- that a related event was declared;
- that affected and responsible parties were recorded;
- that a harm or failure claim and dispute position were stated;
- that acknowledgement, affected response, repair, and forgiveness states were recorded;
- that a remedy plan and remedy evidence were attached;
- that acceptance criteria, memory policy, and reputation effect were declared;
- that non-claims were visible.

It still does not prove truth, blame, adequacy, satisfaction, forgiveness, justice,
restored trust, or full identity by itself.

## What it must not prove

The existence or state of a repair lifecycle must not be used for these overclaims:

- repair lifecycle exists -> wrongdoing is proven;
- dispute exists -> accused party is guilty;
- remedy proposed -> repair happened;
- refund paid -> obligation is morally satisfied;
- apology recorded -> harm is repaired;
- accepted repair -> all harm is gone;
- forgiven -> memory is erased;
- closed -> justice occurred;
- reputation recovered -> trust is restored;
- mediator attested -> settlement is legitimate in every sense.

## Failure modes

- fake repair lifecycle;
- vague related event;
- missing affected parties;
- hidden responsible party;
- coercive forgiveness;
- apology theater;
- refund laundering;
- mediator capture;
- closure laundering;
- reputation laundering;
- permanent punishment disguised as memory;
- memory erasure disguised as repair;
- private harm exposed publicly;
- retaliation against a disputing party;
- agent-created repair without authority;
- delegation misuse repaired only cosmetically;
- obligation breach closed without affected-party acceptance.

## Falsification tests

- Do users distinguish event proof from accepted repair when both are shown together?
- Do users still infer guilt from a dispute state?
- Do users still infer justice from a closed repair lifecycle?
- Do affected parties report better understanding when acceptance criteria and non-claims are visible?
- Do repair records reduce repeated disputes or merely create closure theater?
- Do agents or operators use repair lifecycle records to launder reputation after misuse?
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
- How should repair affect reputation without becoming a score reset?
- How should repair interact with obligation closure?
- How should repair interact with delegation revocation, suspension, or misuse?
- When should abandoned or expired repair remain visible?
