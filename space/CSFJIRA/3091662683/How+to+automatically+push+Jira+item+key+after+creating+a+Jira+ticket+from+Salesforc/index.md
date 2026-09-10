# How to automatically push Jira item key after creating a Jira ticket from Salesforc

Jira issue key is not being pushed to Salesforce automatically after creating a Jira ticket from Salesforce or on the next sequential update on the Jira ticket, even though the **Auto-Push** option is toggled in the associated Jira ticket or Salesforce record.

This is because the **Auto-Push** option from Jira to Salesforce only pushes mapped fields with updated values. The feature doesn’t push all the mapped fields when a Jira ticket is updated. The Jira issue key is a static field, so it would not be pushed.

## Before you start

Make sure that:

- The Jira issue **Key** field is mapped under the expected Project and Issue Type. To learn more, see [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

![image-20240913-085519.png](/cms_trial/assets/f60add19-ddad-451a-93b4-ced1ff31cf41.png)

## Create Jira tickets through the Jira Issues Lightning Component

When creating a Jira ticket from Salesforce, ensure that the **After Creating** option is set to **Pull from Jira**.

![Pull from Jira.png](/cms_trial/assets/9c171ca2-51f4-4163-b328-69d7e6c4f1ed.png)

A notification that a pull from Jira is happening is visible after the Jira ticket is created.

## Create Jira tickets using Apex Trigger

When the following trigger is set to create a Jira ticket automatically, it will not follow the **After Creating** setup, and a pull will not happen after the creation:

```text
JCFS.API.createJiraIssue('<ProjectID>', '<IssueTypeID>');
```

You can use the following Apex Trigger to follow the default setup.

```text
JCFS.API.createJiraIssueWithDefaultPostAction('<ProjectID>', '<IssueTypeID>');
```

To configure the **Default Presets**, see [Configure connection settings](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1463943741/Configure+connection+settings#Default-Presets).

## Use workflow post functions

The Connector also provides workflow post functions, which you can use to achieve this.

**Before you start**

1. Verify the Jira **Key** field is mapped to a Salesforce field
2. In Jira, go to the bound project’s **Project Settings** > **Request Management** > **Workflows**.
3. Click **Edit** next to your mapped issue type.
4. Click **Diagram**, and click the **Create** arrow.
5. Select **Post Functions.**

   ![Post functions.png](/cms_trial/assets/ead8c5b2-db39-4590-953d-d0adafad77bc.png)
6. Click **Add post function** and select **Push to Salesforce** to add it.  
   The created post function is visible under the **Post Functions** bookmark.

   ![Push mapped issue fields.png](/cms_trial/assets/a6009078-1199-465c-9797-a2e6aba1a0a7.png)
7. Publish the workflow to apply your changes.

## Test your solution

After implementing any of these options, create a test Jira ticket from Salesforce to verify the Jira issue key appears correctly in your Salesforce record.

## Related articles

[Configure workflow post functions in Jira](/cms_trial/space/CSFJIRA/1873969278/Configure+workflow+post+functions+in+Jira/)