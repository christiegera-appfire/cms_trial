# Update work item 'Start date' when it is moved to In Progress

| **Goal** | When a work item is moved to ‘In Progress,’ update its Start date to keep the Gantt chart view in [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?hosting=cloud&tab=overview) up to date and remove manual status updates. |
| --- | --- |
| **Scenario** | [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?hosting=cloud&tab=overview) is a flexible PPM tool for Jira to help you manage projects, programs, and portfolios in one place, at any scale. You want to make sure your BigPicture Gantt charts are as accurate as possible, so in an effort to guarantee complete and accurate data, you want to automatically set the Start date of your work items to the date they are transitioned to ‘In Progress’. Additionally, you want to verify that the Start date of a work item cannot be set unless the work item is in a status other than ‘To Do’, so that the date cannot be set before work begins, but it can be reset manually if needed. |
| **Components** | [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post function; BigPicture [Gantt](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918701893) chart |
| **Baseline** | - Transitioning an issue to ‘In Progress’ will always set the Start date field, overwriting any existing value. |

---

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)
- [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-portfolio-resource-management-for-jira?hosting=cloud&tab=overview) or [BigPicture Enterprise](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise-strategic-management-for-jira?hosting=cloud&tab=overview)
- The date field that is updated by JMWE must be the date field that is configured in BigPicture field mappings as the start date of work items.

## 1. Add the *Set issue fields* post function

In this step, you will add a post function to the transition that points to your **In Progress** status. If you have multiple transitions leading to **In Progress**, you should repeat these steps for each transition.

1. Log in to your Jira instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner and select **Work items**.
3. In the left-hand panel, click **Workflows**.
4. From the list of workflows, click the **Action** button for the workflow you want to edit and select **Edit**.
5. Edit the Transition:

   1. When viewing the Workflow in **Diagram** view, select the Transition and click the **Post Functions** link. Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition, then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.

c. Select **Set issue fields** from the list of post functions and click **Add**.

![JMWE for Jira Cloud transition selection interface for start date updates](/cms_trial/assets/0ca04619-9d7c-43db-a143-9f041380cea1.png)

## 2. Configure the post function

**Note**: Following the configuration below will set the **Start date** field for any work item that is transitioned. If you want to limit this behavior to a specific type of work item, use the [Conditional execution](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) option.

In the post function configuration screen, set the following:

1. **Issue(s) to operate on** - Set **Target issues** to *Current issue*.
2. **Fields to update**

   1. Click **Add**.
   2. Set **Field** to *Start date*.
   3. For **New value**, enter the following:

      ```text
      {{ now }}
      ```
   4. Click **Add** at the bottom of the panel.
3. Click **Add** at the bottom of the screen.

![JMWE for Jira Cloud set issue fields configuration for updating work item dates](/cms_trial/assets/fceb5c22-2038-4e78-bb14-9763faf6f374.png)

## 3. Verify BigPicture configurations

No specific configurations or changes are needed in BigPicture; you must only verify that the start date field JMWE updates is also configured as the work item start date in your BigPicture field mappings.

1. Verify that you have adequate permissions to view or modify BigPicture field mappings.
2. Open the BigPicture configuration for the appropriate project.
3. Navigate to **General** > **Fields** to view or edit the BigPicture field mappings for your project.

See [BigPicture Fields](https://appfire.atlassian.net/wiki/spaces/DLP/pages/2212268582) for more information.

## Publish and test your workflow

The last step is to publish your updated workflow and then test the new version to verify that the new extensions have been configured correctly. To test the extensions, you’ll need to trigger the same transition to which they were added and verify the results.

**Note**: It is generally recommended to perform testing in a non-production environment. After testing is complete, you can **migrate your workflow** to your Production environment; see this page for steps on exporting and importing your workflow: <https://support.atlassian.com/jira-cloud-administration/docs/import-and-export-issue-workflows/>.

### Congratulations!

The Start dates for your work items will now be updated automatically, keeping your Gantt chart current and accurate!