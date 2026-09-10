# Calculations

**Note**: Version 2.0 of JMCF for Jira Cloud includes the release of [Scripted Fields](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/713588743). *This feature is currently in* ***limited release***.

Full availability of Scripted Fields will occur in a future release.

The **Calculations** page (Figure 1, right) displays the list of JMCF custom fields and their calculation status; unlike the **My custom fields** page where each custom field is listed once, custom fields on the Calculations page are listed for *each context to which the field has been added*. This is because the custom field is calculated separately for each of its' contexts. Additionally, you must manually trigger a recalculation when adding a new context to a custom field; recalculations can be started by clicking the **Edit custom field config** link under the new context and clicking **Save**.

Th **Calculations** page only lists fields that are in the process of calculation or recalculation; recalculations that are suspended; and completed calculations. Completed calculations **remain on the list for 24 hours and then they are removed**.

**Note**: You may encounter slight delays in the calculation or recalculation of a custom field. If you do not see a calculation running when it is expected, please wait a moment and refresh the list using the **Refresh** button.

**Create Custom Field Wizard vs. Native Jira UI**

In some circumstances, JMCF custom fields will behave differently depending on whether they were created using the [Create Custom Field Wizard](/cms_trial/space/JMCFC/465405703/Create+Custom+Field/) or if they were created through the native Jira UI. The differences are mostly around how the field is initially calculated, or recalculated. The following are specific considerations when creating JMCF custom fields:

- If you create a JMCF custom field using the native Jira UI, you **must open and save** the context configuration for that field to manually trigger a calculation; it will not calculate automatically!   
  For steps on editing the context of a custom field, see <https://support.atlassian.com/jira-cloud-administration/docs/edit-a-custom-fields-options/>.
- If you recover a JMCF custom field from the Trash, you **must open and save** the context configuration for that field to manually trigger a *recalculation*; it will not recalculate automatically!   
  For steps on editing the context of a custom field, see <https://support.atlassian.com/jira-cloud-administration/docs/edit-a-custom-fields-options/>.

The Calculations page includes, from top to bottom:

- **Page Toolbar** - The upper right corner of the page includes a menu with several commands:

  - **Documentation** - Open the JMCF for Jira Cloud documentation.
  - **Support request** - Open the Appfire Support portal to submit a support request.
  - **Feedback** - Open the Appfire Support portal to submit an enhancement or feature request.
  - **Atlassian Community** - Open the [Atlassian Community page for JMCF](https://community.atlassian.com/t5/tag/addon-com.innovalog.jmcf.jira-misc-custom-fields/tg-p/category-id/atlassian-marketplace).
- **Refresh** - Refresh the list of recent calculations and their progress. Completed calculations will remain on the list for 24 hours before they are removed automatically.
- **Search** - Search calculated (or recalculating) fields by name.
- **Calculations Table** - a paginated list of calculations that are currently running.

  - **Pagination** - For instances with many custom fields that recalculate often, the table will be paginated with navigation controls under the table itself.

The table of running calculations includes the following fields.

**Note**: Column headers can be used to sort the Calculations table.

- **Field name** - The name of the field, including the Jira field identifier (e.g. ‘customfield\_12593’).
- **Context** - Lists the contexts to which the custom field has been added. See [Configure custom field context](https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-field-context/) for more information.   
  [note icon] **Note**: Custom fields are listed separately for each context to which they are added.
- **Issues** - The number of issues involved in the calculation or recalculation.
- **Rate** - JMCF works on calculations in a round-robin fashion until all calculations are complete. This column indicates the rate of calculation in issues per second while JMCF is working on that calculation. *This should not be used as an estimate of time to completion*.
- **Progress** - The status of the calculation in terms of percent complete.
- **Action** - This button will change depending on the current status of the calculation.

  - **Restart** [action restart icon] - For calculations that have completed, perform a recalculation.
  - **Suspend** [action pause icon] - Running calculations can be suspended if needed.
  - **Resume** [action resume icon] - Start a suspended calculation.
- **Cancel** - Cancel the calculation and remove it from the list.

**Note**: deleting a calculation does *not* delete the custom field!

You are viewing the documentation for **Jira Cloud**.

![Jira Misc Custom Fields (JMCF) Cloud calculations administration interface](/cms_trial/assets/83407ac0-0961-4f6d-8cbf-305558c194ed.png)