# Set up Time to SLA integration

This guide walks Jira admins through connecting Time to SLA to Connector for Salesforce & Jira, creating integrations that route specific Salesforce instances to a Time to SLA scope, and displaying Jira work item SLAs on Salesforce record pages.

An integration assigns a Time to SLA scope to one or more Salesforce instances connected through the connector. You connect Time to SLA once per tenant, and then create named integrations, each mapped to the Salesforce instance URLs it applies to. After you add the SLA component to a Salesforce record page, users can see the SLAs for an associated Jira work item directly on the record.

## Before you start

Make sure you have:

- Jira administrator access on the Jira instance with Connector for Salesforce & Jira.
- Salesforce administrator access to edit record pages
- [Set up a connection to Salesforce in Jira.](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/)
- [Set up a connection to Jira in Salesforce](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/).
- [Mapped entities](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/) that should sync the SLA data (for example, Task Jira work item type with the Case Salesforce object type). Only mapped entities allow for associations and data synchronization.
- [Installed the Time to SLA app.](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/35684371)
- [Defined SLAs in Time to SLA.](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/35651691)

## Connect your Time to SLA token

Open Time to SLA and Connector in two browser tabs so you can copy and paste easily.

### **Part 1: Copy the token from Time to SLA**

1. In Time to SLA, go to **Administration** > **SLAs in Salesforce**.
2. Click **+ Token**.

   ![Time to SLA add Token](/cms_trial/assets/49eb154b-f6c9-484b-8b8a-5c0fe9ece153.png)
3. Click **Copy and close**. Store the API token to paste it in the next steps.

   ![new API token](/cms_trial/assets/00e3d337-b246-4d44-8591-af9f201c4463.png)

### Part 2: Paste it into Connector

1. In Jira, select **Apps** from the left sidebar.
2. Next to *Connector for Salesforce and Jira,* click **Menu** (▢) > **App settings**.
3. Under *Connector for Salesforce and Jira*, click **Integrations**.
4. Click **Add Token**.

   ![Add Token](/cms_trial/assets/b721b3f8-a571-49a3-9103-eb5437eb8d05.png)
5. Select your **Time to SLA base URL** region. It must match the region of your Time to SLA instance.
6. Paste your **Time to SLA API token**.   
   This token is shared across the tenant. Every integration you create afterward uses it to talk to Time to SLA.

   ![Connect to Time to SLA](/cms_trial/assets/b1b317a2-100d-4943-a06d-d4e9db6471e8.png)
7. Click **Save**.  
   When the status changes to ACTIVE, you can create integrations.

   ![Time to SLA integrations](/cms_trial/assets/ef3e8d5c-1902-4a8e-b59d-eef8a6c476ae.png)

## Create an integration

1. Click **Create an integration**.

   ![Create an integration](/cms_trial/assets/167af959-8f30-4e6d-bf8f-1dc824315827.png)
2. In the *New integration* window, enter the following*:*

   - **Integration name**: Enter a unique name.
   - **Connections**: Select the connection between Jira and Salesforce for this integration.

     You can only select URLs that are authorized for your tenant and aren’t already claimed by another integration.
   - **Time to SLA scope**: Select the scope this integration uses.

     ![New integration window](/cms_trial/assets/1d4ab2e1-8fa1-4faf-bbf8-60010d73b8c3.png)
3. Click **Save**.   
   The integration appears in your *Integrations* list.

   ![image-20261001-192333.png](/cms_trial/assets/b129ac0a-e3c8-4bf6-a4dd-196a43fb6c8a.png)

## Add the SLA component to a Salesforce record page

Finish setup in Salesforce so users can see SLAs on their records. Repeat these steps for each object type layout where you want SLAs to appear.

1. In Salesforce, load a record page,for example, a Case.
2. Click **Settings** > **Edit Page**.

   ![Edit page](/cms_trial/assets/b23cda5d-7d48-4943-9fb3-5a447abe39a3.png)

   The Lightning App Builder loads.
3. In the sidebar, scroll to the bottom to find the **Time to SLA for Jira** component.
4. Drag the component onto the selected location for your page layout.

   ![Lightning App Builder](/cms_trial/assets/990a1714-e3e8-4b21-9ffd-f252dddd5eb9.png)
5. Check whether you have already added the **Jira Issue** component displaying Jira work items in the page layout. If not, add it next to the *Time to SLA for Jira* component.

   ![Time to SLA for Jira component](/cms_trial/assets/5e9f13b7-a6b7-4d46-8b86-06f57ee3c533.png)
6. Click **Activation** and **Save**.
7. Go back to the record page.
8. In the Jira Issue component, click **Associate/Create**.

   ![image-20260921-122042.png](/cms_trial/assets/c0f52103-5568-4a42-a82f-d432f7e58662.png)
9. If you have more than one connection, select the correct one under **Select a Connection.**
10. Under **Associate Jira Issue**, select a Jira Issue that already has SLAs set in Jira.
11. Enable automatic pull to allow SLAs from Jira to synchronize with Salesforce, and click **Associate.**

    ![image-20261001-194312.png](/cms_trial/assets/04918e9a-c6cf-4127-9825-9a7acad1e3f8.png)
12. Refresh the page to display the *Time to SLA for Jira* component with SLA details.

    ![image-20261009-083105.png](/cms_trial/assets/1f15df7e-35eb-4978-a03f-be81d42750d8.png)

## Related pages

- [Set up a connection to Salesforce in Jira.](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/)
- [Set up a connection to Jira in Salesforce](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/).
- [Map entities](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/)
- [Install the Time to SLA app.](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/35684371)
- [Define SLAs in Time to SLA.](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/35651691)