from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class NavigationEntry:
    title: str
    url: str
    parent: Optional[str] = None


def navigation_depth(entry: NavigationEntry, entries: dict[str, NavigationEntry]) -> int:
    depth = 1
    parent = entry.parent
    while parent is not None:
        depth += 1
        parent = entries[parent].parent
    return depth


def build_plan() -> dict[str, object]:
    entries = {
        "Home": NavigationEntry("Home", "/sites/northstar"),
        "Departments": NavigationEntry("Departments", "#"),
        "Finance": NavigationEntry("Finance", "/sites/finance", "Departments"),
        "People Operations": NavigationEntry(
            "People Operations", "/sites/people-operations", "Departments"
        ),
        "Guidance": NavigationEntry("Guidance", "/sites/northstar/SitePages/guidance"),
    }
    depths = {title: navigation_depth(entry, entries) for title, entry in entries.items()}
    return {
        "hub": "Northstar",
        "associated_sites": ["Finance", "People Operations"],
        "navigation_order": list(entries),
        "depths": depths,
    }


if __name__ == "__main__":
    plan = build_plan()
    print(f"hub={plan['hub']}")
    print(f"associated_sites={', '.join(plan['associated_sites'])}")
    print(f"max_navigation_depth={max(plan['depths'].values())}")
    print(f"navigation={' > '.join(plan['navigation_order'])}")
