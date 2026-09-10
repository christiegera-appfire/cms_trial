# Detail report

The SLA Detail Report provides a comprehensive view of all your work items and SLA information on a single page.

With the Detail Report, you can display key details, including:

- **Work item details:** Work Item, Type, Summary, Priority, Reporter, Assignee, Status
- **SLA details:** Name, Indicator, Status, Start Time, Deadline, End Time
- **Time tracking:** Working Duration, Remaining Duration, Paused Duration

## How to create a Detail report

1. In the Time to SLA top menu, click **Reports**.
2. From the *Generate new report*, click **Detail**.

   ![image-20260713-232949.png](/cms_trial/assets/da20aa77-1069-4f82-901e-cd1034f3993e.png)
3. Filter your work items:

   - Use **Project**, **JQL**, or **Issue Filters** to refine the work items included in your report. When you select one, a new dropdown appears.
   - If you select **Issue Filters**, you can also apply Jira’s built-in parameters or a previously saved work item filter.
   - Leave the filter type blank to include all work items.

When filtering your report, you **cannot** use `slaFunctions` in JQL. Instead, use the **+** **More** button to refine your SLA selection.

1. Select the SLAs:

   - Choose the SLAs you want to include in the report. The list displays all SLAs, both enabled and disabled.
   - Leave the field blank to include all SLAs.
2. Use the **+ More** button to tailor the report to your needs.

For example, you can choose to display only the SLAs that are in the critical zone, or to show only the SLAs with an end date within a specific date range. You can add as many parameters as you’d like.

![TTS- More filter selection-20260713-232748.gif](/cms_trial/assets/e92d5212-c9bc-4550-976e-21bb45688b24.gif)

1. Choose a time format for the report.
2. Use the **SLA Columns** and **Issue Columns** dropdowns to add or remove columns from your report.
3. Click **Generate** to create your report.

   - Alternatively, use the dropdown menu to [**Schedule periodic reports**](/cms_trial/space/TTSC/36012105/Periodic+reports/) or [**Create background reports**](/cms_trial/space/TTSC/36241436/Background+reports/).

You can click **Save filter as** to save the configuration, which lets you reuse it in other reports. Once saved, the report filter will appear on the side panel. The saved filters can be managed on the [**Manage report configurations**](/cms_trial/space/TTSC/36012079/Reports/) page.

## Understanding report results

The report provides detailed information in columns to help you analyze your SLAs. The content displayed depends on your customization created with **+ More**, **Format**, **SLA** **Columns**, and **Issue** **Columns**.

![image-20260713-230744.png](/cms_trial/assets/877e7721-4f1e-426c-adb6-df1336588570.png)

- **Working Duration**: Time spent so far.
- **Remaining Duration**: Time left.
- **Paused Duration**: Time paused.
- **Breach Duration**: Time overdue (if applicable).

**Key terms to note:**

- Deadline = Target Date
- Working Duration = Elapsed Duration
- Breached = Overdue

![image-20260713-232245.png](/cms_trial/assets/fb5165c2-2a0f-4d55-8187-fb52406414d4.png)

## Export the report

Using the button on the right-hand side, you can download your report as an XLSX file. Once you click the button, the download will start automatically.