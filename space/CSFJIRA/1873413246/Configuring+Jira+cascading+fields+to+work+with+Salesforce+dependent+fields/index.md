# Configuring Jira cascading fields to work with Salesforce dependent fields

Connector for Salesforce & Jira supports synchronization of cascading fields in Jira with dependent fields in Salesforce.

There are four modes of synchronization types supported:

- Jira Parent - Salesforce Picklist
- Jira Child - Salesforce Picklist (Legacy)
- Merged
- Cascading

## Requirements

Value mappings need to use the exact IDs as shown on the Salesforce page, with the correct case (IDs are case-sensitive) and with no spaces before or after the value. For example,  `00590002fBnyAAE`  is not the same as  `00590002fbnyaae`.

### Jira

- Cascading select lists

Cascading select lists are a type of Jira custom field. Read more on how to [create custom fields in Jira](https://confluence.atlassian.com/adminjiracloud/create-a-custom-field-991923727.html).

### Salesforce

- Salesforce Picklist

Salesforce Picklist fields can be dependent fields. Read more on how to [create dependent fields in Salesforce](https://help.salesforce.com/articleView?id=fields_defining_field_dependencies.htm&type=5).

## Cascading field mapping modes

### Jira Parent - Salesforce Picklist

This mode lets you synchronize only the Parent value of your Jira cascading select list to a Salesforce picklist (dependent or non-dependent picklist).

- You are not able to synchronize bi-directionally in this mode.
- You are not able to update based on the Child value of your Jira cascading select list.

![contentId-1873413246](/cms_trial/assets/b7c6457d-c801-4815-a38e-93359f40dd52.png)

### Jira Child  - Salesforce Picklist (Legacy)

This mode used to be the default behavior of the app if a Jira Cascading list was selected in the mapping.

This mode lets you synchronize only the Child value of your Jira cascading select list to a Salesforce picklist field (dependent or non-dependent picklist).

- The synchronization only works in one direction, from Jira to Salesforce.
- You are **not** able to update based on the Parent value of your Jira cascading select list.

![contentId-1873413246](/cms_trial/assets/52cc46f4-95c7-4ce2-a8b6-c69644a2adbd.png)

### Merged

Merge mode lets you synchronize a combination of the Parent and Child value of your Jira cascading field to a Salesforce picklist field (Parent/Child or non-dependent picklist).

- You are able to synchronize bi-directionally in this mode.
- You are **not** able to update based on the Jira Cascading Child values.
- The Jira value mapping format required for this mode is: `Parent Option;Child Option`.

![contentId-1873413246](/cms_trial/assets/73ebec19-cdb7-416a-bfc3-e488ca9b94e1.png)

### Cascading

This mode lets you synchronize the field values in a fully cascading manner.

You can define the Parent value of your Jira cascading select list to a Salesforce picklist value (Parent or non-dependent picklist), and the Child value of your Jira cascading select list to another Salesforce picklist (Child or a non-dependent picklist).

- You are able to synchronize bi-directionally in this mode.
- You are required to choose the corresponding Salesforce child and parent fields to use this mode.

![contentId-1873413246](/cms_trial/assets/d45e6328-1648-4ccf-b0d5-1aac70602a3b.png)

Be aware that switching between synchronization modes will result in losing existing field value mappings. You will also be required to select a second (dependent) picklist when switching from either of the first 3 modes to the Cascading mode.

### Create a Cascading field mapping

1. Select a Jira cascading select list custom field in the field mapping.

   ![Field mapping](/cms_trial/assets/0d5eb0b4-0064-40af-bdee-053f41357434.png)
2. Select the appropriate synchronization mode that fits your use case.

   ![Sync mode](/cms_trial/assets/517d5c7c-0dac-4d4d-b1eb-ec8d99eada81.png)
3. Select the corresponding Salesforce field(s).  
   Depending on the Sync mode selected, you can either select only the Salesforce field or also the dependent field.

   ![image-20260915-115611.png](/cms_trial/assets/9a5c2869-ea9f-4cf4-bcf6-aeaa5e0cde62.png)
4. Click **Add field mapping** to add the newly created field mapping.
5. For the field mapping you just created, click **Menu** (▢) > **Configure**.

   ![image-20260915-120202.png](/cms_trial/assets/7ba5813f-503d-463f-b372-8ada9a6b1790.png)
6. Add the **Parent** or **Child** values for both Jira and Salesforce and click **Add**.

   ![image-20260915-120322.png](/cms_trial/assets/1b803e18-d6eb-4987-a455-b116dba4130f.png)
7. Click **Configure** when you are done.
8. Click **Save** to apply your changes.