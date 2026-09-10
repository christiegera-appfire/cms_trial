# Product and data connections

## Overview

Dashboard Hub can pull data from a variety of sources. This page explains the types of connections and datasources you can use for different use cases.

## Your current Jira/Confluence instance (Default datasource)

This is automatic; no setup is required. When you install Dashboard Hub, it can already read data from the Jira or Confluence instance it's installed on.

When selecting a datasource for a gadget, the default datasource is called ***This Jira/Confluence instance****.*

### **When to use the default datasource**

Use this method to display data from your *own* instance. This is the most common starting point.

### **How it works**

Gadgets display data based on the dashboard owner's permissions, so viewers only see what the owner can see. You can also switch to **Viewer** mode if you want each person to see data according to their own permissions.

---

## An external Jira or Confluence instance (Connector app)

[Dashboard Hub Connector for Jira](https://marketplace.atlassian.com/apps/1223900) or [Dashboard Hub Connector for Confluence](https://marketplace.atlassian.com/apps/1224209) are free apps that serve as a secure bridge between Dashboard Hub and a *different* Atlassian Cloud instance.

### **When to use a Connector app**

Use a Connector app when you want to pull data from a Jira or Confluence instance that *isn't* the one Dashboard Hub is installed on. For example, you have Dashboard Hub on `company-a.atlassian.net` and want to display data from `company-b.atlassian.net`.

### **How it works**

An admin installs the free connector app on the *external* instance. Dashboard Hub then connects to it while respecting that instance's user permissions. Users can only see data they already have access to on the external site. Data accessed through a Connector datasource relies on the permissions of the Atlassian account connected to the Connector app instance, not necessarily the dashboard owner in the Dashboard Hub instance.

---

## Third-party products (API Token)

You can connect data using the API tokens you create in supported third-party apps.

### **When to use an API token**

Use API tokens when you want to connect to a supported third-party product, for example, Opsgenie, Statuspage, Bitbucket, or others listed in the table below. API tokens are also useful when you want data access defined by a particular user's permissions rather than the dashboard view permissions. This ensures data consistency, as the data displayed will always be within the scope of the token owner's access, regardless of who views the dashboard.

### **How it works**

Generate an API token in the external product, then enter it when creating the datasource in Dashboard Hub. Data displayed is always limited to what that token has access to; it won't change based on the viewer.

![Dashboard Hub product and data connections overview](/cms_trial/assets/997d53af-e6ae-4edf-bc7d-7c879ab263e0.png)

### Supported third-party apps

| **Product** | **Datasource** |
| --- | --- |
| Jira Software  Jira Work Management  Jira Service Management  *Cloud, DC* | User+password (to Data Center)  Personal access token (to Data Center)  API Token (to Cloud)  Connector app (to Cloud) |
| Confluence  *Cloud, DC* | User+password (to Data Center)  Personal access token (to Data Center)  API Token (to Cloud)  Connector app (to Cloud) |
| Bitbucket  *Cloud, DC**(Cloud includes Pipelines)* | API Token (to Cloud)  HTTP access token (to Data Center) |
| Insight | API Token |
| Opsgenie | API Token |
| Statuspage | API Token |
| monday.com  monday dev  monday sales CRM | OAuth |
| Projectrak | API Token |
| **Appfire apps** | **Datasource** |
| Big Picture | API Token |
| Comala Document Management | Any Confluence Data Center Datasource  User+password (to Data Center)  Personal access token (to Data Center) |
| Time to SLA | API Token |

---

### Any product with an API (Custom Reports gadget)

The [Custom Reports gadget](/cms_trial/space/RDD/1529219266/Custom+Reports+-+REST+API+integration/) lets you connect to any external system that has a REST API, including those not natively supported by Dashboard Hub.

### **When to use Custom Reports**

When none of the above options cover the tool you need. Good examples include Zendesk, GitHub, GitLab, Tempo, ServiceNow, internal CRMs, ERPs, or any custom service with an API.

**How it works:** You define the API endpoint, set up authentication (Basic Auth, Bearer Token, or API Key), and use JSON/JSONata to transform and display the data as charts or tables inside a dashboard gadget. It's more of a "build your own" integration, but pre-built [Custom Reports templates](/cms_trial/space/RDD/1568374878/Custom+Reports+templates/) are available to help you get started quickly.

---

## Quick comparison

| I want to show data from… | Use this |
| --- | --- |
| My own Jira/Confluence instance | Default datasource (automatic) |
| A different Jira/Confluence Cloud instance | Connector app (free) |
| monday.com, Opsgenie, Bitbucket, Statuspage, etc. | API Token |
| Zendesk, GitHub, Tempo, or any REST API | Custom Reports gadget |

## Glossary

- **Default datasource**: The connection to the Jira or Confluence instance where Dashboard Hub is installed.
- **Connector app**: A free app that’s required to connect another Jira or Confluence instance where you have not installed Dashboard Hub [Dashboard Hub Connector apps](/cms_trial/space/RDD/146309882/Dashboard+Hub+Connector+apps/).
- **API Token**: Create an API token in the source product and provide it when you create the datasource in Dashboard Hub.
- **User+password**: You provide a user and password so Dashboard Hub can access data. This user+password could be your user name and password or another specifically to allow the data access.
- **Personal access token**: The service lets you create an extra pass to connect data. You generate this pass setting different permissions to the data access (like read-only access).
- **App password**: The service lets you create a special password key to connect for data (the user will not be required). You generate this password, setting different permissions to the data access (like read-only access).
- **HTTP access tokens**: These tokens are a secure way to integrate external applications with Bitbucket. Refer to Atlassian’s [Bitbucket documentation](https://confluence.atlassian.com/bitbucketserver/http-access-tokens-939515499.html) for more information.

## Hybrid dashboards: Data Center supported versions

You can connect to a Data Center instance from your Cloud dashboard. Create a new Jira/Confluence/Bitbucket/Data Center datasource and use it like any other datasource. See [Hybrid hostings dashboards](/cms_trial/space/RDD/146310618/Hybrid+hostings+dashboards/) to learn more.

Our Marketplace listings provided the most up-to-date compatibility information:

- [Dashboard Hub Pro](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-tables?hosting=datacenter&tab=overview)
- [Dashboard Hub for Confluence](https://marketplace.atlassian.com/apps/1224619/dashboard-hub-for-confluence-reports-dashboards-from-jira?hosting=cloud&tab=overview)