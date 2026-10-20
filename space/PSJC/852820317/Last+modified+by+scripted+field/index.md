# Last modified by scripted field

## Problem

You would like to display the name of the last person to update an issue in a custom field.

## Solution

```text
JFieldChange [] changes = lastIssueChanges(key);
return userKeyToDisplayName(changes[size(changes)-1].user);
```