# Delegation

## Definition

Delegation is the bounded transfer of authority from one actor to another for a defined
purpose.

In CRT, delegation is not the same as access, capability, automation, or general trust.

## Operational meaning

Delegation should specify:

- delegator;
- delegate;
- scope;
- duration;
- permitted actions;
- evidence of consent;
- revocation path;
- accountability path.

## What delegation is not

Delegation is not unrestricted autonomy.

Delegation is not a vague instruction.

Delegation is not proven merely by an agent capability document.

Delegation is not proven merely by a signed message unless the signed message contains
the relevant scope.

## Observable behavior

In HODLXXI, delegation may relate to agent capabilities, operator-agent relationships,
inter-agent messages, signed authorization statements, Human Proof requester paths,
future discovery surfaces, and future revocation records.

## Failure modes

- Capability is mistaken for permission.
- Delegation has no clear scope or expiration.
- Revocation is unclear.
- Responsibility disappears between operator and agent.
- A fluent agent is trusted beyond its actual authority.

## Implications for HODLXXI

HODLXXI should prefer bounded delegation over vague agency.

Future runtime mechanisms should distinguish what an agent can do from what it is
allowed to do.

## Open questions

- What should a delegation record contain?
- Should delegation be public, private, or selectively disclosed?
- How should revocation be represented?
- Can delegation be chained across agents?
- Which actions should require renewed consent?
