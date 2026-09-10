# Integration guides

Power Scripts for Jira Cloud offers integration capabilities for orchestrating data flow between various systems without custom interface development.

These capabilities match those available in the Data Center version, maintaining the same powerful functionality that users value in self-hosted environments. All connections to integrated systems can be secured using [TLS certificates](/cms_trial/space/PSJC/601819283/TLS+%2F+SSL+configuration/).

| **With the…** | **You can…** |
| --- | --- |
| [Outgoing mail integration](/cms_trial/space/PSJC/490996015/Outgoing+Mail+configuration/) | Send customized emails using templates with support for multiple languages based on sender or receiver preferences. Include attachments as needed. |
| [Incoming mail integration](/cms_trial/space/PSJC/994018140/Incoming+Mail+configuration/) | Process incoming emails with access to complete message content, including headers. Scripts determine appropriate actions such as creating issues, adding comments, or processing attachments. |
| [Datasource integration](/cms_trial/space/PSJC/490996148/SQL+Datasource+configuration/) | Connect directly to Postgres, MySQL, Oracle, or SQL Server databases to retrieve and manipulate data without separate interfaces. |
| [LDAP integration](/cms_trial/space/PSJC/490995973/LDAP+configuration/) | Connect your Jira Cloud instance to your organization's directory services, enabling SIL scripts to authenticate users, retrieve user information, and maintain consistency between Jira and your enterprise user management system. |
| [Webhooks](/cms_trial/space/PSJC/490996447/Webhook+configuration/) | Extend your Jira functionality by creating custom API endpoints that execute your SIL scripts. This integration enables external systems to interact with your Jira instance through standard REST calls from any HTTP client. |
| [Slack integration](/cms_trial/space/PSJC/490995941/Slack+integration/) | Send automated messages from Jira to your Slack channels, notifying team members about ticket activities such as new issues, updates, comments, or status changes without manual intervention. |
| [Remote systems integration](/cms_trial/space/PSJC/490996050/Remote+systems+configuration/) | Execute SIL scripts on other Jira or Confluence instances that also have Power Scripts or another SIL-based app installed, enabling cross-system automation and data exchange. |