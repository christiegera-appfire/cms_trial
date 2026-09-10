# 7pace Timetracker migration questions

## Can I migrate 7pace Timetracker data from one DevOps server to another?

Is it possible to migrate 7pace Timetracker data from one DevOps server to a different DevOps server?

### Answer

Unfortunately, we **do not** support any migrations between DevOps servers.

On each DevOps server, there is a unique set of IDs (Guid's) for Users and Collections, and we map Timerecords on these IDs. Because the second DevOps server has different IDs for the same User/Collection, we cannot map Timerecords from the TimetrackerDB with IDs from first DevOps server. For 7pace Timetracker, these unknown IDs are another or new Collections/Users.

Please note that any manual changes made to the database by users will render 7pace Timetracker in an unsupported state.

We do support updates to DevOps Server on the same machine; for more information, please click [here](/cms_trial/space/7TFA/1253539922/Installation+guide/).

## Can I migrate 7pace Timetracker data from DevOps server to the Cloud?

Is it possible to migrate 7pace Timetracker data from DevOps server to the Cloud?

### Answer

Yes. There are two options for migrating your data to the Cloud:

1. Export/Import  
   With this option, [export worklogs from the Budgets page](/cms_trial/space/7TFA/1253540085/Budgets/), and then use the [import feature](/cms_trial/space/7TFA/1253540013/Times+Explorer/) on the Times Explorer page.
2. Use the [NPM package that utilizes our REST CRUD API](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/).

For assistance with migrations, please [contact our support team](https://appfire.atlassian.net/servicedesk/customer/portal/35).