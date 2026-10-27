from dataclasses import dataclass
from datetime import date
from typing import Dict, List

ONBOARDING_FIELDS = {
    "Employee name": "text",
    "Start date": "date",
    "Owner": "person",
    "Status": ["Ready", "In progress", "Blocked"],
    "Next review": "date",
}


@dataclass
class OnboardingRecord:
    employee_name: str
    start_date: date
    owner: str
    status: str
    next_review: date


def create_record(employee_name: str, start_date: date, owner: str, status: str, next_review: date) -> OnboardingRecord:
    if status not in ONBOARDING_FIELDS["Status"]:
        raise ValueError(f"Unsupported status: {status}")
    return OnboardingRecord(employee_name, start_date, owner, status, next_review)


def filter_records(records: List[OnboardingRecord], *, owner: str = "", needs_review: bool = False, today: date = date(2026, 11, 1)) -> List[OnboardingRecord]:
    selected = records
    if owner:
        selected = [record for record in selected if record.owner == owner]
    if needs_review:
        selected = [record for record in selected if record.next_review < today]
    return selected


if __name__ == "__main__":
    records = [
        create_record("Maya Chen", date(2026, 11, 2), "Jordan Lee", "Ready", date(2026, 10, 29)),
        create_record("Luis Ortega", date(2026, 11, 9), "Jordan Lee", "In progress", date(2026, 11, 5)),
        create_record("Priya Shah", date(2026, 11, 16), "Ana Gomez", "Blocked", date(2026, 11, 3)),
    ]
    print("Jordan Lee:", [record.employee_name for record in filter_records(records, owner="Jordan Lee")])
    print("Needs review:", [record.employee_name for record in filter_records(records, needs_review=True)])
