from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class PageSection:
    title: str
    web_part: str
    items: List[str]

@dataclass(frozen=True)
class PublishingPage:
    title: str
    sections: List[PageSection]

def northstar_page() -> PublishingPage:
    return PublishingPage(
        title="Policy and onboarding",
        sections=[
            PageSection(
                title="Start here",
                web_part="Text",
                items=["Policy guidance and onboarding actions"],
            ),
            PageSection(
                title="Policy documents",
                web_part="Highlighted content",
                items=["Remote work policy.pdf", "Benefits guide.docx"],
            ),
            PageSection(
                title="Latest updates",
                web_part="News",
                items=["Benefits update"],
            ),
            PageSection(
                title="Onboarding actions",
                web_part="List",
                items=["Jordan Lee — Needs review", "Casey Morgan — Complete"],
            ),
        ],
    )

def render_page(page: PublishingPage) -> str:
    lines = [f"PAGE: {page.title}"]
    for section in page.sections:
        lines.append(f"{section.web_part}: {section.title}")
        lines.extend(f"- {item}" for item in section.items)
    return "\n".join(lines)

if __name__ == "__main__":
    print(render_page(northstar_page()))
