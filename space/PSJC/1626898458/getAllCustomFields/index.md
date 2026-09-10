# getAllCustomFields

## Description

Returns an array of JCustomField type structs for all custom fields in Jira.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllCustomFields() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**JCustomField []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns an array of custom fields.

## Example

```javascript
for(JCustomField cf in getAllCustomFields()) {
    runnerLog("ID: " + cf.id);
    runnerLog("Name: " + cf.name);
    runnerLog("Type: " + cf.type);}
```

## See also