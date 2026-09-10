# Close parent issue when all subtasks are done

---

|  |  |
| --- | --- |
| **Goal** | Eliminate repetitive tasks and save time by automatically closing parent tasks |
| **Scenario** | When your team has closed all of an issue’s subtasks, the parent issue remains open and someone has to manually move it to done. Let’s look at how this common task can be automated with JSU’s Universal Rule Builder. |
| **Components** | [Universal Rule Builder](/cms_trial/space/JSUCLOUD/12517805/Universal+Rule+Builder/): *Related Issue Status* and *Create a Linked Transition* |

## How to configure this rule

This setup uses JSU’s Universal Rule Builder, which is a faster and simpler way to build and edit an automation rule. All of the necessary components are in one place, and you can preview the rule without leaving the configuration page.

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Diagram mode. If you haven't already, switch the workflow viewer to Diagram mode.

   ![Screenshot of Jira workflow editor in Diagram mode.](/cms_trial/assets/9b2bfff1-0e03-43f8-b83d-d3ab22822429.png)
2. We want to close parent issues when their subtasks are done, so we need to add the rule for when issues transition to the DONE status. Click the arrow that points to this status to show the transition rule *Options* menu.
3. Select **Post Functions** to display the *Post Functions* tab.

   ![Screeenshot of Jira Workflow editor showing post functions highlighted in the transition options menu.](/cms_trial/assets/db22bdab-4a68-4cb9-827a-8956bf328bcf.png)
4. Select **Add post function** to view all available post functions.
5. Select the *Access the Universal Rule Builder from JSU* post function, then click **Add** at the bottom of the page. The Universal Rule Builder displays.

   ![List of available post functions shown with the Universal Rule Builder selected.](/cms_trial/assets/8c4a0724-f37d-4fad-9195-9693e88595c8.png)
6. We only want the parent to be transitioned to DONE if **all** of its subtasks are DONE, so we begin by adding a condition. Under *All Components*, select the **Related Issue Status** condition.

   ![Screenshot of the URB list of components.](/cms_trial/assets/c43d4828-646e-487b-91fb-d77e911274c5.png)
7. Select **All Siblings** from the *Relation to issue* dropdown, then select the done status. The condition displays in the rule overview. Next, we define the action that will occur if this condition is true.

   ![The Universal Rule Builder with a configured Related Issue Status condition.](/cms_trial/assets/763458da-cf36-4956-935d-6eb4187225c6.png)
8. Select **Add Component** in the overview.
9. Under *All Components*, select the **Trigger a Linked Transition** post function.

   ![Screenshot of the URB with the selected post function highlighted.](/cms_trial/assets/e6cdca00-9865-4fd8-8b73-885c6e2eab54.png)
10. To configure the action:

    1. Select the type of issue you want to move to a new status when the rule is triggered. We want to move the parent issue to done, so we select **Parent of the task**.
    2. Select the destination status for the issue. Here, we select done from the *Status* dropdown.

       ![Universal Rule Builder with a configured post function and condition.](/cms_trial/assets/00f38c9b-fedf-4337-8ecc-d22cacfcc4b7.png)
11. Enter a name for the rule. Choose a name that helps you identify the rule, for example, `Move parent to Done`.

    ![Screenshot of the URB overview with the Name field complete.](/cms_trial/assets/06078218-e47c-475d-8b61-d35271338cba.png)
12. Select **Add** at the bottom of the page. Asummary of all your post functions applied to this transition is displayed in the draft workflow.

    ![Summary of draft Jira workflow ready to publish.](/cms_trial/assets/5ae8678f-bd06-4a55-93ae-64addaf533ea.png)
13. Select **Publish Draft** at the top of the page. You can choose to save a backup if required before confirming.

## Test the post function

We recommend that you build and test your rules in a test project.

1. Go to an open issue that includes one or more open subtasks. If you do not have a test project with the necessary issues, create a task and add a few subtasks.

   ![Example Jira issue with multiple subtasks in the To Do status.](/cms_trial/assets/565e40cd-ba73-4f20-a4c3-d2ffbf1d33cc.png)
2. Transition all of the subtasks to done.

   ![Example Jira issue with subtasks moved to the Done status.](/cms_trial/assets/c008e491-bcb6-406a-9931-0a1637a0b379.png)
3. Refresh the browser to reload the parent issue. You'll notice that it has now also been transitioned to done - which means our post function has worked as expected.

   ![Screenshot of the example Jira issue with parent task in the Done status.](/cms_trial/assets/17ab0698-88ac-47b4-b08f-3c68edbb7b97.png)