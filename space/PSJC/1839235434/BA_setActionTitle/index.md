# BA_setActionTitle

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | BA\_setActionTitle(value) | **Package** | poweraction |
| **Alias** | form\_setActionTitle | **Pkg Usage** | setActionTitle(value) |

## Description

Overrides the default dialog title. The last call of this routine will override any previous calls.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| value | String | Yes | The new action title. |

## Return Type

**None**

The returned value has no meaning.

## Example

```javascript
BA_createHtmlContent("Lorem ipsum");
BA_setActionTitle("New Title");
```

![Power Scripts for Jira Cloud action title configuration dialog](/cms_trial/assets/e307776e-662e-4050-8f06-d16568821b64.PNG)

## See also