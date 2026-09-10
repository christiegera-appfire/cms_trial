# Step 2 - Prepare your Jira Data Center migration data

In this step, you will prepare your Jira Data Center migration data from the Connector for Salesforce & Jira (Data Center) to the Connector for Salesforce & Jira (Cloud).

## Before you start

- You have reviewed [Step 1 - Plan out your migration](/cms_trial/space/CSFJIRA/2160984266/Step+1+-+Plan+out+your+migration/).
- You have administrator access to the following platforms:

  - Your Jira Data Center instance.
  - Your Jira Cloud site.
  - Your Salesforce organization.

## Prepare Jira Data Center data for migration

1. Make sure an integration user is set up for the Connector for Salesforce & Jira. If one does not exist, follow the documentation on [how to create an integration user account](https://appfire.atlassian.net/wiki/spaces/477986818/pages/2560820245).
2. Log in to your Jira Cloud instance.Log in to your Jira Cloud site.

   1. Select **Apps** from the left sidebar in Jira.
   2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.
   3. Click **Migration Hub** in the left menu.
   4. On the *Migration Hub* page, click **Get Started** to register a webhook that enables the cloud Connector for Salesforce & Jira app to receive data from the Connector for Salesforce & Jira Data Center.

      ![Get started migration](/cms_trial/assets/329a8ad2-c4dd-4cf9-841d-43bc42a5dd4a.png)
   5. A confirmation message appears.

      ![csfjira-success-register.png](/cms_trial/assets/7419e908-a9fb-4719-9c1d-05e18c9f8ff8.png)
3. To prepare your Connector for Salesforce & Jira app data, you must run the Jira Cloud Migration Assistant (JCMA) to choose the projects, users, and groups you want to migrate. Open the JCMA by navigating to **Jira Administration > System > Migrate to cloud**.
4. In the app assessment, select Connector for Salesforce & Jira as **Needed in cloud**.

   ![assess apps](/cms_trial/assets/fae4190c-5b3e-4b9e-9b52-a26644ea7d58.png)
5. Accept the agreement for the app migration to allow Connector for Salesforce & Jira to access your data. If you skip this step, the migration will fail.

   ![Agree to app migration](/cms_trial/assets/36cee55a-1791-4ec2-b8f1-ea5a04b26970.png)
6. Follow the instructions in [Atlassian's JCMA Migration Guide](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/) to run your migration.
7. Monitor the migration status in the *Migration dashboard*.
8. Wait until the status shows **Migration complete** before proceeding.

   ![Migrations dashboards](/cms_trial/assets/d33e2dbf-04dd-48e1-ac3f-6be1c1bc7e7b.png)

## Next steps

- Switch to Jira Cloud to import the migrated data to the Connector for Salesforce & Jira Cloud.

[Unmapped macro: ui-button — no content to fall back on]