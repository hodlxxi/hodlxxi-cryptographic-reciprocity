# evidence-boundary-metadata-v0

## Purpose

Evidence Boundary Metadata v0 defines the minimum metadata a HODLXXI runtime evidence
surface should expose before users, operators, or agents are invited to interpret that
evidence.

The mechanism exists to keep evidence bounded. It should help an observer distinguish:

- evidence from truth;
- timestamps from meaning;
- receipts from satisfaction;
- attestations from truth;
- lockups from commitment;
- key control from identity;
- event history from reputation;
- memory from forgiveness;
- transaction history from reciprocity;
- capability from authority.

This is a Canon-level mechanism candidate. It is not a runtime schema, API contract,
database migration, UI mandate, or implementation claim.

## Canon claims

This mechanism cites existing Canon claims without changing their meanings.

| Claim ID | Source | Boundary used by this mechanism |
| --- | --- | --- |
| `CRT-EVIDENCE-001` | [Evidence Is Not Truth](../chapters/evidence-is-not-truth.md) | Evidence can support, weaken, or revise interpretation, but it is not truth by itself. |
| `CRT-TIME-001` | [Time Is Not Timestamp](../chapters/time-is-not-timestamp.md) | Time data needs sequence, horizon, and interpretation context before it becomes meaningful. |
| `CRT-RECEIPT-001` | [Receipts as Event Proofs](../chapters/receipts-as-event-proofs.md) | A receipt proves a bounded event, not satisfaction, obligation, or trustworthiness. |
| `CRT-IDENTITY-001` | [Identity Is Not Key Control](../chapters/identity-is-not-key-control.md) | A key, endpoint, or Human Proof surface is not full identity. |
| `CRT-OBLIGATION-001` | [Obligation Is Not Payment](../chapters/obligation-is-not-payment.md) | Payment, execution, or a receipt is not obligation fulfillment. |
| `CRT-COMMITMENT-001` | [Commitment Is Not Lockup](../chapters/commitment-is-not-lockup.md) | A lockup is constraint evidence, not complete commitment. |
| `CRT-REPUTATION-001` | [Reputation Is Not a Score](../chapters/reputation-is-not-a-score.md) | Reputation is contextual compressed memory, not a global score. |
| `CRT-FORGIVENESS-001` | [Memory Before Forgiveness](../chapters/memory-before-forgiveness.md) | Forgiveness requires memory, repair, and changed behavior; it is not erasure. |
| `CRT-RECIPROCITY-001` | [Reciprocity Is Not Transaction](../chapters/reciprocity-is-not-transaction.md) | Reciprocity is a pattern across events, memory, expectation, and time. |
| `CRT-AGENT-AUTHORITY-001` | [Bounded Authority for AI Agents](../chapters/bounded-authority-for-ai-agents.md) | Capability, fluency, or key control is not delegated authority. |

Related Canon and runtime documents include the [Canon map](../MAP.md), the
[Runtime claims matrix](../runtime/claims-matrix.md), [Runtime non-claims](../runtime/non-claims.md),
and the [Canon / Runtime Gap Register](../runtime/gap-register.md).

## Problem

HODLXXI can expose receipts, attestations, Human Proof signals, event chains, reputation
summaries, covenant references, verification surfaces, and agent messages. These are
valuable evidence surfaces. They are also dangerous if shown without their boundaries.

A bare evidence surface may invite unsafe inference chains:

- signed -> true;
- timestamped -> meaningful;
- verified -> settled;
- receipt exists -> human satisfied;
- attestation exists -> legitimacy established;
- Human Proof exists -> full identity known;
- lockup exists -> commitment proven;
- event chain healthy -> memory complete;
- reputation summary positive -> actor trustworthy;
- agent can do a task -> agent is authorized to do it.

Evidence Boundary Metadata v0 makes these boundaries visible at the evidence surface
itself. It does not make interpretation automatic. It makes overclaim easier to see,
contest, repair, and falsify.

## Minimum metadata fields

A minimum evidence boundary record should expose the following fields when an evidence
surface is used to support a runtime or Canon-adjacent claim.

| Field | Description | Unsafe inference it helps prevent |
| --- | --- | --- |
| `evidence_id` | Stable identifier for the evidence item or evidence surface. | Prevents later references from silently drifting to a different event or object. |
| `evidence_type` | Bounded type, such as `signed_receipt`, `attestation`, `human_proof`, `covenant_lockup`, `event_chain_health`, or `reputation_summary`. | Prevents one evidence type from being treated as another. |
| `issuer_or_recorder` | Actor, key, system component, verifier, or process that issued or recorded the evidence. | Prevents anonymous evidence from being read as authoritative without source context. |
| `subject` | Actor, job, request, key, lockup, relationship, event chain, or reputation context the evidence concerns. | Prevents evidence about one subject from being generalized to another. |
| `related_actor_keys` | Keys materially related to the evidence, with role context when known. | Prevents key control from being read as full identity or authority. |
| `event_time` | Time the represented event is said to have occurred. | Prevents event occurrence from being collapsed into observation or verification. |
| `observation_time` | Time the evidence was observed, recorded, or surfaced by HODLXXI. | Prevents observation time from being read as event time. |
| `verification_time` | Time a verification rule was applied, if any. | Prevents verification time from being read as proof that the underlying meaning is settled. |
| `bitcoin_block_height` | Bitcoin block height used as an anchor or ordering reference, if present. | Prevents block anchoring from being read as truth, satisfaction, or legitimacy. |
| `sequence_context` | Prior, next, parent, child, or competing events needed to understand ordering. | Prevents a single timestamp from standing in for time, memory, or relationship history. |
| `verification_rule` | Narrow rule applied to the evidence, such as signature check, hash match, inclusion check, or declared policy check. | Prevents verification from expanding beyond the actual rule. |
| `bounded_claim` | The strongest claim the evidence is allowed to support. | Prevents evidence from silently becoming truth, obligation, identity, satisfaction, legitimacy, or trust. |
| `explicit_non_claims` | Claims the evidence explicitly does not support. | Forces the surface to display its own interpretive boundary. |
| `missing_context` | Context known to be absent, private, unresolved, disputed, or not collected. | Prevents absence of context from being mistaken for absence of problems. |
| `contradiction_path` | Where contradictory evidence can be linked, found, or submitted. | Prevents one evidence item from becoming uncontestable. |
| `revocation_path` | Where revocations, corrections, key compromise notices, or withdrawn attestations can be linked. | Prevents stale evidence from remaining authoritative after its basis changes. |
| `counter_evidence_path` | Where counter-evidence from affected actors, observers, or later records can be attached. | Prevents issuer-only evidence from dominating interpretation. |
| `dispute_path` | Where parties can contest meaning, authority, quality, satisfaction, or legitimacy. | Prevents verified event data from being treated as settled human meaning. |
| `repair_path` | Where remedy, correction, restitution, apology, re-performance, or repair records can be linked. | Prevents failure records from becoming permanent punishment or repair theater. |
| `privacy_scope` | Public, pairwise, group-limited, private, redacted, or selectively disclosed visibility. | Prevents evidence boundaries from leaking unnecessary relationship or identity context. |
| `retention_horizon` | Expected retention, expiry, archival, redaction, or review horizon. | Prevents evidence from being treated as either eternal judgment or erasable inconvenience. |
| `human_interpretation_required` | Whether a human must review meaning before a stronger claim is displayed or acted on. | Prevents agents or UI surfaces from converting bounded evidence into final judgment. |

## Example surfaces

| Surface | Example bounded claim | Required boundary emphasis | Explicit non-claims |
| --- | --- | --- | --- |
| Signed receipt | A specific runtime event was signed by a listed key under a stated verification rule. | Show event time, verification time, issuer key, subject, request or job reference, and contradiction/dispute paths. | Does not prove satisfaction, obligation fulfillment, human approval, trustworthiness, or legitimacy. |
| Attestation | A named issuer made a statement about a bounded subject at a recorded time. | Show issuer, subject, authority context if any, revocation path, counter-evidence path, and missing context. | Does not prove truth, justice, legitimacy, identity, or settlement. |
| Human Proof | A surface exposed evidence relevant to human presence, continuity, or participation in a bounded context. | Show subject, related keys, event and observation times, verification rule, privacy scope, and missing identity context. | Does not prove full identity, consent, authority, sincerity, personhood in every sense, or satisfaction. |
| Covenant lockup | A value or spending constraint was observed under a stated rule and time or block context. | Show lockup subject, rule, block height, time horizon, release or revocation context, and related obligation or commitment records if any. | Does not prove love, loyalty, sincerity, legitimacy, obligation, reciprocity, or complete commitment. |
| Event chain health | A local event chain passed a continuity or integrity check over a stated sequence. | Show sequence context, verification rule, missing external anchors, contradiction path, and retention horizon. | Does not prove complete memory, truth, justice, external immutability, or absence of omitted events. |
| Reputation summary | A contextual memory summary was computed from stated inputs over a stated horizon. | Show evidence inputs, domain, time horizon, dispute and repair state, missing context, and human interpretation requirement. | Does not prove global trustworthiness, moral worth, future behavior, legitimacy, or forgiveness. |

## Non-goals

This mechanism does not:

- prove truth;
- prove full identity;
- prove sincerity;
- prove satisfaction;
- prove obligation fulfillment;
- prove legitimacy;
- replace human judgment;
- implement runtime schema yet;
- require all evidence to be public;
- require every small interaction to expose heavy metadata;
- decide disputes;
- launder reputation through better formatting;
- convert cryptographic validity into moral, social, or legal settlement.

## Failure modes

- Metadata is present but users ignore it.
- `bounded_claim` becomes vague or promotional.
- `explicit_non_claims` are hidden below stronger UI language.
- `issuer_or_recorder` is treated as authority without delegation context.
- `bitcoin_block_height` is read as truth rather than ordering evidence.
- `verification_rule` is too broad, opaque, or unverifiable.
- Dispute, revocation, contradiction, and repair paths exist but are not usable.
- Privacy scope leaks identity, relationship, or harm context unnecessarily.
- Retention horizon becomes erasure of accountability or permanent punishment.
- Agents act on evidence without respecting `human_interpretation_required`.
- Reputation summaries compress away dispute, repair, coercion, or missing context.
- Covenant lockups are used as commitment theater.

## Implications for HODLXXI

HODLXXI evidence surfaces should prefer weaker, bounded wording unless this metadata and
its related mechanisms support a stronger claim.

Examples:

- say "receipt verified under this rule" instead of "work accepted";
- say "attestation recorded" instead of "truth established";
- say "Human Proof observed for this context" instead of "identity proven";
- say "lockup observed" instead of "commitment proven";
- say "event chain continuity check passed" instead of "history is complete";
- say "contextual reputation summary" instead of "trust score";
- say "capability declared" instead of "authority granted".

This mechanism should be treated as a candidate boundary layer for future runtime
surfaces, especially receipts, attestations, Human Proof, event chains, covenant lockups,
agent verification, and reputation summaries. It should link outward to obligation,
delegation, repair, reciprocity, identity continuity, and contextual reputation records
when those mechanisms are present, rather than replacing them.

## Open questions

- Which fields must be machine-readable in the first runtime version?
- Which fields should remain human-readable annotations?
- How lightweight can the metadata be for small 21-sat jobs?
- Should `bounded_claim` use a fixed vocabulary or free text?
- How should private contradiction or repair evidence be represented without leaking harm?
- What minimum dispute path is acceptable for pseudonymous actors?
- When should `human_interpretation_required` block agent action?
- How should evidence boundaries be shown in compact UIs without hiding the warning?
- What should happen when old evidence lacks this metadata?
- Which runtime surface should adopt this mechanism first?
