# Canon / Runtime Gap Register

## Purpose

This document tracks the gap between Canon-level concepts and runtime implementation.

Canon mechanisms are conceptual specifications. Runtime surfaces are observable system
behavior. A runtime surface must not claim stronger meaning than it can actually
represent.

This register exists to prevent self-deception, overclaiming, product theater, and
accidental legitimacy laundering.

## Status legend

- **Present:** Runtime appears to expose a surface or behavior directly related to the concept.
- **Partial:** Runtime appears to expose evidence, but not the full mechanism.
- **Missing:** No first-class runtime mechanism is currently represented.
- **Unknown:** Not enough evidence in this repository to classify.
- **Do not claim:** The runtime must not claim this until a stronger mechanism exists.

This register is conservative by default. When evidence is ambiguous, the safer
classification is the one that supports the weaker runtime claim.

## Gap table

| Canon concept / mechanism | Current runtime evidence | Status | Unsafe claim to avoid | Next safe step |
| --- | --- | --- | --- | --- |
| Signed receipt as event proof | Signed receipts, job verification, request/result/payment hashes, agent signatures. | Present / Partial | Receipt proves obligation, satisfaction, repair, or human meaning. | Keep receipt semantics bounded; link receipts to future obligation records only when explicit obligation fields exist. |
| Evidence Boundary Metadata v0 | Evidence surfaces, receipts, attestations, Human Proof, event chains, covenant references, and reputation summaries expose partial evidence but not a shared boundary metadata layer. | Missing as first-class mechanism | Evidence, timestamps, receipts, attestations, lockups, or summaries prove truth, satisfaction, identity, commitment, legitimacy, or trust. | Use the mechanism candidate to expose bounded claim, explicit non-claims, missing context, contradiction, revocation, counter-evidence, dispute, repair, privacy, and retention paths. |
| Minimum Obligation Object v0 | Paid jobs, requests, receipts, invoices, verification endpoint. | Missing as first-class mechanism | Paid job or receipt proves obligation fulfilled. | Define future obligation object schema or doc; keep runtime wording as event proof only. |
| Minimum Delegation Record v0 | Agent identity surfaces, operator key, capabilities, signed messages, requester keys. | Missing as first-class mechanism | Capability, operator key, or agent signature proves delegated authority. | Define read-only delegation record or discovery surface before delegated action claims. |
| Repair Lifecycle v0 | Trust events, attestations, receipts, possibly job status/history. | Missing as first-class mechanism | Refund, apology, closure, or attestation proves repair or forgiveness. | Define repair/dispute lifecycle before reputation restoration or forgiveness claims. |
| Reciprocity Pattern v0 | Repeated events, paid jobs, messages, marketplace interactions, trust events. | Missing as first-class mechanism | Many transactions or repeated interactions prove reciprocity. | Represent event sequences with counterparties, time horizon, expectations, asymmetry, and repair links before reciprocity claims. |
| Identity Continuity v0 | Operator public key, agent public key, requester public keys, Human Proof, discovery endpoints, receipts. | Partial | Key control, endpoint ownership, or Human Proof proves full identity. | Document key purpose, role context, rotation, revocation, compromise, and recovery before continuity claims. |
| Contextual Reputation v0 | Reputation endpoint, trust events, attestations, job/event history. | Partial | Reputation endpoint proves trustworthiness, moral worth, or global score. | Separate domain, role, time horizon, memory inputs, dispute context, repair context, and confidence limits. |
| Runtime Claims Matrix | Existing Canon runtime claims matrix. | Present as documentation | Documentation means runtime enforces all boundaries. | Keep matrix updated after runtime changes. |
| Event chain / trust events | Trust events, event chain, chain health. | Present / Partial | Event chain proves justice, complete context, or external immutability. | Document what the chain preserves and what it does not preserve; avoid justice claims. |
| Human Proof | Human Proof demo / requester key / proof surfaces. | Partial | Human Proof proves full identity, consent, legitimacy, or satisfaction. | Bind Human Proof to specific request context and non-claims. |
| Covenant lockup / covenant references | Covenant-related documents, lockup concepts, operator/covenant references. | Partial / Unknown depending on runtime surface | Locked sats prove human commitment, loyalty, love, legitimacy, or reciprocity. | Treat lockup as constraint evidence only; link to obligation/reciprocity/identity records only when explicit fields exist. |
| Marketplace interactions | Marketplace concepts or prototype references if present. | Partial / Unknown | Listing, payment, or interaction proves trust, reputation, obligation, or reciprocity. | Use marketplace events as inputs to obligation, repair, reciprocity, and reputation mechanisms, not as substitutes. |
| Agent capability surfaces | Agent capabilities endpoint, skills, paid job types. | Present | Capability means authority, legitimacy, or delegated permission. | Keep capabilities separate from delegation and obligation records. |
| AI agent identity | Agent key, discovery document, capabilities, receipts. | Partial | Agent key or fluent behavior proves stable person-like identity or legitimate agency. | Link agent identity to identity continuity and delegation records before stronger claims. |

## Conservative runtime rule

When unsure, runtime wording should downgrade claims.

Examples:

- say "event recorded" instead of "obligation fulfilled";
- say "receipt verified" instead of "work accepted";
- say "key controlled" instead of "identity proven";
- say "capability declared" instead of "authority granted";
- say "contextual memory exists" instead of "actor is trustworthy";
- say "lockup observed" instead of "commitment proven";
- say "repair claimed" instead of "relationship restored".

## Runtime wording checklist

Before adding a runtime claim, ask:

- Which Canon mechanism supports this claim?
- Is the mechanism implemented or only described?
- What evidence backs the claim?
- What does the evidence not prove?
- Is the claim contextual or global?
- Does it confuse event proof with human meaning?
- Does it confuse key control with identity?
- Does it confuse capability with authority?
- Does it confuse memory with punishment?
- Does it confuse forgiveness with erasure?
- Does it expose private relationship context unnecessarily?

## Implementation priority

A conservative suggested priority:

1. Keep receipt semantics bounded.
2. Add runtime wording/non-claim guards.
3. Add identity/key-purpose documentation.
4. Add first-class obligation object.
5. Add delegation record only before delegated agent action.
6. Add repair/dispute lifecycle before reputation restoration.
7. Add contextual reputation only after repair/dispute context exists.
8. Add reciprocity patterns only after enough event memory exists.

This is not a product roadmap. It is a risk-reduction order.

## Open questions

- Which gap is most dangerous to leave ambiguous?
- Which runtime claim currently risks overclaim?
- Which mechanism should be implemented first?
- Which mechanism should remain social/human-readable for now?
- Which gaps matter for the 21-sat demo?
- Which gaps matter for marketplace use?
- Which gaps matter for AI-agent delegation?
- Which gaps matter for covenant meaning?
- What should HODLXXI explicitly refuse to display until the mechanism exists?
