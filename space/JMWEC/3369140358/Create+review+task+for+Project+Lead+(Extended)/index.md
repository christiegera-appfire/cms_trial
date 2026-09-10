# Create review task for Project Lead (Extended)

| **Goal** | Create a review task automatically for specific types of work items **whenever an item is edited**. |
| --- | --- |
| **Scenario** | Building on an [earlier use case](/cms_trial/space/JMWEC/1486291002/Create+review+task+for+Project+Lead/), update the process for large development work items to automatically create a Task for the Project Lead to review the work item for completeness. Additionally, require that the **Approved by Lead** field be checked to transition the item to **In Progress**.  This extended version updates the [earlier use case](/cms_trial/space/JMWEC/1486291002/Create+review+task+for+Project+Lead/) to automate the process whenever the work item is edited, not just when it is created. |
| **Components** | [Shared action](/cms_trial/space/JMWEC/466288975/Shared+actions/) that includes the [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post function; [Field Required](/cms_trial/space/JMWEC/465242701/Field+Required+Validator/) validator.  [Event-based action](/cms_trial/space/JMWEC/465473524/Event-based+actions/) to trigger the automation when a work item is edited. |
| **Baseline** | - The post functions are configured in a **Shared action**. - The Shared action is added to the workflow to trigger the automation when a large Epic is created; the same Shared action is added to an Event-based action to trigger the automation when an Epic is edited. - A custom field exists or is created to designate approval status (e.g. **Approved by Lead**). - Your project has a member assigned to the **Project Lead** role. For more information on Project Leads, see the **Change the project lead** section of <https://support.atlassian.com/jira-software-cloud/docs/edit-a-projects-details/> |

The steps below demonstrate how to build a simple approval process for larger work items in the form of Epics. However, you could add this process to other work item types, including Stories and, for example, limit the required approval to only Stories with a certain number of sub-tasks (or whatever your team uses as a threshold for determining work items requiring a large effort).

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)

## 1. Custom field for Project Lead approval

Verify that your Jira instance has a custom field that can be used to designate that the Project Lead has approved the work item for development. If a field does not exist, create one and add it to the appropriate screens. For more information, see <https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/>.

## 2. Build the Shared action

1. Log in to your Jira instance as an Administrator.
2. In the left-hand sidebar, click **Jira Misc Workflow Extensions**.
3. Click **Shared actions**.
4. In the list of Shared actions, click **Create new action**.
5. Give your new Shared action a name and, optionally, a description.
6. Select **Create issue(s)** from the list of post functions (**Point 1**, **Figure 1**, right).
7. Continue the post function configuration in the next section, below.

![JMWE for Jira Cloud Shared action configuration](/cms_trial/assets/331ba471-1abb-4aea-91a7-209aad9fdc70.png)

## 3. Configure the *Create issue(s)* post function

Leave all fields at their default values unless specified below.

1. For **Issue type**,select *Task* (**Point 1**, **Figure 2**, right).
2. For **Link type**, select *is child of* (**Point 2**, **Figure 2**, right).
3. For **New value**, enter the following script (**Point 3**, **Figure 2**, right):

   ```text
   Project Lead Review - {{ issue.fields.issuekey }}
   ```
4. Click **Advanced options**, then **Settings**.
5. Check the box for **Run this post-function only if a condition is verified**.
6. In the **Write a script** editor, enter the following script (**Point 4**, **Figure 2**, right):

   ```text
   {{ issue.fields.issuetype.name == "Epic" }}
   ```
7. Click **Add** (**Point 5**, **Figure 2**, right).
8. In the Shared action editor, click **Save**.

### Alternate Configuration

The standard configuration, above, runs for all Epics no matter how big. Your workflow may have different thresholds for when a work items requires review, or different ways of designating these types of items. For example, instead of triggering this post function only when an Epic is created you may want to trigger it when any work item with 5 or more [Story Points](https://support.atlassian.com/jira-software-cloud/docs/what-are-story-points/) is created.

To do this, replace the script in Step 5 above with the following:

```text
{{ issue.fields.<your field id> >= 5 }}
```

Additionally, you could expand the requirements for the post function so that it only runs for work items that are Epics AND Epics that have 8 or more Story Points (as opposed to Stories that have 5 or more Story Points):

```text
{% if issue.fields.issuetype.name == "Epic" 
  and issue.fields.<your field id> >= 8 %}
true
{% else %}
false
{% endif %}
```

You **MUST** update the `<your field id>` placeholder in the scripts above with the field ID of the custom field you use to measure work effort. To do this:

1. Click the **Issue Fields** help tab along the bottom of the script editor.
2. Select *Story Points* (or the appropriate field) from the **Select a field** pulldown menu.
3. Take note of the custom field ID displayed in the examples below the pulldown. For example, the field ID is displayed as `issue.fields.customfield_10036`.
4. Enter your custom field ID in the script, replacing `<your field id>`.

For more information on using Story Points, see <https://support.atlassian.com/jira-software-cloud/docs/estimate-an-issue/>.

![JMWE for Jira Cloud Create issue post function configuration](/cms_trial/assets/476d6d0b-50ba-4f31-a4a6-1a406fca3e3f.png)

## 4. Create the Event-based action

After you have built the Shared action, you need to add it to both your Workflow and to an Event-based action that triggers when an Epic is edited. This will cover two scenarios - when a large work item is **created** and when an existing work item is updated to be bigger than your threshold requiring a Project Lead review. First, create the Event-based action:

1. In the left-hand sidebar, click **Event-based actions** under *Jira Misc Workflow Extensions*.
2. In the list of Event-based actions, click **Create new action**.
3. For **WHEN**, select **Issue Updated** in the right-hand panel.
4. Optionally, select **Projects** on the left, search for and add specific projects in the right-hand panel. If you don’t add any projects, the action will run for all projects.
5. Select **Issue Types** on the left and click **Select Issue types** in the right-hand panel.
6. Check the box for **Epic** and click **Add**.
7. Click **Select Post-functions** on the left and select **Shared Action** in the right-hand panel (**Point 1**, **Figure 3**, right).
8. Leave **Target issues** as the default and, optionally, give your Shared action a **Description**.
9. Under **Shared Action**, select the Shared action you created above.
10. Click **Save**.

You do not need to add conditional execution to the Shared action post function, because the **Create issue(s)** post function contained in the Shared action runs conditionally. The Shared action will trigger for every Epic that is updated, but the Create issue post function will only run for Epics that match your conditional execution requirements.

![JMWE for Jira Cloud Event-based action configuration screen](/cms_trial/assets/a7e9f1b1-b52b-4f0e-adb4-0890afc1804a.png)

## 5. Update your workflow

1. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Work items**.
2. In the left-hand sidebar, click **Workflows**.
3. From the list of Workflows, click **Actions** for the appropriate workflow and select **Edit**.
4. Select the Create transition (**Point 1**, **Figure 1**, right).
5. Click the **Add** button for **Perform actions** (**Point 2**, **Figure 1**, right).
6. Select *Shared Action (JMWE app)* from the list of post functions and click **Select** at the bottom of the list.

Leave all fields at their default values unless specified below!

1. Optionally, give your Shared action post function a **Description**.
2. Under **Shared Action**, select the Shared action you created above.
3. Click **Add**.
4. Save your workflow.

You do not need to add conditional execution to the Shared action post function, because the **Create issue(s)** post function contained in the Shared action runs conditionally. The Shared action will trigger for every item created, but the Create issue post function will only run for Epics.

![Add the JMWE Cloud Shared action post function](/cms_trial/assets/53fff3a1-156e-455e-8ea4-b76a69854597.png)

## 6. Add the *Field Required* validator

You must use the JMWE version of the **Field Required** validator so that the validator is only applied to Epics!

To complete your setup, we need to add the Field Required validator to the transition into **In Progress** to guarantee that large work items (Epics) have the custom field **Approved by Lead** checked before allowing the transition to complete.

This validator will only be applied to Epics.

1. In your Workflow Editor, select the transition into **In Progress**.
2. Click the **Add** button for **Validate details**.
3. Select *Field Required Validator (JMWE app)* and click **Select** at the bottom of the list.
4. For **Field(s)**, select *Approved by Lead* (**Point 1**, **Figure 3**, right).
5. Enter an error message as needed (e.g. “'Approved by Lead' is required for large items.”).
6. Under **Validator Scope**, check the box for **Conditional validation** (**Point 2**, **Figure 3**, right).
7. Enter the following script in **Conditional validation expression** (**Point 3**, **Figure 3**, right):

   ```text
   !!issue.issueType && issue.issueType.name == "Epic"
   ```
8. Click **Add** (**Point 4**, **Figure 3**, right).

### Alternate configuration

Similar to Section 3 above, the standard configuration of this validator runs for all Epics no matter how big. You could expand the requirements for the validator so that it only runs for work items that are Epics AND Epics that have 8 or more Story Points similar to the expanded condition above:

```text
!!issue.issueType && issue.issueType.name == "Epic" 
&& issue.<your field id> >= 8
```

You **MUST** update the `<your field id>` placeholder in the scripts above with the field ID of the custom field you use to measure work effort. Follow the steps above to identify the ID of your custom field.

## Save and Test the Workflow

Save your Workflow and publish the changes. To test that the post function is configured correctly, create a new Epic work item and verify that the “Project Lead Review” sub-task was created correctly. Second, verify that the **In Progress** transition displays an error message when the **Approved by Lead** field is left unchecked.

### 🎉 Congratulations

Larger development work items will now be guaranteed a review by the Project Lead, and will not be able to start until the Project Lead has approved them!

![Field Required validator configured to require the Approved by Lead field for Epic work items.](/cms_trial/assets/0a844388-a94d-4b6c-b5e9-428b5a744cf4.png)