# Reschedule issues

## Problem

You want the project lead to reschedule issues in one simple step which includes entering the fix versions, an assignee and an optional comment.

## Solution

## Create the action

Begin by creating the **Reschedule** action.

![Power Scripts for Jira Cloud REST webhooks interface](/cms_trial/assets/747079fb-5f25-4e23-85ba-370417049ecb.png)

## Condition script

Next, enter the following code to set the action as available only for the project lead and applicable only to issues that are not **Resolved** or **Closed**.

#### **Condition script**

```text
number ENABLED = 1;
number DISABLED = 2;
number HIDDEN = 3;

if(projectPM(project) == currentUser() && status != "Resolved" && status != "Closed"){
 return ENABLED;
}

return HIDDEN;
```

## Screen script

Next, enter the below script to prompt the user to select fix versions and a new assignee (the default value is the initial assignee), and enter a comment.

#### **Screen script**

```text
string TEXT = "TEXT";
string TEXT_DISABLED = "TEXT_DISABLED";
string [] fields;

// fix versions
fields = addElement(fields, "Fix Versions");
fields = addElement(fields, TEXT);
fields = addElement(fields, "");

// assignee
fields = addElement(fields, "Assignee");
fields = addElement(fields, TEXT);
fields = addElement(fields, assignee);

// comment
fields = addElement(fields, "Comment");
fields = addElement(fields, TEXT);
fields = addElement(fields, "");

return fields; 
```

This code renders the following screen.

![Power Scripts for Jira Cloud right side panel interface](/cms_trial/assets/867b0f62-b79d-410d-8407-a8ea254b720a.png)

Assigning a string value that contains pipes to a string array splits the original string at the position of each pipe. Thus, you can use **1.0|2.0** as a value for **Fix Versions** to set multiple values.

## Action script

Enter the following Action script.

#### **Action script**

```text
string [] fvers = getElement(argv, 1);
string newAssignee = getElement(argv, 3);
string comment = getElement(argv, 5);

fixVersions = fvers;
assignee = newAssignee;
if(isNotNull(comment)){
	addComment(key, currentUser(), comment);
}
```