# Content cannot be displayed with "You do not have sufficient privileges to access the page"

## Summary

When trying to access the Jira Visualforce page user sees the following error.

![contentId-3091629303](/cms_trial/assets/b71d3a47-5660-428b-ab69-6f6321de20b4.png?version=1&modificationDate=1678792064684&cacheVersion=1&api=v2)

This error message can appear even if the user profile has the Apex access class enabled, as mentioned in the following page - ["Create Jira Issues" and "Associate" Buttons are visible to admins only)](/cms_trial/space/CSFJIRA/2256275346/%22Create+Jira+Issues%22+and+%22Associate%22+buttons+are+visible+to+admins+only/).

## Environment

- Jira Cloud
- Jira DC

## Diagnostics Steps

Not applicable.

## Cause

This issue is usually related to users not having their profile enabled in the Security settings of the Visualforce Page as shown in the image below:

![Security settings of the Visualforce Page.png](/cms_trial/assets/6cebb6cc-d1bc-4aa7-bf20-58db74440e45.png)

## Workaround

Not applicable.

## Resolution

This can be fixed in the Visualforce page security configuration. In Salesforce, go to **Setup >** (on the quick find box)  **Visualforce Page > 'Your\_VisualforcePage' > Security**as shown below:

![contentId-3091629303](/cms_trial/assets/d5a49f7e-8d9f-4a3b-811b-595f7c50e099.png)

Under **JiraIssuesCasePage**, add the profile of the users affected by this as shown below:

![contentId-3091629303](/cms_trial/assets/df50a429-32a7-4c2a-8491-255ef12e4a34.png?version=1&modificationDate=1678792064374&cacheVersion=1&api=v2)