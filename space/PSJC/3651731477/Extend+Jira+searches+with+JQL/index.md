# Extend Jira searches with JQL

Power Scripts adds JQL keywords that let you search Jira using criteria that aren't available with standard JQL. Enable the Link keywords and use `countOfLinks` to find work items based on whether they're linked to other work items.

**Estimated time:** 5 minutes

## Before you begin

Make sure you have:

- Power Scripts for Jira Cloud installed.
- A Jira project that contains some work items with links to other work items.

## Enable JQL standard keywords

First, enable the Power Scripts JQL keywords you want to make available in Jira.

1. Go to **Power Scripts** > **Configurations** > **Automations** > **JQL**.
2. When the *SIL JQL* page opens, select **Standard Keywords**.
3. Enable the JQL keyword categories you want to synchronize. For this example, select the Link category so you can use the `countOfLinks` keyword.
4. Click **Save**.

![PS-standard-keywords.png](/cms_trial/assets/592cf10f-fa72-4176-bf6f-fdfd0127be59.png)

## Synchronize Jira data

Power Scripts needs to synchronize Jira data before its standard JQL keywords can return results. You can select which projects Power Scripts synchronizes so that it only processes the Jira data you need.

1. While still on the SIL JQL page, select the **Synchronization** tab.
2. Click **Add projects and categories** and select the projects and categories you want to use.
3. Click **Save & Synchronize** to start the synchronization.
4. Wait for the synchronization to finish successfully.

![PS-synchronize.png](/cms_trial/assets/d973d1db-c481-417b-b2c1-3fb1a9def74b.png)

The Power Scripts JQL keywords can now use data from the synchronized project.

With Auto-Synchronization enabled, if you don’t select a project, auto-synchronization runs globally. This requires more time and consumes more resources. It is recommended to select only the projects you need.

## Run an extended JQL search

Now use a Power Scripts JQL keyword in Jira.

1. Go to the Jira project you selected in the synchronization.
2. In the left-side menu under Filters, click **Search work items**.
3. Confirm the search is set to **JQL**.
4. Enter: `countOfLinks > 0`. `countOfLinks` is a Power Scripts JQL keyword that can help determine if a work item has one or more links.
5. Run the search.

Jira returns work items in the synchronized project that have one or more work item links.

## Try another search

Change the JQL query to: `countOfLinks = 0`

Run the search again. Using `countOfLinks` in this context searches for Jira work items without links.

You've enabled Power Scripts JQL keywords, synchronized Jira data, and used a JQL keyword to search for specific work items.

## Watch the video

Watch **Advanced JQL keywords** to see the complete process.

## Next steps

Explore the [JQL Support](/cms_trial/space/PSJC/490997937/JQL+Support/) feature guide to learn about the other JQL keywords available with Power Scripts and how to manage synchronization.

Explore the [Feature guides](/cms_trial/space/PSJC/490996521/Feature+guides/) to learn about other ways Power Scripts can automate and customize Jira.