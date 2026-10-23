# Organize issues with hierarchies in Jira dashboards

Hierarchies let you visualize issues organized according to their parent-child relationship. Instead of a flat list, issues appear in a collapsible tree structure that preserves parent-child relationships across multiple levels. Each hierarchy defines which issues are included, with a hierarchy level range and an optional JQL query. You can display hierarchies in the *Rich Filter Results* gadget. Each hierarchy can use one or multiple [views](/cms_trial/space/RFCDOC/783941729/Configure+views/) to display its issues.

In this article, you will learn how to add hierarchies and see how hierarchies interact with views and your dashboard gadgets.

Watch the video guide to organize issues with hierarchies:

For this tutorial, we use a Jira Premium instance, which (like the Enterprise plan) lets you have more than three levels in the Jira issue type hierarchy (Jira Standard has a three-level limit). You can learn more here: [Understanding Jira Hierarchy](https://community.atlassian.com/forums/App-Central-articles/Understanding-Jira-Hierarchy-Complete-Guide-in-2025/ba-p/2947722).

## Before you start

Make sure you have:

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942658).
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql).

## Final result

Once you've worked through the steps in this tutorial, you should have a dashboard that contains two rich filter gadgets:

- A Rich Filter Controller gadget.
- A Rich Filter Results gadget displaying issues organized across three hierarchy levels.

  ![Rich Filter Results gadget ](/cms_trial/assets/3eac0f28-57aa-45a1-bf60-4c585d4ebaba.png)

## Rich filter and dashboard basic setup

In this section, you can set up a basic rich filter and dashboard.

If you've already worked through other [Tutorials](/cms_trial/space/RFCDOC/783942482/User+guides/), you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942658) to create a new rich filter before continuing.

1. Create a new dashboard (**Dashboards** > **Create dashboard**).
2. Use the **One column** layout. You can select it using the **Change layout** menu at the top of the dashboard.
3. Add a **Rich Filter Results gadget** and a **Rich Filter Controller** gadget, both based on your rich filter (see also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
4. Save your gadget configuration.

## Set up hierarchies

Let's set up two hierarchies:

- **Execution**: for a developer team that wants to see the epics and all stories and subtasks related to them, excluding support requests.
- **Strategy**: for higher management to view only initiatives, epics, and their stories, without the subtask level.

1. Open your rich filter configuration.
2. Select **Lists** > **Hierarchies** tab and click **Create hierarchy**.

   ![ Create hierarchy](/cms_trial/assets/c4b769de-2a67-4011-bbd3-e559c0061cb1.png)
3. In the *Create a hierarchy* dialog, enter the following details and click **Create**.

   - **Color**: Purple (use different colors to tell hierarchies apart at a glance)
   - **Name**: *Execution*
   - **Hierarchy structure**: Keep the default level names.
   - **Include levels**: Select the levels you want to include:

     - **From**: Epic
     - **To**: Story
   - **JQL**: `issuetype != "Service Request"`
   - **Views**: Show all views

     ![Create a hierarchy](/cms_trial/assets/455966ca-368b-4e66-83f6-af487d469de7.png)
4. In the same way, create a second hierarchy called *Strategy*.

   - **Color:** Blue
   - **Name:** *Strategy*
   - **Hierarchy structure**: Keep the default level names.
   - **Include levels**: Select the levels you want to include:

     - **From**: Initiative
     - **To**: Story
   - **Views**: Show all views

     ![Strategy hierarchy example](/cms_trial/assets/3e6a460b-dd67-44bd-83c1-6ce8639ecfb6.png)

The **Hierarchies** tab now summarizes your new hierarchy details. You can edit or delete them at any time using the **Edit** (▢) and **Delete** (▢) buttons at the end of each row.

## Display your hierarchies

Once you define your issue hierarchies, your Rich Filter Results gadget can display issues in a collapsible tree structure based on the parent-child relationships.

1. Open the configuration form of your **Rich Filter Results** gadget.
2. In the **Display** section, select the **Configured list** option.
3. Under **Configured list**, select **Show all**.

   ![Rich Filter Results gadget configuration](/cms_trial/assets/db643899-aef7-4267-b668-c6dfaffc1d22.png)
4. Click **Submit** to save.
5. Refresh your dashboard.

   You should now see your two hierarchies, each color-coded, with issues organized into levels within each.

   ![two hierarchies](/cms_trial/assets/97628c10-5acd-4b89-9956-e60fd400559c.png)

There are a few things worth noting about the hierarchy display:

- The issues in the hierarchy scope appear in a collapsible tree, with each issue placed under its parent. Issues without a parent in the hierarchy scope are grouped under a node named after the level. For example, a story without a parent appears under the *Story* node.
- You can expand/collapse each node by clicking the corresponding caret. The **Maximum issues** setting in the gadget configuration determines how many issues are loaded at a time. You can load more issues by clicking **Load more…**.
- Each node displays child counts. These counts correspond to children in the hierarchy scope, regardless of whether they are currently loaded and displayed in the gadget.
- Hierarchies respond to the quick filters applied in the controller, but don't show only the matching issues; they also show all issues related to matching issues (ancestors, siblings, etc.), to preserve the hierarchy structure and context. The matching issues are highlighted with a blue vertical line on the left of the row and are placed before non-matching issues.

## Assign views to hierarchy levels

You can show different views for the hierarchies.

First, create some views:

1. Go to the **Views** tab of the rich filter configuration screen.
2. Create two views (see [Customize issue views and gadget scope](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) for a full guide):

   - **Devs**: Include the columns *Issue Type, Key, Summary, Assignee, Fix Versions*, and *Status*.
   - **Manage**: Include the columns *Issue Type, Key, Priority, Summary, Story Points*, *Time Spent,* and *Due date*.

     ![Views tab](/cms_trial/assets/3e8dbcca-a3ed-482a-94cf-d071b239514d.png)

Now assign those views to your hierarchies:

1. Go back to the **Hierarchies** tab.
2. Click the **Edit** button for *Execution*.
3. Select **Customize shown views** under the **View** section.
4. Select the **Devs** view.
5. Click **Update**.

   ![Edit hierarchy](/cms_trial/assets/102a49a7-dc91-4abd-a9ca-f1518345bb39.png)
6. Edit the *Strategy* hierarchy.
7. Select **Customize shown views** under the **View** section.
8. Select **Manage** view.
9. Click **Update**.

Refresh your dashboard. Then switch between hierarchies; each one now shows its own set of columns, as configured in the view you assigned it.

![hierarchies with views assigned](/cms_trial/assets/ce72622b-7c75-4793-afcb-4f99d0d62af7.png)

## Further exercises

Hierarchies become even more powerful when combined with other rich filter features. To build on this tutorial, try the following:

- Add an **Assignee dynamic filter** to your Rich Filter Controller gadget, as described in [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/). This lets you interactively filter the issues displayed within each hierarchy level.
- Combine hierarchies with a **Teams smart column** in your views to see which team is responsible for each issue at each level.

### Filter issues without losing their hierarchy

When you apply filters, the Rich Filters Result gadget keeps the hierarchy around each matching issue. If you filter by Assignee, for example, the Rich Filters Result gadget shows every matching issue plus the parents, siblings, etc. needed to preserve the structure and context, even if they don't match. This helps you understand where matching issues sit in the wider work context instead of presenting them as a flat list.

**What you'll see**

- Within the same node, matching issues are listed above non-matching ones.
- Next to the node, you can see one or two child counts; for example, 3/5 means that 3 of 5 available children match the filter.

  ![Assignee dynamic filter ](/cms_trial/assets/f21918b0-cc2e-4685-ac58-ed7578e67255.png)