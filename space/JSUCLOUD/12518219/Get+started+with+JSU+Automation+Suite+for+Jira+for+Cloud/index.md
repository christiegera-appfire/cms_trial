# Get started with JSU Automation Suite for Jira for Cloud

## Create your first rule

> **Estimated time:** About 5 minutes
>
> In this guide, you’ll create your first automation rule that will close sub-tasks when a parent work item is closed.

**JSU Automation Suite for Jira Workflows** is our no-code solution to help you and your teams work faster and more efficiently using post functions, conditions, and preconditions to configure workflow rules to increase productivity, facilitate team collaboration, and seamlessly transition your work.

JSU for Jira Cloud offers unlimited automation rule runs, regardless of your Jira plan. Set up and manage your workflow automation exactly as you need it without worrying about reaching usage limits.

## Before you begin

Before you start, make sure that:

1. You have administrator privileges for your Jira instance; creating a JSU rule requires administrator privileges.
2. You have access to the workflow to which this rule will be added.

## Create your first post function

1. 1

   Open your workflow in the Jira workflow editor.
2. 2

   Select the transition into *Done* (1) and click Add Rule (2).

   ![Add a JSU Automation rule to the Done transition. ](/cms_trial/assets/9264d3d9-08fb-48e2-be3d-3b8e51788618.png)
3. 3

   Select the **Linked Transition (JSU)** post function and click **Select**.
4. 4

   Configure the post function:

   1. 1. Select **Parent/Subtask** then select *The subtask(s) of a parent.*
      2. Select the workflow for your sub-tasks and the transition into *Done*.
      3. Click **Add**.![Configure the JSU Automation post function Linked Transition](/cms_trial/assets/fbbe974c-d260-465a-ba3b-b39bc91c3613.png)
5. 5

   Click **Add** to save the post function. Click **Update workflow** to save your workflow.

## Success!

You now have a rule that automatically closes any open sub-tasks when their parent work item is closed! You should thoroughly test your automation by creating a Story with sub-tasks, transitioning some of the sub-tasks to *Done* while leaving some open, and then transitioning your Story to *Done*. Verify that all sub-tasks are also closed.

---

## Start building automation rules

All set to go with your automation goals? Our [JSU Features guide](/cms_trial/space/JSUCLOUD/12518429/Features/) has everything you need.

You can also try our [Universal Rule Builder](/cms_trial/space/JSUCLOUD/12517805/Universal+Rule+Builder/) to build simple or complex rules from a single place, eliminating the need to navigate through Jira multiple times.

## Inspiration

See our [use cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) to explore examples of JSU in action before building your automation. Have a use case of your own that you want to share with other users? [Let us know!](https://appf.re/support)

## Migrating from Jira Data Center?

See our [Migrations](https://appfire.atlassian.net/wiki/spaces/JSU/pages/12683795) section for our feature parity and guides to migration with JCMA and Configuration Manager for Jira.

JSU Cloud is available on [Atlassian Government Cloud](https://www.atlassian.com/blog/announcements/expanding-pathways-to-cloud). If you are migrating to Atlassian Government Cloud and require a FedRAMP Moderate authorized app, you can use JSU for Jira Cloud for code-free automation.

## Need help?

Our Support team is always happy to assist if you encounter any issues with JSU or have feature requests or comments. [Contact us](https://appf.re/support) through our support portal.