# Persistent variables in Issue context

Persistent variables are introduced via the **persistent** keyword. In order to save space, we do not allow **persistent** and [**constant**](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/) modifiers to be used on the same variable, so you can't have both. A persistent variable is always modifiable.

## Using Persistent Variables

Let's install the following action on an easy executable action (like "Start Progress" on the default simplified workflow of Jira), and execute the transition a number of times (a normal Start-Stop progress cycle, in this example, on the same issue).

#### **An action with persistent variables**

```java
persistent number counter = 1; 
persistent boolean flag = false; 
 
description += "\n" + counter + "(" + flag + ")"; 
 
flag = !flag; 
 
counter ++;
```

The above example adds some text to the description of an issue, but unlike the version without the persistent keyword, the appended text will be something like:

```text
1(false)
2(true)
3(false)
4(true)
```

So what's happening here? The truth is that the initialization of the variable happens only once. Subsequent executions will find the persistent variable initialized, will load that particular value, and start from there. The flag will be flipped, and the counter will be incremented with each executed transition on that issue.

The persistent variable is linked to the issue so that If you move to another issue and execute the same action multiple times, you will get a similar output. The first line of the output will still be *1(false)* followed by *2(true)* and so on.

## Examples

Let's suppose that we have a SIL™ listener and we'd like to use that counter variable. You can simply access it in your listener like in the following example:

#### **A listener code**

```java
persistent number counter;
persistent boolean flag = true; //initialization is ignored if the previous script was already executed!
//.............
/// use it in the listener like a normal variable:
counter--;
```

Note that we didn't put any initializer. If the variable is already initialized, the initializer is simply not executed at all, no matter the construct. While such behavior belongs to the logic of the persistent variable, we recommend that you use the same initializer every time so that you won't start with different values.

**See More**

## Recommended ✅

### Script 1

```text
persistent number counter = 1;
persistent boolean flag = true;
...
```

### Script 2

```text
persistent number counter = 1;
persistent boolean flag = true;
...
```

### Script 3

```text
persistent number counter = 1;
persistent boolean flag = true;
...
```

## NOT Recommended ❌

### Script 1

```text
persistent number counter = 1;
persistent boolean flag = true;
...
```

### Script 2

```text
persistent number counter = 100;
persistent boolean flag = false;
...
```

### Script 3

```text
persistent number counter = 7;
persistent boolean flag = true;
...
```

## In Conclusion:

1. The persistent variable is linked to the current issue from the context.
2. Persistent variables are only initialized once. Initialization of a persistent variable will be ignored if that variable was already initialized from a previous execution within a particular context.
3. A persistent variable is a variable whose value survives the script, making it available in many other scripts under the same name.

## Use Case Examples

## Approvals

Let's say you want to create an approval process where a manager must approve a ticket before it can be worked on. This can be accomplished by creating a workflow transition, called "Approve",  that leads back to the original step. Only a manager can see this transition button and when they transition the ticket it will be marked as approved. To do this we would need a couple scripts on this Approval transition:

### **Condition Script:**

```java
//This condition script hides the transition if the user is not a manager or if the issue has already been approved
persistent boolean approved = false;

if(approved == true or userInGroup("managers", currentUser() == false) {
	return false;
}
```

### **Post Function Script:**

```java
//This action script marks the issue as approved using a persistant variable
persistent boolean approved = false;

approved = true;
```

This validator script would go on the "Start Progress" transition, for example.

### **Validator Script:**

```java
//This validator script prevents the user from starting work on the issue until it has been approved
persistent boolean approved;
string errMsg = "You can not perform this action because this ticket has not been approved by a manager";

if(approved != true) {
	return false, "", errMsg;
}
```