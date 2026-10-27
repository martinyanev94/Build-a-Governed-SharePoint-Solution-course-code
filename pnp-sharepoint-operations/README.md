# PnP SharePoint operations

This package contains a repeatable provisioning script and a search-extension plan for the Northstar workspace.

## Prerequisites

- PowerShell 7.2
- Interactive access to the source and target SharePoint sites
- PnP PowerShell

Install the module for the current user:

```powershell
Install-Module PnP.PowerShell -Scope CurrentUser
```

## Export configuration

From this directory, export configuration from the source site:

```powershell
.\src\provision.ps1 -Mode Export -SourceUrl "https://tenant.sharepoint.com/sites/northstar-source" -TemplatePath ".\northstar-template.xml"
```

Review the generated template before applying it. A template describes configuration; it is not a live-data migration.

## Apply configuration

Apply the reviewed template to a target site:

```powershell
.\src\provision.ps1 -Mode Apply -TargetUrl "https://tenant.sharepoint.com/sites/northstar-target" -TemplatePath ".\northstar-template.xml"
```

Verify the resulting target structure separately from permissions and live records.

## Focused page export

For modern pages and related page content only:

```powershell
.\src\provision.ps1 -Mode Export -PagesOnly -TemplatePath ".\northstar-pages.xml"
```

Review the focused template before applying it.

## Search extension plan

`search-plan.json` specifies a modern page with Search Box, Search Filters, Search Verticals, and Search Results web parts. Verify the query connection, filtering behavior, vertical behavior, indexing, and results for representative viewers. Search configuration does not bypass SharePoint permissions.
