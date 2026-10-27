import json


def actionable_link():
    return {
        "elmType": "a",
        "txtContent": "Open record",
        "attributes": {
            "href": "=concat(@currentWeb, '/Lists/Onboarding/DispForm.aspx?ID=', [$ID])",
            "target": "_blank",
            "rel": "noopener noreferrer",
            "title": "Open this onboarding record"
        }
    }


def build_view_formatter():
    return {
        "$schema": "https://developer.microsoft.com/json-schemas/sp/v2/row-formatting.schema.json",
        "rowFormatter": {
            "elmType": "div",
            "children": [actionable_link()]
        }
    }


def validate_contract(formatter):
    link = formatter["rowFormatter"]["children"][0]
    href = link["attributes"]["href"]
    assert link["elmType"] == "a"
    assert "@currentWeb" in href and "[$ID]" in href
    assert "http://" not in href
    assert "https://" not in href.replace(
        "https://developer.microsoft.com", ""
    )
    return "fixed SharePoint route + current item ID"


def main():
    formatter = build_view_formatter()
    print(json.dumps(formatter, indent=2))
    print(f"Safety rule: {validate_contract(formatter)}")


if __name__ == "__main__":
    main()
