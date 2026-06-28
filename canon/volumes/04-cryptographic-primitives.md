# Volume IV: Cryptographic Primitives

## Purpose

This volume studies cryptographic tools as instruments for memory, accountability,
public verification, timekeeping, and durable commitment.

It does not treat trust as authentication.

## Core question

What can cryptographic evidence make visible, and what human meaning remains unproven
even when the cryptographic evidence is valid?

## Scope

This volume covers digital signatures, hashes, public keys, Bitcoin, Lightning,
receipts, attestations, proofs, covenants, time locks, public verification, and event
chains.

It studies these tools as behavioral constraints and evidence surfaces, not as
substitutes for human judgment.

## What this volume claims

- Cryptography can make statements, events, and state transitions verifiable.
- Public keys can anchor continuity, but they do not equal full identity.
- Receipts can prove that an event was recorded, but not that an obligation was fulfilled.
- Payment can create cost, but cost is not automatically commitment.
- Bitcoin time and Lightning payments can support accountability, but they do not preserve meaning by default.
- Public verification can reduce some ambiguity while creating new forms of ritual and overclaim.

## What this volume does not claim

- It does not claim a valid signature proves human meaning.
- It does not claim a receipt proves satisfaction, quality, or obligation fulfillment.
- It does not claim payment proves trustworthiness.
- It does not claim a public key is a person.
- It does not claim a local event chain is immutable public memory.
- It does not claim a covenant declaration is funded commitment.
- It does not claim proof of funds is proof of cooperative character.

## Key Lexicon terms

- [Identity](../lexicon/identity.md)
- [Memory](../lexicon/memory.md)
- [Promise](../lexicon/promise.md)
- [Commitment](../lexicon/commitment.md)
- [Obligation](../lexicon/obligation.md)
- [Reputation](../lexicon/reputation.md)
- [Legitimacy](../lexicon/legitimacy.md)

Future terms likely needed here include proof, evidence, verification, receipt,
attestation, signature, anchor, covenant, time lock, and event proof.

## Runtime relevance

This volume directly maps to current HODLXXI runtime mechanisms:

- signed capabilities;
- signed receipts;
- `/agent/verify/<job_id>`;
- `/agent/attestations`;
- `/agent/chain/health`;
- Lightning invoice/payment flow;
- Human Proof requester signatures;
- proof-of-funds surfaces;
- covenant declaration surfaces;
- inter-agent signed messages.

The runtime linkage layer records what these mechanisms do and do not prove.

## Failure modes

- Authentication is mistaken for trust.
- Event proof is mistaken for obligation proof.
- Key control is mistaken for identity.
- Payment is mistaken for commitment.
- Proof of funds is mistaken for trustworthiness.
- Local chain continuity is mistaken for external anchoring.
- Cryptographic ritual replaces real behavioral constraint.

## Initial chapter backlog

- Receipts are not commitments
- Event proof vs obligation proof
- Key control is not identity
- Proof, evidence, and verification
- Signatures and human meaning
- Payment as cost, not commitment
- Bitcoin time as commitment substrate
- Attestations and their limits
- Public verification and ritual behavior
- Covenants as behavioral constraints

## Falsification focus

This volume fails wherever cryptographic proof creates ritual without real constraint,
identity without continuity, or verification without trustworthiness.

It also fails wherever HODLXXI users reliably overread valid proofs as social facts that
the system did not actually model.

## Open questions

- Which kinds of human meaning can be modeled without destroying them?
- What should a future obligation proof require beyond a receipt?
- When should event memory be externally anchored?
- How should proof systems expose non-claims to ordinary users?
- What cryptographic evidence should HODLXXI refuse to interpret socially?
