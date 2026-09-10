# Create review task for Project Lead

| **Goal** | Create a review task automatically for specific types of work items. |
| --- | --- |
| **Scenario** | For large development items - in this scenario, work items that are Epics - automatically create a Task for the Project Lead to review the issue for completeness. Additionally, require that the **Approved by Lead** field is checked to transition the issue to **In Progress**. |
| **Components** | [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post function, [Field Required](/cms_trial/space/JMWEC/465242701/Field+Required+Validator/) validator |
| **Baseline** | - The post function is configured on the **Create** transition and will only be triggered for Epics. - A custom field exists or is created to designate approval status (e.g. **Approved by Lead**). - Your project has a member assigned to the **Project Lead** role. For more information on Project Leads, see the **Change the project lead** section of <https://support.atlassian.com/jira-software-cloud/docs/edit-a-projects-details/> |

**Note**: the steps below demonstrate how to build a simple approval process for larger items in the form of Epics. However, you could add this process to other work item types, including Stories and, for example, limit the required approval to only Stories with a certain number of sub-tasks (or whatever your team uses as a threshold for determining work items requiring a large effort).

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)

## 1. Custom field for Project Lead approval

Verify that your Jira instance has a custom field that can be used to designate that the Project Lead has approved the work item for development. If a field does not exist, create one and add it to the appropriate screens; see this page for more information: <https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/>.

## 2. Add the *Create issue(s)* post function

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** and select **Work items**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click **Actions** for the appropriate workflow and select **Edit**.
5. Select the Create transition (**Point 1**, **Figure 1**, right).
6. Click the **Add** button for **Perform actions** (**Point 2**, **Figure 1**, right).
7. Select *Create issue(s) (JMWE app)* from the list of post functions and click **Select** at the bottom of the list.

![Add JMWE Cloud post function to Create transition](/cms_trial/assets/a25353fb-f4dd-4475-9743-ac4794790643.png)

## 3. Configure the post function

**Note**: Leave all fields to their default values unless specified below!

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

![JMWE for Jira Cloud Create issue post function configuration](/cms_trial/assets/b81c4c24-29ec-4478-8169-f52b0aea3260.png)

## 4. Add the *Field Required* validator

You must use the JMWE version of the **Field Required** validator so that the validator is only applied to Epics!

Lastly, we need to add the Field Required validator to the transition between **Ready for Work** and **In Progress** to guarantee that large items (Epics) have the custom field **Approved by Lead** checked before allowing the transition to complete.

**Note:** this validator will only be applied to Epics!

1. In the Workflow Editor, select the transition into **In Progress**.
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

### Alternate Configuration

Similar to the post function above, the standard configuration runs for all Epics no matter how big. You could expand the requirements for the validator so that it only runs for work items that are Epics AND Epics that have 8 or more Story Points similar to the expanded condition above:

```text
!!issue.issueType && issue.issueType.name == "Epic" 
&& issue.<your field id> >= 8
```

You **MUST** update the `<your field id>` placeholder in the scripts above with the field ID of the custom field you use to measure work effort. Follow the steps above to identify the ID of your custom field.

## Save and Test the Workflow

Save your Workflow to apply the changes. To test that the post function is configured correctly, create a new Epic work item and verify that the “Project Lead Review” Task was created correctly. Second, verify that the **In Progress** transition displays an error message when the **Approved by Lead** field is left unchecked.

### 🎉 Congratulations!

Larger development items will now be guaranteed a review by the Project Lead, and will not be able to start until the Project Lead has approved them!

![reviewTask-FieldRequired.png](/cms_trial/assets/6acc9757-9e2a-4a96-b163-1702b294d4bf.png)