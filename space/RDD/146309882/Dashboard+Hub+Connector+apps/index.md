# Dashboard Hub Connector apps

## Overview

Dashboard Hub Connector apps arefree apps that easily and securely retrieve information from some Atlassian Cloud products like Jira and Confluence.

You don't need a Dashboard Hub Connector app to start using Dashboard Hub for Jira, but you do need one to connect certain products, namely:

- **External Jira instances**: Install the free app [Dashboard Hub Connector for Jira](https://marketplace.atlassian.com/apps/1223900/ronin-dashboards-connector-for-jira?hosting=cloud&tab=overview). There is no need to install a connector to display information from your current Jira instance; only if you want to retrieve information from an external Jira instance.
- **Confluence**. Install the free app [Dashboard Hub Connector for Confluence](https://marketplace.atlassian.com/apps/1223989/ronin-dashboards-connector-for-bitbucket?hosting=cloud&tab=overview).

This app is a bridge to bring data from other Atlassian products, keeping users and security privileges configured on every instance. This means that users can access data from other Atlassian Cloud products only if their Atlassian accounts have the right privileges.

It is possible to grant access to other datasources while maintaining data security without additional configuration. The main characteristics of the connector app are:

1. Data access is managed on and by each Atlassian Cloud product instance.
2. It requires an admin to install the app and you are ready to go.
3. It requires Dashboard Hub Pro (paid app) to be installed on the main instance.

## Requirements

To use a Connector app:

- Dashboard Hub must be installed on your main instance.
- You need admin access to the Confluence or Jira instance that you want to connect.

## How to install a Connector app

The process is the same for Confluence and Jira. First, go to the Marketplace listing for the required app:

- Connector for Jira: <https://marketplace.atlassian.com/apps/1223900/dashboard-hub-connector-for-jira?hosting=cloud&tab=overview>
- Connector for Confluence: <https://marketplace.atlassian.com/apps/1224209/dashboard-hub-connector-for-confluence?hosting=cloud&tab=overview>

1. Click **Get app**. Install the connector app on your source instance. This is the external Jira or Confluence instance that you want to pull data from.
2. Add the source instance as a datasource in your main instance. This is the instance where Dashboard Hub is installed.

   1. In Dashboard Hub, select **More options** **(…)** > **Add datasource**.
   2. Select either Jira or Confluence depending on your requirement.
   3. Enter a name for the datasource to help you identify it later.
   4. Enter the URL of the external instance.
   5. Select the permissions to apply to the datasource.
   6. Click **Add**.

The external instance is now connected. When configuring gadgets in Dashboard Hub, it will appear as an available datasource.

### Related pages

- [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/)

---

**Need help?** Contact [Appfire support](https://apps.appf.re/support).