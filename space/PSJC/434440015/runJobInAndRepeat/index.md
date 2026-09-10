# runJobInAndRepeat

## Description

Runs a job every specified interval.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | runJobInAndRepeat(silFile, args, interval) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| scriptPath | String | Yes | The source of the script to be executed. |
| args | array string | Yes | The list of the arguments of the job. |
| interval | int | Yes | The interval |

## Return Type

**None**

The returned value has no meaning.

## Example

This example creates a job that runs the script "script.sil" every 30 minutes. The job running will repeat every 30 minutes.

```javascript
string[] args = {key, project};
interval varInterval = "30m";
runJobInAndRepeat("script.sil", args, varInterval);
```

For the **scriptPath** parameter you can either give the relative path (as in the example above), or the absolute path: **C:/Program Files/Atlassian/Application Data/JIRA/silprograms/script.sil**.

In "script.sil" you can access the args using the next syntax:

```javascript
string issueKey = argv[0];
```

## See also