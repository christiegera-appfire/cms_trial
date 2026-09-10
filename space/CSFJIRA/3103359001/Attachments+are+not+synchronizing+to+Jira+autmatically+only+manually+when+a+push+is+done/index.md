# Attachments are not synchronizing to Jira autmatically only manually when a push is done

## Problem

You have followed the documentation to synchronize attachments ([Work with attachments in Salesforce](/cms_trial/space/CSFJIRA/3091695099/Work+with+attachments+in+Salesforce/) ). However, attachments only synchronize when you manually push them to Jira. You created the Apex trigger based on the documentation, but it doesn't seem to work.

## Solution

Depending on the system configuration, the Attachment might be disabled, and the File object might be using the Attachment label in the UI. This means the Apex trigger for the Attachment object won't work because the system uploads files to the File object rather than the Attachment object.

To enable the auto synchronization for the File object, add the trigger shown below:

```text
trigger ContentDocumentLinkTrigger on ContentDocumentLink (after insert) {
    Map<String, Set<Id>> sObjectsByType = new Map<String, Set<Id>>();
    Map<String, List<SObject>> sObjectsToBePushed = new Map<String, List<SObject>>(); 
    for (ContentDocumentLink contentDocumentLink : Trigger.new) {
    String sObjectType = String.valueOf(contentDocumentLink.LinkedEntityId.getSObjectType());
    if (sObjectsByType.containsKey(sObjectType)) {
        sObjectsByType.get(sObjectType).add(contentDocumentLink.LinkedEntityId);
    } else {
        sObjectsByType.put(sObjectType, new Set<Id>{contentDocumentLink.LinkedEntityId});
    }
}

for(String sObjectType : sObjectsByType.keySet()) {
    Set<Id> ids = sObjectsByType.get(sObjectType);
    String sObjectsById = 'SELECT Id FROM ' + sObjectType + ' where Id IN :ids';
    List<SObject> toBePushed = Database.query(sObjectsById);
    if (toBePushed.size() > 0) {
        sObjectsToBePushed.put(sObjectType, toBePushed);
    }
}

if (sObjectsToBePushed.size() > 0) {
    JSFS.API.pushUpdatesToJiraWithMap(sObjectsToBePushed, Trigger.old);
}
```