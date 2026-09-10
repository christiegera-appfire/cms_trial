# Get started with Time to SLA for Cloud

Time to SLA helps you define, track, automate, and report on service level agreements (SLAs) in Jira Cloud. This guide walks you through the initial setup and shows you where to view SLA information after configuration.

## What is Time to SLA?

Time to SLA tracks SLA deadlines based on the goals, calendars, and conditions you configure.

- If you administer Time to SLA, you can configure SLAs, calendars, actions, permissions, and reports.
- If you use SLAs on Jira work items, you can view SLA progress, review SLA history, and receive notifications configured by your administrator.

## For admins

### Step 1: Set up permissions

Before you configure Time to SLA, review who can access its administration features.

1. Open **Apps** > **Time to SLA**.
2. Select **Administration** > **Permissions**.
3. Configure the users and groups that can access the required Time to SLA features.

For details about each permission, see [**Manage permissions**](/cms_trial/space/TTSC/36110655/Manage+permissions/).

### Step 2: Configure calendars

Every SLA uses a calendar to determine its working time. Time to SLA includes a 24/7 calendar by default, so you don't need to create a calendar if your SLA runs continuously.

Create a custom calendar when you need to define business hours, holidays, breaks, or other non-working periods.

- **Using standard business hours?** → Create a new calendar.
- **Using round-the-clock support?** → Stick with the default 24/7 calendar.

[Learn how to configure calendars](/cms_trial/space/TTSC/35750012/Create+calendars/)

Before proceeding, [set your time zone](/cms_trial/space/TTSC/37290034/Administration/) under **Administration** > **General** to ensure accurate calculations.

### Step 3: Define your first SLA

When you first open Time to SLA, you may be asked a few onboarding questions. After you complete the onboarding, the **Get Started** page opens.

Select **Create your first SLA** to begin.

You can create the SLA from a template or from scratch.

![The SLA templates on the Time to SLA for Jira Cloud New SLA page.](/cms_trial/assets/1a04e801-31f5-42d8-986f-29aec5fa468e.png)

You can pick an SLA template to get started:

![The SLA template options on the Time to SLA for Jira Cloud New SLA page.](/cms_trial/assets/b77d756c-6f65-4c66-b82c-c458af7f8b44.png)

- **Time to resolution** – Track how long work items take to resolve.
- **Time to first response** – Measure response time for new work items.
- **Time in “In Progress”** – Monitor how long a work item stays in a particular status.

Select **Create from template**, choose a template, and configure the SLA for your Jira spaces. To configure all SLA settings yourself, select **Create from scratch**. The video below walks you through the steps.

Video script

Hi there! In this video, we’ll show you how to create your first SLA in the Time to SLA app for Jira Cloud. Let’s get started.

First, open the **SLAs** screen, then click on **SLA** or **Create your first SLA**.

Give your SLA a clear name so your team knows what it’s for. Optionally, add a description for more details. After that, select the project this SLA will apply to. You can further refine the issues by specifying additional details like issue type, request type, assignee, and JQL in the next step. When you're ready, hit **Next** to move forward.

Now, let’s set the goals for your SLA. Think of SLA goals as the timeframes or deadlines for tasks. You can set these as specific durations—like days or hours—or tie them to a custom field, such as a due date.

Want to add multiple goals? Just click the Add Goal button. For example, you might create an SLA goal for issues tagged as High Priority or based on certain issue types or request types. These goals will be prioritized from top to bottom.

The SLA will be applied to issues that match the filters or queries you set up.

Now, let's set when the SLA should start, pause, and stop. For example, you can start the SLA when an issue is assigned, pause it while you’re waiting for customer feedback, and stop it once the issue is resolved.

You can add multiple conditions and, if needed, group them using **AND** or **OR** operators for more complex scenarios.

For those who want to dive deeper, Time to SLA has advanced options like the Calculation Method, Critical Zone Percentage, and more. For example, these tools can help you track when an SLA is approaching its deadline and customize notifications to stay ahead of the curve.

And that’s it! Once you’re done, just hit **Save**, and your SLA is ready to go. Now you can track, manage, and meet your deadlines more efficiently in Jira.

To see your SLA in action, create a new issue and open it. This is the SLA panel, where you’ll see a live countdown tracking the time, along with key metrics to help you monitor progress. When the start condition is met, the SLA panel will start ticking. If you want your SLA to apply to existing issues, just run a recalculation within the SLA's scope. There’s more info on that in the documentation.

Once the SLA starts, you’ll automatically receive notifications when it reaches 50% and 75% of its duration to help you stay on top of deadlines.

Thanks for watching! Now that you know the basics, dive into the app and start creating SLAs that help your team deliver results on time, every time. Happy tracking!

[Learn more about defining SLAs](/cms_trial/space/TTSC/35651691/Define+SLAs/)

### Step 4: View and customize the SLA panel

After you create an SLA, verify that it applies to the work items you expect.

You can click **Create a test issue** after creating your first SLA, or create a Jira work item in the SLA's configured scope.

![The screen that appears after you've created your first SLA in the Time to SLA for Jira Cloud app.](/cms_trial/assets/038d1376-7d95-4acb-9da6-41939475e6a7.png)

Open the work item and view the **SLA Panel** to review the SLA's progress.

Previously, the SLA panel appeared automatically when you opened a work item. After our move to Forge, the panel is hidden by default due to platform limitations.

- Admins can make the SLA panel visible by default. For instructions, refer to the [documentation](/cms_trial/space/TTSC/2513797296/Changes+after+the+Forge+migration/).
- Users can open the SLA panel manually by clicking the **Time to SLA** button on the work item view.

The SLA panel is your real-time view of how well your team is meeting your service level agreements. Watch as the panel changes color to reflect the status: blue for on track, yellow for at risk, and red for overdue. Learn more about [how the SLA panel works](/cms_trial/space/TTSC/35815658/SLA+panel/) and how you can customize it.

![An SLA panel created by Time to SLA for Jira Cloud on the Jira work item view.](/cms_trial/assets/7eaa5751-e108-460a-80b9-7ae31a3477e2.png)

To see the SLA panel on your existing work items, you must [recalculate your SLA data](#)**.**

Having problems? Here are quick solutions:

- [Why don’t I see the SLA panel on my work items?](/cms_trial/space/TTSC/34932181/FAQ%3A+SLAs/)
- [Why isn’t my SLA starting?](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/edit-v2/34932181#Why-isn%E2%80%99t-my-SLA-starting%3F)
- [Why is my SLA panel showing incorrect data?](/cms_trial/space/TTSC/34932181/FAQ%3A+SLAs/)

### Step 5: Configure SLA actions

By default, newly created SLAs include two [SLA actions](/cms_trial/space/TTSC/35881090/Actions/) that send notifications when 50% and 75% of the SLA time has elapsed. You can edit these actions, remove them, or [create additional actions](/cms_trial/space/TTSC/3308945429/Create+actions/) such as triggering Jira automation, add comments, change an assignee, update Jira fields, or change priority.

Video script

When an SLA needs attention, your team shouldn’t have to chase the next step.

With SLA actions in Time to SLA, you can define that next step in advance, whether that’s sending a notification, triggering Jira automation, or updating a work item.

In this video, we’ll show you how the **Actions** page gives you one place to create, track, and manage those steps.

On the Actions page, you can quickly see what each action does, which SLA it applies to, which goals it uses, what triggers it, and whether there’s execution history available for review.

You can also use search and filters to find exactly what you need.

Filter actions by SLA or action type, show disabled actions, and customize which columns appear in the table.

This makes it easier to track how SLA notifications and automations are configured across your instance.

When you create an SLA action, you choose what the action should do.

An action can send an email, post a Slack message, trigger Jira automation, change the assignee, add a comment, change the status, update a Jira field, or change the priority.

Then, you decide where and when the action runs. It can apply to a single SLA or to all SLAs.

You can apply it to all goals or only selected goals, then choose the SLA event that triggers the action; for example, when the SLA reaches a certain percentage, is about to breach, or has already breached.

If you only want the action to apply from a certain date, enable this option and choose an **Effective From** date. This prevents the action from running for older work items that match the conditions.

You can also combine multiple action types in the same setup.

For example, when an SLA breaches, a single action can send an email, post a Slack message, change the priority, and assign the work item to another user.

This helps teams respond faster without creating separate configurations for each step.

Let’s say your Time to resolution SLA breaches.

You can create an action that notifies the incident manager by email, sends a Slack message to the support channel, changes the priority to Highest, and assigns the work item to a senior team member.

With SLA actions, your team can manage notifications and SLA-driven updates from one place.

Use the **Actions** page to define how your team responds to SLA events, before they become bigger problems.

See [**Actions**](/cms_trial/space/TTSC/35881090/Actions/) for the available triggers and action types.

### Step 6: Monitor performance with reports and dashboards

Time to SLA offers multiple tracking options. You can monitor time durations, compare SLAs, and gain valuable insights to ensure you’re always on track.

Use **SLA History** on a Jira work item to review the events recorded for an SLA, such as start, pause, resume, reset, breach, extension, and stop events.

![The SLA History tab of Time to SLA for Jira Cloud on the Activity section in Jira work item view.](/cms_trial/assets/388e7a08-1ac1-495f-9202-d11aec89f1e5.png)

Want to dive deeper? Use the [reports](/cms_trial/space/TTSC/36012079/Reports/) to monitor service performance over time. These insights help you identify trends and make data-driven improvements.

![image-20260707-215831.png](/cms_trial/assets/8cecae1c-f190-45b4-b403-8f44095be94b.png)

Want a quick overview of SLA performance? Add the [SLA gadgets](/cms_trial/space/TTSC/181436799/Gadgets/) to your Jira dashboard.

![The TTS - Periodic Met vs Exceeded SLA gadget on the Jira dashboard. ](/cms_trial/assets/a5ed80f9-dc0f-44c4-929f-fc9ddaf68edf.png)