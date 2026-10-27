from dataclasses import dataclass


@dataclass(frozen=True)
class OnboardingRecord:
    item_id: int
    title: str
    owner: str
    status: str
    contract_signed: bool


APP_CONTRACT = {
    "data_source": "Onboarding",
    "screens": ["Create", "Review"],
    "create_fields": ["Title", "Owner", "Status", "Contract signed"],
    "delegated_review_formula": "Sort(Filter(Onboarding,'Contract signed'=false),Title)",
}


def create_record(records, title, owner, status, contract_signed):
    next_id = max(record.item_id for record in records) + 1
    record = OnboardingRecord(next_id, title, owner, status, contract_signed)
    return [*records, record]


def review_queue(records):
    return sorted(
        (record for record in records if not record.contract_signed),
        key=lambda record: record.title,
    )


def delegation_report():
    return "delegated filter and sort expected"


def main():
    records = [
        OnboardingRecord(101, "Aisha Khan", "Jordan Lee", "Needs review", False),
        OnboardingRecord(102, "Marco Silva", "Jordan Lee", "Complete", True),
        OnboardingRecord(103, "Zoe Chen", "Jordan Lee", "Needs review", False),
    ]
    records = create_record(
        records,
        "Nia Patel",
        "Jordan Lee",
        "Needs review",
        False,
    )
    queue = review_queue(records)
    print("experience=" + ",".join(APP_CONTRACT["screens"]))
    print("data_source=" + APP_CONTRACT["data_source"])
    print("formula=" + APP_CONTRACT["delegated_review_formula"])
    print(f"created={records[-1].item_id}:{records[-1].title}")
    print("status=" + records[-1].status)
    print(f"contract_signed={records[-1].contract_signed}")
    print("review_queue=" + ",".join(record.title for record in queue))
    print("delegation=" + delegation_report())


if __name__ == "__main__":
    main()
