# Copy or move attachments

---

|  |  |
| --- | --- |
| **Goal** | Save your team’s time and effort by automatically copying or moving attachments to all of an issue’s subtasks |
| **Scenario** | Imagine you are a Manager and your team was assigned a creative project. You have prepared a Creative Document containing project details and uploaded it to a Jira issue. You have also created subtasks for each team member to work on.  You want to ensure that all team members are aware of and are working from the same details, so you copy the Creative Document to all subtasks. |
| **JSU Components** | [Copy/Move attachments](/cms_trial/space/JSUCLOUD/12518560/Copy+or+Move+Attachments+post+function/) post function |

## How to configure this workflow

There are 2 ways to use the copy/move feature. You can move or copy existing attachments from the source issue, or you can copy or move attachments that are added on a transition screen.

### Copy existing attachments

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Text mode. If you haven't already, switch the workflow viewer to Text mode.
2. Select the transition that will trigger the post function. We are using the in progress transition.
3. Select the *Post Functions* tab, then click **Add Post Function.**
4. Select the Copy/Move attachments (JSU) post function, then click **Add** at the bottom of the page.
5. Configure the post function:

   1. Choose the **Parent/Subtask** [issue relation](/cms_trial/space/JSUCLOUD/12518756/Related+issues/), as you want the post function to be performed when the parent issue is transitioned, and for the attachments to be copied to the subtasks.
   2. **Copy Existing Attachments**: Select the ***Always copy attachments*** option from the drop-down menu so that all the attachments included in the parent issue are copied to the subtasks. You can select a field in your parent issue to have a value, for the attachments to be copied to the subtasks. If you use this option, the attachments will only be copied to the subtasks if that field has a value.
6. Click **Add**.
7. Publish your workflow.

### Test your new rule

1. Go to your parent issue that contains the Creative Document.
2. Move your parent issue to in progress.
3. Refresh the page and see what you have achieved with JSU! Open your subtasks and check your attachments. The document is available, and the whole team can begin working without needing to search for it.

Make sure you edit the project's attachment permissions to be able to copy/move attachments.

### Move attachments added on the transition screen

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Text mode. If you haven't already, switch the workflow viewer to Text mode.
2. Select the transition that will trigger the post function. We are using an approve transition in our content workflow.
3. Select the *Post Functions* tab, then click **Add Post Function.**
4. Select the Copy/Move attachments (JSU) post function then click **Add** at the bottom of the page.
5. Configure the post function:

   1. Choose the **Parent/Subtask** [issue relation](/cms_trial/space/JSUCLOUD/12518756/Related+issues/), as you want the post function to be performed when the parent issue is transitioned.
   2. **Perform as User**: Select **Initiating User**.
   3. **Copy or Move Attachments added during Transition:** Select the **Move** option.
   4. Select the ***Always copy attachments*** option from the drop-down menu so that all the attachments added during the transition on the transition screen are moved to the subtasks. You can select a field in your parent issue to have a value, for the attachments to be moved to the subtasks. If you use this option, the attachments added on the transition screen will only be moved to the subtasks if that field has a value.
6. Click **Add**.
7. Publish your workflow.
8. Ensure that you [assign a transition screen](https://confluence.atlassian.com/jirakb/map-a-screen-to-a-workflow-transition-in-jira-server-720634253.html) to the Approve transition to enable the rule you have configured in your post function.

### Test your new rule

1. Go to your parent issue that contains the Creative Document.
2. Move your parent issue to approve .
3. Upload the Creative Document on the transition screen.
4. Refresh the page and see what you have achieved with JSU! Open your subtasks and check your attachments. The document is available, and the whole team can begin working without having to search for it.