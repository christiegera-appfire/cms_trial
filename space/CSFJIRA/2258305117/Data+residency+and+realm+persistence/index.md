# Data residency and realm persistence

Atlassian data residency lets you to choose where your app data is stored. If security needs or contractual obligations require your data to be held in a particular geographic location, you can choose where it's stored. This feature helps organizations meet compliance requirements by specifying which geographic regions host their data. To learn more, see [Data residency](https://developer.atlassian.com/cloud/jira/platform/data-residency/#realm-persistence) and [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/).  
Connector for Salesforce & Jira supports data residency for new installations and for migrating existing installations from one data location to another. If you already have the Connector installed, you can now move its data to a different location.

## Set your data location

For new Connector for Salesforce & Jira installations, set the data residency location for your Jira instance in Atlassian Administration. Atlassian's instructions cover the steps: [Set the default data residency location](https://support.atlassian.com/security-and-access-policies/docs/set-the-default-data-residency-location/).

Once the location is set, install the Connector. It will automatically use the same location as your Jira instance.

## Migrate existing Connector data to another location

If the Connector is already installed, you can move its data to another location. You request the move in Atlassian Administration, and you need organization administrator permissions to do it. For the steps, see Atlassian's guides to [moving Atlassian app data](https://support.atlassian.com/security-and-access-policies/docs/move-data-to-another-location/) and [moving your Marketplace apps data](https://support.atlassian.com/security-and-access-policies/docs/moving-your-marketplace-apps-data-to-another-location).

## Realms and regions

Each realm represents a geographical area containing specific Amazon Web Services (AWS) regions where your data can be hosted. Currently, the Connector for Salesforce & Jira offers the following realms:

- **Global:** Your in-scope data is hosted within realms determined by Atlassian. Data may be moved between realms (distributed globally) as needed to ensure optimal performance and availability.
- **US:** In-scope data is hosted within the US East and US West AWS regions.
- **EU:** Your in-scope data is hosted within the Frankfurt and Dublin AWS regions.

## Realm persistence

Realm persistence ensures continuity for your app's data location when reinstalling the Connector for Salesforce & Jira. If you uninstall and then reinstall the Connector for Salesforce & Jira within the **persistence period of 30 days**, the app will be installed in the same realm it was previously, preserving access to your existing data. This prevents data loss or access issues when temporarily uninstalling the app.

## View where your data is hosted

To view where your Connector for Salesforce & Jira data is hosted, you must have organization administrator permissions to do this.

1. Go to **Atlassian Administration**.

   ![Screenshot showing the Atlassian Administration button location.](/cms_trial/assets/e8ba7891-2129-4ad8-abc4-4463fa18ceb5.png)
2. Select your organization if you have more than one.
3. Select **Data management** > **Data residency.**
4. Click **Menu** (▢) > **View app details** for the Jira instance where you have the Connector installed.

   ![2026-01-29_14-59-56.png](/cms_trial/assets/e725ba8f-f89e-46ab-b9c6-cb9ab3119849.png)
5. Search for Connector for Jira & Salesforce.

   If the location is set, you will see the name of the location.

   ![contentId-2258305117](/cms_trial/assets/8435ece6-3063-4cee-afda-fad38eb5a164.png)