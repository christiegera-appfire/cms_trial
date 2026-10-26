# getRequestParticipants

## Description

Returns a string array of request participants keys.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getRequestParticipants(requestId\_or\_Key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The key or id of the selected request. |

## Return Type

**String**

## Example

```javascript
return getRequestParticipants("JSD-10");
```

Returns the string array of request participants keys.

## See also