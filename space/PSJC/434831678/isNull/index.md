# isNull

## Description

Checks if the provided variable is null or has no value associated then returns "true", otherwise returns "false".

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isNull(variable) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| variable | Any | Yes | Value you want to test. Value argument can be a string or a variable of any type. |

## Return Type

**Boolean (true/false)**

## Examples

### Example 1

Checks whether the assignee was selected for a ticket.

```javascript
if(isNull(assignee)) {
  assignee = reporter;
}
```

### Example 2

The following line checks whether the **Time Spent** field contains any work logged on the ticket.

```javascript
if(isNull(assignee)) {
  assignee = reporter;
}
```

You can also use the [hasInput](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=hasInput&linkCreation=true&fromPageId=434831678) function to check whether certain fields were filled out during a workflow transition. And among those fields you can also check the work logged in particular.

If **isNull** returns "true" the variable has no value attached. **isNull** returns "false" for **zero** for numeric variables or **blank** for character/string.

## See also