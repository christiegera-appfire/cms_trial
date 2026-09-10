# Step 2 - Migrate your data using the Confluence Cloud Migration Assistant

## Overview

You can migrate your Comala Document Management app data from a hosted instance using the [Atlassian Confluence Cloud Migration Assistant (CCMA)](https://marketplace.atlassian.com/apps/1219672/confluence-cloud-migration-assistant?hosting=datacenter&tab=overview)

![contentId-2193130034](/cms_trial/assets/b3ea7a92-2c34-4be2-8734-3bc36a9bea2c.png)

When creating a migration plan, the **Migration Assistant** lets you connect to your destination cloud and choose what to migrate

It also automatically runs pre-migration checks, including the following for the Comala Document Management app:

- **Space and global workflows cloud compatibility** - Are these workflows in the migration cloud compatible, including any linked global workflows?

The workflow compatibility check also verifies the presence of active page workflows in the spaces. These are not migrated, but the check lets you review whether to consolidate them as space workflows to include in the migration.

## Prerequisites

You must have completed:

- **Prerequisite tasks** on the [Migrate from Data Center to Confluence Cloud](/cms_trial/space/CDMC/3446374401/Migrate+from+Data+Center+to+Cloud+(Connect)/) page
- **CCMA tasks** in [Step 1 - Assess and prepare your migration using the Migration Assistant](/cms_trial/space/CDMC/2193195711/Step+1+-+Assess+and+prepare+your+migration+in+the+Confluence+Cloud+Migration+Assistant/)

## Migrate your data

A migration can include one or more spaces. We recommend migrating small groups of spaces at a time, rather than all at once. This makes it easier to review results and fix any issues.

You can migrate your instance when you have assessed your apps and prepared them and their users for migration. Each migration can include one or more spaces.

- Choose **Migrate your data.**

![contentId-2193130034](/cms_trial/assets/46ba01e7-226e-4a0f-b020-4ad6b27bd346.png)

If you have saved a migration plan or there are existing migration plans, you can choose the **Create new migration** option in the **Migration dashboard**.

The migration assistant takes you through the following steps:

![contentId-2193130034](/cms_trial/assets/b3ea7a92-2c34-4be2-8734-3bc36a9bea2c.png)

### **1. Connect to Cloud**

Name your migration for reference, choose migration as a **Testing** or **Production stage**, and connect to the destination cloud site

You must be signed in as the **Site Administrator** for the Atlassian cloud site you're migrating to.

### **2. Choose what to migrate**

Choose your migration options - what to migrate (spaces, pages, attachments, users, groups, and vendor apps).

![contentId-2193130034](/cms_trial/assets/adfcad7f-5ba3-4727-bbc9-4b29db3b4147.png)

You can choose one or more spaces to migrate and plan one or more migrations. The details of each migration plan are stored in a migration dashboard.

### **3. Run pre-migration checks**

The migration assistant automatically runs a **Check for errors** for each of your system, app versions, apps, spaces, user, and user group data

This includes specific **App vendor checks**.

![contentId-2193130034](/cms_trial/assets/343992e2-9c1b-4226-af29-0757704be59b.png)

**App vendor checks** are run for the apps marked as **Needed in Cloud**. Warnings can be viewed and, if necessary, resolved before proceeding with the migration.

![contentId-2193130034](/cms_trial/assets/b1298f37-871d-4d91-a3f1-55004b5b6a5c.png)

These include the following app vendor checks for the Comala Document Management app:

---

#### **Pre-Migration Workflow Assessment**

Provides relevant information to assess the usage of your workflows before migration.

![contentId-2193130034](/cms_trial/assets/9e85d356-fb24-4a6d-a674-9e56ed31b1b1.png)

A space or global workflow with cloud-incompatible elements is migrated to the cloud, with these elements either adapted to cloud functionality or removed. It is recommended to review these workflows in Confluence Cloud and the changes or updates that might be required.

You can use the [Workflow Translator for Cloud](https://appfire.atlassian.net/wiki/spaces/CDML/pages/649924970) in the hosted app to move a workflow as a cloud-compatible JSON workflow template and explore the functionality in Confluence Cloud before migration.

The Comala Document Management app vendors' checks do not prevent a migration, but they do affect the app's included data.

However, if a blocking error is returned during any **Pre-migration checks**, you cannot proceed with the migration until it is resolved.

![contentId-2193130034](/cms_trial/assets/85eaafd7-a62a-4a40-9576-5a0b0e25e785.png)

When migrating spaces with both global and space workflows, space-scope workflows are now prefixed with a "**~**" in the cloud. This keeps them ordered after global workflows in the app space settings in the cloud, preserving the workflow order from the hosted instance.

Image — asset pipeline pending  
contentId-2360967230

### **4. Review your migration**

With no blocking errors, you can

- Choose **Run now** to start your migration, or
- **Save** it to the **Migrations dashboard** to run it later

![contentId-2193130034](/cms_trial/assets/aeb7de0d-c0c6-4c9f-b001-3c0d9afadc81.png)

When the migration is successful, you can view your Confluence Cloud site using the link.

![contentId-2193130034](/cms_trial/assets/0b861d1e-11db-4629-a48e-8e462951746f.png)

App migration is a parallel multi-transfer process to support process visibility and speed.

The Migrations Dashboard lets you monitor migration progress, view the migration status, and view the migration details for all current migrations.

![contentId-2193130034](/cms_trial/assets/50400e89-657c-4e8d-8b67-4b8c381ee992.png)

If the migration fails, check the CCMA logs, re-run the migration, or [create a support package](/cms_trial/space/CDMC/2193130141/Support+and+troubleshooting+for+migration/) and attach it to a [support request](http://appf.re/support).

See: [Support and troubleshooting for migration](/cms_trial/space/CDMC/2193130141/Support+and+troubleshooting+for+migration/)

## Migration Logs Dashboard

You can use the **Migration Logs** dashboard to monitor the server-side migration logs. Administrators can now track the real-time progress of ongoing migrations and review logs from completed migrations.

The dashboard provides a structured view of available migration logs, organized by source migration name and transfer phase. It also includes a specialized **Log Viewer** component designed to improve readability through syntax highlighting and clear status indicators.

To access the migration logs,

Go to **Confluence Global Administration** > **Comala Document Management** > **Migration logs**

![contentId-2193130034](/cms_trial/assets/e1dcf418-342a-4472-83f6-3494e25d7410.png)

**Usage:**

- **Monitor active migrations**

When a migration is in progress, it automatically appears in the **Select Migration** dropdown under the *Active Session* group. Logs update in real time and automatically scroll to display the latest activity.

- **Review completed migrations**

Use the dropdown to access logs from completed migrations. Each migration is grouped by name and includes a status badge (*SUCCESS* or *FAILED*) to help you quickly identify the outcome.

- **Search for specific transfers**

Start typing in the dropdown to filter migrations by migration name, transfer name, or status.