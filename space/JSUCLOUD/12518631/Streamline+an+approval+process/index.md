# Streamline an approval process

---

|  |  |
| --- | --- |
| **Goal** | Save time and effort by streamlining approvals processes |
| **Scenario** | You want to eliminate unnecessary steps and downtime for those requesting approval, and those approving too. Use automation to automatically transition issues that don’t need approval and restrict the Approved action to selected users. |
| **JSU Components** | - [Follow Up Transition](/cms_trial/space/JSUCLOUD/12518817/Follow+Up+Transition+post+function/) post function - Value Field condition (Jira) - [User is in any users](/cms_trial/space/JSUCLOUD/12518827/User+Is+In+Any+Users+condition/) condition (JSU) |

## How to configure this rule

In this example, we are using an Approvals workflow that we configured for this use case. You can [re-create this workflow](https://support.atlassian.com/jira-cloud-administration/docs/work-with-issue-workflows/) in your instance in a few minutes. The main feature of the workflow is that from the submit status, the issue can move to either awaiting approval or approved.

![Approval workflow in Jira](/cms_trial/assets/3c298f21-4254-4264-b470-66a01aad9195.png)

First, we want to set the criteria we'll use for determining what *requires approval*and what can be streamlined to be automatically *approved***.**

### Part 1: Add Value Field conditions for the Submit → Awaiting Approval transition

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Diagram mode. If you haven't already, switch the workflow viewer to Diagram mode.
2. Select the transition (arrow) connecting the  SUBMIT and AWAITING APPROVAL statuses to display the transition rule options menu.
3. Select **Conditions** from the options list to display the *Conditions* tab.

   ![Draft Jira workflow in diagram view with the transition options menu displayed.](/cms_trial/assets/6b63ba1c-b1a9-476d-88b0-6ec717d4c035.png)
4. Select **Add Condition**.

   ![Conditions tab on the draft workflow transition page.](/cms_trial/assets/3cd43f05-2d5a-489a-a3dc-a06e3269dfe7.png)
5. Select the *Value Field* condition, then select **Add** at the bottom of the page.

   ![List of available workflow conditions in Jira with the Value Field condition selected.](/cms_trial/assets/84bc28d8-563b-4292-be7e-d7c9c4dcd002.png)
6. Now, let's configure the condition to ensure that only the desired issues can transition to awaiting approval.

   1. **Field**: Select the field you want to inspect to determine if an approval can be streamlined for it. In our case, we have a field called `'Budget Required' that we've selected`.
   2. **Condition** - Choose the type of comparison you will use when comparing with the value. In our case, we want to require approval when the *Budget Required* is greater than (or equal to) 1,000. So we need to choose `greater-than-or-equal-to / >=`***.***
   3. **Value**: Type in the value you want to compare the field against. In our example, our chosen value is `1,000`***.***
   4. **Comparison Type**: To ensure that the value (a number) can be compared against the field (also a number), we need to specify that, in this scenario, the value is a `Number`***.***

      ![Value Field condition configuration for budget greater than or equal to 1000.](/cms_trial/assets/cbeb779b-7b64-41ff-a4a3-5eab60011c50.png)
7. Select **Add**. A preview of the condition we've just configured displays.

   ![Draft Jira workflow summary page for the Awaiting Approval transition.](/cms_trial/assets/020b2a42-3ab8-4682-aedf-38d44a92a8d2.png)
8. Publish the draft workflow. Now let’s configure a rule for the other transition.
9. Return to the Approvals workflow and create a draft again.
10. Select the transition (arrow) connecting the submit and approved statuses to display the transition rule Options menu.
11. Repeat steps 3-7, only in the case, we set the Conditionfieldto less-than`<`to ensure that issues with a Budget Required of less than 1,000 can be moved to Approved instead of awaiting approval.

    ![Value Field condition configuration for budget less than 1000.](/cms_trial/assets/50c0c83e-3b4d-4e6a-814f-559300f7f4b9.png)
12. Select **Add**. A preview of the condition we've just configured displays as with the previous condition.
13. Publish the draft workflow then move to Part 2.

### Part 2: Add the User is in any user condition for the Awaiting Approval → Approved transition

1. In the draft workflow, select the transition (arrow) connecting the  AWAITING APPROVAL  and approved statuses to display the transition rule options menu.
2. Select **Conditions** from the options list to display the *Conditions* tab.
3. Select **Add Condition**.
4. Select the *User is in Any Users* condition then select **Add** at the bottom of the page.
5. Add one or more users to the condition. Only the selected users can transition the issue.

   ![JSU-add-condition-approvals.png](/cms_trial/assets/2539c65e-1e7d-4dbe-8013-83345b1fa4a4.png)
6. Select **Add**.

### Part 3: Add JSU’s Followup Transition post function

1. Create another draft of the Approvals workflow.
2. In Diagram mode, select the transition (arrow) connecting In progress and submit.
3. Select **Post Functions**from the Options menu.

   ![Draft Jira workflow in diagram view with the transition options menu displayed.](/cms_trial/assets/0fd84a51-165b-4e6f-a777-1a4208a002f2.png)
4. Select **Add post function** on the *Post Functions* tab.
5. Select *Follow Up Transition (JSU)* then select **Add** at the bottom of the page.

   ![List of available Jira workflow post functions with the Follow Up Transition selected.](/cms_trial/assets/189043a3-3551-4439-891a-6b09193a4575.png)
6. You do not need to configure the post function. Select **Add** again.

   ![Follow Up Transition post function configuration page.](/cms_trial/assets/375d4f58-162a-406a-af1c-7dc368995ea2.png)
7. Publish the workflow.

### Test the rule and see the automation in action

1. Go to an open issue in your Approvals project. In our case, we have an issue currently in  In progress and with a *Budget Required*of 500.

   ![Example Jira issue with a budget field set to 500.](/cms_trial/assets/aab145fc-6710-4d41-97d2-6670ef6a9462.png)
2. Let's move the status to submit.

   ![Example Jira issue with a budget field set to 500 moved to Submit status.](/cms_trial/assets/e8db4636-7bc5-44c2-b417-2de516069943.png)
3. The issue moves to the submit status, then a second (or two) later, automatically to the approved status.

   ![Example Jira issue with a budget field set to 500 moved to the Approved status.](/cms_trial/assets/f63c03f1-b7e4-46b6-afa5-323539ed4775.png)

   The issue history confirms this streamlined transition occurred.

   ![History tab in example Jira issue shows the issue was moved from Submit to Approved.](/cms_trial/assets/c62211c4-a81b-43cc-92a4-4ec28c52c743.png)
4. Now try the same scenario, but where the *Budget Required* is 1,000, or more.

   ![Example Jira issue with a budget field set to 1000.](/cms_trial/assets/3428e4d7-9656-4e8a-9934-1fdee24fb8bf.png)
5. Let's move this issue to submit just like we did before.

   ![Example Jira issue with a budget field set to 1000 moved to Submit status.](/cms_trial/assets/6eeec94c-ba64-4bff-9a9e-faef09f7c425.png)
6. Again, the issue is forwarded to its appropriate next transition; in this case, as the *Budget Required* valueis greater-than-or-equal-to 1,000, it's moved to awaiting approval. Only the users named in the User is in Any User condition set up in Part 2 can select the Approved transition.

   ![Example Jira issue with a budget field set to 1000 moved to the Awaiting Approval status.](/cms_trial/assets/26a5aa25-72cb-4126-a987-fb497f9edb8e.png)
7. The issue history confirms that JSU helped us streamline the approvals here.

   ![History tab in example Jira issue shows the issue was moved from Submit to Awaiting Approval.](/cms_trial/assets/6c5f2d66-43d7-4882-acec-2231a2817b19.png)