# Display all sub-tasks assignees

## Scenario

You require a field that displays all team members working on sub-tasks for a Story.

## Resolution

This solution uses the **Scripted User Collection** custom field type to create a field on Story issues that displays a user badge for any team member assigned to one of the Story’s sub-tasks. This field could also be modified to display all assignees to Stories related to an Epic, or expanded to display all team members working on any issue related to an Epic!

You are viewing the documentation for **Jira Cloud**.

| On This Page |
| --- |

## Follow the Steps

### 1. Create a *Scripted user collection* custom field

1. Log into your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand sidebar, click **Jira Misc Custom Fields**.
4. Click **My custom fields** and in the upper right corner click **New custom field**.
5. Enter a name for your custom field and, optionally, a description.
6. Select **Scripted user collection** and click **Next**.
7. Select the projects and issue types to which the custom field should be added. For this example, we are only going to select **Story** under **Issue types**.
8. Click **Next**.
9. Select the screens to which the new custom field should be added. Click **Next**.
10. Configure the field (Figure 1, right):

    1. In the script editor, enter the following:

       ```text
       // get child issues for the current issue
       const childIssues = await api.issue.getChildIssues(issue)
       // get relevant fields
       const childFields = await Promise.all(childIssues.map(async childIssue => 
         await api.issue.getFields(childIssue, ["issuetype",'assignee'])))

       const assignees = childFields.reduce((acc, fields) => {
         const {issuetype, assignee} = fields
         //only run for subtasks that have an assignee
         if (issuetype.subtask && assignee) {
           acc.push(assignee.accountId)
         }
         return acc
       },[])

       // remove duplicates so each user only displays once
       const final = [...new Set(assignees)]
       return final
       ```
11. Optionally, you can test the results of the script by entering an issue ID in the **Test with issue** field and clicking **Test**.
12. Click **Save**.

### Congratulations!

Open a Story issue that has sub-tasks assigned to other team members. All team members working on any part of a Story should be displayed!

![Jira Misc Custom Fields (JMCF) Cloud story team scripted field configuration](/cms_trial/assets/5ea5425d-181f-4208-b230-660201a14579.png)