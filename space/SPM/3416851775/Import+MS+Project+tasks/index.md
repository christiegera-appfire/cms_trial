# Import MS Project tasks

You can import Microsoft Project tasks into BigPicture and decide how they should be handled during import. Depending on your workflow, you can:

- Convert imported tasks to Jira work items (parents will be converted to default work item types).
- Convert imported tasks to Jira work items (parents will be converted to epics).
- Convert imported tasks to [BigPicture tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/).

BigPicture tasks are stored only in BigPicture and are not synchronized with Jira. This option gives you a safe workspace to review and refine imported tasks, and [convert them to Jira work items](/cms_trial/space/SPM/1918863006/Convert+basic+task+to+Jira+work+item+%2F+Convert+BigPicture+task+to+Jira+work+item/) when you’re ready.

![A gif of the Import from file screen in BigPicture.](/cms_trial/assets/cbb75dd1-7bcf-48d8-9434-8db4e2fa40e7.gif)

## Preconditions

Before importing tasks from a Microsoft Project file into BigPicture, make sure that:

- The [**Import from file**](/cms_trial/space/SPM/1918800781/Import+from+file/) feature is available (requires [BigTemplate](https://marketplace.atlassian.com/apps/1215229/bigtemplate-export-to-pdf-word-excel)).
- You have the necessary permissions:

  - Box admins and Jira admins can import tasks from a file.
  - If the [Permissions for everyone](/cms_trial/space/SPM/1918535770/App-level+permissions/) option is enabled, every logged-in user can import tasks from a file.

## Import data from MS Project

Once you import a file from MS Project, all columns with data will be automatically detected.

Check a list of supported fields in the *Supported fields* section below.

To import tasks:

1. Expand the **Tasks** menu.
2. Select **Import from file**.

   ![Screenshot of the Import from file option.](/cms_trial/assets/72f27ce2-cbc9-4fea-90d9-e4a70bef3dd9.png)
3. Upload a file.
4. Select how the tasks should be converted:

   1. Jira work items (parents will be converted to default work item types)
   2. Jira work items (parents will be converted to epics)
   3. BigPicture tasks
5. Select the Jira space where the work items will be created. For more info, see the *Select Jira space* section below.
6. Add Jira labels to identify imported tasks.
7. Enable **Add labels as an additional filter for the box scope** if you want the entered labels to be added as filters on the [Work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page.
8. Decide whether the [ASAP mode](/cms_trial/space/SPM/1918865340/Strong+dependencies+(App+configuration)/) for dependencies should be on or off.
9. When ready, click **Import**.

   ![Screenshot of importing a Microsoft Project file with tasks in the Gantt module.](/cms_trial/assets/b1c045ba-380e-4f89-9937-ae59a9a68c53.png)

Note that sub-tasks will be imported as default work item types.

To see a real example, watch the video below.