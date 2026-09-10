# Current task limit is set to X tasks

## Current task limit is set to X tasks (old navigation)

## Problem

- User [defined the scope for the box](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/), but cannot save it due to the following warning message:

![Task limit warning saying Current task limit is set to 10 tasks.](/cms_trial/assets/e927e57b-0992-40db-a4f4-0657329d29b7.png)

or

![Task limit warning saying task count limit exceeded.](/cms_trial/assets/9212078c-6b6d-43f6-bc19-aecc4e5af4a1.png)

## Solution

You are seeing this message because the total number of tasks you want to add to the box exceeds the maximum task limit set for that particular box.

### Solution #1: Increase the task limit

To allow the box to have more tasks in its scope, a Jira/App Admin must increase the task limit.

1. Go to the **App settings > Performance > Sync rules** page.
2. In the **Maximum number of tasks in a box** field, enter a new value. For example, 100, 600, 1250, 10700, etc.

![task-limit-app-settings-page.png](/cms_trial/assets/adca5c0f-b9b1-4306-8220-31ccc0cbf4cd.png)

1. Go back to the scope definition page and define the scope for your box.

Keep in mind that task limits are in place to control the app’s performance. The limit of ten tasks in this example is extremely low, and it is unlikely that you will ever encounter such a limitation. However, keeping tens of thousands of tasks in a single box can reduce the app’s performance.

### Solution #2: Narrow down the scope

Another way to go about the task limit is to use JQL to narrow down the scope of the tasks.

1. On the scope definition page, select the task source (using Project, Board, and/or Filter).
2. In the **Narrow down** field, enter your JQL statement.

For example, if the task count for a selected Jira Board (or Boards) is 275 and the task limit is 250, you can add only those tasks that meet specific criteria, such as those that are Tasks and were delivered on a specific date.

![A result of the jql statement. There are now 5 tasks in the scope.](/cms_trial/assets/44ec7254-73e4-4a2e-a221-018957359d8b.png)

## Current task limit is set to X tasks (new navigation)

## Problem

- User [populates box with tasks](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/), but cannot save it due to the following warning message:

![Task limit warning saying Current task limit is set to 10 tasks.](/cms_trial/assets/e927e57b-0992-40db-a4f4-0657329d29b7.png)

or

![Task limit warning saying task count limit exceeded.](/cms_trial/assets/9212078c-6b6d-43f6-bc19-aecc4e5af4a1.png)

## Solution

You are seeing this message because the total number of tasks you want to add to the box exceeds the maximum task limit set for that particular box.

### Solution #1: Increase the task limit

To allow the box to have more tasks in its scope, a Jira/App Admin must increase the task limit.

1. Go to the **App settings > Performance > Sync rules** page.
2. In the **Maximum number of tasks in a box** field, enter a new value. For example, 100, 600, 1250, 10700, etc.

![task-limit-app-settings-page.png](/cms_trial/assets/adca5c0f-b9b1-4306-8220-31ccc0cbf4cd.png)

1. Go back to the Add work items from Jira page and define the scope for your box.

Keep in mind that task limits are in place to control the app’s performance. The limit of ten tasks in this example is extremely low, and it is unlikely that you will ever encounter such a limitation. However, keeping tens of thousands of tasks in a single box can reduce the app’s performance.

### Solution #2: Narrow down the scope

Another way to address the task limit is to use JQL to narrow the scope of the tasks.

1. On the scope definition page, select the task source (using Project, Board, and/or Filter).
2. In the **Narrow down** field, enter your JQL statement.

For example, if the task count for a selected Jira Board (or Boards) is 275 and the task limit is 250, you can add only those tasks that meet specific criteria, such as those that are Tasks and were delivered on a specific date.