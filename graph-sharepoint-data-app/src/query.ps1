$siteId = $env:SHAREPOINT_SITE_ID
Install-Module Microsoft.Graph.Sites -Scope CurrentUser -Force
Connect-MgGraph -Scopes "Sites.Read.All"
$site = Get-MgSite -SiteId $siteId
$lists = Get-MgSiteList -SiteId $siteId
$site | Select-Object Id, DisplayName
$lists.Value | Select-Object Id, DisplayName
