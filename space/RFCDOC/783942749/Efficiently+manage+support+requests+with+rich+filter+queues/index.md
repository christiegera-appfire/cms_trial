# Efficiently manage support requests with rich filter queues

One key aspect of service management is managing support requests as efficiently as possible. This includes tracking support requests as they progress through your support queues from assignment to completion, identifying problems (for example, requests that are unassigned or have been waiting for a support response for a significant amount of time), making sure SLAs are not broken, and efficiently using historical requests as a knowledge base to help answer new ones.

This article walks you through building a powerful support request management dashboard with [Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) that meets the above needs, allowing you to keep up with your service requests with maximum productivity. This is a key part of delivering an effective ITSM strategy.

## Prerequisites

This article assumes that you are using [Jira Service Management](https://www.atlassian.com/software/jira/service-management).

## Use case

Imagine the following scenario (your exact situation might have different numbers of projects or teams or other constraints, but the principles are the same):

- You have three different service management projects to support three different products.
- To answer support requests, you have support agents grouped into two teams that provide coverage for different geographical regions.
- The support agents in each team specialize in different products, with the aim of providing good overall coverage across all of them.

How can you manage all three projects and keep both teams productive and efficient?

## Solution: Use a rich filter-powered dashboard for support request management

[Rich Filters for Jira Dashboards](https://marketplace.atlassian.com/apps/1214789/rich-filters-for-jira-dashboards?hosting=cloud&tab=overview) provide a perfect feature set for managing support request queues, which you'll see in action throughout the article. Rich filters are based on a standard Jira filter, so the issues listed in rich filter gadgets can be cross-project. This enables you to build a single dashboard to manage multiple service management projects, giving rich filters a definite advantage over the default Jira Service Management queues defined for a single project.

To provide a solution to satisfy the use case detailed above, we are going to show you how to create the following dashboard:

![ basic dashboard.png](/cms_trial/assets/ab592dff-ea9e-487a-8258-cedbebf1e9a0.png)

But first, let's explore how this dashboard works and how it can help support teams efficiently manage their support request queues. Later on, we'll walk you through how to build it.

### Managing support issues

The gadget below is a [Rich Filter Results](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) gadget we have named *Support queues.* This is where most of the action happens on this dashboard.Multiple rich filter queues represent each stage of the support process.

![Unassigned queue.png](/cms_trial/assets/b5868da0-23f4-4c0a-838f-4179c7965089.png)

1. Your support agents will look at the *Unassigned queue* and assign appropriate issues to themselves.
2. Next, your support agents would focus on the *Waiting for support* queue, look at the SLAs view, and see what issues are closest to breaching the SLAs to determine what should be worked on first.

   ![Waiting for support queue.png](/cms_trial/assets/33b7abc6-8a64-4942-a1f5-fcaeec7aee93.png)
3. Rich filters allow you to provide multiple views for each queue, all in one place. In our example, the support agents can use the *Detailed* view of the *Waiting for support* queueto get more details on what needs to be done and start actioning support requests.

   ![contentId-783942749](/cms_trial/assets/5c59701f-954c-4031-ba79-416b57c067d6.png)
4. Your support agents can also look at the *Waiting for customer* queue and see whether any issues have been stalled for a long time. Those customers could perhaps use a ping, which could be easily automated.

   ![Waiting for customer .png](/cms_trial/assets/d438aa3c-7a2f-418c-b7fa-fe689f7eefd0.png)
5. The *Recently closed* queue has a number of potential uses. For example, your team could use it to plan a retrospective meeting in which you highlight issues and discuss how to improve in the future.

   ![Recently closed queue .png](/cms_trial/assets/5dea88d8-1a67-44c2-92c2-d550838986cf.png)

### Update and reply to support requests directly from the dashboard

Hovering over a row in a Rich Filter Results gadget highlights the row, plus it causes an **Open issue**dialog button to appear at the right-hand side of the row:

![Open issue_.png](/cms_trial/assets/aced11f7-94d5-4993-a769-a71a356747ee.png)

Clicking this button opens up the detail page for that particular issue in a dialog box overlay, allowing you to update and reply to support requests directly from the dashboard.

### Filtering your support queues

Rich filters provide a controller gadget containing quick filters that can be defined in any way you want.

![quick filters control.png](/cms_trial/assets/9e3be42c-12f5-499a-8e6c-5199805a7799.png)

The quick filters can be used to slice your data further, allowing each rich filter queue to do the job of multiple Jira queues. For example:

- Each support agent can click the **Assigned to me** quick filter to see only the support requests assigned to them. When a quick filter is used in the controller gadget, the other gadgets will apply that filtering, allowing users to focus on issues of interest easily.

  ![Assigned to me quick filter.png](/cms_trial/assets/7601a6ea-90d8-4933-a69e-3cf688c31ac7.png)
- You can filter your dashboard by individual projects or teams to see the situation for those specific groupings. The example below shows the *Support queues* filtered by the *Fox Service Desk* project.

  ![Fox Service Desk.png](/cms_trial/assets/89fd684e-0be8-43ac-a660-16b907e53600.png)

### Filtering the list of all issues to search for related solutions

One of the most valuable tools in your service management toolbox is your knowledge base, a large part of which will be your support history. Your support agents need an effective way of searching through previous issues to find related information to help them resolve current support issues—this is what the gadget we named *All support issues* is for (this, too, is a Rich Filter Results gadget).

![All Support Issues.png](/cms_trial/assets/b5987d34-3e46-4d76-a961-83a8767a568c.png)

Your support agents can use the same controller mentioned above to filter for the issues that might be useful to them. This includes a full-text search of the issues. Let's say an agent has a support query related to LDAP that is causing them some trouble, and they know they've dealt with a similar problem in a specific project before. They could:

1. You can filter by the specific project using the **Project dynamic** filter dropdown and the text `LDAP` using the **Contains text** filter field.

   ![Project dynamic.png](/cms_trial/assets/a4ed5df2-f484-49ae-9daa-6beae5914d12.png)
2. Look at the search results in the *All support issues* gadget to see if they can find helpful information.

   ![TEXT FILTERED.png](/cms_trial/assets/6d1bf754-d236-4f0c-8ebf-67b55e8fd87a.png)

   Use other quick filters to filter their results further if required.

### Providing access to important resources

Rich filters include a text panel gadget to give users easy access to important dashboard resources. These can contain support scripts, predefined answers to common questions, links to important resources, or whatever else you think your support agents need to be productive.

![Text panel gadget containing a checklist, a Common answers expandable box, and a link to External support docs](/cms_trial/assets/69201157-2460-45cb-a5aa-7cedc1e95bf1.png)

This can be fully customized with colors, fonts, expanding/collapsing panels, and more per your needs.

## Rich filter features resources.

The following links provide information on the fundamentals of each rich filter feature used in this dashboard in case you need more information:

- A [Rich Filter Results gadget](/cms_trial/space/RFCDOC/783941759/The+Rich+Filter+Results+Gadget/) to provide easy access to:

  - Multiple [Rich Filter Queues](/cms_trial/space/RFCDOC/783942658/Manage+lists+of+issues+with+rich+filter+queues/) will represent your different support queues.
  - Multiple [Rich Filter Views](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) to provide different views of the support requests for different purposes.
- Another Rich Filter Results gadget to display all issues.
- A [Rich Filter Controller gadget](/cms_trial/space/RFCDOC/783941745/The+Rich+Filter+Controller+Gadget/) containing [static](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/), [dynamic](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/), and [smart filters](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/) enables you to filter your support queues by different dimensions.
- A [Rich Filter Text Panel gadget](/cms_trial/space/RFCDOC/783942398/The+Rich+Filter+Text+Panel+Gadget/) to provide easy access to important resources.
- A [Rich Filter Issue Activity Stream gadget](/cms_trial/space/RFCDOC/783942442/The+Rich+Filter+Issue+Activity+Stream+Gadget/) to provide filterable, at-a-glance monitoring of recent activities on your support requests.

## Start building the *Support request management* dashboard

Now that we've explained what our solution can do let's go ahead and build it.

In this section, you'll create a new rich filter and a dashboard containing all the gadgets you'll need with minimal configuration. You'll do this all in one go, so you won't need to keep returning to dashboard edit mode to add more gadgets later. If you need any instructions on creating rich filters and dashboard basics, you can find them in Get Started [with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942749).

1. Create a new rich filter based on a Jira filter that returns all the support request issues you want to manage with your support request management dashboard (see [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942749) for guidance if needed). Call it something appropriate like "Support request management." Remember that your Jira filter can return support request issues from multiple Service Management projects, so this solution has the advantage of being cross-project.
2. Create a new dashboard with the *Left sidebar layout*, called something appropriate like "Support request management dashboard".
3. Add the following gadgets to your dashboard. In each case, select your *Support request management* rich filter as the *Rich filter* value, then click *Submit*:

   1. Rich Filter Controller gadget
   2. Rich Filter Issue Activity Stream gadget
   3. Two Rich Filter Results gadgets
4. Add a Rich Filter Text Panel gadget to your dashboard (text panel gadgets are not based on rich filters, so you just need to click Submit in the configuration form).
5. Position and name the gadgets as specified below:

   1. Rich Filter Controller gadget: Position it at the top of the left-hand column.
   2. Rich Filter Text Panel gadget: Position it in the left-hand column below the Rich Filter Controller gadget.
   3. Rich Filter Issue Activity Stream gadget: Position it in the left-hand column below the Rich Filter Text Panel gadget.
   4. Rich Filter Results gadget #1: Position it at the top of the right-hand column and rename it to "Support queues."
   5. Rich Filter Results gadget #2: Position it at the bottom of the right-hand column, below the first results gadget, and rename it "All support issues."
6. Click **Done** at the top of the UI to exit dashboard edit mode.

You should now have a basic dashboard that looks like this:

![ basic dashboard.png](/cms_trial/assets/ab592dff-ea9e-487a-8258-cedbebf1e9a0.png)

Important time-saving tips:

1. When you need to configure an existing gadget further, don't do it via dashboard edit mode—you can do it more quickly and with fewer dashboard refreshes using the [*rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) available on each gadget.
2. The *Rich filter menu* also contains an option to open the config for the rich filter on which the gadget is based. For convenience, we recommend keeping the dashboard open in one browser tab, keeping the rich filter configuration open in another tab, and moving between the two as required.
3. When you've changed the rich filter config in one tab and want to see those changes reflected in the dashboard in the other tab, refresh your dashboard quickly and conveniently using your controller's [*Optimized refresh*](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/) [button](/cms_trial/space/RFCDOC/783942462/Get+started+with+Rich+Filters+for+Jira+Dashboards+for+Cloud/).

## Set up your filters

In this section, you will create all the quick filters you'll use in your dashboard. The static and dynamic filters will be usable from your controller and provide a lot of power — they filter the content shown in all other rich filter gadgets based on the same rich filter as the controller (for more information on static and dynamic filters, have a look at [Get started with Rich Filters for Jira Dashboards](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rfcdoc&title=Get%20started%20with%20Rich%20Filters%20for%20Jira%20Dashboards&linkCreation=true&fromPageId=783942749) and [Enhance your Jira dashboards with dynamic filters](/cms_trial/space/RFCDOC/783942548/Enhance+your+Jira+dashboards+with+dynamic+filters/)).

1. Go to the *Static Filters* tab of your rich filter config (accessed via the [*Rich filter*](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/) [menu](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)) and create a new static filter called "Assigned to me", with the *JQL* "`assignee = currentUser()`".
2. Go to the Dynamic Filters tab and add filters based on the Jira fields — *Project*, *Created*, *Priority*, *Customer Request Type*, *Organizations*, *Assignee*, *Issue Type*, and *Contains text*

These provide useful filters for focusing on different issue sets, but the *Contains text* filter deserves a special callout. This provides a full-text search of the *Summary*, *Description*, comment, and any other text fields that might be used in the support requests. This is critical for searching through historical issues to help with answering new, related support requests.

In our scenario, we have two support teams. Let's create a "Team" smart filter to allow you to display a quick filter in your controller to filter by team (for more information on configuring and using smart filters, see our [Use custom smart filters and smart columns on your dashboard](/cms_trial/space/RFCDOC/783942590/Use+custom+smart+filters+and+smart+columns+on+your+dashboard/)article). Later on, you'll also use "Team" as a smart column in your Rich Filter Results gadgets to show which team an issue is assigned to.

1. Go to the *Smart Filters* tab.
2. Create a new smart filter called "Team".
3. Create a separate smart clause for each team in the Team config screen. We've included two, but you might want to include more:

   1. "Green Team": Give it a green color and JQL to filter by members of that team, for example "`assignee in membersOf("green-team")`".
   2. "Orange Team": Give it an orange color and JQL to filter by members of that team, for example, "`assignee in membersOf("orange-team")`"

As an alternative to the above JQL, you might want to filter each team's JIRA issues using JQL like "`assignee in (a,b,c)`", where the letters are different assignee IDs.

Go back to your dashboard and refresh it; your controller should look like this:

![quick filters control.png](/cms_trial/assets/9e3be42c-12f5-499a-8e6c-5199805a7799.png)

## Set up your views

Here, you'll set up rich filter views to provide different views of your issues for different purposes (for more information about using and configuring views, see [Customize issue views and gadget scope](/cms_trial/space/RFCDOC/783942532/Customize+issue+views+and+gadget+scope/)).

1. Go to the *Views* tab of your rich filter config.
2. Create a view called `Main` This will provide a general summary of each issue, including who is assigned to it, what type of support request it represents, the first response time, etc.

   - Give *Main* the following columns: *Issue Type*, *Key*, *Customer Request type*, *Summary*, *Team*, *Assignee*, and *Time to first response*.
3. Create a second view called `Detailed`. This will provide more details about a request and what response is required for it.

   - Give *Detailed* the following columns: *Issue Type*, *Key*, *Summary*, and *Description*.
4. Create a third view called `SLAs`.This will provide specific details about each issue, including whether the SLAs are being met.

   - Give *SLAs* the following columns: *Issue Type*, *Key*, *Summary*, *Team*, *Assignee*, *Time to first response*, and *Time to resolution*.
5. Create a fourth view called `Closed`. This view will provide details about whether the customer was satisfied with the resolution in each case.

   - Give *SLAs* the following columns: *Issue Type*, *Key*, *Summary*, *Team*, *Assignee*, *Satisfaction*, *Time to first response*, and *Time to resolution*.
6. Go back to your dashboard and refresh it to make sure your views are being shown. Both Rich Filter Results gadgets should look the same at this point. For example:

   ![all_views.png](/cms_trial/assets/69e75174-ab07-4699-9857-ddda6b7080de.png)

## Set up your queues

Rich filter queues are more flexible and convenient than native Jira queues in several ways:

- You can use them in any Jira product, not just Jira Service Management.
- They are cross-project — they can list issues from multiple projects at once.
- They can be filtered using quick filters, which means they are interactive. Each one can do the job of several Jira Service Management queues.
- They are conveniently available in your dashboards to combine with other useful information.

Now, you'll set up your queues to represent each stage in your support management process (for more information on configuring queues, see our [Manage lists of issues with rich filter queues](/cms_trial/space/RFCDOC/783942658/Manage+lists+of+issues+with+rich+filter+queues/) article).

1. Go to the *Queues* tab in your rich filter configuration.
2. Create a queue called "Unassigned". This will act as a queue for support requests that have not yet been assigned to anyone. Support agents will pick their next task from this pool.

   1. Give it a red color.
   2. Give it the JQL `status = "Waiting for support" AND assignee is EMPTY`—you want this queue to display issues that are waiting for support but have no assignee.
   3. Click the *Customize shown views* radio button to select only the useful views in this queue. In the resulting *Select one of More views* dropdown, select the *Main, Details, and SLAs* views.
   4. Check the *Static queue* checkbox. This is an important set of issues, and you don't want to filter out any of them when quick filters are applied; you can prevent this by making this queue a static queue.
3. Create a queue called "Waiting for support". This is also an important queue, as it will display all of the open items waiting for support, ordered by *Time to first response so that* you can see the most critical items at the top of the list.

   1. Give it an orange color.
   2. Give it the JQL `status = "Waiting for support" AND assignee is not EMPTY ORDER BY "Time to first response"` — you want this queue to display issues that are assigned and waiting for support, ordered ascending by *Time to first response*.
   3. Click the *Customize shown views* radio button. In the resulting *Select one of more views...* dropdown, select the *Main, Details, and SLAs* views.
   4. Check the *Fixed-order queue* checkbox. This set of issues is ordered in a specific way for a specific purpose; by making it a fixed-order queue, you can prevent it from being reordered.
4. Create a queue called "Waiting for customer" to monitor the status of support requests that are waiting for more input from customers.

   1. Give it a blue color.
   2. Give it the JQL `status = "Waiting for customer" ORDER BY updated DESC`—this will filter for all issues waiting for customer input and order them descending by the time of the last update.
   3. Click the *Customize shown views* radio button. In the resulting *Select one of more views...* dropdown, select the *Main* view. You don't need to access quite as much information about issues that aren't waiting on your team.
5. Create a "Recently closed" queue to view the issues closed in the last week and review whether they met their SLAs and whether the customers were satisfied.

   1. Give it a green color.
   2. Give it the JQL "`status = Closed AND resolutiondate > -7d`"—this will filter for all issues resolved within the last week.
   3. Click the *Customize shown views* radio button. In the resulting *Select one of more views...* dropdown, select the *Closed* view. You are interested in monitoring customer satisfaction information in this queue.

Your Queues tab should look like this:

![queues for use case.png](/cms_trial/assets/90b7222a-3dfe-4809-ba74-aab391f91c2b.png)

## Set up the main Support queues results gadget

Now let's focus on configuring the *Support queues Rich Filter Results* gadget to display the queues as desired.

1. Return to your dashboard and open the config form for the *Support queues* gadget.
2. Click the *Queues* radio button to display the *Queues* section instead of the *Views* section. You want to view all queues in this gadget, so keep the *Show all queues* radio button selected.
3. Click *Submit*.

Your *Support queues* Rich Filter Results gadget should now look like this:

![Support queues Rich Filter Results .png](/cms_trial/assets/3eb4c1c1-ca09-4653-9d8c-4baf56811184.png)

## Set up All support issues result in the gadget

Now let's configure your *All support issues* Rich Filter Results gadget.

1. Open the config form for all support issues gadgets.
2. We don't want to display queues in this gadget, so keep the **All Issues** radio button selected.
3. Click the **Customize shown views** radio button.
4. In the resulting *Add a view* dropdown, select **Main** and **Detailed**. These views provide the appropriate level of detail for using past support requests as a knowledge base.
5. Click **Submit**.

Your *All support issues* Rich Filter Results gadget should now look like this:

![All support issues Rich Filter Results gadget.png](/cms_trial/assets/669ccc87-641b-44b5-a78a-9cd72cfe5709.png)

## Set up your text panel gadget

Finally, let's take a look at your text panel gadget. As mentioned earlier, this can contain whatever content you want. We recommend including the content that will make your support agents most productive. This will likely include:

- Support scripts, meaning common boilerplate text that will be used frequently.
- Predefined answers to common questions, such as how to unlock an account or how to request access to a specific resource.
- Links to important resources, like external documentation, EULAs, and SLA details.
- Important reminders, such as a daily checklist to follow.

We won't tell you exactly what to write in your text panel, as every set of requirements will be slightly different. The following instructions are designed to help you start with it (see also [The Rich Filter Text Panel Gadget](/cms_trial/space/RFCDOC/783942398/The+Rich+Filter+Text+Panel+Gadget/) for further guidance).

1. Open the config form for the Rich Filter Text Panel gadget. In each case below, ensure your cursor is on a new line inside the main text area before following the instructions.
2. Select the *Info panel* from the options provided by the editor in the config toolbar.

   1. Select the *Success* (checkmark) from the row of icons.
   2. Inside the info panel, enter a bulleted list containing some daily instructions along the lines of:

Morning checklist:

1. Look at the *Unassigned* queue. Assign yourself relevant issues.
2. Look at *the Waiting for support queue and SLAs view; find the next work with the Assigned to me* filter.
3. Start on the highest-priority issues.

1. Select *Expand* from the options in the config toolbar.
2. Enter a title for your expansion: "Common answers."
3. Enter the following text into the main body of the expansion: "**Unlocking an account**: You can unlock your account by following these steps."
4. Select *Link* from the options in the config toolbar.

   1. Paste a link to one of your important external docs sites in the *Paste link* field.
   2. In the Text to Display field, enter suitable link text, such as "External support docs."

Your Rich Filter Text Panel gadget should look something like this:

![Text panel gadget containing a checklist, a Common answers expandable box, and a link to External support docs](/cms_trial/assets/69201157-2460-45cb-a5aa-7cedc1e95bf1.png)

## Final result

![ basic dashboard.png](/cms_trial/assets/ab592dff-ea9e-487a-8258-cedbebf1e9a0.png)