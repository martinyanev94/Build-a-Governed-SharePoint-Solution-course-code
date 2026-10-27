from dataclasses import dataclass


@dataclass(frozen=True)
class SearchConfiguration:
    page_title: str
    query: str
    search_scope: str
    required_refinement: str


@dataclass(frozen=True)
class SearchEvidence:
    page_opened: bool
    published: bool
    observed_query: str
    result_titles: tuple[str, ...]
    observed_scope: str
    available_refinements: tuple[str, ...]


def verify_search(
    config: SearchConfiguration, evidence: SearchEvidence
    ) -> tuple[bool, list[str]]:
    failures: list[str] = []
    if not evidence.page_opened or not evidence.published:
        failures.append("Page is not published and visible to the intended audience")
    if evidence.observed_query != config.query:
        failures.append("Observed query differs from configured query")
    if evidence.observed_scope != config.search_scope:
        failures.append("Observed search scope differs from configured scope")
    if (evidence.observed_query == config.query
            and evidence.observed_scope == config.search_scope):
        if config.page_title not in evidence.result_titles:
            failures.append("Published page was not returned for the configured query")
        if config.required_refinement not in evidence.available_refinements:
            failures.append("Required refinement is not available")
    return not failures, failures


def northstar_example() -> tuple[SearchConfiguration, SearchEvidence]:
    config = SearchConfiguration(
        page_title="Benefits enrollment",
        query="Benefits enrollment",
        search_scope="Site",
        required_refinement="Policy",
    )
    evidence = SearchEvidence(
        page_opened=True,
        published=True,
        observed_query="Benefits enrollment",
        result_titles=("Benefits enrollment", "Benefits contacts"),
        observed_scope="Site",
        available_refinements=("Policy",),
    )
    return config, evidence


if __name__ == "__main__":
    config, evidence = northstar_example()
    passed, failures = verify_search(config, evidence)
    if passed:
        print(
            f"PASS: {config.page_title} is published, visible, and "
            f"discoverable in {config.search_scope} scope."
        )
    else:
        print("FAIL: search acceptance check")
        for failure in failures:
            print(f"- {failure}")
