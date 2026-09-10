# Reports

The **Reports** page helps you generate, view, and manage SLA reports in Time to SLA for Jira Cloud.

You can choose from different report types depending on what you want to analyze, from high-level SLA performance trends to detailed work item data.

## Access Reports

To open the Reports page:

1. Go to **Apps** > **Time to SLA**.
2. Select **Reports** from the top navigation.

![Reports page showing the navigation sidebar with report categories and the Generate new report page.](/cms_trial/assets/55d4f5c7-98f4-4647-80fe-157178184173.png)

The **Generate new report** page opens by default. From this page, you can choose the type of report you want to create.

### Reports sidebar

Use the sidebar to generate new reports, access generated reports, and manage report configurations and subscriptions.

- **Generate new report:** Click **Generate new report** to choose and create a new report.
- **Executive reports:** Shows saved Executive reports. Executive reports provide a high-level overview of SLA performance using completed SLA data, allowing you to spot where SLA performance breaks down and why. For more information, see the [documentation](/cms_trial/space/TTSC/3404431363/Executive+reports/) and the [use case](/cms_trial/space/TTSC/3426714512/I+want+to+review+cross-project+SLA+compliance+data+without+manual+spreadsheet+exports/).
- **Periodic reports:** Shows periodic reports that are generated and delivered at regular intervals. Use this page to view and download your periodic reports. For more information, refer to the [documentation](https://support.appfire.com/space/TTSC/36012105).
- **Background reports:** Shows reports generated asynchronously in the background. Use background reports when your report includes a large number of work items to avoid potential timeout errors. For more information, refer to the [documentation](https://support.appfire.com/space/TTSC/36241436).
- **Report configurations:** Access saved and default report configurations. Saved configurations can retain the report filters and, for table-based reports, the column order and sorting. The default options are:

  - Met SLAs
  - Breached SLAs
- **Manage report configurations:** View and manage saved report configurations.
- **Manage report subscriptions:** View and manage report subscriptions.

## Generate a new report

The **Generate new report** page lets you choose the type of report you want to create.

Available report types include:

| **Report type** | **Description** |
| --- | --- |
| [**Executive**](/cms_trial/space/TTSC/3404431363/Executive+reports/) | Analyze SLA performance using completed SLA data. Executive reports are useful for high-level trend analysis and stakeholder reporting. Refer to the [use case](/cms_trial/space/TTSC/3426714512/I+want+to+review+cross-project+SLA+compliance+data+without+manual+spreadsheet+exports/) to learn more. |
| [**Summary**](https://support.appfire.com/space/TTSC/36044860) | View a high-level overview of SLA performance. Summary reports are useful for work item-based reporting. |
| [**Detail**](https://support.appfire.com/space/TTSC/36143159) | Review granular SLA data for in-depth work item analysis. Detail reports are useful for SLA-based reporting. |
| [**Duration**](https://support.appfire.com/space/TTSC/36077648) | Track SLA duration trends over a selected time period using chart-based reports. |
| [**Status**](https://support.appfire.com/space/TTSC/44761089) | Monitor the distribution of SLA achievement using a pie chart. |

**When should you use which?**

Use **Summary** reports when you need a work item-based overview. Use **Detail** reports when you need a more SLA-focused breakdown. Use **Duration** and **Status** reports when you want to visualize SLA data and share results quickly. Use **Executive** reports when you need a stakeholder-friendly view of completed SLA performance over time.

To generate a report:

1. Select **Reports** from the top navigation. The *Generate new report* screen opens.
2. Choose the report type you want to create.
3. Configure the report fields and filters. For detailed instructions, see:

   - [**Executive**](/cms_trial/space/TTSC/3404431363/Executive+reports/)
   - [**Summary**](https://support.appfire.com/space/TTSC/36044860)
   - [**Detail**](https://support.appfire.com/space/TTSC/36143159)
   - [**Duration**](https://support.appfire.com/space/TTSC/36077648)
   - [**Status**](https://support.appfire.com/space/TTSC/44761089)
4. Select **Generate**.

## Save a report configuration

When creating a Summary, Detail, Duration, or Status report, you can save its configuration to reuse the same settings later.

For table-based reports, a saved configuration retains the order in which columns appear.

To save a report configuration:

1. On the **Reports** screen, click either **Summary**, **Detail**, **Duration**, or **Status**.
2. Create the report configuration you want to save for later.
3. Click **Save filter as**.

   ![Report toolbar showing the Save filter as option.](/cms_trial/assets/8470ebfc-cdbf-474b-960d-089a925c690b.png)
4. Give your filter a name.

   ![Save filter dialog for entering a name for a report configuration.](/cms_trial/assets/95129695-da48-40d5-aa64-30575df29652.png)
5. Click **Save**.

Saved configurations appear under **Report configurations** in the sidebar.

When you open a saved configuration and regenerate the report, Time to SLA restores its saved filters and the column order.

## Manage report configurations

You can use the **Manage report configurations** page to review and manage reports, except for the Executive reports, which have their own management page. When you edit a saved report configuration, you can update its filters and, for table-based reports, save a new column order or sorting.

Here is a list of things you can do on this screen:

### Favorite report configurations

You can star your favorite report configurations to list them at the top of the *Report configurations* section in the sidebar.

![Reports sidebar showing report configurations with the option to mark a configuration as a favorite.](/cms_trial/assets/db8e12bc-9cde-4e05-b01b-53207893e3d0.png)

### Filter options

By clicking the actions menu next to the filter, you can clone, delete, and edit filters. By clicking **Manage subscriptions**, you can also quickly create a subscription based on the filter.

Image — asset pipeline pending  
Report configuration actions menu with options to edit, clone, delete, or manage subscriptions.

## Manage report subscriptions

This page displays and lets you manage your subscriptions for periodic reporting.

### View subscriptions

All subscription details are provided here, showcasing the configuration used for each subscription.

- To view the configurations in greater detail, click the chevron button, and the information will be revealed.

  Image — asset pipeline pending  
  Subscription list with the details panel expanded to display report configuration information.

### Subscription options

By clicking the actions menu next to the subscription, you can manage your report email subscriptions. This includes options to edit, clone, and delete your subscriptions as needed.

- Instead of waiting for your report to arrive when it’s scheduled, you can run it immediately by clicking **Run now**.

  Image — asset pipeline pending  
  Subscription actions menu with options including Run now, edit, clone, and delete.