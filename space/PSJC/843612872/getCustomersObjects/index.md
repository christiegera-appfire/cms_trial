# getCustomersObjects

[Unmapped macro: button-handy — no content to fall back on]

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getCustomersObjects(serviceDeskId[, displayNameOrNameOrEmail]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Description

Returns an array of JUser structures

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| serviceDeskId | number | Yes | The ID of the service desk for which the customers will be retrieved |
| displayNameOrNameOrEmail | string | No | A string that fully or partially describes a customer's name, or display name, or email - used for filter the customers |

## Return Type

[**JUser[]**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Examples

### Example 1

```text
return getCustomersObjects(1);
```

Returns an array of JUser structures.

### Example 2

Returns an array of JUser structures, filtered by their name, display name or email using the string "John".

```text
return getCustomersObjects(1, "John");
```

## See also

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]