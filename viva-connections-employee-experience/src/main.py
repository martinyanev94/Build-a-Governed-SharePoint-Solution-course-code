def build_northstar_manifest():
    return {
        "experience_name": "Northstar",
        "feed_items": [
            {
                "title": "Benefits enrollment update",
                "source": "organizational-news",
                "audience": "all-employees",
                "priority": "boosted",
            },
            {
                "title": "New-hire onboarding guide",
                "source": "followed-portal",
                "audience": "all-employees",
                "priority": "standard",
            },
            {
                "title": "Safety briefing",
                "source": "organization-video",
                "audience": "all-employees",
                "priority": "standard",
            },
        ],
        "resources_url": "/sites/Northstar/SitePages/Home.aspx",
    }


def verify_manifest(manifest):
    required_sources = {"organizational-news", "followed-portal", "organization-video"}
    actual_sources = {item["source"] for item in manifest["feed_items"]}
    missing = required_sources - actual_sources
    if missing:
        return ["Missing feed sources: " + ", ".join(sorted(missing))]
    if not manifest["resources_url"]:
        return ["Resources link is empty"]
    return ["Feed contract is complete", "Resources link is present"]


if __name__ == "__main__":
    manifest = build_northstar_manifest()
    for item in manifest["feed_items"]:
        print(item["title"], "->", item["source"], "[" + item["priority"] + "]")
    print("\n".join(verify_manifest(manifest)))
