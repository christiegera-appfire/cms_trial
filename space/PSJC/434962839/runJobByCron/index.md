# runJobByCron

## Description

Runs the job according to the specified cron schedule.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | runJobByCron(silFile, args, cronExpr) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| silFile | String | Yes | The sil file name. |
| args | array string | Yes | The list of the arguments of the job. |
| cronExpr | String | Yes | The cron expression |

## Return Type

**None**

The returned value has no meaning.

## Example

This SIL script will create a job that will run the script "script.sil" at 12pm (noon) every day.

```javascript
runJobByCron("script.sil", {project, key}, "0 0 12 * * ?");
```

In "script.sil" you can access the args using the next syntax:

```javascript
string issueKey = argv[1];
```

You can find more details about using the cron expression according to the used API at [www.quartz-scheduler.org/documentation/quartz-1.x/tutorials/crontrigger](http://www.quartz-scheduler.org/documentation/quartz-1.x/tutorials/crontrigger)

## See also