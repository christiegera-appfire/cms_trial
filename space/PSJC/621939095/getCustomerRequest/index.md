# getCustomerRequest

## Description

Returns a customer request structure

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomerRequest(requestId\_or\_Key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request to be returned |

## Return Type

[**JSMCustomerRequest**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
return getCustomerRequest("SM-1");
```

Returns a customer request structure.

## See also