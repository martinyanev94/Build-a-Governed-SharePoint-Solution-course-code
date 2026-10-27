from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class PageTranslation:
    name: str
    source_language: str
    target_language: str
    published: bool

    def storage_paths(self) -> tuple[Path, Path]:
        source = Path("Site Pages") / f"{self.name}.aspx"
        translation = Path("Site Pages") / self.target_language / f"{self.name}.aspx"
        return source, translation

def publish_report(page: PageTranslation) -> str:
    source, translation = page.storage_paths()
    state = "Published" if page.published else "Draft"
    return (
        f"source={source}\n"
        f"translation={translation}\n"
        f"target={page.target_language}\n"
        f"state={state}"
    )

if __name__ == "__main__":
    page = PageTranslation(
        name="Benefits-enrollment",
        source_language="en-US",
        target_language="fr-FR",
        published=True,
    )
    print(publish_report(page))
