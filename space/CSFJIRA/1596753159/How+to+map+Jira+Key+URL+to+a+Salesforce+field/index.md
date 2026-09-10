# How to map Jira Key URL to a Salesforce field

## Summary

For various reasons, you might want to map the Jira Key URL to a Salesforce field rather than the issue number.

## Environment

- Jira DC
- Jira Cloud

## Diagnostics Steps

Not applicable.

## Cause

Mapping the Key field in Jira to a Salesforce URL field will only retrieve the issue number and not the whole URL.

## Workaround

1. Map the **Key** field in Jira to a Text field type in Salesforce:

   - Navigate to **Apps > Salesforce > Bindings > Mapping > Mappings**
2. Create a formula field and specify the return type as **Text:**

   - In Salesforce, go to **Setup > Object Manager > Case > Field and Relationships >** Create a new **Formula** field.
3. Use the following formula:

   ```text
   HYPERLINK("<Jira_instance_URL>/browse/" & <Mapped_Field_in_Step_1> ,"{JIRA_KEY}")
   ```

### Note

- Please replace the `<Jira_instance_URL>` with your instance URL and `<Mapped_Field_in_Step_1>` with the field name (for example, `text_field__c` ).
- The {JIRA\_KEY} is shown in Salesforce like below and is not a URL you need to replace.

![contentId-1596753159](/cms_trial/assets/b1655580-03b1-47de-9d92-c09ed31f2dcc.png?version=1&modificationDate=1678945285072&cacheVersion=1&api=v2)

## Resolution

Not applicable.