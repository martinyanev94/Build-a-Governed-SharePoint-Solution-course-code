# SharePoint approval workflow

This runnable contract models the approval states for the Northstar HR policy page.
It does not configure a SharePoint tenant. Use it to verify the state transitions and
rejection-note requirement before configuring the Site Pages approval flow.

## Run

```bash
python3 src/main.py
```

Expected output:

```text
42 Approved Approved by Jordan Lee
42 Rejected Rejected by Jordan Lee: Add regional exceptions
```

The SharePoint configuration should use the selected page item ID, approvers with
site-owner or Full Control permissions, and a reader-visible content state that keeps
pending and rejected pages out of the final published experience.
