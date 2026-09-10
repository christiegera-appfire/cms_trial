# saveModifiedIssues

## Description

Saves all modified issues. Clears the memory while doing so. Typical usage are in for / while loops, to help you process a lot more data.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | saveModifiedIssues() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**boolean**

Returns true if all modified issues are saved.

## Example

A typical usage example involves loading a lot of issues but saving them from time to time

```javascript
int i = 0;
for(string k in selectIssues("project = TEST and issueType = Story", 1000)) {
    i++;
    %k%.description += "\n\nmodified"; //modify here the issues
    if(i % 10 == 0) {
        saveModifiedIssues(); //every 10 issues we save
    }
}
```

## See also