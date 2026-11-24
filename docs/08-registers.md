# Decisions, risks and assumptions

| Decision | Proposed direction | Owner | Due |
|---|---|---|---|
| D-01 Initial release scope | NetScaler 14.1 offline assessment followed by read-only lab discovery | Product owner | M0 |
| D-02 Ownership and license | Confirm project IP and lab entitlements before committing to distribution | Sponsor | M0 |
| D-03 Repository and CI | Inspect repo first, then use its conventions and existing CI | Architect | M0 |
| D-04 Evidence rubric | Use vendor applicability plus synthetic functional results and reviewed configuration evidence | Security reviewer | Before M1 grading |
| D-05 Hosting and model | Choose hosting after data residency and cost review. Model use is optional | Architect | Before shared deployment |
| D-06 Pilot authority | Establish environment, approval roles, change window and support path | Appliance owner | M4 |

| Risk | Level | Owner | Trigger and response |
|---|---|---|---|
| Lab access or licenses delayed | High | Appliance owner | Lab access missing at M0. Continue fixtures and rebaseline integration. |
| Limited safe control coverage | High | Product owner | Low documented-control yield. Review assessment-only positioning and patch workflow value. |
| Incorrect build applicability | High | Architect | Any unsupported negative finding. Use indeterminate, correct rules and rerun corpus. |
| Session impact in lab or pilot | High | QA lead | Critical workflow or HA check fails. Block expansion and rehearse recovery. |
| Source or asset drift | Medium | Engineer | Source revision or stale snapshot. Invalidate relevant review and reevaluate. |
| Repository unavailable | Medium | Delivery lead | Confirm owner and access before selecting paths, CI or PR base. |
| Sensitive data leakage | High | Security reviewer | Redaction or access check fails. Stop data flow and use the incident process. |

Initial assumptions are access to legally authorized 14.1 lab devices, vendor material for the corpus, and an operator who can review build and feature semantics. Commercial demand, vendor endpoint coverage, and lab topology are open. Record decision date, approver, rationale and linked evidence when closing each item.
