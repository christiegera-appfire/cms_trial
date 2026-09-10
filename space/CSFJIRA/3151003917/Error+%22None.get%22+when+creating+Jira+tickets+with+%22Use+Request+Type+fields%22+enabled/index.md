# Error "None.get" when creating Jira tickets with "Use Request Type fields" enabled

## Problem

When attempting to create a Jira Service Management (JSM) work item from Salesforce using the **Jira Issues Lightning Component**, a `None.get` error appears, and the work item fails to create. This happens only when the **Use Request type fields** option is enabled in the *Create Jira Issue* window in Salesforce. Creating the same work item type directly in Jira works without any problems.

## Before you start

- You'll need **Jira Administrator** access to make the configuration change below.
- The fix takes just a few minutes and doesn't require changes on the Salesforce side.

## Solution

The **Request Type** field is missing from the Jira *Create Issue* screen used with the issue type you're trying to create from Salesforce. Jira normally adds this field automatically, but it can be removed unintentionally during project reconfiguration.

1. Open your affected Jira Service Management *Space settings*.
2. Navigate to **Request management** > **Screens**.
3. Select the *Create issue* screen of the affected issue type.  
   For example, *Developer escalation*.

   ![Connector for Salesforce & Jira JSM Request Management Screens page with Create Issue screen selected](/cms_trial/assets/29a89e57-650b-432c-8230-35d01f5f3f16.png)
4. Add the **Request Type** field to the screen.
5. Switch back to Salesforce and refresh the *Create Jira Issue* window.
6. Try creating the work item again with the **Use Request type fields** option enabled.