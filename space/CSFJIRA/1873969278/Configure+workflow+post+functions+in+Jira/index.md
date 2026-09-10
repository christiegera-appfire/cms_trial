# Configure workflow post functions in Jira

This page will guide Jira administrators in adding post functions to transitions in their project workflow.

The Connector provides two workflow post functions:

- Create Salesforce Object
- Push to Salesforce

The following steps are meant for classic Jira projects and NOT for next-gen projects.

This is because of the nature of the workflows. Next-gen projects do not have workflow schemes. They have a new workflow editor instead.

For more information, please refer to the [Atlassian documentation](https://www.atlassian.com/software/jira/whats-new/next-gen#overview).

## Create Salesforce Object post function

This post function creates a Salesforce Object from the Jira issue. This is to automate the issue creation operation described in [Creating a Jira Issue from Salesforce](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/).

Important: If there is already an existing association (previously created), the post-function won't trigger.

![image-20251015-134546.png](/cms_trial/assets/16f187c5-d5ba-4b38-8e8b-4e57f08e1293.png)

 It requires these parameters:

- **Connection** - the name of the already authorized [Connection](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=Set%20up%20your%20integration%20in%20Jira%20Cloud&linkCreation=true&fromPageId=1873969278).
- **Salesforce Object** - the Salesforce Object the Jira issue should be created as.

To ensure the post function is operational, the following requirements should be fulfilled:

- A binding from the Jira project (configured with this workflow) to the authorized connection should always exist.
- A Salesforce Object should be configured as available for connection.
- A mapping from the issue type to the Salesforce Object should exist for that binding.

## Push to Salesforce post function

This post function pushes mapped issue fields of the Jira issue to associated Salesforce objects.

To ensure the post function is operational, the following requirements should be fulfilled:

- An authorized Salesforce connection should exist.
- A binding from the Jira project to an authorized Salesforce connection should exist.
- A mapping from the issue type to the Salesforce object should exist for that binding.

## Guide

For full instructions, we recommend visiting Atlassian's official [documentation](https://confluence.atlassian.com/adminjiracloud/advanced-workflow-configuration-776636620.html) on configuring workflows.

In this guide, we'll create a Salesforce object when a Jira issue is created using post functions.  
You may choose the transition of your choice and apply the same steps:

1. Go to **Settings** (⚙️) > **Work items**.
2. In the sidebar, under *Workflows*, click **Workflow schemes**.
3. Choose the project you'd like to customize, and click the associated **Workflow**.

   ![Screenshot of Workflow schemes](/cms_trial/assets/7937e782-a6d8-4e37-b10d-c9105a85eea3.png)
4. Click the **Edit** button to create a workflow draft or resume editing a draft.

You may be in Diagram view at first. Proceed to change to Text view if so.

1. Then, choose a **Transition.** In this case, we'll choose **Create**.
2. On the next screen, click **Add Rule** tab.
3. Click **Add Post Function**.

   ![Screenshot of  Post Function for Create](/cms_trial/assets/a985c684-662e-4377-aef4-8ba65dd55f44.png)
4. Choose **Create Salesforce Object** or **Push to Salesforce,** then click **Add**.

   ![Screenshot of Add Post Function To Transition](/cms_trial/assets/667474a8-ed96-4ae7-916c-cd39e79ea00e.png)
5. On the next screen, configure the parameters if required. Click **Done**.
6. Remember to publish the draft.

   ![contentId-1873969278](/cms_trial/assets/1a2e84bd-30c3-4339-a2d6-4e34ae6b83ab.png)

If these post functions fail, the workflow transition will still be completed.