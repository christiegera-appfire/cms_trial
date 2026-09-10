# addJSDComment

## Description

Posts a comment on the specified issue. Returns a number representing the id of the comment.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addJSDComment(issue, comment [,isPublic]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue |
| comment | String | Yes | Comment that will be posted on the selected issue |
| isPublic | Boolean | No | true for public comment or false for internal comment, the default is true; |

## Return Type

**Number**

The returned number represents the id of the comment.

## Examples

### Example 1

Use the following code to add a **public** comment to the current issue.

```javascript
addJSDComment(key, "I have executed a transition.");
```

The same can also be achieved with the following script:

```javascript
addJSDComment(key, "I have executed a transition.", true);
```

### Example 2

Use the following code to add an **internal** comment to the current issue.

```javascript
addJSDComment(key, "you can't see me", false);
```

## See also