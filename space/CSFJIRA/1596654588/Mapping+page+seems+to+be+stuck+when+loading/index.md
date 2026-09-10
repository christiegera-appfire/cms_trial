# Mapping page seems to be stuck when loading

When trying to access the mapping section of **Bindings** (**Apps** > **Salesforce** > **Bindings** > **Mappings**), the page seems to be stuck when loading.

![contentId-1596654588](/cms_trial/assets/38ae5d49-c567-4fff-8c22-816287477e71.png)

## Environment

- Jira Cloud

## Diagnostics Steps

Should you face this issue, please do the following:

1. Open the browser's development window by right-clicking and selecting **Inspect**.

   ![contentId-1596654588](/cms_trial/assets/a326c003-82dd-4d00-883f-cecb1bdd8f9c.png)
2. Once in the development window, select the **Console** tab.

   ![console.png](/cms_trial/assets/b9fe483b-2ffa-4b30-bdb5-efedf31b1836.png)
3. With the development window open, reproduce the issue.
4. Confirm that you can see an error message which has this text - "Failed to read the 'sessionStorage' property from 'Window': Access is denied for this document":

   ![contentId-1596654588](/cms_trial/assets/ce411d9d-1ac7-4026-adfd-994e990ee438.png)

## Cause

This issue is caused by security settings in your Browser. Specifically, not allowing third-party cookies.

## Resolution

To resolve this issue, you will need to enable third-party cookies for the Atlassian domain in your browser.  Follow these steps for the Chrome browser:

1. At the top right, click the **Menu** icon▢and click **Settings**.
2. Click **Privacy and Security** > **Cookies and Site Data**.
3. In most browsers, you can allow specific sites to access third-party cookies if you have them blocked. In Chrome, scroll down until you see **Sites that can always use cookies**, and click **Add**.
4. In the *Add a site* window, paste or type in the Atlassian domain - [\*.]​[Products | Atlassian](http://atlassian.net/) and make sure the **Including third-party cookies** option is enabled (checked). Click **Add** to complete the step.

   ![contentId-1596654588](/cms_trial/assets/8481ecf9-27e8-4661-a591-fec4c6c956c4.png)