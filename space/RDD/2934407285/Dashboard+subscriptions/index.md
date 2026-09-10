# Dashboard subscriptions

This page explains how to subscribe to a dashboard in Dashboard Hub Pro and Dashboard Hub for Confluence.

## Overview

Subscriptions are automated, secure, and shareable point-in-time reports that reduce manual effort, improve reporting reliability, and ensure that all stakeholders reference the same data. Subscriptions work by setting a schedule to capture a static snapshot of a dashboard and sending it to selected users by email, making them especially useful for recurring reporting cycles such as end-of-sprint or end-of-month reviews.

![Email notification containing a dashboard snapshot link, timestamp, and subscription details.](/cms_trial/assets/86ba15cd-474c-4d12-a585-edbd2cdd3cc4.png)

## Popular use cases

- **Automated reporting for teams**: Schedule monthly dashboard snapshots so team members receive consistent updates without manual preparation. Each report reflects the exact state of the dashboard at the time it was captured.
- **End-of-sprint capture**: When a sprint closes, a dashboard snapshot preserves key metrics such as velocity and completion rates, ensuring sprint results remain accurate, even as work continues in the next cycle.
- **Leadership updates**: Organizations use recurring snapshots to keep leadership informed with reliable, weekly, or monthly dashboard summaries to deliver a fixed reporting cadence.
- **Historical review**:Use snapshots to keep a record of important milestones, such as quarter-end, major releases, or reviews.
- **Secure sharing**:Use the optional password protection to share reports without sharing any other internal data.

### Video overview

Watch the feature video to get started, or follow the instructions below.

Video transcript:

A subscription is a scheduled, automated report that captures your dashboard exactly as it appears at a specific moment in time and sends it to your chosen recipients by email. That captured version is called a snapshot.

You can share snapshots without exposing your live dashboards, and because they’re stored for up to one year, you’ll be able to look back and see exactly where things stood at specific moments.

To create a subscription, open your dashboard and select Share dashboard, then Subscribe to dashboard. From there, you’ll build your schedule. You can choose to send snapshots daily, on specific days of the week, or on set days each month.

Next, you’ll see the password field. Whether this is optional or required depends on how your Jira or Confluence administrator has configured Dashboard Hub. If required password protection is enabled, you must set a password before saving. If a password is added, make sure you share it with your recipients separately; it won’t be included in the notification email.

Then, add your recipients. You can search for individual Jira or Confluence users or groups, and there’s no limit to how many you can include. If you’d like to give recipients some context, add an optional message to the email body.

When you’re ready, click Save. The subscription is active immediately, and the first snapshot will go out at the next scheduled time.

To view a snapshot, recipients click the link in their email. If the snapshot is password-protected, they’ll be prompted to enter it first.

If you need to make changes to the subscription, go to Share dashboard, then Manage subscription. From there, you can update the schedule, recipients, or message, or delete the subscription entirely.

To recap: Subscriptions let you schedule automatic dashboard snapshots and deliver them to your team by email. Set your schedule, configure your recipients, add a password if needed, and save. Your stakeholders will receive consistent, point-in-time reports on the cadence that works for your team, with no manual work required.

## How it works

At the scheduled time, Dashboard Hub:

1. Captures a static, read-only version of the dashboard as it currently appears. Filters, drill-downs, and live data updates are not available in snapshot view.
2. Stores the snapshot as a static asset so the data cannot change after capture. The snapshot is stored for one year, after which it is deleted.
3. Generates a unique public link for that snapshot.
4. Sends an email to all configured recipients containing the link and any optional message you have added.

## How to set up a subscription

1. In Dashboard Hub, open your dashboard and select **Share dashboard** > **Subscribe to dashboard**. The *Create* *subscription* page opens.

   ![Subscription setup page showing schedule, password, recipients, and message configuration options.](/cms_trial/assets/a299b4b5-e7b3-47de-966b-5bce0ff65be9.png)
2. Create the schedule using one of the following options:

| **Option** | **When to use** | **Additional settings** |
| --- | --- | --- |
| **Daily** | Continuous monitoring cadences, stand-up reports | Frequency (once or twice per day); time of day |
| **Days per week** | Sprint reviews, weekly team reports | Day of the week; time of day |
| **Days per month** | Monthly reports, end-of-month billing snapshots | Specific date or relative day (for example, third Wednesday); time of day |

1. **Password**: If you want to protect the snapshot with a password, you can add one here. If your administrator has enabled snapshot password protection, this field is required. Enter the password that the recipients must provide before viewing the snapshot.
2. **Recipients**: Add one or more users or user groups. Start typing a name or group to search, then select from the suggestions. There is a maximum of 100 recipients per subscription.
3. **Message** (*optional*):Add a message to include in the body of the subscription email. Use it to provide context for the snapshot, for example, a summary of the sprint. If left empty, the email will contain only the report name, timestamp, and link.
4. Click **Save**. The subscription is active immediately and the first snapshot will be captured at the next scheduled time.

**Tips**

- Schedules run according to the server time zone configured in your instance.
- If recipients don’t receive the emails, ask your admin to verify the outgoing mail configuration in Jira or Confluence system settings.
- **Communicate passwords separately**.The subscription email does not include the password. Share it with recipients through a separate, secure channel before the first snapshot is delivered.
- If you don’t see the *Subscribe to dashboard* option, check the **Restrict Public Links** setting in Global settings, or contact your admin. If this setting is turned on, only selected users or groups can subscribe to dashboards.

## How to view a snapshot

Click **View snapshot** in your *Subscription* email to open the snapshot in a new browser tab.

- **Without password protection**: The snapshot loads immediately.
- **With password protection**: You are prompted to enter the password before the snapshot is displayed.

## How to manage subscriptions

Use the Manage subscriptions feature to amend a specific dashboard schedule, update a name or email content, change recipients, or delete a subscription. To view all dashboard subscriptions, go to My subscriptions.

**To manage subscriptions:**

1. In your dashboard, select **Share dashboard** > **Manage subscription**.
2. Make any required changes to your subscription in the *Manage subscription* page, then click **Save**.
3. To delete a subscription, click **Delete subscription**.

## new My subscriptions

The *My subscriptions* pagehelps you manage multiple subscriptions from one place. To go to My subscriptions, in the top bar of a dashboard, select **More actions** (**…**) > **My subscriptions**

![The My subscriptions option highlighted in the More actions menu in Dashboard Hub](/cms_trial/assets/5e9e7247-a3b7-43c1-9e58-fa669c5cdfcb.png)

*My subscriptions* provides the following:

- Overview of all subscription details in a list including next scheduled date, recipients, and restrictions.
- **Actions** menu for each subscription that includes options to unsubscribe, edit, or perform a manual run.

![My subscriptions page in Dashboard Hub showing the options available in the Actions menu.](/cms_trial/assets/b4595e4b-f253-4476-954e-c213caacac98.png)

- **Edit**: Click **Edit** to open the *Manage subscription* page for a specific dashboard. This option is available only to the subscription editor.
- **Run now**: Click **Run now** to generate an adhoc snapshot email outside of the defined schedule. This option is available only to the subscription editor.
- **Unsubscribe**: Click **Unsubscribe** to remove your name from the recipient list. To resubscribe later, contact a dashboard editor.

## How to restrict subscriptions with passwords

Administrators can set password requirements for subscriptions in Global Settings. The example below illustrates Global Settings in Jira.

1. Go to **App settings** > **Global Access Restrictions**.
2. Click the **Require a password for email subscriptions** toggle to turn it on. The password requirement applies only to new subscriptions.

   ![Global Settings page showing the toggles under Restrict Global Access and Subscriptions enabled.](/cms_trial/assets/2ab369b3-0b14-4652-9882-7069c6421bbe.png)