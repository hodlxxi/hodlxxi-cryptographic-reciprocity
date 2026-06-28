# Mechanisms

## Purpose

This folder contains Canon-level mechanism specifications.

Mechanism specs are not runtime implementations. They define conceptual structures required before HODLXXI can safely make stronger claims about obligation, delegation, repair, reciprocity, identity continuity, and reputation.

## What mechanism specs are

A mechanism spec is a bridge between Canon theory and future runtime design.

It answers:

- What must be represented before a stronger claim is safe?
- What fields or states are minimally required?
- What runtime surfaces may provide evidence?
- What does the mechanism still not prove?
- What failure modes must be tested?

## What mechanism specs are not

Mechanism specs are not:

- APIs;
- database schemas;
- legal contracts;
- moral judgments;
- runtime implementations;
- product promises;
- final truth;
- evidence that the system already works.

## Mechanism stack

| Mechanism | Primary question | Main boundary it protects | Depends on / relates to |
| --- | --- | --- | --- |
| [Minimum Obligation Object v0](obligation-object-v0.md) | What must be represented before HODLXXI can claim an obligation exists? | Payment, receipt, or execution is not obligation. | Receipts, requests, acceptance criteria, breach, remedy, repair. |
| [Minimum Delegation Record v0](delegation-record-v0.md) | What must be represented before an actor or agent can act under delegated authority? | Capability, key control, or signed message is not authority. | Agent identity, operator key, scope, revocation, accountability, obligations. |
| [Repair Lifecycle v0](repair-lifecycle-v0.md) | What must be represented after harm, breach, misuse, dispute, or failure? | Repair is not erasure, forgiveness, refund, or reputation laundering. | Obligations, delegations, affected response, memory policy, reputation. |
| [Reciprocity Pattern v0](reciprocity-pattern-v0.md) | What must be represented before HODLXXI can claim reciprocal cooperation across time? | Reciprocity is not transaction count, payment history, equal exchange, or score. | Repeated events, expectations, asymmetry, repairs, obligations, reputation. |
| [Identity Continuity v0](identity-continuity-v0.md) | What must be represented before HODLXXI can claim identity continuity over time? | Key control, login, endpoint, Human Proof, or reputation is not identity. | Anchors, key purpose, role context, rotation, revocation, recovery. |
| [Contextual Reputation v0](contextual-reputation-v0.md) | What must be represented before HODLXXI can summarize reputation? | Reputation is contextual compressed memory, not a global score. | Memory inputs, obligations, delegations, repairs, reciprocity, identity, disputes. |

## Suggested reading order

1. [Minimum Obligation Object v0](obligation-object-v0.md)
2. [Minimum Delegation Record v0](delegation-record-v0.md)
3. [Repair Lifecycle v0](repair-lifecycle-v0.md)
4. [Reciprocity Pattern v0](reciprocity-pattern-v0.md)
5. [Identity Continuity v0](identity-continuity-v0.md)
6. [Contextual Reputation v0](contextual-reputation-v0.md)

Start with obligation because promises and acceptance criteria are the smallest unit of accountable relation.
Then delegation because agents need bounded authority.
Then repair because failure must not become either erasure or permanent punishment.
Then reciprocity because cooperation is a pattern across time.
Then identity continuity because long-running actors require rotation, revocation, and recovery.
Then contextual reputation because reputation compresses memory from all previous layers.

## Canon boundary

- Event proof is not obligation.
- Capability is not authority.
- Repair is not erasure.
- Reciprocity is not transaction count.
- Key control is not identity.
- Reputation is not a score.

## Runtime implication

These specs should guide future runtime design but should not be treated as already implemented.

A runtime surface should not claim stronger meaning than the corresponding mechanism can represent.

Examples:

- A signed receipt may support an obligation record but does not prove obligation.
- A capabilities endpoint may support a delegation record but does not prove authority.
- A repair record may support reputation context but does not erase memory.
- A repeated event sequence may support reciprocity context but does not prove trust.
- A key or endpoint may support identity continuity but does not prove full identity.
- A reputation summary may compress memory but does not prove moral worth.

## Current mechanism specs

- [Minimum Obligation Object v0](obligation-object-v0.md)
- [Minimum Delegation Record v0](delegation-record-v0.md)
- [Repair Lifecycle v0](repair-lifecycle-v0.md)
- [Reciprocity Pattern v0](reciprocity-pattern-v0.md)
- [Identity Continuity v0](identity-continuity-v0.md)
- [Contextual Reputation v0](contextual-reputation-v0.md)

## Failure-mode focus

Every mechanism must be tested against:

- overclaim;
- laundering;
- score collapse;
- authority confusion;
- identity confusion;
- memory erasure;
- permanent punishment;
- sybil behavior;
- cartel behavior;
- coercive dependency;
- agent theater;
- privacy leakage.

## Open questions

- Which mechanism should become runtime-readable first?
- Which fields should remain human-readable?
- Which fields should be private or selectively disclosed?
- Which mechanisms are too heavy for 21-sat demo jobs?
- Which mechanisms are necessary for marketplace interactions?
- Which mechanisms are necessary before AI agents can act on behalf of humans?
- What should HODLXXI explicitly refuse to claim even after all mechanism specs exist?
