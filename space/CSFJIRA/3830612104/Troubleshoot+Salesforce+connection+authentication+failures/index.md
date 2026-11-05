# Troubleshoot Salesforce connection authentication failures

Connector for Salesforce & Jira checks connection health each time you open the Connections administration page. The page shows the status of each connection and the date it was last used. Use this article to identify and resolve connections with authentication problems.

## Before you start

Before you start, make sure you have administrator rights in Jira.

### Identify an affected connection

1. In Jira, select **Apps** from the left sidebar.
2. Next to *Connector for Salesforce and Jira,* click **Menu** (▢) > **App settings**.
3. Under *Connector for Salesforce and Jira*, click **Connections**.

   ![Connection health](/cms_trial/assets/4161d8f5-9ac1-4aa9-b89a-9003eed59549.png)
4. Under the *Status* column, review any flagged connections.

- **Expired**: The connection has expired because the refresh token is no longer valid. You need to revoke access and reconnect.  
  For detailed instructions, see [Revoke access for expired connection](https://appfire.atlassian.net/wiki/pages/resumedraft.action?draftId=3224731651).
- **Inactive user**: Authentication fails because the Salesforce user who created the connection is no longer active. You need to reauthorize the connection with an active user.   
  For detailed instructions, see [How to change the Salesforce integration user](/cms_trial/space/CSFJIRA/2256308548/How+to+change+the+Salesforce+integration+user/)
- **Connection issue**: The connection health check failed, and the cause could not be determined. You need to revoke access and reconnect.

### **Avoid expiration**

Check the **Last used** date. If a connection has been idle for a long time, use it again so it doesn’t expire. Salesforce can disconnect a connection after the inactivity period set in its Refresh Token Policy.

### **If the problem persists**

Contact Appfire Support and provide the affected connection details and the displayed failure reason.