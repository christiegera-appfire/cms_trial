# Release notes 11 August 2026

**Release date**: August 11, 2026

This page outlines the updates included in the latest release of the Dashboard Hub family of apps.

---

## New features

## BigPicture OKRs gadget

Dashboard Hub’s **BigPicture OKRs** gadget lets you display your BigPicture OKR progress directly in Dashboard Hub. Select the Objectives you want to track, filter by period, owner, team, or status, and view the results as a tree of Objectives and Key Results with customizable columns. And because it’s built on Dashboard Hub, you’re not limited to a list view. Apply the same charting and aggregation power you use across your dashboards to turn OKR data into insight, like a pie chart of OKRs per team or a bar chart of progress by owner.

This gadget integrates with [BigPicture Advanced](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?hosting=cloud&tab=overview). Make sure you have BigPicture Advanced installed and access to the OKR module.

![BigPicture OKRs gadget in Dashboard Hub showing objective statuses by team](/cms_trial/assets/92b4d331-3b17-46ff-b2ab-44e9b76a9173.png)

## Example use cases

Use this gadget to answer questions about your OKR progress, such as:

- **OKR Progress Tracking**: Monitor the progress of Objectives and their Key Results at a glance without leaving your dashboard.
- **Team OKR Overview**: Filter by team or owner to see which OKRs are assigned to specific people or groups.
- **Period Reviews**: Filter by period to focus on quarterly or annual OKRs during review cycles.
- **Stakeholder Reporting**: Share OKR progress with people outside Jira by embedding dashboards in Confluence pages.

See [BigPicture OKRs](https://support.appfire.com/space/RDD/3402104953/BigPicture+OKRs) or watch the overview video to learn more.

Video script

In this video, we’ll show you how Dashboard Hub’s BigPicture OKRs gadget brings your objectives straight to your dashboards so you can track progress right where your work already lives.

Your team set their objectives for this quarter, but now you have to go look for them. The objectives live in one tool. Your project work lives in another, and this means clicking back and forth across tabs to see how you’re doing

BigPicture OKRs shows you these objectives directly in your Jira dashboard. Setup is quick: add your BigPicture OKR datasource (you’ll need to create the OKR API key in BigPicture), then add the BigPicture OKRs gadget to a dashboard. Choose the objectives and key results that you want to track using the objective selector or a date range.  and then pick the columns to show. Next,  choose how to see them whether as a nested table or one of the many chart options. That’s it. No switching, no copying data out. Your objectives now sit where your team already looks every day.

The objectives, and KPI measures beneath them, are laid out in one clear list. Progress updates as the work moves. The moment something turns “at risk,” it’s there in front of you.

Running a quarterly review? Show just this quarter. Checking in with one team? Show only their goals. Want to see what needs attention? Show only what’s at risk or off track. You set the view to match the conversation you’re about to have so the dashboard answers the question before anyone asks.

The people who care most about your objectives might not work in your Jira space at all. Share the dashboard, create a subscription or add it to a Confluence page, everyone sees the same live progress you do.

Your objectives, and the work that gets you there — finally in one view. That’s the BigPicture OKRs gadget from Dashboard Hub.

You can also try out the BigPicture Custom Charts gadget, part of our BigPicture integration. Visit our Marketplace listing or our user documentation to learn more about using Dashboard Hub and BigPicture together.

---

## Enhancements

## Subscriptions

**My subscriptions**: We’ve added a *My subscriptions* page to help you manage multiple subscriptions from one place. *My subscriptions* provides the following:

- Overview of all subscription logs
- Run now: a manual snapshot capture
- Actions menu for each subscription that includes **Edit**, **Run now**, and **Unsubscribe**.

![My subscriptions page in Dashboard Hub showing the options available in the Actions menu.](/cms_trial/assets/f3b933cd-48bd-4070-8d11-b6524d41a9fa.png)

**Unsubscribe**: We added an Unsubscribe link to the subscription snapshot emails. This lets individual users unsubscribe from a subscription. To resubscribe, a user must contact the subscription creator.

See [Dashboard subscriptions](https://support.appfire.com/space/RDD/2934407285/Dashboard+subscriptions) for more details, or watch the video for a quick overview.

Video script

The team that delivered dashboard snapshots straight to your inbox now brings you a single place to manage all your subscriptions, at once.

To view your subscriptions, open the More actions menu in the top bar of any dashboard and select My subscriptions. Here, you'll see every in one list, the last run status, next scheduled date, who's receiving it, and any restrictions all at a glance.  
If you manage several subscriptions, you can filter your view to see all subscriptions, just the ones you own, or the ones you're subscribed to. Or, use the search field to quickly find a subscription for a specific dashboard.

Each has its own actions menu. If you're the dashboard editor, you can select edit, to update the schedule details, recipient list, or delete the subscription for everyone. Or select run now to send an ad hoc snapshot email right away. So you don't need to wait for an update or open individual dashboards.

Anyone on the list can unsubscribe to remove their name from the recipient list. If you need to subscribe again later, just reach out to a dashboard editor.

With my subscriptions, there's no more digging through dashboards or inboxes. Keep track of everything you follow, own, and send with ease.

## Adaptive Filters

Our Adaptive Filters feature is enhanced by the following updates:

- **Support for native Jira Team field**: The filter applies to all compatible gadgets when a user selects the Team field in the filter bar.
- **Support for Sprint field**: The filter applies to all compatible gadgets when a user selects a Sprint in the filter bar. This enhancement applies to all array field types, for example, labels.
- **More filters**: You can now add up to 10 filters to the Adaptive Filters bar.
- **UI improvements**:

  - We removed the tabs for field selection. When using the search field on the *Customize dashboard filters* page, all matching results are displayed in a single list.
  - You can now drag selected filters to reorder them in the filter configuration. This lets you choose the order in which filters appear in the dashboard.

See [Adaptive filters](https://support.appfire.com/space/RDD/146309549/Adaptive+Filters) to learn more.

## Improved x-axis label readability

Charts that plot a large number of data points now keep their x-axis labels legible. Previously, when many values were displayed, the x-axis labels could overlap and become difficult to read. This enhancement ensures x-axis labels remain clear and readable even when a chart contains a high data density.

![Dashboard Hub gadget showing the improved x-axis layout with clearer labels.](/cms_trial/assets/f823f529-a954-4dd1-b42b-71a18ad8619e.png)

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers. Your support and feedback inspire us to keep improving. We appreciate your trust in Dashboard Hub!