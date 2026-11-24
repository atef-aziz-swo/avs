# Product requirements

Primary users are appliance operators and vulnerability responders. Change approvers need a reviewable record tying the advisory, appliance snapshot, proposed control, evidence, owner and expiry together.

| ID | Requirement | Acceptance |
|---|---|---|
| PR-01 | Import vendor advisory records and optional NVD / KEV context | Repeated imports are idempotent. A revision preserves prior source versions and invalidates stale assessments. A feed failure is visible with last successful ingest time. |
| PR-02 | Inventory appliances in the validated coverage matrix offline, then through authorized read-only discovery | Normalize vendor, product, release train, build, relevant features, deployment profile, HA role and observed time. Missing facts and stale snapshots are visible. Credentials are absent from exports. |
| PR-03 | Assess applicability with deterministic rules | Return affected, not affected, or indeterminate with source, relevant facts and rationale. Conflicting or unknown vendor build information yields indeterminate. |
| PR-04 | Surface vendor-documented temporary options | Options cite a vendor reference, prerequisites, supported profiles, constraints and expiry. Absent or unverified options are clearly marked. |
| PR-05 | Export a reviewable evidence package | Export contains source revisions, snapshot ID, reproducible assessment inputs, test scope where applicable, and a firmware remediation status. |
| PR-06 | Track approvals and retirement in the lab or an approved pilot | Authorized reviewer approves an immutable revision with an expiry. Any material change resets approval. Retirement records confirmed vendor patch status and post-change checks. |
| PR-07 | Manage coverage by product, version and capability | Publish matrix rows with evidence, lifecycle source/check date, adapter revision and validation status. Unmatched or unvalidated inputs yield indeterminate. Discovery and controls require separate validation. |

**Status rules.** Applicability, mitigation availability, evidence, and lifecycle are distinct fields. A completed synthetic regression suite supports a compatibility claim for those scenarios. A control applicability claim requires vendor support and evidence that the approved configuration is present at the intended scope. Unknown or stale evidence cannot advance a release gate.

**Proposed measures, agreed before testing.** Review 10 historical vendor advisories and report both advisory count and distinct CVE count. Achieve 100% evidence traceability and zero unsupported 'not affected' results in the reviewed corpus. Aim for at least 30% lower median analyst time than the manual baseline on paired cases. Report documented-control yield as a measured outcome with all cases in the denominator. Require a 100% pass on agreed critical legitimate workflows and rollback rehearsals before pilot consideration. Track per-scenario impact, observed false blocks and unresolved unknowns separately.
