from dataclasses import dataclass


@dataclass(frozen=True)
class Resource:
    name: str
    location: str
    audience: str


RESOURCES = [
    Resource("Files", "Documents/General", "Northstar members"),
    Resource("Guidance", "Guidance library", "Northstar members"),
    Resource("Onboarding", "HR Onboarding list", "Northstar members"),
]


def can_view(resource: Resource, viewer: str, members: set[str]) -> bool:
    return viewer in members and resource.audience == "Northstar members"


def main() -> None:
    members = {"Alex", "Sam", "Priya"}
    for resource in RESOURCES:
        print(f"{resource.name} -> {resource.location} [{resource.audience}]")

    viewer = "Jordan"
    result = "allowed" if can_view(RESOURCES[0], viewer, members) else "denied"
    print(f"{viewer}: {result}")


if __name__ == "__main__":
    main()
