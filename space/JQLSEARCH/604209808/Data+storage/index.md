# Data storage

Issues that you keep in Jira are extremely important to your business and we make sure that data is properly protected.

### JQL Search Extensions system

The following information is stored in the app’s system:

- installation information necessary for the app to communicate with Jira; including the encrypted token
- user-created queries (filters, su‌bqueries etc.)
- issues, fields, and projects cache necessary to fulfill the app’s functional and performance requirements
- logs for support purposes containing information like Jira issue ids and Jira instance identifiers

Data is automatically removed within a month after uninstallation of the app.

### Stored in Jira

Indexing metadata on issues and other Jira entities

### Data region

JQL Search Extensions stores data in [Atlas Mongo](https://www.mongodb.com/) hosted by [Amazon Web Services](https://aws.amazon.com/) infrastructure in Oregon, United States.

Data in Jira is stored according to your Jira data residency configuration.