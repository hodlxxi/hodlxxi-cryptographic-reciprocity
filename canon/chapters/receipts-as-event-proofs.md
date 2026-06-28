# Receipts as Event Proofs

## 1. Question

What does a HODLXXI receipt prove, and what does it not prove?

This matters because HODLXXI uses paid jobs, signed receipts, verification, attestations, and local event memory. These mechanisms can make events visible, but they can also be overread as proof of human meaning, satisfaction, authority, or fulfilled obligation.

## 2. Scope

This chapter belongs primarily to:

- [Volume IV: Cryptographic Primitives](../volumes/04-cryptographic-primitives.md)
- [Volume VII: HODLXXI](../volumes/07-hodlxxi.md)

It relies on:

- [Promise](../lexicon/promise.md)
- [Commitment](../lexicon/commitment.md)
- [Obligation](../lexicon/obligation.md)
- [Memory](../lexicon/memory.md)
- [Reputation](../lexicon/reputation.md)
- [Legitimacy](../lexicon/legitimacy.md)

Related runtime notes:

- [Runtime receipts](../runtime/receipts.md)
- [Runtime non-claims](../runtime/non-claims.md)
- [Reputation and memory](../runtime/reputation-memory.md)

## 3. Observations

A valid receipt can show that a runtime event was recorded and signed.

It may bind a job type, request hash, payment hash, result hash, timestamp, agent key, and event linkage.

But a person may see a receipt and assume more than the receipt proves. They may assume the requester was satisfied, the result was good, no dispute exists, or a deeper obligation was fulfilled.

Those assumptions can be false even when the receipt is valid.

## 4. Claim

A receipt is an event proof.

It is not an obligation proof unless the obligation, counterparty, acceptance criteria, breach condition, and remedy are explicitly modeled.

The purpose of a receipt is to preserve memory of a recorded event. Its purpose is not to settle every social meaning attached to that event.

## 5. Non-claims

This chapter does not claim that receipts are useless or that cryptographic proof is unimportant.

It claims that receipts must be interpreted within their evidentiary boundary.

A receipt does not by itself prove:

- human meaning;
- output quality;
- requester satisfaction;
- obligation fulfillment;
- dispute absence;
- delegated authority;
- external anchoring;
- forgiveness or repair;
- social legitimacy.

## 6. Working theory

Trust systems fail when evidence is compressed into meaning too quickly.

A receipt is a memory artifact. It preserves that something happened in a bounded runtime context. This is valuable because long-running cooperation requires remembered behavior.

But memory is not judgment.

A receipt can support later interpretation, reputation, audit, dispute, or repair. It should not replace those processes.

The stronger theory is:

1. Events must be remembered before they can be interpreted.
2. Interpretation requires context.
3. Obligation requires counterparty, expectation, acceptance criteria, and remedy.
4. Reputation requires repeated contextual memory.
5. Forgiveness requires remembered failure and visible repair.

A receipt supplies part of step 1. It does not complete steps 2 through 5.

## 7. Runtime evidence

Relevant HODLXXI runtime mechanisms include:

- paid jobs;
- Lightning invoice/payment flow;
- signed receipts;
- `/agent/verify/<job_id>`;
- attestations;
- local AgentEvent chain;
- reputation telemetry;
- Human Proof requester paths.

| Mechanism | What it makes visible | What it does not prove |
| --- | --- | --- |
| Paid job | A task entered a paid execution path. | Satisfaction or fulfilled obligation. |
| Lightning payment | Cost was associated with execution. | Trustworthiness or legitimacy. |
| Signed receipt | A runtime key signed event evidence. | Human meaning or acceptance. |
| Verification endpoint | A receipt can be checked later. | The social interpretation of the event. |
| Attestation | A statement can be exposed. | Truth, context, or final judgment. |
| Event chain | Local memory continuity can be checked. | Global immutability or external anchoring. |
| Reputation telemetry | Operational behavior can be summarized. | Full social reputation. |

## 8. Counterarguments

One objection is that a receipt is enough because the system only needs objective facts.

But objective facts are necessary, not sufficient. Human cooperation often turns on quality, interpretation, reliance, context, and repair.

Another objection is that payment proves seriousness.

Payment can indicate cost, but cost can also become theater or a cheap signal for wealthy actors.

A third objection is that if the receipt verifies, the job is done.

The runtime may be done with its narrow task while a counterparty still disputes meaning, sufficiency, quality, or obligation fulfillment.

## 9. Historical analogies

A paper receipt proves that a transaction was recorded. It does not prove the customer was satisfied or the product was good.

A merchant ledger preserves memory. It helps resolve disputes, but the ledger itself does not eliminate judgment.

A Bitcoin transaction proves movement under consensus rules. It does not prove why the movement happened or whether an off-chain promise was honored.

## 10. Failure modes

- Event proof is mistaken for obligation proof.
- Payment is mistaken for commitment.
- Key control is mistaken for identity.
- Verification is mistaken for trustworthiness.
- A receipt is used as status theater.
- Receipt count becomes fake reputation.
- Disputed outcomes appear settled because the cryptographic event verifies.
- Agents optimize for receipt production rather than meaningful completion.
- The runtime creates memory without repair.

## 11. Implications for HODLXXI

HODLXXI should encode event evidence clearly and verifiably.

Future receipt versions may need:

- requester identity binding;
- proof level;
- acceptance criteria;
- obligation reference;
- dispute or correction state;
- repair or restitution linkage;
- external anchoring reference.

It should be impossible for a valid receipt to be represented as proof of human meaning unless that meaning is explicitly modeled, bounded, and falsifiable.

HODLXXI should not build automatic obligation enforcement, global trust scoring, or reputation penalties directly from receipt count.

## 12. Falsification

This chapter would be weakened if production evidence showed that valid receipts reliably predict obligation fulfillment, requester satisfaction, output quality, and future trustworthy behavior without additional context.

It would be strengthened if users overread receipts, if receipt count becomes reputation theater, or if paid jobs produce valid receipts but disputed meaning.

A concrete runtime test:

Compare user trust decisions when shown only receipt verification versus receipt verification plus non-claims, context, requester identity, acceptance criteria, and dispute state.

If the second group makes better trust decisions, then receipt verification alone is insufficient as a trust primitive.

## 13. Open questions

- What fields would make a receipt stronger evidence without overclaiming?
- Should every receipt include requester proof level?
- Should acceptance criteria be machine-readable, human-readable, or both?
- How should a disputed receipt be represented?
- Can repair be linked to an earlier receipt without erasing the failure?
- When should receipt memory be externally anchored?
- What should a verifier show to prevent ordinary users from overreading receipt validity?
