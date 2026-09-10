# "Create Salesforce Object" and "Associate" buttons are not visible in Jira

## Summary

The buttons to create and associate a Salesforce Object are not visible in the **Associations** section of the Jira issue. 

![contentId-2257911925](/cms_trial/assets/9a98c1dc-e181-4495-89ca-0ac63fa73ff7.png)

## Diagnostics Steps

- Not applicable.

## Cause

The user does not have **Edit Issue** permissions in the project.

## Workaround

- Not applicable.

## Resolution

1. Go to the affected project.
2. Go to **Project Settings** > **Permissions**.
3. Next, click **Actions** > **Edit permissions**.
4. Scroll to **Edit Issues** permission and click **Update**.
5. Select **Project Role** and select the suitable option to add the users or groups.
6. With the proper permission granted, the user can view the buttons.