# Writing Actions (Post-Functions)

This page describes considerations for customizing your workflow actions (actions).

## Writing Actions (Post-Functions)

Actions are the workflow actions executed in the final stage of a transition. They have no special return requirements and consistently execute in the context of the transitioned issue.

A action may be as simple as:

```text
assignee = currentUser();
```

Or you can add complexity to meet a specific requirement.

Unlike validators and conditions, the action is the only place in the workflow where you can modify the issue.

## Parameters

On the Cloud, the only derived parameter is the action ID. It is passed as the only parameter in the script execution, allowing you to create decisions.

An example is below:

![Power Scripts for Jira Cloud WSJF calculation interface display](/cms_trial/assets/aff1f236-9e0c-4140-881b-163f8d1c96e4.png)

And the corresponding script:

```java
logPrint("ERROR", "Postfunction execution - Current user is :" + currentUser() + " postfunction id:" + argv[0]);

switch(argv[0]) {
    case "e6132922-74c4-4315-84f0-32bcb70cddf4": //this is the first postfunction
        logPrint("ERROR", "This is the end, my only friend " + currentUser());
        break;
    case "9c5bbeda-f20c-44ae-bda4-272203e3b412": //this is the second postfunction
        logPrint("ERROR", "The end of our elaborate plans, the end of everything that stands");
        break;
}
```

The output is (on the ERROR level, where the message was pushed):

```text
Postfunction execution - Current user is :6093b81a539c14006ad3c137 postfunction id:e6132922-74c4-4315-84f0-32bcb70cddf4
This is the end, my only friend 6093b81a539c14006ad3c137
Postfunction execution - Current user is :6093b81a539c14006ad3c137 postfunction id:9c5bbeda-f20c-44ae-bda4-272203e3b412
The end of our elaborate plans, the end of everything that stands
```

Even if the script is the same, the different integration points generate unique IDs (on different transitions and workflows). Therefore, you may use this strategy to apply small changes to the logic depending on your location. However, these IDs are not portable from install to install.

The goal is for this information to assist you in script reusability.

## Runtime User & Issue

Actions execute with the user activating the transition, no matter if it’s declared as asynchronous or synchronous. If the transition is triggered by another automation or addon not acting as the triggering user, the current user may be null, so you must deal with it programmatically.

Scripts are executed within the issue context.

## Return Codes For Post-Functions

```text
return;
```

Note that “return;” ends the program, and any values the script returns are ignored.

## Order of the Actions

In general, it’s recommended to place actions after all standard actions. This allows the issue to be re-indexed and the data stored correctly.

The new issue has not been indexed if the action is applied to the create transition. Also, the index does not exist until this step runs the first time, and no data may exist for the issue. For these reasons, it is always best for the action to come after all standard actions.

**Note**

On Jira Cloud, Atlassian decided to launch all actions asynchronously after all the standard actions (actions) are executed, no matter what position they have in the workflow!

More, the transition does not wait for the remote actions (actions) to finish. You may transition twice an issue, while the action linked to the first transition is still running.

Your postfunctions must care about this and you should keep in mind that while your SIL postfunction is running over the snapshot of the issue at the time of triggering, it may not be the reality at the execution time.

Care should also be employed on custom fields values, if they are set by other integrations. Because everything is asynchronous, and Atlassian Jira does not act as a coordinator, but as a trigger-only platform, they may not be set (or set on non-updated values).

This is the Peacock survey macro, which allows users to submit feedback for the page. If you want to make changes to the macro or the survey, please open Peacock in the "Apps" menu.