# Salesforce: "Insufficient Privileges" Error on Connector Visualforce Page

## Summary

When viewing the connector's Visualforce page in Salesforce, you see this error message:

![contentId-3091859120](/cms_trial/assets/4ee93cf9-95fc-4b92-aee0-a9cb0775daac.png)

## Environment

- Jira Cloud
- Jira Data Center

## Diagnostics Steps

- N/A

## Cause

There are two reasons as to why this issue occurs:

- When installing the Connector for Salesforce & Jira package, the **Admin Only** option was selected.
- The **Apex Classes** for users to view and interact with Visualforce pages were not enabled.

## Workaround

- N/A

## Resolution

### Reinstalling Connector for Salesforce & Jira

1. Go to **Setup** > search for **Installed Packages**.
2. Reinstall the Connector for Salesforce & Jira package.
3. Follow the installation steps mentioned in our [Installing the Salesforce Package in Salesforce](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754565/Installing+the+Salesforce+Package+in+Salesforce) guide.   
   **Note**: Choose the **Install for All Users** option.

### Enabling the Apex Class Access

1. Identify the users who are unable to view the **Create Jira Issues** and **Associate** buttons.
2. In Salesforce, go to **Setup > Users > Profiles >** click on the affected users' profile.
3. Search for and edit **Enabled Apex Class Access**.
4. Add the Apex Class according to the Jira environment below:

   1. For Jira Cloud, add all the JCFS classes to the **Enabled Apex Classes** column.

      ![contentId-3091859120](/cms_trial/assets/4643eead-2d52-4e8c-ab3f-262431097828.png)
   2. For Jira Server, add all the JSFS classes to the **Enabled Apex Classes** column.

      ![contentId-3091859120](/cms_trial/assets/33f27693-b7ef-4972-82e6-e8aa90ebdcce.png)