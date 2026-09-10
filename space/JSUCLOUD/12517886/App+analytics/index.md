# App analytics

JSU Automation Suite for Jira Workflows captures analytics data and stores it in a private analytics database hosted by Amazon Web Services (AWS) in the United States of America. The app collects a limited amount of anonymized data to help us decide where to invest for future releases.

### What data do we capture?

- [Tenant-related](https://www.atlassian.com/trust/reliability/cloud-architecture-and-operational-practices#tenant-provsioning-and-lifecycle) information (required by Atlassian)
- JCMA migration data for detailed reporting
- Error logs are stored in AWS for error analytics
- Anonymized usage statistics arecollected to help us make product and feature improvements

### Events

|  |  |  |
| --- | --- | --- |
| Install | collected each time the app is installed |  |
| Uninstall | collected each time the app is uninstalled |  |
| License updated | collected each time the license is updated |  |
| Enable | collected each time the app is enabled |  |
| Disable | collected each time the app is disabled |  |
| Configuration (various) | collected when an operational behavior is modified by a user with any admin level permission, for example, post function is added or updated, app-specific permissions are changed, or a global configuration change. |  |
| Active use (various) | collected when the app performs an operation that impacts the user experience *directly* as a direct result of user (of any role or permission) interaction, for example, interacts with a survey, or updates a work item. |  |
| Passive use (various) | collected when the app performs an operation that impacts the user experience *indirectly* as a result of user (of any role or permission) interaction, regardless of the user’s perception of the impact of the action, for example, a post function executes when a user transitions a work item. |  |
| Scheduled event | monthly poll to collect the number of users of Jira products |  |
| Error | collected when an error is reported to a user, describing the context and event of the error |  |

---

See our [Appfire Trust Center](https://trust.appfire.com/) for more information on security, data processing, and privacy policies that are in effect for all Appfire apps.