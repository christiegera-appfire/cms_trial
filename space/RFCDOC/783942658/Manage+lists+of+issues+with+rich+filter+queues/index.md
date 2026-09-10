# Manage lists of issues with rich filter queues

[Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) provides **queues**, which allow you to manage lists of issues in Rich Filter Results gadgets efficiently. In this article, you'll learn how to create multiple queues to manage your work and see how queues interact with views and working queries.

This article covers the basics of rich filter queues and provides a simple work management example. If you are specifically interested in service management, check out Build a Service Management Dashboard with Rich Filters.

## Prerequisites

- A basic understanding of Jira dashboards and rich filters, as explained in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
- A basic understanding of [Jira Query Language (JQL)](https://www.atlassian.com/software/jira/guides/expand-jira/jql).

## Final result

Once you've worked through the steps in this tutorial, you should have a dashboard that contains two rich filter gadgets:

- A Rich Filter Controller gadget including quick filters to provide interactive filtering on your queues.
- A Rich Filter Results gadget has five work management queues, some with multiple views of the displayed issues.

![interactive filtering .png](/cms_trial/assets/6b8a9aec-002b-4fce-8224-0fbe020cc7fa.png)

## Rich filter and dashboard basic setup

In this section, you'll set up a basic rich filter and dashboard.

1. If you've already worked through other tutorials in our [Learning Center](/cms_trial/space/RFCDOC/783942482/User+guides/), you can base any gadgets you create while following this article on a previously created rich filter. Check that you have one available (find existing rich filters under **Apps** > **Rich Filters**). If not, follow the instructions in [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942658) to create a new rich filter before continuing.
2. Create a new dashboard (**Dashboards** > **Create dashboard**).
3. Make sure it is using the **One column** layout so you can easily see what is going on in the **Rich Filter Results** gadget you'll add below. You can select it using the **Change layout** menu at the top of the dashboard.

   ![one column layout.png](/cms_trial/assets/4b3e4d5d-0dae-4808-825e-57ab9a49427d.png)
4. Add a **Rich Filter Results** gadget and a **Rich Filter Controller** gadget to your dashboard, both based on your Rich filter (See also: [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/)).
5. After saving your gadgets' configuration, ensure the controller is above the results gadget; you can drag and drop it if necessary.

If you want a more detailed explanation of creating a new dashboard, see [Create a simple dashboard](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Jira queues vs. rich filter queues

Queues are not a concept particular to rich filters — [Jira Service Management](https://www.atlassian.com/software/jira/service-management) has [queues available](https://support.atlassian.com/jira-service-management-cloud/docs/what-are-queues/) to manage customer requests. However, we think you'll find rich filter queues more flexible and convenient:

- Jira queues are completely aimed at the service management use case and are available only in Service Management projects. Service management is centered on queues, but we believe queues have uses beyond that and are a powerful tool for managing lists of issues in general. You can use rich filter queues in any Jira product — Jira Service Management, Jira Software, and Jira Work Management.
- Jira queues are not available cross-project, whereas rich filter queues can be used for multiple projects simultaneously. It is possible to create a unified list of issues from multiple projects.
- You can filter each queue using the quick filters available in your Rich Filter Controller gadget. As a result, the rich filter queues are interactive, and each can do the job of several Jira queues.
- Rich filter queues are conveniently available in your dashboards, which can be combined with other useful information/gadgets, all in one place.

## Your first two queues

Let's create two initial queues — one to display top-priority work items and one to provide a view of all issues.

1. Open your rich filter config (described in [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. Select the *Queues* tab, and click **Create queue**.

   ![Create queue.png](/cms_trial/assets/c6a19b08-efa4-416c-8fef-e9a50402a37c.png)
3. Enter the following details in the resulting dialog box and click **Create**.

   - **Color**: Red
   - **Name**: `Top priority`
   - **JQL**: `priority in (Highest, High) AND status != Closed`

     ![image-20240507-090445.png](/cms_trial/assets/3257886e-4a52-4db4-a970-0a2a41f66984.png)
4. In the same way, as above, create another queue with these settings:

   1. **Color**: Blue (the default)
   2. **Name**: `All issues`
   3. **JQL**: Nothing (leave empty)
5. The *Queues* tab will now summarize your new queue details. You can edit or delete your queues using the edit and delete buttons (pen and trash can icons).

   ![Queues tab.png](/cms_trial/assets/6c7ac492-7b54-49b2-aa51-6667029e115d.png)

## Display your queues

If you go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), you should see no difference—by default, Rich Filter Results gadgets display all issues along with any defined views. Let's change the Rich Filter Results gadget to show our queues.

1. Open the configuration form of your **Rich Filter Results** gadget (as described in the [Easier configuration with the](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).
2. In the **Display** section, select the **Queues & Hierarchies** option.   
   The *Queues & Hierarchies* section is now displayed in the configuration form instead of the *Views* section.
3. Under **Queues & Hierarchies**, select the **Show all** option.

   ![image-20260812-153242.png](/cms_trial/assets/3eb26506-7b7c-49e3-b084-026951a57b40.png)
4. Click **Submit** to save your configuration.   
   Your Rich Filter Results gadget will now display your queues. Note how, in our Top priority queue, only a subset of the data is being shown — the total issues number is smaller as we only look at our filtered top-priority items.

   ![Queues Display.png](/cms_trial/assets/bf45c92b-717c-488f-a3cb-d8832ec10ff1.png)

There are several things worth noting about the queue display:

- Each tab contains the name given to the queue in the rich filter config and a count of the number of Jira issues displayed in that queue.
- The tabs are color-coded with the color given to the queue in the rich filter config.
- When the *Show all queues option* is selected, the tabs appear from left to right in the same order specified in the rich filter config. However, you can override this order in the gadget configuration using the Customize shown queues option. This option allows you to choose a subset of the available queues to display and drag and drop them to a different display order.
- You can hover over the queue tabs to bring up a tooltip containing the queue's JQL query.

## Add more queues to manage your work.

In this section, you will appreciate the full power of rich filter queues by adding more queues to show different slices of your data in the same Rich Filter Results gadget. You can use queues to build up complete work management processes on your dashboard and combine queues with other features, as you see later. For example, you could use quick filters in your controller to show only issues assigned to a specific assignee in your queues.

Let's get this done.

1. Open your rich filter config and go back to the *Queues* tab.
2. Add the following queues:

   1. Backlog

      - **Color**: Orange
      - **Name**: `Backlog`
      - **JQL**: `status = Open ORDER BY priority, duedate ASC`
   2. WIP

      - **Color**: Yellow
      - **Name**: `WIP`
      - **JQL**: `status in ("In Progress", Review)`
   3. Closed

      - **Color**: Green
      - **Name**: `Closed`
      - **JQL**: `status = Closed ORDER BY resolved DESC`
3. It would make sense to show the *All issues* queue first so the work management queues can all be next to one another. Drag and drop *All issues* to the top of the list.
4. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). You'll now see all five of your queues displayed.

   ![more QUEUEs.png](/cms_trial/assets/9777bfd1-5058-4eed-90f6-161eb92b1669.png)

## Static and fixed-order queues

There are a couple of queue config options we have not yet covered and are important to know about.

1. Go back to the *Queues* tab of the rich filter config screen.
2. Click the **Top priority** queue's edit button (pen icon) and examine the options in the **Queue behavior options** in the *Update queue* dialog box.

![Update queue dialog box with Top priority queue details entered](/cms_trial/assets/8613e277-269d-4374-81aa-5b38949b39ab.png)

The options are as follows:

- **Static queue**: This setting causes the queue always to display the same issues — the quick filters in controller gadgets do not filter the list. This is useful when you've got a queue that shows a very important set of issues, and you don't want to filter out any of them when quick filters in the controller are applied.
- **Fixed-order queue**: This setting causes the queue always to display its list of issues in a set order (you can't alter the order by clicking on the column headings). This is useful when the order in which you view or action a set of issues is important and should not be altered.

Let's add these options to a couple of appropriate queues

1. In the *Top priority* queue's *Update queue* dialog box, check the **Static queue** checkbox and click **Update**. You don't want to filter out these issues.
2. In the same way as above, update the *Backlog* queue by checking its **Fixed-order queue** checkbox and clicking **Update**. For example, we will keep the backlog sorted in order of priority as specified by the `ORDER BY` clause in the queue's JQL.
3. Your *Queues* tab should now include *Static* and *Fixed Order* labels to show where those settings are applied. Check it before moving on.

   ![static and fixed order.png](/cms_trial/assets/67876266-dd7f-45c7-a634-a222c565baed.png)
4. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). Try filtering and reordering the two queues we updated to see the effect of the applied settings. Note how a dot in the *Top priority* tab denotes a static queue, while on the fixed-order *Backlog* queue, the arrows in the columns used for quick reordering no longer appear.

   ![backlog.png](/cms_trial/assets/d1b42012-2e9c-4b69-8e23-d13ab47fe433.png)

## Display different views on different queues.

You can show different views on different queues, which is useful as you will likely want to see different information in each queue. Let's explore how to do this.

First, we will create some views:

1. Go to the *Views* tab of the rich filter config screen.
2. Create three views, as follows (see [Customize issue views and gadget scope](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) for a more in-depth guide to creating views):

   1. `Summary`: Include the columns *Issue Type*, *Key*, *Priority*, *Summary*, *Reporter*, *Assignee*, *Fix versions*, *Status*, and *Resolution*.
   2. `Product detail`: Include the columns *Issue Type*, *Key*, *Priority*, *Summary*, *Components*, *Assignee*, Fix versions*, Status*, and *Due date*.
   3. `Closed`: Include the columns *Issue Type*, *Key*, *Priority*, *Summary*, *Reporter*, *Assignee*, Fix versions*, Resolution*, and *Resolved*.
3. Your *Views* tab should now look like this. Check it before moving on.

   ![Views.png](/cms_trial/assets/3a4c7dfe-8dd7-4b9b-9e7e-616abe475f56.png)
4. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). You'll now see the *Summary,* *Product detail*, and *Closed* views beside the Queues as differently-styled tabs. Think of the views as sub-tabs inside each queue. Try clicking on a queue and then looking at the different views of that queue to see the difference.

   ![dashboard with views.png](/cms_trial/assets/858700a0-947d-4783-9dc7-e4937c717a55.png)

By default, all views are shown for all queues. Next, let's examine how to display different views in different queues.

1. Go to the rich filter config *Queues* tab. Note how the *Views* column of the queues summary says *All Views* for all the queues.
2. Click the *All issues* queue's **Edit** (▢) button.

   1. In the dialog box, click the **Customize shown views** radio button in the *Views* section to cause the **Select one or more views...** dropdown to appear.
   2. From the dropdown, select **Summary** — this is the only view we want the All issues queue to show.
   3. Click **Update**.
3. In the same way, update the other queues so that they only show the views indicated below:

   1. *Top priority*: *Product detail*.
   2. *Backlog*: Let's add two views for this queue — *Summary* and *Product detail*.
   3. *WIP*: Again, add *the Summary* and *Product details*.
   4. *Closed*: *Closed*.
4. Your *Queues* tab should now look like this. Check it before moving on.

   ![image-20260408-081139.png](/cms_trial/assets/6e2d08fd-fd55-4759-aa21-fdd228cae069.png)
5. Go back to your dashboard and [refresh it](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/). Visit the different queue tabs to see the difference in displayed views.

   ![different queue tabs.png](/cms_trial/assets/d239a292-15b2-47cc-8b36-287356c9941f.png)

If multiple views are selected in the *Select one or more views...* dropdown, you can drag and drop them to change their display order.

## Further exercises

As mentioned earlier, queues can be combined with other features to provide even more power to our dashboards. To complete this tutorial, we'd like you to add some filters to your controller to provide additional interactive filtering of the issues shown in your queues (you can add others if you like):

1. Add an *Assigned to me* static filter to your rich filter, as described in [Get started with Rich Filters for Jira Dashboards](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).
2. Add *Assignee* and *Issue type* dynamic filters to your rich filter, as described in [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/).
3. Add a *Teams* smart filter to your rich filter, as described in [Create a Teams smart filter](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/). Smart filters can also be used as smart columns—you could add a *Teams* smart column to your views to see which team is responsible for actioning each issue.
4. Refresh your dashboard and try using your new filters to filter your queues.

   ![interactive filtering .png](/cms_trial/assets/6b8a9aec-002b-4fce-8224-0fbe020cc7fa.png)

Also, we've kept the example generic in this article so that it can be easily followed by any Jira user, regardless of what Jira application you are using. If you are using [Jira Software](https://www.atlassian.com/software/jira), you could try the following:

- Create a *Current sprint* queue, filtered by the JQL "`Sprint in openSprints()`". This could perhaps replace the more generic *WIP* queue.
- Create a view for the *Current sprint* queue with *Story Points* and *Epic Link* columns.
- Include *Epic Link* and *Sprint* dynamic filters in your controller.

## Understand the difference between rich filter queues, views, and working queries.

In [Customize issue views and gadget scope](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/), we showed you how to create two separate Rich Filter Results gadgets, each filtered with a working query to show a different set of issues and each with two different views available of the issues displayed. Now that we're adding queues into the mix, it is important to step back for a moment and ensure you understand each feature's purpose.

- Working queries are JQL queries applied at the top level of a rich filter gadget, which filters all the data shown in that gadget. You can apply a working query to all rich filter gadgets, except the Rich Filter Controller and Rich Filter Text Panel gadgets. In the article linked above, we create two Rich Filter Results gadgets, one filtered to display "not canceled" issues and one filtered to display "canceled" issues via working queries. This is a good use of working queries. Canceled issues are probably unimportant to the average user's day-to-day work, so it is a good idea to filter them out of their worklist. Still, you might want to monitor them occasionally to ensure that useful items have not been discarded.
- Each Queue accepts a JQL expression as input and is used to create different lists of issues displayed in separate tabs inside a Rich Filter Results gadget. They are specific to Rich Filter Results gadgets. You could use working queries for the same purpose, but you'd need to use a separate Rich Filter Results gadget for each issue list. Queues provide a more convenient, dedicated way to do this.
- Views accept lists of columns as input and are used to display different sets of columns for the same sets of issues. They are specific to Rich Filter Results gadgets.