# Migrate Connector for Salesforce & Jira Data Center to Cloud

Migration involves moving your Connector for Salesforce & Jira from Data Center to Cloud through a three-step process.

## Quick reference on moving from Jira Data Center to Cloud

| **Current product version** | **Platform** | **Target product version** | **Platform** | **Available app migration path** | **License migration** | **Notes** |
| --- | --- | --- | --- | --- | --- | --- |
| [Connector for Salesforce & Jira](https://appfire.atlassian.net/wiki/spaces/477986818/pages/2560819229) | Data Center | [Connector for Salesforce & Jira](/cms_trial/space/CSFJIRA/1873739795/Get+started+with+Connector+for+Salesforce+%26+Jira/) | Cloud | [Migrating from Connector for Salesforce & Jira Data Center to Cloud](/cms_trial/space/CSFJIRA/2161049701/Migrate+Connector+for+Salesforce+%26+Jira+Data+Center+to+Cloud/) | Needed | - Understand the [feature differences](/cms_trial/space/CSFJIRA/2161082491/Connector+for+Salesforce+%26+Jira+feature+differences+for+Jira+DC+and+Cloud/) between the connector for Jira Data Center and Jira Cloud. - Allocate time for a test migration to understand the steps required to migrate data and complete reconfiguration. - This guide assumes you have successfully migrated your Jira Data Center data into Jira Cloud, per [Atlassian's instructions](https://www.atlassian.com/migration/plan/cloud-guide#atlassian-team). |

## Before you start

Make sure you have:

- Understood the [feature differences](/cms_trial/space/CSFJIRA/2161082491/Connector+for+Salesforce+%26+Jira+feature+differences+for+Jira+DC+and+Cloud/) between the connector for Jira Data Center and Jira Cloud.
- Allocated time for a test migration to understand the steps required to migrate data and to complete reconfiguration.
- Ensure a complete review of the following guides:

  - [Atlassian Migration Preparation](https://support.atlassian.com/migration/docs/prepare-to-migrate-your-atlassian-server-products/?__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622088276279.1622094034771.312&__hssc=72543820.10.1622094034771&__hsfp=950301092)
  - [Atlassian Cloud migration guide](https://www.atlassian.com/migration/cloud/guide/introduction/overview?__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622088276279.1622094034771.312&__hssc=72543820.10.1622094034771&__hsfp=950301092)
  - [Jira Cloud Migration Assistant (JCMA) guide](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/?__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622088276279.1622094034771.312&__hssc=72543820.10.1622094034771&__hsfp=950301092)

## Migration guide

At the end of this guide, you will have:

- Completed a review of prerequisites.
- Created a callback URL to JCMA from **Migration Hub** in Jira Cloud.
- Run the JCMA migration.
- Imported data and settings to the Jira Cloud site.

### [Step 1 - Plan out your migration](/cms_trial/space/CSFJIRA/2160984266/Step+1+-+Plan+out+your+migration/)

General overview:

- You have completed all necessary prerequisites.
- You have set aside a maintenance window for your Jira Data Center instance as best practice.
- You have understood and set aside a specific timeline to conclude all your steps based on the steps you have run.

### [Step 2 - Prepare your Jira Server migration data](/cms_trial/space/CSFJIRA/2160754916/Step+2+-+Prepare+your+Jira+Data+Center+migration+data/)

General overview:

- Run the [Jira Cloud Migration Assistant](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/?__hstc=72543820.ab19c70c621fe76686456a1bcc7fc053.1619057720792.1623674729669.1623682280922.142&__hssc=72543820.17.1623682280922&__hsfp=2235196465) (JCMA) to choose the projects and other data that you want to migrate.

### [Step 3 - Import data and settings into the Jira Cloud site](/cms_trial/space/CSFJIRA/2161049766/Step+3+-+Import+data+and+settings+into+the+Jira+Cloud+site/)

General overview:

- Navigate to the Migration Hub and start the data migration to Cloud.
- Reauthorize the Salesforce connection from Jira Cloud.
- Install and configure the Connector for Salesforce and Jira (Cloud) package on Salesforce.
- Verify the migration by testing a connection to Salesforce and creating a test work item on a migrated project.

---

### Next Steps

- [Step 1 - Plan out your migration](/cms_trial/space/CSFJIRA/2160984266/Step+1+-+Plan+out+your+migration/)