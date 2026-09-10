# Summary report

The Summary report provides a comprehensive view of SLA information on a single page, allowing you to analyze performance and monitor SLA compliance at a glance.

## How to create a Summary report

1. In the Time to SLA top menu, click **Reports**.
2. From the *Generate new report*, click **Summary**.

   ![Screenshot 2026-07-14 at 00.02.07.png](/cms_trial/assets/272abd49-1fb1-4710-9ed2-0a65d7135154.png)
3. Filter your work items:

   - Use **Project**, **JQL**, or **Issue Filters** to refine the work items included in your report. When you select one, a new dropdown appears.
   - If you select **Issue Filters**, you can also apply Jira's built-in parameters or a previously saved work item filter.
   - Leave the filter type blank to include all work items.

When filtering your report, you **cannot** use `slaFunctions` in JQL. Instead, use the **+** **More** button to refine your SLA selection.

1. Select the SLAs:

   - Choose the SLAs you want to include in the report. The list displays all SLAs, both enabled and disabled.
   - Leave the field blank to include all SLAs.
2. Use the **+ More** button to tailor the report to your needs.

For example, you can choose to display only the SLAs that are in the critical zone, or to show only the SLAs with an end date within a specific date range. You can add as many parameters as you'd like.

![TTS- More filter selection-20260713-232748.gif](/cms_trial/assets/ee51fe34-7c20-45ab-b410-266a51cce617.gif)

1. Choose a time format for the report.
2. Customize the report by adding extra columns from the **Issue Columns** list.
3. Click **Generate** to create your report.

   - Alternatively, use the dropdown menu to [**Schedule periodic reports**](/cms_trial/space/TTSC/36012105/Periodic+reports/) or [**Create background reports**](/cms_trial/space/TTSC/36241436/Background+reports/).

You can click **Save filter as** to save the configuration, which lets you reuse it in other reports. Once saved, the report filter will appear on the side panel. The saved filters can be managed on the [**Manage report configurations**](/cms_trial/space/TTSC/36012079/Reports/) page.

## Understanding report results

Below is an example Summary report. It displays key information such as: **Issue Number**, **Issue Type**, **Summary**, **Priority**, **Reporter**, **Assignee**, **Status**, and the selected SLA(s) (for example, Time to Resolution).

The content displayed depends on your customization created with **+ More**, **Format**, and **Issue** **Columns**.

![image-20260713-224820.png](/cms_trial/assets/d34ff049-5862-4427-80ff-560abd113317.png)

About SLA status and duration, refer to this information:

- **SLAs within Target**: For SLAs that are still on track to meet their target date, the report shows the **remaining time** until the target is reached.
- **Breached SLAs**: For SLAs that have missed their target date, the report displays the **overdue duration**, indicating how long the SLA has been breached.

## Export the report

Using the button on the right-hand side, you can download your report as an XLSX file. Once you click the button, the download will start automatically.