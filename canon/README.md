# CRT Canon

CRT Canon is the working knowledge corpus of Cryptographic Reciprocity Theory.

It is not a white paper or doctrine. It is a falsifiable canon: a structured body of
definitions, observations, hypotheses, counterarguments, historical analogies, design
implications, and tests for HODLXXI.

## Central question

Can durable cooperation emerge from cryptographically remembered reciprocal commitments
among humans and future AI agents without relying on centralized authority?

## Rule Zero

No claim in CRT Canon is protected from falsification.

Every chapter must answer: How could this be false?

## Relationship to HODLXXI

HODLXXI is not the theory itself. HODLXXI is experimental infrastructure for testing
whether the theory survives contact with real humans, capital, identity, memory,
incentives, reputation, forgiveness, and failure.

Runtime mechanisms should be traceable back to Canon claims. If a mechanism cannot point
to a theoretical origin, it is not yet justified. If a Canon claim cannot suggest
observable behavior, it is not yet testable.

## Maintenance note

Canon is a falsifiable research corpus, not doctrine. Changes should preserve the
question, evidence, limits, and falsification posture of each document rather than
treating any claim as protected belief.

Every chapter should preserve these sections: Question, Scope, Observations,
Claim, Non-claims, Working theory, Runtime evidence, Counterarguments,
Historical analogies, Failure modes, Implications for HODLXXI, Falsification,
and Open questions.

Runtime mechanisms must not claim stronger meaning than the Canon supports. A
runtime surface may prove an event, signature, payment, receipt, constraint, or
other bounded fact without proving human meaning, consent, legitimacy, loyalty,
forgiveness, obligation, authority, or trust.

## Maintenance checks

Check local Canon Markdown links before changing Canon structure:

```bash
python scripts/check_canon_links.py
```

## Structure

- [Charter](CHARTER.md)
- [Chapter template](TEMPLATE.md)
- [Canon index](INDEX.md)
- [Volume I: Foundations](volumes/01-foundations.md)
- [Volume II: Human Nature](volumes/02-human-nature.md)
- [Volume III: Repeated Games](volumes/03-repeated-games.md)
- [Volume IV: Cryptographic Primitives](volumes/04-cryptographic-primitives.md)
- [Volume V: Institutions](volumes/05-institutions.md)
- [Volume VI: AI Agents](volumes/06-ai-agents.md)
- [Volume VII: HODLXXI](volumes/07-hodlxxi.md)

## Runtime linkage

The runtime linkage layer maps Canon claims to actual HODLXXI mechanisms and explicitly
records what those mechanisms do not prove.

- [Runtime linkage overview](runtime/README.md)
- [Runtime non-claims](runtime/non-claims.md)
- [Identity layers](runtime/identity-layers.md)
- [Receipts](runtime/receipts.md)
- [Reputation and memory](runtime/reputation-memory.md)
- [Missing runtime mechanisms](runtime/missing-mechanisms.md)
