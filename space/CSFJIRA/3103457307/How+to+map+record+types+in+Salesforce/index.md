# How to map record types in Salesforce

## Purpose

This article will help you to map the Record Types between Jira and Salesforce.

## Answer

1. Create a "text" [custom field](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/?__hstc=72543820.25abc16d5915fc3a5b62f54243363e56.1672830188938.1675947206513.1675949095738.43&__hssc=72543820.113.1675949095738&__hsfp=3434916455) in Jira.
2. In Salesforce, go to **Object Manager** > **Case**> **Record Types** > Get the 18-character ID in the URL
3. Navigate back to Jira, go to **Apps**> **Salesforce**> **Binding**> **Mapping**> **Mappings**
4. Click **Add**and map the text custom field created in step 1 to *Record Type ID*

   1. To get the Record type Id, in Jira navigate to Settings > Issues > Custom fields > Edit

      You’d be able to see the ID in the URL
   2. Map the record type id values for the mapping created in step #4  

      [Unmapped macro: inline-media-image — no content to fall back on]