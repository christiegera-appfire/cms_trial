# Step 3 - Import data and settings into the Jira Cloud site

This step overrides any existing data on the [Connector for Salesforce & Jira (Cloud)](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?hosting=cloud&tab=overview&__hstc=72543820.f1ffb555b95f54caea1a9a28de23a28f.1606879596997.1622094034771.1622098833267.313&__hssc=72543820.44.1622098833267&__hsfp=950301092). Ensure you have made the necessary backups if you have any important data on the Cloud site.

## Before you start

- You have completed [Step 2 - Prepare your Jira Server/Data Center migration data](/cms_trial/space/CSFJIRA/2160754916/Step+2+-+Prepare+your+Jira+Data+Center+migration+data/).
- You have administrator access to your Jira Cloud site.
- You have administrator access to Salesforce.
- You have an active evaluation or active paid license for Connector for Salesforce & Jira (Cloud).

## Import data and settings guide

As soon as JCMA completes the migration process in Jira Data Center, the Jira project data is ready to be imported into Cloud. For large instances, the migration can take some time to complete, and the project migration status may not be updated immediately. You need to wait for the *Migration Hub* to display new *Project Bindings.*

1. Log in to your Jira Cloud site.
2. Select **Apps** from the left sidebar in Jira.
3. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.
4. Click **Migration Hub** in the left menu.
5. Wait for the migration to complete and refresh the page.
6. When the *Project Bindings Status* changes to ready, click **Start Connector Migration** to migrate application-related data to Cloud.

   ![image-20260519-115923.png](/cms_trial/assets/41d5d98c-0808-4b9f-bebe-2c4d65c092cb.png)

If you only see a greyed-out **Start Connector Migration** button and there are no projects listed, refer to [Step 2](/cms_trial/space/CSFJIRA/2160754916/Step+2+-+Prepare+your+Jira+Data+Center+migration+data/) to upload your project data from Data Center to Cloud first.

1. Select the project bindings you want to migrate. You can select multiple projects if available.
2. Click **Next** to continue.

   ![Select project binding](/cms_trial/assets/f45f8104-a9d7-4d8e-9c37-97e9e24c9eeb.png)
3. Review the Connector-related projects ready to be migrated and click **Migrate**.

   ![image (13).png](/cms_trial/assets/42580ab0-ee46-4b57-a146-d8004bfa7c3b.png)

   The project status changes from Ready to In Progress in the **New** tab.

   ![image-20260519-120413.png](/cms_trial/assets/0dbea880-0733-483b-aba6-438a43762b24.png)

Status definition:

- Not Ready  The app is still waiting for the data to be available in JCMA data warehouse.
- Ready  The app data for this project is ready to be migrated to Cloud.
- In Progress  The Connector for Salesforce & Jira migration is still in progress.
- Failed  Data is not available due to errors or complications.

When the Connector-related project is completely migrated to the Cloud, it moves to the **Completed**tab. The Connector for Salesforce & Jira data, including bindings, connections, and associations, has been successfully migrated to Cloud.

![image-20260519-120622.png](/cms_trial/assets/47a26f75-5922-4907-ba5f-a66d6eb21da6.png)

## Next steps

After the migration, the Connector for Salesforce & Jira data, including bindings, connections, and associations, has been successfully migrated to your Jira Cloud site. To complete the setup, you need to reauthorize the Salesforce connection and configure the Connector on the Salesforce side.

## Reauthorize the Salesforce connection in Jira Cloud

1. Set up and reauthorize the connection to Salesforce.   
   For instructions, see [Set up a connection to Salesforce (Jira Cloud)](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/).

   ![image-20260519-120839.png](/cms_trial/assets/809d6232-bfa7-41c8-ad2c-7b494064aeb4.png)

### Install and configure the Connector for Salesforce and Jira (Cloud) package in Salesforce

Complete the following steps in Salesforce to enable a secure connection from Salesforce to your Jira Cloud site:

1. Install the [Connector for Salesforce and Jira (Cloud) package](https://appexchange.salesforce.com/listingDetail?listingId=a0N3000000E7xufEAB) from the Salesforce AgentExchange.   
   For instructions, see [Install the Salesforce package in Salesforce](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/).
2. Add two remote sites for Jira Cloud in Salesforce to enable a secure connection.  
   For instructions, see [Add new remote site](/cms_trial/space/CSFJIRA/1873412619/Add+new+remote+site/).
3. Configure the Jira Cloud for Salesforce package in Salesforce to connect to a Jira Cloud site.  
   For instructions, see [Set up a connection to Jira](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/)
4. Add Jira Issues (NextGen) componentto view Jira details directly in Salesforce.   
   For instructions, see [Use Jira Issues with Lightning Experience](/cms_trial/space/CSFJIRA/1873543771/Use+Jira+Issues+(NextGen)+with+Lightning+Experience/).

### Verify the migration

Once setup is complete, test the following scenarios to confirm the migration was successful:

- Create a new project in Cloud and test the project's connectivity to Salesforce for any issues.
- Create a new test work item on any known project that was recently migrated and test the end-to-end experience by connecting to Salesforce.