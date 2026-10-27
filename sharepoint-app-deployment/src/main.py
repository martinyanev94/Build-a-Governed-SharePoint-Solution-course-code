from dataclasses import dataclass


@dataclass
class Package:
    name: str
    platform: str
    api_access: str
    scope: str


def validate_package(package):
    errors = []
    if not package["name"].endswith(".sppkg"):
        errors.append("package must use the .sppkg extension")
    if package["platform"] not in {"SharePoint", "Teams", "Viva Connections"}:
        errors.append("unsupported platform")
    if package["api_access"] == "broad":
        errors.append("manual API access review required")
    return errors


def evaluate_risk(package, vendor_reviewed):
    errors = validate_package(package)
    if errors and errors != ["manual API access review required"]:
        return "reject: " + "; ".join(errors)
    if package["scope"] not in {"tenant", "site-collection"}:
        return "reject: deployment scope is missing"
    if package["api_access"] == "broad" or not vendor_reviewed:
        return "hold: manual approval required"
    return "ready: submit to App Catalog approval"


if __name__ == "__main__":
    northstar_package = {
        "name": "NorthstarPolicyCards.sppkg",
        "platform": "SharePoint",
        "api_access": "broad",
        "scope": "site-collection",
    }
    print("Package check: NorthstarPolicyCards.sppkg")
    print("Package check: valid package metadata")
    print("Package check: review required for broad API access")
    print("Risk decision: " + evaluate_risk(northstar_package, vendor_reviewed=True))
    print("Reason: broad API access requires administrator review")
    print("Scope: " + northstar_package["scope"])
