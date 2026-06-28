# Minimum Delegation Record v0

## Purpose

This document defines the minimum conceptual record required to represent delegated
authority in HODLXXI.

Delegation is not capability. Delegation is not key control. Delegation is not mere user
familiarity. Delegation is not agent usefulness. Delegation is not payment. Delegation
is not a signed message by itself.

Delegation requires a bounded grant from a delegator to a delegate, within a scope,
duration, permitted action set, evidence basis, revocation path, and accountability
path.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract,
legal agency framework, or implementation claim.

## Problem

HODLXXI has agent identity surfaces, operator keys, capabilities, paid jobs, receipts,
Human Proof, inter-agent messages, marketplace interactions, and future agent workflows.

These surfaces are useful, but users may infer stronger claims than the system
preserved:

- capability declared -> authority granted;
- agent signed -> user approved;
- operator key exists -> every action authorized;
- paid job accepted -> agent may act broadly;
- agent remembers me -> agent represents me;
- fluent answer -> legitimate representative;
- inter-agent message -> delegated authority.

The delegation record exists to prevent those false inference chains. It makes the
missing grant, scope, duration, evidence, revocation, and accountability structure
visible before HODLXXI presents stronger claims about delegated authority.

## Non-goals

This document does not:

- create an unrestricted autonomy model;
- give agents broad legal agency;
- define enforceable law;
- replace human judgment;
- prove moral legitimacy;
- prove user satisfaction;
- require all delegation details to be public;
- implement runtime code;
- authorize any current runtime action.

## Required fields

A minimum delegation record needs the following fields before HODLXXI can honestly
represent delegated authority.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `delegation_id` | A stable identifier for this delegation record. | Without a stable identifier, later evidence, use, challenge, revocation, rotation, or repair records cannot refer to the same bounded grant. | It does not prove the delegation is valid or legitimate. |
| `delegator` | The actor granting authority. | Delegation requires a declared source of authority rather than a free-floating capability, signature, payment, or agent assertion. | It does not prove full human identity unless linked evidence supports it. |
| `delegate` | The actor or agent receiving bounded authority. | The record must identify who is allowed to act under the grant so authority is not transferred to any fluent or capable actor by implication. | It does not prove capability, competence, or trustworthiness. |
| `scope` | The context in which the delegation applies. | Scope prevents a narrow grant from being read as general representation, broad consent, or continuing agency. | It does not imply authority outside that context. |
| `permitted_actions` | Actions the delegate may perform. | The record must distinguish authorized actions from possible actions, useful actions, paid actions, or technically available actions. | It does not prove the delegate should perform them in every situation. |
| `prohibited_actions` | Actions explicitly outside the grant. | Explicit exclusions reduce ambiguity, especially where a delegate has capability, memory, keys, market access, or persuasive fluency. | It does not prove all other actions are safe. |
| `duration` | Start, expiry, review, or time horizon. | Delegated authority needs temporal boundaries so old consent, old keys, old jobs, or old familiarity are not treated as current authority. | It does not prove continuity beyond the recorded period. |
| `evidence_links` | Proofs, signatures, receipts, attestations, Human Proof, operator records, messages, or obligation references. | Evidence must be attached explicitly so observers can see what the delegation claim depends on. | It does not transform evidence into truth. |
| `consent_basis` | How the delegation was accepted or authorized. | A delegation record needs a declared basis for consent so authority is not inferred from payment, capability, memory, or signed agent output alone. | It does not prove informed consent in every human sense. |
| `revocation_path` | How the delegation can be revoked, expired, rotated, or suspended. | Delegated authority must include a path for stopping, narrowing, replacing, or challenging the grant. | It does not prove revocation will be noticed by every counterparty. |
| `accountability_path` | Who is accountable for delegate actions and how failure, misuse, or dispute is handled. | Authority without accountability can launder agent, operator, marketplace, or user responsibility. | It does not prove justice or repair. |
| `non_claims` | Explicit statements about what this delegation record does not prove. | Non-claims prevent overclaim by making visible that delegation is bounded and incomplete. | It prevents overclaim, but it does not ensure users will read or honor the limits. |

## Optional fields

Optional fields may help specific contexts without making every delegation record heavy:

- `privacy_scope`
- `disclosure_policy`
- `verifier`
- `mediator`
- `related_obligation`
- `related_covenant`
- `related_reputation_context`
- `related_agent_identity`
- `key_rotation_policy`
- `compromise_notice`
- `subdelegation_policy`
- `audit_log_reference`
- `version`

These fields should remain optional because delegations vary in size, risk, privacy,
reversibility, counterparty familiarity, and evidence needs. A simple bounded task may
need a lightweight delegation record, while a high-risk agent workflow may need
verifier, mediator, audit log, key rotation, compromise notice, subdelegation,
obligation, and disclosure context.

Optional fields must not become hidden mandatory bureaucracy. They should add precision
where needed without implying that a small, low-risk delegation is illegitimate merely
because it omits heavyweight context.

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names
states that may be useful when discussing delegation, use, challenge, revocation,
misuse, repair, and closure.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `proposed` | A delegation has been described but not accepted. | Proposal means authority has been granted. |
| `accepted` | The delegator and delegate, or their authorized process, accepted the bounded delegation terms. | Acceptance proves full identity, competence, or legal agency. |
| `active` | The delegation is currently within its recorded scope and duration. | Active means every action by the delegate is wise, authorized, or legitimate. |
| `used` | The delegate has acted or claimed to act under the delegation. | Use proves the action was within scope. |
| `challenged` | A party or process contests authority, scope, evidence, consent, use, or interpretation. | Challenged means the delegate misused authority. |
| `suspended` | The delegation is temporarily paused or blocked pending review, expiry, repair, or updated evidence. | Suspended means all previous actions were invalid. |
| `revoked` | The grant has been withdrawn under the recorded revocation path or an accepted revocation process. | Revoked means every counterparty has noticed or stopped relying on it. |
| `expired` | The recorded duration ended without renewal. | Expired means no harm, reliance, memory, or accountability remains. |
| `rotated` | A key, delegate, evidence basis, or authority path was replaced or updated. | Rotated means continuity is automatically proven. |
| `misused` | The record indicates alleged or accepted action beyond scope, consent, duration, or accountability boundaries. | Misused means justice or repair has occurred. |
| `repaired` | A remedy, correction, restitution, apology, mediation, or other repair path has been recorded as completed or accepted. | Repaired means all harm is gone or memory should be erased. |
| `closed` | The delegation is no longer active under the recorded object. | Closed means morally settled or irrelevant. |

## Runtime surfaces

The delegation record may refer to existing or expected runtime surfaces, but none of
these surfaces proves delegated authority by itself.

| Runtime surface | Possible role in delegation record | What it does not prove alone |
| --- | --- | --- |
| `/.well-known/agent.json` | Agent identity surface, endpoint discovery, declared keys, or metadata. | It does not prove the agent is authorized to represent a user, operator, or counterparty. |
| `/.well-known/hodlxxi-operator.json` | Operator identity surface, operator key, or operator-agent relationship evidence. | It does not prove approval of every agent action. |
| `/agent/capabilities` | Declared tasks, tools, or abilities the agent says it can perform. | It does not prove authority to perform those tasks for anyone. |
| `/agent/request` | Request content, requester key, proposed task, or initial delegation context. | It does not prove accepted delegation or continuing authority. |
| `/agent/message` | Signed or structured agent communication. | It does not prove delegated authority or user approval. |
| Signed receipt | Event proof linked to a request, job, message, or delegation use. | It does not prove the event was authorized. |
| `/agent/verify/<job_id>` | Verification surface for a bounded job, receipt, or claim. | It does not prove the job was within delegated scope. |
| Human Proof | Evidence relevant to human presence or identity context. | It does not prove full identity, consent, or authority. |
| Operator public key | Cryptographic anchor for operator statements or signatures. | It does not prove every agent action is operator-approved. |
| Agent public key | Cryptographic anchor for agent statements or signatures. | It does not prove the agent may represent another actor. |
| Requester public key | Cryptographic anchor for requester statements or signatures. | It does not prove full human identity, informed consent, or broad delegation. |
| `/agent/attestations` | Statements by an actor, agent, verifier, operator, or other surface. | It does not prove truth, legitimacy, or settled authority. |
| `/agent/trust/events` | Event memory that may support chronology, continuity, use, challenge, or revocation review. | It does not prove fairness, complete context, or justice. |
| Marketplace listing | Offer, capability, operator, reputation, or service context. | It does not prove authority to act for a specific user. |
| Marketplace interaction | Trade context, paid job, counterparty relation, or repeated interaction. | It does not prove delegated authority beyond the recorded interaction. |
| Minimum Obligation Object v0 | Related promise, acceptance criteria, breach condition, remedy, or accountability context. | It does not prove an agent had authority to create or modify the obligation. |
| Future delegation endpoint | Publication, lookup, verification, update, or selective disclosure of delegation records. | It would not prove truth, competence, legitimacy, or full consent by itself. |
| Future revocation endpoint | Revocation, suspension, expiry, rotation, or challenge publication. | It would not prove every counterparty received or honored the update. |

## What it can prove

A well-formed delegation record can prove or support only bounded claims:

- that a delegation was represented;
- that delegator and delegate were declared;
- that scope and duration were stated;
- that permitted and prohibited actions were recorded;
- that evidence links were attached;
- that revocation and accountability paths were declared;
- that non-claims were visible.

It still does not prove truth, competence, legitimacy, satisfaction, justice, or full
identity by itself.

## What it must not prove

The existence or state of a delegation record must not be used for these overclaims:

- delegation record exists -> delegate is trustworthy;
- capability exists -> delegation exists;
- user paid -> user delegated authority;
- agent signed -> user approved;
- operator key exists -> all actions are authorized;
- delegation active -> every action within scope is wise;
- delegation revoked -> every counterparty knows;
- delegation expired -> no harm remains;
- delegate is useful -> delegate is legitimate;
- subdelegation happened -> authority is valid.

## Failure modes

- fake delegation record;
- vague scope;
- overbroad permitted actions;
- missing prohibited actions;
- hidden delegator;
- forged consent basis;
- revocation not propagated;
- expired authority still trusted;
- agent acts beyond scope;
- operator and agent responsibility blur;
- subdelegation abuse;
- delegation laundering;
- coercive delegation;
- private context leaked publicly;
- counterparty cannot verify authority;
- agent-created obligation without authority;
- powerful agent becomes charismatic authority.

## Falsification tests

- Do users overtrust agent capabilities when delegation records are absent?
- Do users make better decisions when delegation scope and expiry are visible?
- Do agents act beyond scope in simulated workflows?
- Do counterparties detect revoked or expired delegation?
- Does delegation become too heavy for simple tasks?
- Do users confuse agent usefulness with authority even when non-claims are shown?
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
