# Governed solution integration check

This small verifier records the local acceptance contract for the Northstar
solution. It does not connect to SharePoint or claim tenant execution.

## Run

```bash
python3 src/integration_check.py
```

The example preserves onboarding item ID 42 and checks that an approved record
has content, automation, search, and presentation evidence for an authorized
employee viewer. Confirm the same values remotely through the SharePoint list,
Power Automate run history, configured search scope, and intended Teams, Viva,
or portal surface.

Use the existing PnP provisioning package to create repeatable list, view, page,
and search configuration. Keep the PnP template as configuration, not as a
copy of live onboarding records.
