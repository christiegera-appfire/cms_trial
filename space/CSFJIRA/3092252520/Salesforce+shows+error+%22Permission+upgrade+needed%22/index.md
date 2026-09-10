# Salesforce shows error "Permission upgrade needed"

## Purpose

Due to certain configurations or validations on the workflow some modifications to the Jira issues are not performed by the Connector.

When unlinking the issue from the Salesforce case, errors are triggered as shown in the images below.

![image-20250603-135841.png](/cms_trial/assets/be2d65c1-1501-4f73-b440-9f0d071c2cab.png)

## Answer

There are two root causes for this issue:

## Missing Integration user

The integration user is missing the **Edit** issue permission in Jira.

### Jira Data Center

1. In Jira, go to **Project Settings** > **Project** **permissions**.
2. Click **Permission Helper**.
3. In the *Permission helper* pop-up window, select the affected issue that is unlinked, and check if the user has the **Edit** issue permission.
4. Grant the user the required permission.

### Jira Cloud

1. In Jira, go to **Project Settings** > **Project** **permissions**.
2. Search for *Edit Issues* permission and check if the project role **atlassian-addons-projects-access** is listed there.

   ![project permissions.png](/cms_trial/assets/d011db08-e345-4283-b80f-e71f8dc1a636.png)
3. If the role is missing, click **Actions** > **Edit Permission**.
4. Search for **Edit Issues** permission and click **Update.**
5. Grant the permission to the required project role and click **Update**.

## Issue status is set to be not editable in workflow (Jira DC only)

The status of the issue has the property "jira.issue.editable = false"

1. Read this [documentation](https://confluence.atlassian.com/adminjiraserver/workflow-properties-938847526.html#:~:text=Go%20to%20Administration%20%3E%20Issues.,to%20add%20a%20property%20for.) to understand how to access the workflow property.
2. Delete the property key "jira.issue.editable = false" if it exists.