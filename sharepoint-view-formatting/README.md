# Actionable SharePoint view link

This local contract generates a SharePoint row formatter for the onboarding list.

The `Open record` link uses a fixed display-form route and SharePoint row context:

- `@currentWeb` supplies the web hosting the view.
- `[$ID]` supplies the current list item's ID.
- No caller-provided or external URL is accepted.

Run the contract with:

```bash
python src/main.py
```

Copy the generated formatter into the onboarding view's advanced view-formatting editor, then verify at least two rows with different item IDs in SharePoint. Local validation confirms the JSON contract; it does not configure or remotely verify the SharePoint view.
