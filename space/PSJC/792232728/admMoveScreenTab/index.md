# admMoveScreenTab

## Description

Moves a screen tab to a given position, zero-based. Returns true if move was performed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admMoveScreenTab(screenId, tabId, position) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | [use adm; moveScreenTab(screenId, tabId, position);] |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| screenId | int | Yes | The id of the screen. |
| tabId | int | Yes | The id of the screen tab to be moved. |
| position | int | Yes | The new position. Zero means first |

## Return Type

**boolean**

## See also