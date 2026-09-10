# admGetAllPriorityObjectsFromScheme

## Description

Returns the list of priorities (as JPriority structs) that exist in the given priority scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAllPriorityObjectsFromScheme(prioritySchemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getAllPriorityObjectsFromScheme(prioritySchemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| prioritySchemeName | string | Yes | The name of the priority scheme. |

## Return Type

[**JPriority []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the list of priorities.

## Examples

### Example 1

Returns all the priorities from scheme "Default priority scheme"

```javascript
return admGetAllPrioritiesFromScheme("Default priority scheme");
```

1|Highest|This problem will block progress.|https://psc-atopoloaga.atlassian.net/images/icons/priorities/highest.svg|#d04437|false|2|High|Serious problem that could block progress.|https://psc-atopoloaga.atlassian.net/images/icons/priorities/high.svg|#f15C75|false

### Example 2

Returns all the names and descriptions of priorities from scheme "Default priority scheme"

```javascript
JPriority[] priorities = admGetAllPrioritiesObjectsFromScheme("Default priority scheme");
for (JPriority priority in priorities) {
    string name = priority.name;
    runnerLog("name = " + name);
    string desc = priority.description;
    runnerLog("description = " + desc);
}
```

name = Highest
description = This problem will block progress.
name = High
description = Serious problem that could block progress.

## See also