# SharePoint automation flow contract

Run the local diagnostic and REST-request shaping example with:

```bash
python src/flow_contract.py
```

The script does not call SharePoint and contains no credentials. It records the
information a flow designer must verify: the failed action, triggering item ID,
error text, site address, HTTP method, REST URI, headers, and body.

In Power Automate, map the request fields to **Send an HTTP request to
SharePoint** only when a standard SharePoint action does not expose the needed
operation. Verify the connection permissions and the returned or changed data
in run history and SharePoint.
