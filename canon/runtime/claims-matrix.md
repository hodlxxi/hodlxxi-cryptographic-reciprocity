# Runtime Claims Matrix

## Purpose

This document prevents runtime endpoints, receipts, keys, payments, reputation
telemetry, attestations, event chains, marketplace surfaces, and lockups from being read
as stronger claims than they can support.

Runtime surfaces can preserve bounded evidence. They do not automatically preserve human
meaning, satisfaction, legitimacy, consent, obligation, identity, trust, forgiveness, or
reciprocity.

Core rule:

Runtime surfaces should expose what they prove, what they do not prove, and what
mechanism would be required for stronger claims. Stable Canon claim IDs are listed in the
[CRT Canon Claim Registry](../CLAIMS.md).

## Claim levels

1. **Evidence claim** — Retained information that can support, weaken, or revise interpretation. It must not be confused with truth, justice, legitimacy, satisfaction, or final judgment.
2. **Event claim** — Evidence that a bounded event occurred, was observed, or was recorded. It must not be confused with obligation fulfillment, human satisfaction, legitimacy, or truth about the surrounding context.
3. **Control claim** — Evidence that a party controlled a key, endpoint, account, or signing capability at a time. It must not be confused with identity, authority, consent, or long-term role continuity.
4. **Payment claim** — Evidence that a payment request existed, or that settlement occurred when settlement evidence is present. It must not be confused with obligation, acceptance of broader terms, satisfaction, or repair.
5. **Execution claim** — Evidence that a runtime attempted or completed a bounded action. It must not be confused with correct interpretation, useful outcome, social acceptance, or fulfilled obligation.
6. **Identity claim** — Evidence that a surface links to an identifier, profile, proof, or continuity record. It must not be confused with full human identity, legitimacy, character, authority, or trustworthiness.
7. **Authority claim** — Evidence that an actor was permitted to do a bounded thing under a bounded delegation. It must not be confused with capability, identity, broad legitimacy, or open-ended agency.
8. **Obligation claim** — Evidence that a defined duty, promise, acceptance criterion, or responsibility exists. It must not be confused with payment, execution, receipt, lockup, or satisfaction.
9. **Reputation claim** — Evidence about remembered behavior, telemetry, attestations, or history. It must not be confused with a universal trust score, moral worth, identity, or truth.
10. **Commitment claim** — Evidence that value, time, conduct, or constraints were bound in a specific way. It must not be confused with loyalty, love, legitimacy, fulfilled obligation, or complete intent.
11. **Reciprocity claim** — Evidence of repeated mutual relation across time, memory, and context. It must not be confused with a transaction count, payment history, marketplace activity, or isolated exchange.
12. **Time claim** — Evidence about timestamp, sequence, block height, recency, horizon, or constraint timing. It must not be confused with meaning, sincerity, obligation, maturity, repair, identity continuity, or commitment by itself.

## Matrix

| Runtime surface | Claim type | What it can prove | What it does not prove | Related Canon boundary | Missing mechanism |
| --- | --- | --- | --- | --- | --- |
| Evidence surfaces generally | Evidence claim | Retained information can support, weaken, or revise interpretation. | Truth by itself, justice, legitimacy, satisfaction, consent, authority, or final judgment. | Evidence Is Not Truth (`CRT-EVIDENCE-001`) | Evidence boundary metadata; contradiction, revocation, and counter-evidence paths. |
| `/.well-known/agent.json` | Identity claim / control claim | An agent endpoint declares an identifier, key material, and metadata at a reachable location. | Human identity, legitimacy, delegated authority, or reliable long-term continuity. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Identity continuity record; external anchoring; non-claims in discovery response. |
| `/.well-known/hodlxxi-operator.json` | Identity claim / control claim | An operator endpoint declares operator metadata and key material at a reachable location. | Operator legitimacy, governance authority, consent from participants, or trustworthy conduct. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Operator role record; governance context; continuity evidence. |
| `/agent/capabilities` | Execution claim / authority-adjacent claim | The runtime declares supported actions or interfaces. | Delegated authority, legitimacy, safe use, or permission to act for a user. | Bounded Authority for AI Agents (`CRT-AGENT-AUTHORITY-001`) | Delegation record; authority scope; revocation and expiry model. |
| `/agent/request` | Execution claim | A request was submitted to the runtime and may be processed under bounded conditions. | Authority to perform the request, user satisfaction, obligation acceptance, or correct interpretation. | Bounded Authority for AI Agents (`CRT-AGENT-AUTHORITY-001`) | Request authorization record; acceptance criteria; obligation object. |
| Lightning invoice | Payment claim | A payment path was created, and possibly paid if settlement evidence exists. | Obligation, consent to broader terms, satisfaction, repair, or legitimacy. | Obligation Is Not Payment (`CRT-OBLIGATION-001`) | Acceptance criteria; obligation object; settlement evidence binding. |
| paid job status | Payment claim / execution claim | The runtime associated a job with payment status and possibly execution state. | Fulfilled obligation, correct result, satisfaction, consent, or finality of a dispute. | Obligation Is Not Payment (`CRT-OBLIGATION-001`) | Obligation object; completion criteria; dispute and repair record. |
| signed receipt | Event claim / time claim | A bounded runtime event was signed by the agent key and may carry event-time evidence. | Obligation fulfillment, satisfaction, human meaning, identity, sincerity, or justice. | Receipts as Event Proofs (`CRT-RECEIPT-001`); Time Is Not Timestamp (`CRT-TIME-001`) | Obligation object; satisfaction signal; context bundle; ordering semantics. |
| `/agent/verify/<job_id>` | Event claim / execution claim | The runtime can report verification data for a bounded job or receipt. | That the verified event fulfilled a duty, was meaningful, or was accepted by a human. | Receipts as Event Proofs (`CRT-RECEIPT-001`) | Claim boundary metadata; obligation reference; user-facing non-claims. |
| `/agent/reputation` | Reputation claim | The runtime exposes remembered telemetry, counts, history, or other reputation-adjacent evidence. | Trustworthiness, moral character, truth, legitimacy, or a universal score. | Reputation Is Not a Score (`CRT-REPUTATION-001`) | Reputation schema; context labels; uncertainty and non-score presentation. |
| `/agent/attestations` | Evidence claim / reputation claim / event claim | Attestation records were published or made available by a runtime surface. | Truth of the attested claim, completeness of context, legitimacy, final judgment, or identity. | Evidence Is Not Truth (`CRT-EVIDENCE-001`) | Attestation semantics; issuer context; contradiction, counter-attestation, and revocation model. |
| `/agent/chain/health` | Evidence claim / event claim / memory claim / time claim | A local event chain appears internally consistent and can support relative ordering of recorded events. | Durable public memory, truth machine, justice, repair, forgiveness, complete meaning, or external truth. | Evidence Is Not Truth (`CRT-EVIDENCE-001`); Time Is Not Timestamp (`CRT-TIME-001`) | External anchoring; audit trail; ordering semantics; repair and forgiveness mechanism. |
| `/agent/trust/events` | Event claim / reputation claim | Trust-related events were recorded or exposed by the runtime. | That trust exists, that a relationship is fair, or that harm has been repaired. | Memory Before Forgiveness (`CRT-FORGIVENESS-001`) | Trust event schema; social interpretation layer; repair record. |
| requester public key | Control claim | Someone controlled the requester key for a signature or request. | Human identity, role, authority, consent, or legitimacy. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Requester identity layer; consent record; key rotation and recovery model. |
| operator public key | Control claim | Someone controlled the operator key for a signature, declaration, or endpoint. | Operator legitimacy, governance mandate, participant consent, or moral responsibility. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Operator continuity record; governance record; accountability process. |
| agent public key | Control claim | Someone or something controlled the agent key for a signed message, receipt, or event. | Agent identity in the human sense, delegated authority, truth, or correct execution. | Identity Is Not Key Control (`CRT-IDENTITY-001`) | Agent identity continuity; delegation record; revocation and compromise handling. |
| Human Proof | Evidence claim / identity claim / time claim | A requester or participant produced a proof intended to support a bounded human-linked participation claim, with request, payment, execution, and verification times separated where relevant. | Complete identity, full personhood, uniqueness across contexts, legitimacy, moral standing, sincerity, or authority. | Evidence Is Not Truth (`CRT-EVIDENCE-001`); Time Is Not Timestamp (`CRT-TIME-001`) | Human identity model; Human Proof time semantics; privacy-preserving continuity; abuse, recovery, and non-personhood rules. |
| covenant lockup | Commitment claim / time claim | Value is constrained by script, time, block height, or spending conditions. | Love, loyalty, legitimacy, fulfilled obligation, full commitment, sincere intent, or human meaning. | Commitment Is Not Lockup (`CRT-COMMITMENT-001`); Time Is Not Timestamp (`CRT-TIME-001`) | Covenant purpose; horizon context; context record; explicit non-claims; release and dispute semantics. |
| covenant participant key | Control claim / commitment-adjacent claim | A participant key is referenced by a covenant-related surface or constraint. | Participant identity, loyalty, consent to all meanings, or fulfilled commitment. | Commitment Is Not Lockup (`CRT-COMMITMENT-001`) | Participant role record; consent record; key rotation and recovery model. |
| inter-agent message | Event claim / authority-adjacent claim | An agent key signed or transmitted a bounded message. | Authority, acceptance, obligation, truth, or human consent. | Bounded Authority for AI Agents (`CRT-AGENT-AUTHORITY-001`) | Delegation record; message intent schema; acceptance and rejection semantics. |
| marketplace listing | Identity claim / reputation-adjacent claim | An actor, service, or agent is discoverable with declared metadata. | Legitimacy, trustworthiness, quality, authority, or obligation to transact. | Reputation Is Not a Score (`CRT-REPUTATION-001`) | Listing verification policy; reputation context; dispute history schema. |
| marketplace interaction | Event claim / reciprocity-adjacent claim | A bounded interaction, request, payment, or exchange occurred in the marketplace. | Reciprocity, trust, satisfaction, obligation fulfillment, or durable relationship. | Reciprocity Is Not Transaction (`CRT-RECIPROCITY-001`) | Relationship memory; obligation object; reciprocity context and repair history. |

## Prohibited inferences

The following inference chains are forbidden or unsafe unless an explicit mechanism
supports the stronger claim:

- paid -> obligation fulfilled
- receipt verified -> human satisfied
- key signed -> identity known
- capability declared -> authority granted
- high activity -> trustworthy actor
- locked sats -> sincere commitment
- transaction count -> reciprocity
- attestation published -> truth
- event chain healthy -> justice
- timestamp present -> meaning established
- timelock active -> sincere commitment
- endpoint reachable -> legitimacy
- marketplace listed -> safe counterparty
- job executed -> request correctly understood
- Human Proof present -> complete identity known
- covenant participant key present -> participant consent preserved

## Design implications

Future runtime UX should:

- show non-claims near verification results;
- distinguish payment, execution, receipt, and obligation;
- distinguish key control from identity;
- distinguish capability from authority;
- distinguish reputation telemetry from trust;
- distinguish lockup from commitment;
- distinguish transaction history from reciprocity;
- distinguish timestamp, sequence, block height, recency, and commitment horizon;
- expose missing mechanisms instead of hiding them behind successful checks;
- avoid turning bounded evidence into a single trust badge or score.

## Falsification tests

- Do users make wrong trust decisions when shown only receipts?
- Do users overread public keys as identity?
- Do users treat reputation telemetry as a trust score?
- Do users interpret lockups as commitment?
- Do users treat payment as fulfilled obligation?
- Do users treat agent capabilities as authority?
- Do users treat attestations as settled truth?
- Do users treat a healthy event chain as justice, repair, or forgiveness?
- Do users treat marketplace activity as reciprocity?
- Do users treat timestamps, block heights, or timelocks as proof of meaning or sincerity?
- Do users understand what mechanism is missing for a stronger claim?

## Open questions

- Which runtime surfaces need explicit non-claims?
- Which claims should be machine-readable?
- Should every verification response include claim boundaries?
- What is the minimum obligation object?
- What is the minimum delegation record?
- What should stay social rather than cryptographic?
- Which non-claims should be mandatory in marketplace UX?
- How should contradiction, revocation, repair, and forgiveness be represented without pretending they are fully cryptographic?
