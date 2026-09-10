# Transitioning of Connector for Salesforce & Jira to Appfire infrastructure

## **Customer Communication**

### **Appfire’s infrastructure transfer from ServiceRocket**

On January 11th, 2023 Appfire announced the acquisition of 20+ apps from ServiceRocket. You can find more details[here at Appfire’s news page](https://appfire.com/resource/appfire-news/were-bringing-servicerockets-best-selling-suite-of-apps-to-our-portfolio/). We are proud to announce that on July 29th, 2023, all infrastructure for the Connector for Salesforce and Jira cloud will be transferred from ServiceRocket to Appfire. As a result, a new domain URL has been generated that requires action from our customers in order to finalize the transfer process. This is an enormous accomplishment for everyone involved, and we appreciate your understanding.

#### New domain URL:

Due to security reasons, only authorized URLs are accepted in Salesforce. When you initially installed the Connector for Salesforce and Jira cloud, you whitelisted ServiceRocket’s domain, and now you will need to do the same for Appfire’s domain URL.

#### To add Appfire’s domain URL:

1. Go to the Salesforce page. In the **Quick Find** box in the sidebar, type *remote site settings*.
2. Click the **Remote Site Settings** link that appears.
3. On the **All Remote Sites** screen, click **New Remote Site**.
4. On the **Edit Remote Sites** screen, enter the following details:

   1. **Remote Site Name:**  Jira
   2. **Remote Site URL:** <https://sfjc.integration.appfire.app/>
5. Click **Save**.

Next, authorize the new whitelisted Appfire’s domain URL in Salesforce for the Connector for Salesforce and Jira package.

#### While still on the Salesforce Setup page:

1. In PLATFORM TOOLS, Select **Apps** > **Packaging** and click **Installed Packages.**
2. Select **Configure** for the **Jira Cloud for Salesforce** Package Name. Important information is displayed in a top banner.
3. Click **Update URL** to authorize Appfire’s URL for the Connector for Salesforce and Jira package.

You have successfully added and authorized the Appfire domain URL.

We appreciate your help and look forward to working with you. If you need to contact us for any reason, please do not hesitate to contact [Technical Support](https://apps.appf.re/support).