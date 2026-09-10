# Trigger code when an association is unlinked

The app allows you to subscribe to Appfire’s Salesforce package events to invoke custom code after a specific action occurs.

To be notified about the UNLINK action, you can create a new Apex class that implements the `SfjcActionEventListener` interface.

#### MyListener

```java
global class MyListener implements JCFS.SfjcActionEventListener {
    public void onEvent(String eventName, Map<String,Object> data) {
       System.debug('Hello world!');
       System.debug(eventName);
       System.debug(data);
    }
}
```

The UNLINK event contains the following fields:

- `son` - string, e.g. Case
- `soid` - string - the Case Id
- `jiraIssueId` - string

In this example, `MyListener` listens for a UNLINK event between Jira and a Salesforce object. Once the UNLINK event of the association is detected, a debug message is sent to the execution log.

To use this feature, you must grant the `WebhookRestResource` Apex class access to the integration user profile.

1. Go to **Setup** ▢and enter `Apex Classes` in the **Quick Find** field.
2. Select **WebhookRestResource** > **Security**.

   ![2025-10-15_15-55-50.png](/cms_trial/assets/34a16a0a-c69e-4a21-b993-81af46d43b24.png)
3. Add the integration user profile to the *Enabled Profiles*.

   ![2025-10-15_15-58-44.png](/cms_trial/assets/c0eaad3f-38af-456f-92bf-d46cc7b4ff27.png)