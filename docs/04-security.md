# Security and governance

| Threat or failure | Controls and expected evidence |
|---|---|
| Compromised advisory or prompt injection | Treat source data as inert. Enforce schemas, pin provenance, and show conflicts for review. Model has no change permissions. Verify with synthetic malformed records. |
| Credential or inventory disclosure | Separate identities by environment and purpose, store secrets in a managed vault, use encrypted channels, redact exports and log access. Review sample artifacts for sensitive data. |
| Tampered or replayed approval | Bind approval and signature to immutable digest, appliance scope and expiry. Verify signer authorization and reject mismatches. Record approvals, revocations and changes in append-only audit history. |
| Unauthorized management access | Deny public management ingress, restrict management routes, use read-only access first and audit privilege assignments. Validate separately scoped credentials in lab. |
| Stale inputs or configuration drift | Record freshness and compare observed state with the approved snapshot. Pause changes and require review after meaningful drift. |
| HA or availability regression | Rehearse baseline health, pilot sequencing, abort checks and targeted rollback. Preserve recovery access and backups under the appliance owner's control. |

Separate developer, reviewer and operator roles for pilot changes. Audit actor, action, asset pseudonym, artifact digest, time, decision and reason. Keep production identifiers and raw configurations out of shared fixtures and model inputs. Data owner sets retention and deletion schedules before importing operational data. Workspace and repository access should follow the project ownership and IP decision.

Keep the PoC defensive. Use vendor advisories, sanitized inventories, synthetic functional cases and vendor-documented control configuration checks. Record the evidence scope in every result. Prioritize vendor remediation when no supported temporary control is available.
