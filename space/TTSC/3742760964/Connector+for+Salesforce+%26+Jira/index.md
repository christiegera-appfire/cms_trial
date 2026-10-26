# Connector for Salesforce & Jira

Display SLA information from Time to SLA directly on Salesforce record pages using [Connector for Salesforce & Jira](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=overview&hosting=cloud&utm_source=google&utm_medium=cpc&utm_campaign=grw_dtmp&gad_source=1&gad_campaignid=22181726356&gbraid=0AAAAAD2HsFmcu1L1WibtpyKB_d98qka6B&gclid=CjwKCAjw_pzWBhAkEiwAwDCi1dz_iJF4FiSd-sBzQXf4tbTR7Pg5aDBUr1Iv52UIDlPCLr4o9dMMbxoC7d4QAvD_BwE). This integration lets Salesforce users view SLA details for associated Jira work items without switching between platforms.

To get started, connect Time to SLA to Connector for Salesforce & Jira, create an integration for your Salesforce connection, and add the Time to SLA component to your Salesforce record pages.

### Before you start

To display SLA information in Salesforce, make sure you have:

- [Installed the Time to SLA app](/cms_trial/space/TTSC/35684371/Installation/).
- [Defined SLAs in Time to SLA](/cms_trial/space/TTSC/35651691/Define+SLAs/).
- Jira administrator access on the Jira instance with Connector for Salesforce & Jira.
- Salesforce administrator access to edit record pages.
- [Set up a connection to Salesforce in Jira](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/1873379599).
- [Set up a connection to Jira in Salesforce](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/1873346949).
- [Mapped entities](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/3664152459) that should sync the SLA data (for example, Task Jira work item type with the Case Salesforce object type). Only mapped entities allow for associations and data synchronization.

## Connect Time to SLA to Salesforce

First, generate an API token in Time to SLA and add it to Connector for Salesforce & Jira. You only need to connect the apps once per Jira tenant.

### Step 1: Generate an API token in Time to SLA

1. In Time to SLA, go to **Administration** > **SLAs in Salesforce**.
2. Click **+ Token**.

   ![Time to SLA add Token](/cms_trial/assets/880a67d6-b056-44d2-8af2-78faaf3c3e3e.png)
3. Click **Copy and close** to copy the generated API token.

   ![new API token](/cms_trial/assets/4a4888d8-f58e-4ee8-8f33-41b622b5c97d.png)

Keep the token available for the next step.

### Step 2: Add the token to Connector for Salesforce & Jira

1. In Jira, select **Apps** from the left sidebar.
2. Next to **Connector for Salesforce and Jira**, click **Menu** > **App settings**.
3. Under **Connector for Salesforce and Jira**, select **Integrations**.
4. Click **Add Token**.

   ![Add token](/cms_trial/assets/e90aa529-52f6-40f2-9b2c-e47c0a604436.png)
5. Select the **Time to SLA base URL** region that matches your Time to SLA instance.
6. Paste the API token you generated in Time to SLA.

   ![Connect to Time to SLA](/cms_trial/assets/d1d68513-79bf-4e77-ae93-538a3c41c83a.png)
7. Click **Save**.

Once the connection status changes to ACTIVE , you can start creating integrations.

![Time to SLA integrations](/cms_trial/assets/0e55844c-64af-40e4-bb16-5369a9a3a1a4.png)

The API token is shared across your Jira tenant. All integrations you create use this token to communicate with Time to SLA.

## Create an integration

An integration connects one or more Salesforce instance URLs to a specific Time to SLA scope. This lets you configure which Time to SLA scope each Salesforce connection uses.

To create an integration:

1. In Connector for Salesforce & Jira, go to **Integrations**.
2. Click **Create an integration**.

   ![Create an integration](/cms_trial/assets/b703f6be-ef64-4c8b-ad53-7af224497edc.png)
3. In the **New integration** window, configure the following fields:

   - **Integration name:** Enter a unique name to identify the integration.
   - **Connections:** Select the Salesforce connection you want to use. You can only select authorized connections that haven't already been assigned to another integration.
   - **Time to SLA scope:** Select the Time to SLA scope you want to use for this integration.

     ![New integration window](/cms_trial/assets/329c7fad-d2ca-45e8-a120-2e0db67cbf02.png)
4. Click **Save**.

The new integration appears in your integrations list.

![image-20261001-192333.png](/cms_trial/assets/0ef5ceec-0c77-4d34-8c13-a43a6fcf5f0b.png)

You can create additional integrations to connect other Salesforce instances to their corresponding Time to SLA scopes.

## Add the Time to SLA component to Salesforce

Once you've created an integration, add the **Time to SLA for Jira** component to your Salesforce record pages so users can view SLA information.

You'll need to configure the component for each Salesforce object type where you want SLAs to appear.

1. In Salesforce, open a record page, such as a **Case** record.
2. Click **Settings** > **Edit Page** to open the Lightning App Builder.

   ![Edit page](/cms_trial/assets/3f05a45a-02c3-4259-a9e6-754ad3d6c025.png)
3. In the sidebar, scroll down to find the **Time to SLA for Jira** component.
4. Drag the component to your preferred location on the page.

   ![Lightning App Builder](/cms_trial/assets/55a533ab-b088-46c2-84d5-e9c3e1bd7311.png)
5. Make sure the **Jira Issue** component is also on the page. If it isn't, add it below the **Time to SLA for Jira** component.

   ![Time to SLA for Jira component](/cms_trial/assets/d4c0518d-98b1-43a7-8114-8de6af6e5b65.png)
6. Click **Activation** and **Save** to apply your changes.
7. Return to the Salesforce record page.

## View SLA details in Salesforce

After adding the component, associate a Jira work item with a Salesforce record to display its SLA information.

1. Open the Salesforce record page where you added the components.
2. In the **Jira Issue** component, click **Associate**.

   ![image-20260921-122042.png](/cms_trial/assets/6262094c-9e3b-4feb-b5f6-1272645632a4.png)
3. Select a Jira work item that has SLAs configured in Time to SLA.
4. Enable **Auto pull** to synchronize data from Jira with Salesforce.

   ![image-20261001-194312.png](/cms_trial/assets/95e01999-8bc8-43bb-9485-57a4e908dca8.png)
5. Click **Associate**.
6. Refresh the Salesforce record page.

The **Time to SLA for Jira** component now displays SLA information for the associated Jira work item.

![image-20261005-124634.png](/cms_trial/assets/c866885d-9dd9-4276-ac83-ddc216668485.png)

Salesforce users can view this information directly on the record page without opening Jira.