# Coverage and expansion policy

AVS is designed for multiple appliance products and versions. This documentation describes proposed coverage; it does not establish implemented or validated support.

| Phase | Target | Admission evidence |
|---|---|---|
| Initial validation | NetScaler ADC and Gateway 14.1 | Reviewed advisory corpus, build boundaries and offline evidence exports; discovery and controls pass separate lab gates |
| Additional release trains | Other NetScaler ADC and Gateway versions selected at kickoff | Current vendor lifecycle check, version-specific rules and fixtures, and lab evidence for each claimed capability |
| Additional vendors | Selected ADC, remote-access gateway, firewall or WAF products | Named product owner, authoritative advisory sources, product adapter, independent expected results and capability-specific validation |

Select exact versions and vendors using operator demand, exposure, access to authoritative advisories, vendor lifecycle status, authorized lab access and maintenance cost. Record the selection in D-07 before scheduling implementation. Do not infer current vendor support from a version number or this roadmap. Legacy versions may be admitted for assessment with their lifecycle status visible; any temporary control still needs explicit vendor support evidence.

## Coverage matrix

Maintain a versioned matrix keyed by vendor, product, release train, build range, deployment form and feature profile. Each row records vendor lifecycle status and its source/check date, adapter and rule revisions, evidence links, owner, last validation date and known limits. Track these capabilities separately:

| Capability | Required evidence |
|---|---|
| Advisory assessment and offline inventory | Source mapping, normalized product identity, version comparison and independently reviewed applicability fixtures |
| Read-only discovery | Verified API or export contract, least-privilege role, inventory parity and failure handling for the exact profile |
| Temporary control evaluation | Vendor-documented option, prerequisites, configuration checks and product-specific functional and recovery evidence |
| Production pilot | Approved target boundary, named operator, current evidence and product-specific change and rollback plan |

Use planned, validating, validated or suspended status per capability. A validated capability applies only to its recorded matrix row. Assessment coverage does not imply discovery, available mitigation or production change authority. Unknown products, unvalidated versions and unmatched profiles return indeterminate with a coverage reason; they never inherit a 'not affected' result from another row.

## Expansion gate

For each new row, verify vendor documentation and lifecycle status, approve the corpus and expected results, implement or extend the adapter, run the applicable verification suites and record reviewer acceptance. Reuse shared evidence and lifecycle services while keeping product-specific version rules, collectors, control catalogs and workflow tests explicit. Changes to source semantics, APIs or vendor support can suspend affected capabilities until reevaluation. Re-estimate delivery and assign an ongoing maintenance owner for each expansion.
