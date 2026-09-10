# Create a Salesforce record from Jira

This page explains how to create a Salesforce record (such as a Case) from a Jira work item. All the Salesforce records created will honor the [field and value mapping settings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

## Before you start

To create a Salesforce object:

- You must be a Jira user with [Edit work item](https://confluence.atlassian.com/jiracorecloud/permissions-overview-765593621.html) permission.
- Your administrator must have created the [binding for the Jira project to a Salesforce connection](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=Bind%20a%20project%20to%20a%20connection%20%28Jira%20DC%29&linkCreation=true&fromPageId=3091465546).

## Create a new Salesforce record from a Jira work item

1. In a Jira work item, look under the *Connector for Salesforce* section on the right side of the screen.
2. Click **Create Salesforce Object**.

   ![2025-10-16_13-12-27.png](/cms_trial/assets/e8d0ed03-ec71-4467-b7f1-162ef7141559.png)

   The **Create Salesforce record** window opens.

   ![Create Salesforce record](/cms_trial/assets/462219da-edba-4961-b4ad-38b04a01b0ea.png)
3. From the **Object type** dropdown, select the Salesforce Object type.  
   The available Salesforce Object types depend on how the [mapping configuration has been set up](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).
4. Configure your association with the following options:

   - **View only** - Manual and automatic synchronization are disabled.
   - **Automatic push** - Changes to this work item are pushed automatically to the associated Salesforce record.
   - **Automatic pull** - Changes to the associated Salesforce record are pulled automatically to this work item.
5. From the **After creating** dropdown, select what happens after the Salesforce record is created:

   - Do nothing
   - Pull from Salesforce
6. Click **Create**.  
   The new Salesforce record appears in the list in the *Connector for Salesforce* section.