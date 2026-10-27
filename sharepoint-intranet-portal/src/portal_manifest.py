PORTAL = {
    "title": "Northstar Portal",
    "navigation": ["Guidance", "News", "Documents", "Support"],
    "content": [
        {"title": "Policy guide", "type": "page", "audience": "all"},
        {"title": "Benefits update", "type": "news", "audience": "all"},
        {"title": "Onboarding checklist", "type": "document", "audience": "HR Team Members"},
        {"title": "Support request", "type": "link", "audience": "all"},
    ],
}


def visible_content(viewer_groups):
    return [
        item for item in PORTAL["content"]
        if item["audience"] == "all"
        or item["audience"] in viewer_groups
    ]


if __name__ == "__main__":
    for viewer, groups in {
        "Maya": ["HR Team Members"],
        "Jordan": [],
    }.items():
        titles = [item["title"] for item in visible_content(groups)]
        print(f"{viewer}: {titles}")
