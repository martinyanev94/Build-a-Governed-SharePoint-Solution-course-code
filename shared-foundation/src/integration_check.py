from __future__ import annotations


def validate_journey(record, viewer, evidence):
    required = {"content", "automation", "search", "presentation"}
    missing = required - set(evidence)
    if missing:
        return False, f"missing evidence: {', '.join(sorted(missing))}"
    if record["status"] != "Approved":
        return False, "record is not approved"
    if evidence["content"]["item_id"] != record["item_id"]:
        return False, "content identity changed"
    if viewer not in evidence["presentation"]["allowed_viewers"]:
        return False, "viewer is outside the permission boundary"
    return True, f"item {record['item_id']} traced for {viewer}"


def main():
    record = {"item_id": 42, "title": "Taylor Morgan", "status": "Approved"}
    evidence = {
        "content": {"item_id": 42},
        "automation": {"outcome": "Approved"},
        "search": {"scope": "Northstar hub", "query": "onboarding"},
        "presentation": {"allowed_viewers": ["employee"]},
    }
    verified, message = validate_journey(record, "employee", evidence)
    print(message)
    print("checkpoints: content, automation, presentation, search")
    print(f"result: {'governed journey verified' if verified else 'review required'}")


if __name__ == "__main__":
    main()
