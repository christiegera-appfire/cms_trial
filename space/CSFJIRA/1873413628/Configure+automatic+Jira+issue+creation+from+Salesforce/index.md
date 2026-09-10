# Configure automatic Jira issue creation from Salesforce

This guide will help you configure Automatic Jira issue creation from Salesforce by configuring the required Salesforce triggers. This automation has some important prerequisites and conditions, as noted in the section below.

## Before you start

1. The Salesforce Package must be [installed](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/) and [configured](/cms_trial/space/CSFJIRA/1873772649/Set+up+your+integration+in+Salesforce/).
2. You will need to [configure the available objects and fields](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) before proceeding with other steps.
3. You will also need to confirm that you can manually [create a Jira Issue from Salesforce](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/). If the manual method does not work, then the automation will not work either.
4. Note that Automatic Jira issue creation will work only if:

   1. Salesforce object records, from which you want to create Jira issues automatically, are configured to be available for the authorized connection.
   2. Apex triggers for the respective objects are installed.

## Create and deploy Apex triggers

You need Apex triggers to automatically create Jira issues from Salesforce records. These triggers have to be created and deployed manually in Salesforce. For Salesforce Enterprise and Unlimited edition, the standard deployment of Apex triggers is required (see Salesforce [documentation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_deploying.htm)).

The following code samples show how to write triggers for Cases. To create triggers for other object types, replace the object name in the code accordingly.

## Automatically create a Jira issue after a Salesforce record is inserted

#### **CaseInsertedTrigger**

```java
trigger CaseInsertedTrigger on Case (after insert) {
    JCFS.API.createJiraIssue('1000', '10002');
}
```

Note that you need to, respectively, hardcode the ***Jira project id*** and ***Jira issue type id***. You can get these values from the **Jira REST API**. In future versions of the package, there will be a feature helping admins generate the full code for the trigger from a template.

## Automatically create a Jira issue after a Salesforce record is updated

You can also create an issue automatically after a record is updated (e. g. in an **after update** trigger) as follows:

For cloud administrators, you can choose either:

- A trigger that automatically creates a new Jira issue [and the post action respects the settings after creating the Jira issue.](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) This was an enhancement introduced from JCFS 4.7 onwards to deliver on a popular request. Submit enhancements on [Appfire’s support site.](https://appfire.atlassian.net/servicedesk/customer/portal/11)

#### **CaseUpdatedTrigger**

```java
trigger CaseUpdatedTrigger on Case (after update) {
    JCFS.API.createJiraIssueWithDefaultPostAction('1000', '10002');
}
```

- A trigger that omits any post action once the Jira issue is created

### Caveats

The above-mentioned method works only if you call the API directly from within a trigger. If you need to call the API indirectly, for instance from a helper method, see the advanced usage section below.

## Apex test class for the triggers

Once triggers are created, they need a certain level of test coverage to be allowed to deploy to the Production environment. The package contains a test helper which tests the whole scenario. You simply need to add a unit test for each trigger and call the test helper method. Depending on the trigger event (**after insert** or **after update**) you will have to call the corresponding test helper method. A sample of both tests is shown in the following example:

#### **CaseTriggerTest**

```java
@isTest public class CaseTriggerTest {
    @isTest static void caseAfterInsertTest() {
    	JCFS.JiraTriggerTestHelper.testAfterInsert('Case');
	}
	@isTest static void caseAfterUpdateTest() {
    	JCFS.JiraTriggerTestHelper.testAfterUpdate('Case');
	}
}
```

Just as with the trigger itself, you need a test for each object trigger. All you have to do is replace `Case` in the above code with the actual object name.

After creating your test class, click **Run Test**. This ensures the test gets associated with your newly created trigger and provides code coverage.

You will need to re-run the Apex class if you ever deactivate and reactivate the trigger.

### Custom objects

The Apex API and test helper methods work as well with any custom object. You just need to find out the object name (e.g. `'MyObject__c'`) and use it in the trigger code as documented above. If you are testing a Custom Object, provide the fully qualified name (include your namespace in the Salesforce Object Name, e. g. `'yournamespace__MyObject__c'`)

## Advanced Usage

Our Apex API supports selective issue creation so that you can avoid the automatic creation of Jira issues from unwanted Salesforce objects. For this purpose you can use the following API method:

For administrators, you can choose either:

A trigger that automatically creates a new Jira issue [and the post action respects the settings after creating the Jira issue.](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) This was an enhancement introduced JCFS 4.7 onwards to deliver on a popular request. Submit enhancements on [Appfire’s support site.](https://appfire.atlassian.net/servicedesk/customer/portal/11)

#### **Signature of JCFS.API.createJiraIssueWithDefaultPostAction**

```java
trigger CaseInsertedTrigger on Case (after insert) {
    List<Case> toBeCreated = new List<Case>();
    for(Case c : Trigger.new) {
        toBeCreated.add(c);
    }
    JCFS.API.createJiraIssueWithDefaultPostAction('10300', '10001', toBeCreated, Trigger.old);
}
```

A trigger that omits any post action once the Jira issue is created

#### **Signature of JCFS.API.createJiraIssue**

```java
trigger CaseInsertedTrigger on Case (after insert) {
    List<Case> toBeCreated = new List<Case>();
    for(Case c : Trigger.new) {
        toBeCreated.add(c);
    }
    JCFS.API.createJiraIssue('10300', '10001', toBeCreated, Trigger.old);
}
```

Pass all the records you want to create a Jira issue from as `newObjects`. Note that all the records in this list must be of the same runtime type. So we recommend using a concrete type, e.g. `List<Case>` or `List<Account>`for the variable, you pass as this parameter. The `oldObjects` parameter is not used at the moment so you can pass `Trigger.old`or an empty list for it.

For instance, if you want to create Jira issues only from Cases whose summaries start with `Post` you can use the following trigger code:

#### **Selective automatic JIRA issue creation**

```java
trigger CaseInsertedTrigger on Case (after insert) {
    List<Case> toBeCreated = new List<Case>(); // proper runtime type, List<SObject> won't work
    for(Case c : Trigger.new) {
        if(c.Subject.startsWithIgnoreCase('Post')) {
            toBeCreated.add(c);
        }
    }
    JCFS.API.createJiraIssue('10300', '10001', toBeCreated, Trigger.old);
}
```

## Give us your feedback

We're gathering feedback on implementing an easier method of adding triggers for the Connector. Submit enhancements on [Appfire’s support site.](https://appfire.atlassian.net/servicedesk/customer/portal/11)