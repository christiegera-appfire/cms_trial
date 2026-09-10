# Close parent issue when all subtasks are closed - Legacy

---

|  |  |
| --- | --- |
| **Goal** | Eliminate repetitive tasks and save time by automatically closing parent tasks |
| **Scenario** | When your team has closed all of an issue’s subtasks, the parent issue remains open and someone has to manually move it to done. Let’s look at how this common task can be automated with JSU. |
| **Components** | [Linked Transition](/cms_trial/space/JSUCLOUD/12518766/Linked+Transition+post+function/) post function |

## How to configure this rule

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Diagram mode. If you haven't already, switch the workflow viewer to Diagram mode.

   ![Screenshot of the Jira workflow editor in Diagram mode.](/cms_trial/assets/90eb904a-757a-4f33-b868-c5a2d0cf6fab.png)
2. We want to close parent issues when their subtasks are done, so we need to add the rule specifically to when issues transition to the DONE status. Click the arrow that points to this status to show the transition rule options menu.
3. We want to add a post function to this transition that runs an automation after the issue has been transitioned to the target status. Select **Post Functions** from the options list to display the *Post Functions* tab.

   ![Screenshot of the Jira workflow editor showing post functions highlighted in the transition options menu.](/cms_trial/assets/78259b0f-6174-4d08-bc86-dd6db146c9db.png)
4. Select **Add post function** to view all available post functions.
5. Select the *Linked Transition (JSU)* post function, and then click **Add** at the bottom of the page.
6. We want the parent to automatically close when the last subtask is closed, so we select **Parent/Sub-task** > **The parent of the subtask(s)**.
7. Next, we define **the workflow** and transition we want to apply to the selected parent issue. We want to keep this rule simple, so we only want this rule to apply to issues in our *JSU* project.   
   We select the workflow for our JSU project and the `Done` transition. Any parent issues will be transitioned to DONE as part of the rule we're configuring.

   ![Example configuration of the Linked Transition post function.](/cms_trial/assets/c424cf4e-533f-4579-8c25-d7c322d8757c.png)
8. We only want the parent to be transitioned to DONE if **ALL** of its subtasks are also DONE. We set the conditional status to done.
9. The remaining fields are **optional**. All of these fields are described in detail in the [Linked Transition](/cms_trial/space/JSUCLOUD/12518766/Linked+Transition+post+function/) post function page.
10. Now you're ready to save your new post function. Select **Add** at the bottom of the page.
11. You can now see a**summary** of all your post functions applied to this transition. To confirm this new workflow and test it out, you need to publish it. At the top of the page, select **Publish Draft**. You can choose to save a backup if required before confirming.

## Test the post function in the workflow

Now, we can test the post function in action.

1. Go to an open issue that includes one or more open subtasks.

   ![Example Jira issue with multiple subtasks in the To Do status.](/cms_trial/assets/91f174bd-166a-4835-a006-2953a47c9815.png)
2. Transition all of the subtasks to done.

   ![Example Jira issue with multiple subtasks that have been moved to the Done status.](/cms_trial/assets/4457c982-cfba-4e1b-b5f2-0699effd4fd3.png)
3. Refresh/reload the parent issue. You'll notice that it has now also been transitioned to done - which means our post function has worked as expected!

   ![Screenshot of an example Jira parent issue that was moved to the Done status through a JSU automation.](/cms_trial/assets/b72cf7fd-9412-43a9-9c4d-0f037da1b51c.png)

---

Need more information or help? [Get in touch!](https://appfire.atlassian.net/servicedesk/customer/portals)