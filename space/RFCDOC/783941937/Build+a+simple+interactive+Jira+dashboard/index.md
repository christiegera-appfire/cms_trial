# Build a simple interactive Jira dashboard

## Overview

By the end of this tutorial, you will know how to build a simple Jira dashboard with two interactive gadgets: a Rich Filter Controller gadget and a Rich Filter Results gadget. You can filter the work items that the Rich Filter Results gadget displays by clicking buttons (static filters) in the Rich Filter Controllergadget.

![simple board.png](/cms_trial/assets/6c86ef57-45a0-417a-9288-2dd929827fb0.png)

## Before you start

- Make sure you have created a rich filter. For instructions, see the [Create and access rich filters](/cms_trial/space/RFCDOC/783941927/Create+and+access+rich+filters/) tutorial.

## Add static filters to the rich filter

1. Open the configuration page of your rich filter as described in the [Create and access rich filters](/cms_trial/space/RFCDOC/783941927/Create+and+access+rich+filters/) tutorial.
2. Click the **Static filters** tab.

   ![static filter.png](/cms_trial/assets/95d980b4-9e64-465b-8372-15c45e9e7a46.png)
3. Click **Create static filter** and define two static filters:

   - **Closed** withJQL query: `status = Closed`
   - **Assigned to me** withJQL query: `assignee = currentUser()`

     ![contentId-783941937](/cms_trial/assets/f2e12932-4e19-4abd-acd6-6ac1208dbc24.png)
4. Click **Create**.

## Build the dashboard

1. To create a new [Jira dashboard](https://support.atlassian.com/jira-work-management/docs/what-is-a-jira-dashboard/), click **Dashboards** under Jira navigation.
2. Click **Create dashboard**.

   ![Create Dashboards.png](/cms_trial/assets/f274b90f-a7e3-442a-94d1-d2ceaf686fff.png)
3. Fill in the fields in the dialog and click **Save.**

   1. Choose a name and a description for your dashboard
   2. Choose who can see and edit your dashboard

      ![The Create dashboard window.](/cms_trial/assets/c272065d-f535-4e79-97d9-178a1d1a9ab4.png)
4. You can add a Rich Filter Results gadget to the dashboard by clicking **Add gadget** at the top right of the screen.

In the *Add a Gadget* dialog, simply type `Rich` in the **Search** field to easily find the gadgets provided by the Rich Filters for Jira Dashboards app.

1. In the configuration form of the Rich Filter Results gadget, select your rich filter.   
   You don't need to change anything else for now.

   ![Rich filter results window with the Submit button clicked.](/cms_trial/assets/0c480656-ae90-40ce-8920-4b71a19571d8.png)
2. Click  **Submit**.

The Rich Filter field provides a search function to easily find your rich filter by typing only a part of its name.

## Rich Filter Controller

Add a Rich Filter Controller gadget to the same Jira dashboard.

1. In the configuration form of the Rich Filter Controller gadget, select the same rich filter as in the Rich Filter Results gadget.   
   You don't need to change anything else for now.

   ![Rich filter gadget with the Show all filters option selected.](/cms_trial/assets/dee8a689-f65f-4a1f-b66a-8f463b9cd324.png)
2. Click **Submit**.

The **Rich Filter Controller** gadget displays the two static filters defined in your rich filter.

- They are displayed as on/off buttons that can be independently activated and deactivated simply by clicking them.
- When you activate or deactivate a static filter, the **Rich Filter Results** gadget is updated to display the issue collection obtained by applying the Jira base filter of the rich filter, combined (`AND`ed) with the JQL queries of the active *static filters*. For example, if you click **Closed** static filter*,* the *Rich Filter Results* gadget will be updated to display only the closed issues among those returned by the Jira base filter.

  ![simple board.png](/cms_trial/assets/6c86ef57-45a0-417a-9288-2dd929827fb0.png)

You can change the order of the **static filters** in the rich filter configuration. In each Rich Filter Controller gadget, you can use this default order or customize the list of filters to be displayed by selecting the ones you want and placing them in the order you want.

## Learn more

To learn more about *static filters*, look at [Configuring Static Filters](/cms_trial/space/RFCDOC/783941703/Configure+static+filters/).

To learn how to customize the display of the issues in your Jira dashboard, continue to the tutorial [Define views for your dashboard](/cms_trial/space/RFCDOC/783941943/Define+views+for+your+dashboard/).