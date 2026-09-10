# admMoveFieldLastInTab

## Description

Moves a field from a certain tab on the last position. Returns true if field was moved

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admMoveFieldLastInTab(screenId, tabId, fieldId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; moveFieldLastInTab(screenId, tabId, fieldId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| screenId | int | Yes | The id of the screen. |
| tabId | int | Yes | The id of the screen tab. |
| fieldId | string | Yes | The id of the field, i.e. 'summary', 'customfield\_123456', etc. |

## Return Type

**boolean**

## See also