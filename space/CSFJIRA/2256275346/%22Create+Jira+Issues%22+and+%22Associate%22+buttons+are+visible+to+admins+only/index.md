# "Create Jira Issues" and "Associate" buttons are visible to admins only

## Summary

Under Salesforce Lightning Experience, the **Create Jira Issues** and **Associate** buttons are only visible to admins.

![contentId-2256275346](/cms_trial/assets/801e14a4-b81a-4bee-a142-77cf17ca839c.png)

## Environment

- Jira Cloud
- Jira DC

## Cause

Cloud

The user's profile doesn't have the **Apex Class** access permission enabled for JCFS classes.

DC

The user's profile doesn't have the **Apex Class** access permission enabled for JSFS classes.

## Resolution

Cloud

1. Identify the users who aren't able to see the **Create Jira Issues** and **Associate** buttons.  
   In Salesforce, go to **Setup > Users > Profiles >** click on the users' profile.
2. Look for and edit **Enabled Apex Class Access**.
3. Make sure all JCFS classes have been added to the **Enabled Apex Classes** column.

   ![contentId-2256275346](/cms_trial/assets/ee5565e1-bdad-48f4-9c89-2e13c43c99a4.png)![contentId-2256275346](/cms_trial/assets/737eff63-b558-4612-9c4c-29be39c74f60.png)
DC

1. Identify the users who aren't able to see the **Create Jira Issues** and **Associate** buttons.  
   In Salesforce, go to **Setup > Users > Profiles >** click on the users' profile.
2. Look for and edit **Enabled Apex Class Access**.
3. Make sure all JSFS classes have been added to the **Enabled Apex Classes** column.

   ![contentId-2256275346](/cms_trial/assets/bd770262-d671-4a7c-96dc-0fda753c35f8.png)![contentId-2256275346](/cms_trial/assets/7409f2c1-6d71-48de-9bc2-77217a88e9a3.png)