# Update an issue only in certain conditions

---

Preconditions allow you to execute a post function only under certain circumstances. This helps you create more complex behaviors on your post functions, enabling Jira to do more work for you. In JSU for Jira Cloud, preconditions are part of the post function configuration.

The following use case explains how to get started with JSU preconditions for post functions.

|  |  |
| --- | --- |
| **Goal** | Organize your budget approval issues |
| **Scenario** | *You want to organize your budget approval issues using a project component.*  We will use the Update Any Issue Field post function to set the issue component to Budget, ONLY IF:   - the issue summary contains the word `budget` and; - the issue type is `Story`.   Let's have a look at how this can be automated using preconditions with JSU. |
| **Components** | - [Update Any Issue Field](/cms_trial/space/JSUCLOUD/12518373/Update+Any+Issue+Field+post+function/) post function - [Value Field precondition](/cms_trial/space/JSUCLOUD/12518009/Value+Field+precondition/) - [JQL precondition](/cms_trial/space/JSUCLOUD/12518033/JQL+precondition/) |

## How to configure this rule

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Diagram mode. If you haven't already, switch the workflow viewer to Diagram mode.
2. We want our automation to be executed on the *Create* transition, so we select the arrow that points to To Do to display the *Options* menu.
3. Select **Post Functions** then select **Add Post Function** to display the list of available post functions.
4. Select the *Update Any Issue Field (JSU)* post function then select **Add** at the bottom of the page.
5. On the post function configuration page, select **Add Precondition**.

   ![Add precondition page.](/cms_trial/assets/97c588d9-4e89-4c4f-b208-0c392de27e67.png)
6. We want our preconditions to ensure that only issues with issue type, *Story,* and a Summary containing `budget` text should be targeted for our post function execution.

   1. Add the Value Field precondition, and set `Issue Type = Story`
   2. Add the JQL precondition, and define a query to ensure that only issues containing `budget` in their summary will be found e.g. `key={issue.key} AND summary~budget`.   
        
      ℹ️ You can configure the above preconditions using only JQL. In this case, the search query would be: `key={issue.key} AND summary~budget AND issuetype=Story`. Use a configuration method that is simplest for you.  
      ✅ Always include the query `key={issue.key}` (or similar) on your JQL condition. This ensures that JQL is performed on the current issue. For more details see [JQL Precondition](/cms_trial/space/JSUCLOUD/12518033/JQL+precondition/).

      ![Example of configured Value Field and JQL preconditions.](/cms_trial/assets/b3f5d1cf-18f2-4bc9-ba4e-c4a78961d540.png)
7. Configure the post function.

   1. *Preconditions must be*: set this to **True**.
   2. *Update field on all issues related as*: select **Within same issue**.
   3. Issue Field: select **Component**.
   4. Field Value: enter `Budget`.

      ![Post function configuration with precondition set to True.](/cms_trial/assets/9eef1b7e-994a-485d-ab30-080623ffa22d.png)
8. Select **Add** at the bottom of the page.
9. Publish the workflow.

## Test the rule

1. To test our rule, we create an issue with issue type *Story* and call it *Budget for Hardware*. When we reload the issue, we can see that JSU updated it with the component `Budget`.

   ![Example Jira issue where the precondition is met and the Budget component is added.](/cms_trial/assets/dd2d0e2c-b094-4e31-98f1-464d97093985.png)

Need more information or help? Check out the JSU topic for [workflow preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/).