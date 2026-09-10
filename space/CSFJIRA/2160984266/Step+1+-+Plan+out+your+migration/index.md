# Step 1 - Plan out your migration

In this step, you will plan for a complete migration from the Connector for Salesforce & Jira (Data Center) to the Connector for Salesforce & Jira (Cloud) version.

## Before you start

- Review [Migrate from Jira Data Center to Jira Cloud Connector](/cms_trial/space/CSFJIRA/2161049701/Migrate+Connector+for+Salesforce+%26+Jira+Data+Center+to+Cloud/).
- Confirm the following installation-related tasks are complete:

  - The [Jira Cloud Migration Assistant](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant?__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622088276279.1622094034771.312&__hssc=72543820.10.1622094034771&__hsfp=950301092) app is installed on your Jira Data Center.
  - The [Connector for Salesforce & Jira (Cloud)](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?hosting=cloud&tab=overview&__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622088276279.1622094034771.312&__hssc=72543820.10.1622094034771&__hsfp=950301092) app is installed on your Jira Cloud site.
  - The latest version of the [Connector for Salesforce & Jira (Data Center)](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?hosting=server&tab=overview&__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622088276279.1622094034771.312&__hssc=72543820.10.1622094034771&__hsfp=950301092) app is installed on your Jira Data Center instance.

## Maintenance window

- Depending on the data size and the complexity of the existing configuration, these steps can take up to a few hours to complete. We advise you to schedule a maintenance window to perform the migration.
- [Jira Cloud Migration Assistant (JCMA](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/)[)](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/) handles the migration window as follows:

  - On Jira Data Center, JCMA handles the export. There is no instance downtime.  
    Best practices: Begin with a small number of projects to test the process, then expand the scope once you are confident in the results.
  - On Jira Cloud, JCMA handles data migration as a background task:

    - JCMA initiates the migration from the Jira Data Center side.
    - The migration automatically refers to the latest version of existing data for any particular project.
- Once the data migration to the Cloud is complete, you can initiate the next Cloud-related steps for Connector for Salesforce & Jira.

## Next steps

- We recommend reviewing all migration steps before executing them to estimate the time required.
- Your existing app data will not be overwritten. However, we suggest removing your test data before migrating your production data.

[Unmapped macro: ui-button — no content to fall back on]