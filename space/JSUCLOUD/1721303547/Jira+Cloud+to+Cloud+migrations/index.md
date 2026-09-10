# Jira Cloud to Cloud migrations

JSU Cloud to Cloud migrations are supported by an integration with Appfire’s **Configuration Manager for Jira (CMJ)**. If you use CMJ Cloud, you can now migrate your JSU Cloud workflow rules to another Jira Cloud instance. To start a free trial of CMJ Cloud, visit the [CMJ listing](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) on the Atlassian Marketplace.

## What can I migrate?

CMJ supports the latest version of JSU Cloud, including:

- **Conditions**

  - JSU Rule Builder - Conditions
  - User Is In Any Users (JSU)
- **Validators**

  - JSU Rule Builder - Validators
- **Post functions**

  - Access the Universal Rule Builder from JSU
  - Calculated Field (JSU)
  - Clear Field Value (JSU)
  - Copy / Move Attachments (JSU)
  - Copy Value From Other Field (JSU)
  - Create A Linked Issue (JSU)
  - Follow Up Transition (JSU)
  - Linked Transition (JSU)
  - Update Any Issue Field (JSU)

## Limitations

The integration for JSU allows the migration of JSU workflow rules with the following limitation:

**JQL**: For rules that include JQL queries, JSU returns a warning message in the Migration report. In some cases, the query remains valid in the Cloud instance; in others, it must be reconfigured.

You will need to review the migrated JQL queries to determine which need to be reconfigured as part of a post-migration task.

## How do I use CMJ for migrations?

Learn more about CMJ in our [documentation](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CMJC&title=Get%20started). To start a free trial of CMJ Cloud, visit the [CMJ listing](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) on the Atlassian Marketplace.

## What do I need?

You will need an active CMJ Cloud licence on both your source and destination cloud instances. The CMJ documentation includes more information about [prerequisites](https://appfire.atlassian.net/wiki/spaces/CMJC/pages/193659801).

## Can I use Jira’s Cloud Migration Assistant (JCMA)?

No, JCMA can only be used for migrations between Data Center and Cloud. JCMA does not provide a mechanism for apps like JSU to integrate with a cloud-to-cloud migration.