# Mapping Account Name to a Jira Custom Field

## Purpose

If we map the Salesforce Account Field to a Jira Custom Field, it will be shown as the Account ID rather than its name like in the Salesforce. This behavior is expected due to the value inside the field being the ID rather than the name. An example is below:

![contentId-3091891814](/cms_trial/assets/43c74543-a448-4bd7-b395-e599241a3b75.png?version=1&modificationDate=1678861994297&cacheVersion=1&api=v2)

This article is to help the custom field showing the name of the Account rather than its ID, like the example shown below:

![contentId-3091891814](/cms_trial/assets/260dd7e4-c1c7-4370-865b-517524a30206.png?version=1&modificationDate=1678861994598&cacheVersion=1&api=v2)

## Answer

Rather than directly link the custom field to the Account, we can use the Salesforce Formula Field to get the Account Name first, then link it to the custom field.

The steps for the configuration are:

1. Navigate to **Salesforce Setup** > **Object Manager**.
2. Search for the linked Salesforce object and click to get its setup details.
3. Move to **Fields & Relationships** and click **New**.
4. Select **Formula** and click **Next**.
5. Label the field as you want and select **Text** as the **Formula Return Type**.

   ![contentId-3091891814](/cms_trial/assets/caf71e0d-8098-434a-9204-f4c744e54e9c.png?version=1&modificationDate=1678861994796&cacheVersion=1&api=v2)
6. Insert "Account.Name" to the formula.

   ![image-20241213-141321.png](/cms_trial/assets/8426f050-549c-4f9d-9014-3499ace5f470.png)
7. Finish the field creation.

Check the Salesforce Record that the field able to get the Account Name then do a test pull from Jira to confirm that the Jira custom field is now showing the Account Name.