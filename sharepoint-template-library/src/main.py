from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class TemplateRecord:
    name: str
    scope: str
    configuration: dict[str, Any]
    live_data_policy: str


def build_onboarding_template() -> TemplateRecord:
    return TemplateRecord(
        name="Northstar onboarding list",
        scope="list",
        configuration={
            "columns": ["Employee", "Department", "Status", "Owner", "ReviewDate"],
            "views": ["Owner: Jordan Lee", "Needs review"],
        },
        live_data_policy="never-copy",
    )


def apply_template(template: TemplateRecord) -> dict[str, Any]:
    return {
        "name": "Department-B onboarding list",
        "configuration": dict(template.configuration),
        "items": [],
    }


def validate_applied_template(
    template: TemplateRecord, target: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    if target["configuration"] != template.configuration:
        errors.append("configuration does not match template")
    if template.live_data_policy == "never-copy" and target["items"]:
        errors.append("live data was copied into the target")
    return errors


def main() -> None:
    template = build_onboarding_template()
    target = apply_template(template)
    errors = validate_applied_template(template, target)
    print(f"target={target['name']}")
    print(f"columns={len(target['configuration']['columns'])}")
    print(f"views={len(target['configuration']['views'])}")
    print(f"items={len(target['items'])}")
    print(f"validation={'passed' if not errors else '; '.join(errors)}")


if __name__ == "__main__":
    main()
