# DC to Cloud migration guide

Here is what you need to know about migrating your Jira Data Center (DC) instance with Planning Poker to Jira Cloud.

## 1. DC to Cloud migration

Planning Poker app will appear in [Jira Cloud Migration Assistant](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant?hosting=server&tab=overview) to allow a smooth transition from DC to Cloud.

Most Planning Poker data is migrated one-to-one, including general configuration.

### 1.1. Not migrated

Personal **Asynchronous** **estimates** on each issue will not be migrated. Finish your [Asynchronous estimations](/cms_trial/space/PP/9568542/Planning+Poker+tab+estimation+(Cloud)/) in progress before the migration as their state won’t be transferred.

### 1.2. Special cases handling

- Planning Poker games are not linked to a specific Jira Project and might contain issues from multiple projects. It is possible that some projects and related issues are not migrated. In the case of having **non-migrated issues in the migrated games**, such issues will be blank and will display only issue IDs. Such issues can be removed from games by using the Edit Backlog screen.
- In case if Project is not migrated then corresponding custom fields from this Project will also not be migrated. If you have such custom fields configured as the **Estimation field** for the game you will need to select a new one after the migration. The same applies if the configured **Estimation field** was **Original Story Points** which is not available in Jira Cloud.

### 1.3. Migration troubleshooting

We highly recommend enabling logging for Planning Poker. In order to do that you need to add `lizardbrain.planning_poker.migration` with `info` level at Jira DC’s logging and profiling page ([more info](https://confluence.atlassian.com/jirakb/change-logging-levels-in-jira-server-629178605.html)).

The following log entries will appear during each migration process:

```text
2022-04-21 ... INFO ServiceRunner     [l.planning_poker.migration.CloudMigrationHandler] MIGRATION STARTED...
2022-04-21 ... INFO ServiceRunner     [l.p.migration.provider.MigrationDtoProvider] Preparing MigrationDto...
2022-04-21 ... INFO ServiceRunner     [l.p.migration.provider.MigrationDtoProvider] MigrationDto: MigrationDto(...)
2022-04-21 ... INFO ServiceRunner     [l.planning_poker.migration.CloudMigrationHandler] Writing app data on the cloud ... 
2022-04-21 ... INFO ServiceRunner     [l.planning_poker.migration.CloudMigrationHandler] App data is written.
2022-04-21 ... INFO ServiceRunner     [l.planning_poker.migration.CloudMigrationHandler] MIGRATION DTO CREATED
```

We have put a limit on the maximum size of the Planning Poker data migration bundle. In case if that limit is exceeded you’ll see a corresponding message in the migration log. Please contact our [Support team](mailto:support@appfire.com) to get help then. We anticipate no customers will run into this limit but we have protected our systems from the unexpectedly large data sets.

### 1.4. Repeating the migration

Already migrated sessions will be skipped from further migrations unless they are removed from the Cloud instance, in this case, they will be migrated again.

---

**We are here to help!** In case you need any guidance or help during your migration process, please do not hesitate to [contact us](mailto:support@appfire.com) – we'll be glad to help! We'd also love to listen to your organization's specific needs, so we can adjust product development plans.