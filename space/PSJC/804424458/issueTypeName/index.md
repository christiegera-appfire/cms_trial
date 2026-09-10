# issueTypeName

## Description

Retrieves the issue type name for a given issue type.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueTypeName(name, description, defaultScreenSchemeId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueTypeId | int | Yes | Issue type id |

## Return Type

**string**

The return value is the name of the issue type.

## Example

```javascript
return issueTypeName(10034);
```

Result: Feature Request

## See also