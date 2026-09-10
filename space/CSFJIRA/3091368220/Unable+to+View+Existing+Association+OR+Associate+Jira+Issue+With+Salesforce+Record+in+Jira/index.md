# Unable to View Existing Association OR Associate Jira Issue With Salesforce Record in Jira

## Summary

1. The Salesforce panel in a Jira ticket does not show the existing associations and the Salesforce record keeps on spinning. This could happen to account, opportunity, contact, etc.

   ![contentId-3091368220](/cms_trial/assets/838a3470-ab24-4117-a61e-3573d121c97c.PNG?version=1&modificationDate=1678858811197&cacheVersion=1&api=v2)
2. When searching for a Salesforce record, no results are returned and an endless searching progress is observed.

   ![contentId-3091368220](/cms_trial/assets/4c291989-7257-4bbf-aa02-0b9f4e0b4c5f.PNG?version=1&modificationDate=1678858811527&cacheVersion=1&api=v2)
3. In the browser console, you will see error messages as below:

   ![contentId-3091368220](/cms_trial/assets/f0013424-bf37-4d2b-a34e-6ebe1a317449.PNG?version=1&modificationDate=1678858811469&cacheVersion=1&api=v2)

## Environment

Not applicable.

## Diagnostics Steps

Not applicable.

## Cause

Salesforce object in the Connections' settings are configured with invalid fields. The invalid fields may exist due to permission or the field has been removed from Salesforce.

The examples of invalid fields are shown in Red text below.

![contentId-3091368220](/cms_trial/assets/74c4a24f-89cc-4877-85e4-20b278ec4540.PNG?version=1&modificationDate=1678858811409&cacheVersion=1&api=v2)

## Workaround

Not applicable.

## Resolution

Remove the invalid fields from the Connection's settings.