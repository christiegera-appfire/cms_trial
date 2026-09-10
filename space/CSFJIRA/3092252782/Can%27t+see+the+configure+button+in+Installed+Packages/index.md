# Can't see the configure button in Installed Packages

## Summary

Certain users cannot see the **Configure** button under Installed Packages in Salesforce. This means they cannot access the connector's connection settings.

![contentId-3092252782](/cms_trial/assets/6aeea964-0749-4fdf-aec1-6493d1885d02.png)

## Diagnostics Steps

Not applicable.

## Cause

The user does not have this permission in Salesforce - "Download AppExchange Packages".

## Workaround

Not applicable.

## Resolution

In order to grant this permission:

1. In Salesforce go to **Setup** → **Users** → **Profiles.**

1. Search for “General User Permissions”and make sure there is a check on **Download AppExchange Packages**. It should look like this:

![Download AppExchange Packags .png](/cms_trial/assets/9e21e4a8-da76-40e0-9023-2b2a914352fa.png)

The user must have a **Salesforce license** to use this option.