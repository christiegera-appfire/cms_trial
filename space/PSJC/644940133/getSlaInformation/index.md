# getSlaInformation

## Description

Gets SLA information for the specified issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getSlaInformation(issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The key of the selected issue. |

## Return Type

[**JSlaInformation []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a list of JSlaInformation.

## Example

```javascript
JSlaInformation[] slaInfos = getSlaInformation("JSD-10");
for(JSlaInformation slaInfo in slaInfos) {
    runnerLog("slaInfoName = " + slaInfo.name);
    JSlaOngoingCycle slaOC = slaInfo.ongoingCycle;
    runnerLog("---ongoingCycle---");
    runnerLog("startTime = " + slaOC.startTime);    
    runnerLog("breachTime = " + slaOC.breachTime);    
    runnerLog("breached = " + slaOC.breached);    
    runnerLog("paused = " + slaOC.paused);    
    runnerLog("withinCalendarHours = " + slaOC.withinCalendarHours);    
    runnerLog("goalDuration = " + slaOC.goalDuration);    
    runnerLog("elapsedTime = " + slaOC.elapsedTime);    
    runnerLog("remainingTime = " + slaOC.remainingTime);    
    int indexCC = 1;
    for(JSlaCompletedCycle slaCC in slaInfo.completedCycles) {
        runnerLog("---completedCycle " + indexCC + "---");    
        runnerLog("startTime = " + slaCC.startTime);    
        runnerLog("stopTime = " + slaCC.stopTime);    
        runnerLog("breached = " + slaCC.breached);    
        runnerLog("goalDuration = " + slaCC.goalDuration);    
        runnerLog("elapsedTime = " + slaCC.elapsedTime);    
        runnerLog("remainingTime = " + slaCC.remainingTime);    
        indexCC = indexCC + 1;
    }
    runnerLog("_________________________________________________");
}
```

## See also