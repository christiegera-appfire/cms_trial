# Reporting & API: Service Account, Reporting & REST API and Access Tokens

Set up your [Service Account](https://appfire.atlassian.net/wiki/x/qoO3Sg), view your Reporting API root, confirm reporting page status/health, and view team access tokens.

## Introduction

Under **Settings** > **Reporting and API** > **Service Account**, you can view the [Service Account](https://appfire.atlassian.net/wiki/x/qoO3Sg) that has been set up for your project.

The Service Account was created to perform requests and display more accurate data on some pages in 7pace Timetracker. The data is normally not accessible or viewable to users with more limited permission levels or who do not have access to all projects. Without the Service Account enabled, these users can see either of the following error messages when they open a page within 7pace Timetracker:

- *You don't have access to all projects, or some included iterations or work items were deleted. Therefore, the time calculation may not be accurate.*
- *You don't have access to all projects, iterations, or work items, or some of them were deleted. Please ask your administrator to increase your access level or set up a Service Account in Configuration - Settings.*
- On the *Budgets* page, the work items can be displayed as *removed or not available* to users with restricted permissions (these become visible when the Service Account is configured to an account with elevated permissions).

Instead of giving these team members higher user group rights for all areas of 7pace Timetracker, an administrator can just set up the Service Account to give them a better overall read-only picture of the *Budgets* page, the Budgets export functionality, the API, and the ability to fetch work item names in the *Times Explorer* page.

### 7pace Timetracker (cloud)

This is what Service Account Settings look like on the 7pace Timetracker cloud version:

![Service_Account_Settings_Cloud_Version.png](/cms_trial/assets/ad4bbe71-5e28-419f-b6e5-661ba962a999.png)

To use this feature, as an administrator, click **Set Myself as Service Account** for all users. Note that the user account that is set as the Service Account *must be a member of the DevOps Collection Administrator group* for 7pace Reporting to work.

Once you have set yourself as the Service Account user, 7pace Timetracker automatically detects the configured Service Account and displays data that is normally not accessible to all users.

Clicking the **Do Not Use Service Account** button clears this option and returns the *Budgets* page, the Budgets Export functionality, the API, and the ability to fetch work item names within *Times Explorer* back to their default settings. Thus, your team members can once again see what they saw prior to the Service Account being configured, as detailed in the error messages listed above. If your team members are seeing these messages in areas of 7pace Timetracker that currently support Service Account functionality, as an administrator, set yourself as the Service Account so that these messages disappear.

### 7pace Timetracker (on-premise)

This is what Service Account Settings look like on the 7pace Timetracker (on-prem) version:

![Service_Account_Settings_On_Prem_Version.png](/cms_trial/assets/11056cc7-6356-4c09-9c54-05f6fe6330a1.png)

As an administrator, you can configure it in the configuration tool so that all users of the system can view the data that is currently not accessible. Select a user who belongs to the Project Collection Administrator user group in the configuration tool to achieve this.

As an administrator, set up or change the Service Account in the configuration tool wizard of 7pace Timetracker. See [Configuring Service Account Settings for 7pace Timetracker Using the Configuration Tool](/cms_trial/space/7TFA/1253539922/Installation+guide/) for more information on this process.

### Configuring Service Account settings for 7pace Timetracker (on-prem) using the Configuration tool

The 7pace Timetracker configuration tool wizard automatically starts after you complete 7pace Timetracker installation. For more information on this initial process, including setting up Service Account the first time, please see the [Installation and Configuration](https://appfire.atlassian.net/wiki/x/H4G3Sg) section. You can also start this tool later by running the `TimetrackerOnline.ConfigTool` application, as described in more detailed below, from the `Tools` directory in the default location (`C:\Program Files (x86)\7pace Timetracker\`) of your 7pace Timetracker.

The Service Account setting is required in order for server side tracking to work.

#### Change Service Account settings

1. Navigate to the Timetracker Configuration tool in the `Tools` directory at the default location (`C:\Program Files (x86)\7pace Timetracker\`) of 7pace Timetracker.

![7Pace_Timetracker_Config_Tool.png](/cms_trial/assets/be545028-510b-4833-b2b4-00cf6c97cc2c.png)

2. In the **Service Account** field, check the Service Account configured.

A blank status indicates that the Service Account is not configured.

3. In the **Service Account** field, click the *Change Service Account* link.

![Service_Account.png](/cms_trial/assets/c997a17d-6b50-447d-aeea-af0495c638c5.png)

4. Click the appropriate option for the Service Account.

5. If selecting the Custom Service Account option, enter the required username and password for the selected Service Account.

6. Click the **Save** button to save the changes.

## Reporting and REST API

### 7pace Timetracker for DevOps server (on-premise)

![Report_API_On_Premise.png](/cms_trial/assets/f90766e4-672f-48cd-b7d9-553cf1d1b14c.png)

### 7pace Timetracker for DevOps services (cloud)

![Report_API_Cloud.png](/cms_trial/assets/36e1d7e4-8740-41e8-bd73-915e9bf9f66e.png)

### REST API

#### 7pace Timetracker for DevOps server (on-prem)

![REST_API_On_Prem.png](/cms_trial/assets/cc09a682-4d16-428c-b3b7-cb175dd02a57.png)

#### 7pace Timetracker for DevOps services (cloud)

![REST_API_Cloud.png](/cms_trial/assets/ffd93607-2437-4f86-a88f-f1514ad85b5d.png)

For our full documentation section on 7pace Timetracker's API, click [here](https://appfire.atlassian.net/wiki/x/noG3Sg).

## Introduction to Access Tokens

The *Access Tokens* section of 7pace Timetracker's *Settings* page displays information about tokens that are currently being used in 7pace Timetracker for DevOps services (cloud). These tokens are issued and controlled by 7pace Timetracker and are completely separate from the OAuth and personal access tokens issued by Azure DevOps.

Access tokens allow users to gain access to 7pace Timetracker for DevOps services' API, including the Reporting API and Client API, and are used when you pair the Windows app, for example.

7pace Timetracker's *Access Tokens* page also allows users and administrators to remove tokens for security reasons in the event that you suspect they were stolen or are being used by someone else. For example, if you prepare an Excel file connected by a token with the Reporting API and then share this file, the token can also be shared and your data could be accessed.

### Access Tokens

Administrators can view the access tokens of all users of 7pace Timetracker (see the screenshot below) and can also remove the tokens of these users. Users of 7pace Timetracker can view and remove only their own tokens.

![Access_Tokens.png](/cms_trial/assets/f0df8b35-a393-4949-a6a6-2a488e2c9793.png)