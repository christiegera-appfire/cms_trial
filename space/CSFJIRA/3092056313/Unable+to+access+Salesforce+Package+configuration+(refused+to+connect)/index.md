# Unable to access Salesforce Package configuration (refused to connect)

## Summary

After the Salesforce package is installed successfully, clicking on the configuration link on the installed packages results in a "refused to connect" error.

In Chrome:

![contentId-3092056313](/cms_trial/assets/4a62282e-b907-4b0c-8210-7440b945522a.png?version=1&modificationDate=1678796547627&cacheVersion=1&api=v2)

In Firefox:

![contentId-3092056313](/cms_trial/assets/ed5f74d7-1c1d-40af-a38a-6180dd9f6270.png?version=1&modificationDate=1678796547845&cacheVersion=1&api=v2)

## Environment

- Jira Cloud or Jira Data Center
- All compatible Connector versions

## Diagnostics Steps

Not applicable.

## Cause

Clickjack Protection is enabled in Salesforce.

## Workaround

Not applicable.

## Resolution

[Disable the clickjack protection](https://help.salesforce.com/articleView?id=pardot_sf_connector_disable_clickjack.htm&type=5) in Salesforce Setup:

1. From Setup, enter "*Session Settings*" in the Quick Find box, then select **Session Settings**.
2. In the Clickjack Protection section, deselect **Enable clickjack protection for customer Visualforce pages with headers disabled**.
3. Save your settings.

   ![Enable Clickjack protection for customer Visualforce.png](/cms_trial/assets/a7f5d138-d797-43cb-ad21-e8720428c2d6.png)