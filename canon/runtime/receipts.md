# Receipts

## What a receipt is

A receipt is signed runtime evidence that a particular agent key recorded a state transition involving a job, request hash, payment hash, result hash, timestamp, and event linkage.

## What a receipt can prove

- agent key signed the receipt payload;
- runtime recorded the job state;
- receipt binds job_type/request_hash/payment_hash/result_hash/timestamp;
- receipt can be verified later;
- receipt can support event memory.

## What a receipt does not prove

- human meaning;
- obligation fulfillment;
- output quality;
- requester satisfaction;
- dispute absence;
- legal identity;
- delegated authority;
- external anchoring;
- forgiveness or repair.

## Event proof vs obligation proof

A receipt is an event proof. It is not an obligation proof unless the obligation, counterparty, acceptance criteria, breach condition, and remedy are explicitly modeled.

## Implications for HODLXXI

Future receipt versions may need:

- requester identity binding;
- obligation reference;
- acceptance criteria;
- dispute/correction state;
- repair/restitution linkage;
- external anchoring.
