# An "Invalid Query!" Error pops up when configuring connection in Jira

## Problem

When configuring a connection in Jira, an error message “Invalid Query!” appears.

![Connector for Salesforce & Jira Invalid Query error message in connection configuration](/cms_trial/assets/fd3beb96-3885-4689-be06-12e2bd6534c1.png)

## **Before you start**

Make sure you have:

- Administrator rights in Salesforce - only administrators can edit the integration user

Not sure which user is the integration user? Check out [Determine the Salesforce integration user](https://appfire.atlassian.net/wiki/x/aAZGu) before proceeding.

## Solution

One possible cause is that the Salesforce integration user doesn't have the **View Setup and Configuration** permission enabled. This permission is required for the [Configure email notifications to notify Salesforce users](https://support.appfire.com/space/CSFJIRA/1873773017/Configure+email+notifications+to+notify+Salesforce+users) feature.

To resolve the issue, enable the permission in Salesforce:

1. Log in to Salesforce as an administrator.
2. In Salesforce, in the upper right corner, click the gear icon (▢) and select **Setup**.
3. In the **Quick Find** box, type **Profiles**.
4. Click **Profiles**.
5. Find the profile assigned to the integration user and click **Edit**.
6. Scroll down to the *Administrative Permissions* section.
7. Locate and enable **View Setup and Configuration**.
8. Click **Save**.

After enabling the permission, retry configuring the connection in Jira. The error should no longer appear.