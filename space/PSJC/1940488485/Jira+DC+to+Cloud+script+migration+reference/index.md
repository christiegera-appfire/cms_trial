# Jira DC to Cloud script migration reference

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

The following table provides information about the expected outcome of script migration by script type. It shows which scripts:

- Are expected to migrate without any significant changes (marked with ✅ in the table).
- Will migrate, but significant changes are required (marked with 🟡).
- Will not migrate or the feature is not available in Jira Cloud (marked with ❌).

For additional details, see [Scripts requiring changes when migrating](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/edit-v2/1940488352#Scripts-requiring-changes-when-migrating).

| **DC script type/feature** | **Migrates** | **Feature in Cloud** | **Notes** |
| --- | --- | --- | --- |
| [Workflow conditions](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487273) | 🟡 | ✅ | Condition scripts use [Jira Expressions](https://developer.atlassian.com/cloud/jira/software/jira-expressions/) in Jira Cloud and not SIL unless [rewritten in a different way](/cms_trial/space/PSJC/804552898/Scripted+Conditions+and+Validators+in+cloud+-+a+new+paradigm/). |
| [Workflow validators](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487273) | 🟡 | ✅ | Validator scripts use [Jira Expressions](https://developer.atlassian.com/cloud/jira/software/jira-expressions/) in Jira Cloud and not SIL unless [rewritten in a different way](/cms_trial/space/PSJC/804552898/Scripted+Conditions+and+Validators+in+cloud+-+a+new+paradigm/). |
| [Workflow post functions](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487273) | ✅ | ✅ |  |
| [Listeners](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480908) | ✅ | ✅ |  |
| [Scheduler](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480692) | ✅ | ✅ |  |
| [Start/Stop scripts](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15481432) | ❌ | ❌ | This feature will not be added to Jira Cloud. |
| [Live Fields scripts](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488008) | 🟡 | ✅ | [Live Fields](https://appfire.atlassian.net/wiki/spaces/LF) is written in JavaScript using [Atlassian APIs](https://appfire.atlassian.net/wiki/spaces/LF/pages/1497662612) in Jira Cloud. |
| [Mail handler scripts](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480237) | 🟡 | ✅ | Incoming email scripts use a [different set of functions](/cms_trial/space/PSJC/999162356/Incoming+Mail+Processing+Functions/) in Jira Cloud. |
| [Remote systems](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15486952) | ✅ | ✅ |  |
| [SIL Panel](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489795) | ✅ | ✅ |  |
| [SIL Runner Gadget](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480445) | ✅ | ✅ |  |
| [SIL Template Language](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488414) | ✅ | ✅ |  |
| [Scripted JQL functions](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489314) | 🟡 | ✅ | The concept of [JQL functions is different in Jira Cloud](/cms_trial/space/PSJC/490997937/JQL+Support/). All scripts need to be modified to reflect this. |
| [JSM automation scripts](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480521) | ❌ | ❌ | Feature not currently available in Jira Cloud. May not be added. |
| [Jira automation scripts](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489219) | ❌ | ❌ | Feature not currently available in Jira Cloud. May be added H2 2025 at the earliest. |
| [Webhooks](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489512) | ✅ | ✅ |  |