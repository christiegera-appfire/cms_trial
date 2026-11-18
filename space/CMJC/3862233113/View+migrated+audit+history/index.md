# View migrated audit history

When migrating from Jira Data Center to Jira Cloud, you can preserve the audit history of Configuration Manager for Jira (CMJ) and Project Configurator for Jira (PCJ) and access it in CMJ Cloud.

The imported records provide a read-only history of events from your Data Center instance, allowing you to refer to previous configuration activities after migration.

## Migrate your audit history

CMJ and PCJ audit history is transferred using the Jira Cloud Migration Assistant (JCMA).

To include your audit history in the migration:

1. Open the **Jira Cloud Migration Assistant** on your Jira Data Center instance.
2. On the **Assess and prepare apps** screen, find the app whose history you want to migrate:

   - **Configuration Manager for Jira** for CMJ audit history
   - **Project Configurator for Jira** for PCJ audit history.
3. Set the app's status to **Needed in cloud**.
4. Continue with the migration process in JCMA.

Once the migration is complete, the imported records become available in CMJ Cloud.

## View your imported audit history

To access the imported records, open CMJ Cloud and select **Data center audit log** from the sidebar.

![Data center audit log](/cms_trial/assets/2ca4a61f-8890-4115-bb63-d0dd20c69a00.png)

The page displays the historical events imported from Data Center, including:

- **Date:** When the event occurred.
- **Severity:** The severity level of the event.
- **By:** The user associated with the event.
- **Type:** The type of operation recorded.
- **Event:** A description of the event.
- **App:** The application from which the event originated.
- **Source instance:** The original Data Center instance.

You can browse the records using the pagination controls at the bottom of the table.

The imported audit history is **read-only** and contains only events migrated from Data Center. New CMJ Cloud activities are not recorded on this page.