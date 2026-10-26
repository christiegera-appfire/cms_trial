# Track SLA deadlines across Salesforce and Jira

When customer support teams work in Salesforce and engineering teams work in Jira, keeping track of SLA deadlines across both platforms can be challenging.

By integrating Time to SLA with Salesforce through Connector for Salesforce & Jira, you can display SLA information directly on Salesforce records. Support teams can monitor response and resolution deadlines without leaving Salesforce, while engineering teams manage the associated work items in Jira.

In this example, we'll configure two priority-based SLAs in Time to SLA, escalate a Salesforce case to Jira, and view the SLA details in both platforms.

## Before you start

Make sure you have:

- **Time to SLA for Jira Cloud** installed.
- [**Connector for Salesforce & Jira**](https://marketplace.atlassian.com/apps/1214214/connector-for-salesforce-jira?tab=overview&hosting=cloud&utm_source=google&utm_medium=cpc&utm_campaign=grw_dtmp&gad_source=1&gad_campaignid=22181726356&gbraid=0AAAAAD2HsFmcu1L1WibtpyKB_d98qka6B&gclid=CjwKCAjw_pzWBhAkEiwAwDCi1dz_iJF4FiSd-sBzQXf4tbTR7Pg5aDBUr1Iv52UIDlPCLr4o9dMMbxoC7d4QAvD_BwE) installed, with connections configured between Jira and Salesforce.
- Completed the steps in [Connector for Salesforce & Jira](/cms_trial/space/TTSC/3742760964/Connector+for+Salesforce+%26+Jira/) to connect the apps, create an integration, and add the **Time to SLA for Jira** component to your Salesforce record page.
- [Entity and field mappings](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/3664152459) configured between the Salesforce **Case** object and Jira **Bug** work item type, using the Bug escalation template.

You'll also need the appropriate permissions to create Salesforce cases and Jira work items.

## Step 1: Configure SLAs in Time to SLA

Let's consider a scenario where a customer reports a critical issue in Salesforce that needs to be escalated to an engineering team in Jira.

We'll use two SLAs to track how quickly the team responds to and resolves the issue:

- **Time to first response:** Measures the time from work item creation until the first public response.
- **Time to resolution:** Measures the time from work item creation until the work item is resolved.

Both SLAs have different targets depending on the priority of the Jira work item.

### Time to first response

| **Priority** | **SLA target** |
| --- | --- |
| P1 – Critical | 30 minutes |
| P2 – High | 2 hours |
| P3 – Low | 6 hours |

![image-20260611-080619.png](/cms_trial/assets/505a347f-e86a-424c-bc9c-d3eb4927ed97.png)

### Time to Resolution

| **Priority** | **SLA target** |
| --- | --- |
| P1 – Critical | 6 hours |
| P2 – High | 16 hours |
| P3 – Low | 72 hours |

![image-20260611-080646.png](/cms_trial/assets/025c17da-f851-4b35-91c1-d011d9d3fe0a.png)

Configure both SLAs with the following conditions:

| **Condition** | **Configuration** |
| --- | --- |
| Start | When the Jira work item is created |
| Pause | When the work item status is **Waiting for customer** |
| Stop (First Response) | When a public comment is added |
| Stop (Resolution) | When the work item resolution is set |

For detailed instructions on creating and configuring SLAs, see [Define SLAs](/cms_trial/space/TTSC/35651691/Define+SLAs/).

## Step 2: Create and escalate a case in Salesforce

Now that your SLAs are configured, create a Salesforce case and escalate it to Jira.

1. In Salesforce, create a new **Case** with the following details:

   - **Subject:** Mobile app crashes when uploading profile photo
   - **Priority:** High
   - **Description:** The iOS app closes unexpectedly when users select a photo larger than 5 MB from their gallery. The issue started after the latest app update.
2. Save the case.
3. On the case record page, find the **Jira Issue** component and click **Associate/Create**.

   ![image-20261002-065523.png](/cms_trial/assets/fed3d362-248b-4463-a8b1-89f5b6216ffe.png)
4. Select **Create Jira Issue**.
5. Select your mapped Jira space and choose **Bug** as the work item type.
6. Click **Create**.

   ![image-20261002-071743.png](/cms_trial/assets/2a4360b0-7655-4d12-a9a9-5c4c66af3b79.png)

If the **Bug** work item type isn't available, check that the Salesforce Case object is mapped to the Jira Bug work item type in Connector for Salesforce & Jira. For instructions, see [Configure entity and field mappings from templates](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/3664152459).

## Step 3: View SLA deadlines in Salesforce

After creating the Jira work item, refresh the Salesforce record page to display the synchronized information.

The page now shows:

- **Jira Issue component:** Displays the newly created Jira Bug associated with the Salesforce case.
- **Time to SLA for Jira component:** Displays the **Time to First Response** and **Time to Resolution** SLAs for the associated work item.

Because the case was created with **High** priority, the SLAs use the corresponding targets, provided the priority is mapped correctly between Salesforce and Jira:

| **SLA** | **Target** |
| --- | --- |
| Time to first response | 2 hours |
| Time to resolution | 16 hours |

Both SLAs start tracking time from the Jira work item's creation, based on the configured start, pause, and stop conditions.

Support teams can now monitor these SLA deadlines directly from the Salesforce case without opening Jira.

![image-20261002-072416.png](/cms_trial/assets/5e9cb7a9-1053-4712-bbb0-b412bb559994.png)

## Step 4: View SLAs in Jira

You can also open the newly created Bug work item in Jira to view its SLA details in Time to SLA.

The engineering team can manage the work item in Jira, while the support team monitors its SLA deadlines in Salesforce.

This gives both teams visibility into the same SLA targets while working in their respective platforms.