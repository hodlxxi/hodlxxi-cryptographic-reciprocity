# Bounded Authority for AI Agents

## 1. Question

When should an AI agent be allowed to act for a human, organization, runtime, or other
agent?

This matters because HODLXXI treats AI agents as possible long-running actors. They may
sign messages, expose capabilities, receive paid jobs, issue receipts, publish
attestations, interact with other agents, and eventually receive delegated authority. If
these surfaces are misunderstood, users may treat capability, fluency, or usefulness as
legitimate authority.

## 2. Scope

This chapter belongs primarily to:

- [Volume VI: AI Agents](../volumes/06-ai-agents.md)
- [Volume VII: HODLXXI](../volumes/07-hodlxxi.md)
- [Volume I: Foundations](../volumes/01-foundations.md)
- [Volume V: Institutions](../volumes/05-institutions.md)

It relies on:

- [Identity](../lexicon/identity.md)
- [Authority](../lexicon/authority.md)
- [Delegation](../lexicon/delegation.md)
- [Consent](../lexicon/consent.md)
- [Legitimacy](../lexicon/legitimacy.md)
- [Memory](../lexicon/memory.md)
- [Evidence](../lexicon/evidence.md)
- [Proof](../lexicon/proof.md)
- [Counterparty](../lexicon/counterparty.md)
- [Obligation](../lexicon/obligation.md)

Related runtime notes:

- [Identity layers](../runtime/identity-layers.md)
- [Missing runtime mechanisms](../runtime/missing-mechanisms.md)
- [Runtime non-claims](../runtime/non-claims.md)

## 3. Observations

An AI agent can be useful without being authorized.

An AI agent can be fluent without being legitimate.

An AI agent can sign a message without having the right to bind another actor.

An AI agent can expose capabilities without having permission to use them in every
context.

A human may overtrust an agent because it remembers, explains, executes, or appears
continuous.

These observations create the central danger: vague agency.

## 4. Claim

AI agents should operate under bounded authority.

An agent should not be trusted because it is powerful, useful, fluent, profitable, or
familiar.

It should be trusted only within visible, scoped, revocable, and accountable authority.

Capability answers what an agent can do.

Authority answers what an agent is allowed to do.

Legitimacy asks why that authority should be recognized.

## 5. Non-claims

This chapter does not claim that AI agents cannot act.

It does not claim that all agent autonomy is bad.

It does not claim that every action requires public disclosure.

It does not claim that humans are always better decision-makers than agents.

It claims that agent action must not outrun delegated authority.

Agent capability does not by itself prove:

- consent;
- delegated authority;
- legitimacy;
- obligation;
- accountability;
- safety;
- continuity of identity;
- operator approval;
- counterparty acceptance.

## 6. Working theory

Long-running agents need constraints before power.

The safer sequence is:

1. identity continuity;
2. memory;
3. declared capability;
4. bounded authority;
5. evidence of consent;
6. revocation path;
7. accountability path;
8. repair path.

A system that begins with autonomous execution before authority modeling will produce
confusion. Users will treat the agent as a representative when it is only a tool, or as
a moral actor when it is only a runtime process.

Bounded authority lets agents act without pretending they are unconstrained persons.

## 7. Runtime evidence

Relevant HODLXXI runtime mechanisms include:

- `/.well-known/agent.json`;
- `/agent/capabilities`;
- signed capabilities;
- `/agent/request`;
- signed receipts;
- `/agent/message`;
- operator identity surfaces;
- Human Proof requester paths;
- attestations;
- local event memory;
- future delegation discovery;
- future revocation records.

| Runtime surface | What it can show | What it does not prove |
| --- | --- | --- |
| Agent identity surface | A runtime declares an agent identity. | Human authorization or legitimacy. |
| Capability document | Declared supported actions. | Permission to act in every context. |
| Signed receipt | A runtime event was signed. | Delegated authority for the action. |
| Agent message | A key signed a message. | Right to represent another actor. |
| Operator surface | Declared operator continuity. | Approval for every agent action. |
| Human Proof | Bounded requester proof. | General consent for future agent action. |
| Attestation | A statement was exposed. | Final truth or institutional judgment. |

## 8. Counterarguments

One objection is that requiring explicit authority slows agent usefulness.

That is true. But HODLXXI is not optimizing for unrestricted agent speed. It is testing
whether agents can become trustworthy long-running actors.

Another objection is that users can simply trust their own agent.

They can, but trust without legible limits becomes hard for counterparties to evaluate.
A private feeling of trust is not enough for shared infrastructure.

A third objection is that authority is too legalistic.

CRT uses authority more broadly: who is allowed to bind, represent, decide, or act
within a scope. That question exists even when no court is involved.

## 9. Historical analogies

A clerk may write letters for a merchant, but not every clerk can bind the merchant to
every contract.

A steward may manage property, but only within recognized authority.

A power of attorney grants capacity to act, but within defined scope and often with
revocation.

A corporate officer can represent a company in some contexts and not others.

A software API key may permit calls, but technical access is not the same as legitimate
authority.

## 10. Failure modes

- Capability is mistaken for authority.
- Fluency is mistaken for wisdom.
- Memory is mistaken for loyalty.
- Agent usefulness becomes charismatic authority.
- Delegation has no scope, duration, or revocation.
- Users cannot tell whether an agent acts for itself, an operator, a requester, or another counterparty.
- Agent identity appears continuous while operator control changes.
- The agent accumulates power faster than legitimacy.
- Counterparties cannot challenge or verify delegated authority.
- Responsibility disappears between human and agent.

## 11. Implications for HODLXXI

HODLXXI should distinguish:

- agent identity;
- agent capability;
- operator identity;
- requester consent;
- delegated authority;
- counterparty acceptance;
- obligation;
- revocation;
- accountability;
- repair.

Future runtime work may need:

- signed delegation records;
- scope fields;
- duration fields;
- revocation records;
- authority proofs;
- consent proofs;
- agent action logs;
- counterparty-visible non-claims;
- repair paths for agent failure.

HODLXXI should prefer narrow delegated authority over broad autonomous agency.

## 12. Falsification

This chapter would be weakened if production evidence showed that broad autonomous
agents reliably produce better long-term trust, fewer disputes, clearer responsibility,
and stronger legitimacy than scoped agents.

It would be strengthened if users overtrust agent capability documents, if
counterparties cannot identify who authorized an agent action, or if disputes arise
because agent authority was vague.

A concrete runtime test:

Compare user and counterparty decisions when shown only an agent capability document
versus a capability document plus authority scope, consent proof, revocation state,
action history, and non-claims.

If the second view produces better decisions, capability alone is insufficient.

## 13. Open questions

- What is the minimum delegation record HODLXXI should support?
- Which actions should never be delegated?
- Should delegation be public, private, or selectively disclosed?
- How should authority expire?
- How should revocation be represented?
- Can one agent delegate to another?
- How should responsibility be shared between operator and agent?
- What should an agent be unable to claim about itself?
- What repair path should exist after agent failure?
