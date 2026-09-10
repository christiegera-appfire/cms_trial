# BA_setExecuteButtonText

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_setExecuteButtonText(value) | **Package** | poweraction |
| **Alias** | form\_setExecuteButtonText | **Pkg Usage** | setExecuteButtonText(value) |

## Description

Overrides the default text on the dialog submit button. The last call of this routine will override any previous calls.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| value | String | Yes | The new text to show on the button. |

## Return Type

**None**

The returned value has no meaning.

## Example

```javascript
BA_createHtmlContent("Lorem ipsum");BA_setExecuteButtonText("Don't click!");
```

![Power Scripts for Jira Cloud execute button text configuration](/cms_trial/assets/be467c88-e6ea-493a-aa76-684d8fd30bb1.PNG)

## See also