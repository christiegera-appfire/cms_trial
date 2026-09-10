# Migrating from Data Center

The JMCF app has an automated migration path and can be migrated from **Jira Data Center**; migration requires JMCF for Jira Data Center version 2.5.1 or later. Migration is currently supported using [Jira Cloud Migration Assistant (JCMA)](https://support.atlassian.com/migration/docs/jira-cloud-migration-assistant/) automation only.

Be aware that **JMCF** migration using JCMA is currently in Beta, so you may wish to test the JMCF migration in a trial or test Cloud instance.

**Note:** If you have already migrated to the Cloud and need information regarding how to fix errors, see the [Post Migration page](/cms_trial/space/JMCFC/1465843750/Post+migration/).

## Before you start

1. Make sure you are running **JMCF for Data Center** version 2.5.1 or later.
2. Review the [Feature comparison](/cms_trial/space/JMCFC/1466236964/JMCF+Cloud+vs.+JMCF+Data+Center/) between **JMCF for Jira Data Center** and **JMCF for Jira Cloud**.
3. Read and follow the instructions in [Atlassian’s documentation on Jira Cloud Migration Assistant (JCMA)](https://support.atlassian.com/migration/docs/use-the-jira-cloud-migration-assistant-to-migrate/).

#### Please note:

- The Atlassian APIs do not enable the transfer of large numbers of custom fields; for larger instances with numerous custom fields, you may need to migrate them in batches.
- Due to a bug in JCMA, field context migrations are limited. For custom fields with more than one context, JCMA will only migrate the first context.
- Due to the difference in supported scripting languages between Jira Data Center and Jira Cloud, scripted custom fields will need to be manually recreated; [***scripts will need to be rewritten in JavaScript***](/cms_trial/space/JMCFC/3228467202/Calculated+fields+not+displaying+values+in+JMCF/).
- Formatting applied in Jira Data Center will not be migrated to Jira Cloud - only the definition of the custom field will be migrated.

You are viewing the documentation for **Jira Cloud**.