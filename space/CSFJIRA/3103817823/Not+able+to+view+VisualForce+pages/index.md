# Not able to view VisualForce pages

## Summary

When trying to view a VisualForce page, an *Insufficient Privileges* error is shown, so the user can't see the related Jira Issues and can't create or associate issues.

![contentId-3103817823](/cms_trial/assets/3afe3b05-c221-491f-9165-f40fb62aac61.png)

## Environment

- Jira Cloud
- Salesforce

## Cause

This is usually because the current user has not been granted access.

## Resolution

In order to grant this access:

1. In Salesforce, go to the **Setup** > **Custom Code** > **VisualForce Pages**.

   ![VisualForce Pages](/cms_trial/assets/137f2710-8ee1-4881-a505-059e211db2ca.png)
2. Click the **Security** link, and you will be sent to the Page Level Security Page.
3. Select the Current User Profile from the Left side and click the **Add** button and click **Save**.

   ![Current User Profile](/cms_trial/assets/f8e7c738-46b4-4f66-9dcf-9cd93d9158ed.png)

Now you have given Page Level Security to the Profile Added.