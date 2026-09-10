# How to connect the Advanced Tables for Confluence app to the Jira application

## Overview

This guide outlines how to connect the **Advanced Tables for Confluence** app to **Jira** from the Atlassian Administration platform. Connecting these apps allows the **Advanced Table Viewer** macro to query and render Jira work item data directly within your Confluence pages.

**Permission boundaries**

- Jira data visibility in Confluence is strictly bound by Jira permissions.
- Advanced Tables adheres to Jira project and work item security-level permissions, ensuring that end users see only the Jira data they have permission to view.

## Prerequisites

- You must be an organization or site administrator for the target Atlassian site.
- Both Confluence Cloud and Jira Cloud (Software, Service Management, or Work Management) must be active on the same Atlassian site.
- Advanced Tables for Confluence must already be installed on your Confluence instance.
- You must have administrator access(or a Jira account with permission to authorize app connections) on the Jira site you want to connect to authorize the connection.

## Manage app connections

Follow these steps to establish the app connection between Advanced Tables for Confluence and your Jira instance. [Read more](https://support.atlassian.com/organization-administration/docs/managing-an-installed-app/#Manage-app-connections).

### **Navigate to Connected apps**

- Go to [admin.atlassian.com](https://admin.atlassian.com) and sign in.
- Select your **Organization** if you manage more than one.

  ![Select your organization to navigate to connected apps](/cms_trial/assets/608bfd41-c539-4e13-ac9c-e0d96fd5f908.png)
- In the left navigation, select **Apps**, then choose **Sites**.
- Select your target site.

  ![Under Apps_select target site.png](/cms_trial/assets/b6218341-271d-40fc-9aec-8a2c5197f0bb.png)
- In the left navigation, select **Connected apps**.
- The **Connected apps** page displays the list of apps currently installed in your instance.
- Find the Advanced Tables for Confluence app in the list of installed apps. You can use the quick search bar if needed.
- For the Advanced Tables for Confluence app, click **View app details**.

  ![In the Connected apps list, find Advanced Tables for Confluence and click View app details](/cms_trial/assets/5433901a-9567-4c0f-9964-a89eee9fefec.png)

### **App connections**

- On the app details page, click the **Connections** tab.

  ![from the Advanced Tables details page, click Connections tab](/cms_trial/assets/a87f2768-6569-48f8-bcd2-eaae158de7ac.png)
- The **App Connections** page displays a list of all Atlassian products (for example, Jira, Confluence) that this app can integrate with, along with their status (**Connected** or **Not connected**).
- To connect the **Jira** **app**, click **Connect** under **Actions**.

  ![Click Connect for Jira apps](/cms_trial/assets/123769a2-b6ab-4c26-a9e5-ab4876ebb90e.png)
- Review the permissions in the right panel detailing what data the app will access in Jira. Click **Connect** to grant permissions.

  ![Review permissions and click Connect](/cms_trial/assets/2f9236f6-32fd-4a5d-a452-c1fda6b6d719.png)
- The connection status for **Jira Apps** updates to **Connected**.

  ![Advanced Tables for Jira apps is connected to Jira Apps](/cms_trial/assets/3e50d1d6-f354-4735-a4d3-02c91d9df86b.png)
- Once connected, users can now configure the Advanced Table Viewer macro to import data from the connected Jira site. Refer to [Configure Jira work items in Advanced Table Viewer macro](/cms_trial/space/TBL/3510927447/Configure+Jira+work+items+in+Advanced+Table+Viewer+macro/).

- Once the app connection is established, the link stays active until an administrator disconnects it or authorization is revoked in Jira.
- To disconnect the **Jira** **Apps** connection at any time, navigate to the **Connections** tab and click **Disconnect**.