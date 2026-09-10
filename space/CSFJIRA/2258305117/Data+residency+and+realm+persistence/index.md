# Data residency and realm persistence

Atlassian data residency allows choosing where the app data is stored geographically. If you have security needs or contractual obligations that require your data to be held in a particular geographical location, you have a choice over where your data can be held. This feature helps organizations meet compliance requirements by specifying which geographic regions host their data. To learn more, see [Data residency](https://developer.atlassian.com/cloud/jira/platform/data-residency/#realm-persistence) and [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/).

Currently, Connector for Salesforce & Jira doesn’t support migration from one data location to another. If you have your Connector already installed, you can’t change its location for the moment.

## Set your data location

For new installations of Connector, you can set your Jira instance data residency location in Atlassian Administration.

1. Go to **Atlassian Administration**.
2. Select your organization if you have more than one.
3. Select **Data management** > **Data residency.**
4. Click **Set location**.
5. Review information about the steps involved. Select **Next**.
6. Select the location from the menu where you want to move your app. Select **Next**.
7. Select a move window. Select **Next**.
8. Install the Connector.  
   It will automatically use the same location as your Jira instance.

## Realms and regions

Each realm represents a geographical area containing specific Amazon Web Services (AWS) regions where your data can be hosted. Currently, the Connector for Salesforce & Jira offers the following realms:

- **Global:** Your in-scope data is hosted within realms determined by Atlassian. Data may be moved between realms (distributed globally) as needed to ensure optimal performance and availability.
- **US:** In-scope data is hosted within the US East and US West AWS regions.
- **EU:** Your in-scope data is hosted within the Frankfurt and Dublin AWS regions.

## Realm persistence

Realm persistence ensures continuity for your app's data location when reinstalling the Connector for Salesforce & Jira. Meaning, if you uninstall and then reinstall the Connector for Salesforce & Jira within the **persistence period of 30 days**, the app will be installed in the same realm it was previously, preserving access to your existing data. This prevents data loss or access issues when temporarily uninstalling the app.

If you uninstall and then reinstall the app after the 30-day persistence window, your app might be assigned to a different region than before, and you can lose access to your previous data.

## View where your data is hosted

To view where your Connector for Salesforce & Jira data is hosted, you must have organization administrator permissions to do this.

1. Go to **Atlassian Administration**.

   ![Screenshot showing the Atlassian Administration button location.](/cms_trial/assets/e8ba7891-2129-4ad8-abc4-4463fa18ceb5.png)
2. Select your organization if you have more than one.
3. Select **Data management** > **Data residency.**
4. Click **Menu** (▢) > **View app details** for the Jira instance where you have the Connector installed.

   ![2026-01-29_14-59-56.png](/cms_trial/assets/e725ba8f-f89e-46ab-b9c6-cb9ab3119849.png)
5. You can search for Connector for Jira & Salesforce.

   If the location is set, you will see the name of the location.

   ![contentId-2258305117](/cms_trial/assets/8435ece6-3063-4cee-afda-fad38eb5a164.png)