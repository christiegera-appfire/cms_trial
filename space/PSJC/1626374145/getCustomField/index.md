# getCustomField

## Description

Gets all information about the custom field. Routine returns a JCustomField structure type.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomField(customfieldId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| customfieldId | string or number | Yes | Id of the custom field to retrieve information for. |

## Return Type

[**JCustomField**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JCustomField field = getCustomField("customfield_12345");
runnerLog(field.id);
runnerLog(field.name);
runnerLog(field.type);
```

## See also