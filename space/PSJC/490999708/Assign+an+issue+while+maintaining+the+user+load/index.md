# Assign an issue while maintaining the user load

## Problem

You want to assign new issues to the user with the least number of tasks to balance the workload across the team.

## Solution

This recipe assumes that you already have a project and a workflow associated with it in your Jira installation. If not, go to the [Jira documentation](http://confluence.atlassian.com/display/JIRA043/Activating+Workflow) to find out how to do this.

## Add a SIL action

1. Create a draft workflow.
2. Go to the **Create** transition.
3. On the **Post Functions** tab, select the **Add** checkbox.
4. Select **(k) SIL Action** and click **Add**.

![Power Scripts for Jira Cloud user assignment load balancing script results](/cms_trial/assets/804c490a-226b-4bda-ad83-32e7ec68a6e3.PNG)

For more information on configuring workflows, go to the [Atlassian documentation](http://confluence.atlassian.com/display/JIRA043/Configuring+Workflow).

## Write the code

After you’ve added the action, the user interface is displayed.

Enter a name for your program. This is used in the name of the file where the program is saved. For more examples, go to our documentation on [writing condition validators and actions](/cms_trial/space/PSJC/490999217/Writing+Actions+(Post-Functions)/).

To assign an issue while also maintaining the user load, enter the following code.

```text
string[] prjMembers = projectMembers(project);
string minUser;
number minIssues = -1;
number issuesNumber = -1;
string query = "project = " + project + " AND status in ('Open', 'In Progress', 'Reopened') AND assignee = ";
string jql;
 
for (string user in prjMembers) {
  jql = query + user;
  issuesNumber = arraySize(selectIssues(jql));
  if ((minIssues == -1) || (issuesNumber < minIssues)) {
    minIssues = issuesNumber;
    minUser = user;
  }
}
 
assignee = minUser;
```

Click **Add**.

![Power Scripts for Jira Cloud assignee load distribution settings](/cms_trial/assets/6989de6e-c3c5-4d21-a513-39c3674df881.png)

It is recommended that you move the SIL™ actions after all other actions. To do this, click **Move Down** until the SIL™ actions reach the bottom of the actions list.

## Test the code

Publish your draft workflow to activate it.

To test the action, create a new issue. Complete the required fields and click **Create**. The issue is assigned to the user with the smallest number of tasks.

## Example

This is an example of how you can randomly assign an issue to project users.

To assign the issue randomly, enter the following code and make sure to use the **random** function.

```text
string[] prjMembers = projectMembers(project);
number n = arraySize(prjMembers);
 
if (n > 0) {
 assignee = arrayGetElement(prjMembers, random(n));
} else {
 assignee = projectPM(project);
}
```