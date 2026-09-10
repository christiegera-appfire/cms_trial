# How to bulk update the JQL of dashboard gadgets

This page explains how to use **Bulk update JQL** in Dashboard Hub to update the JQL query for all compatible dashboard gadgets at once. This replaces any JQL query or filter applied to individual gadget configurations.

## Overview

Dashboards often represent a specific space or team. When something changes, you might need to reconfigure your dashboard gadgets. On a large dashboard, this is time-consuming and easy to get wrong. Bulk update JQL lets dashboard owners apply a single JQL query across all compatible gadgets at once, directly from the dashboard header, without opening each gadget's configuration settings.

This is useful if you:

- Duplicate and reuse dashboards across sprints, projects, or teams.
- Share a dashboard template and need to adapt it quickly for different contexts.
- Maintain large dashboards and want confidence that every gadget is looking at the same dataset.

### Watch the overview video to learn more and get started:

Video transcript:

If you manage dashboards with multiple gadgets, updating each one individually takes time. Bulk update JQL lets you apply a single JQL query or filter to all your compatible gadgets at once, right from the dashboard header.

This is especially useful when you’re duplicating a dashboard for a new sprint, project, or team. Instead of opening each gadget’s settings individually, you update them all at once. It’s also great for setting up dashboards from a template.

Start by clicking Edit on your dashboard. Then click Bulk update JQL in the top bar.

You’ll see a JQL input field appear at the top of the dashboard. Compatible gadgets are highlighted with a blue border and selected by default. The input field lists the queries and filters already applied to your gadgets, so you can select one as a starting point or type a new query. You can also select a saved filter if one is available for your Jira datasource.

If you don’t want to update a specific gadget, just clear its checkbox.

Click Preview to validate your query and see the results across your gadgets.

When you’re happy, click Apply, then Save. Your JQL now applies across all selected gadgets.

If your dashboard has multiple slides, repeat the process on each slide.

## Instructions

If you’re a dashboard editor, follow the steps below to apply a JQL query or filter to the dashboard data. The filter applies to compatible gadgets. If your dashboard has multiple [slides](/cms_trial/space/RDD/146309888/How+to+set+up+a+slideshow/), you need to apply the bulk JQL to each slide.

1. Click **Edit** in your dashboard.
2. Click **Bulk update JQL** in the dashboard top bar. A JQL input field appears at the top of the dashboard, and compatible gadgets are highlighted with a blue border.

   ![The Bulk update JQL input field shown in Dashboard Hub with selected compatible gadgets.](/cms_trial/assets/c669f594-4a9f-4ab4-baf5-28cd7d92c9fe.png)
3. Type your JQL query or select a saved filter. The input field displays the current queries or filters applied to gadgets if configured.
4. Click **Preview**. The query validates in real time. All your compatible Jira gadgets will be filtered.
5. If you don’t want to update the JQL of any of the compatible gadgets, clear the corresponding checkbox.
6. Click **Apply**. The JQL replaces the existing query in all selected gadgets.
7. (Optional) To make changes to the JQL, apply a new bulk filter or query, or edit an individual gadget configuration.
8. Click **Save**.

**Did you know?** If you use JQL Search Extensions (JSE), you can use your saved JSE filters in Dashboard Hub. JSE by Appfire adds over 50 keywords and functions for faster and more precise searching in Jira. Visit our [Marketplace listing](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?utm_term=&utm_campaign=Vansah%20-%20Performance%20Max&utm_source=adwords&utm_medium=ppc&hsa_acc=5225442043&hsa_cam=22794333589&hsa_grp=&hsa_ad=&hsa_src=x&hsa_tgt=&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=22794334942&gbraid=0AAAAAogQknepyiRVdJOqzOWahIzt993FK&gclid=CjwKCAjwidXQBhAZEiwA4egw6ABCAKh6AFlT2aCtdz6-Z29HJjtuT7Ez08c9n4pwcn1fawck-KgBZBoCit8QAvD_BwE) to start your free trial.