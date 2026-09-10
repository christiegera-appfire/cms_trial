# When trying to create a Jira issue, a Jira validation failed is showing up although mapping configuration remains the same

## Problem

The Connector starts throwing Jira validation failed errors even though you haven't changed your mapping configurations.

![3EF09AAC-4363-4FD4-8CE6-D9899916C769_4_5005_c-20240816-035325.jpeg](/cms_trial/assets/82f406bb-f4f6-4ac9-a67c-e41919c53df7.jpeg)

## Solution

The most common cause is a change to a field's configuration (like a renamed field). Here's how to fix it:

1. Identify the problematic field.

   1. Go to Jira **Settings** (▢) → **Work items** → **Custom fields**.
   2. Select any field, click **Menu** (▢) → **Edit details**.
   3. Replace the ID in the URL with the ID of your custom field.

      ![fieldid.png](/cms_trial/assets/aa1fe805-aa09-4fbc-acd0-f9a45f526be0.png)
2. Once you identify the field, verify if there are any modifications to the field.
3. Refresh the mapping.

   1. Remove the field from your mappings.
   2. Add the field again - this rebuilds the mapping JSON and resolves most errors.

If the changes to the field were related to permissions or it was removed from any screen, then this solution does not apply, and the changes have to be reverted.