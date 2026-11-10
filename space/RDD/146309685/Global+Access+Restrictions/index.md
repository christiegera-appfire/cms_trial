# Global Access Restrictions

## Overview

This page explains how to configure global access restrictions for Dashboard Hub.

To configure the Global Access Restrictions, go to **App settings** > **Global Access Restrictions**.

![Dashboard Hub Global Settings](/cms_trial/assets/08a45f74-4c86-4a47-aa51-4f366629883c.png)

### Restrict Global Access

When **Restrict Global Access** is enabled, only selected users and groups can access the app. Users not included in the selected users or groups won’t be able to create, edit, or remove dashboards.

Remember that the visibility of each dashboard is configured at the dashboard level. See [Dashboard permissions](/cms_trial/space/RDD/146309693/Dashboard+permissions/).

If a user accesses a public link, global restrictions are not enforced. It doesn’t matter if that user is logged in. See [Share a dashboard with a public link](/cms_trial/space/RDD/146310576/Share+a+dashboard+with+a+public+link/) for more information.

### Restrict Access to the Customer Portal

Admins can restrict access to reporting dashboards for customers using Jira Service Management customer portals. For more details, see [Manage access to the Jira Service Management Customer Portal](/cms_trial/space/RDD/146309699/Manage+access+to+the+Jira+Service+Management+Customer+Portal/).

### Restrict Public Links

If you select **Restrict Global Access**, only selected users and groups will be able to create public links for external dashboard sharing. Remember that public links enable external, anonymous access, allowing individuals without access to your instance to view the content shared using these links. Read more about [public links](/cms_trial/space/RDD/146310576/Share+a+dashboard+with+a+public+link/).

### Adaptive filters on external dashboards

Use the Adaptive Filters restriction to hide the Adaptive Filters bar on dashboards shared using a public link or the Jira Service Management Customer Portal. See [Adaptive Filters](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=rdd&title=Dynamic%20filters&linkCreation=true&fromPageId=146309685) to learn more.

### AI Beta

Enable AI Beta to allow users to use AI dashboard insights. This setting is on by default. Turn it off if you don’t want to give users access to Dashboard Hub’s AI features.

### Subscriptions

- Turn on **Require a password for email subscriptions** to ensure all subscriptions are password proetected.
- If you turn on **Allow AI insights in subscriptions**, users can add an AI summary to the subscription emails when they create a subscription. This setting is off by default.

## Related pages

- [Dashboard permissions](/cms_trial/space/RDD/146309693/Dashboard+permissions/)