# Error Logs

**Note**: Version 2.0 of JMCF for Jira Cloud includes the release of [Scripted Fields](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/713588743). *This feature is currently in* ***limited release***.

Full availability of Scripted Fields will occur in a future release.

The **Error logs** page (Figure 1, right) displays a paginated list of any errors that have occurred with **JMCF for Jira Cloud** custom fields. Potential errors could include:

- An outage in Jira or Forge that causes JMCF calculations or display values to unexpectedly fail
- A misconfigured custom field (e.g. a scripted custom field with a scripting error) that causes JMCF calculation errors
- A bug in the JMCF application that may cause errors during configuration, calculation/re-calculation, or display of a custom field

**Please note**: Currently, Atlassian storage constraints limit the retention of error logs to **100 logs per day for seven days only**.

The error console data on the nature of the error and provides tools for acknowledging and deleting error logs. The page includes four primary sections:

- **Page Toolbar** - The upper right corner of the page includes a menu with several commands:

  - **Documentation** - Open the JMCF for Jira Cloud documentation.
  - **Support request** - Open the Appfire Support portal to submit a support request.
  - **Feedback** - Open the Appfire Support portal to submit an enhancement or feature request.
  - **Atlassian Community** - Open the [Atlassian Community page for JMCF](https://community.atlassian.com/t5/tag/addon-com.innovalog.jmcf.jira-misc-custom-fields/tg-p/category-id/atlassian-marketplace).
- **Acknowledged** - Show or hide Acknowledged error logs.
- **Actions** - Bulk actions to acknowledge all errors or delete all errors.
- **Refresh** - Refresh the Error logs table.
- **Search** - Search the Error logs table by:

  - **Field name** (full name or partial name)
  - **Field ID**
  - **Type** (full type name or partial name)
  - **Error details**
- **Error Table** - List of error logs.

  - **Pagination** - For instances with many custom fields that encounter errors, the table will be paginated with navigation controls under the table itself.

Additionally, the error table consists of the following columns:

**Note**: Column headers can be used to sort the Calculations table.

- **Time** - Full date and time of the error.
- **Type** - The type of error.
- **Details** - Extended error details in the specific error message encountered.
- **Field Name & ID** - The field name and Jira unique identifier.  
  [note icon] **Note**: Occasionally an error will occur that is not related to a specific custom field. When this occurs, the field name and ID column will display **none**.
- **Acknowledged On** - *Only visible when the* ***Acknowledged*** *checkbox is checked at the top of the page.* The date and time when the error log was acknowledged.
- **Acknowledged** - Check this box to acknowledge the error. Acknowledged errors remain in the error list table, but are hidden by default. Uncheck this box to mark the error as unacknowledged.
- **Delete** - Completely remove the error log. **This action cannot be undone!**

You are viewing the documentation for **Jira Cloud**.

### On This Page

![Jira Misc Custom Fields (JMCF) Cloud error logs administration page](/cms_trial/assets/8afe2a05-0c9e-4005-99d4-63bb5d834c40.png)