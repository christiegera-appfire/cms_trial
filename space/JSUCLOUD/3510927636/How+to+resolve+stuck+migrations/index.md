# How to resolve stuck migrations

If your JSU Automation Suite migration remains in the **Ready** state, it doesn't necessarily mean the migration failed. In some cases, Atlassian's Cloud Migration Assistant doesn't start the vendor app migration, so JSU never receives a migration request.

Because JSU only processes migration requests sent by Atlassian, Appfire can't start or restart the migration independently.

## How can I tell whether JSU received the migration?

Appfire Support can verify whether a migration request reached the JSU migration service. If no migration record exists, the migration was never initiated for the app, even if the Atlassian migration plan shows it as **Ready**.

## Can Appfire restart the migration?

No. Appfire can't manually trigger a JSU migration. Vendor app migrations are initiated by Atlassian's migration platform.

## What should I do?

If Appfire Support confirms that no migration request was received:

1. Contact Atlassian Support and ask them to verify that the vendor app migration was initiated.
2. If advised by Atlassian, create a copy of the migration plan and run the migration again.

## Why does Appfire need Atlassian to investigate?

Appfire and Atlassian each have visibility into different parts of the migration process. If a migration doesn't start or appears stuck, both teams can compare logs to determine whether the vendor app migration request was initiated.