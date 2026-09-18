# Get started with Rich Filters for Jira Dashboards for Cloud

This article gives newcomers to the [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) app a quick introduction, explaining what it is and can do, how to access it, and how to use it to create a simple dashboard.

## Before you start

Make sure that you have:

- Access to a Jira instance with the [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) app installed.
- One or more existing [Jira filters](https://support.atlassian.com/jira-software-cloud/docs/save-your-search-as-a-filter/) will be a base for your rich filters
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql)

## Why should I use Rich Filters for Jira Dashboards?

**Rich Filters for Jira Dashboards** lets you take control of your Jira. It provides a powerful and flexible toolset for generating custom data views and reports, delivered in a user-friendly, intuitive package. You can replace multiple Jira dashboards with a single, rich, filter-powered dashboard, keeping all your functionality in one place and improving productivity.

## The final result of this tutorial

When you've worked through all the steps in this tutorial, you should have a dashboard that includes:

- A Rich Filter Controller gadget includes two filter buttons to filter the issues in your dashboard.
- A Rich Filter Results gadget to display the list of issues.

## 1. Create rich filters

A rich filter is a smart layer on top of a regular Jira filter that gives you extra options for filtering and displaying issues.

1. From the Jira menu, select **Apps > Rich Filters**.

   ![Rich Filters under Apps](/cms_trial/assets/ca4b0793-ebfd-4acb-bea5-a85d1bc61703.png)
2. On the Rich Filter Home screen, click **Create rich filter**.

   ![Create rich filter](/cms_trial/assets/dbebb68c-1128-4417-a86c-c84255242174.png)
3. Enter a name, and choose an existing Jira filter to base it on (you need view access, not ownership).
4. Click **Create**.

![Details tab](/cms_trial/assets/dc334282-4d81-4318-9606-412ae3c2b8c3.png)

## 2. Create a simple dashboard

1. From the Jira menu, select **Dashboards**and click**Create dashboard**.

   ![Create Dashboards](/cms_trial/assets/bf4cddfe-73bf-4e0e-965b-4c30fefa2f41.png)
2. In the **Create dashboard** dialog box, enter a **Name** for your dashboard and save it.

   ![Rich filter dashboard](/cms_trial/assets/d10a2b48-08ed-4b40-99ff-2ca45310a168.png)
3. In the **Add a Gadget** panel, search for **Rich Filter Results**, add it, select your rich filter from its dropdown, and click **Submit**.

   ![Rich Filter Result](/cms_trial/assets/4aff5e13-77d4-491a-9038-a4d5e698e920.png)
4. Add a **Rich Filter Controller** gadget the same way. Search for it, add it, select the same rich filter, and click **Submit**.
5. Click **Done** to exit the edit mode.

![example of a dashboard in edit mode with two gadgets inserted](/cms_trial/assets/80391f32-36bd-4537-9fb9-91c03c5edb88.png)

## 3. Add some static filters to your controller

1. Go back to your rich filter **Details** screen.
2. Select the **Static Filters** tab.
3. Click **Create static filter**.

   ![Static filters tab](/cms_trial/assets/eff2aac6-36be-43d9-9e54-16e97cb5db64.png)
4. In the *Create a static filter* dialog box, fill in the details:

   - **Name:**  `Closed`
   - **JQL**: `status = Closed`
5. Click **Create**
6. Create another static filter in the same manner with:

   - **Name:**  `Assigned to me`
   - **JQL**: `assignee = currentUser()`
7. Go back to your dashboard.
8. Refresh your dashboard with the **Optimized refresh** (▢)button.

   ![contentId-783942462](/cms_trial/assets/987a02b2-f500-417d-80e3-c7c16e6af6ef.png)

You'll now see the static filters you created available as buttons in the **Rich Filter Controller** gadget. Try toggling them on and off and see how the issue list updates in real-time.

![Closed static filter](/cms_trial/assets/cbfdde17-a4f9-4329-955a-97e4c4c831b5.png)

## Next steps

You can work through the [Tutorials](/cms_trial/space/RFCDOC/783941917/Tutorials/) articles in order, but each one works as a standalone topic, so you can jump to specific topics of interest if that suits you better.

You can use the rich filter you created in this article as a starting point for other tutorials.