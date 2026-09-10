# How to make a Jira paragraph custom field expandable when creating a Jira issue from Salesforce

By default, Jira Paragraph/Multi-line custom fields don’t behave the same way in Salesforce as they do in Jira, where the field allows for multiple lines. However, there’s a way to expand the field in the Salesforce Lightning Component (similar to the Jira Description field) by mapping it to a Salesforce Rich Text field.

Please note that this is a workaround solution for automation. You can use it at your own risk.

## Instructions

1. Ensure that the custom field is added and appears in the Lightning Component while still not expandable.

   ![contentId-2257977638](/cms_trial/assets/56a202e1-27ae-40db-919a-604e7285b210.png)
2. In the selected Salesforce Object record, click the **Gear Icon** (▢) **> Edit Object**
3. Go to the **Field & Relationships** page.
4. To create a new field, click **New** and select the **Text Area (Rich)** data type.
5. Click **Next**
6. Follow the setup wizard and give the field a name of your choice.
7. Map the new Salesforce Rich Text field with the Jira Paragraph field. For detailed instructions, see [Configure field mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

   ![contentId-2257977638](/cms_trial/assets/64729427-5050-4072-9acd-1a88da6acd7f.png)
8. Confirm in Salesforce that the field is now expandable.

   ![contentId-2257977638](/cms_trial/assets/86e749c8-4bd6-48c8-82ad-f113bc81ec00.png)

It is not necessary to create a new field. If your Salesforce Object already has a Rich Text field, you can follow the same steps and map the existing Rich Text field to the Jira Paragraph field.