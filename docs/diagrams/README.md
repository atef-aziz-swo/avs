# AVS architecture diagrams

Proposed reference design, not a record of deployed Azure resources. The initial scope remains NetScaler ADC and Gateway 14.1. Azure is an optional host for the same Linux product, alongside the dedicated local Linux VM deployment.

| Diagram | Scalable source | High-resolution image |
|---|---|---|
| Azure landing-zone reference | [SVG](avs-azure-landing-zone.svg) | [4800 × 3420 PNG](avs-azure-landing-zone.png) |
| Linux VM and component boundaries | [SVG](avs-linux-components.svg) | [4800 × 3400 PNG](avs-linux-components.png) |

SVGs contain editable text, shapes and connectors with embedded official icon assets. PNGs provide predictable rendering in Markdown viewers. Open the full-size image or SVG for review rather than relying on a narrow document preview.

## Azure placement and responsibilities

Use an internal Corp workload subscription with inherited policy, access controls, naming and tags. Place the AVS Linux VM in its own resource group and spoke VNet. Reuse the platform connectivity subscription's hub, VPN Gateway, Azure Firewall and Bastion where available. This is a workload placement view, not a complete enterprise landing-zone hierarchy. Tenant identity, platform management subscriptions, DNS and security ownership must align with the organization's existing landing zone. Microsoft's guidance distinguishes internal Corp workloads from public-facing Online workloads. [Landing-zone networking guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/design-area/network-topology-and-connectivity).

The hub-and-spoke structure follows Microsoft's reference pattern, with customer-managed hub services. Bastion provides an administration path; it is not the user-facing AVS access path. The diagram does not show a public IP on the workload VM. Platform services such as VPN Gateway or Bastion may have their own public endpoints according to the selected SKU and deployment. [Hub-spoke reference architecture](https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke).

Illustrative spoke allocations, subject to platform approval and overlap checks:

| Resource | Example | Purpose |
|---|---|---|
| Workload resource group | `rg-avs-prod` | VM, NIC, disks, workload networking and backup resources |
| Spoke VNet | `10.40.0.0/24` | Private AVS workload address space |
| Workload subnet | `snet-avs`, `10.40.0.0/27` | AVS private NIC, NSG and route table |
| Private-endpoint subnet | `snet-pe`, `10.40.0.32/27` | Blob private-endpoint NIC; represented by the endpoint icon |
| Blob private DNS zone | `privatelink.blob.core.windows.net` | Private storage name resolution from AVS |

Configure peering to permit the required forwarded traffic and gateway transit, with the spoke using the approved remote gateway. Explicitly route corporate destination prefixes from the AVS subnet through the hub firewall when inspection is required; do not assume a default route overrides more-specific propagated routes. Configure the gateway-side return route for the spoke through the firewall and verify symmetric routing. Keep the firewall's required routing intact. Bastion access and private-endpoint traffic need their own validated paths; they do not automatically traverse the firewall. [Hybrid firewall routing guidance](https://learn.microsoft.com/en-us/azure/firewall/tutorial-hybrid-portal).

## Flow and access matrix

| Source → destination | Access | Design requirement |
|---|---|---|
| Corporate reviewers → AVS | HTTPS 443 over private connectivity | Restricted source networks, AVS authentication and authorization |
| Host administrators → AVS VM | SSH via approved Bastion path | Restricted administrator role, NSG and host policy; no public VM SSH |
| Collector → NetScaler management | HTTPS on approved management endpoint | Hybrid route, destination allowlist, trusted TLS and restricted read-only account |
| Worker → vendor sources | HTTPS through hub egress or approved corporate proxy | Source allowlist, DNS, bounded retries; offline import alternative |
| AVS → enterprise identity provider | Approved OIDC HTTPS endpoints | Explicit egress and callback configuration; identity integration must be implemented |
| Host backup process → Azure Blob | HTTPS through private endpoint | Coordinated encrypted backup set, storage data authorization and private DNS |
| Optional monitoring agent → Azure Monitor | Approved telemetry endpoints | Redaction, retention and platform-approved connectivity; omitted detailed path |

The site-to-hub line represents connectivity for the whole corporate site, including appliance management, rather than only the adjacent operator card. Numbered diagram lines are selected logical flows. The worker's artifact writes and maintenance access to database/artifacts are described in the component legend; they are not all drawn as separate wires.

For Azure backups, prefer a VM managed identity scoped to the backup container through a data-plane role selected for the upload tool's exact operations. Do not expose VM identity credentials or the metadata endpoint to application containers. Validate host/container isolation and backup restore/delete permissions separately. This is an Azure-host integration requirement, not a change to local appliance credential storage.

A Blob private endpoint gives the storage service a private network access path; it does not place the storage account inside the subnet or disable its public endpoint automatically. Explicitly disable public network access, link/configure private DNS and test resolution from AVS. Encrypt coordinated application backups before upload, retain recoverable copies according to site policy and rehearse restore. Native VM snapshots alone do not replace the application-consistent backup procedure. [Azure Storage private endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-private-endpoints).

## Initial baseline and optional services

- PostgreSQL is a local container with persistent data on the VM's data disk. The design does not require Azure Database for PostgreSQL, AKS or Azure Container Apps.
- Appliance credentials start as protected local files with restricted read-only mounts. Vault integration is later; Azure hosting does not make Key Vault mandatory.
- Approval records start as authenticated, authorized, audited decisions bound to revision digest, scope and expiry. Cryptographic approval signing is later.
- Azure Monitor is optional. Entra ID is the proposed enterprise OIDC provider in the Azure variant; authentication must be configured and tested.
- Azure Blob is an optional off-host backup destination. A local deployment can use a different approved destination.
- A single VM provides no automatic host failover. Hub-service reuse, recurring Azure costs and regional resource availability need validation before deployment.

## Icons and regeneration

Azure service icons are unmodified assets from Microsoft's [official architecture icon collection](https://learn.microsoft.com/en-us/azure/architecture/icons/), downloaded from the linked `Azure_Public_Service_Icons_V25.zip` package. The selected originals are in [icons](icons). Microsoft's terms permit their use in architecture diagrams and documentation; the icons remain Microsoft's property and are not AVS branding. Local AVS components use neutral cards rather than icons for unrelated Azure managed services.

Generate the diagrams from the repository root:

```powershell
python -m pip install -r scripts/diagram-requirements.txt
python scripts/generate_architecture_diagrams.py
```

The generator uses Segoe UI on Windows or DejaVu Sans on Linux for text-width checks. It embeds the icons, creates both SVGs and renders 2× PNGs using resvg. Rendering can differ slightly between fonts; inspect both images after changing labels or layout. Generated SVGs and PNGs are committed deliverables, so readers do not need Python or a renderer.
