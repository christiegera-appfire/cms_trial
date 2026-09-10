# Install the Connector for Salesforce package in sandbox

This page guides you through installing the Salesforce package for Connector for Salesforce & Jira in a **Sandbox** environment. Installing in a sandbox first lets you test the integration, run through your setup, and confirm everything works as expected before rolling the package out to Production. Follow these steps to ensure a smooth integration.

## Before you start

- Make sure you have installed the Connector in [Jira Cloud](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/).
- Make sure the sandbox you're installing into is fully refreshed and available.

## For new package versions

- When a new package version is available, we push an upgrade to your Salesforce instance. This ensures your instance automatically receives bug fixes and improvements.

## Licensing and pricing

Salesforce AgentExchange displays a standard pricing notice saying: *You must pay to use this solution.* However, there’s no separate Salesforce-side charge. The app is licensed and billed entirely through your Jira subscription on the Atlassian Marketplace. The Salesforce package itself is free. If you already have an active Jira subscription, you can proceed through the AgentExchange install flow without making any additional purchase.

## Install guide

1. Go to Salesforce AgentExchange and open the [Connector for Salesforce and Jira (Cloud) package](https://appexchange.salesforce.com/listingDetail?listingId=a0N3000000E7xufEAB).
2. Click **Try It** to install the package in the Salesforce sandbox environment.

   ![ AgentExchange](/cms_trial/assets/56834806-40d8-488a-9dde-9e6411208ede.png)
3. For the *Choose a trial type* step,select **Try in your sandbox**.
4. Check your data in the *Share your contact info* step and click **Continue to Installation**.

   ![start your trial](/cms_trial/assets/647827fb-91be-4eac-b0da-d1a545023b78.png)
5. Click **Log In & Install**.
6. In the *Salesforce login* window, click **Use Custom Domain**.
7. ![Use Custom Domain](/cms_trial/assets/8805c1d5-31c3-4064-bc21-f7eab2e43ed6.png)

   For **Custom Domain**,enter your sandbox URL and click **Continue**.
8. Select one of the three installation options, and click **Install**.   
   In most cases, **Install for All Users** is the best option.

   ![Install for All Users ](/cms_trial/assets/f08703a4-9d0b-4657-a426-a2272a3e4812.png)
   - **Install for Admins Only** option limits permissions to admin users:

     - Only Salesforce Admins can be used as integration users to [set up a connection to Salesforce](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/).
     - Only Salesforce Admins can view the content of the [Lightning components](/cms_trial/space/CSFJIRA/1873740233/Configure+Lightning+Web+components/), even when it is added to the Salesforce Object layouts.
     - Standard users might also encounter errors, as shown [in this knowledge base page](/cms_trial/space/CSFJIRA/3091957268/%22Salesforce+security+settings+blocked+the+connection%22+error/).
     - Salesforce Professional editions only have **option two** available.
   - **Install for All Users** option gives view and create permissions to all users.
   - **The Install for Specific Profiles**…option lets you map the values of the packaged Profile to an existing Profile in the target org. This mapping allows the Connector package's permissions and settings to be applied to a specific existing Profile in the subscriber org.
9. After the Salesforce package is ready and installed, click **Done** to move to the*Installed Packages* screen.

## Next steps

- Add a Remote Site to allow a connection from the Salesforce package to your Jira instance. Follow the [Add a new remote site](/cms_trial/space/CSFJIRA/1873412619/Add+new+remote+site/) page for instructions.