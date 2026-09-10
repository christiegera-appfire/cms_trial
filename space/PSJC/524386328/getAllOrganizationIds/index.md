# getAllOrganizationIds

## Description

Returns the Ids of all Service Desk organizations.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getAllOrganizationIds() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**Number**

Returns a number array of organization Ids.

## Examples

### Example 1

```javascript
return getAllOrganizationIds();
```

Result: 11|12|13|14

### Example 2

```javascript
for(number id in getAllOrganizationIds()) {
    runnerLog(getOrganizationNameById(id));
}
```

Result: "Company A"
"Company B"
"Company C"

## See also