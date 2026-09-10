# How can I verify if the high number of API calls originate from the SFJC connector?

## Purpose

The API calls number has gone up significantly and you want to verify if the API calls are related to the Salesforce JIRA connector application.

## Answer

1. In Salesforce, check who is the integration user that the connector is using to access Salesforce from Jira.
2. Go to **Setup** > **Connected Apps OAuth Usage** > **User Count** and click on the number.

   ![Connector for Salesforce & Jira Connected Apps OAuth Usage page with User Count column](/cms_trial/assets/231cd0e7-38dc-4686-94a0-daad339357be.png?version=1&modificationDate=1678784457130&cacheVersion=1&api=v2)
3. This will take you to the **Connected Apps User's Usage** page and show you the user.
4. Perform the following report on **Salesforce Classic** to list all the users with the total number of API calls:

   ```text
   <Salesforce-URL>/00O?rt=104&retURL=%2F00O&c=UN&c=FULL_NAME&c=EM&c=CID&c=TS&c=CC&duel0=FULL_NAME%2CUN%2CEM&scope=organization&details=yes
   ```
5. If a dedicated Salesforce user is used as an integration user, you can verify by observing the **call count** in the report.

   ![Connector for Salesforce & Jira Salesforce Classic API usage report showing user call counts](/cms_trial/assets/62d4c1ba-481b-44e2-8855-62d2c208f366.png?version=1&modificationDate=1678784457203&cacheVersion=1&api=v2)

\_\_confluenceADFMigrationUnsupportedContentInternalExtension\_\_