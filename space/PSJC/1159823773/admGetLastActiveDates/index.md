# admGetLastActiveDates

## Description

Returns a JLastActiveDates structure containing information about last active dates of the user on different products.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetLastActiveDates(accountId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | lastActiveDates(accountId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| accountId | string | Yes | The account Id of the user to be queried. |

## Return Type

[**JLastActiveDates**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the last active dates of the user.

## Example

```javascript
JLastActiveDates lastActive =  admGetLastActiveDates(currentUser());
int indexCC = 1;
for(JProductLastActiveDate plad in lastActive.productLastActiveDates) {
    runnerLog("---productLastActiveDate " + indexCC + "---");   
    runnerLog("product = " + plad.product);
    runnerLog("lastActive = " + plad.lastActive);
    indexCC++;
}
runnerLog("--------------");
runnerLog("addedToOrganization = " + lastActive.addedToOrganization);
```

## See also