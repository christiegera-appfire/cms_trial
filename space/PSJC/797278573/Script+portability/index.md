# Script portability

The Simple Issue Language (SIL), included with Power Scripts for Jira Cloud and Power Scripts for Data Center, is designed to keep scripts portable across Jira environments. In most cases, you can move SIL scripts between Jira Data Center and Jira Cloud with minimal rewrites. This page explains what remains compatible, what changes during migration, and which platform differences can affect your scripts.

Simple Issue Language (SIL) is practically identical on Jira DC and Jira Cloud.

## Why SIL makes your scripts super portable

One of the main benefits of SIL is that scripts are portable across instances and hosting types. This is possible because the SIL language was created to run at a higher level than a general programming language. It functions as a domain-specific language that simplifies scripting, reducing implementation complexity while preserving scripting flexibility.

## Benefits of SIL portability

Appfire places a lot of importance on ensuring your scripts can migrate from older versions of Jira to newer ones without requiring any changes. That's why Power Scripts uses the simple, JavaScript-like language SIL instead of Java-based scripting approaches, which often require additional maintenance during upgrades. The benefits include:

- Scripts written in older versions work in any future version.
- You can migrate scripts from DC to Cloud without rewriting.
- No modifications are needed when upgrading Jira.

---

## What differences to expect when migrating scripts

### Function differences between Data Center and Cloud

Since the SIL language depends on the Jira API, differences between the DC and Cloud APIs can subsequently affect SIL functions. Even though most Atlassian APIs are similar across hosting types, there are occasional differences, illustrated in the example below.

For example, when adding a comment on the DC version, you can set its visibility to a group or a project role. On Cloud, you can only use a project role.

Of the more than 700 Power Scripts functions available in the Cloud, only 0.4% differ from their Data Center equivalents.

### Power Scripts DC functions that are not available in the Cloud

Some DC Jira functions aren't available in the Cloud. For example, administrator functions for Jira reindexing aren't necessary in the Cloud. Other functions aren't available for two reasons:

- Atlassian API limitations.
- Cloud function development is still in progress.

Appfire is continually adding new features to make Power Scripts even more powerful. We’ve added 200+ new functions, and soon, there will be more Cloud functions than DC functions.

---

## What adjustments are required when migrating

Unfortunately, some changes will still be required due to architectural differences between the DC and Cloud versions.

### Configuration differences that can affect scripts

A minor difference can stem from the distinction between a Data Center and Cloud instance, but could also be due to different instances running on the same platform. For example, differences between a development instance and a production instance, even if both are running on Data Center, could affect scripts. These are usually differences in configurations or settings.

#### **Concrete names versus aliases**

If a script uses concrete configuration names instead of aliases, it needs to be updated. This applies to:

- Custom field ID’s
- Project names or keys
- Status/priority names
- Issue type names (or any other object that has a name)

#### **Permission settings**

In Power Scripts, each script runs as a user, inheriting that user's permissions. If permissions differ between Jira versions or hosting types, this can impact your script.

### Differences that will impact your scripts

Issues arise when Jira Data Center and Jira Cloud functionality differs, and scripts become incompatible.

#### **Conditions and Validators**

When Jira Cloud was launched, custom conditions and validators didn’t exist. This is because they were incompatible with the Jira Cloud architecture. Performing an action in the Cloud sets off a chain reaction of microservices and events all at once. Conditions and validators require a pause in those events while they determine what should happen next. Since Cloud doesn’t support this workflow, Atlassian released the expressions language, the only way to create custom conditions and validators.

This means that SIL scripts written for Data Center will need to be rewritten using the expressions language, reimagined to support the Cloud product, or removed entirely.

#### **JQL functions**

Jira Cloud has a feature that’s similar to the JQL functions available in DC versions. However, they aren’t real JQL functions that are executed during a search and run to determine if an issue should be included in the results as part of the query. Instead, the results are pre-calculated in the Cloud, and the JQL functions query the result. That’s why they’re called JQL aliases in the Cloud; they act similarly to JQL functions in Data Center. JQL functions used on Jira Data Center will need to be rewritten to accommodate differences in Jira Cloud. Scripts that could be executed as part of a [custom JQL search](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489314) will need to be rewritten as custom [JQL keyword (alias)](/cms_trial/space/PSJC/490997951/Custom+Keywords/) scripts.

#### **Live Fields**

Atlassian recently introduced the ability to create functionality such as Live Fields. As they have released only a few APIs for a select set of custom fields, Live Fields in Jira Cloud won’t be as powerful as its Data Center predecessor.

To reduce the number of changes:

- **Use SIL aliases**: by using SIL aliases, you avoid using the custom field ID directly in the script, protecting it from changes.
- **Clean up old projects prior to migration**: make any necessary project changes in your familiar environment rather than dealing with them in the new and unfamiliar Cloud setting.
- **Use migration tools like CMJ**: Did you know that Power Scripts is compatible with the [Configuration Manager Cloud Migration Tool](https://appfire.atlassian.net/wiki/spaces/CMT)? Configuration Manager helps analyze and report changes so that they can be resolved prior to the migration.