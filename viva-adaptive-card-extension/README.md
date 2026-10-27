# Viva Adaptive Card Extension prototype

This local prototype models the data and interaction contract for the Northstar Viva Connections safety card.

## Run

```bash
python src/main.py
```

Expected output includes an initial `Acknowledge` state followed by an `Acknowledged` state for Jordan Lee.

The Python prototype verifies card behavior locally. A production ACE requires an SPFx-compatible project, packaging, App Catalog deployment, Viva Dashboard placement, and tenant-side verification.
