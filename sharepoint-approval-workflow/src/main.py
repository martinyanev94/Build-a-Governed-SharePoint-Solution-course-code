from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    DRAFT = "Draft"
    PENDING = "Pending approval"
    APPROVED = "Approved"
    REJECTED = "Rejected"


@dataclass
class Page:
    item_id: int
    title: str
    status: Status = Status.DRAFT
    decision_note: str = ""


def submit(page: Page, editor: str) -> Page:
    if page.status is not Status.DRAFT:
        raise ValueError("only drafts can be submitted")
    page.status = Status.PENDING
    page.decision_note = f"Submitted by {editor}"
    return page


def approve(page: Page, approver: str) -> Page:
    if page.status is not Status.PENDING:
        raise ValueError("only pending pages can be approved")
    page.status = Status.APPROVED
    page.decision_note = f"Approved by {approver}"
    return page


def reject(page: Page, approver: str, note: str) -> Page:
    if page.status is not Status.PENDING or not note.strip():
        raise ValueError("pending pages need a rejection note")
    page.status = Status.REJECTED
    page.decision_note = f"Rejected by {approver}: {note}"
    return page


def run_demo() -> None:
    page = Page(42, "Remote work policy")
    submit(page, "Alex")
    approve(page, "Jordan Lee")
    print(page.item_id, page.status.value, page.decision_note)

    page.status = Status.DRAFT
    submit(page, "Alex")
    reject(page, "Jordan Lee", "Add regional exceptions")
    print(page.item_id, page.status.value, page.decision_note)


if __name__ == "__main__":
    run_demo()
