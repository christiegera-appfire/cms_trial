# Remove assignee when an issue moves back to To Do

---

|  |  |
| --- | --- |
| **Goal** | Remove the Assignee when an issue moves back to to do and transition all subtasks in progress back to to do . |
| **Scenario** | You identify a change in priorities. Progress on an issue may need to be paused or stopped entirely so you want the Assignee field set to Unassigned when the issue moves back to to do. Because work is paused on the parent issue, you want to ensure that all subtasks in progress automatically move back to to do. |
| **Components** | [Universal Rule Builder](/cms_trial/space/JSUCLOUD/12517805/Universal+Rule+Builder/): *Update Any Issue Field* and *Trigger a Linked Transition* |

This setup uses the Universal Ruler Builder. Here, you can see how easily you can configure two different post functions in one place.

## Example setup

Follow the interactive demo to learn how to set up this use case, or follow the numbered steps below.

## How to configure this rule

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Diagram mode. If you haven't already, switch the workflow viewer to Diagram mode.

   ![Screenshot of Jira workflow editor in Diagram mode.](/cms_trial/assets/c25e8d2d-0a7f-4494-9012-d9c63711c801.png)
2. We want the post function to run when an issue moves to to do. Click the arrow that points to this status to display the transition *Options* menu.
3. Select **Post Functions** to display the *Post Functions* tab.

   ![Screenshot of Jira workflow editor showing post functions highlighted in the transition options menu.](/cms_trial/assets/63897810-35f1-42ec-b7d2-8683ef623e6e.png)
4. Select **Add post function** to view all available post functions.
5. Select the *Access the Universal Rule Builder from JSU* post function, then click **Add** at the bottom of the page. The Universal Rule Builder displays.

   ![List of available post functions shown with the Universal Rule Builder selected.](/cms_trial/assets/c78bf644-3e89-4f75-b4e3-c8d7491469b1.png)
6. In the list of components, select the Update Any Issue Field post function.

   ![Screenshot of The Universal Rule Builder with the list of available components.](/cms_trial/assets/d4bf6518-ac2e-4c7c-9c53-8e488a799df6.png)
7. To configure the post function:

   1. From the *Field Name* drop-down list, select the field that you want to update following the transition. Here, we select *Assignee*.

      ![Screenshot of the field options drop-down list displaying the Assignee field.](/cms_trial/assets/25a680b5-5928-4854-8db0-bc8b213671ba.png)
   2. In the *Assignee* field, select the new value that you want to assign to the field when the transition is complete. Here, we select *Unassigned*.

      ![Screenshot of the Assignee field set to Unassigned.](/cms_trial/assets/cae12800-0a31-443e-b4b7-72fb5733c7d7.png)
8. In the rule overview, enter a name for the rule. Choose a name that helps you identify the rule, for example, `Update assignee to Unassigned`.

   ![Screenshot of the rule overview as described in the procedure on this page.](/cms_trial/assets/f022af7b-d1a9-4620-aa98-8290f240d62f.png)
9. Click **Add component**.
10. In the list of components, select Trigger a Linked Transition.
11. Select **The subtasks of the parent** issue relation type option.
12. Select the **To Do** status from the list of available statuses.

    ![JSU-URB-Trigger-a-linked-issue.png](/cms_trial/assets/84df29ef-fa58-4dd0-8f90-321aa5bbf330.png)
13. Select **Add** at the bottom of the page. Asummary of all your post functions applied to this transition is displayed in the draft workflow.
14. Select **Publish Draft** at the top of the page. If necessary, you can save a backup before confirming.

## Test the post function in the workflow

We recommend that you build and test your rules in a test project.

1. Go to an issue in your project that is in progress or another status that can be transitioned back to to do. If you don’t have any, you can create one and select an assignee. Ensure that this issue has subtasks that are in in progress .

   ![Jira issue assigned to Demo-user.](/cms_trial/assets/3a89dfd7-6616-45a8-9c68-3b1109b6dfae.png)
2. Move the issue to to do.
3. Refresh your browser to reload the issue. You'll see that the previous assignee has been removed and the issue is unassigned.
4. Go to one of the issue’s subtasks that was in progress and confirm the status has changed to to do .

   ![Jira issue is unassigned after the transition to To Do.](/cms_trial/assets/52fee34e-a9f9-4741-89ce-a25842820c24.png)