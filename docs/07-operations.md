# Operations and pilot runbook

**Offline and read-only operation.** Monitor feed freshness, collection age and errors, unclassified builds, evaluation failures and outstanding evidence reviews. Record the last successful refresh per source or asset. On failure, keep the last valid snapshot, show its age and prevent stale records from qualifying for a change.

**Before a pilot change.** Link the vendor advisory, verified asset build and profile, approved control revision, ticket, backup reference, expiry, health baseline, and named operator. Confirm HA health and recovery access with the appliance owner. Ensure vendor-supported sequencing and an approved window. Pause if build, policy binding, role, or health differs from approved evidence.

**During the window.** Have the operator apply the approved scoped change in the agreed sequence. Observe appliance health, HA state, management access, and designated user workflows before expanding scope. Stop on failed checks, unexpected drift, lost telemetry, unanticipated policy matches or session impairment.

**Recovery.** Pause rollout and alert the appliance owner and incident lead. Use the rehearsed rollback for that exact change and verify service baseline and HA health. Reconcile observed configuration before retrying a change with an uncertain outcome. Escalate through the existing incident procedure if baseline recovery fails. Capture timeline, affected scope and evidence.

**Expiry and retirement.** Alert the owner before expiry. An extension requires renewed evidence and approval. After verifying vendor patch build on each applicable appliance and passing agreed health checks, retire the temporary control through a change ticket. Confirm expected bindings and close the evidence record. If the control expires before patching, route the decision to the appliance owner and security reviewer for a documented disposition.
