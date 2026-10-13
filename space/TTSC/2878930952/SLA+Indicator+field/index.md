# SLA Indicator field

The SLA Indicator field displays SLA status directly in Jira work items. It helps you identify whether an SLA is in progress, breached, or met without opening the SLA panel.

The field supports three statuses:

- **In progress:** The SLA is running and hasn't breached its goal.
- **Breached:** The SLA has exceeded its target.
- **Met:** The SLA goal has been achieved.

When you click the information icon next to the field, a detailed breakdown appears, showing all related SLA configurations and their current states.

## Use cases

The SLA Indicator is a Jira custom field, which means you can use it anywhere Jira fields are supported.

For example, you can:

- Add it as a column in the work item navigator
- Use it in Jira Query Language (JQL) searches.
- Display it in dashboards and gadgets
- Include it in queues and reports

This helps you monitor SLA statuses and prioritize work without opening individual work items.

For example, you can create a Jira filter that displays work items with an **In progress** SLA Indicator status. Your team can then use the filter to identify work that needs attention.

## Create an SLA Indicator field

1. Go to **Apps** > **Time to SLA** > **Administration** > **SLA Fields**.
2. Click the **SLA field** button.
3. Select **TTS -** **SLA Indicator**.

   ![Create an SLA Field dialog with TTS SLA Indicator selected, name and description fields, and SLA sources dropdown.](/cms_trial/assets/9ee70c2a-4262-4d0e-a6aa-8a9b92f210e9.png)
4. Enter a name for the field.
5. Optionally, provide a description.
6. Under **SLA sources**, select the SLAs you want the field to monitor:

   - **ALL SLAs:** Include all available SLAs.
   - **Individual SLAs:** Select specific SLAs from the list.
7. Click **Create**.

The SLA Indicator field is created. You can now configure where it appears in Jira.

## After creating the field

After creating the SLA Indicator field, configure its visibility in Jira. Make sure that:

- The field is in scope for the correct Jira projects and work item types.
- The field is added to the relevant Jira screens.
- The field is included in the work item layout.

For detailed steps, refer to Atlassian’s documentation on [creating](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) and [managing fields and screens](https://support.atlassian.com/jira-cloud-administration/docs/find-your-custom-fields/).

## Enable live updates (optional)

You can enable **Live updates** to keep SLA Indicator field values up to date automatically in the background.

Live updates is turned off by default. You can enable it separately for each SLA Indicator field.

When enabled, Time to SLA updates the custom field value when:

- The Jira work item is updated.
- The SLA status changes.

You don't need to open the work item to trigger these background updates.

This helps keep SLA statuses current across Jira boards, filters, and automation rules.

Live updates doesn't automatically populate SLA Indicator fields for work items whose SLAs haven't started. The field needs an applicable SLA to calculate its status.

### Turn on live updates

1. Go to **Apps** > **Time to SLA** > **Administration** > **SLA Fields**.
2. Find the SLA Indicator field you want to configure.
3. Turn on **Live updates**.

Time to SLA now updates the field in the background when the work item is updated or its SLA status changes.

## Understand how the field is populated and updated

After you create the SLA Indicator field and configure Jira, the field isn't automatically populated for all existing work items.

To populate the field with SLA values, you can either:

- **Open the work item:** Time to SLA calculates the SLA value and populates the custom field when you view the work item.
- **Run SLA recalculation:** Recalculate SLAs for existing work items to populate or update their custom field values without opening each work item individually.

Once populated, the SLA Indicator field can display SLA information in the work item navigator, dashboards, queues, and gadgets.

For more information, see [Recalculation](/cms_trial/space/TTSC/35456416/Recalculation/).

Once you configure the field in Jira, and open the work item:

- The field displays the current SLA status.

  ![Jira work item view showing the SLA Indicator field with Breached status in the details panel.](/cms_trial/assets/efd78bb8-043f-492e-81e4-075bfb7099da.png)
- Clicking the information icon shows a detailed SLA breakdown.

  ![Delivery indicator details dialog listing multiple SLAs with expected time, elapsed time, and remaining or breached values.](/cms_trial/assets/67e5248c-6c5e-4d08-9184-474e3666ec85.png)
  - **Expected Time** means the SLA deadline, which is the exact date and time by which the SLA goal must be met.
  - **Elapsed**/**Remaining**/**Breached** values are the same data you see in the SLA panel on the work item view.

  The table reflects the data from the moment the page was last refreshed. To see the most recent SLA data, refresh the work item page.

The info icon is available only on the work item page. It is not available in the other Jira views.

## How multiple SLAs are evaluated

If you select multiple SLAs in the SLA sources, the SLA Indicator follows this logic:

1. If **any** selected SLA is **Breached**, the field displays **Breached**.
2. If none are breached and at least one is **In progress**, the field displays **In progress**.
3. If **all** selected SLAs are **Met**, the field displays **Met**.

When you click the information icon, you can see the detailed status of all selected SLAs.

The field provides a summarized status, while the information dialog provides the full breakdown. Together, they provide both a quick overview and detailed insights.

## Using the SLA Indicator field in JQL search

The SLA Indicator custom field can be used in JQL searches to filter work items by SLA status. This lets teams quickly identify items that are breached, still in progress, or successfully met, directly from the work item navigator, boards, dashboards, or saved filters.

### Available JQL values

When used in JQL, the SLA Indicator field supports the following values:

- `BREACHED`
- `IN PROGRESS`
- `MET`
- `EMPTY`

These values appear in the JQL autocomplete dropdown when typing:

![Jira JQL search with SLA Indicator field showing autocomplete options EMPTY, BREACHED, IN PROGRESS, and MET.](/cms_trial/assets/a5daf1c5-5b17-45d5-87a0-0da6f41f4c12.png)

## Troubleshooting

### The SLA Indicator field is empty

The field may appear empty if:

- You created the custom field through Jira's field settings but haven't completed its SLA field configuration in Time to SLA.
- The SLA hasn't started running for the work item.
- The field hasn't been populated for an existing work item.

Check that the field is configured correctly in **Administration** > **SLA Fields** and that an applicable SLA has started.

### The SLA Indicator field isn't visible

If the field doesn't appear on a Jira work item, use Jira's **Find your field** option to identify missing configuration.

Check that:

- The field is in scope for the project's work item type.
- The field is associated with the relevant screens.
- The field is included in the work item layout.

### The SLA Indicator displays an outdated status

If the SLA Indicator displays an outdated status in Jira boards, filters, or other views, check whether **Live updates** is enabled.

Live updates is turned off by default. Without it, SLA Indicator values may remain unchanged until the work item is opened and the field value is refreshed.

### The SLA Fields page takes a long time to load

The *SLA Fields* page may take longer to load in Jira instances with a large number of custom fields.

This is related to Atlassian Cloud platform limitations. Time to SLA retrieves current custom field data whenever you open the page, so loading times can vary depending on the number of fields in your Jira instance.