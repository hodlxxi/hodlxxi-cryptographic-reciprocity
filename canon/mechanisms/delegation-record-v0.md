# Minimum Delegation Record v0

## Purpose

This document defines the minimum conceptual record required to represent delegated
authority in HODLXXI.

Delegation is not capability. Delegation is not key control. Delegation is not mere user
familiarity. Delegation is not agent usefulness. Delegation is not payment. Delegation
is not a signed message by itself. An operator key is not blanket legitimacy, and agent
fluency is not authority.

Delegation requires a bounded grant from a visible delegator to a visible delegate,
within a scope, permitted action set, prohibited action set, authority source, evidence
basis, time horizon, revocation path, accountability path, dispute path, and explicit
non-claims.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract,
legal agency framework, or implementation claim.

## Canon claims and mechanism dependency

This mechanism cites existing Canon claims without changing their meanings.

| Claim ID | Source | Boundary used by this mechanism |
| --- | --- | --- |
| `CRT-AGENT-AUTHORITY-001` | [Bounded Authority for AI Agents](../chapters/bounded-authority-for-ai-agents.md) | Capability, fluency, usefulness, or agent output is not delegated authority. |
| `CRT-IDENTITY-001` | [Identity Is Not Key Control](../chapters/identity-is-not-key-control.md) | Key control, endpoint control, Human Proof, or operator key possession is not full identity or legitimate representation by itself. |
| `CRT-EVIDENCE-001` | [Evidence Is Not Truth](../chapters/evidence-is-not-truth.md) | Signatures, receipts, attestations, messages, and logs are evidence; they do not settle truth, consent, legitimacy, or authority by themselves. |
| `CRT-TIME-001` | [Time Is Not Timestamp](../chapters/time-is-not-timestamp.md) | Delegated authority needs created, effective, expiry, revocation, and ordering context; a timestamp alone is not authority order. |
| `CRT-OBLIGATION-001` | [Obligation Is Not Payment](../chapters/obligation-is-not-payment.md) | Payment, job execution, or receipt evidence does not create obligation or delegation by itself. |

Minimum Delegation Record v0 explicitly depends on
[`evidence-boundary-metadata-v0`](evidence-boundary-metadata-v0.md). Every evidence item
used to support delegated authority should have an `evidence_boundary_refs` entry or be
treated as incomplete evidence. Raw signatures, receipts, paid jobs, attestations,
Human Proof records, operator statements, audit logs, and marketplace events must not be
read as delegated permission without boundary metadata that exposes issuer, subject,
verification rule, missing context, non-claims, revocation path, dispute path, privacy
scope, and human interpretation requirements.

When a delegated action creates, changes, fulfills, breaches, disputes, or otherwise
touches obligations, the delegation record should link to
[`obligation-object-v0`](obligation-object-v0.md) through `obligation_refs`. Delegation
does not replace the obligation object. It only records who was permitted to act, under
what authority boundary, with what evidence and accountability path.

Related Canon and runtime documents include the [Canon map](../MAP.md), the
[Runtime claims matrix](../runtime/claims-matrix.md), [Runtime non-claims](../runtime/non-claims.md),
and the [Canon / Runtime Gap Register](../runtime/gap-register.md).

## Problem

HODLXXI has agent identity surfaces, operator keys, capabilities, paid jobs, receipts,
Human Proof, inter-agent messages, marketplace interactions, future agent workflows, and
future obligation records.

These surfaces are useful, but users may infer stronger claims than the system
preserved:

- capability declared -> authority granted;
- agent signed -> user approved;
- operator key exists -> every action authorized;
- key controlled -> identity or representation proven;
- signed message exists -> delegated permission exists;
- paid job accepted -> agent may act broadly;
- agent remembers me -> agent represents me;
- fluent answer -> legitimate representative;
- inter-agent message -> delegated authority;
- obligation touched by agent -> agent had authority over that obligation.

The delegation record exists to prevent those false inference chains. It makes the
missing grant, scope, action boundary, evidence boundary, time horizon, revocation,
accountability, obligation context, and non-claims visible before HODLXXI presents
stronger claims about delegated authority.

## Non-goals

This document does not:

- create an unrestricted autonomy model;
- give agents broad legal agency;
- define enforceable law;
- replace human judgment;
- prove moral legitimacy;
- prove user satisfaction;
- require all delegation details to be public;
- convert capability into authority;
- convert key control into identity;
- convert a signed message into delegated permission;
- convert operator keys into blanket legitimacy;
- convert evidence boundary metadata into truth;
- convert an obligation reference into authority over that obligation;
- implement runtime code;
- authorize any current runtime action.

## Required fields

A minimum delegation record needs the following fields before HODLXXI can honestly
represent delegated authority.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `delegation_id` | A stable identifier for this delegation record. | Without a stable identifier, later evidence, use, challenge, revocation, rotation, repair, or obligation records cannot refer to the same bounded grant. | It does not prove the delegation is valid or legitimate. |
| `delegator` | The actor, process, organization, user, operator, or prior delegation source granting authority. | Delegation requires a visible source rather than a free-floating capability, signature, payment, operator key, or agent assertion. | It does not prove full human identity, key ownership, legitimate office, or authority unless linked evidence supports those claims. |
| `delegate` | The actor, agent, process, organization, or key receiving bounded authority. | The record must identify who may act under the grant so authority is not transferred to any fluent, capable, or key-controlling actor by implication. | It does not prove capability, competence, continuity, identity, or trustworthiness. |
| `delegator_role` | The role in which the delegator claims to grant authority, such as user, requester, payer, operator, maintainer, verifier, mediator, or obligation party. | Role context prevents key control or payment from being mistaken for every possible authority source. | It does not prove the delegator actually holds that role. |
| `delegate_role` | The role in which the delegate may act, such as runtime agent, task performer, verifier, messenger, market lister, or obligation assistant. | Role context prevents a narrow assistant role from becoming general representation. | It does not prove the delegate may act in any other role. |
| `scope` | The context in which the delegation applies, including subject, domain, counterparty, job, marketplace listing, obligation, or runtime surface when relevant. | Scope prevents a narrow grant from being read as general representation, broad consent, or continuing agency. | It does not imply authority outside that context. |
| `allowed_actions` | Actions the delegate may perform. | The record must distinguish authorized actions from possible actions, useful actions, paid actions, signed actions, or technically available actions. | It does not prove the delegate should perform them in every situation. |
| `prohibited_actions` | Actions explicitly outside the grant. | Explicit exclusions reduce ambiguity where a delegate has capability, memory, keys, market access, obligation access, or persuasive fluency. | It does not prove all other actions are safe. |
| `authority_source` | The bounded basis for the delegator's authority, such as direct user consent, operator policy, prior delegation, obligation role, marketplace terms, or governance process. | Authority needs a declared source so observers do not infer it from capability, key control, signature, payment, or fluency. | It does not prove that the authority source is valid, current, legitimate, or legally enforceable. |
| `consent_evidence_refs` | References to evidence said to support consent, acceptance, or authorization. | Consent evidence must be attached explicitly so a signed agent message, paid job, or operator statement is not treated as consent by itself. | It does not prove informed consent, absence of coercion, or full identity. |
| `evidence_boundary_refs` | References to Evidence Boundary Metadata v0 records for evidence in `consent_evidence_refs`, `audit_log_refs`, obligation records, or other supporting surfaces. | Delegation interpretation depends on evidence type, issuer, subject, verification rule, non-claims, missing context, revocation, dispute, privacy, and human interpretation boundaries. | It does not settle interpretation; it only exposes evidence boundaries. |
| `created_time` | Time the delegation record was created or first represented. | Creation time distinguishes record creation from effective authority, action time, revocation time, and later verification. | It does not prove the delegation was already effective or valid. |
| `effective_time` | Time or interval when the delegation becomes active, if accepted. | Authority may begin after consent, payment, review, activation, or another ordered event; it must not be inferred from the earliest timestamp. | It does not prove consent, scope compliance, or continuing authority. |
| `expiry_or_horizon` | Deadline, review window, block range, job boundary, task completion boundary, relationship horizon, or other temporal limit. | Delegated authority needs temporal boundaries so old consent, old keys, old jobs, old listings, or old familiarity are not treated as current authority. | It does not prove continuity beyond the recorded period. |
| `revocation_path` | How the delegation can be revoked, expired, rotated, narrowed, suspended, or challenged. | Delegated authority must include a path for stopping, narrowing, replacing, or contesting the grant. | It does not prove revocation will be noticed by every counterparty. |
| `accountability_path` | Who is accountable for delegate actions and how failure, misuse, harm, overclaim, or dispute is handled. | Authority without accountability can launder agent, operator, marketplace, or user responsibility. | It does not prove justice, repair, or enforceability. |
| `obligation_refs` | References to Minimum Obligation Object v0 records the delegation creates, modifies, verifies, touches, disputes, or helps fulfill. | Delegated actions affecting obligations need obligation context so authority is not inferred from payment, execution, or receipt surfaces. | It does not prove the obligation exists, was accepted, was fulfilled, or was legitimately changed. |
| `audit_log_refs` | References to event logs, receipts, messages, attestations, verification records, or trust events recording use of the delegation. | Use must be traceable enough to detect scope drift, expired authority, ignored revocation, or obligation misuse. | It does not prove that logged use was authorized, complete, fair, or truthful. |
| `dispute_path` | Where delegator, delegate, affected parties, counterparties, or observers can contest authority, scope, consent, evidence, obligation impact, or interpretation. | Delegation claims can be validly signed yet contested in meaning, consent, order, or legitimacy. | It does not prove the dispute process is fair or final. |
| `privacy_scope` | Public, pairwise, group-limited, private, redacted, or selectively disclosed visibility for the delegation record and related evidence. | Delegation may expose sensitive relationship, identity, marketplace, obligation, or harm context; visibility must be bounded. | It does not prove secrecy is justified or that private context is safe. |
| `status` | Current conceptual state, such as `proposed`, `accepted`, `active`, `used`, `challenged`, `suspended`, `revoked`, `expired`, `rotated`, `misused`, `repaired`, `closed`, or `unknown`. | Observers need to know whether the grant is proposed, current, contested, revoked, expired, repaired, or unresolved. | It does not prove moral settlement, legal status, or scope compliance. |
| `explicit_non_claims` | Explicit statements about what this delegation record does not prove. | Non-claims prevent overclaim by making visible that delegation is bounded and incomplete. | It prevents overclaim, but it does not ensure users will read or honor the limits. |
| `human_interpretation_required` | Whether human review is required before stronger claims about consent, identity, authority, obligation effect, dispute, or repair are displayed or acted on. | Some delegations cannot be safely interpreted by agents or UI state alone, especially when evidence is incomplete, disputed, relational, or high-stakes. | It does not guarantee correct human judgment. |

## Optional fields

Optional fields may help specific contexts without making every delegation record heavy:

- `disclosure_policy`
- `verifier`
- `mediator`
- `related_covenant`
- `related_reputation_context`
- `related_agent_identity`
- `key_rotation_policy`
- `compromise_notice`
- `subdelegation_policy`
- `confidence_level`
- `version`

These fields should remain optional because delegations vary in size, risk, privacy,
reversibility, counterparty familiarity, obligation impact, and evidence needs. A simple
bounded task may need a lightweight delegation record, while a high-risk agent workflow
may need verifier, mediator, audit log, key rotation, compromise notice, subdelegation,
obligation, and disclosure context.

Optional fields must not become hidden mandatory bureaucracy. They should add precision
where needed without implying that a small, low-risk delegation is illegitimate merely
because it omits heavyweight context.

## Time and order semantics

Delegation time must be modeled as ordered context, not a single timestamp. The record
must distinguish at least:

- `created_time`: when the delegation record was represented;
- `effective_time`: when the bounded grant begins, if accepted;
- `expiry_or_horizon`: when review, expiry, task completion, block height, or other
  temporal boundary matters;
- revocation, suspension, rotation, challenge, and use times when available through
  `audit_log_refs` and their `evidence_boundary_refs`.

A signature time, payment time, receipt time, message time, block height, or verification
time must not be treated as delegated authority order by itself. Ordering requires
sequence context, authority source context, consent evidence, revocation context, and
evidence boundaries. If these are missing, the record should say `unknown` or require
human interpretation rather than implying authority.

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names
states that may be useful when discussing delegation, use, challenge, revocation,
misuse, repair, and closure.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `proposed` | A delegation has been described but not accepted. | Proposal means authority has been granted. |
| `accepted` | The delegator and delegate, or their authorized process, accepted the bounded delegation terms. | Acceptance proves full identity, competence, or legal agency. |
| `active` | The delegation is currently within its recorded scope and time horizon. | Active means every action by the delegate is wise, authorized, or legitimate. |
| `used` | The delegate has acted or claimed to act under the delegation. | Use proves the action was within scope. |
| `challenged` | A party or process contests authority, scope, evidence, consent, use, obligation impact, or interpretation. | Challenged means the delegate misused authority. |
| `suspended` | The delegation is temporarily paused or blocked pending review, expiry, repair, or updated evidence. | Suspended means all previous actions were invalid. |
| `revoked` | The grant has been withdrawn under the recorded revocation path or an accepted revocation process. | Revoked means every counterparty has noticed or stopped relying on it. |
| `expired` | The recorded horizon ended without renewal. | Expired means no harm, reliance, memory, or accountability remains. |
| `rotated` | A key, delegate, evidence basis, authority source, or authority path was replaced or updated. | Rotated means continuity is automatically proven. |
| `misused` | The record indicates alleged or accepted action beyond scope, consent, horizon, revocation, obligation, or accountability boundaries. | Misused means justice or repair has occurred. |
| `repaired` | A remedy, correction, restitution, apology, mediation, or other repair path has been recorded as completed or accepted. | Repaired means all harm is gone or memory should be erased. |
| `closed` | The delegation is no longer active under the recorded object. | Closed means morally settled or irrelevant. |

## Runtime surfaces

The delegation record may refer to existing or expected runtime surfaces, but none of
these surfaces proves delegated authority by itself. Each evidence reference should be
paired with evidence boundary metadata when possible.

| Runtime surface | Possible role in delegation record | What it does not prove alone |
| --- | --- | --- |
| `/.well-known/agent.json` | Agent identity surface, endpoint discovery, declared keys, or metadata. | It does not prove the agent is authorized to represent a user, operator, or counterparty. |
| `/.well-known/hodlxxi-operator.json` | Operator identity surface, operator key, or operator-agent relationship evidence. | It does not prove approval of every agent action or blanket legitimacy. |
| `/agent/capabilities` | Declared tasks, tools, or abilities the agent says it can perform. | It does not prove authority to perform those tasks for anyone. |
| `/agent/request` | Request content, requester key, proposed task, payment context, or initial delegation context. | It does not prove accepted delegation or continuing authority. |
| `/agent/message` | Signed or structured agent communication. | It does not prove delegated authority, user approval, or permission by itself. |
| Signed receipt | Event proof linked to a request, job, message, or delegation use. | It does not prove the event was authorized. |
| `/agent/verify/<job_id>` | Verification surface for a bounded job, receipt, or claim. | It does not prove the job was within delegated scope. |
| Human Proof | Evidence relevant to human presence or identity context. | It does not prove full identity, consent, or authority. |
| Operator public key | Cryptographic anchor for operator statements or signatures. | It does not prove every agent action is operator-approved or legitimate. |
| Agent public key | Cryptographic anchor for agent statements or signatures. | It does not prove the agent may represent another actor. |
| Requester public key | Cryptographic anchor for requester statements or signatures. | It does not prove full human identity, informed consent, or broad delegation. |
| `/agent/attestations` | Statements by an actor, agent, verifier, operator, or other surface. | It does not prove truth, legitimacy, settled authority, or delegated permission. |
| `/agent/trust/events` | Event memory that may support chronology, continuity, use, challenge, revocation, or obligation review. | It does not prove fairness, complete context, or justice. |
| Marketplace listing | Offer, capability, operator, reputation, or service context. | It does not prove authority to act for a specific user. |
| Marketplace interaction | Trade context, paid job, counterparty relation, consent evidence, or repeated interaction. | It does not prove delegated authority beyond the recorded interaction. |
| Minimum Obligation Object v0 | Related promise, acceptance criteria, breach condition, remedy, or accountability context. | It does not prove an agent had authority to create or modify the obligation. |
| Evidence Boundary Metadata v0 | Boundary context for signatures, receipts, attestations, logs, messages, payments, Human Proof, and marketplace evidence. | It does not prove truth, consent, legitimacy, identity, or authority by itself. |
| Future delegation endpoint | Publication, lookup, verification, update, or selective disclosure of delegation records. | It would not prove truth, competence, legitimacy, or full consent by itself. |
| Future revocation endpoint | Revocation, suspension, expiry, rotation, or challenge publication. | It would not prove every counterparty received or honored the update. |

## Example mappings

These examples show how the record should bound common HODLXXI-adjacent interactions.
They are not runtime schema examples.

| Scenario | Minimum delegation fields to expose | Evidence and obligation boundary requirement | Unsafe claim to avoid |
| --- | --- | --- | --- |
| Operator delegates bounded runtime action to agent | `delegator`, `delegate`, `delegator_role`, `delegate_role`, `scope`, `allowed_actions`, `prohibited_actions`, `authority_source`, `created_time`, `effective_time`, `expiry_or_horizon`, `revocation_path`, `accountability_path`, `status`, `explicit_non_claims`. | Operator statement, operator key, agent key, policy, and audit logs should link through `consent_evidence_refs`, `audit_log_refs`, and `evidence_boundary_refs`. Use `obligation_refs` if the runtime action affects obligations. | Operator key means every agent action is legitimate. |
| User delegates a paid 21-sat task to agent | `delegator`, `delegate`, roles, `scope`, `allowed_actions`, `prohibited_actions`, `authority_source`, `consent_evidence_refs`, `created_time`, `effective_time`, `expiry_or_horizon`, `revocation_path`, `accountability_path`, `privacy_scope`, `status`, `explicit_non_claims`. | Payment, invoice, request, acceptance, receipt, and verification evidence should carry evidence boundary metadata. If the task creates a promise, acceptance criteria, breach condition, or remedy expectation, link `obligation_refs` to Minimum Obligation Object v0. | Payment means broad delegation, obligation fulfillment, or satisfaction. |
| Agent posts or signs a message | `delegate`, `delegate_role`, `scope`, `allowed_actions`, `prohibited_actions`, `authority_source`, `consent_evidence_refs`, `evidence_boundary_refs`, `audit_log_refs`, `status`, `explicit_non_claims`. | The signature is evidence of a key-controlled message only. It needs evidence boundary metadata and, if it claims to speak for a user/operator, a matching active delegation record. | Agent signature means user consent or delegated permission. |
| Agent touches an obligation object | `delegator`, `delegate`, roles, `scope`, `allowed_actions`, `prohibited_actions`, `authority_source`, `obligation_refs`, `accountability_path`, `dispute_path`, `audit_log_refs`, `human_interpretation_required`. | The affected obligation must be referenced through `obligation_refs`; evidence of the agent's action and authority must link through `evidence_boundary_refs`. Human interpretation should be required when authority, acceptance, breach, remedy, or repair meaning is contested. | Agent action on an obligation means the agent had authority or the obligation is settled. |
| Agent marketplace listing or capability declaration | `delegate`, `delegate_role`, `scope`, `allowed_actions`, `prohibited_actions`, `authority_source`, `evidence_boundary_refs`, `privacy_scope`, `status`, `explicit_non_claims`. | Listing evidence, capability declarations, operator statements, and reputation context should carry evidence boundary metadata. Add `consent_evidence_refs` only for actual delegation grants, not for mere capability publication. | Marketplace listing or capability declaration means authority to act for a specific user. |

## What it can prove

A well-formed delegation record can prove or support only bounded claims:

- that a delegation was represented;
- that delegator and delegate were declared;
- that delegator and delegate roles were stated;
- that scope, allowed actions, and prohibited actions were recorded;
- that an authority source was declared;
- that consent evidence references and evidence boundary references were attached;
- that created, effective, and expiry or horizon fields were distinguished rather than
  collapsed into one timestamp;
- that revocation, accountability, dispute, privacy, audit, and obligation paths were
  declared when relevant;
- that status and explicit non-claims were visible;
- that human interpretation was required or not required according to the record.

It still does not prove truth, competence, legitimacy, satisfaction, justice, full
identity, valid consent, obligation fulfillment, or moral settlement by itself.

## What it must not prove

The existence or state of a delegation record must not be used for these overclaims:

- delegation record exists -> delegate is trustworthy;
- capability exists -> delegation exists;
- key controlled -> identity or representation proven;
- signed message exists -> delegated permission exists;
- user paid -> user delegated broad authority;
- agent signed -> user approved;
- operator key exists -> all actions are authorized;
- agent fluency -> legitimate authority;
- delegation active -> every action within scope is wise;
- delegation used -> use was within scope;
- delegation revoked -> every counterparty knows;
- delegation expired -> no harm remains;
- delegate is useful -> delegate is legitimate;
- subdelegation happened -> authority is valid;
- obligation object referenced -> agent had authority over the obligation.

## Failure modes

- capability treated as authority;
- key control treated as identity;
- agent signature treated as user consent;
- signed message treated as delegated permission;
- expired delegation still used;
- revoked delegation ignored;
- delegation scope too broad;
- overbroad allowed actions;
- missing prohibited actions;
- agent creates obligations without authority;
- agent modifies, verifies, closes, or disputes obligations without authority;
- operator key used as blanket legitimacy;
- hidden delegator;
- missing accountability path;
- missing or unusable revocation path;
- missing dispute path;
- missing evidence boundary metadata;
- forged consent basis;
- revocation not propagated;
- agent acts beyond scope;
- operator and agent responsibility blur;
- subdelegation abuse;
- delegation laundering;
- coercive delegation;
- private context leaked publicly;
- counterparty cannot verify authority;
- powerful or fluent agent becomes charismatic authority.

## Falsification tests

- Do users overtrust agent capabilities when delegation records are absent?
- Do users make better decisions when delegation scope, allowed actions, prohibited
  actions, and expiry are visible?
- Do users still confuse key control with identity when delegator and delegate roles are
  shown?
- Do users still treat signed agent messages as user consent when explicit non-claims are
  shown?
- Do agents act beyond scope in simulated workflows?
- Do counterparties detect revoked or expired delegation?
- Do obligation records prevent agents from creating or modifying obligations without
  visible authority?
- Does evidence boundary metadata reduce overclaim from signatures, receipts, payments,
  attestations, and marketplace listings?
- Does delegation become too heavy for simple tasks?
- Do users confuse agent usefulness or fluency with authority even when non-claims are
  shown?
- Do repair/dispute paths reduce harm after misuse?

## Open questions

- What is the minimum useful delegation record?
- Which fields must be machine-readable?
- Which fields should remain human-readable?
- Which fields should be private or selectively disclosed?
- Should every agent action require a delegation reference?
- Which actions should never be delegated?
- Should subdelegation be forbidden by default?
- How should delegation interact with obligation objects?
- How should delegation interact with reputation?
- How should revocation propagate to counterparties?
- How should an agent prove it is acting within scope without exposing private context?
- When should `human_interpretation_required` block an agent from acting?
