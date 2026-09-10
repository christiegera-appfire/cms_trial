# Installation guide

### Prerequisites for 7pace Timetracker (On-Prem & Cloud)

| **Requirement** | **Details** |
| --- | --- |
| Administrator Rights | On the local system and on Azure DevOps. |
| Browser Compatibility | 3 latest versions of Microsoft® Edge, Firefox, Chrome. Internet Explorer is no longer supported (use an older version of 7pace Timetracker if using IE). |
| .NET Framework | Starting with Timetracker 5.3, .NET 4.8 and higher is required. |
| HTTPS | Both the DevOps server and 7pace Timetracker should use HTTPS. |
| ASP.NET Core Runtime Hosting Bundle (Timetracker 5.46.0+) | Requires [ASP.NET Core Runtime Hosting Bundle 6.0.14](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-aspnetcore-6.0.14-windows-hosting-bundle-installer) and higher. |
| ASP.NET Core Runtime Hosting Bundle (Timetracker 5.53.0+) | Requires [ASP.NET Core Runtime Hosting Bundle 8.0.1](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-aspnetcore-8.0.1-windows-hosting-bundle-installer) and higher. |
| Azure DevOps Server Compatibility | Compatible with Azure DevOps 2019, 2020, and 2022.  Microsoft SQL Server 2016, 2017, or later. |
| TFS (Team Foundation Server) Compatibility | Microsoft Team Foundation Server 2018, 2017 (RTM, Update 1 and later), 2015 (Update 2.1 and later).  Microsoft SQL Server 2012, 2014, 2016, 2017. |
| Timetracker Server System Requirements | Minimum: dual-core processor, 4 GB of RAM, and a fast hard-disk drive.  Recommended: quad-core processor, 8 GB of RAM, and a fast hard-disk drive / SSD.  Microsoft Windows Server 2012 or later. |
| SSL Certificate | 7pace uses Sectigo DV Wildcard SSL Certificate for the \*.[timehub.7pace.com](http://timehub.7pace.com/) domains. Validated at <https://crt.sh/?id=3448288647>. |
| SQL Server Collation | Supports only general Latin collations (e.g., SQL\_Latin1\_General\_CP1\_CI\_AS). |
| IIS WebSocket Protocol | Needs to be installed and enabled, as per DevOps server requirements. See [documentation](https://learn.microsoft.com/en-us/iis/configuration/system.webserver/websocket). |
| Authentication | Negotiate (Windows authentication) and Anonymous authentication must be enabled on the Timetracker server. Required for 7pace Timetracker API and SignalR authentication in on-premises environments. |

#### 🗔 Prerequisites for Windows App

- Microsoft® Windows® 10
- Network connection to the server running Timetracker

7pace Timetracker does not officially support a load balancer. Still, if your DevOps servers are running behind a load balancer, we have prepared a configuration that might work for you: [Running DevOps with a load balancer Timetracker configuration](/cms_trial/space/7TFA/1253540297/Running+DevOps+with+a+load+balancer+Timetracker+configuration/).

### Installation Guide for DevOps Services (Cloud)

This tutorial will walk you through the steps to enable 7pace Timetracker for DevOps Services for your organization.

### Log in to Your DevOps Services Organization

Log in to <https://dev.azure.com/> using your valid Microsoft DevOps Services organization.

*A valid DevOps Services organization is required.*

- 7pace uses Sectigo DV Wildcard SSL Certificate for the \*.[timehub.7pace.com](http://timehub.7pace.com/) domains. This certificate is valid and accepted by most systems and applications, and can be validated at this address: <https://crt.sh/?id=3448288647>.

### Install 7pace Timetracker on Your DevOps Services Organization.

After logging in, access the [Visual Studio Marketplace](https://marketplace.visualstudio.com/) and locate and click the 7pace Timetracker icon.

![Install_DevOps.png](/cms_trial/assets/5a6ab5fe-8edd-43ca-a88e-9b299350a7b7.png)

On the Timetracker app page, click **Get**.

The browser displays the organization page.

![Browser_Org_Page.png](/cms_trial/assets/a3bb437f-f975-4cca-b0df-9337037980a1.png)

Click the drop-down list and select your DevOps Services organization, then follow the prompts to install.

### Ensure "7pace Timetracker" Menu Selection Displays

Once the 7pace Timetracker server component is enabled on your organization, ensure that the "**7pace Timetracker**" menu selection appears on the main menu bar of DevOps Services. 7pace Timetracker will be visible for all DevOps users during your trial period. Upon trial expiry, Timetracker will no longer appear for users not already created in Timetracker.

### Uninstalling the 7pace Timetracker Extension

***Important:*** *When you uninstall 7pace Timetracker from your system, the installer does not automatically remove the 7pace Timetracker extension - you must follow the steps below to complete the process.*

1. Sign in to your DevOps Services account.
2. Open your Collection in the DevOps Services Control Panel.
3. Select **Extensions** from the left-side menu.
4. Click the **Uninstall** link.

### Installation Guide for DevOps Server (On-Prem)

When you first install DevOps Server, a default collection is created that contains all team projects. If you host multiple team projects in DevOps Server, you can manage these more efficiently by grouping them with other projects that have similar requirements or objectives, such as those that access a specific code base. By creating separate Team Project Collections, you can group team projects together in one or more organizational units, allowing you to manage the group of team projects as an independent resource with its own user groups, server resources, and maintenance schedule. When you create a collection, you specify the logical and physical resources that team projects within that collection can use. All the artifacts and data that those team projects use are stored in a single database of the collection.

7pace Timetracker is collection-based. Data from all collections is stored in one database. However, the data from these collections does not intersect. Each collection acts as a separate, unique organization, so you won't see Timetracker data from one collection in another collection; each collection has different data.

#### Download 7pace Timetracker Server (On-Prem)

1. Access the [7pace downloads page](https://appfire.com/products/7pace-azure-devops-server) on the Appfire website.
2. Click **Get started**.
3. Based on your operating system, click **Download Windows app** or **Download Mac app**.
4. Your browser downloads the installation file.

#### Install 7pace Timetracker Server (On-Prem)

1. Go to the location where you saved the 7pace Timetracker installation file.
2. Extract the installer zip file on your system.
3. Double-click the installer file to run the installer.

All necessary software will be checked for presence.

***Note:*** *Ensure that you are running the installer with administrator permissions.*

The system will display the Welcome page.

![Install_Setup.png](/cms_trial/assets/f9f1d1c5-c798-40cc-967d-d4b9ce8b8a50.png)

1. Click **Next**.  
   The system displays the "End User License Agreement" page.

![End_User_License_Agreement.png](/cms_trial/assets/861c4848-3a23-4b21-a91c-f2fad1180a6c.png)

5. Accept the agreement and click the "Next" button.

![Destination_Folder.png](/cms_trial/assets/2e8cd76d-537d-4ea2-a829-c32921957252.png)

The Destination Folder window displays.

6. Choose the destination folder where you want to install 7pace Timetracker (click "Change" if you want to select somewhere other than the default folder) and click "Next".

![Install.png](/cms_trial/assets/1b700d0a-1a4f-4113-a064-a08a2a0ab701.png)

The "Ready to install 7pace Timetracker" page displays.

7. Follow the installation prompts until the system displays the 7pace Timetracker Setup Wizard confirmation page.

8. After copying the files for 7pace Timetracker Server, the installer applies the necessary configurations to the system. The system then displays the Windows Security dialog box for you to enter your username and password to connect to DevOps Server. After you provide valid credentials, the installer completes the remaining installation process and displays the page, below.

![Setup_Complete.png](/cms_trial/assets/ceaabf09-5e48-4333-864d-43358ab1debe.png)

1. Click the **Finish** button.

#### Configuration Wizard - Initial Installation

After 7pace Timetracker installation completes successfully, the 7pace Timetracker configuration wizard that is bundled with the installer starts automatically.

The wizard allows you to configure Timetracker installed locally with DevOps Server or installed locally but integrated with the remote DevOps Server. You can re-start this tool any time you want, if you need to make changes, by running the TimetrackerOnline.ConfigTool application from the "Tools" folder in your 7pace Timetracker installation location.

**IMPORTANT**: **SSL v2** and **v3** protocols are enabled, as some customers still use 7pace Timetracker with legacy TFS. To switch off/on any protocols 7pace Timetracker uses in the configuration tool manually during your installation of 7pace Timetracker, please see the links, below, for guidance:  
<https://disablessl3.com/iis.html>  
<https://www.digicert.com/kb/ssl-support/iis-disabling-ssl-v3.htm>

***Note:*** *Timetracker was not tested with and does not officially support hosting in a relative/virtual directory and can only be hosted in the root directory.*

#### Configuration Guide

After installation is complete, the "Welcome!" page of the 7pace Timetracker Configuration wizard displays.

![Welcome_Message.png](/cms_trial/assets/0ed0c91d-7c7d-4525-adf7-178d4fdc8e33.png)

1. Click the **Next** button to continue.

The wizard detects the local DevOps Server on which you have installed 7pace Timetracker and displays your DevOps URL.

![DevOps_Server_Settings.png](/cms_trial/assets/6e09d2f1-c26e-48a8-88f4-a8cb1a3fefca.png)

1. Choose one of the required options from the following selections:

- **Install on local machine along with DevOps Server**: 7pace Timetracker is installed on the local system where DevOps Server is also installed.
- **Install locally and integrate with remote DevOps Server**: 7pace Timetracker is installed on the local system but integrated with the remote DevOps Server.

1. Click the **Next** button.

The system displays the "Database Settings (Microsoft SQL Server)" page.

![Database_Settings_MS_SQL_Server.png](/cms_trial/assets/920d6310-c0f7-4f9d-b28e-fa9c4663c8a9.png)

***Note:*** *On the "Database Settings (Microsoft SQL Server)" page, the option to select the same Microsoft SQL Server as DevOps Server is disabled if you are configuring your 7pace Timetracker with a remote DevOps Server. In that case, you will need to specify the SQL Server details. Also, please note that only general Latin collations in the SQL Server database (for example: SQL\_Latin1\_General\_CP1\_CI\_AS) are supported.*

1. Check that the database server name and authentication details are correct and click the **Next** button.

The system displays the "Internet Information Server (IIS) Settings" page.

![Internet_information_Server_Settings.png](/cms_trial/assets/ccf12d4e-6163-46c0-82ca-4ebd44d74c9f.png)

***Note:*** *7pace Timetracker is using the same technology as DevOps Server, and we put a security cookie into every request. This cookie can, in some cases, interfere with the DevOps Server cookie. Having Timetracker on the same domain as DevOps Server can cause cookies to be overridden. The solution is to change the address of Timetracker to something distinct/different from the DevOps Server address.*

1. Check that the "Host Name" and "Network Host Port" are correct.

***Note:*** *The* ***HTTPS Certificate*** *drop-down list only appears if you are using secure HTTP (that is, 'https'). The configuration tool only looks for certificates in the Web Hosting store. If the certificate is stored in a personal or alternative store, it will not be listed.*

1. Click the **HTTPS Certificate** drop-down list and select the certificate that you want to use.
2. Click the **Build-in-Account** drop-down list, and select the application pool account or click the **Custom Account** and specify the custom account details.
3. Click the **Next** button.

The system displays the "Service Account" page.

![Service_Account.png](/cms_trial/assets/22c73ae2-227e-4025-a1f9-5593393cbecf.png)

Here, you can configure the "Service Account" (found within the "Settings" page of 7pace Timetracker -> "Service Account") to display data that is usually not visible to all users. You can either enter the details for a "Custom Service Account" (we recommend that you use a team member who belongs to the Project Collection "Administrators" user group, since this has the highest permission level), or use the same account that you configured as the Application Pool Account. **Important: The Service Account is required in order for server-side tracking and Work Item Automation to work. You can read more about it here:** [**What is the Service Account used for?**](/cms_trial/space/7TFA/1253540352/What+is+the+Service+Account+used+for%3F/)

1. Enter a valid username, including the domain name, if necessary.
2. Enter a valid password for the specified username.
3. Click the **Next** button to continue.

The **Email Settings** page displays.

![Email_Settings.png](/cms_trial/assets/ef45f238-8dff-4faf-b51a-42e5abb83c14.png)

If you "Enable Email Alerts", the users will receive an email notification when tracking was stopped by the system due to no response from the user during activity checks. Under "Authentication", most mail servers require authorization in order to send emails. Please enter your credentials here.

1. Click **Next**.

The **Installing Work Item Form Contributions** page displays.

![Install_Work_Item_Form_Contributions.png](/cms_trial/assets/195da576-0312-4231-a306-5728d1f07504.png)

This window allows you to select the Project Collections to which you want the 7pace Timetracker tab and "Start Tracking" button on the work item form to be installed.

1. Click **Next**.

The tool starts applying the settings.

![Apply_Settings.png](/cms_trial/assets/b49512ee-41b6-4678-880f-5241d4b9a488.png)

1. Click **Next**.

After a "Kudos! 7pace Timetracker is configured and ready to go" message, the wizard setup will be complete.

1. Click the **Finish** button to close the wizard.

### Making Configuration Changes

Once you successfully complete the installation of 7pace Timetracker for DevOps Server and configure it with the automatic configuration tool wizard that is bundled with the installer, the configuration tool is a part of your system. This tool allows you to configure Timetracker installed locally with DevOps Server or installed locally but integrated with the remote DevOps Server. Should you need to make any configuration changes in the future, it's easy to open the tool and make those changes at a later time.

The **Service Account is required** for server-side tracking and Work Item Automation to work. Additionally, there is a new page to assist you in setting up **email notifications** in the Timetracker configuration wizard.

You can find the 7pace Timetracker Configuration tool in the Tools directory at the default location (`C:\Program Files (x86)\7pace Timetracker\`) of Timetracker.

7pace Timetracker Configuration Tool

![Configuration_Tool.png](/cms_trial/assets/63b3c345-2a0c-4e6d-95e5-7f8eee7c5282.png)

#### Starting and Stopping 7pace Timetracker

With the 7pace Timetracker configuration tool, you can start and stop the 7pace Timetracker application.

1. From the Windows start menu, run the 7pace Timetracker Configuration tool.
2. In the **7pace** **Timetracker Status** field, check the current status of 7pace Timetracker (if it is running or stopped).

![Status_Running.png](/cms_trial/assets/8d8ed184-579b-4f6c-b705-1998eb804d45.png)

1. In the **7pace Timetracker Status** field, click the **Start/Stop Application** link.

![Start_Stop_Application_Pool.png](/cms_trial/assets/2cc61ee2-d376-462e-9846-edbc90c5da8e.png)

The "Start/Stop Application Pool" window displays.

- If 7pace Timetracker DevOps Server is running, click the **Stop** button to stop the 7pace Timetracker application.
- If 7pace Timetracker DevOps Server is stopped, click the **Start** button to start the 7pace Timetracker DevOps Server application.

1. Click the **Close** button to close the window.

#### Changing IIS Settings

With the 7pace Timetracker DevOps Server configuration tool, you can "Change IIS Settings".

1. From the Windows start menu, run the 7pace Timetracker Configuration tool.
2. In the **Application Pool Account** field, check the current application pool configuration.

![Change_IIS_Settings.png](/cms_trial/assets/b83496d3-bcdd-4a09-8cf2-59414b186a6f.png)

1. In the **Application Pool Account** field, click the **Change IIS Settings** link.

![IIS_Settings.png](/cms_trial/assets/18bca49a-0ea8-4acd-bb27-d05dc1045ab3.png)

The system displays the IIS Settings window.

1. Specify the appropriate values for the **Host Name** and **Network Host Port**.

(Optional) Click the **HTTP Certificate** drop-down list and select the appropriate certificate.

***Note:*** *The* ***HTTPS Certificate*** *drop-down list only appears if you are using secure HTTP (that is, 'https'). The configuration tool looks for certificates only in the Web Hosting store. If the certificate is stored in a Personal or other store, it will not be listed.*

1. In the **Application Pool Account** section, select the account that you want to use or specify the custom account settings.
2. Click the **Save** button.

#### Changing the DevOps Server URL

From the DevOps Server Timetracker configuration tool, you can change the DevOps Server URL.

1. From the Windows start menu, run the 7pace Timetracker (on-prem) Configuration tool.
2. In the **DevOps Server URL** field, you can see the DevOps Server URL that is currently configured.

![DevOps_Server_URL.png](/cms_trial/assets/f127f40d-1b20-435e-9212-c072c456a1f5.png)

1. In the DevOps **Server URL** field, click the **Change DevOps Server URL** link:

![Change_DevOps_Server_URL.png](/cms_trial/assets/72f9810d-6be5-49aa-97ca-4d67261a5994.png)

1. In the **DevOps Server URL** field, enter a valid DevOps Server URL.

(Optional) Click the **Show me where to find this information** link to for additional information on where you can get the correct DevOps Server URL.

1. Click the **Save** button.

#### Changing SQL Settings

From the 7pace Timetracker configuration tool, you can change the SQL Server settings.

1. From the Windows start menu, run the 7pace Timetracker Configuration tool.
2. In the **SQL Server** field, you can see the SQL Server that is currently configured.

![Change_SQL_Settings.png](/cms_trial/assets/09b5f797-aad3-4a72-9f6e-c58d179f56cb.png)

1. In the **SQL Server** field, click the **Change SQL Settings** link.

![Change_SQL_Settings_Link.png](/cms_trial/assets/3f700bdc-d0c6-45dc-a541-4369e5ac1422.png)

The Database Settings window displays.

1. Select the appropriate server name and the authentication required for that server.
2. Click the **Save** button.

#### Changing the Service Account

**Important:** Please note that the **Service Account is required** for server-side tracking and Work Item Automation to work. You can read more about it here: [What is the Service Account used for?](/cms_trial/space/7TFA/1253540352/What+is+the+Service+Account+used+for%3F/)

1. From the Windows start menu, run the 7pace Timetracker Configuration tool.
2. In the **Service Account** field, you can see the Service Account that is currently configured.

![Change_Service_Account.png](/cms_trial/assets/9781c535-a8f0-4e7e-9658-241bbe7d695f.png)

***Note:*** *A blank status indicates that the Service Account has not been configured.*

1. In the **Service Account** field, click the **Change Service Account** link.

-> The system displays the Service Account window.

7pace Timetracker Service Account Window

![Change_Service_Account_Link.png](/cms_trial/assets/461ef5bd-df8f-4660-bd56-c9035b3dc23c.png)

***Note:*** *Users don't have the option to not use the Service Account when configuring Timetracker, as it is required for server-side tracking to work.*

1. Click the appropriate option for the Service Account.
2. 5. If selecting the "Custom Service Account" option, enter the required username and password for the selected Service Account.
3. 6. Click the **Save** button.

#### Changing Email Settings

From the 7pace Timetracker configuration tool, you can change Email Settings.

1. From the Windows start menu, run the 7pace Timetracker Configuration tool.
2. 2. In the **Email Settings** field, you can see the email account that is currently configured.

![Change_Email_Settings.png](/cms_trial/assets/b48683bb-fb48-4a00-8ce6-645588945daa.png)

1. In the **Email Settings** field, click the **Change Email Settings** link.

![Change_Email_Settings_Enable_Email_Alerts.png](/cms_trial/assets/ec6f04fa-ece9-43aa-81b5-be4e9d7366cb.png)

The Email Settings window displays.

1. You can choose to enable or disable email alerts. If enabled, users will receive an email notification when tracking was stopped by the system due to no response from the user during time tracking activity checks. Under "Authentication", most mail servers require authorization in order to send emails. Please enter your credentials here.
2. Click the **Save** button.

#### Update Availability

From the 7pace Timetracker configuration tool, you can update the "7pace Timetracker" tab and "Start Tracking" button (added to the work item form) settings.

![Update_Availability.png](/cms_trial/assets/68bc081f-b8d0-4e04-b4c0-38b23a533617.png)

Clicking the "Update availability" link allows you to reinstall the WiT "7pace Timetracker" tab and "Start Tracking" button (added to the work item form) to existing collections. If you create a new collection, you can navigate to the configuration tool and manually apply the "7pace Timetracker" tab and "Start Tracking" button here.

### Activating 7pace Timetracker for DevOps Server (Online & Offline) and Activating Proxy Server Settings

#### Activating 7pace Timetracker

***Note:*** *Before purchasing a license for 7pace Timetracker for DevOps Server, install the trial version by downloading the application from* [*www.7pace.com*](http://www.7pace.com)*. With the trial, you can use all 7pace Timetracker features for 28 days, without any limitations.*

To determine the best 7pace Timetracker subscription for you and your team, please view our different per-user pricing plans at <https://www.7pace.com/pricing>. The purchasing experience is within the installed software. After starting a trial or installing Timetracker, head for the 'Organization Settings' of your Azure DevOps organization, and look for '7pace Timetracker'. Here, you can manage your subscription. For more information on purchasing before or after your trial expires, see [How to Buy 7pace Timetracker After Your Trial Ends](/cms_trial/space/7TFA/1253539946/Misc%3A+User+%26+Subscription+Management/).

**You will find your subscription ID on any invoice or email from the commerce system**. 7pace Timetracker can then be activated via two different methods - **online** or **offline**.

#### Applying your license online

Online activation requires an internet connection to run 7pace Timetracker server. Support for a proxy server is available. For more information, see below.

We recommend online activation of your license because of the following benefits:

- Upon renewal, activation continues without interruption of service
- You only need to apply your subscription ID once
- Changes to your subscription appear immediately in all your server systems

1. On the "Settings" page, select "Subscription" or follow the direct path Organization Settings -> Extensions -> 7pace Timetracker -> Subscription.

![Extension_Subscription.png](/cms_trial/assets/864ecbd9-266a-41a0-85fe-0e7fd690d6e9.png)

1. On the "Subscription" page, you can click "Buy Now" if your trial has expired or under "Do you have an existing subscription?" copy and paste your subscription ID into the "Subscription ID" field and click the "Apply" button.

The page refreshes, displaying subscription info.

![Subscription_Current_Plan.png](/cms_trial/assets/2114605c-71da-424f-aba3-40277bedb2d0.png)

#### Applying your license offline

If your server cannot connect to the Internet, please contact us at [support@7pace.com](mailto:support@7pace.com) and provide us with your subscription ID. We will issue a file for offline activation for you.

1. On the 7pace Timetracker menu bar, click **Settings** - > Subscription or follow the direct path Organization Settings -> Extensions -> 7pace Timetracker -> Subscription.
2. Click the **Enforce offline validation** **mode** hyperlink.

![Enforce_Offline_Activation.png](/cms_trial/assets/f56dbc4e-69a8-40ec-bafa-e3c7ab04e478.png)

1. The file dialog box opens.
2. Click the **Continue to enforce Offline Activation** link to select the license file.  
   5. Apply the license.

#### Enabling proxy server settings

When you use an online subscription ID to activate your 7pace Timetracker for DevOps Server license, Timetracker keeps connecting to the license server to check whether the subscribed license is active or not. However, if your DevOps server is behind a proxy server, Timetracker won't be able to connect to the license server and will display a message that your license is inactive.

***Important:*** *Currently, 7pace Timetracker only supports the http(s) proxy settings.*

1. On the "Settings" page of the 7pace Timetracker menu, click on "Subscription" and follow the hyperlink or access directly from path Organization Settings -> Extensions -> 7pace Timetracker -> Subscription.

![Enable_Proxy_Server_Settings.png](/cms_trial/assets/0cf1e91d-213a-42d4-8873-29b159a216ee.png)

1. Click the **Proxy settings** link.

The Proxy Settings for the License dialog box opens.

![Proxy_Settings.png](/cms_trial/assets/7c6e5749-11d7-43f5-a441-d5d10f4c2dad.png)

1. Click the **Enable proxy** check box.

![Proxy_Settings_for_License.png](/cms_trial/assets/e6022b64-2da4-4586-9dfa-309d43f012d4.png)

1. In the **Server address and port** field, specify the correct proxy server address with the port number.  
   (Optional) Click the **Use PROXY authentication** checkbox if your proxy server requires authentication.
2. In the **Username** and **Password** fields, type in your credentials.
3. Click the **Apply** button.

You might get an error message if the specified proxy server address is incorrect or the specified proxy server is not reachable.

Upgrading 7pace Timetracker for DevOps Server (On-Prem) & Updating DevOps Server

#### 7pace Timetracker 3 and later

*You can update DevOps Server while still keeping Timetracker 3 and above installed. Prior to Timetracker 3, you had to uninstall Timetracker first, before you were able to update DevOps Server. With Timetracker 3 and higher, you no longer have to uninstall Timetracker before beginning your DevOps Server update.*

#### Timetracker 2.x

*For 2.x versions of Timetracker, you can update DevOps Server while keeping Timetracker 2.x installed if you are not crossing releases/updates of DevOps Server with architecture changes. Otherwise, you will have to uninstall Timetracker before upgrading your version of DevOps Server. For additional information and instruction on how to do this, please read* [*this article*](/cms_trial/space/7TFA/1253539917/7pace+Timetracker+Legacy+Versions+and+Legacy+TFS/) *in the "FAQ" section of our Knowledge Base.*

#### Upgrading Timetracker

Upgrading 7pace Timetracker for DevOps Server to the latest available version does not require you to backup your data or save any custom settings from your current version; existing data and settings are retained in the database. In addition, there is not a fixed upgrade path that you need to follow; you can upgrade from any previous version of the application to the very latest version available on the 7pace Timetracker website. (Please note that there is no way to roll back from Timetracker to previous versions once the update has been done.) Although you can directly download 7pace Timetracker to your production environment, we recommend that you first do so to your test environment to identify any issues specific to your environment. You also need to ensure that your current version of DevOps Server supports the latest version of Timetracker.

#### Before You Start

Read and/or subscribe to the [7pace Blog](https://www.7pace.com/blog/) for the most up-to-date list of features, fixes, and improvements in the version to which you want to upgrade.

#### Update DevOps Server

1. Ensure that DevOps Server is updated to the latest supported version. On your DevOps Server, open the Administration Console and check the current DevOps Server version in **Application Tier Summary**.

![Update_DevOps_Server_Version.png](/cms_trial/assets/738e2b7c-6691-487c-8787-af6a9597a0f7.png)

1. Access the Microsoft Visual Studio website (<https://www.visualstudio.com/>) and download the required update for your DevOps Server version (refer to the [Microsoft MSDN](https://www.visualstudio.com/news/tfs2015-update2-vs) website for information on the latest DevOps Server update).
2. 3. After completing the update, check that you can successfully access DevOps Server. If it is running properly after the update, you are now ready to upgrade your version of 7pace Timetracker.

#### Install the Latest Version of 7pace Timetracker

1. Go to the 7paceTimetracker website (<https://www.7pace.com/download>).
2. 2. On the [Download](https://www.7pace.com/download) page, check the supported system requirements.
3. 3. Download the latest 7pace Timetracker version that will support the updated version of your Azure DevOps.
4. 4. Install 7pace Timetracker, as per the installation guide, above.
5. 5. After the installation has successfully completed, check the "About" or "Overview" page of Timetracker within the "Settings" page.

   - Go to **Time** > **Settings** > **About**.
   - Check that the version number has changed to the upgraded version.

### Uninstalling 7pace Timetracker

***Note:*** *Uninstalling 7pace Timetracker Server does not remove its data from the database. You can install it again after uninstalling it and view your previous data on all pages (data will be retained for one year).*

1. Go to your DevOps Server system where you installed 7pace Timetracker.
2. Open the Windows Control Panel and then select "Programs".
3. Click "Uninstall".
4. Select 7pace Timetracker and click the **Uninstall** button.

### .NET Core Update Requirements

With the release of Timetracker 5.53.0, 7pace Timetracker made the switch to .NET 8

1. .NET 8 runtime bundle is a prerequisite for this update. Please make sure you install it before proceeding (see [documentation](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-aspnetcore-8.0.1-windows-hosting-bundle-installer)).
2. System requirements: 7pace Timetracker no longer supports TFS 2015 (any version) and requires Windows Server 2016 or Windows 8.
3. Please ensure that your DevOps Server and Timetracker instances use HTTPS protocol.
4. This version of 7pace Timetracker introduces significant changes. Please make sure you backup your database before proceeding.
5. During the installation, you will be asked to enter all passwords (SQL Server, Service Account and Email) again when configuring Timetracker. Please ensure you are ready to enter the required information when prompted.
6. .NET 6 runtime bundle is a prerequisite for 7pace Timetracker 5.46 - 5.52
7. Net Core 3.1 runtime bundle is a prerequisite for 7pace Timetracker 5.11 - 5.44.3

### List of IP Ports and URLs that Should be Whitelisted

The following IP addresses must be whitelisted:

- **40.114.210.78**
- **13.89.172.5**
- **13.71.123.138**
- **13.70.72.34**
- **20.50.2.18**

The following domains should be also whitelisted:  
**\*.cdn.7pace.com**  
**\*.timehub.7pace.com/**  
**timehub.7pace.com**   
**\*-7pace-timetracker.azureedge.net**  
**panel.timehub-services.7pace.com**

### Inherited Process Model Configuration vs. XML

Starting with Azure DevOps Server 2019, the Inheritance Process Model configuration is supported. This has been the default process used in Azure DevOps for quite some time now.

Upon creating a new collection in your Azure DevOps Server 2019 and newer, you will be asked to choose the process model for the new collection (see screenshot below).

![Create_Team_Project_Collection.png](/cms_trial/assets/d8940592-ad16-483f-afdb-574c52b6f7fb.png)

The main difference for 7pace Timetracker (and the end user) is that to add Work Item Contributions (the additional "7pace Timetracker" tab and "Start Tracking" button on the work item form) for an XML-based collection, it is required to modify all Work Item types' XML and upload modified XML definitions back to DevOps server.

In the Inheritance Process Model, this is no longer required and supported, and extensions will work out-of-the-box after installation. In this case, the 7pace Configuration Tool will display a disabled checkbox on the "Installing Work Item Form Contributions" window:

![Installing_Work_Item_Form_Contributions.png](/cms_trial/assets/2f63fb0f-581b-4cc0-a9df-40ae938d073c.png)

To configure visibility in the inherited processes, you can navigate to the Process Customization page and change the visibility of Timetracker contributions (see details [here](https://docs.microsoft.com/en-us/azure/devops/organizations/settings/work/custom-controls-process?view=azure-devops)).

### Collecting 7pace Timetracker Error Logs

7pace Timetracker does not generate error log files, however, you can use the Event Viewer application of the Windows operating system to collect any error details in Timetracker.

#### Timetracker Web Application

1. On the Windows system where you installed the 7pace Timetracker Server, open the **Windows Event Viewer** application.

![Windows_Event_Viewer.png](/cms_trial/assets/fdbfebb7-b060-447c-bf7b-83073f189048.png)

1. In the left pane, click **Event Viewer (Local)** -> **Windows Logs** -> **Application**.
2. In the applications list, search for **Error** in the **Level** column.
3. Select the **Error** level.

![Select_Error_Level.png](/cms_trial/assets/652ab7da-3f97-4754-9af4-6cf4666521d6.png)

The General tab displays the error details.

1. Copy the error details and paste those details into a text file.
2. Send the text file to the 7pace Timetracker Support team for further analysis of the error.

#### 7pace Timetracker for Windows App

To access Windows App error logs, please navigate to:

%APPDATA%\Local\Timetracker\{win app version}\app.log

### Managing Internal Targets

Internal targets are tasks that fall outside the realm of epics, stories, features, and work items, such as **vacation**, **sick days**, **meetings**, **parental leave**, **travel**, etc.

You can manage your internal targets in 7pace Timetracker in one of the following ways:

- Include them as part of your project and/or sprint
- Maintain them independently

#### Include Internal Targets as Part of Your Project

To include internal tasks as part of your project or sprint, you would simply create separate work items for the vacation, sick days,meetings, etc., within the project or sprint, and ask your team members to track time to these work items. The downside to this method is that when your sprint is over, the internal tasks are included in that, and so you then loose the detailed history that goes with it.

#### Maintain Internal Targets Independently

To maintain your internal targets independently from your project work items, you would create a separate project for them, define the work items for each internal target/task, and then track time to those targets/tasks.

Managing internal targets independently from within a separate project has the following benefits:

- **Define once, use forever**: You define the work items once in a separate project, irrespective of the project or sprint, and keep tracking time to them indefinitely.
- **Budget Assignment**:You can assign a budget to the project that contains your internal targets and then ask your team members to track time against that budget. Once you set the budget, you can always check the time tracked for the internal targets across the budgeted time. This provides managers with detailed information about planned vs. tracked time by all team members for all internal targets.
- **Data Analytics**: You can export time details for the project containing internal targets and generate reports that provide detailed analysis of the time spent on these tasks by all your team members. For example, if a team member took one vacation day in a given work week, they would fill out their timesheet for that week with eight (8) hours logged to an internal target/task that belongs to its own separate project. When the time details report is generated, you can clearly see the total time spent by that team member on true work items and the time logged as vacation.

### Configuring Internal Targets as an Administrator

Below, we have listed the steps that you, as an administrator, need to perform to configure internal targets/tasks, from identifying which tasks you want to include, to setting up the template, structure, and hierarchy.

***Note:*** *We have explained these steps according to the 'Scrum' project template, but you can use any template. You do, however, need to ensure that you maintain proper hierarchy from project to work items.*

1. **Identify all required internal targets**

For example, vacation, parental or extended leave, meetings, travel.

1. **Create a new project in Azure DevOps for your internal targets**

For example, "Internal Targets".

***Note:*** *While naming the project, we advise you to choose a name that you can easily recognize and distinguish from other projects as unique to internal targets.*

1. **Create a "placeholder" iteration to group the PBIs and tasks**

For example, "Internal-tasks".

You can use this iteration to group the PBIs and tasks created for the internal targets.

1. **Create a single PBI for the entire team or separate PBIs for different groups in the team.**

For example, "Internal" or "Int-Developers", "Int-Testers", "Int-Support".

1. **In the PBI, create task-type work items for each internal target that you identified for your team.**

For example, int-vacation, int-leaves, int-travel, int-daily scrum, int-sprint review, int-sprint planning, and so on.

***Note:*** *You'll notice that the naming structure of the PBIs and work items we used starts with a specific string, like "Int". You can elect to follow a similar naming structure so it's easier to search for these work items when you add time or filter them in reports.*

After performing these steps, the Azure DevOps project (with 'Scrum' template) structure will look something like this:

![Internal_Team_Tasks.png](/cms_trial/assets/d53b8866-7136-45cd-ac19-9ed8c2c41eae.png)

1. **(Optional) Create a new budget and assign the PBIs and tasks for internal targets to the budget.**

On the "Iteration" page, you can view the items created for internal targets. Assign a budget to these items, if desired.

### Tracking Time for Internal Targets as a Team Member

Once an administrator creates the outlined internal targets and shares the work item IDs for those, as a team member, you can then either track your time using the Windows or Mac App or the built-in Web App (for example, for a meeting) or manually add time after-the-fact (such as for a sick day or vacation) on the "Monthly" or "Timesheet" pages or directly on the internal target work item ID.

### Viewing Time for Internal Targets as a Manager or Team Lead

For a manager or team lead, Timetracker provides different options for you to view the worklog details of internal targets. On the "Times Explorer" page, you can filter by project, title, or team member to view exactly the details you want to see. On the "Budgets" page, you can export the details of just the internal targets project and view those details in Excel.