# unscheduleJob

## Description

Un-schedules a job.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | unscheduleJob(jobKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| jobKey | String | Yes | The job key. |

## Return Type

**None**

The returned value has no meaning.

## Example

```javascript
for(string jobKey in getScheduledJobKeys()){
    unscheduleJob(jobKey);
}
```

The SIL™ script above deletes all the scheduled jobs.

## See also