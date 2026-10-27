from dataclasses import dataclass

CATEGORY_RULES = {
    "content": ("publish", "policy", "news", "video", "link"),
    "collaboration": ("shared files", "co-author", "teams channel"),
    "automation": ("notify", "approval", "when", "changes"),
    "extensibility": ("custom", "spfx", "api", "power apps"),
}

@dataclass(frozen=True)
class PortalRequirement:
    text: str
    category: str

def classify(text: str) -> str:
    normalized = text.lower()
    matches = [
        category
        for category, signals in CATEGORY_RULES.items()
        if any(signal in normalized for signal in signals)
    ]
    return "+".join(matches) if matches else "needs-discovery"

def map_requirements(texts: list[str]) -> list[PortalRequirement]:
    return [PortalRequirement(text, classify(text)) for text in texts]

if __name__ == "__main__":
    requests = [
        "Publish the remote-work policy",
        "Show the team's shared files in Teams",
        "Notify HR when onboarding status changes",
        "Add a custom operational panel",
        "Publish the policy and notify HR when it changes",
    ]
    for item in map_requirements(requests):
        print(f"{item.category}: {item.text}")
