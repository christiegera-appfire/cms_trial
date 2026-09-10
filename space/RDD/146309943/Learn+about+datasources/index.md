# Learn about datasources

## Overview

Datasources are the host apps of the data you want to render in your dashboard, for example, the default Jira instance where Dashboard Hub is installed, or a connection with a Google sheet through an API. This article provides an introduction to the different datasource types, permissions, and viewing modes.

See [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/) to learn how to configure a datasource.

## Datasources and gadgets

To display data, most gadgets use a datasource, and several gadgets can share the same datasource. When you configure your first gadget in a dashboard, you have the option to configure all compatible gadgets automatically with that datasource. For example, if your dashboard has four gadgets that use a Bitbucket datasource, when you configure the first one; the rest can be automatically configured with the same datasource.

### Types of datasources

- **Default datasource**: This is the Jira or Confluence instance where you install Dashboard Hub. No setup is required. Data access and permissions are determined by the dashboard owner's permissions within the connected platform.
- **Connector app**: Connector apps connect to a different Jira or Confluence instance from the default instance. These are free apps available from the Atlassian Marketplace.
- **API token**: You can connect to supported third-party apps using an API token, for example, if you want to display data from Opsgenie, Statuspage, or Bitbucket. API tokens are also useful when you want data access defined by a particular user's permissions rather than the dashboard view permissions.

See [Product and data integrations](/cms_trial/space/RDD/146310010/Product+and+data+connections/) for more information on selecting a connection type for your datasource and a list of supported apps.

## Permissions in datasources

Datasources fetch and display information from external products, which sometimes require extended permissions to access restricted or confidential data, or information that you want to keep private. In this case, you can configure permissions and indicate who can use and/or edit your datasources. You can use the following access restrictions options:

- **Anyone can use and edit**
- **Anyone can use, some can edit**
- **Only specific people can use or edit**

You can configure permissions when you create a datasource, or by editing the datasource in the *Manage Datasources* page.

See [Manage permissions on datasources](/cms_trial/space/RDD/1899429890/Manage+permissions+on+datasources/) to learn more.

## Datasource viewing modes

Datasource viewing modes give you greater flexibility in how gadgets display data. This feature lets you control whether data is displayed based on the permissions associated with the configured credentials, such as API tokens or OAuth tokens, rather than the viewer’s permissions.

**Credentials**

The gadget always uses the credentials configured by the user who created this datasource to load and display data. These credentials are independent of the viewer or owner permissions.

Datasources configured with specific authentication credentials will always use those credentials to display data, regardless of who is viewing the dashboard.

![Datasource token permissions tooltip.](/cms_trial/assets/e83de2de-a916-4d29-95ea-705c46202846.png)

**Viewer**

The gadget displays data according to the user's permissions. Users without access to certain fields/projects will not see restricted data.

![Dashboard Hub viewer permissions setting](/cms_trial/assets/add81193-1fa2-4c2d-ae98-0b3ed63e05fe.png)

Datasources created using Connector apps or local instances using the default datasources “My Jira instance” or “My Confluence instance” can use Viewermodeor Owner mode**.**

**Owner**

The gadget uses the dashboard owner’s permissions to load data, ensuring a consistent view for all dashboard users.

The Owner Mode can be disabled by admins; select the global setting: **Restrict Owner View Mode**

![Datasource permissions tooltip for dashboard owner.](/cms_trial/assets/6f304521-4aa0-42bc-bddc-ba5e5e7cde36.png)

| **Datasource** | **How the data can be displayed** |
| --- | --- |
| My Jira instance (local Cloud or Data Center instance)  or  My Confluence instance (local Cloud or Data Center instance) | Viewer OR Owner |
| Connector app (remote Cloud instance) | Viewer OR Owner |
| API Token (Cloud instance) | Credentials |
| User name and password (Data Center instance) | Credentials |
| Personal Access API Token (Data Center instance) | Credentials |