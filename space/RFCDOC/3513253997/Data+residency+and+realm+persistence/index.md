# Data residency and realm persistence

Atlassian data residency lets you choose where the app data is stored geographically. If you have security needs or contractual obligations that require your data to be held in a particular geographic location, you can choose where your data is stored. This feature helps organizations meet compliance requirements by specifying which geographic regions host their data. To learn more, see [Data residency](https://developer.atlassian.com/cloud/jira/platform/data-residency/#realm-persistence) and [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/).

Currently, Rich Filters doesn’t support migration from one data location to another. If you have your Rich Filters already installed, you can’t change its location for the moment.

## Set your data location

For new installations of Rich Filters, you can set your Jira instance data residency location in Atlassian Administration.

1. Go to **Atlassian Administration**.
2. Select your organization if you have more than one.
3. Select **Data management** > **Data residency.**
4. Click **Set location**.
5. Review information about the steps involved. Select **Next**.
6. Select the location from the menu where you want to move your app. Select **Next**.
7. Select a move window. Select **Next**.
8. Install the Rich Filters  
   It will automatically use the same location as your Jira instance.

## Realms and regions

Each realm represents a geographical area containing specific Amazon Web Services (AWS) regions where your data can be hosted. Currently, the Rich Filters offer the following realms:

- **Global:** Your in-scope data is hosted within realms determined by Atlassian. Data can be moved between realms (distributed globally) as needed to ensure optimal performance and availability.
- **US:** In-scope data is hosted within the US East and US West AWS regions.
- **EU:** Your in-scope data is hosted within the Frankfurt AWS regions.

## Realm persistence

Realm persistence ensures continuity for your app's data location when reinstalling the Rich Filters. This means that if you uninstall and then reinstall the Rich Filters within the **persistence period of 30 days**, the app will be installed in the same realm it was previously, preserving access to your existing data. This prevents data loss or access issues when temporarily uninstalling the app.

If you uninstall and then reinstall the app after the 30-day persistence window, your app might be assigned to a different region than before, and you can lose access to your previous data.

## View where your data is hosted

To view where your Rich Filters data is hosted, you must have organization administrator permissions to do this.

1. Go to **Atlassian Administration**.

   ![Screenshot showing the Atlassian Administration button location.](/cms_trial/assets/4d066836-60ed-47aa-8b66-e08ebe261e32.png)
2. Select your organization if you have more than one.
3. Select **Data management** > **Data residency.**
4. Click **Menu** (▢) > **View app details** for the Jira instance where you have the Rich Filters installed.

   ![2026-01-29_14-59-56.png](/cms_trial/assets/e191c1fb-c019-4b7a-a182-62e7ea7da0a8.png)
5. You can search for Rich Filters.

   If the location is set, you will see the name of the location.

   ![contentId-3513253997](/cms_trial/assets/79670c2c-ce5d-4f93-b190-8f565932a903.png)