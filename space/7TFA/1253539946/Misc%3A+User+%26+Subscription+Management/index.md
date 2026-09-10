# Misc: User & Subscription Management

Add new users, change user roles, buy Timetracker after your trial ends, change your subscription, view invoices, and apply the Free plan.

## User Management settings

**User Management** resides under the *Settings* page of 7pace Timetracker or from *Azure DevOps Organization settings*/*(Extensions) 7pace Timetracker / Permissions*).

![Permissions.png](/cms_trial/assets/196a8e5b-dd1e-4bb4-884a-7ad3dfbb68f8.png)

If you are a project collection administrator, you can assign any of your DevOps users the permissions and user roles they require. If you have a dedicated administrator of a system, that person is no longer required to have an administrator role (or a license) in 7pace Timetracker, but can still manage users.

### User roles general information

Keep in mind the following points when assigning permissions/user roles to your team members:

- Assignment of user roles determines the information and pages accessible to the user.
- All users who have access to 7pace Timetracker can create worklogs.
- Users have full control over their time tracking.
- If a worklog has been added by someone on behalf of a user (like a manager for a developer), both the manager and developer can alter that worklog the first time. However, if the developer makes any changes, it can be altered only by that developer going forward. Unless, a specific role has been selected in the "Editing Time" dropdown under **Settings** > **General** > **Rules**, allowing that role to edit other users' time.
- A user assigned the **NONE** role has no access to 7pace Timetracker. DevOps server (on-prem) users assigned to **NONE** can still see the *7pace Timetracker* tab, but can only see a *You don't have access to this feature.* message if selected. They can see the *7pace Timetracker* section on the work item form with the **Start Tracking** and **Add Time** buttons. Instead of the buttons being displayed, they will see a *You don't have access to this feature*. message. If they try to click any page in 7pace Timetracker, they will see a *This door is locked* message. DevOps services (cloud) users set to **None** cannot see the *Time* or the *7pace Timetracker* tab or any 7pace Timetracker pages at all.
- Changes made on DevOps server's own time management **Remaining Time** field are not restricted by 7pace Timetracker, even if these fields are set to be under the control of 7pace Timetracker.

### Licensed users - how to view and change user roles

Clicking the blue path link, as depicted in the above screenshot, brings you to the *Permissions* page, defaulting to show licensed users of 7pace Timetracker.

![Licensed_User_View_Change_Role.png](/cms_trial/assets/f49b786c-cc0e-4fa3-a1d1-92498a804b7c.png)

Selecting a user causes their current role to display (**Administrator**, in the example below) and a list of assignable roles to display on the right.

![Permissions_Administrator.png](/cms_trial/assets/27d80006-5476-4c0f-ad81-63215f666698.png)

You can select multiple licensed users or click **Select all** and assign them to a new role all at once (helpful for larger teams).

When you select a user in the left panel and then click a corresponding **Role** in the right panel, the role that you assign to that user is immediately effective without having to save anything. The **None** role is an exception that asks for confirmation.

### Unlicensed users - adding new users

![Unlicensed_User_Add_New.png](/cms_trial/assets/f8038629-2e83-49c6-95b3-3cfdb68d7aa3.png)

Clicking the blue **+ Add Users** button causes a separate window to open, displaying unlicensed users.

![Add_Users_Unlicensed.png](/cms_trial/assets/43b7c8a2-e53b-49d1-ab05-4a7821bc5f4e.png)

Select a user or multiple users, if applicable, and then click the **Assign Role** dropdown arrow on the right panel.

![Add_Users_Unlicensed_Assign_Role.png](/cms_trial/assets/98ab71bc-ca62-4cdb-80da-c015c99f4a26.png)

To save your changes, click the blue **Add users** button at the bottom-right of the window. The window is closed and the unassigned user is now displayed in the licensed window.

## Accepting the 7pace Timetracker invitation email

When a new user is assigned a license for 7pace Timetracker for Azure DevOps, they receive an automated invitation email. Users must accept this invitation and agree to the policy to access the product features within Azure DevOps.

This step is easy to miss during onboarding. If a user has the correct Azure DevOps access level and a valid 7pace role but still cannot see or use 7pace, confirm that they received and accepted the invitation email.

## What you can do in 7pace

### How to add multiple users in ADO or Active Directory Groups

It is possible to add multiple users that belong to the same Active Directory group or Azure DevOps group.

1. On the **Organization Settings** > **Extensions** > **7pace Timetracker** > **Permissions** page, click the **Add Users** button.

2. Type the name of the user group. Once selected, you can see the list of all current users that belong to this group.

3. Select specific users or use the **Select all Unlicensed Users** option.

4. Assign roles to the selected users that belong to the group at that point in time.

Each license is assigned to an individual user and not to a group. As DevOps does not have webhooks on user group changes, it is not possible to dynamically un-assign licenses from users who are removed from the group or to assign new licenses to new members.

If you need to automate the process of license allocation within a certain group, we suggest using a Windows Scheduled Task that monitors the group’s user list, and then, assign or unassign roles with a POST function to call the [/api/rest/users/roles](https://timehub.7pace.com/api_reference/index.html?urls.primaryName=7pace%20Timetracker%20API%20documentation%20v3.2#/REST%20CRUD/Rest_users_roles_post:~:text=Timetracker%20licensed%20users-,Set%20roles%20/%20permissions%20for%20the%20list%20of%20Timetracker%20licensed%20users,-Parameters) endpoint of TimeTracker’s [REST CRUD API](https://appfire.atlassian.net/wiki/x/o4C3Sg).

### How to set the default role in 7pace Timetracker

As a project collection administrator, you can select the **Default** role that is automatically assigned to new users of 7pace Timetracker.

From the **Default Role** dropdown, select the role that best suits the desired permission level for your **Default** role.

![Set_Default_Role.png](/cms_trial/assets/b8767df2-7545-4af8-b942-be33edea708a.png)

Page refreshes and a *Role was successfully changed* message displays at the top of the page.

All users assigned to the **Default** role, now or in the future, instantaneously inherit these new permissions.

## Subscription Management settings

For a quick reference on plan tiers, pricing, and trial rules, see [7pace Timetracker Subscription Plans and Trial Information](/cms_trial/space/7TFA/3639738655/7pace+Timetracker+Subscription+Plans+and+Trial+Information/).

### Change your 7pace Timetracker subscription plan type

1. To change your current 7pace Timetracker subscription, navigate to *Settings* in **7pace Timetracker** > **Subscription** (users do not have access to the *Subscription* page of 7pace Timetracker). The plan selection page displays. Depending on the number of users selected in the **Users Assignable** dropdown, the plans applicable to the number of users displays. In the example, because you have less than 20 assignable users selected, the Ultimate plan is not available as a selection. Because you have more than three assignable users selected, the Free plan is also not available.

![Change_Subscription_Plan.png](/cms_trial/assets/3d9efe26-ff53-47ff-a3ca-cb9b2de2df33.png)

1. Click the blue **Upgrade** button under **Team**. The order details page displays. Because you already had an existing Start annual plan, the difference in price between the two plans is computed and shown in the **Billed immediately** field. Because the Team plan is an upgrade from the Start plan, the cost of the original plan is deducted from what you are about to pay for your original plan. Likewise, if you decide to downgrade your plan, any overage remains as a credit on your account to be applied to your next invoice.
2. Click **Buy Now**. The *Activation Information* page displays the updated plan and relevant information.

### How to change from annual to monthly billing

1. To change your current 7pace Timetracker subscription from annual billing to monthly or vice versa, navigate to *Settings* in **7pace Timetracker** > **Subscription**.

1. Click the blue *Change* link under *Billing*. The *Your Order* page displays, defaulting to the opposite selection that you currently have. In the example above, the original subscription was an annual one, so when the order page displays, *Monthly* is the default.
2. Click **Change**. Under *Billing*, your subscription plan information now displays as **Monthly**.

### Add users on your 7pace Timetracker subscription

1. To change the number of users on your 7pace Timetracker subscription, navigate to *Settings* in **7pace Timetracker** > **Subscription**.
2. In the *Users* section, click **Change**.
3. In the *Users Assignable* section, use the up and down arrows to change the number of users to the new amount. The plan dollar amount changes to reflect the new number of users.

![Users_Assignable.png](/cms_trial/assets/e1ffac90-93a4-466a-bace-2f00c413c698.png)

1. Click the blue **Continue** button on the applicable plan. The *Your Order* page displays, showing final dollar amounts.
2. Click **Buy Now** to finalize the change.

To decrease the number of users on your subscription to less than the number of users you currently have assigned to 7pace Timetracker, navigate to **Settings** > **User Management** (**Organization Settings** > **Extensions** > **7pace Timetracker** > **Permissions**). Change the user roles of the appropriate number of users to **None**.

![Choose_Number_of_Users.png](/cms_trial/assets/8a2850db-e90f-4a86-af2b-3bf1b39203b1.png)

### Change the billing address of your subscription

1. To change your 7pace Timetracker billing address, navigate to *Settings* in **7pace Timetracker** > **Subscription** (users do not have access to the *Subscription* page of 7pace Timetracker):

![Change_Subscription_Bill_Address.png](/cms_trial/assets/e981abd2-9997-40d8-8e92-1710b332ed7d.png)

2. At the top of the page, click *Billing*.

![Manage_Billing_Address_Window.png](/cms_trial/assets/35dd7dbb-9906-4f31-8375-b6fafe0f7763.png)

3. In the *Billing Address* section, click **Manage Billing Address**.

1. A popup window displays, allowing you to edit your billing address.

![Edit_Bill_Address.png](/cms_trial/assets/d09bf6b3-26e1-4ca5-99d2-e6915d6b9ea8.png)

Make desired changes and then click the **Update** button.

### Change the payment details on your subscription

1. To change your 7pace Timetracker payment details, navigate to *Settings* in **7pace Timetracker** > **Subscription** (users do not have access to the *Subscription* page of 7pace Timetracker):

![Change_Payment_Details.png](/cms_trial/assets/7cadf3f5-2c84-4936-a8e9-1db680f3b674.png)

2. At the top of the page, click *Billing*.

![Adjust_Payment_Details.png](/cms_trial/assets/1d933bef-21ed-456b-a9be-5b62e16307cc.png)

3. In the *Payment Details* section, select **Adjust Payment Details**.

![Add_Payment_Details_New.png](/cms_trial/assets/a82ba855-54fc-4d37-a4f2-597ea46ce464.png)

4. Type in your payment details in the required fields and click **Add**.

### Change the contact information on your subscription

1. To change your 7pace Timetracker contact information, navigate to *Settings* in **7pace Timetracker** > **Subscription** (users do not have access to the Subscription page of 7pace Timetracker):

![Change_Contact_Information.png](/cms_trial/assets/e41683e7-18c8-4572-a3e4-631187afcc5d.png)

2. At the top of the page, click *Billing*.

![Manage_Contact.png](/cms_trial/assets/7361466d-15cc-4012-93c5-f0a01a863052.png)

3. In the *Contact Info* section, select **Manage Contact**.

![Update_Contact_Details.png](/cms_trial/assets/a8181962-e914-4073-801d-7313f0072108.png)

4. In the resulting popup window, make any necessary changes and click **Update**.

### How to find 7pace Timetracker invoices or credit notes

1. To view 7pace Timetracker invoices, navigate to *Settings* in **7pace Timetracker** > **Subscription** (users do not have access to the *Subscription* page of 7pace Timetracker):

![Find_Invoices.png](/cms_trial/assets/506e18a7-1f7b-411a-8b67-d4e5ef8a4f7f.png)

2. Click *Invoices*.

![Invoices_Tab.png](/cms_trial/assets/a9a836eb-b478-44f9-bd0b-deb464b76424.png)

All invoices and credit notes display. You can click each invoice or credit note to download and/or print.

### How to Apply 7pace Timetracker's free subscription plan

To apply the Free plan (maximum of three users), if you are not currently on a trial of 7pace Timetracker, you must first cancel your current subscription. In addition, our Free plan is only available for 7pace Timetracker cloud, not the on-premise version. 7pace Timetracker Free is limited to three users and 500 visible worklogs per account with community support

1. To cancel your current 7pace Timetracker subscription to switch to the Free plan, navigate to *Settings* in **7pace Timetracker** > **Subscription** or from *Azure DevOps Organization settings*/*(Extensions) 7pace Timetracker*/*Permissions*). Please note that you must be a project collection administrator to have access to the *Subscription* page of 7pace Timetracker.

![Subscription_Free.png](/cms_trial/assets/9a1d6cad-a099-4e56-a745-8d6b8597d5fe.png)

The *Activation Information* page displays. You can see that 13 users are currently assigned a license in the above example.

2. Click the blue *Cancel Subscription* link.

![Cancel_Subscription_Link.png](/cms_trial/assets/32050af5-c297-4b3f-ba7a-fb6f93250e5b.png)

The cancel subscription confirmation popup window displays with **Cancel Immediately** (selected by default).

3. Click the **Confirm Cancellation** button.

![Confirm_Cancellation.png](/cms_trial/assets/cd2566df-a92e-4c11-b0ad-ba18b91e5876.png)

Page refreshes, and **Current Plan** displays as **Cancelled**.

4. Click the blue **Buy Now** button.

![Buy_Now_Button.png](/cms_trial/assets/5c0b326b-39d1-446c-8a25-dce99eb68284.png)

The plan selection page displays, and because in this example there are more than three users assigned to 7pace Timetracker, the Free plan is grayed out and unavailable as a selection.

5. Close out the window and click *Permissions*.

![Permissions_Tab.png](/cms_trial/assets/d93d3f47-4cfc-4379-af02-2a31f514c1a1.png)

The organization users who are licensed and unlicensed to 7pace Timetracker are displayed.

6. Click a user's or multiple users' name(s).

![Permissions_Administrator_Users.png](/cms_trial/assets/287448f3-0d3a-4940-ad8f-ccf3fe7249e4.png)

The various user roles are displayed on the right side of the screen.

7. Select **None** as the user role for however number of users is required to bring the count down to three or less. A confirmation popup message displays.

8. Accept the user message so that only three users or fewer are licensed to use 7pace Timetracker.

9. Click **Subscription** again.

![Free_Plan_Available.png](/cms_trial/assets/91514d2e-c56c-4617-b013-945e28043d92.png)

The Free plan option now displays as available.

10. Click **Switch** to change to the Free plan. The Free plan is applied and active.