# getUserOrganizations

## Description

Gets organizations names in which the user is present.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getUserOrganizations(userAccountId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| userAccountId | string | Yes | The account id of the user for which we'll retrieve the organizations. |

## Return Type

**String []**

Returns all the organizations names in which the user is present.

## Example

### Example 1

```javascript
return getUserOrganizations(currentUser());
```

## See also