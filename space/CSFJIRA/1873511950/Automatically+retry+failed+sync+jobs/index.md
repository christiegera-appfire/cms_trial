# Automatically retry failed sync jobs

You can set Connector for Salesforce & Jira to retry failed Salesforce auto-sync jobs automatically. These jobs occasionally fail due to service disruptions or other factors.

Retries are only triggered when the server responds with a `503 - Service Unavailable` status code.

Failed jobs are automatically retried up to five times, at approximately 5, 10, 30, 60, and 90 minutes from the first failure.

This feature is not enabled by default. To enable it, a Salesforce administrator must follow the steps below.

For additional information about this feature and to learn how to view the status of failed sync jobs, refer to [View all failed sync jobs and retry status on Salesforce](/cms_trial/space/CSFJIRA/3091957712/View+all+failed+sync+jobs+and+retry+status+on+Salesforce/).

## Steps to enable auto-sync retry

1. In Salesforce, navigate to **Setup.**
2. Enter `Custom Settings` in the **Quick Find** field and click the **Custom Settings** entry when it appears in the list.
3. In the *Label* column, click **Sync Feature**. The *Sync Feature* page opens.
4. Click **New** to continue.
5. Click the **Enable Autosync Retry** option to enable it.
6. Click **Save**.

The Autosync retry option is now set.

## Related information

- [View all failed sync jobs and retry status on Salesforce](/cms_trial/space/CSFJIRA/3091957712/View+all+failed+sync+jobs+and+retry+status+on+Salesforce/)