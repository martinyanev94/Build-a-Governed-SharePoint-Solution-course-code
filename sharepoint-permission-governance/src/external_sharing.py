from dataclasses import dataclass

SHARING_LEVELS = (
    "Anyone",
    "New and existing guests",
    "Existing guests",
    "Only people in your organization",
)


@dataclass(frozen=True)
class SharingRecommendation:
    tenant_limit: str
    site_setting: str
    effective_setting: str
    approved_domains: tuple[str, ...]
    library_audience: str
    permission_exception: str


def recommend_external_sharing(
    tenant_policy: str,
    site_request: str,
    approved_domains: tuple[str, ...],
    library_audience: str,
    permission_exception: str,
) -> SharingRecommendation:
    tenant_rank = SHARING_LEVELS.index(tenant_policy)
    site_rank = SHARING_LEVELS.index(site_request)
    effective = SHARING_LEVELS[max(tenant_rank, site_rank)]
    return SharingRecommendation(
        tenant_limit=tenant_policy,
        site_setting=site_request,
        effective_setting=effective,
        approved_domains=approved_domains,
        library_audience=library_audience,
        permission_exception=permission_exception,
    )


if __name__ == "__main__":
    recommendation = recommend_external_sharing(
        tenant_policy="New and existing guests",
        site_request="Existing guests",
        approved_domains=("partners.example.com",),
        library_audience="Approved Partner Materials",
        permission_exception="none",
    )
    print(f"tenant_limit: {recommendation.tenant_limit}")
    print(f"site_setting: {recommendation.site_setting}")
    print(f"effective_setting: {recommendation.effective_setting}")
    print(f"domain_scope: {', '.join(recommendation.approved_domains)}")
    print(f"library_audience: {recommendation.library_audience}")
    print(f"permission_exception: {recommendation.permission_exception}")
