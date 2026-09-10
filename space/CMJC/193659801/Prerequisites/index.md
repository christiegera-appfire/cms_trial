# Prerequisites

## Before you deploy project configuration between Jira Cloud sites

To deploy project configurations between Jira Cloud sites, you must install **Configuration Manager** **for Jira (CMJ) Cloud** on both sites.

**Supported Jira Cloud plans**

You musthave either the **Standard**, **Enterprise**, or **Premium** cloud plan **on both** Jira Cloud sites. Trial or paid licenses of these three types are supported.

Migrations to Jira Cloud on the Free plan are **not supported**. [Learn more](https://support.atlassian.com/jira-cloud-administration/docs/explore-jira-cloud-plans/)

### Prerequisites

- You need to have **User access admin** or **Organization admin** permissions on both Jira Cloud sites to deploy configurations between them. Alternatively, if you’re still using the original user management content, you need to have **Site admin** or **Organization Admin** permissions. You can learn more about the different admin roles in [Atlassian’s documentation](https://support.atlassian.com/user-management/docs/what-are-the-different-types-of-admin-roles/#Admin-roles).
- You need to have the **Service project agent** permission if you want to deploy Jira Service Management (JSM) configurations.
- If any of your Cloud instances are using a **Premium Cloud plan** with the*Allowlist*option turned on, then you’ll need to add the following IP addresses to their allowlist - **23.23.215.132** and **52.205.121.251.**
- You must install **Configuration Manager for Jira Cloud** on both of your sites. Visit the [installation instructions](/cms_trial/space/CMJC/194183182/Installation+guide/) for the exact steps.
- You need **two license tokens** for CMJ Cloud provided by Appfire - a separate token for each Jira Cloud site.
- You need to have an Atlassian **API token** for your Atlassian account. [Learn more](/cms_trial/space/CMJC/193594026/Authorize+with+API+token/) about why you need an API token and how to get one.
- You need to have the **same third-party** **apps** installed on both Jira Cloud sites.

## Before you migrate from Jira Server/Data Center to Jira Cloud

To migrate Jira Server/Data Center projects and issues to the cloud, you must install **Cloud Migration Tool** on your server or data center instance and **Configuration Manager** **for Jira (CMJ) Cloud** on your Jira Cloud site.

**Supported Jira Cloud plans**

You **must have either the Standard, Enterprise or Premium** cloud plan on the destination Jira Cloud site. Trial or paid licenses of these three types are supported.

Migrations to Jira Cloud on the Free plan **are not supported**. [Learn more](https://support.atlassian.com/jira-cloud-administration/docs/explore-jira-cloud-plans/)

### Prerequisites

- 🌍Jira Server/Data Center needs to have **Internet access.**
- You need to have **Jira System Administrator** permissions on Jira Server/Data Center.
- You need to have **User access admin** or **Organization admin** permissions on both Jira Cloud sites to deploy configurations between them. Alternatively, if you’re still using the original user management content, you need to have **Site admin** or **Organization Admin** permissions. You can learn more about the different admin roles in [Atlassian’s documentation](https://support.atlassian.com/user-management/docs/what-are-the-different-types-of-admin-roles/#Admin-roles).
- You need to have the **Service project agent** permission on the Jira Cloud site if you want to migrate Jira Service Management (JSM) configurations.
- If the Cloud instance you’re migrating to is using a **Premium Cloud plan** with the*Allowlist*option turned on, then you’ll need to add the following IP addresses to its allowlist - **23.23.215.132** and **52.205.121.251.**
- You must install **Cloud Migration Tool** on your Jira Server/Data Center. Visit the [installation instructions](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CMT&title=Installation%20and%20upgrade).
- You must install **Configuration Manager for Jira Cloud** on your site. Follow the installation instructions above.
- You need to have an Atlassian **API token** for your Atlassian account. [Learn more](https://appfire.atlassian.net/wiki/spaces/CMT/pages/197892240) about why you need an API token and how to get one.
- You need to have the **apps** installed on your Jira Server/Data Center instance also installed on your Jira Cloud site.

**App compatibility between Jira Server/DC and Cloud**

Note that third-party apps, even if they are available for Cloud and Server, will work differently in most cases. Please **get in touch with the third-party app vendor** regarding the migration procedure of the app data.