from dataclasses import dataclass
from enum import Enum
from typing import List


class Host(str, Enum):
    SHAREPOINT_FULL_PAGE = "SharePointFullPage"
    TEAMS_TAB = "TeamsTab"
    TEAMS_PERSONAL_APP = "TeamsPersonalApp"


@dataclass
class StatusItem:
    name: str
    status: str


class StatusExperience:
    def __init__(self, host: Host, items: List[StatusItem]):
        self.host = host
        self.items = items

    def render(self) -> str:
        layout = "wide" if self.host == Host.SHAREPOINT_FULL_PAGE else "compact"
        lines = [f"Northstar Status — {self.host.value}", f"layout={layout}"]
        lines.extend(f"{item.name}: {item.status}" for item in self.items)
        return "\n".join(lines)


SUPPORTED_HOSTS = [
    "SharePointWebPart",
    "TeamsPersonalApp",
    "TeamsTab",
    "SharePointFullPage",
]

ICON_SIZES = {
    "outline": (32, 32),
    "color": (192, 192),
}


def build_demo() -> List[StatusItem]:
    return [
        StatusItem("Benefits", "Ready"),
        StatusItem("Equipment", "In progress"),
        StatusItem("Manager review", "Blocked"),
    ]


def main() -> None:
    items = build_demo()
    for host in (Host.SHAREPOINT_FULL_PAGE, Host.TEAMS_TAB):
        print(StatusExperience(host, items).render())
        print()


if __name__ == "__main__":
    main()
