# Delivery plan and starter backlog

Proposed planning assumption: one engineer with part-time architecture, security and appliance-owner support. Estimates are elapsed ranges after entry dependencies are met and cover the first NetScaler 14.1 validation target. Additional products and versions require separate estimates and maintenance capacity.

| Milestone | Estimate | Exit |
|---|---|---|
| M0 Kickoff | 2–5 working days | Owners, repository access, IP disposition and delivery baseline confirmed |
| M1 Offline assessment | 1–2 weeks | Fixture-to-report flow and reviewed applicability corpus |
| M2 Read-only lab integration | 1–2 weeks | Authorized collection, sampled parity with operator inventory and safe handling of failures |
| M3 Lab evidence and review | 2–3 weeks | Reviewed control catalog, synthetic regression, recovery rehearsal and evidence review |
| M4 Pilot decision | 1 week | Sponsor, security reviewer and appliance owner accept or defer pilot |

| Ticket | Owner role | Depends on | Acceptance / priority |
|---|---|---|---|
| AVS-01 Project access and ownership | Delivery lead | — | Confirm repo access, named owners, lab sponsor and usage rights. P0 |
| AVS-02 Schemas and fixtures | Architect | — | Version advisory, snapshot and assessment schemas with vendor, product and release train identity. Include valid, missing and conflicting examples. P0 |
| AVS-03 Vendor advisory import | Engineer | AVS-02 | Parse fixed sample advisories, preserve provenance and replay without duplicate revisions. P0 |
| AVS-04 Applicability evaluator | Engineer | AVS-02, 03 | Demonstrate boundary builds, unsupported profiles and indeterminate output. P0 |
| AVS-05 First evidence export | Engineer | AVS-04 | Generate a reviewable report from fixtures without network access. P0 |
| AVS-06 Lab provisioning and inventory | Appliance owner | AVS-01 | Authorize sandbox, confirm licensing, seed standalone and HA profiles where available. P0 |
| AVS-07 Read-only collector | Engineer | AVS-05, 06 | Compare exported fields with manual inventory and confirm writes are denied. P1 |
| AVS-08 Control catalog and synthetic verification | QA lead | AVS-05, 06 | Link approved examples to vendor references and run agreed legitimate traffic suite. P1 |
| AVS-09 Review, expiry and rollback rehearsal | Security reviewer | AVS-08 | Demonstrate revision-bound approval, expiry handling and recovery evidence. P1 |
| AVS-10 Pilot readiness | Product owner | AVS-07, 09 | Publish scorecard, change boundary and signed go/no-go decision. P1 |
| AVS-11 Coverage matrix and adapter contract | Architect | AVS-02 | Define product adapter interfaces, capability gates and unmatched-product indeterminate behavior. P0 |
| AVS-12 Additional NetScaler release train | Engineer | AVS-11, 05 | Select a train through D-07 and pass its assessment corpus; gate discovery and controls separately. P2 |
| AVS-13 First additional vendor product | Engineer | AVS-11, 05 | Select a product through D-07, implement its adapter and publish reviewed capability evidence and limits. P2 |

**Sprint 1 demo.** Run a local fixture through intake, applicability and export. Show a build boundary, a missing input and an advisory revision. Commit schemas, examples and operations notes alongside implementation.

**Working agreements.** Weekly demo and risk review. A ticket is done when acceptance criteria pass, evidence is reviewable, relevant operational docs are updated, and open limitations are recorded. Verify PR checks and protection settings once repo access is available. Sprint estimates exclude procurement and production change windows.
