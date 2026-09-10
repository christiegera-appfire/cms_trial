# Install the Salesforce package in Salesforce

This page guides you through installing the Salesforce package for Connector for Salesforce & Jira. This process is essential for synchronizing Salesforce objects with issues in Jira. Follow these steps to ensure a smooth integration.

You can install the package either in you production Salesforce environment or in the Sandbox. For Sanbox instructions, see [Install the Salesforce package in Salesforce](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/).

## Before you start

- Make sure you have installed the Connector in [Jira Cloud](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/).

## For new package versions

- When a new package version is available, we push an upgrade to your Salesforce instance. This ensures your instance automatically receives bug fixes and improvements.

## Licensing and pricing

Salesforce AgentExchange displays a standard pricing notice saying: *You must pay to use this solution.* However, there’s no separate Salesforce-side charge. The app is licensed and billed entirely through your Jira subscription on the Atlassian Marketplace. The Salesforce package itself is free. If you already have an active Jira subscription, you can proceed through the AppExchange install flow without making any additional purchase.

## Install guide

1. Go to Salesforce AgentExchange and open the [Connector for Salesforce and Jira (Cloud) package](https://appexchange.salesforce.com/listingDetail?listingId=a0N3000000E7xufEAB).
2. Click **Get it Now** to install the package in the production environment or click **Try It** to install the package in your sandbox.   
   For Sanbox instructions, see [Install the Salesforce package in Salesforce](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/).

   ![AgentExchange](/cms_trial/assets/0ab4e02c-78a5-4e13-846f-b9687ad2f955.png)
3. Log in and click **Install in Production**.
4. Review the terms and conditions, then click **Confirm and Install** to move to the*Package Installation Landing* page.
5. Select one of the three installation options, and click **Install**.   
   In most cases, **Install for All Users** is the best option.

   ![Install for All Users ](/cms_trial/assets/f545754a-cb5e-4030-aaa1-2402935dc921.png)

- **Install for Admins Only** option limits permissions to admin users:

  - Only Salesforce Admins can be used as integration users to [set up a connection to Salesforce](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/).
  - Only Salesforce Admins can view the content of the [Lightning components](/cms_trial/space/CSFJIRA/1873740233/Configure+Lightning+Web+components/), even when it is added to the Salesforce Object layouts.
  - Standard users might also encounter errors, as shown [in this knowledge base page](/cms_trial/space/CSFJIRA/3091957268/%22Salesforce+security+settings+blocked+the+connection%22+error/).
  - Salesforce Professional editions only have **option two** available.
- **Install for All Users** option gives view and create permissions to all users.
- **Install for Specific Profiles**…option lets you map the values of the packaged Profile to an existing Profile in the target org. This mapping allows the Connector package's permissions and settings to be applied to a specific existing Profile in the subscriber org.

1. After the Salesforce Package is ready and installed, click **Done** to move to the*Installed Packages* screen.

## Next steps

- Add a Remote Site to allow a connection from the Salesforce Package to your Jira instance. Follow the [Add a new remote site](/cms_trial/space/CSFJIRA/1873412619/Add+new+remote+site/) instructions.