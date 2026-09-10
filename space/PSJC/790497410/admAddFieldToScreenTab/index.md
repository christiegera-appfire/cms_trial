# admAddFieldToScreenTab

## Description

Adds a field to a certain tab on a screen. Returns true if field was added

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admAddFieldToScreenTab(screenId, tabId, fieldId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; addFieldToScreenTab(screenId, tabId, fieldId);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| screenId | int | Yes | The id of the screen. |
| tabId | int | Yes | The id of the screen tab. |
| fieldId | string | Yes | The id of the field, i.e. 'summary', 'customfield\_123456', etc. |

## Return Type

**boolean**

## See also