# Migrating to Jira Cloud with Configuration Manager for Jira

JSU has been integrated with Configuration Manager for Jira (CMJ) and the Configuration Manager Cloud Migration Tool, providing a new migration path for Jira space workflows customized with JSU.

If you use CMJ and JSU for Jira Data Center, you can now migrate your JSU configurations and data to a Jira Cloud instance to meet more of your migration needs.

## How do I use the Configuration Manager Cloud Migration Tool?

You can learn more about using the migration tool in the [Cloud Migration Tool documentation](https://appfire.atlassian.net/l/cp/2p0GJSdX). If you want to start a free trial of CMJ Cloud, visit the [CMJ listing](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) on the Atlassian Marketplace.

## What do I need?

To migrate JSU workflow data to Jira Cloud using CMJ, you will need CMJ Cloud on your target cloud instance and the free Configuration Manager Cloud Migration Tool installed on your source server instance.

|  |  |
| --- | --- |
| **Installed on Source (Server/Data Center)** | **Installed on Destination (Cloud)** |
| JSU Automation Suite for Jira Workflows v2.48.0 or later | JSU Automation Suite for Jira Workflows |
| Configuration Manager Cloud Migration Tool v3.1.0 or later | Configuration Manager for Jira |

It is highly recommended that you **test your migration** on a **staging Cloud instance** so you can become familiar with the results, before proceeding with a migration of your Server app data to your production Cloud instance.

You should also review our [feature parity page](/cms_trial/space/JSUCLOUD/12519139/JSU+Data+Center+vs+Cloud+feature+comparison/), particularly the references to Screen Security Configuration on Jira Cloud and the behavior of the Perform As User feature in JSU Cloud.

## Limitations

The integration for JSU supports the migration of Jira workflow JSU configurations and data, including post functions, conditions, validators, and other mappings with the following limitation:

**JQL**: For each migrated JQL query, JSU returns a warning message in the Migration report. In some cases, the query remains valid in the Cloud instance; in others, it must be reconfigured.

You will need to review the migrated JQL queries to determine which need to be reconfigured as part of a post-migration task.

## Can I access my migration reports in JSU?

Yes. Once a successful migration is complete, you can view the report and manage your migrations in the Cloud Migration Tool and JSU’s [*Migration Reports*](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/171016193) page.

## What’s the difference between the CMJ Migration Tool and Atlassian’s Jira Cloud Migration Assistant?

Appfire’s [Cloud Migration Tool](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CMT&title=Installation%20and%20upgrade) and Atlassian’s Jira Cloud Migration Assistant (JCMA) can migrate Jira DC spaces and their work items to Jira Cloud. Both offer safe and reliable migrations to Jira Cloud. If you are considering either option for your migration needs, see <https://appfire.atlassian.net/wiki/spaces/SUPPORT/pages/315326465> to learn more about their benefits and key differences. If you have additional questions or need help with CMJ, submit a request through our [support portal](https://appf.re/support).