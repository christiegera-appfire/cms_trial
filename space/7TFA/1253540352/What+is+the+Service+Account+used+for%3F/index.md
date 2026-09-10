# What is the Service Account used for?

## Question

I see the "Service Account" on my 7pace Timetracker Settings. Can you tell me what this is and what it it used for?

## Answer

We use the [Service Account](/cms_trial/space/7TFA/1253540308/Reporting+%26+API%3A+Service+Account%2C+Reporting+%26+REST+API+and+Access+Tokens/) to perform requests and display data on some pages within 7pace Timetracker that would normally not be accessible or viewable to users with limited permission levels. The Service Account is required for server side tracking to work an it is necessary in order for Work Item Automation to function. The Service Account option helps display more accurate data to those team members with lower permission levels who do not have access to all projects. Instead of having to give these team members higher user group rights for all areas of 7pace Timetracker, you can just set up the Service Account to give them a better overall picture of the Budgets page, the Budgets Export functionality, the ability to fetch work item names within Times Explorer, and the API.

In **7pace Timetracker for DevOps Services (cloud)**, to get to the Service Account, navigate to the Settings page -> Reporting & API -> Service Account.  As a user with expanded permissions, here you can set yourself as the Service Account for all users. For more information on configuring the Service Account for 7pace Timetracker for DevOps Services, click [here](/cms_trial/space/7TFA/1253540308/Reporting+%26+API%3A+Service+Account%2C+Reporting+%26+REST+API+and+Access+Tokens/).

In **7pace Timetracker for DevOps Server (on-prem)**, you have the option of setting up or changing the Service Account in the configuration tool wizard of 7pace Timetracker. We recommend that you choose a user with the highest permission level, which is anyone who is a member of the Project Collection Administrators user group. Once complete, you can then navigate to the Settings page -> Reporting & API -> Service Account and view which Service Account has been configured. For more information on configuring the Service Account for 7pace Timetracker for DevOps Server, setting it up during initial installation or changing it post-installation, click [here](/cms_trial/space/7TFA/1253540308/Reporting+%26+API%3A+Service+Account%2C+Reporting+%26+REST+API+and+Access+Tokens/).