# Configure Datasource Allowlist Settings

## Overview

The process for updating data source allowlist settings differs between Cloud and Data Center. This document outlines these differences and how to configure them.

- **Cloud**: Managed through Appfire’s Jira configuration screen.
- **Data Center**: Managed through the platform Atlassian.

This feature is only available for Dashboard Hub Pro and Dashboard Hub for Confluence (Cloud and Data Center). Dashboard Hub for Bitbucket and Dashboard for monday.com do not include this configuration option yet.

## Cloud

The Allowlist must be configured in the **Global Settings** section of Dashboard Hub. To configure, follow these steps:

1. Select the **More** dropdown.
2. Click **Apps.**
3. Click **Manage apps.**
4. Navigate to Dashboard Hub's left sidebar and click **Global Settings.**
5. Under **Datasource Restrictions,** you can choose **Allowlist**.

   ![Dashboard Hub datasource allowlist settings page](/cms_trial/assets/ad852010-fe1f-40e1-8c42-757c5ad863f7.png)

### Restriction Type

Three different restrictions can be set:

**Disabled -** Data can be retrieved from any source with no restrictions.

- Data can be retrieved from **any source** without limitations; no restrictions are enforced on where the data comes from.
- This is recommended for environments where external integrations are required.

**Do not allow external data sources** - only restrict data retrieval to this instance.

- Restricts data retrieval to the current Jira or Confluence instance only. Thus, **external data sources are entirely blocked**, ensuring that all queries and reports use internal data only.
- Recommended for **high-security environments** where external data access is not permitted.

**Allowlist** - Only allows data from data sources with domains explicitly listed here.

- Only allows data retrieval from **explicitly approved** domains**.** Thus, Users must **manually specify allowed domains** to ensure secure connections.
- Recommended for **controlled access scenarios**, only trusted external data sources should be used.

## Data Center

Dashboard Hub delegates the configuration on the Atlassian platform configuration: <https://confluence.atlassian.com/adminjiraserver/configuring-the-allowlist-1014667309.html>

To configure the Allowlist in the Data Center, follow these steps:

1. From the top navigation bar, select **Administration**  > **System**.
2. Select **Allowlist**.
3. Enter the URL or expression you want to allow.
4. Choose the **Type** of expression (see *Expression Types* below for examples).
5. Choose **Allow Incoming** if you need to allow CORS requests. See [Configuring the allowlist](https://confluence.atlassian.com/adminjiraserver/configuring-the-allowlist-1014667309.html#Configuringtheallowlist-AllowIncomingSection) for more details).
6. Choose **Allow anonymous users** if you need to allow unauthenticated users.
7. Choose **Add**. Your URL or expression appears in the allowlist.

Image — asset pipeline pending  
Image

To test that your allowed listed URL works as expected, you can enter a URL in the **Test a URL** field. Icons will indicate whether incoming or outgoing traffic is allowed for that URL.