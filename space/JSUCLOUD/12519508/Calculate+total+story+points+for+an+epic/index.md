# Calculate total story points for an epic

---

|  |  |
| --- | --- |
| **Goal** | Use Jira to run a calculation rather than extracting data to another platform or performing the calculation manually. |
| **Scenario** | Imagine you are a Manager who relies on multiple calculations to make business decisions. You can simplify your work by attaching numerical values within project issues and displaying calculations on the project epic. With some preplanning, you can then use JSU to run the calculations for you. Let’s see how we use JSU to calculate the ‘Total Story Points’ on an epic. |
| **JSU Components** | [Calculated Field](/cms_trial/space/JSUCLOUD/12520029/Calculated+Field+post+function/) post function |

## Example setup

1. Create and add the custom fields on which you will build your calculations, e.g. Total story points on epic.
2. Create an epic in your project and add the associated stories and tasks.
3. Add story points to each of the epic’s child issues.

## How to configure this workflow

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Text mode. If you haven't already done so, switch the workflow viewer to Text mode.
2. Select the IN PROGRESS transition.
3. Select the *Post Functions* tab, then click **Add Post Function.**
4. Select the Calculated Field (JSU) post function then click **Add** at the bottom of the page.

   ![Screenshot of the list of JSU post functions showing the Calculated Field post function selected.](/cms_trial/assets/93dab533-33e0-4c74-80e7-59ab73221f8a.png)
5. Configure the post function:

   1. For the *Calculate field on all issues related as* option, select **Within the same issue.**

      ![Screenshot of the Calculated Fields post function configuration options.](/cms_trial/assets/fcc5f1dc-140a-436f-82b3-7f215369492f.png)
   2. Select *Total story points* from the field dropdown. This is the field we created in our example setup.
   3. Define the formula:

      1. We want to calculate the sum of the story points in the stories of our epic, so we select the *Sum* function from the dropdown and then select the *issuesInEpic* function. When the *issuesInEpic* function is combined with a function like the *sum*, it will retrieve the values of the selected field from all issues in the epic.
      2. Select the *Story points* field to add it to the formula. 

         ![Example formula for calculating the total story points for an epic.](/cms_trial/assets/ffba77a2-7771-4b36-80c3-937c86e462cc.png)
6. Click **Add**.
7. Publish your workflow.
8. Move the epic to In Progress and see the sum of all the story points from all the child tasks displayed in the epic’s Total Story Points field.