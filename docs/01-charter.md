# Project charter

**Problem.** Infrastructure teams may face a gap between a vendor security advisory and a verified patch across their network and security appliances. Manual applicability assessment and change preparation consume part of that interval.

**Outcome.** Give an appliance operator a timestamped, traceable assessment and enough evidence to decide whether a vendor-supported temporary control warrants a controlled change. Continue tracking the vendor patch as the permanent remediation.

**Initial release.** NetScaler ADC and Gateway 14.1 only. Additional versions and products are later increments with separate selection, estimates and validation.

**Platform direction.** A shared assessment and evidence platform for multiple appliance products and versions, introduced through independently validated adapters. NetScaler ADC and Gateway 14.1 remain the first validation target. Additional NetScaler release trains follow, then selected ADC, remote-access gateway, firewall or WAF products from other vendors. These are roadmap categories; exact products and versions require selection and evidence before any support claim. See the [coverage and expansion policy](09-coverage.md).

The initial release covers advisory normalization, sanitized inventory, applicability, documented mitigation options, and evidence reports. A separately gated lab increment covers evaluation of approved control configurations with synthetic traffic and rollback rehearsal. Each product has separate discovery, control and pilot gates. A production pilot requires a new release decision. Firmware modifications, inline proxying, and kernel integrations are deferred.

| Accountable role | Responsibility |
|---|---|
| Sponsor / product owner | Own scope, budget, success criteria and release decisions |
| Technical architect | Own design, contracts and decision records |
| Delivery lead | Own dependencies, scheduling and risk review |
| Security reviewer | Own evidence criteria, data handling and release concurrence |
| Appliance owner / operator | Own lab access, vendor support checks, changes and recovery |
| QA lead | Own the test corpus, baselines and independent results review |

One person may cover multiple roles during discovery. Independent approval is required for changes to a pilot appliance.

**Kickoff exit.** Assign named owners, confirm ownership and IP obligations, approve lab use and retention policy, agree on candidate selection and success thresholds, and start the offline fixture work. Track labor, lab licensing, compute, storage and any model usage separately. Commit spend after the sponsor reviews the estimates and access dependencies.

**Go/no-go.** Advance to a pilot only after validation, security and appliance owners accept the evidence and nominate a pilot boundary. Continue as an assessment-only product if temporary controls are rarely supported or evidence costs outweigh time saved. Validate demand through interviews with infrastructure leads and security responders before committing to pricing or packaging.
