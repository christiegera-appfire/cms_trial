# Periodic reports

Periodic reports are generated and delivered at regular intervals, helping with decision-making and serving as project deliverables. You can:

- Create multiple report subscriptions,
- Receive reports directly in your email inbox on a schedule you define.

You can view, download, and manage your periodic reports from the **Periodic reports** page.

![image-20260714-151854.png](/cms_trial/assets/7d531431-2d95-4400-8804-8f510e8ef3eb.png)

## How to create a periodic report

1. In the Time to SLA top menu, click **Reports**.
2. Select a report type.

Select a report type that supports periodic reports: **Summary, Detail, SLA Durations,** or **SLA Status**.

Periodic reports are not available for **Executive** reports.

1. Configure your report according to its type. For more details, refer to the documentation for [**Summary**](/cms_trial/space/TTSC/36044860/Summary+report/), [**Detail**](/cms_trial/space/TTSC/36143159/Detail+report/), [**SLA Durations**](/cms_trial/space/TTSC/36077648/Durations+report/), or [**SLA Status**](/cms_trial/space/TTSC/44761089/Status+report/) reports.
2. Once you’re satisfied with your configuration, click the chevron next to **Generate** to reveal the dropdown menu.

   ![Screenshot 2026-07-14 at 15.52.50.png](/cms_trial/assets/ec379646-1d37-4c7e-86d4-6c113291c311.png)
3. Click **Schedule periodic report**. The *Subscribe for Report* screen appears.
4. On the *Subscribe for Report* screen, provide the following details:

   ![Time to SLA Periodic reports subscription settings dialog](/cms_trial/assets/32ac4953-2625-41ea-ac48-cb50f7026a9b.png)
   - **Name:** Assign a name to your report.
   - **Recipients:** Specify who will receive the report.
   - **Editors:** Add users who can edit the report settings.
   - **Schedule:** Click **Build Cron expression** to pick a time for the report. After you've chosen your preferred time, click **OK**.

     ![Time to SLA Periodic reports schedule configuration dialog](/cms_trial/assets/443e408e-e7bd-405b-b230-df0a4902ad46.png)
   - **Email this report, even if there are no issues found:** Check this box if you want to be notified in such cases.

Periodic reports help you share data efficiently, but access should be managed carefully. Only editors and designated recipients can view the report on the **Periodic reports** screen.

**As the subscription owner, you’re responsible for ensuring that only authorized users receive and access the report****.** Before adding recipients, review the report’s scope and confirm that each recipient has the necessary permissions.

1. Click **Save** to schedule the report.

Once generated, the report appears on the **Periodic Reports** page, where you can view its status and download the report. Recipients receive the standard notification email when the report is ready, based on the subscription’s email settings.

![image-20260831-125851.png](/cms_trial/assets/c3b86236-a4f7-4d28-b617-82be075ef687.png)

![image-20260831-130621.png](/cms_trial/assets/c40225f0-6ae9-4b68-a3be-963691942ed7.png)

![image-20260831-130858.png](/cms_trial/assets/ef1a5e3a-e66f-4a5d-8838-c666a717ccba.png)

### **What to do if you don’t receive a report**

Check the **State** section on the *Periodic reports* page. It displays your report's current status and can help you identify any issues preventing delivery.

![Time to SLA Periodic reports table showing generated reports](/cms_trial/assets/02806540-0ffb-48b7-87c1-2f4c4151e26a.png)

## How to create a subscription from a saved filter

1. Go to **Manage report configurations**.
2. Find the filter you want and click the actions menu button.

   ![Time to SLA Periodic reports report details with SLA data](/cms_trial/assets/fa065b7c-94df-45ce-916c-67d57d97d45b.png)
3. Click **Manage Subscriptions**. A subscription page for the filter you have chosen appears.
4. Click the **Add subscription** button. The *Subscribe for Report* screen appears.

   ![Time to SLA Periodic reports results table with summary columns](/cms_trial/assets/a58dcaa0-99d7-4059-a427-5a11eab8556b.png)
5. Configure your subscriptions by following the steps described above.
6. Click **Save** to schedule the report.

## How to create a subscription from a background report

1. Click **Background Reports**.
2. Find the filter you want and click the actions menu button.

   ![Time to SLA Periodic reports detailed results with SLA status](/cms_trial/assets/16401671-d131-4b59-94e1-c85ab0ba7307.png)
3. Click **Add Subscription**. The *Subscribe for Report* screen appears.
4. Configure your subscriptions by following the [steps](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/edit-v2/36012105#How-to-create-a-periodic-report) described above.
5. Click **Save** to schedule the report.

## How to download periodic reports

1. Go to the **Periodic Reports** page.
2. Find the report you want to download and click the settings icon next to it.
3. Select **Download report** to start the download automatically.

The report will be downloaded automatically in `.CSV` format.

For **SLA Durations** and **SLA Status** reports, the CSV contains the same summary data as the **Excel export** available from the report page for the same configuration. Charts are not included in the periodic report.