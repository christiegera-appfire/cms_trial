# Get started with Rich Filters for Jira Dashboards for Cloud

**Rich Filters for Jira Dashboards has been developed and deployed on Atlassian Forge, Atlassian’s most advanced cloud development platform.**

See our [documentation](https://support.appfire.com/space/RFCDOC/3171189121) or contact [support](https://support.appfire.com/page/support) for help.

This article provides newcomers to the [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) app with a rapid introduction, explaining what it is and can do, how to access it, and how to use it to create a simple dashboard.

## Prerequisites

- Access a Jira instance with the [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) app installed.
- One or more existing [Jira filters](https://support.atlassian.com/jira-software-cloud/docs/save-your-search-as-a-filter/) will be a base for your rich filters
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql)

Rich filters are free to try for 30 days; after that, the subscription cost scales based to user tier. See our [pricing information](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=pricing) for more details.

## Why should I use Rich Filters for Jira Dashboards?

Whether you're a casual user or an expert, you'll agree that Jira can sometimes be cumbersome and hard to handle, especially as your querying and reporting needs get more complex. You start to work with larger teams with diverse user requirements.

**Rich Filters for Jira Dashboards** lets you take control of your Jira. It provides a powerful and flexible toolset for generating custom data views and reports, delivered in a user-friendly, intuitive package. You can replace multiple Jira dashboards with a single, rich, filter-powered dashboard, keeping all your functionality in one place and drastically improving productivity.

![Dashboard overview](/cms_trial/assets/94cfd9b9-fcf8-446f-9045-c2728c0a5078.png)

Key features include:

- Simple and complex filters are combined to generate precise real-time data views.
- Multiple views for different requirements and job roles.
- Several gadgets for sophisticated reporting include charts, gauges, statistics, and metrics.
- Multidimensional data insights with numeric & time-tracking fields, averages & other formulas, and custom values and ratios.
- Intuitive UI that allows easy editing, reordering, and color-coding.

This content is written for the Cloud version of Jira. A separate resource covers rich filters for the Jira Data Center.

## The final result of this tutorial

When you've worked through all the steps in this tutorial, you should have a dashboard that includes:

- A Rich Filter Controller gadget includes two filter buttons to filter the issues in your dashboard.
- A Rich Filter Results gadget to display the list of issues.

![Closed static filter](/cms_trial/assets/cbfdde17-a4f9-4329-955a-97e4c4c831b5.png)

## Create and access rich filters

A rich filter is an intelligent layer that sits on top of a basic Jira filter and provides advanced options for filtering and displaying the issues it returns. Let's examine how to access rich filters and create your first one.

1. Once Rich Filters for Jira Dashboards is installed on your Jira instance, you can start to use it by selecting **Apps > Rich Filters** from the Jira menu.

   ![Rich Filters under Apps](/cms_trial/assets/ca4b0793-ebfd-4acb-bea5-a85d1bc61703.png)
2. You should now be on the Rich Filter **Home** screen. Click **Create rich filter**.

   ![Create rich filter](/cms_trial/assets/dbebb68c-1128-4417-a86c-c84255242174.png)
3. In the resulting dialog box, enter a name for your rich filter and choose an existing Jira filter to base it upon.

   ![Create_rich_filter.png](/cms_trial/assets/55d11b92-dd3e-4ad6-a6f0-0d083c4e7cbc.png)

You need the right to view the selected Jira filter, but you don't need to be its owner.

1. Click **Create**.   
   This creates the rich filter and relocates you to the **Details** screen.
2. (Optional) Add the **Description** and the **Administrators** of the filter, and click **Submit**.

   ![Details tab](/cms_trial/assets/dc334282-4d81-4318-9606-412ae3c2b8c3.png)

You can access your rich filters anytime by selecting **Apps > Rich Filters** from the main menu. They'll be listed there.

## Create a simple dashboard

1. From the Jira menu, select **Dashboards**and click**Create dashboard**.

   ![Create Dashboards](/cms_trial/assets/bf4cddfe-73bf-4e0e-965b-4c30fefa2f41.png)
2. In the **Create dashboard** dialog box, enter a **Name** for your dashboard and click **Save**.  
    You'll be relocated to the dashboard configuration screen.

   ![Rich filter dashboard](/cms_trial/assets/d10a2b48-08ed-4b40-99ff-2ca45310a168.png)
3. Here, you can add gadgets to your dashboard. The two types of rich filter gadgets you are currently interested in are:

   1. **Rich Filter Results gadgets** to display your work items.
   2. **Rich Filter Controller gadgets** to filter the display of data in your rich filter gadgets.
4. Add a **Rich Filter Results** gadget:

   1. Start typing `Rich Filter Results` in the **Add a Gadget**side panel search box to filter for the gadget you want, and click its **Add** button.
   2. In the *Rich Filter Results* gadget you just added, select your rich filter from the dropdown menu at the top for now.
   3. Click **Submit** to save it (we'll cover the other options available here in other tutorials).

      ![Rich Filter Result](/cms_trial/assets/4aff5e13-77d4-491a-9038-a4d5e698e920.png)
5. Add a **Rich Filter Controller** gadget in the same way as above.

   1. Again, once you've added your gadget, select your rich filter in the **Rich filter** dropdown and click **Submit**.
6. You can drag the *Rich Filter Controller* gadget into the left-hand column of the dashboard and the *Rich Filter Results* gadget into the right-hand column.
7. If you want your dashboard layout to look exactly like ours, select the **Left sidebar**layout from the **Change layout**menu at the top of the dashboard.

   ![Change layout for dashboards](/cms_trial/assets/6302d6e3-1a2d-4438-9793-b2614492e7b7.png)

At this point, you should have a dashboard in edit mode with two gadgets inserted.

![example of a dashboard in edit mode with two gadgets inserted](/cms_trial/assets/80391f32-36bd-4537-9fb9-91c03c5edb88.png)

- If you navigate elsewhere, you can find your way back to your dashboard by selecting your dashboard name from the *Dashboards* menu.
- You can get back to the configuration form for each gadget by selecting **Configure gadget** from the **Menu** (▢ ) in the bottom of the gadget.

Once you have finished experimenting with your configuration settings, click **Done** to exit dashboard edit mode.

If you don't see any work items displayed on your dashboard, make sure the Jira filter you selected to base your rich filter on returns work items on the **Search work items** screen.

If you are doing a lot of rich filter configuration work, you can easily switch between the two by keeping your dashboard open in one tab and the rich filter configuration screen open in another.

Before moving on, it is worth discussing sorting tables in rich filters. By default, the display order of the list of issues in the Rich Filter Results gadget is defined by the base Jira JQL filter on which the rich filter is based. You can change the sorting by clicking on a table header to sort by that column. Click the header multiple times to toggle between ascending and descending — the relevant arrow next to the column name will be highlighted to remind you whether the sorting is currently ascending (up arrow) or descending (down arrow).

For example, the image below shows the list sorted in descending order by **Summary**.

![Summary sorting](/cms_trial/assets/2f68a2cf-7098-416a-8c98-bc4036e5fbac.png)

These sorting controls are standard in any table in rich filters for all sortable fields.

## Add some static filters to your controller

At this point, your dashboard should be working fine, but it isn't *doing* much right now:

1. The Rich Filter Results gadget shows a basic view of the list of issues returned by the Jira filter you configured.
2. By default, the Rich Filter Controller gadget lets you type in JQL queries to filter the data displayed in the Rich Filter Results gadget.

   1. Try typing in a simple query like `status = Closed` and click **Apply**.
   2. You can reset the query by clicking the **X** button at the bottom-right corner of the controller. This button clears all filters currently applied.

      ![Clear all quick filters](/cms_trial/assets/cacc3002-373a-4394-9f62-500323f6943d.png)
3. To make filtering more flexible, you can add **static filters** to the controller that apply your JQL. Static filters are buttons in the Rich Filter Controller gadget and allow you to toggle JQL queries on and off, using them on top of your base filter. You can use multiple filters at the same time.

In this section, you will add two static filters to your controller.

1. Go back to your rich filter **Details** screen.
2. Select the **Static Filters** tab.
3. Click **Create static filter**.

   ![Static filters tab](/cms_trial/assets/eff2aac6-36be-43d9-9e54-16e97cb5db64.png)
4. In the *Create a static filter* dialog box, fill in the details:

   - **Name:**  `Closed`
   - **JQL**: `status = Closed`

     ![Create a static filters](/cms_trial/assets/81ed72df-18f8-4e8f-82ce-6d492ea0eacd.png)
5. Click **Create**
6. Create another static filter in the same manner with:

   - **Name:**  `Assigned to me`
   - **JQL**: `assignee = curentUser()`
7. Go back to your dashboard.
8. **Refresh** your dashboard using the Rich Filter Controller gadget's **Optimized refresh** (▢)button, available in the bottom-right corner.

   ![contentId-783942462](/cms_trial/assets/987a02b2-f500-417d-80e3-c7c16e6af6ef.png)

The **Optimized refresh**  (▢) button refreshes all rich filter gadgets based on the same rich filter as the controller without reloading everything like the default Jira refresh controls. This is especially useful if you go to your rich filter configuration screen, make changes, then go back to your dashboard and want to refresh all your gadgets instantly.

1. You'll now see the static filters you created available as buttons in the **Rich Filter Controller** gadget. Try toggling them on and off and see how the issue list updates in real-time. Note also how, when you hold the pointer over the filters, you get a tooltip showing the exact JQL query that powers each one.

   ![Closed static filter](/cms_trial/assets/cbfdde17-a4f9-4329-955a-97e4c4c831b5.png)

You can change the order of the static filters in the rich filter config screen.

1. Go back to your rich filter and select **Static Filters***.*
2. Drag the static filters up and down the list to change the order (you can also Tab to the filter to focus it, press Space, and then use the up and down cursor keys to adjust its position).
3. Return to your dashboard and click the **Optimized refresh** (▢) button in the controller. The filters will appear in the controller in the same order as in the *Static Filters* screen list.

When working with Rich filters, you can always find help and resources under the **App menu** (▢):

- **Gadget documentation** - takes you to the gadget documentation page
- **Contact support -** takes you to the Appfire Atlassian support site
- **Download support file** - downloads a text file with the gadget details
- **About Rich Filters** - takes you to the Marketplace Rich Filters for Jira Dashboards site

![2026-02-10_10-37-43.png](/cms_trial/assets/9c07a721-1af0-48ab-b442-4747fc895373.png)

## Next steps

You can work through the [Tutorials](/cms_trial/space/RFCDOC/783941917/Tutorials/) articles in order, but each one works as a standalone topic, so you can jump to specific topics of interest if that suits you better.

You can use the rich filter you created in this article as a starting point for other tutorials.