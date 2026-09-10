# JQL use cases

---

We built integrated JQL in many of our [workflow post functions](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/), allowing Jira administrators to set wider parameters that can be fully customized.

Below, you will find a few examples demonstrating how flexible and powerful JQL can be when used with JSU. Refer to the [JQL reference](/cms_trial/space/JSUCLOUD/12518329/JQL+reference/) for details on how to use JQL with JSU.

## JQL in post functions

In several JSU post functions, you can specify a JQL query to retrieve the issues to be modified by the post function. See also [Related Issues](/cms_trial/space/JSUCLOUD/12518756/Related+issues/).

### Use Case 1: Update the Description of particular sibling issues

- **Post function**: Update Any Issue Field
- **Transition**: `Resolve` in our *Testing Subtask* workflow

![Screenshot of the Update Any Issue Field configuration as described on this page.](/cms_trial/assets/b831daac-a8c2-4a3c-a075-869475c70962.png)

### Use case 2: Copy fields from a template issue

- **Post function**: Copy Value from Other Field

We are using issue XY-23 as a template. Only Jira admins can view this issue. It has pre-configured values for several fields.

![Screenshot of an example JQL query for issue key.](/cms_trial/assets/a5165cbb-bcca-4b95-b011-e085754ae0d6.png)

### Use Case 3: Change the status of critical issues in an Epic

**Post function**: Linked Transition

If an epic has critical and blocker issues that are still in the open state, change it to in progress.

![Screenshot of the Linked Transition post function configured with a JQL query. Returned issues will be moved to In Progress.](/cms_trial/assets/d062225a-16df-4541-bf33-5a3e870761ca.png)