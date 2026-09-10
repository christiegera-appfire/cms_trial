# Supported configuration elements

## Supported configuration elements in cloud-to-cloud deployments

The table below lists the configuration elements that CMJ Cloud and CMT are able to deploy through snapshots.

✅ Supported

❌ Not yet supported

⚠️ Supported with some specifics

| **Configuration** | **CMJ Cloud** |
| --- | --- |
| Projects |  |
|  | Jira company projects | ✅ |
|  | Тeam-managed projects | ❌ |
|  | Jira Service Management (JSM) projects | ⚠️  Only partial deployment is available. See the full list of currently [supported JSM configurations](/cms_trial/space/CMJC/1160020327/Migrate+Service+Management+projects+to+the+Cloud/). |
|  | Product discovery projects | ❌ |
|  | Customer service management projects | ❌ |
| Agile boards | ✅ |
| App data | ⚠️  Only includes data for the apps [listed here](https://appfire.atlassian.net/wiki/spaces/AppIn/pages/2872607748). |
| Custom fields | ✅ |
| Dashboards | ❌ |
| Events | ⚠️  Custom events cannot be created yet. They can only be referenced if they already exist on the destination instance. |
| Field Configurations | ✅ |
| Filters | ⚠️  Only the filters associated with boards in the deployment scope are moved. JQL isn’t transformed. |
| Field layouts | ✅ |
| Groups | ⚠️  Group membership will not be transferred |
| Issues | ❌ |
| Issue Link Types | ✅ |
| Issue Types | ✅ |
| Priorities | ✅ |
| Project Categories | ✅ |
| Schemes |  |
|  | Field Configuration Schemes | ✅ |
|  | Issue Security Schemes | ✅ |
|  | Issue Type Screen Schemes | ✅ |
|  | Notification Schemes | ✅ |
|  | Permission Schemes | ✅ |
|  | Screen Schemes | ✅ |
|  | Workflow Schemes | ✅ |
| Screens | ✅ |
| Sprints | ✅ |
| Statuses | ✅ |
| Resolutions | ✅ |
| Roles | ✅ |
| Users | ✅ |
| Workflows | ✅ |

### Specifics of deploying boards and filters

When deploying boards and filters from a Jira Cloud site, CMJ Cloud is able to:

- add the ones that don’t exist in the destination Jira Cloud, and
- modifies the existing ones on the destination Jira Cloud if differences are detected.

However, when migrating from [Jira Server to Cloud](https://appfire.atlassian.net/wiki/spaces/CMT/pages/197922405), Jira Server boards, filters, and sprints are only added to Jira Cloud. For such migrations, the boards, filters, and sprints existing in the destination aren’t modified in any way.