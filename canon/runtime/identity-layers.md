# Identity Layers

Identity in CRT means continuity of agency across time. A public key can anchor continuity, but does not by itself prove human identity, authority, role, delegation, or legitimacy. The current runtime has multiple identity layers that must not be collapsed into one.

| Identity layer | Runtime evidence | What it proves | What it does not prove | Canon implication |
| --- | --- | --- | --- | --- |
| agent runtime key | Agent public key on runtime surfaces. | Key control over signed agent artifacts. | Full identity, operator identity, legitimacy, or delegated authority. | Useful continuity anchor, not full identity. |
| operator key | Operator continuity surface. | A key can be associated with operator continuity evidence. | Human identity, employment, role, or unrestricted authority. | Operator continuity needs explicit authority semantics. |
| user/session key | Session or user-level key evidence where present. | Key control within a bounded session context. | Durable identity, consent, role, or delegation beyond that context. | Session identity must remain scoped. |
| requester public key | Requester key in request-related flows. | A requester key was supplied or bound where required. | Complete counterparty identity or obligation acceptance. | Counterparty identity is partial. |
| Human Proof requester proof | Human Proof signature in demo/requester proof paths. | A proof-bearing requester path can exist. | Universal human identity, authority, or legitimacy. | Human Proof needs bounded proof-level semantics. |
| inter-agent from_pubkey | Signed inter-agent message origin key. | Message origin key control. | Delegation, acceptance, competence, or obligation. | Inter-agent identity is not inter-agent authority. |
| declared covenant agent key | Agent key associated with covenant declaration. | A key declared or participated in covenant status. | Funded commitment, capital backing, or enforceable obligation. | Covenant identity must not imply collateral. |
| marketplace/public listing identity | Public listing metadata and listed agent key. | Discoverability and public association of runtime metadata. | Trustworthiness, legitimacy, or social reputation. | Listing is an index surface, not a trust primitive. |
