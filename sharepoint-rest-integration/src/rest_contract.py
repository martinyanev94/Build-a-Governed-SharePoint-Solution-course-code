from dataclasses import dataclass
from urllib.parse import quote


@dataclass(frozen=True)
class RestRequest:
    method: str
    uri: str
    headers: dict[str, str]
    body: dict[str, object] | None = None


def build_get_request(site_url: str, list_title: str, item_id: int) -> RestRequest:
    list_path = quote(list_title, safe="")
    uri = (
        f"{site_url}/_api/web/lists/GetByTitle('{list_path}')/items"
        f"({item_id})?$select=Id,Title,Status"
    )
    return RestRequest("GET", uri, {"Accept": "application/json;odata=nometadata"})


def build_status_update(site_url: str, list_title: str, item_id: int, status: str) -> RestRequest:
    list_path = quote(list_title, safe="")
    uri = (
        f"{site_url}/_api/web/lists/GetByTitle('{list_path}')/items"
        f"({item_id})"
    )
    headers = {
        "Accept": "application/json;odata=nometadata",
        "Content-Type": "application/json;odata=nometadata",
        "X-HTTP-Method": "MERGE",
        "If-Match": "*",
    }
    return RestRequest("POST", uri, headers, {"Status": status})


def verify_sequence() -> dict[str, object]:
    site_url = "https://contoso.sharepoint.com/sites/Northstar"
    read_request = build_get_request(site_url, "Onboarding", 17)
    update_request = build_status_update(site_url, "Onboarding", 17, "Approved")
    item = {"Id": 17, "Title": "Jordan Lee", "Status": "Pending"}
    item["Status"] = update_request.body["Status"]
    read_back = {
        "Id": item["Id"],
        "Title": item["Title"],
        "Status": item["Status"],
    }
    result = {
        "read_uri": read_request.uri,
        "update_method": update_request.method,
        "item_id": read_back["Id"],
        "title": read_back["Title"],
        "status": read_back["Status"],
    }
    return result


if __name__ == "__main__":
    print(verify_sequence())
