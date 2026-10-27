from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Requirement:
    surface: str
    action: str
    needs_selection: bool


def choose_extension(requirement: Requirement) -> Dict[str, object]:
    if requirement.surface == "page":
        return {
            "type": "Application Customizer",
            "locations": ["top or bottom page placeholder"],
        }
    if requirement.surface == "field":
        return {
            "type": "Field Customizer",
            "locations": ["specified list or library field"],
        }
    if requirement.surface == "command":
        return {
            "type": "ListView Command Set",
            "locations": ["command bar", "context menu"],
        }
    if requirement.surface == "form":
        return {
            "type": "Form Customizer",
            "locations": ["create, edit, or display form"],
        }
    raise ValueError(f"Unsupported surface: {requirement.surface}")


def prototype(requirement: Requirement) -> Dict[str, object]:
    choice = choose_extension(requirement)
    return {
        **choice,
        "action": requirement.action,
        "selection_required": requirement.needs_selection,
    }


if __name__ == "__main__":
    request = Requirement("command", "archive", True)
    result = prototype(request)
    print(f"extension={result['type']}")
    print(f"location={' and '.join(result['locations'])}")
    print(f"selection_required={result['selection_required']}")
    print(f"action={result['action']}")
