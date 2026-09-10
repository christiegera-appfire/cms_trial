# Automatically create sub-tasks on 'Development' issues

| **Goal** | Automatically create sub-tasks for new Development issues. |
| --- | --- |
| **Scenario** | You want to automatically create sub-tasks for specific non-Developer teams to ensure that new or updated features are reviewed by teams that are downstream of primary development. |
| **Components** | [Event-based Action](/cms_trial/space/JMWEC/465473524/Event-based+actions/): Issue created event, [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post function, [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post function |
| **Baseline** | - “Development issues” are for your development team only and are limited to the issue types **Story** and **Tasks**. - Issue types such as Epics (e.g. for Product/Project Management) and Bugs (for QA) will not trigger this event. - The post functions are configured to create **sub-tasks** on Stories and Tasks. |

In these scenarios, some examples of useful related issues or sub-tasks are:

- QA issues for testing and verification
- Documentation tasks
- “Review” tasks for Support teams, Marketing, or Project Management

### Alternate Configurations

Your workflows may use different organization, or you may want to use different methods of designating Development issues.

Be sure to review the **Alternate Configuration** callouts below for suggestions on how to modify this configuration for your specific circumstances!

---

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)
- The issue types **Story** and **Tasks** are reserved for development use only

## 1. Create the Event-based Action

1. Log into your instance as an administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Apps**.
4. In the left-hand panel under *JIRA MISC WORKFLOW EXTENSIONS,* click **Event-based actions** and click **Create new action** in the upper right corner.
5. Give your Event-based action a name and, optionally, a description.
6. Under **WHEN**, make sure **Select Event** is selected. In the right-hand panel, select **Issue Created** (**Figure 1**, right).
7. Set the other options under **WHEN** as needed.
8. Under **IF SCOPE**:

   1. Leave **Projects** set to Any.
   2. Click **Issue Types**.
   3. In the upper-right corner of the right panel, click **Select Issue types**.
   4. Check the boxes for **Story** and **Task** (**Point 1**, **Figure 2**, right).
   5. Click **Add** (**Point 2**, **Figure 2**, right).

### Alternate Configuration

- You may use Stories and Tasks for additional teams, so you don’t want to create related issues/sub-tasks for every Story and Task   
    
  <use custom issue types, labels to designate Development issues, or check User/Team assignment>

![Event-based Action select event configuration](/cms_trial/assets/2839735e-89ec-4e2f-ac49-b7265380c517.png)![Event-based action select issue type configuration](/cms_trial/assets/7c20cca6-981c-4a11-ae53-b5a8e0272851.png)

## 2. Add the *Create issue(s)* post function

In the first post function we will create two sub-tasks - one for the QA Team and one for Documentation.

1. Under **THEN**, click **Select Post-functions**.
2. In the right-hand panel, click **Create issue(s)** in the list of post functions. The [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) configuration screen will open.
3. Leave **Project** as *Same as current issue*.
4. For **Issue type** select *Sub-task* (**Point 1**, **Figure 3**, right).
5. Leave **Parent issue** and **Link type** as the default values.
6. For **Summary** select *Custom value from script*.
7. Under **New value** enter the following script (**Point 2**, **Figure 3**, right):   
   `{{it}} for {{issue.fields.issuekey}} - {{issue.fields.summary}}`
8. Expand the **Advanced options** section, then expand **Actions after issue creation**.
9. Check **Create multiple issues**.
10. Under **Iterator**, enter the following (**Point 3**, **Figure 3**, right) to create 2 sub-tasks (one for each value in the comma-separated list):   
    `QA - Testing, Documentation - Updates`
11. Click **Save** to save your post function configuration.

### Alternate Configuration

- You may want to automatically create related issues for other issue types <expand the types of issues included in the EBA>
- You may want to **always** create some related issues/sub-tasks, but only **conditionally** create others <use labels to designate issues requiring QA or documentation, and check for those labels in Conditional Execution of the PFs>

Check labels for conditional sub-tasks (Nunjucks in the Iterator option)

![Create issues post function configuration](/cms_trial/assets/b864ab6d-225a-407c-a919-4d8679446c5c.png)

## 3. Add the *Set issue fields* post function

While the **Create issue(s)** post function enables you to copy values from the source issue to the newly created issues, it does not enable you to explicitly set field values for the new issues. To do this, we need to use the **Set issue fields** post function and pass the ID values for the newly created sub-tasks to the post function so that it can set values as needed.

1. Under **THEN**, click **Select Post-functions** if it is not already selected.
2. Click **Add Post-function** in the upper-right corner of the right hand panel.
3. Select **Set issue fields** and click **Add**. The Set issue fields configuration screen will open.
4. We need to use Nunjucks to access the IDs of the issues created in Section 2, above. For **Target issues** select *Issues returned by the following Nunjucks template*.
5. In the script editor (**Point 1**, **Figure 4**, right), enter:   
   `{{ context.newIssueKeys }}`
6. Under **Fields to update**, click **Add**.
7. In the panel for the new field, select *Description* under **Field**.
8. Under **New value** (**Point 2**, **Figure 4**, right), enter the following:

   ```text
   This is a sub-task for issue {{ issue.fields.issuekey }}. 

   Please review the main issue before proceeding.
   ```
9. Click **Add** in the field configuration panel (**Point 3**, **Figure 4**, right).
10. Click **Save** (**Point 4**, **Figure 4**, right).

### Alternate Configurations

<if creating Stories under epics, it may be possible to assign the Story to a Team?>

## Save and Test the Action

In the main Event-based Action editor, click **Save** to complete the configuration. To test the new action, create a new Story or Task and verify that JMWE has created two sub-tasks and has automatically set the correct Summary and Description values.

### Congratulations!

You now have a surefire way to create and assign tasks to your necessary support teams.

Combine this use case with the [Linked Issue Status Validator](/cms_trial/space/JMWEC/465504708/Linked+Issues+Status+Validator/) and you can guarantee that issues cannot be closed until all child issues (or sub-tasks) are closed!

![Set issue fields post function configuration](/cms_trial/assets/58932cd5-1095-4ef9-a29c-e3b1cb937ade.png)