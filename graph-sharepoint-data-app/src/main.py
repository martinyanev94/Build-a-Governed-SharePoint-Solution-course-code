import json
import os
import sys
from urllib.request import Request, urlopen


def get_site(site_id: str, token: str) -> dict:
    request = Request(
        f"https://graph.microsoft.com/v1.0/sites/{site_id}",
        headers={"Authorization": f"Bearer {token}"},
    )
    with urlopen(request) as response:
        return json.load(response)


def get_lists(site_id: str, token: str) -> dict:
    request = Request(
        f"https://graph.microsoft.com/v1.0/sites/{site_id}/lists",
        headers={"Authorization": f"Bearer {token}"},
    )
    with urlopen(request) as response:
        return json.load(response)


def demo() -> None:
    site = {"id": "site-123", "displayName": "Northstar HR Hub"}
    lists = {
        "value": [
            {"id": "list-onboarding", "displayName": "Onboarding"},
            {"id": "list-policies", "displayName": "Policies"},
        ]
    }
    print(site["displayName"])
    print(site["id"])
    for item in lists["value"]:
        print(item["displayName"])


def remote() -> None:
    site_id = os.environ["SHAREPOINT_SITE_ID"]
    token = os.environ["GRAPH_TOKEN"]
    site = get_site(site_id, token)
    lists = get_lists(site_id, token)
    print(site.get("displayName", "<unnamed site>"))
    print(site["id"])
    for item in lists.get("value", []):
        print(item.get("displayName", "<unnamed list>"))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--remote":
        remote()
    else:
        demo()
