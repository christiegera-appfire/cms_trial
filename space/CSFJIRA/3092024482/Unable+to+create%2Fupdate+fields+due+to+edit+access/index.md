# Unable to create/update fields due to edit access

## Summary

When pulling data from Salesforce, the following error appears:

```text
Unable to create/update fields: customTextAreaField__c. 
Please check the security settings of this field and verify that it is 
read/write for your profile or permission set.
```

![contentId-3092024482](/cms_trial/assets/c2d349eb-d4d3-4eaf-8781-764089bc95b4.png?version=1&modificationDate=1678796545911&cacheVersion=1&api=v2)

## Environment

- Jira Cloud and Server
- All versions

## Diagnostics Steps

1. **Identify the integration user**:

   1. In Salesforce's setup, search in **Quick Find** “Connected Apps OAuth Usage”.
   2. In the connected app “Salesforce & JIRA Cloud Connector”, click on the **User Count**.
   3. When the new screen appears, it will show you who is the integration user.
2. **Identify the Profile for the Integration user**:

   1. Once you have identified the Integration user, you must identify its profile.
   2. Search “Users” in the **Quick Find**. Then search for the integration user from step 1, and click on **Profile**. Then scroll down to **Field-Level Security**and click on the object that you’re working on (For example: “Case” object)
3. Check whether the fields have Read and Edit permissions.

   ![contentId-3092024482](/cms_trial/assets/7c669141-d794-4ea2-ab92-e491cffbf388.png?version=1&modificationDate=1678943934458&cacheVersion=1&api=v2)

## Cause

The Integration User doesn't have **edit access** to the problematic fields.

## Workaround

Not applicable.

## Resolution

Make sure the problematic fields have edit access for the Integration User profile.