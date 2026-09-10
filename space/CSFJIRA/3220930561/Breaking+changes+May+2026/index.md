# Breaking changes May 2026

**Release date**: May 6, 2026

Salesforce has announced an [upcoming security update](https://help.salesforce.com/s/articleView?id=005132365&type=1), effective Monday, May 11, 2026, that restricts the use of uninstalled connected apps. If you’re using an uninstalled connected app for Connector for Salesforce & Jira, it will break your connection. Review the change carefully and complete any required actions before **May 11, 2026**.

---

## Install the connected app in Salesforce

To comply with Salesforce's OAuth security requirements, make sure you’ve installed the Connector for Salesforce & Jira connected app in your Salesforce platform.

**Steps**

1. In Salesforce, go to **Setup**.
2. In the **Quick Find** box, search for **Connected Apps OAuth Usage** and select it.
3. Find **Salesforce & Jira Cloud Connector** in the list and click **Install**.  
   If you don’t see the **Install** button, the app is already installed, and you’re all set.

   ![image-20260504-144259.png](/cms_trial/assets/bc4a0630-e616-4d42-b956-9cf6e2439f2a.png)
4. Follow the instructions provided by the Salesforce UI to complete the approval.

---

As part of this security update, Salesforce refresh tokens will expire after a maximum of 30 days of inactivity. If your connection goes unused for up to 30 days, you'll need to reauthorize it. For more details, see [Revoke access for expired connection](/cms_trial/space/CSFJIRA/3224731651/Revoke+access+for+expired+connection/).

---

**Support and resources**

- For more information, refer to the following resources:  
  [Revoke access for expired connection](https://appfire.atlassian.net/wiki/pages/resumedraft.action?draftId=3224731651&draftShareId=8ab1d4d1-acf4-4433-912b-85794b9d830b).
- If you encounter any issues, raise a ticket with our [support team](https://appf.re/support)[.](https://appf.re/support)

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Connector for Salesforce & Jira !

---