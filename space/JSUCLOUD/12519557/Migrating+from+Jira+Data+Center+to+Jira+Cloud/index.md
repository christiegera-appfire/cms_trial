# Migrating from Jira Data Center to Jira Cloud

JSU for Jira Cloud is approved for [Atlassian Government Cloud (AGC)](/cms_trial/space/JSUCLOUD/2165083529/Atlassian+Government+Cloud/). AGC is an Atlassian cloud environment for US government agencies, currently an EAP.

JSU supports migration from Jira Data Center to Jira Cloud using the Jira Cloud Migration Assistant (JCMA), but *migration to AGC using JCMA is not currently supported for any Marketplace app*; this is an Atlassian limitation and cannot be resolved by Appfire. Please see Atlassian ticket [MIG-2403](https://jira.atlassian.com/browse/MIG-2403) for more information.

If you use JSU Data Center and are planning a migration to Jira Cloud, you can use Atlassian’s JCMA or Appfire’s Configuration Manager for Jira (CMJ) Cloud Migration Tool to migrate most of your JSU workflow configurations.

We recommend that you test your migration on a **staging** Cloud instance so you can become familiar with the results before proceeding with a migration of your Data Center app data to your production Cloud instance. You can use a free trial of CMJ on a staging instance to determine which tool works best for your needs.

To learn more about migrating your JSU app and its workflow rules from Jira Data Center to Jira Cloud, see the [Jira Cloud Migration Assistant](https://appfire.atlassian.net/wiki/spaces/JSU/pages/12684875) page. If you use Configuration Manager for Jira, see the [Configuration Manager for Jira](/cms_trial/space/JSUCLOUD/1721834794/Migrating+to+Jira+Cloud+with+Configuration+Manager+for+Jira/) page.

## Before you migrate

Before starting your migration, verify that:

- Your Jira instance is running a supported Atlassian version.
- You are using the latest supported version of JSU.
- You are using the latest version of the Jira Cloud Migration Assistant (JCMA).
- You have reviewed any migration limitations and known issues. Using outdated Jira, JSU, or JCMA versions may result in migration failures or incomplete migration results.
- You have reviewed our [feature comparison tables](/cms_trial/space/JSUCLOUD/12519557/Migrating+from+Jira+Data+Center+to+Jira+Cloud/) to understand the differences between our Cloud and Data Center apps. We also note differences between Jira Data Center and Jira Cloud that must be considered to help resolve any potential errors.

See our full feature parity in [JSU Data Center vs Cloud feature comparison](/cms_trial/space/JSUCLOUD/12519139/JSU+Data+Center+vs+Cloud+feature+comparison/).

## Feature summary

|  |  |
| --- | --- |
| **Post functions** | All the post functions we offer on Jira Data Center are also available on Jira Cloud. |
| **Preconditions for post functions** | All the preconditions we offer for Jira Data Center are also available on Cloud. Note that preconditions are no longer separate from post functions; they are now part of the post function. See [Workflow Preconditions](/cms_trial/space/JSUCLOUD/12518025/Workflow+preconditions/) for more information. |
| **Conditions** | Due to technical limitations, JSU for Jira Cloud provides only the [User Is In Any Users](/cms_trial/space/JSUCLOUD/12518827/User+Is+In+Any+Users+condition/) condition. Most conditions provided in JSU for Jira Data Center are now integrated and maintained by Atlassian for Jira Cloud.  The Status Changed and JQL conditions are not supported in Jira Cloud. |
| **Validators** | All validators provided in JSU for Jira Data Center are supported by Atlassian and are transformed into native validators in Jira Cloud. |
| **Custom Fields** | Due to technical limitations, the three custom fields we provide in JSU for Jira Data Center (Location, Location Select, and Directions) are not available on JSU for Jira Cloud. |
| **Space Variables** | JSU for Jira Data Center provides functionality to store variables per space, which can then be used in workflow post functions. This feature is not currently supported on Jira Cloud; it's in the roadmap, and we will let you know as soon as it's available. |

If you are looking for information about **JSU Cloud to Data Center** migration, see  [Migrating from Jira Cloud to Jira Server](https://appfire.atlassian.net/wiki/x/dgi-/).