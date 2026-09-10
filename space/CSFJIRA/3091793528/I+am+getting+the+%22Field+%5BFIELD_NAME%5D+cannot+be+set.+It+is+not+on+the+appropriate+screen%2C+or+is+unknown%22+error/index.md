# I am getting the "Field [FIELD_NAME] cannot be set. It is not on the appropriate screen, or is unknown" error

## Summary

When trying to create an issue the user is getting an error that a field is not on the appropriate screen or is unknown.

## Environment

- Jira DC and Jira Cloud

## Diagnostics Steps

Not applicable.

## Cause

This issue is caused by not having the specified field in the **Default Create Screen**.

## Workaround

Not applicable.

## Resolution

If the issue involves a **Custom Field ID**, we will first need to find the name of the field (if not, you can skip the following steps):

1. Navigate to **Administration > Issues >Custom Fields**.
2. Go to the Cog Icon  (Jira Server) or the ellipsis (Jira Cloud) and hover over the **Configure** or **Screens** option.
3. Observe the URL at the bottom left of the browser window.  You will find the ID at the end of the link.  
   Example:

   ![contentId-3091793528](/cms_trial/assets/1a55f03f-3c64-4c9c-9eff-57e43c1e419f.png)

To add the Field to the corresponding Screen:

1. Open the Project where the issue is happening.
2. Go to **Project Settings**.
3. Click on **Screens**.
4. Click on the name of your screen to expand.  You should see something like the screen below:

   ![contentId-3091793528](/cms_trial/assets/87dafa22-e98d-458f-ae0e-f52702652ddd.png)
5. Click the name of the screen next to **Create issue.**
6. Finally, add the missing field to the list.