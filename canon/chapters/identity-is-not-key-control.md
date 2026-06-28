# Identity Is Not Key Control

## 1. Question

What does control of a cryptographic key prove about identity?

This matters because HODLXXI uses public keys, signatures, requester proofs, operator surfaces, agent capabilities, covenant declarations, and inter-agent messages. These mechanisms can anchor continuity, but they can also be overread as proof of human identity, role, authority, consent, or legitimacy.

## 2. Scope

This chapter belongs primarily to:

- [Volume I: Foundations](../volumes/01-foundations.md)
- [Volume IV: Cryptographic Primitives](../volumes/04-cryptographic-primitives.md)
- [Volume VI: AI Agents](../volumes/06-ai-agents.md)
- [Volume VII: HODLXXI](../volumes/07-hodlxxi.md)

It relies on:

- [Identity](../lexicon/identity.md)
- [Memory](../lexicon/memory.md)
- [Evidence](../lexicon/evidence.md)
- [Proof](../lexicon/proof.md)
- [Verification](../lexicon/verification.md)
- [Counterparty](../lexicon/counterparty.md)
- [Authority](../lexicon/authority.md)
- [Delegation](../lexicon/delegation.md)
- [Consent](../lexicon/consent.md)
- [Legitimacy](../lexicon/legitimacy.md)

Related runtime notes:

- [Identity layers](../runtime/identity-layers.md)
- [Runtime non-claims](../runtime/non-claims.md)

## 3. Observations

A public key can be stable across time.

A signature can show that the holder of a corresponding private key authorized a message under a defined signing rule.

A requester proof can bind a key to a particular request.

An operator key can anchor continuity for a public runtime surface.

An agent key can sign capabilities, receipts, or messages.

But none of these alone proves the full identity of a human, the social role of an actor, the legitimacy of authority, or the meaning of consent.

## 4. Claim

Key control is evidence of control over a cryptographic capability.

It is not full identity.

A public key can anchor continuity, but identity in CRT requires continuity of agency across time, interpretable behavior, memory, role context, and recognized constraints.

## Claim IDs

| Claim ID | Existing claim |
| --- | --- |
| `CRT-IDENTITY-001` | Key control is evidence of control over a cryptographic capability; it is not full identity. |

## 5. Non-claims

This chapter does not claim that keys are unimportant.

It does not claim that signatures are weak.

It does not claim that public keys cannot anchor identity systems.

It claims only that key control must not be collapsed into full identity.

Key control does not by itself prove:

- legal identity;
- human identity;
- role;
- counterparty context;
- consent;
- authority;
- delegation;
- legitimacy;
- trustworthiness;
- moral responsibility;
- continuity of intention.

## 6. Working theory

Identity is continuity through time.

A key can help maintain continuity because it provides a stable cryptographic reference point. But the key is only one layer.

CRT identity requires at least three layers:

1. cryptographic continuity;
2. behavioral memory;
3. contextual interpretation.

A system that has only the first layer can verify signatures but cannot safely infer social meaning.

A long-running actor becomes more identifiable when key continuity is joined with remembered behavior, explicit roles, constrained authority, visible delegation, and meaningful counterparty relationships.

## 7. Runtime evidence

Relevant HODLXXI runtime mechanisms include:

- agent public key;
- operator public key;
- requester public key;
- Human Proof requester paths;
- signed receipts;
- signed capabilities;
- inter-agent messages;
- covenant participant keys;
- marketplace identity surfaces;
- local event memory.

| Runtime layer | What it can show | What it does not prove |
| --- | --- | --- |
| Agent key | A runtime key signed a statement. | Full agent legitimacy or delegated authority. |
| Operator key | A declared operator key exists. | That every action is authorized by the operator. |
| Requester key | A key is associated with a request. | Legal identity or payer identity. |
| Human Proof | A requester can sign a bounded request. | Complete counterparty model. |
| Inter-agent message | A key signed a message. | Authority to act on behalf of another actor. |
| Covenant key | A key appears in a covenant context. | Funding, sincerity, or social obligation. |
| Marketplace identity | A listing or actor can be represented. | Trustworthiness or consent beyond the listing. |

## 8. Counterarguments

One objection is that a public key is the only identity needed in a cryptographic system.

That may be true for narrow protocol validity, but CRT is not only about protocol validity. It studies trust, obligation, memory, reciprocity, forgiveness, and legitimacy.

Another objection is that adding identity context weakens privacy.

This is a serious risk. The answer is not to expose everything. The answer is to separate identity layers and support selective disclosure.

A third objection is that human identity is too messy to model.

Some parts may remain social, but the system must still say what key control does not prove.

## 9. Historical analogies

A seal on a letter can identify a household or office, but it does not always prove who physically used it, whether the action was authorized, or whether the message was legitimate.

A bank card can prove possession and authorization under narrow payment rules, but it does not prove the moral identity of the user.

A username can persist across time, but the account can be sold, shared, stolen, abandoned, or used performatively.

A passport can identify a legal person, but it does not prove trustworthiness, authority in a specific context, or fulfilled obligation.

## 10. Failure modes

- Key control is mistaken for human identity.
- Signature validity is mistaken for consent.
- Agent capability is mistaken for authority.
- Operator declaration is mistaken for continuous authorization.
- Requester key is mistaken for payer, beneficiary, or counterparty.
- A key is transferred, compromised, shared, or abandoned.
- A sybil actor resets identity by creating a new key.
- Reputation attaches to a key without enough context.
- Privacy is destroyed by overcorrecting toward full identity disclosure.

## 11. Implications for HODLXXI

HODLXXI should preserve separate identity layers.

It should distinguish:

- key control;
- account/session continuity;
- requester identity;
- payer identity;
- operator identity;
- agent identity;
- counterparty role;
- authority;
- consent;
- delegation;
- legitimacy.

The system should expose what each identity surface proves and what it does not prove.

Future runtime work should avoid representing a public key as a complete identity object unless the claim is explicitly bounded.

## 12. Falsification

This chapter would be weakened if production evidence showed that key control alone reliably predicts continuity of behavior, authority, consent, and trustworthy action across long horizons.

It would be strengthened if users overread public keys as people, signatures as consent, capability documents as authority, or requester keys as complete counterparties.

A concrete runtime test:

Compare user decisions when shown only a public key and signature versus the same key plus role, proof level, event history, authority scope, consent boundary, and known non-claims.

If the second view produces better trust decisions, key control alone is insufficient as an identity primitive.

## 13. Open questions

- What is the minimum useful identity layer for paid jobs?
- Should requester identity become first-class in runtime storage?
- How should identity remain private while still supporting accountability?
- When is a public key enough?
- When is Human Proof enough?
- How should compromised or abandoned keys be represented?
- How should agent identity survive model, runtime, or operator changes?
- What should HODLXXI refuse to infer from key control alone?
