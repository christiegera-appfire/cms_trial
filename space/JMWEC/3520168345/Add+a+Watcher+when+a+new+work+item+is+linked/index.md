# Add a Watcher when a new work item is linked

| **Goal** | When a new work item is linked to the item that triggers this Action, add the Assignee of the work item as a Watcher to the link target. |
| --- | --- |
| **Scenario** | You want to streamline and automate communication between teams by automatically adding the Assignee of a work item as a Watcher to the target work item of the link. For example, you have Support tickets that are linked to a Bug and want to add the owner of the Support ticket as a Watcher on the Bug work item. This automatically adds the Support team member into the chain of communication on progress reports on the associated Bug. |
| **Components** | [Event-based Action](/cms_trial/space/JMWEC/465473524/Event-based+actions/): Issue Link Added event, [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post function |
| **Baseline** | None. |

---

## Requirements

- Jira Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)

**Note**: This configuration is built using two separate Jira Spaces - one for Development and one for Support, and it uses a filter to only trigger the post function when a Support issue is linked to a Development work item. This is not a requirement!

## 1. Create the Event-based Action

1. Log into your instance as an administrator.
2. In the left-hand panel, expand **Apps** and click **Jira Misc Workflow Extensions**.
3. Click **Event-based actions** and click **Create new action** in the upper right corner.
4. Give your Event-based action a name and, optionally, a description.
5. Under **WHEN**, make sure **Select Event** is selected. In the right-hand panel, select **Issue Link Added** (**Figure 1**, right).
6. Set the other options under **WHEN** as needed.
7. Under **IF SCOPE**:

   1. For **Projects** select the appropriate Space for your configuration, or select *Any*.
   2. For **Issue Types** select the appropriate work items for your configuration, or select *Any*.
   3. Check the box for **Only apply to issues that match a Nunjucks condition**.
   4. Click the **Nunjucks** text field and enter the following (**Figure 2**, right):

      ```text
      {{ context.issueLink.sourceIssueId | issue("project") | projectInfo | field("name") | capitalize | truncate(7) === "SUPPORT..."}}
      ```
   5. Click **Save**.

### Configure the Nunjucks Script

The Nunjucks script in **Step 7**, above, filters out any linked work item that is not in a Space starting with “SUPPORT”. This ensures that only work items from a specific space will have their Assignee added as a Watcher to the work item that triggers the action. Update this filter as needed for your workflow.

![Select the Issue Link Added event for your JMWE Cloud Event-based action](/cms_trial/assets/f17946ee-0057-4c9b-87ce-a7fe864d89d1.png)![Configure a Nunjucks condition for your JMWE Cloud Event-based action](/cms_trial/assets/8284adbe-efe1-484e-ab6a-9f68a3a3f4d1.png)

## 2. Add the *Set issue fields* post function

1. Under **THEN**, click **Select Post-functions**.
2. In the right-hand panel, click **Set issue fields** in the list of post functions. The [*Set issue fields*](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) *post-function* configuration screen will open (**Figure 3**, right).
3. For **Target issues** leave the default value of *Current Issue*.
4. Under **Fields to update**, click **Add**.
5. For **Field**, select *Watchers*.
6. For **New value**, enter the following Nunjucks code:   
   `{{ context.issueLink.sourceIssueId | issue | field("assignee") }}`
7. Click **Update**.
8. Click **Save**.

![Configure the Set issue fields post function for your JMWE Cloud Event-based action](/cms_trial/assets/4586438b-610a-4066-9287-bf19a7ef008e.png)

## Save and Test the Action

In the main Event-based Action editor, click **Save** to complete the configuration. To test the new action, link an issue from the SUPPORT space (or your configured link source space) to a work item in the Development space. Verify that the Assignee of the Support work item is added as a Watcher on the Development work item.

### Congratulations!

Your Support team members will automatically be notified of changes to any Bug that is linked to their tickets!