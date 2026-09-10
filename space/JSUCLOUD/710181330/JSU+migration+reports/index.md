# JSU migration reports

With JSU Migration reports, Jira admins can identify and resolve issues that arise during the migration of JSU space workflows and data to Jira Cloud.

## What reports are available?

JSU Migration reports are available for migrations performed with Jira Cloud Migration Assistant (JCMA) and Appfire’s Configuration Manager Cloud Migration Tool.

## Report features

- Total number of rules displayed in the summary.
- Details of missing references: ID/name and description of:

  - Custom field
  - Space
  - Work item type
  - Status
  - Resolution
- Columns for *Rule Name*, *Workflow*, and *Transition* with corresponding links to the workflow or rule summary in your Jira instance.
- A checkbox in the *Resolved* column lets you keep track of which issues you have resolved in the Cloud instance.
- Sortable columns to help you organize the issues in a way that suits you best.

## How can I view a report?

If you use the Jira Cloud Migration Assistant (JCMA) or Appfire’s Configuration Manager Tool, you can view the report immediately after migration by clicking the link in the corresponding app. Your reports are also available directly from JSU’s *Migration* page.

**To open a Migration report in JSU:**

1. In the top bar in Jira, select **Apps** > **JSU Automation Suite for Jira Workflows**.
2. In the JSU global navigation bar, select **Reporting** > **Migration**.
3. Select **View Report** for the required migration.

   ![Screenshot of the JSU Migration report page with the View Report button highlighted in red.](/cms_trial/assets/11c0ce49-df99-4b2b-8627-65497f324148.jpg)

   The report summary displays.

   ![Screenshot of sample JSU migration report.](/cms_trial/assets/6b03142a-b774-4837-8a5a-930197496245.png)
4. To view details for missing references, hover over the individual rule line.

   ![Screenshot of missing reference details in a JSU migration report.](/cms_trial/assets/0e40b836-655e-48bf-8864-bbbb326b1f86.png)

The example report below illustrates three instances of missing data from the migration. The Jira admin used this information to resolve the issue that resulted in the missing custom field.

![Screenshot of a sample migration report as described on this page.](/cms_trial/assets/7f7fc31c-6fd4-4220-b6ce-96d71dab58b5.png)

## Related pages

- [Migrating with the Jira Cloud Migration Assistant (JCMA)](/cms_trial/space/JSUCLOUD/12517840/Migrating+with+the+Jira+Cloud+Migration+Assistant+(JCMA)/)Our guide to using JCMA to migrate JSU Data Center data to JSU Cloud uses a sample migration to show you how to use our *original* beta migration report.
- <https://appfire.atlassian.net/wiki/spaces/JSU/pages/684064819>: JSU is now supported in Data Center to Cloud migrations through the Configuration Manager Cloud Migration Tool.