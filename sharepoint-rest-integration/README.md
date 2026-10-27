# SharePoint REST integration

This prototype constructs and locally checks a read request and an update request for a SharePoint list item.

## Run

```bash
python src/rest_contract.py
```

The script simulates the item transition locally and performs an explicit local read-back. In Power Automate, map the same values to **Send an HTTP request to SharePoint** and verify the action response and the stored item in SharePoint.

The connection identity must have permission for the requested operation. Replace the example site URL with the target site and confirm that `Status` is the list column's internal name.
