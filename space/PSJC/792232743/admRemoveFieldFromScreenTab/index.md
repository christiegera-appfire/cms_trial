# admRemoveFieldFromScreenTab

## Description

Removes a field from a certain tab on a screen. Returns true if field was removed

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveFieldFromScreenTab(screenId, tabId, fieldId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; removeFieldFromScreenTab(screenId, tabId, fieldId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| screenId | int | Yes | The id of the screen. |
| tabId | int | Yes | The id of the screen tab. |
| fieldId | string | Yes | The id of the field, i.e. 'summary', 'customfield\_123456', etc. |

## Return Type

**boolean**

## See also