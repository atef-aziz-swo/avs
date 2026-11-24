# Verification and release evidence

Select ten historical NetScaler 14.1 vendor advisories before testing. Record selection rationale, versions, appliance profiles, expected applicability and the presence or absence of a documented workaround. Include out-of-scope and ambiguous inputs. Have an appliance operator independently label expected results and adjudicate differences with the security reviewer.

| Suite | Key cases | Release evidence |
|---|---|---|
| Import | Duplicate, revision, malformed input, stale feed | Versioned provenance and deterministic replay |
| Applicability | Build boundaries, differing features, unsupported train, missing or conflicting evidence | Expected result and rationale per fixture |
| Collector | Correct role, denied writes, permissions, timeouts, partial fields, HA inventory | Device parity sample and failure records |
| Configuration | Vendor-supported configuration and expected bound scope using approved lab examples | Before/after snapshot and control contract results |
| Legitimate workflows | Login, MFA where enabled, resource enumeration, launch, reconnect, logout, and HA failover where supported | Scenario matrix by profile, observed failures and comparison with baseline |
| Lifecycle | Expired or changed approval, tampered evidence, drift, rejected change, recovery | State transition and recovery record |

Run comparable manual and AVS-assisted assessment sessions on paired cases and document start/stop criteria, analyst and elapsed time. Report median times with sample count and limitations. Record available SLA and baseline session impact criteria before lab changes. Track evidence by revision, appliance profile, time, outcome, and reviewer. Report any excluded scenario with rationale.

**Pilot gate.** Meet the approved product thresholds, close unresolved critical issues, prove targeted rollback, verify source and snapshot freshness, and obtain security and appliance-owner concurrence. A synthetic result supports only the specific observations recorded. Use the approved change window and named operator to make any pilot change.
