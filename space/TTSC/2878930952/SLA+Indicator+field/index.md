# SLA Indicator field

The SLA Indicator field displays the current SLA status directly inside a Jira work item. It provides a quick visual overview of whether an SLA is:

- **In progress**
- **Breached**
- **Met**

When you click the information icon next to the field, a detailed breakdown appears, showing all related SLA configurations and their current states.

## Use cases

The SLA Indicator is a Jira custom field, which means you can use it anywhere Jira fields are supported.

For example, you can:

- Add it as a column in the work item navigator
- Use it in JQL searches
- Display it in dashboards and gadgets
- Include it in queues and reports

This allows teams and managers to monitor SLA health and prioritize work without opening individual work items. For example, you can create a gadget that displays only work items where the SLA Indicator is *In progress*, foreasy ticket prioritization**.**

---

## How to create an SLA Indicator field

1. Go to **Apps** > **Time to SLA** > **Administration** > **SLA Fields**.
2. Click the **SLA field** button.
3. Select **TTS -** **SLA Indicator**.

   ![Create an SLA Field dialog with TTS SLA Indicator selected, name and description fields, and SLA sources dropdown.](/cms_trial/assets/9ee70c2a-4262-4d0e-a6aa-8a9b92f210e9.png)
4. Enter a name.
5. Optionally, provide a description.
6. **SLA sources –** Choose which SLAs this field should monitor. In the configuration, you can select:

   - **ALL SLAs**, or
   - Individual SLAs available in your instance (select them one by one)
7. Click **Create**.

## After creating the field

To make the SLA field visible in work items, ensure that:

- It is in scope for the correct project and work item type.
- It is added to the relevant screens.
- It is included in the work item layout.

For detailed steps, refer to Atlassian’s documentation on [creating](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) and [managing fields and screens](https://support.atlassian.com/jira-cloud-administration/docs/find-your-custom-fields/).

## How it appears in work items

After you create the SLA Indicator field and configure Jira, it won’t automatically be applied to all existing work items. Open the work item at least once to attach the custom field, calculate its SLA value, and display it in the work item navigator, dashboards, queues, or gadgets.

The field becomes populated **only** **after** the work item is viewed.

**Why does this happen?**

Jira custom fields are calculated and stored when a work item is accessed. They do not automatically recalculate in the background for all existing work items. Once the work item is opened:

- Time to SLA calculates the SLA value.
- The custom field is updated.
- Custom field value changes do not appear in the Jira work item history even if they are updated.

This behavior is expected and cannot be disabled.

Once you configure the field in Jira, and open the work item:

- The field displays the current SLA status.

  ![Jira work item view showing the SLA Indicator field with Breached status in the details panel.](/cms_trial/assets/efd78bb8-043f-492e-81e4-075bfb7099da.png)
- Clicking the information icon shows a detailed SLA breakdown.

  ![Delivery indicator details dialog listing multiple SLAs with expected time, elapsed time, and remaining or breached values.](/cms_trial/assets/67e5248c-6c5e-4d08-9184-474e3666ec85.png)
  - **Expected Time** means the SLA deadline, which is the exact date and time by which the SLA goal must be met.
  - **Elapsed**/**Remaining**/**Breached** values are the same data you see in the SLA panel on the work item view.

  The table reflects the data from the moment the page was last refreshed. To see the most recent SLA data, refresh the work item page.

The info icon is available only on the work item page. It is not available in the other Jira views.

## How the field is updated

Jira does not automatically refresh field values in the background. This can cause your field to display outdated information on certain screens.

### Example

Your SLA is about to be breached in 2 minutes. You close the work item. Three minutes pass. You check the work item from the work item navigator. The SLA Indicator still shows **In progress**, not **Breached**.

This happens because Jira does not refresh field values in the background. The SLA value is calculated when the work item page is first opened.

## How multiple SLAs are evaluated

If you select multiple SLAs in the SLA sources, the SLA Indicator follows this logic:

1. If **any** selected SLA is **Breached**, the field displays **Breached**.
2. If none are breached and at least one is **In progress**, the field displays **In progress**.
3. If **all** selected SLAs are **Met**, the field displays **Met**.

When you click the information icon, you can see the detailed status of all selected SLAs.

The field provides a summarized status, while the information dialog provides the full breakdown. Together, they provide both a quick overview and detailed insights.

## Using the SLA Indicator field in JQL search

The SLA Indicator custom field can be used in JQL searches to filter work items by SLA status. This lets teams quickly identify items that are breached, still in progress, or successfully met, directly from the work item navigator, boards, dashboards, or saved filters.

### Available values

When used in JQL, the SLA Indicator field supports the following values:

- `BREACHED`
- `IN PROGRESS`
- `MET`
- `EMPTY`

These values appear in the JQL autocomplete dropdown when typing:

![Jira JQL search with SLA Indicator field showing autocomplete options EMPTY, BREACHED, IN PROGRESS, and MET.](/cms_trial/assets/a5daf1c5-5b17-45d5-87a0-0da6f41f4c12.png)

## Troubleshooting

### Why your SLA Indicator field is empty

The field may appear empty if:

- You’ve created the custom field through the Jira fields settings and haven’t completed the SLA field configuration.
- The SLA hasn’t started running for the work item.

### Why you can’t see the SLA field even though you created it

If the field does not appear, use Jira’s **Find your field** option from the work item view to identify the missing configuration.

### Why you see a spinner for a long time when opening the SLA Fields page

This is due to Atlassian Cloud platform limitations. The more custom fields your Jira instance has, the longer it may take to load the **SLA Fields** page. This happens because Time to SLA retrieves and displays up-to-date custom field data every time the page is opened.