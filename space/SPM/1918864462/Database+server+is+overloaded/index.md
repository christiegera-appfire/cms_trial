# Database server is overloaded

In case of contacting our Support Team via [our portal](https://appfire.atlassian.net/servicedesk/customer/portal/11) or [e-mail](mailto:support@bigpicture.one) **for the first time**, please remember to:

- Describe a problem in detail.
- Collect the required data (described below) and **attach** it to the request.
- Provide an exact timestamp when a problem occurred.

If you have contacted the Atlassian Support Team regarding performance problems before and have a preliminary analysis, let us know and add our **Support Team** to that ticket.

**Problem:**

A database administrator observes that the database server is overloaded (for example, CPU usage for the database server is high or long-running queries that come from BigPicture / BigGantt / BigTemplate).

To make sure that these queries come from our BigPicture, check if table prefixes in the Jira database begin with:

1. AO\_0456E7\_ - for BigPicture
2. AO\_8AC478\_ - for BigGantt
3. AO\_DA6AB9\_ - for BigTemplate

**Required data to collect and send to the Support Team:**

- Data that your database administrator delivered to you (specific long-running queries, CPU usage for the database server graphs, etc.).
- Database monitoring:

  1. Go to the **App Configuration > Advanced > Technical info** page.
  2. Navigate to the **Monitoring** section and **switch on** the **Database monitoring** option.
  3. Reproduce the problem (it may take up to a few hours).
  4. If you managed to reproduce the issue, return to the **Technical info** page.
  5. Download logs by clicking **Download support zip** under the **Support data** section.
  6. Navigate to the **Monitoring** section and **switch off** the **Database monitoring** option. Otherwise, server resource consumption may be slightly higher due to the increased amount of logs.