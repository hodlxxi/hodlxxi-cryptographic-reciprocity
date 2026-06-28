# CRT Canon Runtime Linkage Map

This document maps CRT Canon claims to HODLXXI runtime mechanisms.

It is not implementation documentation. It is a falsification bridge between theory and working system behavior.

## Purpose

The Canon should not remain abstract.

Every serious CRT claim should eventually connect to:

1. a runtime mechanism;
2. an observable behavior;
3. a failure mode;
4. a falsification test.

Likewise, every major runtime mechanism should eventually point back to:

1. a Canon volume;
2. a Lexicon term;
3. a reason it exists;
4. a way it could fail.

## Linkage table

| Canon claim | Lexicon terms | Runtime mechanism | Observable behavior | Failure mode | Falsification test |
|---|---|---|---|---|---|
| Trust is a prediction about future behavior under uncertainty. | Trust, Memory, Reputation | Agent jobs, receipts, public verification, reputation surfaces | Users can inspect prior behavior before relying on an agent or operator | Valid records fail to improve actual reliability | Users with access to history do not make better trust decisions than users without history |
| Identity is continuity of agency across time. | Identity, Memory, Legitimacy | Persistent public-key identity, operator key, signed runtime metadata | The same actor can be recognized across sessions, jobs, receipts, and attestations | Key control is mistaken for full identity | Key continuity exists but users still cannot distinguish operator, agent, delegate, or impersonator roles |
| A commitment is a promise made costly to abandon. | Promise, Commitment, Obligation | Paid requests, Lightning invoices, signed receipts, covenant-oriented verification | Actors pay, sign, lock, or otherwise incur cost before claiming completion or seriousness | Cost becomes empty ritual or status theater | Paid actions increase appearance of seriousness but do not correlate with completion, reliability, or accountability |
| Reputation is compressed memory. | Reputation, Memory, Trust | Reputation endpoint, attestations, event history, verification records | Prior behavior is summarized for future decision-making | Reputation becomes a score that hides context | A single reputation summary produces worse decisions than contextual event review |
| Forgiveness is restored cooperation after remembered failure. | Forgiveness, Memory, Reputation | Future repair flows, retryable jobs, corrected attestations, visible restitution | A failed actor can recover only through visible repair or changed constraints | Forgiveness becomes laundering | Actors repeatedly fail, perform shallow repair, and regain trust without changed behavior |
| Legitimacy is recognized authority to bind or represent future behavior. | Legitimacy, Identity, Obligation | Agent discovery, capability statements, delegated authority, operator declarations | Users can see what the agent claims authority to do and who stands behind it | Technical capability is confused with legitimate authority | Users rely on agent actions without understanding delegation, operator authority, or limits |
| Reciprocity can be delayed, asymmetric, and still cooperative. | Reciprocity, Obligation, Trust | Marketplace flows, paid human proof, covenant relationships, attestations | Participants can create durable obligations without immediate equal exchange | Asymmetry becomes exploitation or dependency | Long-lived asymmetric relationships reduce user autonomy or produce systematic extraction |
| Memory must preserve accountability without destroying repair. | Memory, Forgiveness, Reputation | Receipts, event logs, verification endpoints, future decay or repair policies | Records allow accountability while preserving paths for correction | Permanent memory creates brittle exclusion | Minor or repairable failures permanently exclude actors despite later reliable behavior |

## Current runtime mechanisms requiring Canon linkage

These mechanisms should be mapped in more detail in future PRs:

- `/.well-known/agent.json`
- `/agent/capabilities`
- `/agent/skills`
- `/agent/reputation`
- `/agent/attestations`
- `/agent/chain/health`
- `/agent/request`
- `/agent/jobs/<job_id>`
- `/agent/verify/<job_id>`
- Human Proof demo flow
- Lightning invoice and payment receipt flow
- Operator public-key continuity
- Covenant Explorer and covenant verification
- Marketplace trust gates

## Near-term research tasks

1. Create one linkage document per major runtime surface.
2. Add Canon references to runtime documentation without changing runtime behavior.
3. Define which observations can be collected safely without creating surveillance or reputation abuse.
4. Separate cryptographic validity from human meaning in every mechanism.
5. Identify failure cases where the system proves an action but fails to preserve commitment meaning.

## Rule

A runtime feature is not mature until it can answer:

- Which Canon claim does this test?
- Which Lexicon term does this operationalize?
- What behavior should become visible?
- What could go wrong?
- What would make us revise the theory?
