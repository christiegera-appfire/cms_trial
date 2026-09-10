# Export and import of rich filters data

The **Export to Backup** bulk operation allows Jira administrators to create backup files containing rich filter configurations. These backup files can be **imported** on the same Jira instance or a copy of it, ensuring that referenced Jira object IDs remain consistent.

### Export Rich Filters

1. Go to theRich filters **Bulk ops** screen.
2. Check all the filters you would like to export.
3. Select **Export to Backup** to generate a backup file.

![contentId-1723924660](/cms_trial/assets/2f78b547-ef41-46f5-a1aa-66a971b882ef.png)

### Import Rich Filters

Jira administrators can import rich filter backups in the following ways:

1. **Clone Rich Filters**

   - Creates new rich filters using the backup configuration.
   - Assign new IDs to rich filters and their sub-objects (such as static filters).
   - Enables cloning within a Jira instance or transferring rich filters to a copy of the instance (e.g., staging to production).

The rich filter transfer use case does not apply to dashboards using rich filters. Any rich filter gadgets in the destination instance—whether existing or transferred separately—will not automatically reference the transferred rich filters.

1. **Restore Rich Filters with Original IDs**

   - Works only within the same Jira instance.
   - Restores rich filters exactly as exported, preserving their original IDs.
   - Ensures that dashboards and rich filter gadgets remain functional without manual updates.

To access the **Import from backup** screen:

1. Go to theRich filters **Home** screen.
2. Click **Import** in the side navigation menu.
3. Select **Import from backup.**