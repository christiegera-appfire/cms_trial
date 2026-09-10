# Time of last transition

## Problem

You want to show the time the last transition was made on an issue show it appears in the list of search results or a dashboard.

## Solution

```text
string [] changes = fieldHistory(key, "status");

if(size(changes) > 0) {
    date lastChange = changes[size(changes)-2];
    return formatDate(toTimeZone(lastChange, "GMT-5"), "h:mm a");
}
```

Example output: `2:17 PM`