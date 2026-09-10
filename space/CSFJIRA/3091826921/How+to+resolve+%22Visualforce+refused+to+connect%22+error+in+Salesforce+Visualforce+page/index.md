# How to resolve "Visualforce refused to connect" error in Salesforce Visualforce page

## Summary

When configuring Visualforce pages for the Connector for Salesforce and Jira, a "<Salesforce-URL>.jcfs.visualforce.com refused to connect" error is displayed.

![contentId-3091826921](/cms_trial/assets/7b047385-2cea-4b26-8caf-465c3a91629d.png?version=1&modificationDate=1678795527421&cacheVersion=1&api=v2)

## Environment

- Jira
- Salesforce

## Diagnostics Steps

Not applicable.

## Cause

- **Clickjack Protection** setting being enabled in Salesforce.
- **Visualforce Cross-Origin Security Headers** setting being enabled in Salesforce.

## Workaround

Not applicable.

## Resolution

1. In Salesforce, go to **Setup** > **Security Controls** > **Session Settings.**
2. Scroll to **Clickjack Protection** > Uncheck the **Enable Clickjack protection for customer Visualforce pages with headers disabled** checkbox.

   ![Enable Clickjack protection for customer Visualforce.png](/cms_trial/assets/0a4591bf-41e1-4416-91e5-d45d0058de1d.png)
3. Scroll to **Visualforce Cross-Origin Security Headers** > Uncheck the **Cross-Origin Embedder Policy (COEP)** checkbox and then click **Save** at the bottom of the page.

   ![Cross-Origin Embedder Policy (COEP).png](/cms_trial/assets/385792f5-8bdb-4d28-99bd-115ebd02954d.png)