# How to resolve Unauthorized Endpoint or The session has expired. Please refresh the page error.

## Summary

After applying the [API access token](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/) on the Salesforce package an *Unauthorized Endpoint* message appears, and the page is stuck in a loop.

![contentId-3100410230](/cms_trial/assets/50f21f3d-2e3f-4753-908b-f909684daf0d.png)

Another error that can be seen after adding the API token:

![contentId-3100410230](/cms_trial/assets/e648e999-dc05-494e-852d-ac94eb33f450.png)

## Environment

- Jira Cloud or Jira Server

## Cause

| Environment | Cause |
| --- | --- |
| Cloud | This is usually caused by the Connector's server URL not being configured in 'Remote Site Settings'. |
| Server | This is usually caused by the Jira instance URL not being configured in 'Remote Site Settings'. |

## Resolution

| Environment | Resolution |
| --- | --- |
| Cloud | 1. Go to the Salesforce page. In the **Quick Find** box in the sidebar, type "*remote site settings*". 2. Click the **Remote Site Settings** link that appears. 3. On the **All Remote Sites** screen, click the **New Remote Site** button. 4. On the **Edit Remote Sites** screen, enter the following details: **Remote Site Name:** `Jira` **Remote Site URL:**<https://sfjc.integration.appfire.app> 5. Click **Save**. 6. Please revoke the access from both ends 7. [Re-authorize the connection](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/) 8. [Copy a new API Token from the Connector configuration in JIRA](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/) |
| Server | 1. Go to the Salesforce page. In the **Quick Find** box in the sidebar, type "*remote site settings*". 2. Click the **Remote Site Settings** link that appears. 3. On the **All Remote Sites** screen, click the **New Remote Site** button. 4. On the **Edit Remote Sites** screen, enter the following details: **Remote Site Name:** `Jira` **Remote Site URL:**`<enter your Jira instance URL>` 5. Click **Save.** 6. Revoke the access from both ends. 7. [Re-authorize the connection.](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/) 8. [Copy a new API Token from the Connector configuration in JIRA](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/). |

If, after following all these steps, the issue persists, please verify that your Jira instance meets all the system requirements; you can find more information about it[here](/cms_trial/space/CSFJIRA/1873412305/System+and+platform+requirements/).