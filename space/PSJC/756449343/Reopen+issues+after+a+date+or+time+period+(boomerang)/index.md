# Reopen issues after a date or time period (boomerang)

## Problem

Sometimes a task is not really complete and needs to be followed up on at a later time. Leaving the issue open as reminder can create a mess on reports and in backlogs and does not necessarily work effectively.

## Solution

A solution would be to close the ticket with some added information. For example, a transition screen can be added where the user can enter a date or a time period that should indicate when the issue should be reopened.

### Writing the code

The following script will reopen the issue on a specified date.

```java
//the transition id's are needed by the autoTransition() function
string [] transitionIds;
transitionIds["Bug"] = "11";
transitionIds["Task"] = "21";
transitionIds["Story"] = "31";

for(string pkey in argv) {
    //the following JQL query is responsible for selecting the issues that are ready to be reopened
    string JQL = "project = " + pkey + " AND type in (Bug, Task, Story) AND statusCategory = Done AND \"Reopen Date\" <= startOfDay()";
    
    //select issues using JQL and loop through them
    for(string i in selectIssues(JQL, 500)) {
        autotransition(transitionIds[i.type], i); //reopen the issue
        addComment(i, currentUser(), "This issue has been automagically reopened because it has reached the reopen date previouslly assigned."); //add comment explaining why the issue was reopened
        %i%.priority = "High"; //increase the priority assuming it is not already high
    }
}
```

The above script can also be modified to work with an interval. So, instead of the user specifying that the issue should be reopened on November 12th, the user could tell the script to reopen in 90 days. In this case, a custom field would be used and the user would enter an interval value similar to tracking time. So the user would enter “90d” to represent 90 days.

```text
//the transition id's are needed by the autoTransition() function
string [] transitionIds;
transitionIds["Bug"] = "11";
transitionIds["Task"] = "21";
transitionIds["Story"] = "31";

for(string pkey in argv) {
    //the following JQL query is responsible for selecting the issues that are ready to be reopened
    string JQL = "project = " + pkey + " AND type in (Bug, Task, Story) AND statusCategory = Done AND \"Reopen After Period\" is not EMPTY";

    //select issues using JQL and loop through them
    for(string i in selectIssues(JQL, 500)) {
        //calculate the reopen date
        date reopenDate = i.resolutionDate + i.reopenPeriod;
        if(currentDate <= reopenDate) {
            autotransition(transitionIds[i.type], i); //reopen the issue
            addComment(i, currentUser(), "This issue has been automagically reopened because it has reached the reopen date previouslly assigned."); //add comment explaining why the issue was reopened
            %i%.priority = "High"; //increase the priority assuming it is not already high
        }
    }
}
```

NOTE: This script can be modified so that it **clones** the closed issue instead of reopening it. To do this the line of code that uses the autoTransition() function (lines 13 and 16) would be replace with code that would use the [createIssue()](/cms_trial/space/PSJC/434507110/createIssue/) function.

### Configuring the script to run

This script is designed to be run periodically using the [SIL Scheduler](/cms_trial/space/PSJC/490998807/SIL+Scheduler/). The script can be configured to run daily using an interval (as shown below) or can be configured with more granular control using a CRON schedule. An easy way to create the CRON schedule is to use a tool like [www.cronmaker.com](http://www.cronmaker.com).

![Power Scripts for Jira Cloud trace enablement settings](/cms_trial/assets/12461fb0-66cd-4840-9614-dac39e500605.png)

Notice the arguments being passed to the script. These represent the project keys that they script should scan for issues that need to be reopened. The script is designed to loop through these project keys are search through the issues one-by-one. This can be seen in line 7 in each of the scripts. For more information on how to use the argv variable to pass arguments see [this page](/cms_trial/space/PSJC/756252819/Arguments+(argv+variable)/).