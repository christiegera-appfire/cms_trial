# SLAs Breach Watch

## Overview

Given the time-sensitive nature of SLA, it's paramount to keep an eye and meet the deadlines agreed in the SLAs. Thus, **the “SLAs Breach Watch” gadget displays Jira issues with SLAs that are about to be breached or have recently been breached**. Support agents are notified of potential breaches, allowing them to take action to prevent or resolve SLA breaches.

The gadget tracks elapsed time, remaining time for SLAs, SLA status, and more, while also conveying a sense of urgency and importance.

This gadget requires <https://appfire.atlassian.net/wiki/spaces/TTSC>

Data Center version <https://appfire.atlassian.net/wiki/spaces/TTS> not available by default, check [Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)

This gadget is **multi-project**, so you can report across your whole portfolio of projects

## Views

This gadget offers two different ways to display the issues with SLAs breached or about to be breached: The **Extended view** and the **List view**. In both cases, the issues are sorted in chronological order, first the recently breached issues, then the issues about to be breached.

The information provided for each issue is:

- Related to the **issue**: Issue key, type, summary, status and assignee.
- Related to the **SLA**: SLA name, status, time elapse, time remaining, breached time.

### Extended View

This view is thought to display a lesser number of issues but in a more clean way.

![Dashboard Hub SLAs breach watch extended](/cms_trial/assets/831c9436-7371-46c6-b708-05548881de49.png)

### List View

This view is intended for those cases where the need to display issues goes beyond a few items. All the key information is still available but using a lean design.

![Dashboard Hub SLAs breach watch list](/cms_trial/assets/34ea9a20-972e-4e90-89ba-35831e170bf1.png)

Important:

- The gadget displays all issues with SLAs that are breached or about to be breached. If an issue has multiple SLAs in it, then each issue will be displayed
- The **API token** you need from Time to SLA to create a datasource requires the SLA and Issue SLA generate to use in Dashboard Hub has to have the "SLA" and "Issue SLA" access

![Dashboard Hub API token configuration](/cms_trial/assets/f6888531-44b2-43ef-83f8-90555fbbedce.png)

## Configuration

![Dashboard Hub SLAs Breach Watch SLA breach watch config](/cms_trial/assets/0ad67f96-fee4-4690-84b5-848b723d7eae.png)

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, select a **Time to SLA** datasource, remember that you have to create this datasource first.
- The **JQL (Jira Query Language) query or filter** to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). If you don’t add any and click “Load”, the gadget will request all the content in the source instance, this might cause performance issues. We recommend adding at least one clause, for example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- The **SLA** to display the data from, remember that these SLAs are the ones provided by the <https://appfire.atlassian.net/wiki/spaces/TTSC> app.
- The **Time for Recently Breached**:the period of time you want to display issues that have been breached recently. The issues with an SLA breached in the Last day, Last week, Last 2 weeks or Last month.
- The **View** **type**

  - **List View**, where issues are displayed in a table-like format to maximize the number of items displayed.
  - **Extended View**, where issues are displayed in a cleaner and more visual way.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration