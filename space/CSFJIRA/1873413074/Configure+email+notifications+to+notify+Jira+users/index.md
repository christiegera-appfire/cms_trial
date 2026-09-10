# Configure email notifications to notify Jira users

You can configure Connector for Salesforce & Jira to send email notifications when an event is triggered.

The setup consists of two parts:

1. Specifying Jira groups to notify in Jira.
2. Creating and deploying the required Apex triggers in Salesforce.

Currently, the Connector supports sending email notifications to Jira users when someone creates a Case comment.

## Specifying Jira groups to notify

Jira groups can be specified at the Connection level. This affects each binding and Jira project that is using the Connection.

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/af6d1b71-9a03-46ee-b03f-c4f707383654.png)
3. Under *Connector for Salesforce*, click **Connections**.
4. On the *Salesforce Connections* screen, navigate to the **Connection** you want to configure and select **Configure.**
5. Under **Notification Settings**, choose who you want to send notifications to by selecting:

   - **All recipients of Issue Commented event**
   - **Current Assignee**, **Reporter**
   - **All Watchers**
   - **All Voters**
   - **Groups**  
     For more information about **All recipients of Issue Commented event**, see *Sending Notifications Based on a Project's Notification Scheme***.**

     ![contentId-1873413074](/cms_trial/assets/c4f6bbd9-4016-4a24-8fb2-8cd9ed734bb9.png)
6. Click **Save**.

## Send notifications based on a project's notification scheme

The **All recipients of Issue Commented event** setting allows you to enable email notifications defined within your [Jira's Notification Scheme](https://confluence.atlassian.com/adminjiracloud/creating-a-notification-scheme-776636401.html).

The event that is triggered is the **Issue Commented** event and is dependent on the Notification Scheme that is set up for the project to which the Connection is bound.

Only the following recipients are supported:

- Current Assignee
- Reporter
- Single User
- Group
- All Watchers

## Create and deploy Apex triggers

The Connector relies on **Apex triggers** to be informed of changes on Salesforce objects. These triggers have to be created and deployed manually in Salesforce.

For Salesforce Enterprise and Unlimited editions, the standard deployment of Apex triggers are required (see Salesforce [Deploying Apex](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_deploying.htm) documentation).

## Notify Jira of new comments on cases

This provides notifications when someone creates a comment in Salesforce.

Note that the email notification will be sent:

- Based on the ***Comment Privacy***and ***Comment Tag Filter***settings in the Connection configuration page.
- Only to Jira issues currently associated with the **Case**.
- Only to Jira users (in the specified groups) who have access to the associated Jira issue.

A successful email notification may look like this:

![contentId-1873413074](/cms_trial/assets/ec530e8a-8795-40af-8887-a2c6ee07160b.png)

## Add CaseComment trigger

The ***JCFS.API.fireEvents()*** API endpoint allows Jira to be notified of events happening in Salesforce, typically originating from Salesforce triggers.

Call ***JCFS.API.fireEvents()*** in an ***after insert*** Trigger on ***CaseComment*** as follows:

#### **Notify JIRA of new comments on Cases**

```java
trigger CaseCommentsCreated on CaseComment (after insert) {
	JCFS.API.fireEvents(JCFS.Events.fromCreatedCaseComments(Trigger.new));
}
```

If you don't want to send all triggered CaseComment objects to Jira, you can pass a filtered ***List<CaseComment>*** to ***JCFS.Events.fromCaseComments()***.

## Test CaseComment trigger

To get test coverage for CaseComment trigger use the provided test helper as shown:

#### **Apex test class for CaseComment trigger**

```java
@isTest public class CaseCommentCreatedTriggerTest {
	@isTest static void caseCommentAfterInsertTest() {
		Case randomCase = new Case(Subject = 'CaseCommentCreatedTriggerTest');
		insert randomCase;
		CaseComment randomCaseComment = new CaseComment(
			ParentId = randomCase.Id,
			CommentBody = 'In faucibus orci est, vitae dignissim enim commodo a.'
		);
		JCFS.JiraTriggerTestHelper.testAfterInsert(randomCaseComment);
	}
}
```

## Advanced information

If you have other triggers with Webservice callouts that are executed as a result of running this test, you might get an error message like this:

```text
Method defined as TestMethod do not support Web service callouts
```

To fix this error, you need to specify a fake response for the callouts. `JiraTriggerTestHelper` already provides a mock for its test method, but it will not mock other webservice callouts. Therefore, you may need to provide your own implementation of HttpCalloutMock.

Customize the following code according to your callout method:

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

Then, set the mock before the CaseCommentCreatedTriggerTest test method is called.

#### **CaseCommentCreatedTriggerTest**

```java
@isTest public class CaseCommentCreatedTriggerTest {
    @isTest static void caseAfterInsertTest() {
        Test.setMock(HttpCalloutMock.class, new SuccessCalloutMock());
        Case randomCase = new Case(Subject = 'CaseCommentCreatedTriggerTest');
		insert randomCase;
		CaseComment randomCaseComment = new CaseComment(
			ParentId = randomCase.Id,
			CommentBody = 'In faucibus orci est, vitae dignissim enim commodo a.'
		);
        Test.startTest();
        insert randomCaseComment;
        Test.stopTest();
    }
}
```

For more details, please refer to the Salesforce [Testing HTTP Callouts](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_restful_http_testing_httpcalloutmock.htm) documentation.