# Decisions, risks and assumptions

| Decision | Proposed direction | Owner | Due |
|---|---|---|---|
| D-01 Initial release scope | Multi-product platform; NetScaler ADC and Gateway 14.1 first, then independently gated coverage expansion | Product owner | M0 |
| D-02 Ownership and license | Confirm project IP and lab entitlements before committing to distribution | Sponsor | M0 |
| D-03 Repository and CI | Inspect repo first, then use its conventions and existing CI | Architect | M0 |
| D-04 Evidence rubric | Use vendor applicability plus synthetic functional results and reviewed configuration evidence | Security reviewer | Before M1 grading |
| D-05 Hosting and model | Choose hosting after data residency and cost review. Model use is optional | Architect | Before shared deployment |
| D-06 Pilot authority | Establish environment, approval roles, change window and support path | Appliance owner | M4 |
| D-07 Expansion selection | Select exact additional NetScaler trains and other vendor products using demand, lifecycle evidence, lab access and maintenance capacity | Product owner | Before expansion planning |

| Risk | Level | Owner | Trigger and response |
|---|---|---|---|
| Lab access or licenses delayed | High | Appliance owner | Lab access missing at M0. Continue fixtures and rebaseline integration. |
| Limited safe control coverage | High | Product owner | Low documented-control yield. Review assessment-only positioning and patch workflow value. |
| Incorrect build applicability | High | Architect | Any unsupported negative finding. Use indeterminate, correct rules and rerun corpus. |
| Session impact in lab or pilot | High | QA lead | Critical workflow or HA check fails. Block expansion and rehearse recovery. |
| Source or asset drift | Medium | Engineer | Source revision or stale snapshot. Invalidate relevant review and reevaluate. |
| Repository unavailable | Medium | Delivery lead | Confirm owner and access before selecting paths, CI or PR base. |
| Coverage or adapter confusion | High | Architect | Unvalidated product inherits a result or control. Block that coverage row, correct dispatch and rerun product isolation fixtures. |
| Expansion exceeds maintenance capacity | Medium | Product owner | No owner or current evidence for a product. Suspend affected capabilities and rebaseline scope. |
| Sensitive data leakage | High | Security reviewer | Redaction or access check fails. Stop data flow and use the incident process. |

Initial assumptions are access to legally authorized 14.1 lab devices, vendor material for the corpus, and an operator who can review build and feature semantics. Commercial demand, additional product/version selection, vendor lifecycle status, vendor endpoint coverage, and lab topology are open. Each expansion requires its own authorized fixtures or lab access and a maintenance owner. Record decision date, approver, rationale and linked evidence when closing each item.
