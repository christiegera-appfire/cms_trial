# Data residency and realm persistence

Atlassian data residency lets you choose where your app data is stored. If security needs or contractual obligations require your data to be stored in a particular location, you can select the region that hosts it. This helps your organization meet compliance requirements.

To learn more, see [Data residency](https://developer.atlassian.com/cloud/jira/platform/data-residency/#realm-persistence) and [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/).

## How it works for Rich Filters

Rich Filters uses the same data location as your Jira instance. Rich Filters has no separate location setting.

### **New installations**

Set your data location in Atlassian Administration, then install Rich Filters. The app automatically uses the location you selected, provided that the app supports that region.

### **Existing installations**

Rich Filters supports migrating app data from one data location to another, so you can change the location of an existing installation without reinstalling. For the steps to set or move your location, see Atlassian’s [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/) page.

### Realms and regions

Each realm is a geographical area containing specific Amazon Web Services (AWS) regions where your data can be hosted. Rich Filters currently offers these realms:

- **Global:** Your in-scope data is hosted in realms determined by Atlassian. Data can be moved between realms as needed to ensure optimal performance and availability.
- **US:** In-scope data is hosted in the US East and US West AWS regions.
- **EU:** In-scope data is hosted in AWS regions within the European Union, currently Frankfurt and Dublin.

#### Realm persistence

Realm persistence keeps your app’s data location consistent when you uninstall and reinstall Rich Filters.

- If you uninstall and reinstall Rich Filters **within 30 days**, the app is installed in the same realm as before, so you keep access to your existing data.
- If you reinstall **after 30 days**, the app might be assigned to a different realm, and you could lose access to your previous data.

For more detail, see [Realm persistence](https://developer.atlassian.com/cloud/jira/platform/data-residency/#realm-persistence) in Atlassian’s documentation.

#### View where your Rich Filters data is hosted

You need organization administrator permissions to view your app’s data location. In Atlassian Administration, go to **Data management > Data residency** and open the app details for your Jira instance. If a location is set, you’ll see its name there.

For the full walkthrough, see [Understand data residency](https://support.atlassian.com/security-and-access-policies/docs/understand-data-residency/).