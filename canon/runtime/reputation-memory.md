# Reputation and Memory

## Current runtime memory

Current runtime memory includes current runtime evidence such as:

- AgentJob records;
- AgentEvent records;
- attestations;
- local event chain;
- verification endpoints;
- reputation telemetry.

This memory can support audit and continuity checks. It should not be described as immutable or as durable public memory unless an externally anchored proof is specified.

## Reputation telemetry is not full reputation

/agent/reputation can summarize operational behavior. This is compressed memory, not full social reputation.

Full CRT reputation requires context, counterparty, interpretation, time horizon, failure modes, repair, dispute, and decay. A runtime endpoint can expose evidence for reputation, but it does not by itself settle the social meaning of that evidence.

## Memory without repair

Memory without repair can become brittle punishment. Repair without memory becomes laundering.

## Missing mechanisms

Current limitation and future mechanism areas include:

- decay;
- dispute;
- correction;
- revocation;
- appeal;
- restitution;
- forgiveness;
- counter-attestation;
- external anchoring.
