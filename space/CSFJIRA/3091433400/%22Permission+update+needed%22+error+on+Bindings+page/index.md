# "Permission update needed" error on Bindings page

## Summary

When configuring or adding entity mappings in the **Bindings** page, the user gets the "Permission update needed" error message.

![image-20250826-141717.png](/cms_trial/assets/2592f2e9-bc9a-4de5-909c-23ff0cdd0f58.png)

## Environment

- Jira Cloud
- Jira DC

## Cause

The user making the changes has insufficient permission on a project level.

## Resolution

1. Locate the project you want to configure the bindings for.
2. Go to **Project Settings** > **Access** > **Project permissions**.
3. Next, click **Actions** > **Edit permissions**.
4. Make sure the user who is configuring the mapping has the following permissions:

   - Administration Permissions

     - Administer Projects
   - Project Permissions

     - Browse Projects
   - Issue Permissions

     - Create Issues
     - Edit Issues
     - View Issue
   - For Jira Cloud, ensure that the *atlassian-addons-project-access* roleis granted with all the permissions.