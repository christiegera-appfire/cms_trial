# Understand Salesforce API call usage

Connector for Salesforce & Jira uses Salesforce APIs to communicate and synchronize with Salesforce.

However, Salesforce places a daily limit on API calls, and it is possible to run into a `REQUEST_LIMIT_EXCEEDED` error message, especially if you have other applications that also make multiple API calls. This daily limit depends on what Salesforce edition your organization is using.

## Check Salesforce API call usage from within Salesforce

As an admin, you can see API call usage from within Salesforce. This process allows you to see general API call usage for all Salesforce applications, not just for Connector for Salesforce & Jira.

1. In Salesforce, go to **Settings** > **Setup**.
2. In the sidebar, under *SETTINGS*, click **Company Settings** > **Company Information**.

   ![2025-10-16_11-27-51.png](/cms_trial/assets/0d3501d3-cfcc-404c-942e-4428daf87242.png)
3. Under *Organization Detail*, you can see the number of API Requests for the past 24 hours.

   ![64dcf649-7bf2-424e-9291-90a8be6be772.png](/cms_trial/assets/fc795b16-4224-456f-86f0-055a0b5c53a9.png)

## Estimate Salesforce API call usage

Consult the following table to estimate Salesforce API calls the Connector requests based on each major operation:

| **Operation** | **Estimated API call usage** |
| --- | --- |
| User | Viewing a Jira issue | 1 API call per page load, if there is any association. |
| Associating a Salesforce record | 1 API call per search. Delayed search keystrokes will invoke 1 API call each.  1 to 2 API calls to complete an association, depending on the association configuration. |
| Creating a Salesforce record | 1 to 4 API calls to complete a record creation, depending on the association configuration.  If attachment sync is enabled, an additional 5 API calls per attachment. |
| Updating a Jira issue | 1 to 2 calls for each non-view-only association. |
| Admin | Setting up connection | 1 API call per setup.  5 additional API calls if importing from Salesforce compact layout. |
| Configuring a connection | 2 API calls per page load. |
| Configuring a binding | 1 API call per page load.  1 API call per mapping dialog load. |

## Related information

- [System and platform requirements](/cms_trial/space/CSFJIRA/1873412305/System+and+platform+requirements/)
- [Getting help](/cms_trial/space/CSFJIRA/2258337826/Help+and+support/)