# admMoveFieldRelativeInTab

## Description

Moves a field from a certain tab on the position following the specified field. Returns true if field was moved

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admMoveFieldRelativeInTab(screenId, tabId, fieldId, afterFieldId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; moveFieldRelativeInTab(screenId, tabId, fieldId, afterFieldId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| screenId | int | Yes | The id of the screen. |
| tabId | int | Yes | The id of the screen tab. |
| fieldId | string | Yes | The id of the field, i.e. 'summary', 'customfield\_123456', etc. |
| afterFieldId | string | Yes | The id of the field used as relative position, i.e. 'summary', 'customfield\_123456', etc. |

## Return Type

**boolean**

## See also