# getScheduledJobKeysByScript

## Description

Returns the list of scheduled jobs keys by the path of the script they use and the optional parameter args.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getScheduledJobKeysByScript(path[, args]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| path | String | Yes | The path of SIL file used by job. |
| args | array string | No | The list of the arguments of the job. |

## Return Type

**String []**

Returns the list of the scheduled jobs keys by the path of the script they use and the optional parameter args.

## Example

```javascript
string[] args = {issueType, project};
runnerLog("The jobs keys are : " + getScheduledJobKeys("test.sil", args));
```

The example above will return the list of all scheduled jobs keys that match the path and arguments provided.

## See also