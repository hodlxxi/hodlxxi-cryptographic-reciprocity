# Identity Continuity v0

## Purpose

This document defines the minimum conceptual structure needed to represent identity continuity in HODLXXI.

Identity is not key control.
Identity is not a login.
Identity is not an endpoint.
Identity is not a single signature.
Identity is not a public profile.
Identity is not reputation.
Identity is not delegation.
Identity is not legal name by default.
Identity continuity is not automatic persistence of a key.

Identity continuity requires an anchor, role context, key purpose, rotation path, revocation path, recovery path, continuity evidence, compromise handling, privacy boundary, and explicit non-claims.

This is a Canon-level mechanism specification. It is not a runtime schema, API contract, legal identity system, personhood proof, authority model, reputation model, or implementation claim.

## Problem

HODLXXI has agent keys, operator keys, requester keys, Human Proof, signed receipts, discovery endpoints, attestations, reputation memory, obligations, delegation records, repair records, reciprocity patterns, and covenant participant keys.

These surfaces can preserve evidence, but they do not by themselves preserve identity continuity. Users may infer false claims:

- key signed -> identity known;
- same key -> same meaningful actor forever;
- endpoint reachable -> legitimate identity;
- profile exists -> person is real;
- Human Proof -> full identity known;
- reputation history -> identity continuity;
- operator key exists -> all agent actions are operator identity;
- agent key signs -> agent has stable identity;
- key rotation -> continuity preserved automatically;
- key compromise notice -> harm resolved.

The identity continuity record exists to prevent those false inference chains. It makes visible the difference between anchor control, role context, key purpose, continuity evidence, rotation, revocation, recovery, compromise, privacy, and non-claims over time.

## Non-goals

This document does not:

- create a legal identity system;
- require doxxing;
- require real-name identity;
- prove personhood;
- prove moral character;
- prove legal accountability;
- prove authority;
- prove reputation;
- solve sybil resistance by itself;
- erase the need for human judgment;
- implement runtime code.

## Required fields

A minimum identity continuity record needs the following fields before HODLXXI can honestly represent identity continuity across time rather than reducing identity to key control, login, signature, endpoint ownership, or single-session proof.

| Field | Description | Why it is required | What it does not prove |
| --- | --- | --- | --- |
| `identity_id` | Stable identifier for this continuity record. | Without a stable identifier, anchors, rotations, revocations, recovery events, obligations, delegations, reputation context, and repairs cannot refer to the same continuity record over time. | It does not prove identity is true or legitimate. |
| `subject` | Human, agent, operator, organization, family member, service, marketplace actor, or unknown/pseudonymous actor. | Observers need to know what kind of subject is being represented before interpreting keys, claims, roles, and evidence. | It does not prove full human identity. |
| `identity_anchor` | Public key, endpoint, DID-like identifier, Nostr key, Bitcoin key, domain, covenant participant key, Human Proof, or other anchor. | Continuity needs at least one declared anchor so evidence can be associated with a subject representation. | It does not prove identity by itself. |
| `key_purpose` | Authentication, signing receipts, operator declaration, agent identity, requester proof, covenant participation, delegation, messaging, marketplace listing, or other purpose. | Key control is only meaningful in relation to purpose; a key used for one purpose must not silently authorize or identify across every other purpose. | It does not prove authority outside that purpose. |
| `role_context` | Operator, agent, requester, performer, verifier, beneficiary, mediator, covenant participant, marketplace actor, family member, or unknown. | Identity claims are interpreted through roles; the same anchor may carry different meaning as operator, agent, requester, verifier, or family member. | It does not prove role legitimacy. |
| `continuity_evidence` | Events, signatures, attestations, receipts, rotations, revocations, reputation context, obligations, delegation records, repair records, reciprocity patterns, or covenant references. | Continuity across time requires evidence beyond a single signature or endpoint snapshot. | It does not transform continuity evidence into truth. |
| `rotation_path` | How keys or anchors can be replaced while preserving continuity. | Long-running identity needs a way to survive key replacement without pretending the old key remains permanent identity. | It does not prove a rotation is valid unless evidence supports it. |
| `revocation_path` | How compromised, obsolete, fraudulent, or expired anchors are revoked. | Observers need to know how an anchor can stop being trusted or associated with a continuity claim. | It does not prove every counterparty noticed. |
| `recovery_path` | How continuity may be restored after loss, compromise, death, incapacity, service failure, or agent failure. | Continuity needs a bounded way to represent recovery without treating recovery as automatic or unquestionably legitimate. | It does not prove recovery is legitimate. |
| `compromise_notice` | How suspected or confirmed compromise is represented. | Compromise must be visible as a state or notice rather than hidden behind continued signatures or reputation history. | It does not prove harm is repaired. |
| `privacy_boundary` | What parts of identity continuity are public, private, sealed, selectively disclosed, or pseudonymous. | Identity continuity can be useful without forcing all identity context into public disclosure. | It does not prove hidden context is irrelevant. |
| `linked_records` | Related obligations, delegations, repairs, reciprocity patterns, reputation context, receipts, attestations, Human Proof, covenants, or marketplace records. | Identity continuity often depends on adjacent records, but those links need to be explicit and inspectable. | It does not prove those records are correctly interpreted. |
| `current_state` | Current conceptual state, such as `active`, `rotated`, `revoked`, `compromised`, `recovered`, `disputed`, `dormant`, `deceased`, `retired`, or `unknown`. | Observers need to distinguish active, changed, damaged, disputed, inactive, ended, and uncertain continuity claims. | It does not prove moral or legal conclusion. |
| `non_claims` | Explicit statements about what this identity continuity record does not prove. | Non-claims prevent anchors, signatures, Human Proof, reputation memory, rotation, recovery, or role labels from laundering stronger identity claims. | It prevents overclaim, but it does not ensure users will read or honor the limits. |

## Optional fields

Optional fields may add precision in contexts where identity continuity is high-stakes, privacy-sensitive, mediated, familial, agentic, inherited, contested, or jurisdiction-sensitive:

- `disclosure_policy`
- `verifier`
- `mediator`
- `witness`
- `guardian`
- `inheritance_context`
- `death_or_incapacity_note`
- `agent_shutdown_policy`
- `operator_agent_relation`
- `sybil_risk`
- `impersonation_risk`
- `jurisdiction_note`
- `version`

These fields should remain optional because identity continuity varies by subject, role, risk, privacy boundary, culture, jurisdiction, relationship, and evidentiary need. A simple pseudonymous marketplace actor should not be forced into the same disclosure structure as a family covenant participant, mediated recovery process, legal organization, or long-running operator-agent relationship.

Optional fields must not become hidden mandatory doxxing. They should add context where needed without implying that an omitted verifier, witness, guardian, jurisdiction note, or inheritance context makes a low-stakes or pseudonymous identity continuity record invalid.

## State model

The following lifecycle is a conceptual model, not a runtime state machine. It names states that may be useful when discussing identity continuity across anchors, keys, roles, rotations, revocations, recovery, compromise, privacy, and evidence.

| State | Meaning | Unsafe inference to avoid |
| --- | --- | --- |
| `created` | A continuity record has been represented, but its history, evidence, and use may be minimal. | Created means identity is true or legitimate. |
| `active` | The record is currently represented as usable for its stated subject, anchors, purposes, and role contexts. | Active means trustworthy, authorized, or legally accountable. |
| `rotated` | One or more anchors or keys have been replaced under a declared rotation path. | Rotated means continuity was preserved automatically. |
| `revoked` | One or more anchors or keys have been marked obsolete, fraudulent, expired, or no longer valid for the declared purpose. | Revoked means all harm, reliance, or ambiguity is resolved. |
| `compromised` | Suspected or confirmed compromise has been represented. | Compromised means every affected party knows what happened. |
| `recovery_pending` | Recovery has been requested, proposed, or initiated but is not yet represented as complete. | Pending recovery means recovery will be legitimate or successful. |
| `recovered` | Continuity has been represented as restored after loss, compromise, death, incapacity, service failure, or agent failure. | Recovered means the recovery was legitimate or uncontested. |
| `disputed` | Parties, observers, or evidence contest the subject, anchor, role, continuity, rotation, revocation, recovery, or interpretation. | Disputed means one side is lying or guilty. |
| `suspended` | Use of the record or an anchor is paused while compromise, dispute, recovery, or review is unresolved. | Suspended means identity is false. |
| `dormant` | The record is inactive but not necessarily revoked, retired, deceased, or false. | Dormant means abandoned, safe, or resolved. |
| `retired` | The record is intentionally ended or no longer used for active continuity. | Retired means no memory, obligation, harm, or accountability remains. |
| `deceased` | The subject is represented as deceased, where that state is relevant and appropriate to disclose. | Deceased means every legal, familial, inheritance, or agent-shutdown issue is settled. |
| `unknown` | Available evidence is insufficient to assign a more specific state. | Unknown means safe, unsafe, legitimate, illegitimate, human, or non-human. |

## Runtime surfaces

The identity continuity record may refer to existing or expected runtime surfaces, but none of these surfaces proves identity continuity by itself.

| Runtime surface | Possible role in identity continuity | What it does not prove alone |
| --- | --- | --- |
| `/.well-known/agent.json` | Discovery context for an agent endpoint, declared keys, capabilities, or identity-related metadata. | It does not prove the endpoint is legitimate identity or that the agent has person-like continuity. |
| `/.well-known/hodlxxi-operator.json` | Discovery context for operator declarations, operator keys, and operator-agent relationships. | It does not prove every agent action belongs to the operator identity. |
| Operator public key | Anchor for operator declarations, receipts, attestations, delegation, or recovery evidence. | It does not prove full identity, authority, or legal accountability. |
| Agent public key | Anchor for agent messages, receipts, attestations, or runtime claims. | It does not prove stable human identity or moral agency. |
| Requester public key | Anchor for requester authentication, signed requests, receipts, or payment-adjacent events. | It does not prove personhood, legitimacy, or continuing identity. |
| Human Proof | Evidence that may contribute human-presence or identity-context signals. | It does not prove full identity, legal name, authority, or moral character. |
| Signed receipt | Event proof connected to a subject, key, action, request, delivery, payment, or verification. | It does not prove identity beyond bounded signature and event context. |
| `/agent/verify/<job_id>` | Verification output for a job or evidence item linked to a subject or anchor. | It does not prove the subject's full identity or continuity. |
| `/agent/attestations` | Statements by parties, agents, verifiers, mediators, witnesses, or observers. | It does not prove truth, legitimacy, consent, or stable identity. |
| `/agent/reputation` | Contextual memory that may help interpret repeated behavior under an identity continuity record. | It does not prove identity continuity or reduce identity to reputation. |
| `/agent/trust/events` | Chronological memory for events, disputes, repairs, rotations, revocations, attestations, and state changes. | It does not prove complete context or moral meaning. |
| Minimum Delegation Record v0 | Linked scope, duration, permitted actions, consent evidence, revocation, and accountability for delegated authority. | It does not prove identity, legitimacy, or authority outside the delegation. |
| Minimum Obligation Object v0 | Linked promises, acceptance criteria, breach conditions, remedy paths, and closure states. | It does not prove identity continuity or obligation fulfillment by itself. |
| Repair Lifecycle v0 | Linked failure, acknowledgement, remedy, affected response, forgiveness, memory, and re-entry context. | It does not prove trust was restored or identity continuity is uncontested. |
| Reciprocity Pattern v0 | Linked repeated interaction, counterparties, expectation, asymmetry, repair, and evidence across time. | It does not prove identity, loyalty, or future cooperation. |
| Covenant participant key | Anchor for participation in covenant-adjacent commitments, constraints, or references. | It does not prove kinship, affection, full identity, or legitimacy. |
| Marketplace listing | Public or semi-public offer context that may include an actor, service, anchor, or reputation context. | It does not prove the actor is real, trustworthy, or continuous. |
| Inter-agent message | Message evidence between agents, operators, requesters, or services. | It does not prove authority, consent, personhood, or identity continuity. |
| Future identity continuity endpoint | Possible publication or query surface for identity continuity records. | It would not prove full identity, personhood, or legitimacy by itself. |
| Future key rotation endpoint | Possible surface for representing rotation evidence and successor anchors. | It would not prove rotation validity without supporting evidence and context. |
| Future revocation endpoint | Possible surface for representing revoked, expired, fraudulent, or compromised anchors. | It would not prove every counterparty noticed or that harm was repaired. |

## What it can prove

A well-formed identity continuity record can prove or support only bounded claims:

- that an identity continuity record was represented;
- that a subject and anchor were declared;
- that key purpose and role context were stated;
- that continuity evidence was attached;
- that rotation, revocation, recovery, and compromise paths were declared;
- that privacy boundaries and linked records were visible;
- that non-claims were visible.

It still does not prove full identity, personhood, legal identity, moral character, authority, reputation, legitimacy, or trustworthiness by itself.

## What it must not prove

The existence or state of an identity continuity record must not be used for these overclaims:

- identity record exists -> person is real;
- key signed -> identity known;
- same key -> same meaningful actor forever;
- Human Proof exists -> full identity known;
- profile exists -> legitimacy;
- reputation exists -> identity continuity;
- key rotated -> continuity preserved;
- key revoked -> harm repaired;
- recovery path used -> recovery legitimate;
- agent key exists -> stable person-like identity;
- operator key exists -> every action belongs to operator identity.

## Failure modes

- key loss;
- key compromise;
- stolen identity anchor;
- fake continuity record;
- sybil identity;
- impersonation;
- reputation laundering through rotation;
- blame laundering through key revocation;
- operator-agent identity confusion;
- agent identity theater;
- endpoint hijack;
- domain loss;
- privacy leakage;
- forced doxxing;
- dead actor still treated as active;
- compromised key still trusted;
- recovery captured by attacker;
- continuity claim used to erase past misconduct;
- identity reduced to legal name;
- identity reduced to score.

## Falsification tests

- Do users overread key signatures as identity?
- Do users make better decisions when key purpose and role context are visible?
- Do users still treat Human Proof as full identity?
- Do users detect compromised or revoked anchors?
- Can attackers launder reputation through rotation?
- Can agents simulate stable identity through repeated signing?
- Does selective disclosure preserve privacy without destroying useful continuity?
- Does identity continuity become too heavy for simple pseudonymous use?
- Do users confuse operator identity with agent action?

## Open questions

- What is the minimum useful identity continuity record?
- Which fields must be machine-readable?
- Which fields should remain human-readable?
- Which fields should be private or selectively disclosed?
- How should pseudonymous identity be preserved without doxxing?
- How should death, incapacity, inheritance, or agent shutdown be represented?
- How should identity continuity interact with reputation?
- How should identity continuity interact with delegation?
- How should identity continuity interact with obligations?
- How should identity continuity interact with repair and forgiveness?
- How should key rotation preserve accountability without permanent punishment?
- What identity claims should HODLXXI never make?
