# Change the Reporter and Assignee of an issue

This page helps you configure the mappings to allow Connector for Salesforce to assign a different user to a created issue.

## Guide

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/6c8c76eb-a432-48c5-85b4-764de4561b15.png)
3. Choose your desired **Bindings**, then click **Mapping**.

   ![binding.png](/cms_trial/assets/ab9ad34e-5e31-4a3f-9616-31e0510617a7.png)

   On the **Mapping Configuration** screen, choose the **Issue Type** you want to configure.   
   For this example, let's choose **Task**.
4. Click **Mappings**.

   ![Mapping bindings.png](/cms_trial/assets/3349fbd7-3525-4247-88c2-4f1fed5f3048.png)
5. The **Task to Case field mappings** dialog box appears.
6. In the **Jira Field**, choose **Reporter**, and in the **Salesforce Field**, choose **Owner ID.**
7. Click**+ Add**.

   ![task to case mapping.png](/cms_trial/assets/3c6703f0-cdd1-4cea-963f-60b12dfd673d.png)
8. Once you've clicked the **+ Add** button, click **Configure**.
9. Select a **Jira** **default** and **Salesforce default** value for unmapped reporters and assignees.   
   For detailed instructions, see [Set default value](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).
10. In **Reporter** field, add the *username* of the account you want to add.

    ![Reporter field.png](/cms_trial/assets/49f08271-1bc0-4642-a8ca-93279bdf7565.png)
11. For the **Salesforce Fields Value**, you are required to obtain an 18-character Owner ID.  
    To get this, write down your 15-character User ID from your Salesforce profile URL:

    ![contentId-1858371793](/cms_trial/assets/9acee589-b586-40fb-a519-7f20058925c1.png)
12. Use [this tool to make the conversion](https://www.adminbooster.com/tool/15to18) of the User ID.

    ![contentId-1858371793](/cms_trial/assets/5c05c909-1492-4150-889e-6287bd300bd2.png)
13. Copy the converted ID, paste it under the **Owner ID** column, click **+ Add**, then click **Save**.

Make sure you paste or key in the Salesforce ID exactly as generated, with the correct case (this ID is case-sensitive). and with no spaces before or after the value. For example, `00590002fBnyAAE` is not the same as `00590002fbnyaae`.

![contentId-1858371793](/cms_trial/assets/4366edf3-90e2-4abd-82ca-32318ab17787.png)![contentId-1858371793](/cms_trial/assets/c10402d6-3918-4561-8074-9800ebbe0818.png)

1. In Salesforce, create a new case assigned to the designated owner, where the **Owner** in Salesforce is using the admin username that has already been mapped in Jira.
2. [Create a Jira Issue from Salesforce](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/).

   ![contentId-1858371793](/cms_trial/assets/0783512f-0859-4a1e-95b1-5f6d0c8619b6.png)
3. Back in Jira, you should now be able to see the admin user instead of "*Salesforce & Jira Cloud Connector*" as the **Reporter**.

   ![contentId-1858371793](/cms_trial/assets/8b8a2a84-ccf1-4ec7-99bc-f32c7f929c74.png)
4. Go to Salesforce and change the *Case Owner* to change the case's owner to ensure the add-on can synchronize with the **Reporter** field.
5. Go back to Jira and **Pull** the updated changes made in Salesforce.  
   You should now be able to see the new changes.  
   The user must be manually mapped as well.