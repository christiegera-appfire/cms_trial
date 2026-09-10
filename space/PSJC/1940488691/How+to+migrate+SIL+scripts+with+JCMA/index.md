# How to migrate SIL scripts with JCMA

Power Scripts will be unavailable during scheduled maintenance on July 18-19, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

When using Atlassian’s [Jira Cloud Migration Assistant](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant?tab=overview&hosting=datacenter) (JCMA) to migrate your Jira DC instance to Jira Cloud, you can transfer many of your existing SIL scripts during your cloud migration process. JCMA can handle the migration of scripts between the two environments as part of the overall migration procedure. There are specific considerations to ensure successful script migration, and this guide outlines what you can expect when migrating your SIL scripts, including what gets migrated, what doesn't, and the necessary post-migration actions to ensure your scripts continue functioning properly in the cloud environment.

---

## Before you begin

Before migrating your SIL scripts, learn more about how JCMA works and prepare your environment properly. JCMA migrates your Jira DC configuration first, followed by the Power Scripts app migration.

For comprehensive information about JCMA capabilities and processes, refer to:

- [JCMA documentation](https://support.atlassian.com/migration/docs/jira-cloud-migration-assistant/)
- [What gets migrated with JCMA](https://support.atlassian.com/migration/docs/what-gets-migrated-with-the-jira-cloud-migration-assistant/)

### How to prepare your scripts for migration

Review the comprehensive [SIL script migration guide](/cms_trial/space/PSJC/1940488352/SIL+scripts+migration+guide/) for detailed information about prerequisites, necessary consistencies, and step-by-step instructions for automated script migration.

---

## What gets migrated

During Power Scripts migration with JCMA, some of the app configurations and their associated scripts automatically transfer from Jira DC to Cloud. However, due to fundamental differences in Jira Cloud's architecture, some configurations may require additional adjustments post-migration.

| **Configuration tab** | **What gets migrated** |
| --- | --- |
| General | - Some configurations and settings, such as Charset and Max Script Runtime. |
| Advanced | - Scheduler - Listeners - Panels - Workflows post-functions |
| Integrations | - Some Mail Sender Options configurations relevant to Jira Cloud - Datasources - Web Hooks  - Slack |
| Other | SIL Runner Gadgets  Only the configuration settings are migrated. After the migration, you must [add the gadgets](/cms_trial/space/PSJC/490996338/SIL+Runner+Gadget+configuration/) to a Jira Cloud dashboard. |

---

## What does not get migrated

The table below summarizes which script components cannot be automatically migrated to Jira Cloud and what approach you should take for each component.

| **Unsupported script components** | **What to do about it** |
| --- | --- |
| Conditions and validators | Conditions and validators won't migrate because they require Jira Expressions in Jira Cloud instead of SIL.   - You must completely rewrite them using [Jira Expressions](https://developer.atlassian.com/cloud/jira/software/jira-expressions/). |
| Live Fields scripts | Live Fields scripts won’t migrate because they require JavaScript and Atlassian APIs instead of SIL.   - You must recreate these scripts using JavaScript.   Live Fields for Cloud has more limited functionality than the DC version, which might require developing workarounds where cloud features are missing. |
| JQL scripts | JQL functionality works differently in Jira Cloud. Your existing JQL scripts will not migrate automatically.   - You must reconfigure your JQL scripts. SIL provides utility scripts that can help with [JQL-related migration](/cms_trial/space/PSJC/1940488352/SIL+scripts+migration+guide/) by:    - Scanning your existing JQL filters to identify where DC keywords are used that won't work in Jira Cloud.   - Automatically updating those JQL filters to use Cloud-compatible keywords. |
| Native Jira automation and JSM-specific integration | The native [Jira automation support](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489219) and [Jira Service Management automation](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480521) features are either deprecated or do not exist in Jira Cloud. The scripts related to these features will not be migrated. |
| Some Listener event settings | The events that Listeners use in Jira DC do not map directly to Jira Cloud events. While the content of the scripts will be migrated, configurations referencing events without cloud mappings will not be created.   - You must manually create the necessary configurations in Jira Cloud. You can then use the migrated script content. |
| SIL aliases | The SIL Aliases configuration itself is not automatically migrated by JCMA; you must manually recreate these settings in your Cloud instance. However, if your scripts are already using aliases (instead of hardcoded custom field IDs), this is beneficial - after you manually set up the aliases in Cloud, your scripts will automatically work with the new custom field IDs. This makes scripts much more portable between environments. |
| Persistent variables | Like SIL Aliases, persistent variables migration will be implemented in a future release. These can also be migrated with custom scripts for now. |
| SIL settings | Some settings specific to the file system or system performance of your DC instance will not migrate as they may not be relevant in the cloud environment. These include SIL Cache size, Threads, SIL Home, Security, Templates directory, and Remotes. |

---

## How JCMA handles your scripts

Understanding the technical behaviors and outcomes of JCMA during the migration process will help you set proper expectations for your script migration. This section outlines specifically how JCMA processes your scripts during transfer - which scripts get copied, how dependencies are managed, what happens when the same script exists in both environments, and how configurations are handled. These points describe the actual migration mechanism and help you anticipate the state of your scripts immediately after the migration completes.

### Steps for migrating SIL scripts

Migrating scripts from Jira DC to Cloud involves a structured approach for different script types. The process includes preparing scripts by updating aliases, validating critical scripts like post functions and listeners first, and then addressing other script types in order of complexity.

For detailed step-by-step instructions, see [this page](/cms_trial/space/PSJC/1940488414/Automated+script+migration/).

### Script migration scope

JCMA will copy all scripts that are linked to configurations ([Post Functions](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15486855), [SIL Listeners](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480908), [SIL Schedulers](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480692), [Webhooks](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489512), [SIL Panel](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489795), [SIL Runner Gadget](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480445)) and their included dependencies. For scripts that reference other scripts using [inclusions](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487128), those included scripts will be migrated as well. JCMA automatically identifies all referenced scripts, including those nested at multiple levels, ensuring that all required scripts are migrated. The folder structure of the scripts migrated to Jira Cloud is consistent with the existing structure on Jira DC.

Scripts in the SIL Manager that are not linked to any configurations will not be migrated automatically. If you need these scripts, you must create a separate migration task.

### Script conflict handling

If a script already exists in the cloud with the same file location and name but different content, JCMA will do the following:

1. Create a backup of the cloud file by renaming it with a `.bac` extension.
2. Copy the Jira DC file to the Jira Cloud location.

For example, if you migrate `test.sil` to the cloud where a different `test.sil` already exists, JCMA will create `test.bac` containing the original cloud content, then replace `test.sil` with the DC version. Note that any cloud configurations pointing to the original `test.sil` will now reference the migrated content.

### Configuration duplication

For configurations like [SIL Scheduler](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480692), where the same script can be used multiple times, JCMA does not overwrite existing configurations during multiple migrations. Instead, configurations will be duplicated, potentially requiring cleanup after migration.

---

## What to do after the migration

Once JCMA migration is complete, perform these tasks to ensure scripts work correctly in Jira Cloud:

| **Task** | **Details** |
| --- | --- |
| Review supporting documentation | Consult these documentation resources to ensure proper configuration and optimization of your scripts in the cloud environment:   - [Script migration reference](/cms_trial/space/PSJC/1940488485/Jira+DC+to+Cloud+script+migration+reference/) - [SIL scripts migration guide](/cms_trial/space/PSJC/1940488352/SIL+scripts+migration+guide/) - [Useful tools and scripts for post-migration script adjustment](/cms_trial/space/PSJC/1940488576/Useful+tools+and+scripts+for+post-migration+script+adjustment/) - [SIL functions differences between Jira DC and Cloud](/cms_trial/space/PSJC/1940488545/SIL+functions+differences+between+Jira+Data+Center+and+Cloud/) |
| Review the migration summary document | Once the migration completes, you'll find a summary file in the `migrations` folder of the `kepler` home directory. This file contains details about migrated configurations and scripts. |
| Post-migration testing | Thoroughly test all migrated scripts and configurations to verify they function as expected in the cloud environment.  For details, see [Post-migration testing](/cms_trial/space/PSJC/1940488352/SIL+scripts+migration+guide/). |
| Configure SIL Listener events | Since event mappings for SIL Listeners might not migrate completely. After the migration, you must review and reconfigure Listener events in Jira Cloud appropriately. |
| Clean up duplicated SIL Schedulers | If you've performed multiple migrations, review and clean up any duplicated SIL Scheduler configurations that might have been created. |
| Migrate standalone scripts | Manually migrate any scripts that were not associated with a configuration, as these aren't automatically migrated by JCMA.  For additional information, see the [Backup and restore section](/cms_trial/space/PSJC/516456599/Managing+your+solution%3A+Self-Help/), which is part of Power Scripts for Jira Cloud [Self-Help](/cms_trial/space/PSJC/516456599/Managing+your+solution%3A+Self-Help/) feature. |
| Rewrite non-migrated scripts | You'll need to rewrite:   - Conditions and validators using Jira Expressions - Live Fields scripts using JavaScript - JQL scripts to work with Jira Cloud functionality   For additional information, see [Required post-migration script changes](/cms_trial/space/PSJC/1940488352/SIL+scripts+migration+guide/) sections and [Scripted conditions and validators in cloud - a new paradigm](/cms_trial/space/PSJC/804552898/Scripted+Conditions+and+Validators+in+cloud+-+a+new+paradigm/). |