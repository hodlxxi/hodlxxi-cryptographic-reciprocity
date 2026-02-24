# Data Sources, Privacy, and Ethics Boundaries

## Potential data sources
1. Public blockchain transaction/script metadata.
2. Descriptor-derived lock structure summaries (where lawful and consented).
3. Application-level event logs (simulation and test environments).
4. Survey or experimental participant data (opt-in only).

## Privacy boundaries
- Do not publish raw identity-linked financial data without explicit consent.
- Prefer aggregated, k-anonymous summaries.
- Separate research identifiers from operational identifiers.
- Minimize retained fields and retention duration.

## Ethics principles
- Proportionality: collect only what is needed for stated hypothesis tests.
- Transparency: document preprocessing and exclusion criteria.
- Reproducibility with privacy: share synthetic or aggregated derivatives when raw data is sensitive.

## Data governance suggestions
- Data inventory and lineage table.
- Access control tiers.
- Incident response for accidental disclosure.
