# Connector for Salesforce & Jira feature differences for Jira DC and Cloud

Last updated onDecember 22, 2025.

|  |  |  |
| --- | --- | --- |
| **Migration Focus Area** | **Feature** | **Platform** |
| **Server/Data Center** | **Cloud** |
| Versioning/License | Version Support | Min Upgradable  [Jira version](https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html) - click the link to determine if your Jira version is still supported | Migrate to NextGen Cloud using steps at [Migration Path](/cms_trial/space/CSFJIRA/2161082534/Migration+path+Connector+for+Salesforce+%26+Jira+Server+or+Data+Center+to+Cloud/). |
| License | Available through Atlassian Marketplace. | Available through Atlassian Marketplace only. Monthly subscriptions are the default option. However, discounted annual subscriptions are available upon request to our Atlassian Sales team. |
| Jira Differences | Jira data | All related features from Server/Data Center migrating to the cloud will depend on the JCMA and Atlassian Jira migration support. | Please review   - [What gets migrated with the Jira Cloud Migration Assistant](https://support.atlassian.com/migration/docs/what-gets-migrated-with-the-jira-cloud-migration-assistant/), especially data in custom fields. |
| Jira integration user | In a migration scenario, an integration user must first be set up on the Jira Server or Data Center. This is a prerequisite for the migration process. Refer to [Set up an integration user - Connector for Salesforce & Jira](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=Set%20up%20an%20integration%20user%20%28Jira%20DC%29&linkCreation=true&fromPageId=2161082491) for steps on how to set up this user. | There is no need to set up an integration user on Cloud. |

## Feature parity

| **Features** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| **Connectors configuration in Jira** |
| - Binding projects to a connection | ✅ | ✅ |  |
| - Setting connection to Salesforce | ✅ | ✅ | In Jira DC you need to set up an integration user before setting up a connection. |
| **Connectors configuration in Salesforce** | ✅ | ✅ |  |
| - Setting connection to Jira | ✅ | ✅ | Based on your Jira environment, you need to add different Remote Sites:  **Jira Data Center:** Add a Remote Site for your Jira instance URL  **Jira Cloud:** Add Remote Sites for:   - <https://sfjc.integration.appfire.app> - <https://eu-sfjc.integration.appfire> |
| **Synchronization** |
| Entity mapping | ✅ | ✅ |  |
| Field mapping | ✅ | ✅ |  |
| Value mapping | ✅ | ✅ |  |
| Default value mapping | ❌ | ✅ | Default value mapping is available only on Jira Cloud. |
| Sync direction: Manual & auto bi-directional | ✅ | ✅ |  |
| Support for custom Salesforce objects | ✅ | ✅ |  |
| Create Jira work items | ✅ | ✅ | Creating Jira work items from Salesforce for the Jira Service Management (JSM) projects is supported only for Jira Cloud. |
| Create Salesforce records | ✅ | ✅ |  |
| Get updates from Salesforce | ✅ | ✅ |  |
| Get updates from Jira | ✅ | ✅ |  |
| Send updates to Salesforce | ✅ | ✅ |  |
| Send updates to Jira | ✅ | ✅ |  |
| View Jira comments in Salesforce | ✅ | ✅ |  |
| View Salesforce comments in Jira | ✅ | ✅ |  |
| Push and pull attachments | ✅ | ✅ |  |
| Chatter Support | ✅ | ✅ |  |
| JQL functions | ✅ | ✅ |  |
| Reporting | ✅ | ✅ |  |
| Search page | ✅ | ✅ |  |
| **Post functions** |
| Push to Salesforce post function | ✅ | ✅ |  |
| Create Salesforce object post function | ✅ | ✅ |  |
| **Automate your integration** |
| Automatic Jira work item creation and push updates | ✅ | ✅ | Triggers for Cloud and Jira DC differ [Automatic Jira Issue Creation and Push Updates in the same trigger](https://appfire.atlassian.net/wiki/x/NIWrbw) |
| Configure automatic pull from Salesforce | ✅ | ✅ | Triggers for Cloud and Jira DC differ [Configure Automatic Pull from Salesforce](/cms_trial/space/CSFJIRA/1873446010/Configure+Automatic+Pull+from+Salesforce/) |
| Associate Jira work item with Salesforce records and trigger post actions | ✅ | ✅ | Triggers for Cloud and Jira DC differ [Associate Jira work item with Salesforce records and trigger post actions automatically](/cms_trial/space/CSFJIRA/1873413550/Associate+Jira+work+item+with+Salesforce+records+and+trigger+post+actions+automatically/) |
| Trigger code when an association is unlinked | ✅ | ✅ | Triggers for Cloud and Jira DC differ [Trigger code when an association is unlinked](/cms_trial/space/CSFJIRA/1874002013/Trigger+code+when+an+association+is+unlinked/) |
| **Associating** |
| Associate Jira issues | ✅ | ✅ |  |
| Associate Salesforce records | ✅ | ✅ |  |
| Bulk association | ❌ | ✅ | Bulk associate available in Cloud. |
| Run the association report | ✅ | ✅ |  |
| REST API | ✅ | ✅ | Cloud version and DC version APIs are different. Check the documentation for details:   - [API reference](/cms_trial/space/CSFJIRA/1685193166/API+reference/) - [API reference for Jira DC](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=API%20reference%20for%20Jira%20DC&linkCreation=true&fromPageId=2161082491) |
| **Notifications** |
| Email notifications to Salesforce users | ✅ | ✅ |  |
| Email notifications to Jira users | ✅ | ✅ |  |
| **Salesforce features support** |
| Visualforce | ✅ | ✅ |  |
| Lightning UI | ✅ | ✅ |  |
| NextGen | ✅ | ✅ |  |