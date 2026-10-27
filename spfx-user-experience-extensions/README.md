# SPFx user-experience extension prototype

This local Python contract maps a SharePoint interaction surface to an SPFx extension type.

Run it with:

```text
python src/main.py
```

Expected output:

```text
extension=ListView Command Set
location=command bar and context menu
selection_required=True
action=archive
```

The script records a design decision; it does not deploy an SPFx package or modify a SharePoint tenant. The selected extension and command locations must still be implemented and verified in the generated SPFx solution.
