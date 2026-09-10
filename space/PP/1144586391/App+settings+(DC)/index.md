# App settings (DC)

This page is about **Planning Poker for Jira Data Center**. Using **Cloud**? [**Click here**](/cms_trial/space/PP/1144061974/Planning+Poker+for+Jira+Cloud/).

This page outlines the configuration options for Planning Poker for Jira. While most settings are common across both versions, a few differences exist.

### How to access settings

1. Click the Jira cog icon, then **Manage apps** > OTHER > **Planning Poker Configuration**.
2. Find Planning Poker in the apps list, and click **Configure**.

   ![contentId-1144586391](/cms_trial/assets/88d304f9-0910-403f-9c9f-2f9aa883f238.png)

- **Enable permissions –**   
  Use this setting to restrict access to the app for specific user groups in Jira. Users outside those groups will see a "Sorry, you don't have permissions for Planning Poker" message upon trying to access it. Keep in mind that default Jira admin groups always have access.
- **Allow users to change mobile URL –**   
  When using the mobile version of Planning Poker (as part of the Jira mobile app), users typically scan a QR code to join the game. However, in certain situations, the QR code URL may be incorrect due to the company's specific Jira configuration. Enabling this option allows users to change the mobile URL. When you click on the Mobile version button, an additional step appears to set the URL dynamically:

![contentId-1144586391](/cms_trial/assets/c1ec71a1-e737-4356-9563-75b7c2df7106.png)

![contentId-1144586391](/cms_trial/assets/eae2e3f2-a504-4250-b85f-c4dc90696286.png)

- **Disable mobile version –**   
  Completely hide the mobile version of the app (useful if your team works solely on desktops).

- **Enable alternative socket transport mode –**    
  Use this when you encounter issues such as being unable to vote in Poker games or experiencing unexpected behaviors like the message "Please wait — Game Admin is choosing a story to estimate" even when you are an admin. The app uses two communication methods, and sometimes, one might be restricted in your company's network. Enabling this lets you switch to the alternative method.
- **Hide top menu "Planning Poker" link –**   
  Remove the Planning Poker link from the Jira top menu bar.