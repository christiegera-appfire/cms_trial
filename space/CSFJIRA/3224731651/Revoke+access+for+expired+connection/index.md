# Revoke access for expired connection

## **Summary**

This issue is caused by a Salesforce security policy that automatically expires refresh tokens after 30 days of inactivity. Once the token expires, the connection between Salesforce and Jira stops working, and all automated workflows and data syncs that rely on it will fail until an administrator reauthorizes it.

**No data is lost when a connection expires.** Existing Salesforce and Jira records are not affected. Only new syncs and automated workflows are paused until the connection is reauthorized.

### **Symptoms**

You may encounter the  **Salesforce authorization failed** error when a connection has expired. Automated workflows and data syncs between Salesforce and Jira stop working until the connection is reauthorized.

## Before you start

Make sure you have:

- Jira administrator permissions - only Jira administrators can revoke and reauthorize connections.

## Resolution

Complete step 1 for connections in Jira.

Complete step 2 if you use the Jira connections in Salesforce.

### **1. Revoke access for the connection**

1. In Jira, go to **Apps** from the left sidebar.
2. Under *Connector for Salesforce*, click **Connections**.
3. Select the impacted connection, and click **Revoke Access**.

   ![Connector for Salesforce Connections page with the Revoke Access button selected for an expired connection.](/cms_trial/assets/365f7c80-7cf7-40ad-8551-a03484d0c212.png)
4. Click **Revoke** toconfirm.
5. Click **Authorize**.
6. Sign in with Salesforce credentials when prompted.

### **2. Change the Access Token in the Salesforce connection**

1. In Salesforce, click **Settings**> **Setup**.
2. In the sidebar, use **Quick Find** to find *Package* and go to **Installed Packages**.
3. Look for *Jira Cloud for Salesforce* and click **Configure**.
4. Click **Change access token** next to the connection.

   ![Jira Cloud for Salesforce configuration page with the Change access token option highlighted.](/cms_trial/assets/197ac89f-af6e-4d51-a97d-8ceffa9a3770.png)
5. Switch to Jira and go to **Apps** from the left sidebar.
6. Under *Connector for Salesforce*, click **Connections**.
7. Click **Menu** (▢)> **API Access Token.**

   Image — asset pipeline pending  
   Connections page showing the More actions menu with API Access Token selected.
8. The *API Access Token*dialog window appears with the **Salesforce access token.**

   ![Salesforce access token shown in the API Access Token page.](/cms_trial/assets/675497d2-7209-4f97-9e14-05b793197664.png)
9. Copy the Salesforce access token and save it.
10. Under **Access Token** in the *Change Access Token* window, paste the new Salesforce Access Token you have just copied in step 9.

    ![Change Access Token dialog with the Access Token field highlighted.](/cms_trial/assets/fd7e1a71-9c4d-489e-ab9a-8b76f6ea40fc.png)
11. Click **Save**.