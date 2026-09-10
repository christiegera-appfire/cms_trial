# Associate Jira work item with Salesforce records and trigger post actions automatically

## Overview

Salesforce Apex API methods allow for associating a Jira work item with a Salesforce record or a list of Salesforce records and triggering a default action that happens immediately after an association. This simplifies the process of integrating Salesforce with Jira by eliminating the need for custom API code.

- `associateJiraIssue`- associates a Jira work item with a list of Salesforce records, for example, cases, accounts, or contacts. It doesn’t trigger default post-actions after the association.

  - Syntax**:** `associateJiraIssue(String jiraKey, List<SObject> sObjects)`
  - Parameters**:**

    - `jiraKey`: The Jira work item key
    - `sObject`: A type of Salesforce object for the records you want to associate with the specified Jira work item. To learn more about `sObject`, see the [Salesfors developers](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_sobject.htm) documentation.
- `associateJiraIssueWithDefaultPostActions` - associates a Jira work item with a list of Salesforce records and triggers default post-action. Administrators can configure the default action that happens immediately after an association in the **Connections** settings.
- ![After Associating.png](/cms_trial/assets/c4954bfc-05bf-422e-aa24-07ff26f0ba10.png)
- Syntax**:** `associateJiraIssueWithDefaultPostActions(String jiraKey, List<SObject> sObjects)`

  - Parameters**:**

    - `jiraKey`: The key of the Jira work item.
    - `sObject`: A type of Salesforce object for the records you want to associate with the Jira work item. To learn more about `sObject`, see the [Salesforse developers](https://developer.salesforce.com/docs/atlas.en-us.apexref.meta/apexref/apex_methods_system_sobject.htm) documentation.

These methods eliminate the need for complex custom code when interacting with Jira endpoints to update associations.

## Before you start

- Ensure that the Jira work item key provided is valid and accessible using the connected Jira instance ([set up a connection to Salesforce](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/), [bind a project to a connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/)).
- Configure the default post-actions triggered by `associateJiraIssueWithDefaultPostActions` in the **Connections** setup in the Jira-Salesforce integration. [Configure connection settings after Associating](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).

## Instructions

1. In Salesforce, in the upper right corner, click the gear icon (▢) and select **Setup**.
2. In the **Quick Find** box, type `Apex Triggers`.
3. Click **Developer Console** on the *Apex Triggers*screen.

   ![Apex Triggers.png](/cms_trial/assets/704ac4d8-72e2-4f6d-8a9b-9939f5880b2d.png)
4. On the *Developer Console*screen, select **File** > **New** > **Appex Trigger**.

   ![New Apex Trigger.png](/cms_trial/assets/ab4ad2a9-ad79-44be-925a-5e4d58001f60.png)
5. Fill in Apex Trigger details:  
   For example:  
   **Name:** `AssociateOnCreate`  
   **sObject:** Case - Select the Salesforce Object type you want to associate from the list.

   ![Submit New Apex Trigger.png](/cms_trial/assets/1535343b-0d7c-4bba-b83e-c473dc0a19cc.png)
6. Click **Submit**.
7. Paste the Apex Trigger into the code console.

   ![Example code.png](/cms_trial/assets/d49fff94-2c44-4e06-82ab-5f1ff4d19bd1.png)

### Example Apex Trigger

Here is an example of using `associateJiraIssueWithDefaultPostActions` in an Apex trigger to associate a Jira work item with newly created Salesforce cases:

```text
trigger AssociateOnCreate on Case (after insert) {
    JCFS.API.associateJiraIssueWithDefaultPostActions('S8U-8', Trigger.new);
}
```