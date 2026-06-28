# Counterparty

## Definition

A counterparty is another actor whose behavior, consent, reliance, risk, or future claim matters to an interaction.

In CRT, counterparty is not merely an address, account, public key, or API caller. It is the other side of a relationship that may create memory, promise, obligation, reciprocity, dispute, repair, or reputation.

## Operational meaning

A counterparty becomes operational when the system can represent:

- who or what the other actor is;
- what interaction connects the actors;
- what claim, promise, payment, receipt, or obligation relates them;
- what each side can later verify;
- what each side may dispute, accept, repair, or forgive.

## What counterparty is not

A counterparty is not automatically a legal identity.

A counterparty is not automatically a trusted actor.

A counterparty is not only a public key.

A counterparty is not only the payer.

A counterparty is not only the requester.

## Observable behavior

In HODLXXI, counterparties may appear through:

- requester public keys;
- Human Proof requester paths;
- paid job requests;
- receipts;
- marketplace interactions;
- covenant participants;
- inter-agent messages;
- future dispute or repair records.

## Failure modes

- The runtime records a job but not a meaningful counterparty.
- A payer is mistaken for the real counterparty.
- A public key is mistaken for full identity.
- A receipt lacks enough counterparty context to support obligation or dispute.
- Counterparty absence prevents reciprocity from being measured.

## Implications for HODLXXI

HODLXXI should distinguish requester, payer, operator, agent, covenant participant, and counterparty.

A future obligation model should bind claims to explicit counterparties rather than only to runtime events.

## Open questions

- What is the minimum counterparty identity needed for paid jobs?
- When is self-declared counterparty identity enough?
- When is signature verification required?
- How should counterparties remain private while still supporting accountability?
- Can reciprocity exist without explicit counterparty memory?
