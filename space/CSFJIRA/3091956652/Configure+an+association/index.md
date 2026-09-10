# Configure an association

This page explains how to configure existing associations in Jira and Salesforce.

The association configuration can be overridden by the Connection configuration. If a configuration does not show the expected behavior, verify that the respective setting on the Connection configuration is enabled.

## Guide

### Jira

1. In a Jira work item, look under the *Connector for Salesforce* section on the right side of the screen.
2. Find the association you want to configure and click **Configure**.

   ![record association](/cms_trial/assets/ceeb0d08-9075-48a2-824a-992310600d61.png)

   The *Configure association* window opens.

   ![Configure association window](/cms_trial/assets/62a68579-a807-4aca-9c5e-ecf2b0deee15.png)

1. Configure your association using the following options:

   - **View only** - Manual and automatic synchronization will be disabled.
   - **Automatic push** - Changes to this work item will be pushed automatically to the associated Salesforce record.
   - **Automatic pull** - Changes to the associated Salesforce record will be pulled automatically to this work item.
2. Set the options and click **Save**.

### Salesforce

1. Open a Salesforce record that has already been [associated with a Jira work item](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/).
2. In the Salesforce record, in the **Jira Issues** panel, click the dropdown for the Association you want to configure and choose **Configure**.

   ![screenshot of  Jira Issues panel](/cms_trial/assets/f9120cbd-a2c8-4f1d-a988-1502e6df08b3.png)

   The*Configure Association* window opens.

   ![screenshot of Configure Association](/cms_trial/assets/ae85d136-b284-40c1-90a2-a86a126308b0.png)
3. Set the desired options for the chosen Association and click **Apply**.

### Salesforce LWC

1. Open a Salesforce record that has already been [associated with a Jira Issue](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/).
2. In the Salesforce record, in the **Jira Issues** panel **tiles/table view**, click the dropdown for the Association you want to configure and select **Configure**.

   ![screenshot of  Jira Issues LWC panel](/cms_trial/assets/7f1de542-896d-44c3-b5de-3e8c266c8182.png)
3. The **Configure Association** side panel opens.

   ![screenshot of  Configure Jira Issues](/cms_trial/assets/74c489ca-afee-446a-9299-815a938a7ce7.png)
4. Set the desired options for the chosen Association and click **Save**.