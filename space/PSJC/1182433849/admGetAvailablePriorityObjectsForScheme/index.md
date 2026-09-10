# admGetAvailablePriorityObjectsForScheme

## Description

Returns a list of priorities (as JPriority structures) available for adding to a given priority scheme.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetAvailablePriorityObjectsForScheme(prioritySchemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getAvailablePriorityObjectsForScheme(prioritySchemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| prioritySchemeName | string | Yes | The name of the priority scheme. |

## Return Type

[**JPriority []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the list of the priority names available to be added.

## Examples

### Example 1

Returns all the priorities that can be added to the scheme

```javascript
return admGetAvailablePriorityObjectsForScheme("New priority scheme");
```

Very Important|must be fixed|https://psc-atopoloaga.atlassian.net/iconH|#ff2320|false|10003|Not Important|doesn't matter|https://psc-atopoloaga.atlassian.net/nip|#008000|false

### Example 2

Returns all the priorities that can be added to the scheme

```javascript
JPriority[] availablePrioObjs = admGetAvailablePriorityObjectsForScheme("New priority scheme");
for (JPriority prio in availablePrioObjs) {
    runnerLog("status color for \" " + prio.name + "\" is " + prio.statusColor);
}
```

status color for " Very Important" is #ff2320
status color for " Not Important" is #008000

## See also