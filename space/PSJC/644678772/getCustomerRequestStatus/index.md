# getCustomerRequestStatus

## Description

Returns a list of JSMCustomerRequestStatus structures, containing all the statuses in which the request was

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomerRequestStatus(requestId\_or\_Key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The key or id of the selected request. |

## Return Type

[**JSMCustomerRequestStatus[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JSMCustomerRequestStatus[] customerRequestCurrentStatuses = getCustomerRequestStatus("SM-1");
int indexCC = 1;
for(JSMCustomerRequestStatus customerRequestStatus in customerRequestCurrentStatuses) {
    runnerLog("---customerRequestStatus " + indexCC + "---");    
    runnerLog("status = " + customerRequestStatus.status);
    runnerLog("statusCategory = " + customerRequestStatus.statusCategory);
    runnerLog("statusDate = " + customerRequestStatus.statusDate);    
    indexCC = indexCC + 1;
}
```

Returns a list of JSMCustomerRequestStatus structures for the request "SM-1"

## See also