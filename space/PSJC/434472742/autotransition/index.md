# autotransition

## Description

Executes a transition and moves to the specified step. It will execute the transition only if the transition is valid for the current status of the issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | autotransition(transition, issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| transition | String | Yes | Id of the transition that will be executed. |
| issuekey | String | Yes | Key of the issue the transition will be executed for. |

## Return Type

**Boolean (true/false)**

If the return value is "true", the transition was executed successfully. A "false" return value means that the transition failed. In this case check the log for additional details.

## Examples

### Example 1

```javascript
autotransition(121, "PRJ-123");
```

Returns "true" if the transition with the **ID=121** for the issue **PRJ-123** was executed and "false" if the transition wasn't executed.

### Example 2

```javascript
autotransition("Require information", "PRJ-232");
```

Returns "true" if the transition requirng information for the issue **PRJ-232** was executed and "false" if the transition wasn't executed.

1. To use the function on the **Create Issue** transition, it is very important that you place the SIL action (post function) **after** the "Creates the issue originally" action but **before** "Fire a Issue Created event that can be processed by the listeners.". Positioning the SIL™ action otherwise will de-synchronize the issue from the workflow. That will set an invalid status for the workflow step it is in.
2. If the transition requires a screen it will not be displayed for additional input.
3. You should do all issue modifications in or before the action that contains the calling of the auto transition.
4. All actions executed by the called transitions should not modify the issue. These actions could be used for sending notifications.
5. If there are validations and /or conditions in the transition called after the one that contains the auto transition, and these validations fail, the transition will not be executed.

## See also