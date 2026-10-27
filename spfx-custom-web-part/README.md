# Northstar Status SPFx web part

This project contains the Northstar Status SharePoint Framework web part and its deployment verification record.

## Build and package

Use the SPFx-compatible Node.js and npm versions selected for this project, then run:

```text
gulp bundle --ship
gulp package-solution --ship
```

The production bundle is written under `temp/deploy`, and the SharePoint Framework solution package is written under `sharepoint/solution`.

## Verify deployment

Review `deployment_verification.md` while checking the package in the tenant App Catalog and the published target page. The verification boundary is:

- package availability at the recorded App Catalog scope;
- rendering on the published Northstar Portal page;
- the operational status data source;
- the signed-in viewer's existing SharePoint permissions.

The local evidence helper can be run with:

```text
python src/deployment_check.py
```

Expected output:

```text
VERIFIED: Northstar Status
```

A local result documents the expected evidence contract. It does not replace checking the remote App Catalog, published page, or viewer access.
