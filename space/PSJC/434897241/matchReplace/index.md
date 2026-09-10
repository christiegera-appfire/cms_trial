# matchReplace

## Description

Uses a regex expression to find and replace text within a string.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | matchReplace(source, target, replacement) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| source | String | Yes | Text string to be updated. |
| target | String | Yes | Regex expression used to target text for replacement. |
| replacement | String | Yes | Replacement text used to update the target text found by the regex expression. |

## Return Type

**String**

## Examples

### Example 1

```javascript
Oh, you are a Nigerian prince? Here is my credit card number 1111-2222-3333-4444.
matchReplace(sourceText, "\d{4}-?\d{4}-?\d{4}-?\d{4}", "XXXX-XXXX-XXXX-XXXX");
```

Returns: "Oh, you are a Nigerian prince? Here is my credit card number XXXX-XXXX-XXXX-XXXX."

### Example 2

```javascript
string HTML = "<p>Geckos are a group of usually small, usually <strong style='color: blue;'>nocturnal</strong> lizards. They are found on every continent except Australia.</p>
return matchReplace(HTML, "<[^>]*>", "");
```

Returns: Geckos are a group of usually small, usually nocturnal lizards. They are found on every continent except Australia.

## See also