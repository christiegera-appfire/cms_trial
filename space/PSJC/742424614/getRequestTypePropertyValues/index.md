# getRequestTypePropertyValues

## Description

Gets a list of property keys for the specified request type from the provided service desk.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getRequestTypePropertyValues(serviceDeskId, requestTypeId, propertyKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The servicedesk id for which to retrieve the properties. |
| requestTypeId | number | Yes | The request type id for which to retrieve the properties. |
| propertyKey | string | Yes | The name of the property for which we'll get the values. |

## Return Type

**string[]**

## Example

```javascript
return getRequestTypePropertyValues(1, 2, "propKey");
```

Returns: "value1|val2|test3"

## See also