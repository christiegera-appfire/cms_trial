# I want to review cross-project SLA compliance data without manual spreadsheet exports

🤔 **Context:** A team lead needs a centralized view of historical SLA compliance across multiple projects or clients for routine performance monitoring and stakeholder reviews.

🌧️ **User problem:** Tracking performance across dozens of distinct Jira or Jira Service Management (JSM) projects usually requires manual effort. Teams often spend hours exporting CSV data and aggregating it in external spreadsheets to calculate company-wide compliance or client-specific delivery rates. Furthermore, if a metric shows a performance dip during a review or weekly audit, identifying the root cause requires manual investigation across individual projects and tickets, leading to delayed insights and administrative friction.

☔ **Solution:** Using Time to SLA’s Executive reports

The [Executive reports](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/3404431363/Executive+reports?atl_f=PAGETREE) feature provides a native, high-level overview of completed SLA data across multiple projects simultaneously, eliminating the need for external tools.

Image — asset pipeline pending  
Executive reports dashboard showing SLA compliance across multiple projects.

You can slice the data by dynamic time intervals (Daily, Weekly, Monthly, or Quarterly) and organize it using up to three levels of hierarchical grouping (for example, *Space > Priority > Assignee*). Color-coded thresholds (**Green**, **Yellow**, **Red**) allow you to spot performance drops instantly. If a specific timeframe or project shows a critical threshold warning, you can click directly on that hyperlinked cell to open a detailed view of the exact Jira work items driving that metric, providing total data transparency in seconds.

Image — asset pipeline pending  
Detailed Executive reports view showing SLA compliance metrics with drill-down links to Jira issues.

## Problem solved!