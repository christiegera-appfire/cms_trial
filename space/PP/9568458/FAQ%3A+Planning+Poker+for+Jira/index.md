# FAQ: Planning Poker for Jira

Here are the answers to some of your most frequently asked questions. If you think we’re missing any critical tips, let us know by getting in touch with us through the [Appfire Support Portal](https://appfire.atlassian.net/servicedesk/customer/portal/11).

## ☁️ Cloud

#### **What is the price for the plugin? Can I pay only for users who use Planning Poker for Jira Cloud?**

Answer:

You can check the price [here](https://marketplace.atlassian.com/apps/1212495/planning-poker?tab=overview&hosting=cloud).

According to Atlassian’s pricing policy, apps are billed based on the number of users in your Atlassian product. Jira Cloud apps are priced based on the maximum number of users of the Jira products on your instance. For example, if you have Jira Software (50 users) and Jira Service Management (10 agents) in the same instance, you pay the 50-user price for apps.

#### **How can I access Planning Poker for Jira Cloud plugin?**

Answer:

To access the Planning Poker for Jira plugin, simply navigate to the left side menu within each project or board. Look for the app section and select the Planning Poker for Jira tab to access the dedicated dashboard. Additionally, you can also find the application conveniently located in the upper right corner of the native Board view.

Once installed, the Planning Poker will add a new menu item in the Jira top menu and project sidebar.

| **Jira top menu App > Planning Poker** | **Software project sidebar** |
| --- | --- |
| contentId-9568458 | contentId-9568458 |

#### **Why can’t I vote for issues in the P**l**anning Poker session?**

Answer:

Planning Poker for Jira offers different user roles to ensure effective collaboration. During configuration, specific roles are assigned to users. Only moderators and estimators have the privilege to vote for issues, while spectators do not possess this capability.

If you find yourself unable to vote for issues in Planning Poker for Jira, it is recommended to review the Estimators configuration to determine your assigned role. By checking your role, you can understand the limitations and capabilities associated with your account in the Planning Poker session.

#### **I’m getting this error: “Field "customfield\_XXXXX" cannot be set. It is not on the appropriate screen, or unknown. Please, resubmit to add this estimate as comment to this issue.” How can I fix it?**

Answer:

This error happens when it is not possible to set the custom field. In most cases, this is about Story Points field, which is by default not visible on the issue detail view. To fix this problem do the following steps:

1. Go to **Project Settings.**
2. Click **Screens** from the sidebar.

   ![contentId-9568458](/cms_trial/assets/2f9689f7-08e3-4f4b-9121-cb2ed3b946e8.png)
3. Click the Screen name of the needed Issue Type.

   ![contentId-9568458](/cms_trial/assets/c137247d-4e1c-4904-b1f0-faa3f62041c1.png)
4. Add your field via the **Select Field** search box.

   ![contentId-9568458](/cms_trial/assets/ad735c51-3db4-456e-a7ce-d3a5cb3a2f7f.png)
5. If you're using **Issue New Layout**, click on the **Issue Layout**.

   ![contentId-9568458](/cms_trial/assets/d9a55bcf-01a1-43fe-871d-3063731ec1b9.png)
6. Make sure the **Story Points** field is always visible.

   ![contentId-9568458](/cms_trial/assets/9a42711c-1f21-4add-8524-dd6cfc906dcc.png)

#### **Why do I only see the message "Wait for the admin to start" while I'm in the session?**

Answer:

In Planning Poker for Jira, the estimation process within a session is initiated by the moderator. When a new session is created, the moderator needs to manually select the first issue for estimation to commence. This process does not occur automatically. Consequently, participants in the session will see the message "Wait for the moderator to start" until the moderator selects the initial issue and officially begins the estimation.

#### **How can I remove the Planning Poker icon from the project sidebar?**

Answer:

Simply go to the project sidebar and click **Project Settings** > **Planning Poker**. Then turn on the **Hide Planning Poker button in the sidebar** toggle.

![contentId-9568458](/cms_trial/assets/2ad0d0d2-7d73-494c-889e-9320e80f2466.png)

#### **Is it possible to disable the mobile version of Planning Poker?**

Answer:

Certainly! Navigate to **Manage Apps** > **Planning Poker** > **Configure**, and check the **Disable mobile version** box.

|  |  |
| --- | --- |
| contentId-9568458 | contentId-9568458 |

#### **Is there a way to restrict access to Planning Poker for specific user groups?**

Answer:

Navigate to **Manage Apps** > **Planning Poker** > **Configure**, enable the **User permissions will be checked** option, and then choose the desired user groups that should have access to Planning Poker.

## 🏬 Data Center

#### **What is the price for the plugin? Can I pay only for users who use Planning Poker for Jira Data Center?**

Answer:

You can check the price [here](https://marketplace.atlassian.com/apps/1212495/planning-poker?tab=overview&hosting=datacenter).

Data Center apps are sold as an annual subscription. You are eligible for support and version updates as long as your subscription is active.  
According to Atlassian’s pricing policy, apps are billed based on the number of users in your Atlassian product. For Jira 7.0 or later, the app tier should match the maximum tier of the licensed Jira products on your instance. For example, if you're running Jira Software (500 users) and Jira Service Management (25 agents) on the same instance, you should purchase the 500-user tier for apps.

For versions of Jira prior to 7.0, the app tier should match the licensed user tier for Jira. Even if fewer users want to use the app than your Jira license, the two licenses should match exactly.

#### **How can I access Planning Poker for Jira DC plugin?**

Answer:

To access the Planning Poker for Jira DC plugin, simply navigate to the left side menu within each project or board. Look for the Jira navigation bar and select the Planning Poker for Jira tab to access the dedicated dashboard. Additionally, you can also find the application conveniently located in the upper right corner of the native Board view.

#### **Why can’t I vote for issues in the Planning Poker session?**

Answer:

Planning Poker for Jira offers different user roles to ensure effective collaboration. During configuration, specific roles are assigned to users. Only moderators and estimators have the privilege to vote for issues, while spectators do not possess this capability.

If you find yourself unable to vote for issues in Planning Poker for Jira, it is recommended to review the Estimators configuration to determine your assigned role. By checking your role, you can understand the limitations and capabilities associated with your account in the Planning Poker session.

#### **Why do I only see the message “Please wait — Game Admin is choosing a story to estimate” while I'm in the session?**

Answer:

In Planning Poker for Jira, the estimation process within a session is initiated by the moderator. When a new session is created, the moderator needs to manually select the first issue for estimation to commence. This process does not occur automatically. Consequently, participants in the session will see the message "Please wait — Game Admin is choosing a story to estimate" until the moderator selects the initial issue and officially begins the estimation.

Alternatively, **if the moderator sees "Wait for the moderator to start",** there might be a technical issue with the way Jira communicates with the Apache server. There is an option to change the way Planning Poker connects to the Apache server.

By default, it establishes a long-time connection, and you can change the app’s behavior. To do this, navigate to the **Manage Apps** section in your Administration settings, then go to **Planning Poker** configuration at the bottom of the left-side menu. Enable the alternative socket transport mode. You can find instructions on how to do this in the following link: [poker-server-polling.mp4](https://www.screencast.com/t/dO0qv2VC)

#### **I’m getting this error: “Field "customfield\_XXXXX" cannot be set. It is not on the appropriate screen or is unknown. Please, resubmit to add this estimate as a comment to this issue.” How can I fix it?**

Answer:

This error happens when it is not possible to set the custom field.

![contentId-9568458](/cms_trial/assets/17120831-02c8-432d-8510-c419f72eb14c.png)

In most cases, this is about the Story Points field, which is by default not visible on the issue detail view. To fix this problem, do the following steps:

1. Click the Jira cog icon, and then **Issues.**
2. Click **Screens** from the sidebar.

   ![contentId-9568458](/cms_trial/assets/1e24b24e-9575-48b4-bd49-c0bae002cdf3.png)
3. Navigate to the Screen name of the needed Issue Type, and click **Configure**.
4. Add your field via the **Select Field** search box.

   ![contentId-9568458](/cms_trial/assets/c8e034c5-2fe1-4d82-a3a4-727f1ba69082.png)
5. Go to any issue in that project, and click **Edit Issue** > **Configure Fields** to make sure the Story Points field is always visible.

   ![contentId-9568458](/cms_trial/assets/204ca7eb-a02f-49b0-b0a9-88af04cd0a14.png)

#### **How can I remove the Planning Poker icon from the navigation bar?**

Answer:

Simply go to the global settings and click **Manage app** > **OTHER > Planning Poker Configuration**. Then turn on the **Hide top menu "Planning Poker” link** box**.**

![contentId-9568458](/cms_trial/assets/43cc31d5-22af-45b2-a481-850d68eb2931.png)

#### **Is it possible to disable the mobile version of Planning Poker?**

Answer:

Certainly! Navigate to **Manage app** > **OTHER > Planning Poker Configuration**, and check the **Disable mobile version** box.