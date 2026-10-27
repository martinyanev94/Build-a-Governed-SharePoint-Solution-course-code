param(
    [ValidateSet("Export", "Apply")]
    [string]$Mode = "Export",
    [string]$SourceUrl = "https://tenant.sharepoint.com/sites/northstar-source",
    [string]$TargetUrl = "https://tenant.sharepoint.com/sites/northstar-target",
    [string]$TemplatePath = ".\northstar-template.xml",
    [switch]$PagesOnly
)

if ($Mode -eq "Export") {
    Connect-PnPOnline -Url $SourceUrl -Interactive
    if ($PagesOnly) {
        Get-PnPSiteTemplate -Out $TemplatePath -Handlers Pages,PageContents -IncludeAllPages -PersistBrandingFiles
    } else {
        Get-PnPSiteTemplate -Out $TemplatePath
    }
    Write-Host "Exported template to $TemplatePath"
} else {
    Connect-PnPOnline -Url $TargetUrl -Interactive
    Invoke-PnPSiteTemplate -Path $TemplatePath
    Write-Host "Applied template to $TargetUrl"
}
