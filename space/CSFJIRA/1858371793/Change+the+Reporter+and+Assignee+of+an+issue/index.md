# Change the Reporter and Assignee of an issue

This page helps you configure the mappings to allow Connector for Salesforce to assign a different user to a created issue.

## Guide

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/6c8c76eb-a432-48c5-85b4-764de4561b15.png)
3. Select your **Binding**, then click **Menu** (▢) > **Edit**.

   ![image-20260915-093429.png](/cms_trial/assets/e9c3e8fe-c53d-4875-84ca-c2371051690f.png)
4. On the *Entity mapping* screen, select the mappingyou want to configure.  
   For this example, let's select **Task** -> **Case** mapping.

   ![Entity mapping](/cms_trial/assets/270a06f1-5475-4dd9-b48e-89a1652f68e2.png)

The **Task → Case Field mappings** window opens on the right.

1. In the **Jira Field**, select **Reporter**, and in the **Salesforce Field**, select **Owner ID.**
2. Click**Add field mapping**.

   ![Field mapping](/cms_trial/assets/dd3104bc-5846-4c4c-b997-87c1e308fea4.png)
3. Next to the new field mapping**,** click **Menu** (▢) > **Configure**.

   ![Configure option](/cms_trial/assets/0f1cba88-7ea7-4b7d-9825-d34dec4c4066.png)
4. Select a **Jira** **default** and **Salesforce default** value for unmapped reporters and assignees.   
   For detailed instructions, see [Set default value](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).
5. Under the **Reporter** field, add the *username* of the account you want to add.

   ![image-20260915-103116.png](/cms_trial/assets/44b9d38f-1c4f-4071-aeda-7d3070ee70fd.png)
6. For the **Salesforce Fields Value**, you are required to obtain an 18-character Owner ID.  
   To get this, write down your 15-character User ID from your Salesforce profile URL:

   ![contentId-1858371793](/cms_trial/assets/9acee589-b586-40fb-a519-7f20058925c1.png)
7. Use [this tool to make the conversion](https://www.adminbooster.com/tool/15to18) of the User ID.

   ![contentId-1858371793](/cms_trial/assets/5c05c909-1492-4150-889e-6287bd300bd2.png)
8. Copy the converted ID, paste it under the **Owner ID** column, click **+ Add**, then click **Configure**.

Make sure you paste or key in the Salesforce ID exactly as generated, with the correct case (this ID is case-sensitive). and with no spaces before or after the value. For example, `00590002fBnyAAE` is not the same as `00590002fbnyaae`.

![image-20260915-103319.png](/cms_trial/assets/b52c42fb-3644-4bd0-a634-4ea2a35137c3.png)

1. In Salesforce, create a new case assigned to the designated owner, where the **Owner** in Salesforce is using the admin username that has already been mapped in Jira.
2. [Create a Jira Issue from Salesforce](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/).

   ![contentId-1858371793](/cms_trial/assets/0783512f-0859-4a1e-95b1-5f6d0c8619b6.png)
3. Back in Jira, you should now be able to see the admin user instead of "*Salesforce & Jira Cloud Connector*" as the **Reporter**.

   ![contentId-1858371793](/cms_trial/assets/8b8a2a84-ccf1-4ec7-99bc-f32c7f929c74.png)
4. Go to Salesforce and change the *Case Owner* to change the case's owner to ensure the add-on can synchronize with the **Reporter** field.
5. Go back to Jira and **Pull** the updated changes made in Salesforce.  
   You should now be able to see the new changes.  
   The user must be manually mapped as well.