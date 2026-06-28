# Obligation Is Not Payment

## 1. Question

When does a paid action become an obligation?

This matters because HODLXXI uses Lightning payments, paid jobs, signed receipts, requester proofs, attestations, and verification surfaces. These mechanisms can show cost and execution, but they can also be overread as proof that a meaningful promise was accepted and fulfilled.

## 2. Scope

This chapter belongs primarily to:

- [Volume I: Foundations](../volumes/01-foundations.md)
- [Volume III: Repeated Games](../volumes/03-repeated-games.md)
- [Volume IV: Cryptographic Primitives](../volumes/04-cryptographic-primitives.md)
- [Volume VII: HODLXXI](../volumes/07-hodlxxi.md)

It relies on:

- [Promise](../lexicon/promise.md)
- [Commitment](../lexicon/commitment.md)
- [Obligation](../lexicon/obligation.md)
- [Receipt](../lexicon/receipt.md)
- [Evidence](../lexicon/evidence.md)
- [Proof](../lexicon/proof.md)
- [Counterparty](../lexicon/counterparty.md)
- [Consent](../lexicon/consent.md)
- [Reputation](../lexicon/reputation.md)
- [Legitimacy](../lexicon/legitimacy.md)

Related chapters:

- [Receipts as Event Proofs](receipts-as-event-proofs.md)
- [Reputation Is Not a Score](reputation-is-not-a-score.md)
- [Memory Before Forgiveness](memory-before-forgiveness.md)

## 3. Observations

Payment creates cost.

Cost can signal seriousness, filter spam, and mark that something entered an execution path.

But payment does not automatically define what was promised, who accepted it, what would count as completion, what would count as breach, or what remedy should follow failure.

A paid job can complete in a narrow runtime sense while still failing a human expectation.

A receipt can verify while the obligation remains undefined.

## 4. Claim

Payment is evidence of cost.

It is not an obligation by itself.

An obligation requires at least a counterparty, a promise or expectation, acceptance criteria, a time horizon, a breach condition, and a remedy or repair path.

Without these, payment produces evidence of exchange, not a full obligation relation.

## 5. Non-claims

This chapter does not claim that payment has no meaning.

It does not claim that paid jobs are invalid.

It does not claim that obligations must be legal contracts.

It does not claim that every small job needs a heavy obligation model.

It claims that HODLXXI should not represent payment or receipt verification as proof of fulfilled obligation unless obligation semantics are explicitly modeled.

Payment does not by itself prove:

- promise;
- consent to broader terms;
- acceptance;
- satisfaction;
- completion quality;
- breach absence;
- remedy;
- legitimacy;
- durable commitment.

## 6. Working theory

Promises become obligations when they create accountable expectations between actors.

A cost signal can support this process, but it is not enough.

The minimum obligation lifecycle is:

1. proposal;
2. counterparty identification;
3. consent or acceptance;
4. stated promise;
5. acceptance criteria;
6. performance or delivery;
7. verification;
8. dispute path;
9. remedy, repair, or closure.

A system that skips these steps may produce valid paid events but weak obligations.

## 7. Runtime evidence

Relevant HODLXXI runtime mechanisms include:

- `/agent/request`;
- Lightning invoice/payment flow;
- paid job status;
- signed receipts;
- `/agent/verify/<job_id>`;
- requester proof paths;
- attestations;
- event-chain memory;
- reputation telemetry;
- future dispute and repair records.

| Runtime surface | What it can show | What it does not prove |
| --- | --- | --- |
| Lightning invoice | A payment path was created. | Promise, acceptance, or obligation. |
| Paid job | Work entered an execution path. | Satisfaction or durable commitment. |
| Receipt | A bounded event was signed. | Fulfilled obligation. |
| Verification endpoint | A receipt can be checked. | Human completion criteria. |
| Requester proof | A key is bound to a request. | Complete counterparty relation. |
| Attestation | A statement was exposed. | Final judgment or remedy. |
| Reputation telemetry | Some memory can be summarized. | Repair-aware obligation history. |

## 8. Counterarguments

One objection is that payment itself is the obligation: the user paid, the agent delivered.

That can be true for very narrow jobs if the terms are simple and accepted. But even then, the obligation exists because the terms and completion criteria are understood, not because payment alone magically created them.

Another objection is that explicit obligation semantics are too heavy for small tasks.

That may be true. HODLXXI can keep small jobs lightweight while still avoiding overclaim. The runtime can say: paid execution completed, not obligation fulfilled.

A third objection is that markets already solve this.

Markets solve some exchange problems, but they still rely on norms, refunds, dispute handling, warranties, ratings, reputation, and legal or social enforcement.

## 9. Historical analogies

A tip signals gratitude or incentive, but not always a contract.

A receipt proves a transaction, but not satisfaction or remedy.

A deposit can signal commitment, but the rules of forfeiture, return, and breach must be known.

Merchant credit systems depended not only on payment but on remembered performance and remedy.

Bitcoin transactions settle according to consensus rules, but they do not encode the full off-chain obligation that motivated the payment.

## 10. Failure modes

- Payment is mistaken for consent.
- Receipt verification is mistaken for obligation fulfillment.
- Paid jobs become ritual without clear promises.
- Users assume remedies that the runtime never offered.
- Agents optimize for paid completion instead of meaningful fulfillment.
- Disputes arise because acceptance criteria were never modeled.
- Reputation treats paid activity as trustworthy behavior.
- A wealthy actor buys the appearance of commitment.
- A counterparty cannot identify what was actually owed.

## 11. Implications for HODLXXI

HODLXXI should keep paid execution distinct from obligation fulfillment.

Future runtime work may need an obligation object with fields such as:

- counterparty;
- promise;
- consent evidence;
- acceptance criteria;
- time horizon;
- breach condition;
- dispute state;
- remedy path;
- repair events;
- closure state.

Until then, paid job surfaces should use narrow language: request, payment, execution, result, receipt, verification.

They should not silently imply fulfilled obligation.

## 12. Falsification

This chapter would be weakened if paid job events alone reliably produced shared understanding, low dispute rates, clear remedies, and durable cooperation without explicit obligation modeling.

It would be strengthened if users overread payment or receipts as commitment, if disputes arise over completion criteria, or if reputation systems treat paid activity as fulfilled obligation.

A concrete runtime test:

Compare user interpretation of a paid receipt alone versus a paid receipt plus explicit promise, acceptance criteria, counterparty, dispute state, and remedy path.

If the second view produces better trust decisions, payment alone is insufficient as an obligation primitive.

## 13. Open questions

- What is the minimum obligation object HODLXXI should support?
- Which paid jobs need explicit acceptance criteria?
- Should every paid job have a counterparty field?
- What is the difference between result delivery and obligation fulfillment?
- How should breach be represented?
- What remedies are appropriate for tiny Lightning-paid jobs?
- Can repair be modeled without turning every interaction into a contract?
- What should HODLXXI refuse to claim from payment alone?
