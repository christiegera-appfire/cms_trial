# Automatically remove a closed epic from the backlog

---

|  |  |
| --- | --- |
| **Goal** | Get a clear view of your team's actual backlog |
| **Scenario** | *Do your epics stay in the backlog of your Jira agile board after closing them? Here's why.*  Besides the workflow status, epics have an additional field called *epic status* which is only accessible on the Backlog screen. Only epics with the Epic status field marked as DONE get removed from the backlog.  Let's have a look at how this can be automated using JSU. |
| **Components** | - [Update Any Issue Field](/cms_trial/space/JSUCLOUD/12518373/Update+Any+Issue+Field+post+function/) post function - [Value Field](/cms_trial/space/JSUCLOUD/12518009/Value+Field+precondition/) precondition |

## How to configure this rule

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Text mode.
2. Select the transition for which you want to run the post function. In this case, we are using the done transition.

   ![Screenshot of a draft workflow issue page displayed in Text mode with the Done transition highlighted.](/cms_trial/assets/2f74f9a7-3807-4c91-a71d-ef0f7ba15c22.png)
3. Select the *Post Functions* tab, then select **Add Post Function**.
4. Select the *Update any issue field (JSU)* post function, then click **Add**.
5. Because we want to perform this post function only for Epics, we need to configure a [precondition](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/). Set the precondition to be *True*. In this transition, you want to have your Epic status updated to done.
6. Complete the required fields to configure the post function:

   1. *Update field on all issues related*: **Within same issue**
   2. *Issue Field*: **Epic status**
   3. *Field Value*: **Done**

      ![Configuration options for the Update Any Issue Field post function.](/cms_trial/assets/829ab4de-cd63-4326-b551-c65bdec8a03c.png)
7. Create your precondition to prevent errors when the workflow is used on non-epic issues. Click **Add Precondition,** then click **Add** next to the *Value Field* precondition.

   ![Screenshot of the list of available JSU preconditions.](/cms_trial/assets/051a9913-ec5e-417f-b7f0-ad22d8edde18.png)

   .
8. Set Issue type = `Epic`.

   ![Value Field precondition options set to Issue field is equal to Epic.](/cms_trial/assets/f19d6e79-d438-4cb0-9746-55a4fc513a81.png)
9. Select **Add** at the bottom of the configuration page, then publish your workflow.
10. Now test your new post function with some test issues. Your epic is currently visible on the backlog; move your epic to done and go back to your backlog. The epic is longer there.

This is only a sample of what you can do with JSU. See our [app documentation](/cms_trial/space/JSUCLOUD/12518373/Update+Any+Issue+Field+post+function/) for some more examples and configuration screenshots.