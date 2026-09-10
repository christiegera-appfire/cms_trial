# How to enable status transition from Salesforce to Jira using Automation for Jira

## Purpose

We'll discuss how to synchronize status from Salesforce to Jira since the status field in Jira is **read-only**. This allows the pushing of status updates from Salesforce to Jira, thus completing the overall automated workflow process. The following are the steps to show how you can utilize Automation for Jira in conjunction with the connector to enable a more seamless workflow transition.

## Answer

The following knowledgebase article explains how you can utilize Automation for Jira in conjunction with the connector to enable a more seamless workflow transition.

You may incur charges for using Jira Automation. For Jira Cloud, single project rule executions do not count towards the usage. Check this documentation for more information: [How is my usage calculated?](https://support.atlassian.com/jira-software-cloud/docs/how-is-my-usage-calculated/) You can also [view your usage](https://support.atlassian.com/jira-software-cloud/docs/view-your-usage/) to keep track of how many executions left in the month. For Jira Server, please see guidelines [here](https://marketplace.atlassian.com/apps/1215460/automation-for-jira-server?hosting=server&tab=overview).

## Basics: Automation for Jira

The main thing about automation is to create a **rule**. The **rule** in Automation for Jira consists of 4 key concepts:

- Triggers - The starting action that will be used as a reference to kick-off the automation. (The *Listener)*
- Conditions - This allows the user to narrow down the scope and be more specific on the required use-case.
- Actions - When the Triggers and Conditions are met, this will be the one that performs the ***automation****.*
- Branch Rule - This will apply the actions to all the related issues that you’ve selected/filtered.

## Creating a rule

For this example, we are creating a rule to specifically automate status transition. Automation for Jira can be used for many other use cases.

1. Navigate to **Settings > System > Global automation.**  
   You can also press “Cmd + K” or “.” (dot) to open up the shortcut navigator and search for “Automation”.

   ![Screenshot of navigator](/cms_trial/assets/994e89dd-8110-4591-99c6-63f8b8b95f4b.png)
2. Click **Create rule** on the top right.
3. This is where you will need to specify the **Trigger.**

   ![contentId-1874002066](/cms_trial/assets/bde4add6-b4a6-49c5-8a94-5dd6f0ecb546.png)
4. Select **Field value changed**for this specific use-case to automate remote status transition.
5. Have a custom field configured in Jira that acts as a middle-man between Jira and Salesforce. We recommend using the **Select List (Single Choice)**field type as it can be an additional *status*field that can be used to sync Salesforce and Jira. We created the **Remote Status Transition** field as an example - see diagram below.
6. You can also select if you want it to be specific to a *Work item operation*: Create work item, Edit work item, Transition work item, Assign work item, or leave it blank for *All* *work item operations*.

   ![2025-10-16_09-29-29.png](/cms_trial/assets/c638aa2d-ba18-43b9-8f77-48ac23ee40f7.png)
7. After clicking **Next**, you can choose to add a **condition, branch rule, or action**.

   ![2025-10-16_09-30-44.png](/cms_trial/assets/aac66873-82f3-414e-932a-f56275ba74cd.png)
8. Select **Add a condition.**

   ![screenshot of condition](/cms_trial/assets/b9e10d95-be56-4b1c-a127-2010455fe1ac.png)
9. From here, you can choose how to narrow down the scope. We use **User condition** and we select the **Salesforce & Jira Cloud Connector**app user (at the Criteria) as the **User condition.**

   ![screenshot of fuser condition](/cms_trial/assets/57878320-1a70-4743-b9d9-063fa2790dcd.png)
10. Step 9 will ensure that the automation will only run if the value is changed by the Salesforce and Jira Connector app.
11. Add an additional condition by selecting the **New condition** again then select the **Work item fields condition**.
12. Now, select the custom field that you’ve created. in this scenario, we will select **Remote status transition** and select **equals** to **Yes**. This **Work item fields condition**combined with the **User condition** (in step 9) will make sure that the automation will only run if the value of the field is changed to **Yes**, and the user who changes the value is the **Salesforce & Jira Cloud Connector**app user. ⚠️ Ensure that the field is added to the “Edit” Jira Issue screen; otherwise, the Automation would not be able to detect the field changes.

    ![screenshot of work item field condition](/cms_trial/assets/d9fb8895-6ac5-4b3e-bc58-fe2602b134c8.png)
13. After saving, add a **New action.**
14. From here, you can select the various types of actions that the automation can perform. Select **Transition work item.**
15. Select the **Destination status**to the status that you want the automation to transition to.

    ![screenshot of transitioning work item](/cms_trial/assets/9f0353f5-cdde-4491-ba50-873387de9ab6.png)
16. Lastly, click **Turn on rule** to enable the automation.

    ![contentId-1874002066](/cms_trial/assets/1ccb8cf6-2386-42ea-9b40-5501b680b1f6.png)
17. Now, you’ll have an automation that will transition the issue status to **Waiting for Jira Team** whenever the following scenario occurs.

    1. The value for the **Remote Status Transition** field is updated.
    2. The user that updates the **Remote Status Transition** field is the **Salesforce & Jira Cloud Connector**app user.
    3. The value for **Remote Status Transition** is changed to **Yes**.

## Workflow post-function to synergize with the automation

1. Since the above automation is configured to transition the issue to a specific status based on a Select List field value, we can create a post-function to enable looping.
2. To do that, navigate to the project’s workflow (Project settings > Workflow)
3. Click on a transition to the status, and click **Post Functions** on the right.

   ![Screenshot of Post Functions option](/cms_trial/assets/94714b34-82d3-481d-a154-6683995c4625.png)
4. From here, click on the **Add post function**button on the right.

   ![screenshot of Add Post Function window](/cms_trial/assets/c66dc34f-d498-4f99-a533-fae2bbe03f82.png)
5. Select **Update Issue Custom Field**and click **Add.**

   ![Screenshot of Post Functions to transition](/cms_trial/assets/e4724357-1c4c-4502-b011-2cc48760efdf.png)
6. Select **Remote Status Transition**field and enter **No** for the Custom Field Value.

   ![Screenshot of adding Parameters to functions](/cms_trial/assets/c54a211d-66c1-44c5-b329-5a3608c2b2b0.png)
7. After adding the post function, remember to publish the draft of the workflow.
8. With the post function added, the **Remote Status Transition** field value will change to **No** whenever the transition happens, in this case, we configured the transition to **In Progress** status.