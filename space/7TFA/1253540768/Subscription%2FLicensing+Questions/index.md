# Subscription/Licensing Questions

### Question

I have my Timetracker subscription ID, how do I activate it?

### Answer

This article refers to 7pace Timetracker on Azure DevOps Server (on-premises).

Timetracker can be activated with two methods - online and offline.

**Online Activation**

The online activation is the recommended way to activate Timetracker and comes with these benefits:

- On renewal, the activation continues without interruption of service
- You only need to apply the subscription ID once
- Changes to your subscription appear immediately in all your server systems

**How to apply:**

Please make sure to **copy your Subscription ID to the page Time > Settings > Subscription**, available from the web access of Azure DevOps Server.

You will find the subscription ID on any invoice or mail from the commerce system, such as on any invoices found under the Timetracker Settings page -> Subscription -> Invoices (you must be a project collection admin to access this information).

**Troubleshooting: Server not connected to the internet**

In case your server cannot connect to the internet, please [contact our Support team](mailto:supportzaure@appfire.com). We will issue a file for offline activation for you.

For more information on this topic, please see [Activating 7pace Timetracker for DevOps Server & Activating Proxy Server Settings](/cms_trial/space/7TFA/1253539922/Installation+guide/) in our user documentation.

The online activation is available since Timetracker version 2.8 and requires an internet connection for the server running the Timetracker server. Support for a proxy server is available since version 2.8.1.

### Question

How does licensing work within 7pace Timetracker with regard to named users?

### Answer

7pace Timetracker is licensed under the 'named user' model. A named user is a unique person authorized to use the software. "Use" is defined as every form of touching the software; this includes roles such as managers and administrators who need to perform any kind of operation with the software or use data created by the software in a direct connection.

Every named user needs to have a valid license. The license is not transferable to other persons once it has been assigned. If the person with an assigned license eventually stops using the software and/or resigns from his/her position in the company, his/her named user license can be assigned to a different person or can be unlicensed.

A named user can use the service on the instance (DevOps Organization/Server) where 7pace Timetracker is installed. The only exception from this is the Ultimate plan, which allows a named user to use 7pace Timetracker on unlimited instances within that enterprise.

7pace Timetracker’s Plans

**Ultimate Plan**

Unlimited accounts (cloud)

Unlimited servers (on-premise)

**Team Plan**

Dedicated account (cloud) or dedicated server (on-premise)

**Start Plan**

Dedicated account (cloud only)

**Free Plan**

Cloud only, 3 users or less

**Legacy DevOps Services Plans** (formerly VSTS)

Dedicated account (cloud only)

**Legacy DevOps Server Plan** (formerly TFS)

Unlimited accounts (cloud)

Unlimited servers (on-premise)

### 

### Question

Who sees the "7pace Timetracker Free Trial" countdown, the "Why am I seeing this?" link, along with the "Buy Now" option ribbon in 7pace Timetracker?

![FAQ_Subscription.png](/cms_trial/assets/0f9cc81f-6322-47b5-a98d-5b7d20f60bc9.png)

### Answer

You are seeing this link because you are a project collection administrator. Only project collection administrators can see this “7pace Timetracker Free Trial” countdown and the “Buy Now” option. You must be a project collection administrator to purchase 7pace Timetracker.

Non-admin users of 7pace Timetracker will **not** see this “7pace Timetracker Free Trial” notification bar, the "Why am I seeing this?" link or the “Buy Now” button. Non-admin users also don't have access to the "Subscription" page of 7pace Timetracker.

When a trial subscription is created, all regular DevOps users will see the “Time” tab (now displaying as "7pace Timetracker) and are set to the “Default” role, which is automatically set to “Team” permissions. As an administrator, you can change this default role and any specific users on your team to unique roles under Settings -> [User Management](/cms_trial/space/7TFA/1253539946/Misc%3A+User+%26+Subscription+Management/).

If an administrator wants to restrict access to 7pace Timetracker for certain users, those users can be assigned the role of “None”. On-prem DevOps Server users will then still see the “Time” tab, but will only see a “This door is locked” message on any page within 7pace Timetracker. Cloud-based DevOps Services users set to "None" will not see the “Time” (or "7pace Timetracker") tab or any 7pace Timetracker pages.

### Question

I have a monthly or annual subscription - when and how can I cancel this? What happens if I need to adjust the count of users?

### Answer

Your subscription lasts only for the time you have subscribed - one month for monthly, one year for annual subscriptions. If you don't cancel, the subscription will renew on day of expiration. You can cancel at any time, which means that the subscription will not renew any longer. You can't stop a subscription in between, your license will always be available until the end of the running period.

You can change the amount of users at any time. You can start with 10, and change to 50 after 3 weeks. And 6 weeks later you change to 5 users. Whenever you do an adjustment, the rest of your subscription period will be re-computed. If you reduce the amount of users, your account will get a credit, if you extend the amount of users and the billing will be higher, you will get charged. This is called proration. This re-computation is exact per day and the new user count is effective immediately. Your subscription will not be renewed by these actions of adjustment, the date of expiration stays the same.

You can also change your subscription length at any time, from monthly to annual and the other way round. Your subscription will be prorated (re-computed) the same way as described above.

The only thing that doesn't work - a credit can't be paid out, it will always be applied to the next invoice.

You can do all these adjustments at any time from right within 7pace Timetracker's Subscription Management module found under the "Settings" tab -> "Subscription" or from *Azure DevOps Organization settings / (Extensions) 7pace Timetracker / Permissions.*Alternatively, send us a message here in the support channel and we will help you.

### Question

If I need to uninstall and re-install Timetracker, are my records and data safe? How are work items changed with the installation or uninstallation of Timetracker?

### Answer

**Yes**, the recorded time data is safe.

Uninstalling Timetracker does only remove the executables and system registrations. The data is stored in the database and not touched by the uninstallation.

If you install Timetracker for DevOps Server (on-prem), setup checks if the tables exist in the database. If there are no tables, the tables are created. If the tables exist, they are left in their state as they are. If the tables exist in a scheme of a previous version of Timetracker, the tables are updated.

It is similar with Timetracker for DevOps Services (cloud), the only difference being that you don't need to run any installer; you do everything within your DevOps account.

Fields that were modified by Timetracker (like Completed/Remaining work) will keep their values as this data is stored directly in DevOps Server and Services and Timetracker only modifies them. After uninstall, these fields will behave as usual; Timetracker will not modify them.

### Question

What happens after my 7pace Timetracker subscription expires (or the trial period ends)?

### Answer

After your subscription has expired or your trial ends, with the cloud-based version of 7pace Timetracker, 7pace data and time records are kept for a period of up to one year. For on-premise 7pace Timetracker, data will be kept depending on your own specific self-hosted server rules.

With an expired subscription of 7pace Timetracker, the UI of Timetracker will be blocked and you will no longer be able to track or add time, export, use the 7pace API or any other Timetracker functionality.

To instantly restore full functionality within 7pace Timetracker, (re-)activate your subscription by having a project collection administrator navigate to the "Settings" page -> Subscription or contact us at sales@7pace.com.