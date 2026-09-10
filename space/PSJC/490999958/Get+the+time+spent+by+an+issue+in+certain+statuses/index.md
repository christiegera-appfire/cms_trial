# Get the time spent by an issue in certain statuses

## Problem

You want to measure the amount of time an issue spent in certain statuses.

## Solution

**Writing the code**

The following SIL™ code does all the magic:

```text
function getStatusesTimeSpent(string issueKey) {
    // function that returns a map with key status and value total time spent
    interval[] result;
    string[] statusHistory = fieldHistory(issueKey, "status");
    
    date oldDate = %issueKey%.created;
    if(!size(statusHistory) > 0) {
        //status never changed
        result[%issueKey%.status] = currentDate() - oldDate;
        return result;
    }
    
    string oldStatus = statusHistory[1];
    interval timeSpent = 0;
    
    for(number i = 3; i < size(statusHistory); i += 2) {
        string newStatus = statusHistory[i];
        date newDate = statusHistory[i-1];
        timeSpent = newDate - oldDate;
        if(isNotNull(result[oldStatus])) {
            // if issue already was in this status add the time interval to the time spent
            result[oldStatus] = result[oldStatus] + timeSpent;
        } else {
            // otherwise set the time spent for this status
            result[oldStatus] = timeSpent;
        }
        oldStatus = newStatus;
        oldDate = newDate;
    }
    //add also last status time interval
    interval lastTime = currentDate() - oldDate; 
    if(isNotNull(result[oldStatus])) {
        result[oldStatus] = result[oldStatus] + lastTime;
    } else {
        result[oldStatus] = lastTime;
    }
    
    return result;
}
```

You then just have to call getStatusesTimeSpent function, giving the desired issue key as parameter and you will get an array containing all statuses in which the issue was, as well as the total time spent for each status:

```text
string[] timeSpentInStatuses = getStatusesTimeSpent("DEMO-1");
return timeSpentInStatuses[1]; // will return a time interval spent in status "Open" for issue "DEMO-1"
```

Note that you can access time spent for each status only by its id.

You can see the corresponding ids for your statuses either by looking directly into the jira database, in the issuestatus table, either from the Status administration section in Jira, by hovering over the edit link of each status and see the id parameter in the corresponding url.