# SharePoint template library

This local contract demonstrates safe reuse of the Northstar onboarding list structure.

Run it with:

```bash
python3 src/main.py
```

Expected output:

```text
target=Department-B onboarding list
columns=5
views=2
items=0
validation=passed
```

The Python contract does not create or verify a remote SharePoint list. After applying the equivalent site or list template in SharePoint, inspect the target list to confirm its columns, views, and item count.
