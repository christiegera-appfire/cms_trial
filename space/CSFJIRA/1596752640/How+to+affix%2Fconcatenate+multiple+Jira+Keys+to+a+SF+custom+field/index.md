# How to affix/concatenate multiple Jira Keys to a SF custom field

## Purpose

By default, you can send a Jira key to a text field which is overwritten when you have multiple associations.

This guide will explain how to add multiple Jira Keys to a Salesforce rich text field (Multiple Jira keys) using [Salesforce Flow](https://help.salesforce.com/s/articleView?id=sf.flow.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5#:~:text=A%20flow%20is%20an%20application,and%20scheduled%20actions%20from%20processes.).

Known limitations:

- By unlinking or removing an association, the Jira key will not be removed from the multiple Jira key field. This needs to be done manually.
- The Salesforce Flow only works when creating Jira issues from Salesforce. If you create a Salesforce record from Jira, the Salesforce Flow will not trigger.

These type of requests are out of support scope. We have tested this solution in our staging environment and we encourage you to test this solution in a sandbox environment before introducing it to your production environment.

Salesforce Prerequisite:

- Jira key field (text).
- Multiple Jira keys (rich text).
- Case object.
- Salesforce Flow.

## Answer

## Salesforce General Configuration

1. In Salesforce, create a text field named "Jira Key". Set the character length of a 255 characters.
2. Create a rich text field named "Multiple Jira Key". Set the maximum field length of 32000. Set the **Visible Lines** value based on your use case.
3. In Jira, create a mapping for the Key field (Jira) to the Jira Key field (Salesforce).

## Salesforce Flow Configuration

1. Create a [Salesforce Flow](https://help.salesforce.com/s/articleView?id=sf.flow.htm&type=5) rule similar to the image below:

   ![contentId-1596752640](/cms_trial/assets/2a8424ca-183b-46ea-9581-ee2f3211a9d0.png)
2. Next, create an [Update Record](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_data_update.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5#:~:text=Identify%20Salesforce%20records%20to%20update,set%20the%20field%20values%20individually.) similar to the image below:

   ![contentId-1596752640](/cms_trial/assets/0632f158-a7af-44f3-98cb-39badcd86b5a.png)
3. Set the following in the **Configure Trigger** section in the Salesforce Flow configuration:

   1. Trigger the Flow When: A record is created or updated.
4. Next, set the following in the **Set Entry Conditions**section:

   ![contentId-1596752640](/cms_trial/assets/a9f034f8-28c9-4453-9d53-25a7fcfe0811.png)
5. Follow the configuration for the **When to run the Flow for Updated Records** and **Optimize the Flow** **for**:

   ![image-20241213-125021.png](/cms_trial/assets/382c5f75-b545-4f92-b21f-ce40a5d10d5e.png)
6. Set the following conditions:

   - JIRA\_Key\_\_c is Null = False (To get the key when you create a Salesforce record from Jira.)
   - JIRA\_Key\_\_c is changed = True (To halt the rule from running in a loop and to only execute when the Jira key changes.)
7. In the **Edit Formula** section set the following. This will append the Jira Key to the Multiple Jira Key:

   ```text
   {!$Record.Multiple_Jira_Keys__c} &' '& {!$Record.JIRA_Key__c}
   ```

   ![contentId-1596752640](/cms_trial/assets/9fd08bb4-480a-45fd-b14c-5b65f8e23676.png)

## Salesforce Updates Record Configuration

1. Set the following in the **Jira key append** section in the Updates Record configuration:

   1. How to Find Records to Update and Set Their Values: Specify conditions to identify records, and set fields individually.
2. Next, set the following in the **Set Entry Conditions**section:

   ![contentId-1596752640](/cms_trial/assets/0411f77d-3a7b-434d-adc5-ff5e6e54cec0.png)
3. The **Value** field in the image above is an example, change this to the object that you want to configure to.
4. You can debug the setup by going to **Case RecordID** > **Activate** > **Save**. The Multiple Jira Keys field will have this format, ex: "CSF-347 CSF-348 CSF-300".
5. Once the configuration is complete, Jira key field changes with a new value (from a new Jira issue created from Salesforce or any new associations). The multiple Jira key will take that new value from the Jira key field.

   ![contentId-1596752640](/cms_trial/assets/78aafb3a-64e6-409f-9bc1-fe2d2682455f.png)

## Notes

- Once the Salesforce Flow is created, you will be able to create a report in Salesforce based on the Jira keys. This enables you to see all the associated Jira keys to a Case Record.
- More information about the report creation in Salesforce can be read here: [Salesforce Reporting on Jira Issue Key](/cms_trial/space/CSFJIRA/3104407562/Salesforce+Reporting+on+Jira+Issue+key/)