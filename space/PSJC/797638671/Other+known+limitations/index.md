# Other known limitations

There are some additional limitations and known issues when using Power Scripts with Jira Product Discovery projects.

## SIL Manager compatibility

Product Discovery field information is not fully compatible with the [SIL Aliases panel](/cms_trial/space/PSJC/496206102/Managing+aliases+from+the+SIL+Manager/) within the [SIL Manager](/cms_trial/space/PSJC/490996983/SIL+Manager/). This panel cannot access Product Discovery-specific fields when retrieving the custom field list from Jira.

The SIL Aliases panel is designed to update the `sil.aliases` file by rewriting the entire file with data from the interface. As a consequence, any Product Discovery fields added to the `sil.aliases` file will be overwritten by the UI panel, potentially causing scripts to stop working.

**Workaround:** Schedule the [Custom fields support SIL script](/cms_trial/space/PSJC/793280566/Custom+fields+support+SIL+script/) to run periodically to restore missing aliases. The script won't create duplicates and can be run multiple times safely without affecting existing aliases.

## User attribution inconsistencies

When Power Scripts updates issues in Product Discovery projects, the actions are performed by the current user instead of the addon. This affects operations like:

- Editing or deleting comments
- Managing attachments
- Setting field values

This occurs because the Power Scripts addon doesn't have the necessary permissions to perform these operations directly in Product Discovery projects.