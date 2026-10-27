# SharePoint app deployment checklist

This local example records the decision evidence needed before submitting a SharePoint app package to an App Catalog. It does not connect to a tenant or upload files.

## Run

```bash
python3 src/main.py
```

The example uses `NorthstarPolicyCards.sppkg`, targets SharePoint, requests broad API access, and records site-collection scope. The expected decision is a manual approval hold.

## Review boundary

A successful local check does not prove that SharePoint accepted or deployed the package. An administrator must verify the package in the appropriate tenant-wide or site collection App Catalog, review requested permissions and vendor evidence, and record the approval decision.
