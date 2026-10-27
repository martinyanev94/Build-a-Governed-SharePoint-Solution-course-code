"""Boundary review for the Northstar intelligent-content prototype."""

solution = {
    "capability": "extract employee and department",
    "input_format": "scanned PDF",
    "pages": 10,
    "output": "library columns plus managed terms",
    "billing": {"model": "pay-as-you-go", "azure_subscription": True,
                 "resource_group": "northstar-hr", "transaction_scope": "HR library",
                 "billing_evidence": False},
    "taxonomy": {"terms": ["Department: Human Resources", "Topic: Benefits"],
                 "source": "local-managed", "managed_terms_available": False},
    "signature": {"format": "PDF", "signees": 2, "placeholders_ready": True,
                  "service_enabled": False, "region_verified": False},
}


def render_decision(solution):
    print(f"capability: {solution['capability']}")
    print(f"input: {solution['input_format']}; pages: {solution['pages']}")
    print(f"output: {solution['output']}")
    print(f"billing: {solution['billing']['model']}; Azure subscription required")
    print(f"taxonomy: {', '.join(solution['taxonomy']['terms'])}")
    print(f"signature: {solution['signature']['format']}; {solution['signature']['signees']} signees")


def review_boundaries(solution):
    billing = solution["billing"]
    taxonomy = solution["taxonomy"]
    signature = solution["signature"]
    checks = {
        "billing": (billing["azure_subscription"] and billing["resource_group"]
                    and billing["transaction_scope"] and billing["billing_evidence"]),
        "taxonomy": (bool(taxonomy["terms"])
                     and taxonomy["source"] == "local-managed"
                     and taxonomy["managed_terms_available"]),
        "signature": (signature["format"] == "PDF"
                      and 0 < signature["signees"] <= 10
                      and signature["placeholders_ready"]
                      and signature["service_enabled"] and signature["region_verified"]),
    }
    status = "ready" if all(checks.values()) else "review-required"
    return checks, status


def main():
    render_decision(solution)
    checks, status = review_boundaries(solution)
    print(f"checks: {', '.join(f'{key}={value}' for key, value in checks.items())}")
    print(f"status: {status}")


if __name__ == "__main__":
    main()
