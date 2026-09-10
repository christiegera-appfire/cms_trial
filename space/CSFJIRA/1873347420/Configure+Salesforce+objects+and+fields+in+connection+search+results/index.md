# Configure Salesforce objects and fields in connection search results

This guide will help you configure Connection search results by setting up what **Salesforce Objects** are defined in the search as well as what **Salesforce Fields** are searchable. Only Salesforce object types and fields explicitly added here are available for entity and field mapping, enabling associations between Jira work items and Salesforce records. The objects and fields you configure will be visible to end users in Jira.

## Add Salesforce object types to the search results

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.
3. Under *Connector for Salesforce*, click **Connections**.
4. At the *Salesforce Connections*screen, click **Configure** next to the connection you want to set up.

   ![Configure Connection](/cms_trial/assets/c17e4e28-7674-4e09-8351-357cefa37d20.png)
5. Click **+Add Salesforce Object**.

   ![Add Salesforce object.png](/cms_trial/assets/7c3c2163-4fd4-4854-9fca-732aa30c8e0e.png)
6. At the *Add Salesforce Object* window, select a Salesforce object type you want to make available in Jira.

   ![contentId-1873347420](/cms_trial/assets/95e72ad3-a6a8-48d2-9af7-6d5c2912bba9.png)
7. Click **Next**.
8. Select the **Salesforce Field** you want to add and click **Add.**   
   Repeat for each field you want to include.

   ![Salesforce Field](/cms_trial/assets/b924da53-6e3f-4789-84be-d3f50b8e5da6.png)

Fields added here will appear to end users in record views and mapping screens.

1. Click **Next.**  
   The *Connection Configuration* page opens with the list of Salesforce objects.
2. To save your configuration, click **Apply Changes**.

   ![Apply changes.png](/cms_trial/assets/e74f4038-1b58-4383-b0e1-38d3d17f71a2.png)

   The Salesforce object types you just added now appear as a [searchable Salesforce Object in the Associate Object window](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/).

## Add a Salesforce field to an existing object

1. At the Salesforce *Connections* screen, click **Configure** next to the connection you want to modify.

   ![Connections.png](/cms_trial/assets/6b6b4c01-67ec-427e-a2f5-762e6d904641.png)
2. At the*Connection Configuration* screen, click **Fields** next to the Salesforce object you want to configure.

   ![fields.png](/cms_trial/assets/f1586f40-49ab-44b8-a5ac-3969ad8793f4.png)
3. Select the Salesforce field you want to add from the **Salesforce Field** dropdown and click **Add**.

   ![Salesforce Fields](/cms_trial/assets/3ec76868-0cb4-49ad-a000-0bde579faba4.png)
4. Click **Next**.
5. When the new **Salesforce Field** is added, click **Apply Changes**.

   ![Apply changes.png](/cms_trial/assets/e74f4038-1b58-4383-b0e1-38d3d17f71a2.png)

## Render Object primary field instead of Object ID

We recommend configuring object details to display instead of object IDs in the Association details window in Jira. This makes Salesforce records easier to identify for end users — for example, showing the User object's Full Name field instead of an unreadable User object ID.

1. Add the Created By field to the Case object.

   ![Case object fields](/cms_trial/assets/de95e7c3-ed74-4f6a-95b1-d0929f02c83e.png)

   The Created By field is displayed as an ID in the *Association details* view:

   ![Association details view](/cms_trial/assets/dd2207ce-b164-480a-a1d6-e63369b7250d.png)
2. Add the User Salesforce object and add the Full Name Salesforce Field as a primary field to replace the ID with meaningful data.

   ![User Salesforce object ](/cms_trial/assets/f8870fc8-330e-4ee7-9cbe-856377b11c6b.png)

   The Connector uses this configuration to automatically translate the object ID into the full name.

   ![Created by displayed as the full name](/cms_trial/assets/22501ad1-441d-4542-aa21-bef9e5ef72b9.png)

The primary field is automatically chosen to replace the object ID.

## Next steps

- [Bind a space to a connection](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=Bind%20a%20Project%20to%20a%20Connection%20%28Jira%20Cloud%29&linkCreation=true&fromPageId=1873347420)