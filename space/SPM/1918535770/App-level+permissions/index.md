# App-level permissions

App-level (or global) permissions determine access to the app and its pages, and the scope of actions users can perform within the app.

**Temporary access issue for OKR and Priorities**

Currently, Jira Administrators may not automatically have access to the OKR and Priorities modules in BigPicture.

Until this issue is fixed, Jira Administrators must be granted access to these modules directly in BigPicture. To provide access, assign either:

- App Admin role, or
- App OKR Admin and App Priorities Admin roles.

A fix is planned for late August or early September 2026.

## Navigation and access

Only Jira and App Admins can access global security settings.

1. Click the **App settings** button.
2. Select **Administration** > **Security** from the dropdown.

![Screenshot of the Security tab under Administration.](/cms_trial/assets/b973d91d-bf6c-4d98-be4c-af1adb31ef3c.png)

You are now on the **Administration** > **Security** page.

![Screenshot of the Security page in the BigPicture Administration.](/cms_trial/assets/319b8633-4ffc-4931-a0fe-92ecb836ada3.png)

## App Security (page)

### Every user is the App Admin (toggle)

This toggle switch changes permissions in BigPicture only. It doesn't affect user permissions in Jira.

![Screenshot of the Every user is the App Admin toggle switch.](/cms_trial/assets/48ea85c5-f82c-419d-b8c7-268cefc41ac3.png)

#### Toggle switched ON

When enabled, every logged-in Jira user has the same administrative level of access, which includes:

- App Administration
- Boxes and their content (depending on Jira permissions and security settings).

When the **Every user is the App Admin** toggle is on, you can't assign global roles to individual users or Jira groups because all users have full access to manage the app and boxes.

Likewise, this toggle disables [box-level security settings](/cms_trial/space/SPM/1918797447/Box-level+permissions/) (security roles for [box types](/cms_trial/space/SPM/1918830000/Box+types/) are not affected).

| **App** ***Security*** **page** | **Box** ***Security*** **page** |
| --- | --- |
| Screenshot of the settings when the Every user is the App Admin toggle is enabled. | Box security page. The box-level security roles cannot be assigned due to the permissions for everyone option being active. |

The **Every user is the App Admin** option is useful for small teams or when you're testing the app. It helps you quickly see how things work. But in a live environment, you may need more advanced access controls to keep things secure.

The **Every user is the App Admin** option doesn't override Jira permission settings. If a user is not permitted to access a project in Jira, this option won't allow them to view it in BigPicture, either.

If you want your users to view and manage all boxes in BigPicture, ensure you have granted them the relevant permissions in Jira.

#### Toggle switched OFF

When the **Every user is the App Admin** option is disabled, Jira/App Admins can manage global role permissions on the **Administration** > **Security** page. The security settings on the **box configuration** > **Security** page are also enabled.

### Role permissions

The following security roles are available in BigPicture:

| **Role name** | **Description** |
| --- | --- |
| App Admin | Owns the entire application configuration and governance. Can access and manage any box. Grants full control over all settings, modules, and boxes, including permissions, structure, and data access. |
| App Financial Admin | Controls financial planning and management. Provides full access to create, edit, and manage financial data in the boxes they have access to.  The App Financial Viewer and App Financial Admin are [Financials module-specific roles](/cms_trial/space/SPM/1918765525/Financials+module+permissions/). |
| App Financial Viewer | Provides read-only access to financial data. Allows visibility into budgets and financial metrics without the ability to modify them in the boxes they have access to.  The App Financial Viewer and App Financial Admin are [Financials module-specific roles](/cms_trial/space/SPM/1918765525/Financials+module+permissions/). |
| App OKR Admin | Manages strategic objectives and key results. Allows creation, editing, and maintenance of OKRs across the organization. |
| App OKR User | Can view and edit Objectives and Key Results based on the permission settings of the OKR module. |
| App Priorities Admin | Manages prioritization frameworks and data. Allows configuration and maintenance of priorities used for planning and decision-making. |
| App Resource Admin | Manages organizational resources. Allows configuration of resources used across planning and execution. |
| App User | Has basic access to the App, which is dependent on the individual permissions given at box levels. |

#### App Admin

App Admins have full access to the *App Configuration,* *App Administration*, and every box and gadget. They can create new boxes and view and configure every existing box in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/).

- Jira Admins automatically get the App Admin role, but they do not show up in the App **Administration** > **Security** tab by default.
- Only Jira Admins and App Admins can give the App Admin role to others.
- Once a user is granted the App Admin role, they can set up the app and add other users to the App Admin role, even if they aren't Jira Admins.

When a Jira Admin grants someone the App Admin role, that user can manage the app and all boxes. Their name will appear under the App Admin role (**Administration** > **Security**) but not on the **box configuration** > **Security** pages.

| **App** ***Security*** **page** | **Box** ***Security*** **page** |
| --- | --- |
| App security page. | Box security page. |

#### App User

The App User is the basic global role that allows Jira users to:

- See BigPicture under **Apps** in Jira
- Open BigPicture

Access to the app alone does not automatically grant access to individual boxes (even if the App User is permitted to view and/or manage a respective Jira project).

Important For that reason, to ensure users can benefit from using BigPicture, they must be granted:

- App User role in BigPicture
- project permissions in Jira
- a box-level security role to view/manage respective boxes
- BigPicture gadgets

Below, you can see how these permissions affect one another:

A Jira user was not assigned the App User role. As a result, they:

- Can't see BigPicture under Jira’s **Apps**

![A spalsh screen informing about insufficient permission to access BigPicture.](/cms_trial/assets/68910587-a4f2-42a9-bd7e-6ba43aeaea09.png)

A Jira user was assigned the App User role, but not a box-level security role to any of the boxes. As a result, they:

- Can see BigPicture under Jira’s **Apps**
- Can open BigPicture
- Can't access any box data in BigPicture

![A spalsh screen informing about insufficient permission to see box data BigPicture.](/cms_trial/assets/7f83de05-5d91-4c66-8e71-10cc63f7ae6f.png)

#### App Resource Admin

This role grants you access to and management of all resource-related pages within the app’s *Administration* section. The Resource Admin role builds upon the App User role, meaning that users with this role:

- Have basic access to the app but cannot access the *App Configuration.*
- Can access boxes based on individual box security settings (but they do not get access to all boxes like the App Admin).
- Are allowed to administer resource-related global configuration on the resource [Individual's details page](/cms_trial/space/SPM/1918637190/Individual%27s+details+page/) (including all its subpages).
- Can access the Administration page but not the Resources tab.

## Grant and manage global security roles

Global roles can be assigned to individual Jira users and Jira groups.

Jira and App Admins can grant global roles in BigPicture in the following ways:

1. On the *Security* page, find the security role you want to assign.
2. Click **Manage assignments** next to the role.

   ![Screenshot of the Manage assignments button.](/cms_trial/assets/19f84c81-35ad-4a36-9b78-67b6047677ae.png)
3. From the dropdown, under **Users**, select a Jira user or multiple users in one go; if you want to add a Jira group or groups to a specific role, select them from the list under **Groups**.

   ![Screenshot of the Manage assignments window.](/cms_trial/assets/6a545a80-36c5-4082-a0b9-1fe88ad371bc.png)

The roles are assigned, and you don't need to confirm them with any additional buttons.

Alternatively:

1. Click the **+Assign role** button.
2. A dialog appears. Select whether you want to assign a user or a group.

   ![Screenshot of the Assign security role window.](/cms_trial/assets/8561fb6a-4f8f-4486-893f-a055a35abc40.png)

1. Next, select the global role from the list.

You can assign only one person or group at a time. To add more users and groups to the role, check the **Add another** box.

1. Click the **Save** button to finish the process.