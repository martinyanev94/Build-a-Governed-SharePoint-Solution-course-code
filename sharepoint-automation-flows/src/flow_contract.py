"""Runnable contract for diagnosing flow failures and shaping REST requests."""


def diagnose_failure(action_name, item_id, error):
    return {
        "action": action_name,
        "item_id": item_id,
        "error": error,
        "next_step": "Inspect the action input that the error names.",
    }


def build_rest_request(site_address, item_id):
    return {
        "site_address": site_address,
        "method": "GET",
        "uri": f"_api/web/lists/GetByTitle('Onboarding')/items({item_id})",
        "headers": {"Accept": "application/json;odata=nometadata"},
        "body": "",
    }


if __name__ == "__main__":
    failure = diagnose_failure(
        "Update item", 42, "Status value rejected"
    )
    print(f"FAILED {failure['action']} for item {failure['item_id']}")
    print(f"ERROR {failure['error']}")
    print(f"NEXT {failure['next_step']}")

    request = build_rest_request("https://northstar.sharepoint.com/sites/hr", 42)
    print(f"{request['method']} {request['uri']}")
    print(f"Accept: {request['headers']['Accept']}")
