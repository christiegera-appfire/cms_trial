# "Insufficient access: insufficient access rights on object id:[0031a...]"

## Purpose

When trying to sync the Salesforce record, an error is thrown "insufficient access right to object ID [..]"

![image-20250218-072220.png](/cms_trial/assets/eb466cc0-0c48-4630-aee4-451d8c4c2b5e.png)

## Answer

This error is usually related to the integration user not having enough access to the object as mentioned in this [Salesforce knowledge base](https://help.salesforce.com/s/articleView?id=000383442&type=1).

In Salesforce, it is recommended to make sure that the integration user is allowed to "modify all" objects.

1. Go to **Setup** > **Administer**  > **Jira Cloud/Server for Salesforce** >  **User Count** (click on the number).
2. Click on the profile and find **Standard Object Permissions** or **Custom Object Permission** depending on the object that's causing the issue.
3. If you are unable to search for the profile from Step 2, use this [Salesforce guide](https://www.salesforcetutorial.com/object-permissions/) alternatively.
4. Click **Edit** and grant **Modify All** permission to the profile.

   ![image-20250218-072231.png](/cms_trial/assets/f2f702d4-a1d2-42c4-9e8b-3b4584b4b67c.png)