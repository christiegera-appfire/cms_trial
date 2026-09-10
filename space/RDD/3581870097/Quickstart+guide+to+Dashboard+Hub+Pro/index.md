# Quickstart guide to Dashboard Hub Pro

## Create your first dashboard in minutes

This page walks you through the setup step by step, from an empty dashboard to a shared view of your important Jira data. This example uses three gadgets. You can use any gadget that is compatible with your datasource, or a utility gadget, like Rich Text, that doesn’t need source data.

**Before you begin**: A Jira administrator installs Dashboard Hub Pro on a Jira instance. The instance it's installed on is the **default datasource**, so your data is ready to use with no setup, and any user can complete the steps below without administrator permissions. See [Installation](/cms_trial/space/RDD/2146336847/Installation/) if it isn't set up yet.

---

## Step 1: Open Dashboard Hub

In the left sidebar in Jira, select **Apps** > **Dashboard Hub**. This is the home for all your dashboards, where you'll view, create, and manage them.

---

## Step 2: Create a blank dashboard

**Why create from scratch?** You can start from a **template**, but some templates pull data from other tools like Bitbucket or Statuspage, which you need to connect first. Building from scratch on your default Jira datasource is the quickest way to a working dashboard.

1. Option A: If this is the first time you open Dashboard Hub, click **Create dashboard** on the *Get started* page.  
   Option B: In Dashboard Hub, click **More actions** (**…**) in the top right, then select **Create dashboard**.
2. Enter a name for your dashboard, for example, `My first dashboard`.

---

## Step 3: Add gadgets

**Concept · Gadget.** A gadget is a single chart, table, or report on your dashboard. You can choose from over 90, and we regularly add new ones.

1. Click **Add gadget** at the top of the dashboard, or **Browse all**.

   ![DH-MyFirstDashboard.png](/cms_trial/assets/0ad2b739-5515-43a5-a554-bc82002bf4bf.png)
2. Click **Select multiple** to add more than one gadget at a time.
3. Select **Show only compatible datasource** to ensure only compatible gadgets are available.

   ![DH-New dashboard selected toggles.png](/cms_trial/assets/c882c14a-44a9-4d27-bea0-dc56ca29c8ae.png)
4. Select two or three gadgets, depending on the data you want to visualize. In this example, we select Jira Custom Charts, Progress Tracker, and Rich Text.

Most gadgets use JQL queries or saved filters to determine the work items used to build the report.

1. Click **Add gadgets**.

---

## Step 4: Choose the data to display

You configure each gadget's visualization, even when you start from a template.

Most gadgets have two parts to configure: *what it shows* (the data) and *how it looks* (the visualization). Complete both parts for each gadget on the dashboard.

1. Click **Config** on the Jira Custom Charts gadget. This is the most versatile gadget.
2. The gadget name displays by default, but you can change it so it is more meaningful to you and your team.
3. Your data is already connected. The instance where Dashboard Hub is installed is your default datasource, called **This Jira instance**.

**Concept · Datasource.** A datasource is where a gadget gets its data. Dashboard Hub automatically reads the Jira site it's installed on, so you don't need to set anything up to get started. Want data from somewhere else later, like another Jira site, BigPicture, Bitbucket, or somewhere else through any REST API? You can add more datasources anytime, but you don't need to right now.

1. If your instance has a large number of work items or spaces, you can add a JQL query or select a saved JQL filter to narrow the number of work items to load; query a specific work type, assignee, or space, for example, `project = Birch`.
2. Click **Load**.

   ![DH-My First dashboard-custom charts.png](/cms_trial/assets/e56f5cb6-6e31-46a3-8eb4-0067ffabf28f.png)

---

## Step 5: Choose how to view the data

1. **View Type**: Depending on the selected gadget, you have different visualization options. For the Jira Custom Charts gadget in this example, select **Pie Chart**.
2. **Chart By**: Choose how to segment the data. Here, we use **Issue Type**.
3. Keep the default **Aggregation Field** and **Aggregation** options.
4. (optional) If you want to include a statistic in the rendered gadget, select an option under **Show statistics**. In this example, we select **Total Work Items**.
5. A preview of the rendered data displays. When you are happy with the visualization, click **Save**.

   ![DH-Get-started-pie.png](/cms_trial/assets/6833e922-e77d-452f-b8a3-039acfaa61b1.png)

---

## Step 6: Configure the remaining gadgets

You can skip this step if you want to move directly to viewing a saved dashboard with only one gadget.

### **Progress Tracker**

The Progress Tracker gadget can display progress at the Epic, Theme, and Initiative level, or other work types by different estimation statistics.

1. Follow the instructions in Step 4, using a JQL query that matches your instance.

   ![DH-Get-started-progress-tracker.png](/cms_trial/assets/2dc2e535-fabb-4dfd-9868-889a45de9cdc.png)
2. Select the start and end date fields, for example **Created** and **Resolved**, or use custom fields.
3. Select the metric to use to calculate progress, for example, **Work Item Count**.
4. Choose the view type: **List** or **Extended**.
5. Click **Save**.

### **Rich Text**

The Rich Text gadget is a utility gadget that doesn’t require a datasource. Use it to provide contextual information to your dashboards, such as a team and project description, what reports are included, or how to customize view with adaptive filters. The rich content supports formatted text, links, emojis, lists, images, and videos.

1. Click **Config**.
2. Add the content that you want to display on your dashboard.
3. Click **Save**.

---

## Step 7: Save the dashboard

When you are ready, click **Save** in the top right of the dashboard. The new dashboard displays.

![Screenshot 2026-08-27 at 15.29.47.png](/cms_trial/assets/2c848273-95d9-4057-ae2b-868ec076b961.png)

---

## Step 8: Share it with your team

You’ve created a dashboard that shows your team’s key metrics; now you want to share it. You can share a dashboard in a few ways, depending on the access viewers have to the data: share the dashboard with an internal link, create a public link, export it to PDF or PNG, or create a subscription. In this example, we will subscribe to the dashboard to receive snapshots on a set schedule.

1. At the top of the dashboard, click **Share dashboard** > **Subscribe to dashboard**.
2. Create the schedule:

   1. Select the frequency and time
   2. You are subscribed by default as the subscription creator. Select additional recipients (users or groups) if needed.
   3. (optional) Set a password if you want to add password protection to the emailed snapshot.

      ![DH-Get-started-subscribe.png](/cms_trial/assets/11b24376-084e-4a80-9a06-faa69a4b8ea6.png)

## Tips

|  |  |
| --- | --- |
| **Save time when configuring multiple gadgets** | Want your reports to represent the same underlying data? Select the **Use these settings to configure empty compatible gadgets** option when you configure a gadget. |
| **Reuse dashboards** | You configured a dashboard for one team; clone it and use **Bulk Update JQL** to change the underlying data for all compatible gadgets. |
| **Your established Jira dashboard is missing key metrics** | Use Dashboard Hub gadgets in native Jira dashboards. They are available in the *Add a gadget* panel. |
| **Try project dashboards** | Project dashboards give teams instant visibility into space-specific reports. These dashboards are populated with gadgets tailored to the space type, including dedicated dashboards for Jira Software and Jira Service Management.  The first time you open Dashboard Hub from a space, the app automatically creates and loads the dashboard in the **Dashboard Hub** tab. The space owner is assigned as the default dashboard owner. |
| **Customize the look and feel of a dashboard** | You can rearrange and resize individual gadgets in the dashboard. Most gadgets let you customize default colours and reorder or hide statistics and metrics. |

## Next steps

You created your first dashboard and shared it with your team. What’s next?

- [Explore our catalog of over 90 gadgets](https://support.appfire.com/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics)
- [Learn about connection types and datasources](https://support.appfire.com/space/RDD/146309943/Learn+about+datasources)
- [Understand dashboard permissions](https://support.appfire.com/space/RDD/146309693/Dashboard+permissions)
- [Customize dashboard adaptive filters](https://support.appfire.com/space/RDD/146309549/Adaptive+Filters)
- Learn more about the gadgets used in this example

  - [Jira Custom Charts](https://support.appfire.com/space/RDD/146309431/Jira+Custom+Charts)
  - [Progress Tracker](https://support.appfire.com/space/RDD/146309546/Progress+Tracker+-+Epics,+Themes,+and+Initiatives)
  - [Rich Text](https://support.appfire.com/space/RDD/146309606/Rich+Text)