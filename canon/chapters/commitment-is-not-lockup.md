# Commitment Is Not Lockup

## 1. Question

What does a Bitcoin lockup prove, and what does it fail to preserve?

This matters because HODLXXI uses Bitcoin time, covenants, public keys, receipts, verification, and long-horizon constraints. A lockup can make commitment visible and costly, but it can also become ritual, status theater, or financial performance without human meaning.

## 2. Scope

This chapter belongs primarily to:

- [Volume I: Foundations](../volumes/01-foundations.md)
- [Volume IV: Cryptographic Primitives](../volumes/04-cryptographic-primitives.md)
- [Volume V: Institutions](../volumes/05-institutions.md)
- [Volume VII: HODLXXI](../volumes/07-hodlxxi.md)

It relies on:

- [Commitment](../lexicon/commitment.md)
- [Promise](../lexicon/promise.md)
- [Obligation](../lexicon/obligation.md)
- [Memory](../lexicon/memory.md)
- [Evidence](../lexicon/evidence.md)
- [Proof](../lexicon/proof.md)
- [Legitimacy](../lexicon/legitimacy.md)
- [Trust](../lexicon/trust.md)
- [Counterparty](../lexicon/counterparty.md)

Related chapters:

- [Receipts as Event Proofs](receipts-as-event-proofs.md)
- [Obligation Is Not Payment](obligation-is-not-payment.md)
- [Identity Is Not Key Control](identity-is-not-key-control.md)
- [Reputation Is Not a Score](reputation-is-not-a-score.md)

## 3. Observations

A Bitcoin lockup can constrain spending across time.

A covenant or time-locked script can make a future condition visible, verifiable, and difficult to fake.

A long lockup can impose opportunity cost.

A public lockup can create a durable signal.

But the same lockup does not prove the actor's inner intention, the counterparty's understanding, the social meaning of the act, or whether the act will remain legitimate over time.

A person may lock sats and still use the system as performance, manipulation, status theater, empty ritual, or reputation laundering.

## 4. Claim

A lockup is a constraint proof.

It is not a complete commitment proof.

A lockup can support commitment by making cost, time, and constraint visible. But commitment in CRT also requires meaning, counterparty context, remembered promise, obligation boundary, and interpretable behavior over time.

## Claim IDs

| Claim ID | Existing claim |
| --- | --- |
| `CRT-COMMITMENT-001` | A lockup is a constraint proof; it is not a complete commitment proof. |

## 5. Non-claims

This chapter does not claim that lockups are useless.

It does not claim that Bitcoin time is irrelevant.

It does not claim that cryptographic constraints cannot strengthen commitment.

It does not claim that HODLXXI should avoid covenants or time locks.

It claims only that a lockup must not be treated as the whole commitment.

A lockup does not by itself prove:

- sincerity;
- love;
- loyalty;
- promise fulfillment;
- counterparty acceptance;
- obligation scope;
- legitimacy;
- social meaning;
- future repair;
- resistance to manipulation.

## 6. Working theory

Commitment becomes stronger when intention is constrained by visible cost.

Bitcoin lockups are powerful because they make some future behavior harder to fake. They transform words into constraints.

But constraints are not meaning.

A cryptographic system can preserve that sats were locked while losing why they were locked, for whom, under what expectation, with what obligation, and with what path for dispute or repair.

The strongest commitment form in HODLXXI is not merely locked value. It is locked value plus remembered relationship, explicit counterparty context, durable identity, interpretable promise, and visible consequences over time.

## 7. Runtime evidence

Relevant HODLXXI mechanisms include:

- covenant declarations;
- two-branch time-locked scripts;
- operator and participant public keys;
- proof-of-funds surfaces;
- receipt verification;
- event-chain memory;
- reputation telemetry;
- future obligation records;
- future repair records.

| Mechanism | What it can show | What it does not prove |
| --- | --- | --- |
| Time lock | Coins cannot move before a condition or height. | Human meaning or sincerity. |
| Covenant script | A spending path is constrained. | Social legitimacy of the constraint. |
| Public key | A key participates in a script. | Full identity or authority. |
| Proof of funds | Value is visible. | Commitment, love, or obligation fulfillment. |
| Receipt | An event was recorded. | The meaning of the locked value. |
| Reputation telemetry | Some behavior can be summarized. | Full social trust. |

## 8. Counterarguments

One objection is that a lockup is commitment because it imposes real cost.

Cost matters. But cost alone can be used for theater. Wealthy actors can buy signals. Desperate actors can overcommit. Manipulators can lock value to create false confidence.

Another objection is that Bitcoin removes ambiguity.

Bitcoin removes some ambiguity about valid state transitions. It does not remove ambiguity about human intention, obligation, gratitude, betrayal, forgiveness, or legitimacy.

A third objection is that social meaning should remain outside the protocol.

Some meaning should remain social. But the system must still prevent users from mistaking cryptographic constraint for complete commitment.

## 9. Historical analogies

A wedding ring is a costly symbol, but it is not the marriage.

A hostage or collateral can deter betrayal, but it does not prove love or loyalty.

A legal bond can create enforceable cost, but it does not guarantee honor.

A religious vow can preserve public form while losing inner meaning.

A Bitcoin transaction proves consensus-valid movement, not the full story behind the movement.

## 10. Failure modes

- Locked sats become status theater.
- A wealthy actor buys the appearance of commitment.
- A desperate actor locks too much and becomes dependent.
- Counterparties overtrust a lockup without understanding terms.
- A lockup lacks clear obligation or remedy.
- A public covenant becomes ritual without relationship.
- Reputation attaches to locked value rather than fulfilled behavior.
- The system proves constraint while losing human meaning.
- Long lockups become coercive rather than trustworthy.
- Users confuse financial sacrifice with legitimacy.

## 11. Implications for HODLXXI

HODLXXI should present lockups as constraint evidence, not complete commitment evidence.

Future HODLXXI surfaces should distinguish:

- locked value;
- script terms;
- participant keys;
- counterparty context;
- stated promise;
- obligation boundary;
- time horizon;
- dispute state;
- repair path;
- non-claims.

The system should make it difficult to represent locked sats as proof of love, loyalty, trustworthiness, or fulfilled obligation unless those meanings are separately modeled and bounded.

## 12. Falsification

This chapter would be weakened if production evidence showed that lockups alone reliably create durable cooperation, accurate trust decisions, low dispute rates, and preserved human meaning without additional context.

It would be strengthened if users overread lockups as trust, if high-value locks become status theater, if locked value launders reputation, or if counterparties misunderstand what a covenant proves.

A concrete runtime test:

Compare user decisions when shown only locked value and script data versus locked value plus counterparty context, promise, obligation boundary, dispute state, repair path, and non-claims.

If the second view produces better trust decisions, lockup alone is insufficient as a commitment primitive.

## 13. Open questions

- What should HODLXXI call a lockup without overclaiming?
- What minimum context should appear beside a covenant?
- Should lockups have stated purpose fields?
- When does a lockup become coercive?
- Can small lockups create honest commitment signals better than large ones?
- What should be private, public, or selectively disclosed?
- How should a covenant show that it proves constraint but not full human meaning?
- What should HODLXXI refuse to infer from locked value alone?
