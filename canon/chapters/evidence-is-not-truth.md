# Evidence Is Not Truth

## 1. Question

What does evidence in CRT make possible, and what must it not be mistaken for?

This matters because HODLXXI preserves receipts, signatures, attestations, event chains,
payments, runtime checks, reputation-adjacent memory, and Human Proof signals. These
surfaces can support interpretation, dispute, repair, verification, and reputation. They
can also be overread as truth, justice, legitimacy, satisfaction, or moral standing.

## 2. Scope

This chapter belongs primarily to:

- [Volume I: Foundations](../volumes/01-foundations.md)
- [Volume IV: Cryptographic Primitives](../volumes/04-cryptographic-primitives.md)
- [Volume VI: AI Agents](../volumes/06-ai-agents.md)
- [Volume VII: HODLXXI](../volumes/07-hodlxxi.md)

It relies on:

- [Evidence](../lexicon/evidence.md)
- [Proof](../lexicon/proof.md)
- [Verification](../lexicon/verification.md)
- [Receipt](../lexicon/receipt.md)
- [Attestation](../lexicon/attestation.md)
- [Memory](../lexicon/memory.md)
- [Reputation](../lexicon/reputation.md)
- [Legitimacy](../lexicon/legitimacy.md)
- [Identity](../lexicon/identity.md)

Related Canon chapters:

- [Receipts as Event Proofs](receipts-as-event-proofs.md)
- [Identity Is Not Key Control](identity-is-not-key-control.md)
- [Reputation Is Not a Score](reputation-is-not-a-score.md)
- [Memory Before Forgiveness](memory-before-forgiveness.md)
- [Bounded Authority for AI Agents](bounded-authority-for-ai-agents.md)
- [Obligation Is Not Payment](obligation-is-not-payment.md)
- [Commitment Is Not Lockup](commitment-is-not-lockup.md)
- [Reciprocity Is Not Transaction](reciprocity-is-not-transaction.md)

Related runtime notes:

- [Runtime claims matrix](../runtime/claims-matrix.md)
- [Runtime non-claims](../runtime/non-claims.md)
- [Runtime receipts](../runtime/receipts.md)
- [Reputation and memory](../runtime/reputation-memory.md)
- [Canon / Runtime Gap Register](../runtime/gap-register.md)

## 3. Observations

Evidence is retained information. It may be a receipt, log entry, signature, payment
record, attestation, event-chain link, verification output, observation, message, or
runtime telemetry.

Evidence matters because judgment without retained information becomes guesswork,
forgetting, or power. But retained information does not interpret itself.

A valid signature can prove that a key signed a statement under a verification rule. It
does not prove that the statement is true, that the signer was legitimate, that the
statement was fairly obtained, or that the interpretation attached to the statement is
just.

An event chain can preserve continuity. It does not prove justice.

A receipt can preserve an event. It does not prove satisfaction.

A Human Proof signal can support a bounded participation claim. It does not prove full
personhood, moral legitimacy, uniqueness across all contexts, or authority.

## 4. Claim

Evidence is retained information that can support, weaken, or revise interpretation; it
is not truth by itself.

Evidence becomes useful when a community, counterparty, verifier, runtime, court,
mediator, agent, or participant can inspect what it records, what rule checked it, what
context is missing, what contradicts it, and what stronger claim it does not support.

The purpose of evidence in CRT is not to remove judgment. It is to make judgment less
arbitrary, more contestable, more memory-preserving, and more falsifiable.

## 5. Claim IDs

| Claim ID | Existing claim |
| --- | --- |
| `CRT-EVIDENCE-001` | Evidence is retained information that can support, weaken, or revise interpretation; it is not truth by itself. |

## 6. Non-claims

This chapter does not claim that evidence is weak, optional, or merely subjective.

It claims that evidence has boundaries.

Evidence does not by itself prove:

- truth;
- legitimacy;
- justice;
- satisfaction;
- full identity;
- moral standing;
- authority;
- consent;
- obligation fulfillment;
- trustworthy character;
- complete context;
- final interpretation.

The chapter also does not claim that human judgment is always superior to runtime
verification. Human judgment can be biased, corrupt, forgetful, or captured. The claim is
that verification and judgment answer different questions.

## 7. Working theory

CRT should treat evidence as a retained input to interpretation, not as the end of
interpretation.

The safer theory is:

1. Evidence preserves something that can later be inspected.
2. Proof checks evidence against a defined rule.
3. Verification reports whether a rule was satisfied.
4. Interpretation asks what the evidence means in context.
5. Judgment decides what should follow, including trust, repair, dispute, forgiveness,
   refusal, or escalation.

This creates several important boundaries:

| Boundary | Safer interpretation |
| --- | --- |
| Evidence vs truth | Evidence can support a truth claim, weaken it, or revise it. It is not the truth claim itself. |
| Proof vs evidence | Proof is evidence that satisfies a defined verification rule; other evidence may remain relevant. |
| Receipt vs satisfaction | A receipt records a bounded event; it does not prove a human accepted or valued the outcome. |
| Attestation vs truth | An attestation records that an issuer made or exposed a claim; it does not settle whether the claim is true. |
| Event-chain continuity vs justice | Continuity can show ordering or internal consistency; it does not prove fairness, repair, or rightful outcome. |
| Signed statement vs legitimacy | A signature can bind a key to a statement; it does not prove the signer had standing, authority, or moral right. |
| Observed behavior vs interpreted meaning | Behavior can be remembered; its meaning may depend on expectation, context, role, harm, and response. |
| Evidence accumulation vs reputation laundering | More evidence can improve judgment, but accumulated artifacts can also launder status if context and contradiction disappear. |
| Evidence preservation vs human judgment | Preservation makes judgment auditable; it does not remove the need for judgment. |

The stronger the downstream claim, the more explicit the missing context must become.

## 8. Runtime evidence

Relevant HODLXXI runtime mechanisms include:

- signed receipts;
- `/agent/verify/<job_id>`;
- Lightning invoices and settlement evidence;
- attestations;
- local AgentEvent chains;
- `/agent/reputation` and reputation-adjacent telemetry;
- Human Proof requester or participant paths;
- agent, requester, operator, and covenant participant keys;
- marketplace listings and interactions;
- runtime rule checks.

| Surface | Bounded evidence it can provide | Stronger meaning it must not claim |
| --- | --- | --- |
| Signed receipt | A runtime key recorded a bounded event. | Satisfaction, fulfilled obligation, justice, or trustworthiness. |
| Verification endpoint | A defined rule accepted a receipt or job artifact. | Total social meaning of the event. |
| Lightning payment | Cost, invoice, or settlement evidence under specific payment rules. | Obligation, consent, repair, or acceptance. |
| Attestation | An issuer made a claim in a context. | Truth, legitimacy, final judgment, or absence of contradiction. |
| Event chain | Local continuity or internal consistency. | External truth, justice, forgiveness, or repair. |
| Signed statement | A key signed bytes or a structured claim. | Authority, legitimacy, rightful representation, or correctness. |
| Reputation telemetry | Remembered behavior and summaries. | Moral character, universal trust, or a complete reputation score. |
| Human Proof | Bounded evidence relevant to human-linked participation. | Full personhood, uniqueness everywhere, moral legitimacy, or authority. |
| Runtime verification | Rule satisfaction under known inputs. | Complete truth, complete context, or social acceptance. |

## 9. Counterarguments

One objection is that systems need clear facts, not endless interpretation.

CRT agrees that systems need clear facts. The boundary is that facts become dangerous
when users infer unrecorded meanings from them. A verified receipt is clearer and more
useful when it also states what it does not verify.

Another objection is that enough evidence eventually becomes truth.

Accumulation can strengthen confidence, but it can also magnify bias, bury
contradictions, or create reputation laundering. More artifacts do not automatically mean
better interpretation if the artifacts share the same blind spot.

A third objection is that human judgment is unreliable, so runtime verification should
replace it.

Runtime verification can reduce some forms of arbitrariness. It cannot decide every
question of context, harm, legitimacy, consent, fairness, personhood, or repair unless
those questions are reduced to explicit rules, and that reduction is itself a judgment.

## 10. Historical analogies

A signed contract is evidence of agreement. It may still be disputed because of fraud,
duress, capacity, ambiguity, unconscionability, breach, or changed circumstances.

A court exhibit is evidence. It is not the verdict.

A notarized document is evidence that a process occurred. It does not prove that the
underlying statement is true.

A chain-of-custody log can support confidence in handling. It does not prove that the
outcome is just.

A ledger can preserve entries. It does not decide whether the entries were rightful,
complete, or fairly interpreted.

## 11. Failure modes

- Evidence is displayed as truth.
- A proof result hides the evidence boundary.
- A receipt is treated as satisfaction.
- An attestation is treated as settled truth.
- A healthy event chain is treated as justice.
- A signed statement is treated as legitimacy.
- Observed behavior is assigned meaning without context.
- Evidence accumulation becomes reputation laundering.
- Runtime verification replaces rather than informs human judgment.
- Contradictory evidence, revocation, or counter-attestation paths are missing.
- Human Proof is marketed as full personhood or moral legitimacy.
- Reputation collapses cited evidence into a single score.

## 12. Implications for HODLXXI

Every evidence surface should expose what it proves and what it does not prove.

Receipts should remain bounded event evidence. They may support later interpretation,
obligation analysis, dispute, repair, or reputation, but they should not silently become
proof of satisfaction or fulfilled obligation.

Attestations need issuer, context, timestamp, scope, revocation, dispute, and
counter-attestation paths before stronger claims are made from them.

Event chains should not be called truth machines. They can preserve continuity and make
some tampering visible, but they do not by themselves produce justice, repair, or
legitimacy.

Reputation should cite evidence without collapsing judgment into a single score. It
should show memory inputs, context, uncertainty, dispute state, decay, repair, and limits.

Human Proof should remain bounded evidence for a defined participation or requester
claim. It should not be represented as full personhood, universal uniqueness, moral
legitimacy, legal identity, or authority.

Runtime verification should verify rules, not total social meaning. A verifier should
make visible the checked rule, inputs, outputs, missing context, and non-claims.

## 13. Falsification

This chapter would be weakened if users and counterparties consistently made accurate
trust, obligation, legitimacy, satisfaction, and repair judgments from bare evidence
surfaces without additional context, non-claims, contradiction paths, or human review.

It would be strengthened if users overread valid proofs, receipts, attestations, event
chains, Human Proof signals, or reputation telemetry as truth, justice, legitimacy,
satisfaction, personhood, or moral standing.

Concrete runtime tests:

1. Show users a verified receipt alone, then a verified receipt with explicit non-claims,
   obligation context, acceptance criteria, and dispute state. If the second view
   improves decisions, bare receipt evidence is insufficient.
2. Show users an attestation alone, then the same attestation with issuer context,
   revocation status, counter-attestations, and scope. If the second view changes
   judgments, attestation is not truth by itself.
3. Show users event-chain health alone, then chain health with repair, dispute, and
   external anchoring context. If the second view changes judgments, continuity is not
   justice.
4. Show users reputation summaries with and without cited evidence and uncertainty. If
   cited evidence changes decisions, reputation must not collapse into score.

## 14. Open questions

- What is the minimum evidence-boundary metadata every runtime surface should expose?
- Which evidence boundaries should be machine-readable versus user-facing prose?
- How should contradiction, revocation, and counter-attestation paths be represented?
- When should evidence decay, and when should it remain durable?
- Which evidence should be public, private, or selectively disclosed?
- What runtime UI best prevents users from confusing proof with truth?
- How can Human Proof remain useful without becoming personhood theater?
- What forms of evidence accumulation create reputation laundering?
