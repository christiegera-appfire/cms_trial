# runJobAt

## Description

Runs a job at the specified date.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | runJobAt(silFile, args, date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| silFile | String | Yes | The sil file name. |
| args | array string | Yes | The list of the arguments of the job. |
| date | Date | Yes | The date-time you wish the job to run. Must be in the future |

## Return Type

**None**

The returned value has no meaning.

## Example

This example will create a job that will run the sil script at the date specified.

```javascript
date varDate = "2015-08-20T18:30:55";
runJobAt("script.sil", {project, key}, varDate);
```

In "script.sil" you can access the args using the next syntax:

```javascript
string issueKey = argv[1];
```

## See also