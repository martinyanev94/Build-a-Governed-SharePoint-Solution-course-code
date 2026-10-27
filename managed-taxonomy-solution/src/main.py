TAXONOMY = {
    "Department": {
        "hr-001": "Human Resources",
        "eng-001": "Engineering",
    },
    "Topic": {
        "onb-001": "Onboarding",
        "benefits-001": "Benefits",
    },
}

CONTENT = [
    {"title": "Policy-Remote-Work", "Department": ["eng-001"], "Topic": ["benefits-001"]},
    {"title": "Policy-Onboarding", "Department": ["hr-001"], "Topic": ["onb-001"]},
    {"title": "Onboarding-Checklist", "Department": ["hr-001"], "Topic": ["onb-001"]},
]


def filter_content(content, taxonomy, field, term_id):
    if term_id not in taxonomy[field]:
        raise ValueError(f"Unknown term {term_id!r} in {field}")
    return [
        item for item in content
        if term_id in item.get(field, [])
    ]


if __name__ == "__main__":
    department_results = filter_content(
        CONTENT, TAXONOMY, "Department", "hr-001"
    )
    print("Department = Human Resources")
    for item in department_results:
        print(item["title"])
