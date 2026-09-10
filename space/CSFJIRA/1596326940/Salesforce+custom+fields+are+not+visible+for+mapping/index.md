# Salesforce custom fields are not visible for mapping

## Summary

When trying to add a formula field to the mappings, this custom field does not show up in the field-mapping lookup.

## Environment

- Jira Cloud and DC

## Diagnostics Steps

- When trying to add a custom field (formula), the field is not displayed as an option for the mappings.

  ![contentId-1596326940](/cms_trial/assets/b10b81a3-2120-48e6-8607-4b2c6b4a91a8.png?version=1&modificationDate=1678857298838&cacheVersion=1&api=v2)

## Cause

This happens because the formula field has been created with a **relationship** from a Child Object and Child Objects are not supported by the connector.

Formula fields with relationship configured can be detected by checking the Syntax, you will find an **"\_\_r"**, as shown in the image below.

![image-20241213-142643.png](/cms_trial/assets/763bcf0a-a8ae-4879-9893-c0f8ef4095af.png)

## Workaround

This issue can be fixed by migrating the field to a **Parent Object** or **Standard Object** instead of using a field.

## Resolution

Not applicable.