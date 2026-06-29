# Reciprocity Pattern v0

## Purpose

This document defines the minimum conceptual structure needed to represent reciprocity
in HODLXXI.

Reciprocity is not a transaction. Reciprocity is not payment history. Reciprocity is not
transaction count. Reciprocity is not a trust score. Reciprocity is not repeated
activity. Reciprocity is not symmetry at every moment. Reciprocity is not immediate
exchange. Reciprocity is not guaranteed by friendship, kinship, covenant, marketplace
history, or agent interaction.

Reciprocity requires a pattern over time among recognizable counterparties,
expectations, asymmetry, memory, repair context, and changed behavior. Bounded evidence
may support that pattern, but evidence does not make the pattern true by itself.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract,
relationship classifier, legal claim, reputation score, trust score, or implementation
claim.

## Canon claims and mechanism dependency

This mechanism cites existing Canon claims without changing their meanings.

| Claim ID | Source | Boundary used by this mechanism |
| --- | --- | --- |
| `CRT-RECIPROCITY-001` | [Reciprocity Is Not Transaction](../chapters/reciprocity-is-not-transaction.md) | A transaction is an event; reciprocity is a pattern across events, actors, memory, expectation, and time. |
| `CRT-EVIDENCE-001` | [Evidence Is Not Truth](../chapters/evidence-is-not-truth.md) | Evidence can support reciprocity interpretation, but it does not settle truth, fairness, trust, or relationship meaning by itself. |
| `CRT-TIME-001` | [Time Is Not Timestamp](../chapters/time-is-not-timestamp.md) | Reciprocity needs sequence, horizon, delay, recurrence, repair review, and changed behavior context; timestamps alone are not enough. |
| `CRT-OBLIGATION-001` | [Obligation Is Not Payment](../chapters/obligation-is-not-payment.md) | Payment history is not obligation, and obligation history is not reciprocal relationship by itself. |
| `CRT-REPUTATION-001` | [Reputation Is Not a Score](../chapters/reputation-is-not-a-score.md) | Reputation context may inform interpretation, but a score, count, badge, or summary is not reciprocity. |
| `CRT-FORGIVENESS-001` | [Memory Before Forgiveness](../chapters/memory-before-forgiveness.md) | Repair, forgiveness, and re-entry require preserved memory and changed behavior; a repair record does not restore reciprocity by itself. |

Reciprocity Pattern v0 explicitly depends on
[`evidence-boundary-metadata-v0`](evidence-boundary-metadata-v0.md). Each event,
payment, receipt, attestation, message, covenant reference, delegation record, repair
record, or reputation input used to support a reciprocity pattern should have an
`evidence_boundary_refs` entry or be treated as incomplete evidence. Raw activity must
not be read as reciprocal meaning without issuer, subject, verification rule, missing
context, non-claims, contradiction, dispute, revocation, privacy, retention, and human
interpretation boundaries.

When reciprocal interpretation involves promises, acceptance criteria, paid jobs,
breach, remedy, satisfaction, or obligation closure, this mechanism should link to
[`obligation-object-v0`](obligation-object-v0.md) through `obligation_refs`. Obligation
context may explain what parties expected or owed, but it does not prove the
relationship was reciprocal.

When agents act for counterparties, negotiate, request, pay, verify, communicate, or
repair on behalf of humans or other principals, this mechanism should link to
[`delegation-record-v0`](delegation-record-v0.md) through `delegation_refs`. Agent
activity cannot safely identify the true counterparty, authority boundary, consent,
accountability path, or relationship context without delegation records.

When failures, breaches, disputes, forgiveness, changed behavior, or re-entry affect
reciprocity, this mechanism should link to
[`repair-lifecycle-v0`](repair-lifecycle-v0.md) through `repair_lifecycle_refs`. Repair
records may support interpretation of renewed cooperation, but they must not be treated
as proof that reciprocity, trust, or fairness has been restored.

Related Canon and runtime documents include the [Canon map](../MAP.md), the
[Runtime claims matrix](../runtime/claims-matrix.md), [Runtime non-claims](../runtime/non-claims.md),
and the [Canon / Runtime Gap Register](../runtime/gap-register.md).

## Problem

HODLXXI has receipts, payments, obligations, delegation records, repair records,
covenants, reputation memory, marketplace interactions, agent messages, and trust
events.

These surfaces can preserve events and evidence, but they do not by themselves preserve
reciprocal meaning. Users may infer false claims:

- many transactions -> reciprocity;
- repeated interaction -> trust;
- payment history -> reciprocal relationship;
- equal exchange -> fairness;
- equal sats -> equal burden or benefit;
- locked value -> reciprocal commitment;
- reputation score -> reciprocity;
- repair completed -> reciprocity restored;
- agent interaction -> relationship exists;
- activity volume -> cooperation;
- delayed return -> exploitation or virtue without context.

The reciprocity pattern exists to prevent those false inference chains. It makes visible
the difference between event sequence, counterparties, roles, expectation, asymmetry,
memory, repair, delegation, obligation context, reputation context, private burden, and
bounded evidence over time.

## Non-goals

This document does not:

- create a universal trust score;
- reduce human relationship to transactions;
- infer reciprocity from transaction count, score, or activity volume;
- require perfect symmetry;
- require immediate repayment;
- treat equal exchange as fairness by itself;
- treat payment history as reciprocal relationship;
- treat repair records as restored reciprocity;
- require all relationship context to be public;
- prove friendship, loyalty, love, fairness, legitimacy, or trust;
- guarantee cooperation;
- replace human judgment;
- implement runtime code.

## Required fields

A minimum reciprocity pattern needs the following fields before HODLXXI can honestly
represent reciprocal cooperation as a pattern across time rather than a single
transaction, payment, score, receipt, activity burst, or exchange.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `reciprocity_pattern_id` | Stable identifier for this reciprocity pattern. | Without a stable identifier, events, obligations, delegations, repairs, reputation context, and evidence cannot refer to the same pattern over time. | It does not prove cooperation exists. |
| `counterparties` | Actors, keys, agents, groups, or principals involved. | Reciprocity requires recognizable counterparties so response, delay, asymmetry, and repair are not free-floating event claims. | It does not prove full identity, authority, loyalty, or stable relationship. |
| `counterparty_roles` | Role labels such as buyer, seller, requester, performer, delegator, delegate, family member, friend, covenant participant, mediator, or observer. | Roles shape expectations and reveal when agents or intermediaries may hide the true counterparty. | It does not prove the role is legitimate or consented to. |
| `relationship_context` | Family, friend, marketplace, service, agent delegation, covenant, community, repair/re-entry, mixed, private, or unknown context. | The same event sequence can mean different things in different contexts; interpretation needs a declared frame. | It does not prove affection, kinship, legitimacy, or trust. |
| `event_refs` | References to ordered events such as payments, receipts, requests, obligations, repairs, messages, attestations, covenant actions, or marketplace interactions. | Reciprocity is interpreted across events, so chronology and event type must be visible. | It does not transform repeated events into reciprocity. |
| `evidence_boundary_refs` | References to evidence boundary records for each material event or input. | Reciprocity claims need bounded evidence so raw records are not overread as truth, fairness, trust, or relationship meaning. | It does not make evidence complete or true. |
| `obligation_refs` | Related obligation objects where promises, acceptance criteria, breach, remedy, satisfaction, or closure affect the pattern. | Obligations may explain expectations, failures, remedy paths, and unresolved burdens. | It does not prove obligations were fulfilled or that the relationship was reciprocal. |
| `delegation_refs` | Related delegation records where agents or delegates act for counterparties. | Delegation context is needed to identify authority scope, true counterparty, consent evidence, revocation, and accountability. | It does not prove the delegate acted wisely, loyally, or legitimately. |
| `repair_lifecycle_refs` | Related repair lifecycles where failures, breaches, disputes, forgiveness, or re-entry affect the pattern. | Repair context is needed to preserve memory and distinguish renewed cooperation from repair laundering. | It does not prove trust or reciprocity was restored. |
| `time_horizon` | Period over which reciprocity is interpreted. | Delayed response, durable support, breach, exit, and repair cannot be evaluated without time boundaries. | It does not prove long-term commitment. |
| `sequence_context` | Ordering semantics for requests, payments, delivery, delay, breach, repair, re-entry, and changed behavior. | Reciprocity depends on order; a delayed return can mean generosity, negligence, repair, exploitation, or normal rhythm depending on sequence. | It does not settle meaning by itself. |
| `expectations` | What each party appears to expect, including explicit, inferred, disputed, or unknown expectations. | Observers need to distinguish gift, payment, debt, service, obligation, care, favor, and cooperation. | It does not prove expectations were shared, legitimate, or understood. |
| `asymmetries` | Declared imbalances in timing, contribution, power, need, risk, information, dependence, or visibility. | Reciprocal cooperation can be asymmetric over time, but asymmetry must be bounded to avoid exploitation laundering. | It does not excuse abuse or coercion. |
| `contributions` | Material and non-material things each party gave, did, risked, or made available. | Transaction count and paid amount omit labor, risk, attention, care, opportunity cost, and private support. | It does not prove value equivalence. |
| `benefits` | Benefits each party received or expected to receive. | Fairness cannot be interpreted without understanding who benefited and how. | It does not prove benefits were adequate, consented, or fairly distributed. |
| `burdens` | Costs, risks, dependencies, private harms, emotional labor, delays, exposure, or opportunity costs borne by each party. | Public records often omit private burden; reciprocity can be falsely claimed when burdens are hidden. | It does not prove the burden was justified or fully known. |
| `delayed_returns` | Expected or observed returns that occur later than the original contribution. | Delayed reciprocity is common but easily confused with default, exploitation, or virtue signaling. | It does not prove delayed return will happen or was owed. |
| `non_monetary_actions` | Care, mentoring, introductions, repair work, restraint, warnings, forgiveness, moderation, or other non-payment actions. | Payment history alone omits many reciprocal actions. | It does not prove non-monetary actions were sufficient or sincere. |
| `dispute_or_breach_context` | Disputed facts, contested expectations, alleged breach, harm, coercion, dependency, cartel risk, or unresolved disagreement. | Reciprocity claims are unsafe when failure or dispute is hidden. | It does not prove guilt, innocence, or final breach. |
| `repair_or_reentry_context` | Repair status, forgiveness annotation, re-entry conditions, changed behavior horizon, and memory/non-erasure rules. | Re-entry into cooperation requires memory and changed behavior, not just closure or apology. | It does not prove restored trust or restored reciprocity. |
| `reputation_context` | Relevant contextual reputation inputs, summaries, disputes, repairs, or confidence limits. | Reputation may inform interpretation of repeated behavior, especially after dispute or re-entry. | It does not reduce reciprocity to a score. |
| `status` | Current conceptual state, such as `observed`, `emerging`, `active`, `asymmetric`, `strained`, `disputed`, `repair_pending`, `repaired`, `forgiven`, `dormant`, `exited`, `broken`, or `unknown`. | Observers need to distinguish tentative, active, damaged, repaired, inactive, ended, and uncertain patterns. | It does not prove moral truth or future cooperation. |
| `explicit_non_claims` | Explicit statements about what this reciprocity pattern does not prove. | Non-claims prevent transaction count, repair, reputation, covenant, or agent interaction from laundering stronger relationship claims. | It prevents overclaim, but it does not ensure users will honor the limits. |
| `human_interpretation_required` | Whether and why human interpretation remains required. | Reciprocity involves meaning, consent, expectation, private burden, and fairness that cannot be settled by records alone. | It does not guarantee correct human judgment. |

## Optional fields

Optional fields may add precision in contexts where reciprocity patterns are
privacy-sensitive, high-stakes, mediated, contested, agentic, or marketplace-adjacent:

- `privacy_scope`
- `disclosure_policy`
- `mediator`
- `verifier`
- `related_covenant`
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

These fields should remain optional because reciprocal patterns vary by relationship,
severity, privacy, power asymmetry, evidentiary need, and time horizon. A casual
marketplace pattern should not require the same disclosure as a long-running covenant,
family support pattern, delegation relationship, or contested repair process.

Optional fields must not become hidden mandatory bureaucracy. They should add context
where needed without implying that an omitted emotion marker, mediator, verifier, or
risk field makes a low-stakes pattern invalid.

## Example mappings

These examples show how the fields bound interpretation. They are not templates for
runtime code and do not prove the relationships described.

| Scenario | Relevant fields | Safe bounded interpretation | Unsafe inference to reject |
| --- | --- | --- | --- |
| Repeated 21-sat jobs between the same actors | `counterparties`, `event_refs`, `evidence_boundary_refs`, `time_horizon`, `sequence_context`, `expectations`, `contributions`, `status`, `explicit_non_claims` | A repeated low-value interaction pattern may be represented as observed or emerging if counterparties, order, expectations, and evidence boundaries are visible. | Twenty-one sat payments, repeated receipts, or successful verification prove trust, satisfaction, obligation fulfillment, or reciprocity. |
| Marketplace buyer/seller history | `counterparty_roles`, `relationship_context`, `event_refs`, `obligation_refs`, `reputation_context`, `dispute_or_breach_context`, `benefits`, `burdens` | Marketplace history can support limited context about repeated trade, fulfillment, disputes, and unresolved burdens. | Buyer/seller activity, ratings, equal payment, or repeat purchases prove reciprocal relationship or fairness. |
| Agent acting for a user across repeated tasks | `counterparties`, `counterparty_roles`, `delegation_refs`, `event_refs`, `evidence_boundary_refs`, `obligation_refs`, `sequence_context`, `human_interpretation_required` | Agent-mediated tasks may be included only with delegation context showing who acted for whom, within what scope, and under what accountability path. | Agent messages or repeated agent performance prove the human principal consented, was the true counterparty, or formed a relationship. |
| Covenant lockup between family or friends | `relationship_context`, `event_refs`, `time_horizon`, `expectations`, `asymmetries`, `benefits`, `burdens`, `delayed_returns`, `explicit_non_claims` | A covenant lockup can be evidence of a constraint within a relationship context and time horizon. | Locked value proves love, loyalty, commitment, fairness, or reciprocal care. |
| Post-repair re-entry into cooperation | `repair_lifecycle_refs`, `dispute_or_breach_context`, `repair_or_reentry_context`, `sequence_context`, `time_horizon`, `reputation_context`, `status` | Re-entry can be represented as tentative renewed cooperation after preserved memory, repair criteria, affected response, and changed behavior horizon. | Repair completed, apology made, refund paid, or forgiveness recorded means reciprocity or trust is restored. |
| Asymmetric help with delayed return | `expectations`, `asymmetries`, `contributions`, `benefits`, `burdens`, `delayed_returns`, `time_horizon`, `human_interpretation_required` | One party giving more now may be recorded as asymmetric cooperation with an expected or uncertain delayed return. | Imbalance proves exploitation, virtue, debt, fairness, or entitlement without context. |

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names
states that may be useful when discussing reciprocal patterns across events, actors,
memory, expectation, asymmetry, repair, and time.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `observed` | Events involving recognizable counterparties have been observed, but reciprocity has not been established or claimed. | Observation means relationship. |
| `emerging` | Repeated interaction and early expectations are visible, but the pattern remains tentative. | Emerging means cooperation is reliable. |
| `active` | The pattern is currently represented as ongoing, with evidence of response across time. | Active means future cooperation is guaranteed. |
| `asymmetric` | The pattern includes delay, imbalance, gift, debt, one-way support, or unequal timing within declared tolerance. | Asymmetry means exploitation is acceptable. |
| `strained` | Expectations, timing, balance, conduct, or response have become concerning but not conclusively broken. | Strain means bad faith or final breach. |
| `disputed` | Parties or observers contest facts, meaning, expectation, obligation, repair, delegation, or state. | Dispute means one side is lying or guilty. |
| `repair_pending` | A repair path is expected, proposed, underway, or awaiting affected response. | Pending repair means repair will occur. |
| `repaired` | A repair lifecycle or accepted process records that a failure was addressed under stated criteria. | Repaired means trust or reciprocity is restored. |
| `forgiven` | Forgiveness, non-retaliation, or re-entry has been recorded with memory preserved. | Forgiven means memory is erased. |
| `dormant` | The pattern is inactive but not necessarily ended or broken. | Dormant means abandoned, safe, or resolved. |
| `exited` | A party or accepted process records exit from the pattern. | Exit means no obligation, memory, harm, or consequence remains. |
| `broken` | The pattern is represented as failed, breached, or no longer sustaining reciprocal cooperation. | Broken means permanent moral judgment. |
| `unknown` | Available evidence is insufficient to assign a more specific state. | Unknown means safe, unsafe, cooperative, or non-cooperative. |

## Runtime surfaces

The reciprocity pattern may refer to existing or expected runtime surfaces, but none of
these surfaces proves reciprocity by itself.

| Runtime surface | Possible role in reciprocity pattern | What it does not prove alone |
| --- | --- | --- |
| Signed receipts | Event proof for work, payment, request, delivery, verification, or response, linked through evidence boundary metadata. | It does not prove obligation, relationship, commitment, satisfaction, fairness, trust, or reciprocity. |
| `/agent/verify/<job_id>` | Verification output for a job or evidence item in the event sequence. | It does not prove shared meaning, satisfaction, or reciprocal cooperation. |
| `/agent/request` | Request surface that may begin or continue an interaction sequence. | It does not prove acceptance, obligation, or relationship. |
| Lightning invoices | Payment request or settlement evidence linked to an event. | It does not prove care, trust, obligation, fairness, or reciprocity. |
| Paid job status | Evidence that a job reached a paid state. | It does not prove satisfaction, commitment, or future cooperation. |
| `/agent/trust/events` | Chronological memory for interactions, disputes, repairs, attestations, and state changes. | It does not prove complete context or moral meaning. |
| `/agent/reputation` | Contextual memory that may inform interpretation of repeated behavior. | It does not prove reciprocal trust or reduce reciprocity to a score. |
| `/agent/attestations` | Statements by parties, agents, verifiers, mediators, or observers. | It does not prove truth, legitimacy, consent, fairness, or stable relationship. |
| Evidence Boundary Metadata v0 | Bounded claim, source, verification, missing context, non-claims, contradiction, dispute, privacy, and interpretation boundary for evidence used by the pattern. | It does not prove truth or reciprocal meaning. |
| Minimum Obligation Object v0 | Linked promises, acceptance criteria, breach conditions, remedy paths, and closure states relevant to the pattern. | It does not prove fulfillment, affection, loyalty, or reciprocity by itself. |
| Minimum Delegation Record v0 | Linked authority, scope, duration, permitted actions, consent evidence, revocation, and accountability where agents act for counterparties. | It does not prove loyalty, wisdom, legitimacy, or relationship depth. |
| Repair Lifecycle v0 | Linked failure, remedy, affected response, forgiveness, memory, changed behavior, and re-entry context. | It does not prove trust was restored or reciprocity resumed. |
| Covenant lockup | Evidence of value constraint, time constraint, or covenant-adjacent commitment context. | It does not prove reciprocal loyalty, legitimate commitment, love, or fairness. |
| Covenant participant keys | Evidence of declared key participation in a covenant context. | It does not prove full identity, kinship, affection, or future cooperation. |
| Human Proof | Human-presence or identity-context evidence relevant to a pattern. | It does not prove consent, character, legitimacy, or reciprocity. |
| Marketplace listing | Public or semi-public offer context that may anchor repeated marketplace interaction. | It does not prove trustworthiness or relationship. |
| Marketplace interaction | Purchase, service, fulfillment, dispute, or review-adjacent evidence. | It does not prove cooperation beyond the bounded interaction. |
| Inter-agent message | Message evidence between agents or humans using agents. | It does not prove intimacy, authority, consent, true counterparty, or relationship. |
| Future reciprocity endpoint | Possible publication or query surface for reciprocity pattern records. | It would not prove moral truth or future cooperation by itself. |
| Future relationship memory endpoint | Possible selective memory surface for relationship context over time. | It would not prove friendship, love, loyalty, or legitimacy by itself. |

## What it can prove

A well-formed reciprocity pattern can prove or support only bounded claims:

- that a pattern was represented;
- that counterparties and roles were declared;
- that events were ordered;
- that evidence boundary references were attached or gaps were visible;
- that time horizon, sequence context, and relationship context were stated;
- that expectations, asymmetries, contributions, benefits, burdens, delayed returns, and non-monetary actions were recorded;
- that obligation, delegation, repair, and reputation context were linked where relevant;
- that dispute, breach, repair, and re-entry context were visible where relevant;
- that explicit non-claims and human interpretation requirements were visible.

It still does not prove friendship, loyalty, love, legitimacy, stable cooperation,
restored trust, fairness, moral worth, or future reciprocity by itself.

## What it must not prove

The existence or state of a reciprocity pattern must not be used for these overclaims:

- pattern exists -> relationship is trustworthy;
- many transactions -> reciprocity;
- repeated interaction -> trust;
- equal exchange -> fairness;
- equal sats -> equal benefit, burden, or justice;
- payment history -> reciprocal relationship;
- one-sided support -> exploitation;
- asymmetry tolerated -> abuse is acceptable;
- delayed return expected -> exploitation or virtue is settled;
- obligation link exists -> reciprocal relationship exists;
- repair link exists -> reciprocity restored;
- reputation context positive -> reciprocal trust exists;
- reputation score high -> reciprocity exists;
- covenant exists -> reciprocal commitment exists;
- agent messages repeated -> relationship exists;
- delegation record exists -> agent created a reciprocal relationship for the principal;
- status active -> future cooperation guaranteed.

## Failure modes

- transaction count treated as reciprocity;
- activity volume treated as cooperation;
- repeated interaction treated as trust;
- equal sats treated as fairness;
- payment history treated as reciprocal relationship;
- reputation score treated as reciprocity;
- one-sided dependence disguised as reciprocity;
- cartel behavior disguised as reciprocity;
- coercive dependency;
- gift turned into obligation trap;
- reputation laundering through repeated small interactions;
- repair record treated as restored reciprocity;
- repair used to reset pattern too easily;
- memory used as permanent punishment;
- agent-mediated interactions hiding the true counterparty;
- agent-generated relationship theater;
- private burden omitted from public record;
- delayed return misread as exploitation or virtue without context;
- sybil-created reciprocity;
- marketplace activity misread as trust;
- covenant lockup misread as reciprocal loyalty;
- family or friendship context exploited;
- default mistaken for delayed reciprocity.

## Falsification tests

- Do users make better trust decisions with pattern context than with transaction count alone?
- Does bounded evidence metadata reduce false reciprocity claims from bare receipts, payments, or attestations?
- Does explicit time horizon and sequence context reduce confusion between delayed reciprocity, default, repair, and exploitation?
- Does explicit asymmetry tolerance reduce false breach accusations?
- Does it also increase tolerance of exploitation?
- Do obligation links help distinguish payment history from reciprocal relationship?
- Do delegation links reveal when agent-mediated interactions hide the true counterparty or authority boundary?
- Do repair lifecycle links help distinguish renewed cooperation from repair laundering?
- Do users overread repaired or active patterns as future guarantees?
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
- How should reciprocity interact with delegation?
- How should reciprocity interact with repair and forgiveness?
- How should AI agents participate in reciprocal patterns without simulating false intimacy?
- What patterns should be impossible or discouraged?
