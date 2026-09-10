# updateSprint

## Description

Used to modify the details and properties of an existing sprint. It allows for adjustments in sprint duration, goals, or other attributes.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | updateSprint(sprintId, name, [goal, [startDate, endDate]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sprintId | Integer | Yes | The sprint id |
| sprintName | String | Yes | The sprint name. Must have some value |
| goal | String | No | The sprint goal |
| startDate | date | No | The sprint start date |
| endDate | date | No | The sprint end date |

## Return Type

**Boolean**

Returns true if the sprint is updated.

## Examples

### Example 1

Simple name update.

```javascript
return updateSprint(12345, "New name for sprint");
```

Returns true if successful, false if otherwise.

### Example 2

Updates name and dates.

```javascript
return updateSprint(12345, "New name for sprint", "2025-01-01", "2025-01-14");
```

Returns true if successful, false if otherwise.

## See also