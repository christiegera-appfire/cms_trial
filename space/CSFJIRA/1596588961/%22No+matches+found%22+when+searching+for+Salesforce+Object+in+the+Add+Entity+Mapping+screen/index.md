# "No matches found" when searching for Salesforce Object in the Add Entity Mapping screen

## Summary

When adding an Entity Mapping in the *Bindings* page, the available Salesforce Objects are not shown in the dropdown and cannot be searched.

![contentId-1596588961](/cms_trial/assets/158f1e55-019e-435d-a95f-935d506a64e4.png?version=1&modificationDate=1678795881368&cacheVersion=1&api=v2)

## Environment

- JIRA Cloud

## Diagnostics Steps

Not applicable.

## Cause

There are no defined Salesforce Objects set up in the *Connection Configuration* page.

![image-20241213-142440.png](/cms_trial/assets/82c8156c-c0eb-480a-b37a-6799dee057cb.png)

## Workaround

Not applicable.

## Resolution

1. Go to **Apps** > **Salesforce** > **Connections** > **Configure**.
2. Click **Add Salesforce Objects** and add the required Salesforce Objects.
3. You can choose to toggle **Import Layout** on to automatically import fields from the Salesforce Object.

   ![contentId-1596588961](/cms_trial/assets/559713d6-380c-45cd-a827-4454fb29a66b.png?version=1&modificationDate=1678795881566&cacheVersion=1&api=v2)
4. Click **Next** and click **Apply Changes** on the top right of the page.