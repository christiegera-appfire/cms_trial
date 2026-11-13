# Background reports

When your report filters return a large number of results, generating the report can take some time. Background reports allow you to create reports that run asynchronously in the background, so you can continue working without interruption.

If your report involves a high number of work items, we **strongly recommend** using background reports to avoid potential timeout errors.

![image-20260714-161850.png](/cms_trial/assets/fc20eb1b-221e-4d44-9b56-740226b523c1.png)

On the **Background Reports** page, you can:

- View details of all your background reports
- Download reports in `.CSV` format
- Add subscriptions for periodic reporting
- Delete old or unnecessary reports

## How to create a background report

1. In the Time to SLA top menu, click **Reports**.
2. Select a report type.

Background reports are not available for **Status** and **Durations** reports.

1. Configure your report according to its type. For more details, refer to the related documentation: [**Summary**](/cms_trial/space/TTSC/36044860/Summary+report/), [**Detail**](/cms_trial/space/TTSC/36143159/Detail+report/).
2. Once you’re satisfied with your configuration, click the chevron next to **Generate** to reveal the dropdown menu.

   ![image-20260714-152933.png](/cms_trial/assets/280057cf-e926-4d2c-af43-f2e504f7a542.png)
3. Click **Create background report**. The *Create background report* screen appears.

   ![Time to SLA Background reports status dialog with report actions](/cms_trial/assets/caa85bca-567b-4ae1-998b-42768a02904d.png)
4. Assign a name (for example, `tts-summary-report`) to your report.
5. Click **Generate**.

The report generation will start immediately in the background. You can navigate to the Background Reports to see the report status.

You can create a subscription directly from your background report. For detailed instructions, refer to the [related documentation](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/edit-v2/36012105#How-to-create-a-subscription-from-a-background-report).

## How to download background reports

1. Go to the **Background Reports** page.
2. Find the report you want to download and click the actions menu button next to it.
3. Select **Download report** to start the download automatically.

The report will be downloaded automatically in `.CSV` format.