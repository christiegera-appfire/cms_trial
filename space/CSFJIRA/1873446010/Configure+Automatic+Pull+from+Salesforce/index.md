# Configure Automatic Pull from Salesforce

When a support agent updates a case in Salesforce, the linked Jira issue should reflect that change without anyone having to trigger a manual sync. Automatic Pull makes this happen by using Apex triggers in Salesforce to detect record changes and push them to the associated Jira issues instantly.

This means your engineering team always works with up-to-date information, without relying on agents to remember to sync, and without administrators having to intervene every time a record changes.

This page walks you through everything you need to configure as a Jira and Salesforce administrator to allow Automatic Pull from Salesforce by enabling the **Allow** **Automatic Pull**option and configuring the required Salesforce triggers.

Automatic Pull only works if:

- Connection is configured to Allow Automatic Pull
- Association is configured to Allow Automatic Pull
- Salesforce Triggers for the respective objects are installed
- Connection allows modification
- The Salesforce object for which you configure the Automatic Pull trigger is configured to be available

**Automatic Pull in Jira** is called the **Automatic Push in Salesforce**. The naming is chosen based on the user's point of view for the respective system.

## Before you start

Make sure you have:

- Administrator rights in Jira
- [configure the available objects and fields](/cms_trial/space/CSFJIRA/1873347420/Configure+Salesforce+objects+and+fields+in+connection+search+results/) before proceeding with the following steps.
- [Installed](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/) and [configured](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/) the Salesforce package

## Enable connection to allow Automatic Pull

1. Select **Apps** from the left sidebar in Jira.
2. Under *Connector for Salesforce*, click **Connections**.
3. On the *Salesforce Connections* window, navigate to the Connectionyou want to configure and click **Configure.**

   ![Configure Connections](/cms_trial/assets/f5f40947-a483-4f29-a0d6-e1b86a117b6a.png)
4. On the*Connection Configuration* window, find the *Connection Settings* and enable the **Allow Automatic Pull** option.
5. Make sure the **Allow Modification** option is enabled.

   ![Connection Configuration](/cms_trial/assets/61693cd2-3bf5-4543-8cf3-6d631143a0bc.png)

## Enable Automatic Pull for an association

Automatic Pull from Salesforce has to be enabled/disabled per association. Set it up either when [creating an association](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754430) or later by [Configuring an association](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/1953366688). Additionally, the preset configuration for the Automatic Pull switch can be configured on the **Connection Configuration** page.

## Create and Deploy Apex triggers

The Connector relies on Apex triggers to be informed of changes on Salesforce records. These triggers have to be created and deployed manually in Salesforce. For Salesforce Enterprise and Unlimited editions, the standard deployment of Apex triggers is required (see Salesforce [documentation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_deploying.htm)).

The following code samples show how to write triggers for **Cases**. To create triggers for other objects, replace the object name in the code accordingly.

### Push to Jira after Object updated

**Cloud**

#### **CaseUpdatedTrigger**

```java
trigger CaseUpdatedTrigger on Case (after update) {
    JCFS.API.pushUpdatesToJira();
}
```

**DC**

#### **CaseUpdatedTrigger**

```java
trigger CaseUpdatedTrigger on Case (after update) {
    JSFS.API.pushUpdatesToJira();
}
```

Apex test class for the triggers

Once triggers are created, they need a certain level of test coverage to be allowed to deploy to the Production environment. The package contains a test helper that tests the whole scenario. You simply need to add a unit test for each trigger and call the test helper method as follows:  
  
**Cloud**

#### **CaseUpdatedTriggerTest**

```java
@isTest public class CaseUpdatedTriggerTest {
    @isTest static void testTriggerAfterUpdate() {
        JCFS.JiraTriggerTestHelper.testAfterUpdate('Case');
    }
}
```

**DC**

#### **CaseUpdatedTriggerTest**

```java
@isTest public class CaseUpdatedTriggerTest {
    @isTest static void testTriggerAfterUpdate() {
        JSFS.JiraTriggerTestHelper.testAfterUpdate('Case');
    }
}
```

Your Jira and Salesforce systems should now be ready to push changes on configured Salesforce records automatically to the associated Jira issues.

Just as the trigger itself, you need a test for each object trigger. All you have to do is replace `Case` in the above code with the actual object name.

After creating your test class, click **Run Test**. This ensures the test gets associated with your newly created trigger and provides code coverage.

You will need to re-run the Apex class if you ever deactivate and reactivate the trigger.

The above-mentioned method works only if you call the API directly from within a trigger. If you need to call the API indirectly, for instance from a helper method, see the advanced usage section below.

The API should not be called from within a **Future**. When called from a **Future,** the API simply logs it as a warning. Check your **Apex** **Logs** to see if that is the case if the automatic synchronization is not working.

### Custom objects

The Apex API and test helper methods work as well with any custom object. You just need to find out the object name (e.g. "`MyObject__c`") and use it in the trigger code as documented above. If you are testing a Custom Object, provide the fully qualified name (include your namespace in the Salesforce Object Name, e.g. `'yournamespace__MyObject__c'`). You can get the fully qualified name from the **API Name,** which contains your namespace and the Salesforce Object Name.

To obtain the API Name, navigate to your [custom object definition detail configuration](https://help.salesforce.com/articleView?id=dev_objectedit.htm&type=5) window and look for the **API name**. For more information, view the [Salesforce documentation on namespace prefixes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_namespace_prefix.htm).

### Advanced usage

The Apex API supports selective pushing, so that you can exclude unwanted Salesforce records from the push. For this purpose, use the following API method:

**Cloud**

#### **Signature of JCFS.API.pushUpdatesToJira**

```java
JCFS.API.pushUpdatesToJira(List<SObject> newObjects, List<SObject> oldObjects)
```

**DC**

#### **Signature of JCFS.API.pushUpdatesToJira**

```java
JSFS.API.pushUpdatesToJira(List<SObject> newObjects, List<SObject> oldObjects)
```

Pass all the records for which you want a push to Jira to happen as `newObjects`. Note that all the records in this list must be of the same runtime type. So we recommend using a concrete type, for example, `List<Case>` or `List<Account>`for the variable you pass as this parameter. The `oldObjects` parameter is not used at the moment, so you can pass `Trigger.old`or an empty list for it.

For example, if you want to push updates only for Cases whose summaries start with "*Post,*" you can use the following trigger code:  
  
**Cloud**

#### **Push updates to JIRA selectively**

```java
trigger CaseUpdatedTrigger on Case (after update) {
    List<Case> toBePushedToJira = new List<Case>(); // proper runtime type, List<SObject> won't work
    for(Case c : Trigger.new) {
        if (c.Subject.startsWithIgnoreCase('Post')) {
            toBePushedToJira.add(c);
        }
    }
    JCFS.API.pushUpdatesToJira(toBePushedToJira, Trigger.old);
}
```

**DC**

#### **Push updates to JIRA selectively**

```java
trigger CaseUpdatedTrigger on Case (after update) {
    List<Case> toBePushedToJira = new List<Case>(); // proper runtime type, List<SObject> won't work
    for(Case c : Trigger.new) {
        if (c.Subject.startsWithIgnoreCase('Post')) {
            toBePushedToJira.add(c);
        }
    }
    JSFS.API.pushUpdatesToJira(toBePushedToJira, Trigger.old);
}
```

### Attachments

If you would like automatic pull of attachments, a separate trigger is required. To make this work, enable the **Synchronize Attachments** option in the Connection settings. For details, see the [attachment configuration](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) steps in the setting document.  
  
**Cloud**

#### **Attachment Trigger**

```java
trigger AttachmentTrigger on Attachment (after insert) {  
    Map<String, Set<Id>> sObjectsByType = new Map<String, Set<Id>>();
    for(Attachment a : Trigger.new) {
        String sObjectType = String.valueOf(a.ParentId.getSObjectType());
        if (sObjectsByType.containsKey(sObjectType)) {
            sObjectsByType.get(sObjectType).add(a.ParentId);
        } else {
            sObjectsByType.put(sObjectType, new Set<Id>{a.ParentId});
        }
    }
    
    for(String sObjectType : sObjectsByType.keySet()) {
        Set<Id> ids = sObjectsByType.get(sObjectType);
        String sObjectsById = 'SELECT Id FROM ' + sObjectType + ' where Id IN :ids'; 
        List<SObject> toBePushed = Database.query(sObjectsById);
        JCFS.API.pushUpdatesToJira(toBePushed, Trigger.old);
    }
}
```

**DC**

#### **Attachment Trigger**

```java
trigger AttachmentTrigger on Attachment (after insert) {  
    Map<String, Set<Id>> sObjectsByType = new Map<String, Set<Id>>();
    for(Attachment a : Trigger.new) {
        String sObjectType = String.valueOf(a.ParentId.getSObjectType());
        if (sObjectsByType.containsKey(sObjectType)) {
            sObjectsByType.get(sObjectType).add(a.ParentId);
        } else {
            sObjectsByType.put(sObjectType, new Set<Id>{a.ParentId});
        }
    }
    
    for(String sObjectType : sObjectsByType.keySet()) {
        Set<Id> ids = sObjectsByType.get(sObjectType);
        String sObjectsById = 'SELECT Id FROM ' + sObjectType + ' where Id IN :ids'; 
        List<SObject> toBePushed = Database.query(sObjectsById);
        JSFS.API.pushUpdatesToJira(toBePushed, Trigger.old);
    }
}
```

To get test coverage for the Attachment trigger, use the provided test helper below:  
  
**Cloud**

#### **Apex test class for Attachment trigger**

```java
@isTest public class AttachmentTriggerTest {
    @isTest static void caseAfterInsertTest() {
        Case randomCase = new Case(Subject = 'AttachmentTriggerTest');
        insert randomCase;
        Attachment randomAttachment = new Attachment(ParentId = randomCase.Id, Name = 'test.txt', Body = Blob.valueOf('Test'));
        JCFS.JiraTriggerTestHelper.testAfterInsert(randomAttachment);
    }
}
```

**DC**

#### **Apex test class for Attachment trigger**

```java
@isTest public class AttachmentTriggerTest {
    @isTest static void caseAfterInsertTest() {
        Case randomCase = new Case(Subject = 'AttachmentTriggerTest');
        insert randomCase;
        Attachment randomAttachment = new Attachment(ParentId = randomCase.Id, Name = 'test.txt', Body = Blob.valueOf('Test'));
        JSFS.JiraTriggerTestHelper.testAfterInsert(randomAttachment);
    }
}
```

### Salesforce Files

If you would like an automatic pull of Salesforce Files, you will need another trigger. To make this work, **Synchronize Attachments** must be enabled in the Connection settings. For details, see the [attachment configuration](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) setting document.

**Cloud**

#### **File Trigger**

```java
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
        JCFS.API.pushUpdatesToJiraWithMap(sObjectsToBePushed, Trigger.old);
    }
}
```

**DC**  
To use this Salesforce File trigger, please update the Salesforce Package to the latest version.

#### **File Trigger**

```java
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
}
```

Uploading multiple files in Salesforce at the same time may result in duplicate attachments in Jira.

To get test coverage for the `ContentDocumentLink` trigger, use the provided test helper below:  
  
**Cloud**

#### **Apex test class for ContentDocumentLink trigger**

```java
@isTest public class ContentDocumentTriggerTest {
    @isTest static void caseAfterInsertTest() {
        Case randomCase = new Case(Subject = 'ContentDocumentTriggerTest');
        insert randomCase;
		ContentVersion contentVersion = new ContentVersion(PathOnClient = 'PathOnClient', VersionData = Blob.valueOf('Test'));
		insert contentVersion;
        ContentVersion createdContentVersion = [SELECT ContentDocumentId FROM ContentVersion WHERE Id = :contentVersion.Id];
        ContentDocumentLink randomContentDocumentLink = 
            new ContentDocumentLink(
                ContentDocumentId = createdContentVersion.ContentDocumentId, 
                LinkedEntityId = randomCase.Id,
                ShareType = 'V'
            );
        JCFS.JiraTriggerTestHelper.testAfterInsert(randomContentDocumentLink);
    }
}
```

**DC**

#### **Apex test class for ContentDocumentLink trigger**

```java
@isTest public class ContentDocumentTriggerTest {
    @isTest static void caseAfterInsertTest() {
        Case randomCase = new Case(Subject = 'ContentDocumentTriggerTest');
        insert randomCase;
		ContentVersion contentVersion = new ContentVersion(PathOnClient = 'PathOnClient', VersionData = Blob.valueOf('Test'));
		insert contentVersion;
        ContentVersion createdContentVersion = [SELECT ContentDocumentId FROM ContentVersion WHERE Id = :contentVersion.Id];
        ContentDocumentLink randomContentDocumentLink = 
            new ContentDocumentLink(
                ContentDocumentId = createdContentVersion.ContentDocumentId, 
                LinkedEntityId = randomCase.Id,
                ShareType = 'V'
            );
        JSFS.JiraTriggerTestHelper.testAfterInsert(randomContentDocumentLink);
    }
}
```

To make this work, **Synchronize Attachments** must be enabled in the Connection settings.