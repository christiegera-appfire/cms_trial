# Migrating JMWE

The JMWE app has an automated migration path and can be migrated from **Jira Data Center**; migration requires JMWE for Jira Data Center version 7.2.0 or later. Migration is currently supported using [Jira Cloud Migration Assistant (JCMA)](https://support.atlassian.com/migration/docs/jira-cloud-migration-assistant/) automation or [Configuration Manager for Jira (CMJ)](/cms_trial/space/JMWEC/466288825/Migrating+Using+Configuration+Manager+for+Jira+(CMJ)/).

**Note:** If you have already migrated to the Cloud and need information regarding how to fix errors, see the [Post Migration page](/cms_trial/space/JMWEC/465473765/Post+migration/).

## Before you start

1. Make sure you are running **JMWE for Data Center** version 7.2.0 or later.
2. Review the [Feature comparison](/cms_trial/space/JMWEC/465473954/Feature+Comparison+-+JMWE+Data+Center+vs.+JMWE+Cloud/) between **JMWE for Jira Data Center** and **JMWE for Jira Cloud**.
3. Read and follow the instructions in [Atlassian’s documentation on Jira Cloud Migration Assistant (JCMA)](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/).

#### Please note:

- Currently, Shared actions, Event-based actions, and Scheduled actions **are** migrated, but due to some feature differences, it is **highly recommended** that you verify these actions after migration.
- Any JMWE conditions, validators, and/or post-functions where you employed Groovy scripting will throw errors and will need to be updated with either [Jira expressions](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) or [Nunjucks expressions/scripts](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/).
- Because Jira Cloud runs post-functions after a transition completes, there are no error handling capabilities in Jira Cloud to prevent transitions from completing. Post-functions that include error handling in your Data Center instance will display warnings on the Post-migration page.