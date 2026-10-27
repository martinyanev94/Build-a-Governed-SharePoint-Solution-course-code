# Microsoft Graph SharePoint data application

This prototype retrieves a SharePoint site and its lists through Microsoft Graph.

## Local contract check

Run the dependency-free demo:

```text
python3 src/main.py
```

Expected output:

```text
Northstar HR Hub
site-123
Onboarding
Policies
```

## Remote Python request

Provide a delegated Graph access token and a permitted site ID without saving either value in the repository:

```text
export SHAREPOINT_SITE_ID='your-site-id'
export GRAPH_TOKEN='token-from-your-authenticated-session'
python3 src/main.py --remote
```

The remote mode calls the v1.0 site and lists endpoints and prints selected response fields.

## PowerShell SDK request

Use PowerShell 7 when possible. The script installs the Sites module for the current user, connects with a read scope, and retrieves the site and lists:

```text
$env:SHAREPOINT_SITE_ID = 'your-site-id'
./src/query.ps1
```

Do not commit access tokens. Confirm the requested scope and tenant consent with the administrator, and verify that the signed-in identity can read the target site.
