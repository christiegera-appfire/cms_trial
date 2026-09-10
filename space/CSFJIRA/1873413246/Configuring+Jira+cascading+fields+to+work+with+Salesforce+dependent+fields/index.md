# Configuring Jira cascading fields to work with Salesforce dependent fields

Connector for Salesforce & Jira supports synchronization of cascading fields in Jira with dependent fields in Salesforce.

There are four modes of synchronization types supported:

- Jira Parent - Salesforce Picklist
- Jira Child - Salesforce Picklist (Legacy)
- Merged
- Cascading

## Requirements

Value mappings need to use the exact IDs as shown on the Salesforce page, with the correct case (IDs are case-sensitive). and with no spaces before or after the value. For example,  `00590002fBnyAAE`  is not the same as  `00590002fbnyaae`.

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

This mode is used to be the default behavior of the app if a Jira Cascading list was selected in the mapping.

This mode allows you to synchronize only the Child value of your Jira cascading select list to a Salesforce picklist (dependent or non-dependent picklist).

- The synchronization only works in one direction, from Jira to Salesforce.
- You are **not** able to update based on the Parent value of your Jira cascading select list.

![contentId-1873413246](/cms_trial/assets/52cc46f4-95c7-4ce2-a8b6-c69644a2adbd.png)

### Merged

Merge mode lets you synchronize a combination of the Parent and Child value of your Jira cascading field to a Salesforce picklist (Parent/Child or non-dependent picklist).

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

Be aware that switching between synchronization modes will result in losing existing field value mappings. You will also be required to select a second (dependent) picklist when switching from either the first 3 modes to the Cascading mode.

### Create a  Cascading field mapping

1. Select a Jira cascading select list custom field in the field mapping.

   ![screenshot of Cascading field mapping](/cms_trial/assets/f1b328ac-f149-4105-93cf-34f45ebf2554.png)
2. Select the corresponding Salesforce field(s).  
   Depending on the Cascading mode, you can either select only the first field or both.

   ![screenshot of salesforce Cascading field mapping](/cms_trial/assets/5b5cb063-ae47-4c26-bc54-4aed2b5b53d9.png)
3. Click **+ Add** to add the newly-created field mapping.
4. Click **Configure** on the field mapping you just created.

   ![screenshot of configuring field mapping](/cms_trial/assets/cf3a5bf2-9b2c-453a-9d20-8bae42afc0bb.png)
5. Choose the appropriate synchronization mode that fits your use case.

   ![2025-10-15_11-36-35.png](/cms_trial/assets/be46bbd4-a7ce-405f-afa6-5b460757575d.png)
6. Add the **Parent** or **Child** values for both Jira and Salesforce and click **Add**.
7. Save the value mapping configuration when you are done.