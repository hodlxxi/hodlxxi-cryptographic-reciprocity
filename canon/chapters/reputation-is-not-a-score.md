# Reputation Is Not a Score

## 1. Question

What is reputation in CRT, and why is it dangerous to reduce it to a single score?

This matters because HODLXXI exposes reputation telemetry, attestations, receipts, trust
events, and local event memory. These mechanisms can help observers reason about past
behavior, but they can also create false confidence if compressed into a naive global
score.

## 2. Scope

This chapter belongs primarily to:

- [Volume I: Foundations](../volumes/01-foundations.md)
- [Volume III: Repeated Games](../volumes/03-repeated-games.md)
- [Volume V: Institutions](../volumes/05-institutions.md)
- [Volume VII: HODLXXI](../volumes/07-hodlxxi.md)

It relies on:

- [Reputation](../lexicon/reputation.md)
- [Memory](../lexicon/memory.md)
- [Evidence](../lexicon/evidence.md)
- [Attestation](../lexicon/attestation.md)
- [Trust](../lexicon/trust.md)
- [Counterparty](../lexicon/counterparty.md)
- [Forgiveness](../lexicon/forgiveness.md)
- [Legitimacy](../lexicon/legitimacy.md)

Related runtime notes:

- [Reputation and memory](../runtime/reputation-memory.md)
- [Runtime non-claims](../runtime/non-claims.md)
- [Missing runtime mechanisms](../runtime/missing-mechanisms.md)

## 3. Observations

HODLXXI runtime can expose operational telemetry: jobs, receipts, attestations,
event-chain continuity, successful verification, public reports, and aggregate
summaries.

These are useful evidence surfaces.

But a user may treat any visible reputation number, count, badge, ratio, or summary as a
full judgment of trustworthiness.

That interpretation can be wrong.

A high number may reflect activity rather than character, volume rather than quality,
completed events rather than fulfilled obligations, or visibility rather than
reliability.

## 4. Claim

Reputation is compressed memory.

A score is only one possible compression of memory, and often a dangerous one.

Reputation in CRT must remain contextual, counterparty-sensitive, revisable, and
connected to evidence, dispute, repair, and time.

## 5. Non-claims

This chapter does not claim that metrics are useless.

It does not claim that aggregation is always bad.

It does not claim that humans can evaluate everything manually.

It claims that a reputation score must not be treated as full reputation unless the
compression method, context, limits, and failure modes are explicit.

A reputation score does not by itself prove:

- trustworthiness;
- moral character;
- obligation fulfillment;
- legitimacy;
- absence of dispute;
- quality of past behavior;
- future reliability;
- repair after failure;
- resistance to manipulation.

## 6. Working theory

Reputation helps cooperation by compressing past behavior into usable memory.

Without compression, memory becomes too large for humans and agents to interpret.

But compression destroys context.

The danger is not reputation itself. The danger is unaccountable compression.

A healthy reputation system should preserve enough context to answer:

- reputation for what;
- according to whom;
- over what time horizon;
- with what evidence;
- under what dispute state;
- after what repair;
- against what possibility of manipulation.

## 7. Runtime evidence

Relevant HODLXXI runtime mechanisms include:

- `/agent/reputation`;
- signed receipts;
- attestations;
- event-chain health;
- paid job history;
- Human Proof requester paths;
- trust events;
- marketplace listing;
- future dispute and repair records.

| Runtime surface | What it can show | What it does not prove |
| --- | --- | --- |
| Reputation telemetry | Aggregated operational memory. | Full social reputation. |
| Receipt count | Number of recorded events. | Quality, satisfaction, or fulfilled obligation. |
| Attestations | Published claims or summaries. | Truth or final judgment. |
| Event-chain health | Local continuity of memory. | External anchoring or justice. |
| Paid job history | Activity and payment flow. | Trustworthiness or long-term cooperation. |
| Marketplace listing | Claimed offer context. | Honesty, fulfillment, or safety. |

## 8. Counterarguments

One objection is that users need a simple score because they cannot inspect all
evidence.

This is true. But simplicity must not hide what the score discards. A score can guide
attention, but it should not replace judgment.

Another objection is that markets already use ratings successfully.

They do, but ratings also produce manipulation, review farming, retaliation, herd
effects, and context collapse.

A third objection is that without scoring, the system cannot scale.

CRT should not reject compression. It should design compression that remains auditable,
contextual, and corrigible.

## 9. Historical analogies

Merchant reputation depended on repeated dealings, letters, guild networks, kinship, and
remembered failures. It was not merely a number.

Credit scores compress financial behavior into a usable signal, but they can erase
context and create institutional dependency.

Online ratings help strangers transact, but they also invite gaming, fake reviews,
retaliation, and platform capture.

Honor systems preserve memory of behavior, but they can become brittle, violent, or
impossible to repair.

## 10. Failure modes

- A trust score becomes a caste system.
- Receipt count becomes reputation theater.
- High-volume actors appear trustworthy while low-volume actors remain invisible.
- Cartels inflate each other's reputation.
- Sybil actors reset identity faster than reputation can accumulate.
- Reputation becomes punishment without repair.
- Repair becomes laundering without memory.
- Users optimize for score rather than cooperative behavior.
- Context is erased by aggregation.
- A platform becomes the authority over legitimacy.

## 11. Implications for HODLXXI

HODLXXI should treat reputation telemetry as evidence, not final judgment.

A future reputation surface should preserve:

- evidence links;
- counterparty context;
- time horizon;
- job type or interaction type;
- proof level;
- dispute state;
- correction state;
- repair or restitution linkage;
- decay or aging model;
- non-claims.

HODLXXI should avoid global trust scores until it has stronger models for counterparty
context, dispute, correction, repair, and sybil resistance.

## 12. Falsification

This chapter would be weakened if a simple global score reliably predicted trustworthy
future behavior across contexts, counterparties, and time horizons better than
contextual reputation evidence.

It would be strengthened if users overtrust scores, if receipt count becomes reputation
theater, if high-score actors exploit context gaps, or if disputes require evidence that
the score erased.

A concrete runtime test:

Compare user decisions when shown a single score versus contextual reputation evidence:
receipts, attestations, job types, counterparty history, dispute state, repair state,
and non-claims.

If contextual evidence produces better decisions, then score-only reputation is
insufficient.

## 13. Open questions

- What should HODLXXI aggregate, and what should remain contextual?
- Should reputation decay over time?
- Should different job types have separate reputation contexts?
- How should disputed events affect reputation?
- How should repair change interpretation without erasing memory?
- How can reputation resist sybil reset and cartel inflation?
- What reputation information should be public, private, or selectively disclosed?
- What should HODLXXI refuse to reduce to a score?
