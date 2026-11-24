# Adaptive Vulnerability Shield | Project kickoff
Version 0.1 · Proposed baseline · 24 November 2026

AVS helps operators assess NetScaler 14.1 exposure, evaluate approved compensating controls, and track temporary protection through vendor patch verification. The first milestone is an offline evidence report. The next milestone is read-only discovery against an authorized lab.

| Document | Kickoff question |
|---|---|
| [Charter](01-charter.md) | Why build it, who owns it, and when do we stop? |
| [Product requirements](02-product-requirements.md) | What can operators do and how will we measure success? |
| [Technical architecture](03-architecture.md) | What are the boundaries, interfaces, and data contracts? |
| [Security and governance](04-security.md) | How are evidence, credentials, and changes controlled? |
| [Delivery and backlog](05-delivery.md) | What should the team implement first? |
| [Verification plan](06-verification.md) | What evidence supports each release decision? |
| [Operations and pilot](07-operations.md) | How will operators monitor, recover, and retire controls? |
| [Decision and risk registers](08-registers.md) | Who resolves the open decisions and risks? |

Source: AVS_Product_Concept.docx v0.1. The referenced repository is [mayoit/avs](https://github.com/mayoit/avs). Repository access and the Windows checkout could not be verified. This package assumes no existing layout or CI provider. Review for path conflicts before importing these files. References for kickoff verification include [NetScaler documentation](https://docs.netscaler.com/), [NVD](https://nvd.nist.gov/), and [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). Product thresholds, estimates, and technology choices below are proposals.
