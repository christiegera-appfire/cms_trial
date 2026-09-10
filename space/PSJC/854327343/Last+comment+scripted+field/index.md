# Last comment scripted field

## Problem

You want to show the last comment made on an issue as a custom field so that it will display in the issue results list or on an issue sidebar.

## Solution

### Display comment text only

```text
JComment lastComm = getLastComment(key);
return lastComm.text;
```

The field will display nothing if no comments have been made on the issue.

### Display comment text only with default for no comment

```text
JComment lastComm = getLastComment(key);

if(isNotNull(lastComm.author)) {
    return lastComm.text;
} else {
    return "No comment has been left on this issue.";
}
```

### Display the authors name followed by the comment text

```text
JComment lastComm = getLastComment(key);
return userKeyToDisplayName(lastComm.author) + ": " + lastComm.text;
```

Example output: `Jonathan Muse: I don’t understand why Jon always gets the last taco.`

### Display the authors name followed by comment date and text

```text
JComment lastComm = getLastComment(key);
return userKeyToDisplayName(lastComm.author) + + " (" + formatDate(lastComm.created, "MM-dd-yyyy") + "): " + lastComm.text;
```

Example output: `Jonathan Muse (03-25-2024): I don’t understand why Jon always gets the last taco.`