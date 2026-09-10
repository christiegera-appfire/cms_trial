# Get started with JMWE for Jira Cloud

## Create your first extension

> **Estimated time:** About 5 minutes
>
> In this guide, you’ll create your first extention that will set the **Assignee** field when a work item is transitioned to *Testing*.

**JMWE for Jira Cloud** is our no-code solution to customize and automate workflows in Jira - built for advanced, unlimited automation and smarter workflow control. Using a combination of Event-based actions, scheduled actions, and workflow extensions, you can streamline processes, validate and guarantee data integrity, and save time and effort in moving your work forward.

JMWE for Jira Cloud offers unlimited automation rule runs, regardless of your Jira plan. Set up and manage your workflow automation exactly as you need it without worrying about reaching usage limits.

## Before you begin

Before you start, make sure that:

1. You have administrator privileges for your Jira instance; creating JMWE extensions requires administrator privileges.
2. You have access to the workflow to which this rule will be added.

## Create your first post function

1. 1

   Open your workflow in the Jira workflow editor.
2. 2

   Select the transition into *Testing* (1) and click **Add Rule** (2).

   ![firstExtension-AddRule.png](/cms_trial/assets/31032237-4ec7-4ce6-8a28-20d6432ebb86.png)
3. 3

   Select the **Set Issue Fields (JMWE app)** post function and click **Select**.
4. 4

   Configure the post function:

   1. 1. Click **Add** under **Fields to update**.
      2. Select the field **Assignee** then enter the Nunjucks code `{{ issue | projectInfo | field("lead.accountId") }}`*.*
      3. Click **Add**.![firstExtension-ConfigureRule.png](/cms_trial/assets/dd9c5349-371e-4bea-bd1b-df455bb9b816.png)
5. 5

   Click **Add** to save the post function. Click **Update workflow** to save your workflow.

## Success!

You now have a rule that automatically assigns a work item to your Project Lead (Space owner) when it is transitioned toa specific status! You should thoroughly test your automation by creating a work item, transitioning it to the selected status, and check the **Assignee** value. Verify that it has been correctly assigned.

---

## Examples

Want to see examples of how to implement extensions to automate your processes? Check the [Use Cases](/cms_trial/space/JMWEC/466225276/Use+cases/) for specific scenarios and their solutions using post-processes, conditions, and validators.

## Appfire Blog

[Appfire’s blog](https://appfire.com/resources/blog) is a central location for news, tutorials, and other resources for all of Appfire’s products and services, including **JMWE**!

## Get Help

See the [Knowledge Base](/cms_trial/space/JMWEC/465241585/Knowledge+Base/) for steps on solving common issues.

Check the [Troubleshooting and support](/cms_trial/space/JMWEC/465503894/Help+and+Support/) page for steps on how to resolve errors and gather information for support requests.