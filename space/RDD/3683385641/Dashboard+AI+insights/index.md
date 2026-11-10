# Dashboard AI insights

## Overview

**Dashboard insights** are available to anyone viewing the dashboard. It turns the data behind Dashboard Hub gadgets and dashboards into clear, plain-language interpretations so you can see what the numbers mean without digging through raw tables or charts. You can also use it for tips and help to improve data visualizations. It works on Dashboard Hub for Jira and Confluence, right where your dashboards already live.

Instead of interpreting a chart yourself, you get short, plain-language notes on what your data shows: trends, what stands out, and what needs a closer look.

- Every insight is generated from the live data in your gadgets, not generic advice.
- Insights are concise and structured so you can scan them quickly.

## How to use dashboard insights

Click **Dashboard insights** at the bottom-right of a dashboard to open a resizable panel. It aggregates insights across all compatible gadgets on the dashboard, summarizing the insights and relevant actions you can take. Drag the panel to reposition it or click **Dashboard insights** again to minimize it.

![Dashboard Hub dashboard showing the Dashboard insights button used to open the insights panel.](/cms_trial/assets/67ba13dc-4798-4d88-8a02-fc7314e83df0.png)

In dashboards with multiple slides, dashboard insights are relevant to the active slide only.

### Read insights

Expand an insight to read a quick summary of what your dashboard is showing. Insights reads your dashboard for you, surfacing the trends, changes, and anything unusual worth your attention.

![Dashboard insights panel displaying an expanded insight with a summary of dashboard data.](/cms_trial/assets/136587e2-c8f6-4673-a459-8834efa09730.png)

**Examples**:

- Open issues rose 18% this week, mostly in the Payments project.
- 3 of the 5 teams on this dashboard are behind their sprint target.
- Bugs marked Highest priority have been open for 12 days on average, up from 7 last month.
- 6 OKRs have not been started.

### Review recommendations

Recommendations suggest next steps based on what it finds. Review each recommendation and choose whether to act on it. Nothing changes until you decide.

### Apply a dashboard filter

Some recommendations provide a filter action to reveal specific data, for example, to reduce a date range or work item scope. Click the filter link to apply it to your dashboard. The filter runs on your current view only; it doesn't change any underlying data.

![Dashboard insights panel displaying recommendations and an option to apply a dashboard filter.](/cms_trial/assets/be967514-f05f-47a7-9d4f-632b5dbf5dc8.png)

**Examples**:

- New bugs are coming in faster than they're being fixed. Consider setting aside time each sprint for bug fixing.
- One person is assigned almost half of the open issues. Consider sharing the work more evenly across the team.
- Move incomplete issues (NIC-1, NIC-2, NIC-3 and others) to the backlog or a new sprint.
- With this many categories, the differences are hard to see. Try a different chart type or fewer categories.

### Follow-up chat

Use the chat field in the insights panel to ask follow-up questions, including how-tos. Each answer carries the full context of your dashboard, so you can dig deeper without re-explaining what you're looking at.

![Dashboard insights panel showing the follow-up chat field and an example response.](/cms_trial/assets/92925317-7830-49d2-b4dc-88c26014963c.png)

**Examples**:

- What's the biggest risk to this sprint?
- Why did our velocity drop?
- Which team needs the most help right now?
- How do I add more segments?

## Include dashboard insights in dashboard subscriptions

You can add a dashboard AI insights summary to a dashboard subscription snapshot email to highlight anything that needs attention. To include the summary, turn on the **Include AI insights** toggle in the *Create subscription* or *Manage subscription* page.

![Dashboard subscription settings showing the Include an AI insights toggle.](/cms_trial/assets/bed691d0-d84a-48e2-a67f-5c352dfc83f3.png)

## Manage AI settings

The **Enable AI features for this site** toggle is **on** by default for sites with an active trial or commercial license. The **Allow AI insights in subscription emails** toggle is **off** by default. A Jira administrator can manage these settings in *Global Settings*.

![Global Settings showing the Enable AI features for this site and Allow AI insights in subscription emails toggles.](/cms_trial/assets/97324457-30c5-4cbc-9f3a-d4b6329ca88e.png)

## AI usage limits

Dashboard Hub Insights has monthly usage limits. Each time you open Insights or ask a follow-up question, it counts towards your usage.

There are two limits:

- **Your personal limit**: How much you can use Insights each month.
- **Your site's limit**: How much everyone on your site can use Insights each month, combined.

If you reach either limit, Insights stops until the limit resets on the 1st of the month.

### Processing limits

If a dashboard renders a lot of data, AI processing might not be available. If this happens, try updating your gadget configurations to reduce the data.