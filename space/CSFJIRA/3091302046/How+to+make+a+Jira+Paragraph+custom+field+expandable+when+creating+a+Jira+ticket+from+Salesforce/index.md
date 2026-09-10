# How to make a Jira Paragraph custom field expandable when creating a Jira ticket from Salesforce

## Issue

By default, the Jira **Paragraph/Multi-Line** custom field does not behave the same way in Salesforce as it does in Jira. Nonetheless, it appears that there is a way to trick the Lightning Component to make the field expandable the same as the Jira Description field by mapping it to a Salesforce Richtext field.

## Instructions

1. Confirm that the custom field is added and appears in the Lightning Component while it is still not expandable.

   ![contentId-3091302046](/cms_trial/assets/72fbaf8c-dee9-4713-98b8-397f3049f042.png)
2. In the selected Salesforce Object, edit the object through **Gear Icon > Edit Object**
3. Navigate to the **Field & Relationships** page.
4. Create a new field with **Text Area (Rich)** data type.
5. Follow the creation wizard and set the name as you like.
6. When the field is created, map the new Salesforce Richtext field with the Jira Paragraph field.

   ![contentId-3091302046](/cms_trial/assets/a36ae997-cb16-4ab4-8181-a9c7b5ff611b.png)
7. Confirm in Salesforce that the field is now expandable.

   ![contentId-3091302046](/cms_trial/assets/c51d7864-9baf-460d-ac92-a4cdc00f1b01.png)

It is not necessary to create a new field. The same step will work with an already created Richtext field available for the Salesforce Object.