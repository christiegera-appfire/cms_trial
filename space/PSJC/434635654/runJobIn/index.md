# runJobIn

## Description

Runs a job in a specified interval.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | runJobIn(silFile, args, interval) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| silFile | String | Yes | The sil file name. |
| args | array string | Yes | The list of the arguments of the job. |
| interval | int | Yes | The interval |

## Return Type

**None**

The returned value has no meaning.

## Example

This example will create a job that will run the script "script.sil" after 30 minutes. (the script will run only once)

```javascript
string[] args = {key, project}; //assume we're in the context of an issue
interval varInterval = "30m";
runJobIn("script.sil", args, varInterval);
```

In "script.sil" you can access the args using the next syntax:

```javascript
string issueKey = argv[0];
```

## See also