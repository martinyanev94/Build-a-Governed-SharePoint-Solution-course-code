from dataclasses import dataclass, field
from typing import Dict, List

@dataclass(frozen=True)
class ContentType:
    name: str
    columns: List[str]

@dataclass
class ContentModel:
    central_types: Dict[str, ContentType] = field(default_factory=dict)
    consumers: Dict[str, List[str]] = field(default_factory=dict)

    def publish(self, content_type: ContentType, destinations: List[str]) -> None:
        self.central_types[content_type.name] = content_type
        for destination in destinations:
            self.consumers.setdefault(destination, []).append(content_type.name)

def describe(model: ContentModel) -> List[str]:
    lines = []
    for name, content_type in model.central_types.items():
        columns = ", ".join(content_type.columns)
        lines.append(f"central:{name} [{columns}]")
    for destination, content_types in model.consumers.items():
        lines.append(f"consumer:{destination} -> {', '.join(content_types)}")
    return lines

if __name__ == "__main__":
    model = ContentModel()
    onboarding = ContentType(
        name="Onboarding Record",
        columns=["Owner", "Status", "Review Date"],
    )
    model.publish(onboarding, ["HR Intake", "Policy Library"])
    print("\n".join(describe(model)))
