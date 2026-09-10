# isIssueFieldChanged

## Description

Verifies if the field was changed during the specific event.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isIssueFieldChanged() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**Boolean (true/false)**

Returns 'true' if the field was changed during the specific event, and 'false' otherwise.

## Example

```javascript
if(isIssueFieldChanged("description")) {
 logPrint("ERROR", "Event: Field 'description' IS CHANGED ");
}
else {
 logPrint("ERROR", "Event: Field 'description' IS NOT changed ");
}
```

```javascript
if(isIssueFieldChanged("description")) {
 logPrint("ERROR", "Event: Field 'description' IS CHANGED ");
}
else {
 logPrint("ERROR", "Event: Field 'description' IS NOT changed ");
}
```

## See also