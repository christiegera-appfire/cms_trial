# refreshIssue

## Description

Refreshes the issue in the interpreter. Issue MUST not be modified in the current script. Returns true if the issue is refreshed (reloaded from Jira). Use it only in certain cases, as it may cause unnecessary slowness

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | refreshIssue(key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | string | Yes | Issue key. |

## Return Type

**boolean**

Returns true if the issue is refreshed, false if not.

## Example

Assuming customfield\_12345 is always asynchronously set by another addon...

```javascript
string k = "THEPRJ-666";
while(%k%.customfield_12345 == null) {
 refreshIssue(k);
}
```

Issue is refreshed, careful usage is advised

## See also