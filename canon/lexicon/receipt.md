# Receipt

## Definition

A receipt is a remembered record of a bounded event.

In HODLXXI, a receipt is strongest when it is signed, verifiable, linked to event
memory, and explicit about what it does not prove.

## Operational meaning

A receipt can support memory by recording:

- that a runtime event occurred;
- which key signed the record;
- which request or result was referenced;
- when the event was recorded;
- how later verification can inspect it.

## What a receipt is not

A receipt is not automatically obligation fulfillment.

A receipt is not requester satisfaction.

A receipt is not output quality.

A receipt is not delegated authority.

A receipt is not repair.

## Observable behavior

In HODLXXI, receipts may appear in paid job flows, verification endpoints, attestations,
and local event memory.

A receipt can become evidence for reputation, but it is not reputation by itself.

## Failure modes

- Receipt count becomes reputation theater.
- A valid receipt is treated as proof of fulfilled obligation.
- Low-quality behavior produces many valid receipts.
- Disputed outcomes appear settled because an event verifies.
- Receipts accumulate without correction, dispute, or repair.

## Implications for HODLXXI

Receipt semantics should remain narrow until obligations, counterparties, acceptance
criteria, dispute state, and remedies are explicitly modeled.

## Open questions

- What should receipt v2 include?
- Should receipts bind requester proof level?
- Should receipts include acceptance criteria?
- How should disputed receipts be represented?
- Should receipt memory be externally anchored?
