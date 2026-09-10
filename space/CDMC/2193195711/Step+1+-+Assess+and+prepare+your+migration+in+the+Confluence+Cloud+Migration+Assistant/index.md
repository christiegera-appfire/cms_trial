# Step 1 - Assess and prepare your migration in the Confluence Cloud Migration Assistant

## Overview

The [Atlassian Confluence Cloud Migration Assistant (CCMA)](https://marketplace.atlassian.com/apps/1219672/confluence-cloud-migration-assistant?hosting=datacenter&tab=overview) can transfer spaces, users, groups, and vendor app data to migrate Comala Document Management from a hosted instance.

You can assess and prepare your migration using the CCMA, which includes several assessments and checks. This includes assessing the **Apps** **needed in the Cloud**, checking app availability in Confluence Cloud, and checking vendor support for the migration. In addition, the assistant helps you review your users and email domains.

## Prerequisites

Several pre-requisite tasks are detailed in the [Migrate from Data Center to Cloud](/cms_trial/space/CDMC/3446374401/Migrate+from+Data+Center+to+Cloud+(Connect)/) page. These must be undertaken before migration and include:

- [Pre-requisite tasks](/cms_trial/space/CDMC/3446374401/Migrate+from+Data+Center+to+Cloud+(Connect)/) - Installation of the latest app versions and reviewing app functionality
- [Pre-migration assessment](/cms_trial/space/CDMC/3446374401/Migrate+from+Data+Center+to+Cloud+(Connect)/) - Current usage of workflows in your hosted instance
- [Pre-migration steps](/cms_trial/space/CDMC/3446374401/Migrate+from+Data+Center+to+Cloud+(Connect)/):

  - Consolidating any required page workflows

You should also have set up a destination Confluence Cloud site.

You must have administrator permission in both the Confluence Data Center instance and the Confluence Cloud site to create and run a migration.

## Assess and prepare your migration

The **Atlassian Confluence Cloud Migration Assistant** is used to assess and prepare apps and users for your migration

In Confluence global administration in your Confluence Data Center instance:

- Open the **Migration Assistant**

![Comala migration assistant link in global admin sidebar](/cms_trial/assets/a74c6e37-50e8-4fca-b3c4-335fda9ca3e8.png)

The **Migration Assistant home** screen takes you through several steps to prepare your migration.

![Comala Cloud Migration Assistant home page](/cms_trial/assets/736d53b6-09f6-40d9-a047-5d38f6c57e5f.png)

If you have previously undertaken a migration, the **Migrations dashboard** is displayed.

You need to:

### **1. Assess your apps**

Check which vendor apps you need in Confluence Cloud, including cloud compatibility and availability.

![Comala Migration Assistant assess your apps with neededincloud dropdown](/cms_trial/assets/15fb5a80-bfdc-45c2-b9b9-17b4f26f44e0.png)

Use the **Decision** menu options to set the apps that are **Needed in cloud**.

### **2. Prepare your apps**

Use the assistant to

- **Connect** to the cloud site
- **Install** the apps set as **Needed in cloud** (and any alternative apps)
- **Agree to app migration** to let the assistant migrate the app data

![Comala Migration Assistant agree to app migration confirmation](/cms_trial/assets/a01041a1-332a-4021-add5-db299459e6e4.png)

You must also use the **Migration Assistant** to

### **3. Assess and prepare your users**

This helps you review and check

- Users and user groups
- All email addresses are valid and unique

### 4. Review all email domains

You must **review all email domains** and set them as trusted or blocked

Comala Document Management data migration includes user details, such as approvers, in the last workflow state.

After you have assessed your apps and prepared them and their users for migration, you can then use the CCMA to migrate selected spaces in your instance.

When you start to migrate using the CCMA, it runs several pre-checks, including app vendor checks for Comala Document Management

## Next step

[Step 2 - Migrate your data](/cms_trial/space/CDMC/2193130034/Step+2+-+Migrate+your+data+using+the+Confluence+Cloud+Migration+Assistant/)