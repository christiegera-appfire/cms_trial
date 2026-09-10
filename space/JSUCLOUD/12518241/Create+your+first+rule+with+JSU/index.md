# Create your first rule with JSU

This example scenario shows you how to add a JSU automation rule to your team-managed space using the *Linked Transition* post function.

***Have you ever forgotten to close your subtasks before you close a work item?***

Let’s see how we use JSU to automate closing multiple subtasks under a parent work item.

Video transcript

The JSU Automation Suite for Jira Cloud is a no-code solution to help you and your teams work faster and more efficiently. Using a collection of post functions, conditions, and preconditions, you can configure workflow rules to increase productivity, facilitate team collaboration, and seamlessly transition your work.

JSU offers unlimited automation rule runs, so you can set up and manage your workflow automations exactly as you need without worrying about reaching usage limits.

Even more, JSU now supports team managed Spaces in Jira Cloud! This opens up JSU automations to Space Administrators, enabling them to create rules for only their Space.

This video will demonstrate how to create a new JSU rule for a team-managed project.

To add a new JSU rule, go to Space settings and expand Work types. Click the work type you want to automate, and click Edit workflow.

Select the transition that should trigger your new rule. In this example, we'll use the transition into Released.

Click Restrict transition.

Click Add Restrict transition rule.

Select JSU Rule Builder - Conditions and click Select. This will let us restrict the transition so that all subtasks of a Story need to be in a status of Waiting for Release before the Story can be transitioned to Released.

Give your rule a name and click Add condition.

Select Related issue status.

For issue relation, select Subtask of the parent issue in transition.

For issue status, select the status values Waiting for Release.

Click Add.

Click Update workflow to publish your updated workflow.

To test our new rule, we try to move a work item with subtasks to Released. Note that the transition is not available because one subtask is still In Progress. Once that subtask is updated, the transition becomes available, and when we move the Story, all subtasks have also been moved to Done!

## Instructions

|  |
| --- |
| **Step 1: Edit the workflow for your Team-managed space** |
| From **Space settings** click **Work types** → **Story** → **Edit workflow**. Edit your workflow to add a JSU Automation |
| **Step 2: Select the transition that you want to trigger the post function** |
| In the workflow editor, select the transition into the *Done* status (point 1, Figure 2). Click **Add Rule** (point 2, Figure 2). Add a JSU Automation rule to your workflow transition |
| **Step 3: Select JSU post function** ***Linked Transition.*** |
| From the list, select **Linked Transition (JSU)**. Click **Select**. Select the JSU Cloud post function Linked Transition (JSU) |
| **Step 4: Configure the post function** |
| The automation should transition all sub-tasks to the *Done* status when their parent work item is transitioned.   1. Select **Parent/Subtask** then select *The subtask(s) of a parent.* 2. Select the workflow for your sub-tasks and the transition into *Done*. 3. Click **Add**.  Configure your JSU Cloud post function |
| **Step 5: Update your workflow** |
| Click **Update workflow** to save your changes. |

| Test the workflow rule |
| --- |
| Once the workflow is saved, you should test the outcome. To help ensure that your JSU rules work the way your team expects, run them in a test space with user permissions that represent the different roles within your team.   1. Set up an issue and create multiple sub-tasks in our test space. 2. Transition the parent issue to *Done* then watch JSU move all sub-task statuses to *Done* automatically.   Don't forget to click refresh your browser to see the changes. |

You can learn more about how JSU can improve your workflows by following the worked examples in our [use cases](/cms_trial/space/JSUCLOUD/12518487/Use+cases/). Our [Features](/cms_trial/space/JSUCLOUD/12518429/Features/) sections provides details on the different parameters or options you can use when configuring our post functions, conditions, or validators.

## Related pages

- [Use cases](https://appfire.atlassian.net/wiki/spaces/JSU/pages/12682671)
- [Universal Rule Builder](/cms_trial/space/JSUCLOUD/12517805/Universal+Rule+Builder/)
- [JSU features guide](https://appfire.atlassian.net/wiki/spaces/JSU/pages/12682804)