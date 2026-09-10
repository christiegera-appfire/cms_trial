# Migration to Forge

## Overview

Appfire's Connector for Salesforce & Jira Cloud has moved to Atlassian Forge, Atlassian’s most advanced cloud development platform. Atlassian is ending support for the Connect framework by December 31, 2026. Please upgrade before then to prevent permanent data loss and and app failure.

## How to upgrade to Forge

To upgrade the app to the Forge version, you need Jira administrative privileges. Throughout the migration process, all existing data is fully preserved. The migration changes only the app framework.

1. Navigate to **Apps** > **Manage apps**.
2. Under *Connected apps,* the Connector for Salesforce & Jira app displays an **Update** label. Click **View app details**.
3. To upgrade the app, click **Accept & update**.
4. The *Confirm app update* dialog opens. Click **Update**.

### What happens during upgrade

- All your Salesforce-Jira connections and configurations are preserved.
- No data loss occurs during the migration.
- The upgrade happens with minimal interruption.
- No reconfiguration required.

- Please update to the latest version by the end of 2026 to keep your app running. If you miss the deadline, the app stops working and data syncing breaks.

For more information, see: [Atlassian's official announcement on Connect end of support](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps).

## Navigation changes

### Admin pages

Admin pages (such as *Connections*, *Bindings*, and *Settings*) are now located in **Jira admin settings** under **Apps**.

![Jira admin settings ](/cms_trial/assets/2b8dd33a-045c-49e1-8acc-496605e86065.png)

To access administrator pages, go to **Apps** > **Connector for Salesforce and Jira Cloud** > **App settings**.

![App settings](/cms_trial/assets/bf564327-0742-4c42-83ab-ccbaa7abcb62.png)

### **Documentation link**

The direct documentation link from the old top-navigation dropdown has been removed. You can access documentation from the **Help menu** under the **Jira admin settings** pages.

![Documentation link](/cms_trial/assets/8fbcc09f-d38c-436a-a77d-544875ce5ac3.png)

## For DC customers

The migration path has been adapted to work with the Forge framework on both the Cloud and DC sides.  
Before migrating from Jira Data Center to Jira Cloud, ensure you are on the latest version of Connector for Salesforce & Jira in both DC and Cloud. Performing a migration from older versions of the connector on either side is not advised.

For instructions, see [Migrate Connector for Salesforce & Jira Data Center to Cloud](/cms_trial/space/CSFJIRA/2161049701/Migrate+Connector+for+Salesforce+%26+Jira+Data+Center+to+Cloud/).

## Support and resources

If you have questions or need assistance with the upgrade process, our support team is here to help.

Contact our support team: [support.appfire.com](https://support.appfire.com/page/support)

### Additional resources

- [Complete migration guide: DC to Cloud](/cms_trial/space/CSFJIRA/2161049701/Migrate+Connector+for+Salesforce+%26+Jira+Data+Center+to+Cloud/)
- [Atlassian's Connect end of support announcement](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps)