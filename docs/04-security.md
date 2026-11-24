# Security and governance

| Threat or failure | Controls and expected evidence |
|---|---|
| Compromised advisory or prompt injection | Treat source data as inert. Enforce schemas, pin provenance, and show conflicts for review. Model has no change permissions. Verify with synthetic malformed records. |
| Credential or inventory disclosure | Separate identities by environment and purpose. Initially store secrets in protected local files, mount them read-only only into services that need them, and encrypt host storage and backups. Use encrypted channels, redact exports and log access. Vault integration is a later option. Review file permissions and sample artifacts for sensitive data. |
| Tampered or replayed approval | Bind an authenticated reviewer's explicit decision to an immutable digest, appliance scope and expiry. Check reviewer authorization, current revision, revocation and expiry before accepting approval; reject mismatches. Record reviewer identity, decision, timestamp, reason, approvals, revocations and changes in append-only application audit history. Cryptographic signing of approval artifacts is a later option. |
| Unauthorized management access | Deny public management ingress, restrict management routes, use read-only access first and audit privilege assignments. Validate separately scoped credentials in lab. |
| Stale inputs or configuration drift | Record freshness and compare observed state with the approved snapshot. Pause changes and require review after meaningful drift. |
| Cross-product rule or control selection | Bind rules, controls and approvals to vendor, product, version constraints and profile. Reject mismatches and test adapter isolation. |
| HA or availability regression | Rehearse baseline health, pilot sequencing, abort checks and targeted rollback. Preserve recovery access and backups under the appliance owner's control. |

Separate developer, reviewer and operator roles for pilot changes. Audit actor, action, asset pseudonym, artifact digest, time, decision and reason. Keep production identifiers and raw configurations out of shared fixtures and model inputs. Data owner sets retention and deletion schedules before importing operational data. Workspace and repository access should follow the project ownership and IP decision.

Keep the PoC defensive. Use vendor advisories, sanitized inventories, synthetic functional cases and vendor-documented control configuration checks. Record the evidence scope in every result. Prioritize vendor remediation when no supported temporary control is available.

**Initial security baseline.** Protected local secret files and authenticated, audited approvals are accepted initial-release decisions recorded as D-09 and D-10. Host administrators provision and rotate credential files; the application stores opaque references. Application-level audit controls do not prevent a privileged host administrator from altering local data. Future vault integration and cryptographic approval signing require their own implementation and verification. Release-package signature verification remains a separate supply-chain requirement.
