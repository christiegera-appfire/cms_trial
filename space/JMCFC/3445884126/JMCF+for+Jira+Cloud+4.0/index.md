# JMCF for Jira Cloud 4.0

This version, released on November 7, 2024, includes the following changes:

Be aware that **JMCF** migration using JCMA is currently in Beta, so you will want to test the JMCF migration in a trial or test Cloud instance.

## Migration

### Migrating to JMCF Cloud

Migration of JMCF custom fields is now supported between Jira Data Center and Jira Cloud using [Jira Cloud Migration Assistant (JCMA)](https://support.atlassian.com/migration/docs/jira-cloud-migration-assistant/).

### Known issues

Migrating using JCMA is currently in Beta; there are a few known issues with migration. You should test your migration thoroughly before running it in a production environment!

- The Atlassian APIs do not enable the transfer of large numbers of custom fields; for larger instances with numerous custom fields, you may need to migrate them in batches.
- Field context migrations are limited due to a bug in JCMA. For custom fields with more than one context, only the first context will be migrated by JCMA.
- Due to the difference in supported scripting languages between Jira Data Center and Jira Cloud, scripted custom fields will need to be manually reconfigured; scripts will need to be rewritten in JavaScript.

---

▢ **Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the Marketplace.
- Stuck with something? Raise a ticket with our support team.
- Do you love using our app? Let us know what you think here.

▢ **Credits**

A heartfelt thank you to our valued customers! Your incredible support and feedback inspire us to improve our apps and products continually. You are the driving force behind why we create software. We appreciate your trust in JMWE!

|  |  |
| --- | --- |
| **Release date** | November 7, 2024 |
| **Highlights** | - Migration support using JCMA |
| **Tags** | migration |