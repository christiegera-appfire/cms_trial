# Automatic Jira Issue Creation and Push Updates in the same trigger

## One trigger per object

If you have one Apex trigger listening to multiple events (e. g. **after insert** and **after update**) you can still use the Apex API to create Jira issues and/or push updates to Jira. Sometimes, though, you want to call the API conditionally based on the actual event. In that case you can do so by adding some checks per case:

#### **CaseTrigger**

```java
trigger CaseTrigger on Case (after insert, after update) {
    if (Trigger.isInsert && Trigger.isAfter) {
        JCFS.API.createJiraIssue('10000', '10002');
    }
    if (Trigger.isUpdate && Trigger.isAfter) {
        JCFS.API.pushUpdatesToJira();
    }
}
```

## Apex test class for the trigger

Depending on which trigger events (**after insert** or **after update**) are used in the trigger you have to call the corresponding test helper method.

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

As with the trigger itself, you may need a test for each object trigger. All you have to do is replace `Case` in the above code with the actual object name.

After creating your test class, click **Run Test**. This ensures the test gets associated with your newly created trigger and provides code coverage.

You will need to re-run the Apex class if you ever deactivate and reactivate the trigger.

## Custom objects

The Apex API and test helper methods work as well with any custom object. You just need to find out the object name (e.g.:`MyObject__c`) and use it in the trigger and test code as documented above.

## Advanced section

If you have other triggers with Webservice callouts that are executed as a result of running this test, you might get an error message like this:

```text
Method defined as TestMethod do not support Web service callouts
```

In order to fix this error, you need to specify a fake response for the callouts. JiraTriggerTestHelper already provides a mock for its test method, but it will not mock other web service callouts. Therefore, you may need to provide your own implementation of HttpCalloutMock.

Please customize the following code according to your callout method:

#### **SuccessCalloutMock**

```java
public class SuccessCalloutMock implements HttpCalloutMock {
    public HTTPResponse respond(HTTPRequest req) {
        HttpResponse response = new HttpResponse();
        response.setStatusCode(200);
        return response;
    }
}
```

Then, set the mock before the JiraTriggerTestHelper test method is called.

#### **CaseTriggerTestAdvanced**

```java
@isTest public class CaseTriggerTest {
    @isTest static void caseAfterInsertTest() {
        Test.setMock(HttpCalloutMock.class, new SuccessCalloutMock());
        Case c = new Case();
        Test.startTest();
        insert c;
        Test.stopTest();
    }
    @isTest static void caseAfterUpdateTest() {
        Test.setMock(HttpCalloutMock.class, new SuccessCalloutMock());
        Case c = new Case();
        insert c;
        Test.startTest();
        update c;
        Test.stopTest();
    }
}
```

Also, note that the **Push API** should not be called from within a **Future**. When called from a **Future,** the **Push API** simply logs it as a warning. Check your **Apex** **Logs** to see if that is the case if the automatic synchronization is not working.

For more details, please refer to the [Salesforce documentation](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_restful_http_testing_httpcalloutmock.htm).