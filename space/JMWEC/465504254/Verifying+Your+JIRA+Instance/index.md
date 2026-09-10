# Verifying Your JIRA Instance

After successful installation, you need to verify and potentially adjust your Jira instance configuration to avoid errors during the execution of JMWE post-functions. Most of the configuration required to run the JMWE add-on is done automatically, but if you have customized Jira security settings such as [**Permission Schemes**](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/) or [**Issue Security**](https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-security-schemes/) schemes, you might have to make some additional manual changes.

### Identifying configuration issues

If you have already configured JMWE post-functions in your workflows and they do not seem to be working appropriately, go to the [Troubleshooting and Support](/cms_trial/space/JMWEC/465241931/Troubleshooting+and+Support/) page under*JIRA MISC WORKFLOW EXTENSIONS*, wait a few moments, and check whether an error box appears mentioning Security Errors.

### Create at least one JIRA Project

In order for the JMWE add-on to work properly, you need to have created *at least one* Jira Project. If you haven't, most configuration pages will not work, and you will see security errors in your logs.

## 1. Check Global permissions

Verify that the `atlassian-addons-admin` group has the **Jira Administrators** permission.

**Steps:**

1. Log in to your Jira instance as an administrator.
2. Click the **Settings** ⚙️ icon in the upper right corner of the window and select **System**.
3. Click **Global permissions**in the left-hand panel.
4. Check whether the `atlassian-addons-admin` group belongs to the **Jira Administrators** and **Browse users and groups**permissions (pictured, below).

   ![JMWE for Jira Cloud instance verification interface showing validation status](/cms_trial/assets/402f4869-098d-436f-b5ff-b75e82a5e698.png)
5. If either of these checks fails, your Jira instance is not properly configured. [Uninstall](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/317751444) and then [reinstall JMWE](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Installing%20or%20Re-installing%20on%20Jira%20Cloud&linkCreation=true&fromPageId=465504254) and check again. If the checks still fail, contact [Atlassian Support](https://support.atlassian.com/contact) and provide details on these issues.

[Unmapped macro: legacy-content — no content to fall back on]

## 2. Check your Permission schemes

For each permission scheme, make sure all permissions are granted to the `atlassian-addons-project-access` project role in the *Permission Scheme* of the project.

**Steps:**

1. Log in to your Jira instance as an administrator.
2. Click the **Settings** ⚙️ icon in the upper right corner of the window and select **Issues**.
3. Click **Permission schemes**in the left-hand panel.
4. Click on the first *Permission Scheme*
5. Verify that the `atlassian-addons-project-access` project role is granted all permissions. If not, grant the missing permissions to that project role.
6. Repeat with all other *Permission Schemes.*

## 3. Check your Issue Security schemes

For each Issue Security scheme, make sure that the `atlassian-addons-project-access` project role belongs to **every** Security Level.

**Steps:**

1. Log in to your Jira instance as an administrator.
2. Click the **Settings** ⚙️ icon in the upper right corner of the window and select **Issues**.
3. Click **Issue security schemes**in the left-hand panel.
4. Click on the first *Issue Security Scheme.*
5. Verify that the `atlassian-addons-project-access` project role belongs to each *Security Level*.

   1. If not, use the *Add* link to add the `atlassian-addons-project-access` project role to each security level.
6. Repeat with all other *Issue Security Schemes.*

## 4. If you are using jira.permission.\* workflow step properties

You need to add the `atlassian-addons-project-access` project role to the `jira.permission.*` property value

**Steps:**

1. Log in to your Jira instance as an administrator.
2. Click the **Settings** ⚙️ icon in the upper right corner of the window and select **Issues**.
3. Click **Workflows**in the left-hand panel.
4. For the workflow which has the transition you wish to edit, click the action button [menu button icon] and select **Edit**.
5. Click **View Properties** for the workflow step.
6. If you have a property set up, add another property with the `atlassian-addons-project-access` project role.

   For example, if you have,

- `jira.permission.comment.group=some-group,` add a new property`jira.permission.comment.projectrole=xxxxx`
- `jira.permission.comment.group=some-group` and `jira.permission.comment.user=some-user,` add a third property: `jira.permission.comment.projectrole=xxxxx`
- `jira.permission.comment.user.1=user-a` and `jira.permission.comment.user.2=user-b` add a new property `jira.permission.comment.projectrole=10000`
- `jira.permission.comment.projectrole=10001` add a new property `jira.permission.comment.projectrole.2=10000`

where `xxxxx` is the ID (hover on the actions for the project role in the **Project role browser** page for the ID) of the `atlassian-addons-project-access` project role.

See [**here**](http://www.j-tricks.com/tutorials/permissions-based-on-workflow-status) for the list of `jira.permissions.*` properties.