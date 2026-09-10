# Calculate 'End Date' based on Story points

| **Goal** | When a work item’s Story Points field is updated, calculate the Estimated end date field to keep the Gantt chart view in [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?hosting=cloud&tab=overview) up to date and automate the planning process during estimation. |
| --- | --- |
| **Scenario** | [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?hosting=cloud&tab=overview) is a flexible PPM tool for Jira to help you manage projects, programs, and portfolios in one place, at any scale. You want to make sure your BigPicture Gantt charts are as accurate as possible, so in an effort to provide the most accurate timeline during planning and estimation, you want to automatically set the BigPicture field ‘End date’. |
| **Components** | [Event-based action](/cms_trial/space/JMWEC/465473524/Event-based+actions/): Issue Field Value Changed; [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post function; BigPicture [Gantt](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918701893) chart |
| **Baseline** | - Story points are the method of estimation used. - In the base configuration, the field ‘End date’ will be updated for any work item with Story Points assigned. **End date** is a field added by BigPicture and is the default end date field set for work items in the field mapping. |

---

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)
- [BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-portfolio-resource-management-for-jira?hosting=cloud&tab=overview) or [BigPicture Enterprise](https://marketplace.atlassian.com/apps/1215158/bigpicture-enterprise-strategic-management-for-jira?hosting=cloud&tab=overview)
- The date field that is updated by JMWE must be the date field that is configured in BigPicture field mappings as the End date of work items.

## 1. Create the Event-based Action

1. Log into your instance as an administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Apps**.
4. In the left-hand panel under *JIRA MISC WORKFLOW EXTENSIONS,* click **Event-based actions** and click **Create new action** in the upper right corner.
5. Give your Event-based action a name and, optionally, a description.
6. Under **WHEN**, make sure **Select Event** is selected. In the right-hand panel, select **Issue Field Value Changed** (**Figure 1**, pictured right).
7. Under **Fields to monitor**, select **Story Points** and click **Save**.
8. Under **IF SCOPE**, set **Projects** and **Issue Types** as needed. Filter issues as necessary.

### Calculating the end date

The Set issue fields post function will set the field **End date** using a basic calculation; this calculation uses 1 work day for each Story point. You should adapt this calculation as needed for your team!

![JMWE for Jira Cloud eventbased action setup for calculating end dates from story points](/cms_trial/assets/8e8974c9-bbb6-416b-a31f-50380b3f85cc.png)

## 2. Add the *Set issue fields* post function

The Nunjucks script below references two Jira fields - **Start date** and **Story points** - to calculate the new value for **End date**. The script contains field reference examples taken from one Jira instance (`customfield_10015` and `customfield_10036`). You must replace these field IDs with the IDs specific to your instance!

1. Under **THEN**, click **Select Post-functions**.
2. In the right-hand panel, click **Set issue fields** in the list of post functions. The [*Set issue fields*](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) configuration screen will open.
3. For **Target issues** leave the default value of *Current Issue*.
4. Under **Fields to update** click **Add**.
5. Set **Field** to the custom field **Estimated end date**.
6. For **New value**, enter the following Nunjucks code, where `customfield_10015` is the **Start date** and `customfield_10036` is **Story points**:

   ```text
   {% if issue.fields.customfield_10015 != null %}
   	{{ issue.fields.customfield_10015 | date('add', issue.fields.customfield_10036 , 'days') | date }}
   {% endif %}
   ```

   1. [note icon] To determine the field IDs for your instance, use the Nunjucks Help tools located below the editor. Click **Issue Fields** to open the Help panel and search for **Start date** and **Story points**. See [Issue Fields in Nunjucks Templates](/cms_trial/space/JMWEC/465504298/Issue+Fields+in+Nunjucks+Templates/) for more information.
7. Click **Add**.
8. Configure the remaining options as needed.
9. Click **Save**.
10. In the main Event-based Action editor, click **Save** to complete the configuration.

![JMWE for Jira Cloud post function configuration for end date calculation based on story points](/cms_trial/assets/d6e70343-c3b2-40dd-8dab-44f31d2eea77.png)

## 3. Verify BigPicture configurations

No specific configurations or changes are needed in BigPicture; you must only verify that the end date field JMWE updates is also configured as the work item end date in your BigPicture field mappings.

1. Verify that you have adequate permissions to view or modify BigPicture field mappings.
2. Open the BigPicture configuration for the appropriate project.
3. Navigate to **General** > **Fields** to view or edit the BigPicture field mappings for your project.

See [BigPicture Fields](https://appfire.atlassian.net/wiki/spaces/DLP/pages/2212268582) for more information.

## Test the Action

To test the new action, update the **Story points** field for a work item that has a **Start date** value, but does not have any points assigned. Verify that JMWE updates the **End date** according to the calculation you entered in the post function.

**Note**: It is generally recommended to perform testing in a non-production environment. After testing is complete, you can **migrate your workflow** to your Production environment; see this page for steps on exporting and importing your workflow: <https://support.atlassian.com/jira-cloud-administration/docs/import-and-export-issue-workflows/>.

### Congratulations!

Your work items will now automatically update when **Story points** are set or updated! The end date will be adjusted for all work items, helping keep your Gantt chart current and accurate!