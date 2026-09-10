# Listener implementation examples

This guide provides a step-by-step walkthrough for creating two different types of issue listeners in a system using SIL Manager. You will learn how to set up listeners that automatically add comments when an issue is created and when an issue's fields are updated.

## How to create a simple Issue listener

1. Open the SIL Manager and save the following script as `example1_listener.sil`:

```text
//simply adds a comment
addComment(key, currentUser(), "Your description is " + length(description) + " characters long");
```

This script adds a comment to the current issue that includes the length of its description.

![PSJC-example-listener.png](/cms_trial/assets/48e6d264-7200-4150-922b-a482f583a510.png)

1. Navigate to **Power Scripts** > **Configurations** > **Automations** > **Listeners** and set up a listener that uses the saved script and the **Issue Created** event.

![PSJC-listeners.png](/cms_trial/assets/dbb7eb0c-5bc8-4c11-a205-bd8f793ff8d1.png)

To concentrate on testing just this listener, you can disable all other listeners in your Jira.

1. Navigate to your test project and test the script. Each time an issue is created, the comment should appear in the issue.

![contentId-490998290](/cms_trial/assets/6cd73c2e-2456-4819-8c11-44bad3c705d6.png)

---

## How to create an Issue Updated listener

Next, create a second listener to monitor updates on an issue's fields. The listener will be filtered to a specific project to demonstrate its full capabilities.

1. Open the SIL Manager and save the following script as `example2_listener.sil`:

```text
//check if the field of interest was changed
if(project == "TEST" && isIssueFieldChanged("description")) {
    //get the change and play !
    JFieldChange change = getEventIssueFieldChange("description");
    addComment(key, currentUser(), "Field " + change.field + " ( changed by " + change.user  + "), old size was " + length(change.oldVal) + " chars, now is " + 
                                    length(change.newVal) + " chars");
}


//The following may be used to deal with multiple changes:
//JFieldChange [] arr = getEventIssueChanges();
//if you want to intercept multiple changes, you may get them and process accordingly
```

This script checks if the **Description** field has been changed in the TEST project. If so, it adds a comment detailing the description's old and new size and the user who made the change.

Remember to replace 'TEST' with the name of your specific project.

![contentId-490998290](/cms_trial/assets/2146cfa5-78fb-4347-8321-280fb201f95c.png)

1. Navigate to **Power Scripts** > **Configurations** > **Automations** > **Listeners** and set up a listener that uses the saved script and the **Issue Updated** event.

![PSJC-listeners.png](/cms_trial/assets/dbb7eb0c-5bc8-4c11-a205-bd8f793ff8d1.png)

1. Navigate to your test project and test the script. Each time an issue's description is updated, a comment will appear detailing the old and new size of the description field.

![contentId-490998290](/cms_trial/assets/2656ad1a-2640-48a2-a78f-a0726c5f9fb0.png)