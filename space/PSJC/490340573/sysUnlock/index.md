# sysUnlock

## Description

Removes a named lock. If you forget to call it, all locks will be cleared at the termination of the script.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sysUnlock(lockKey) | **Package** | system |
| **Alias** |  | **Pkg Usage** | unlock(lockKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| lockKey | String | Yes | The lockKey is the issue key (Jira) or page id (Confluence), or any unique string to give the lock name. |

## Return Type

**None**

## Examples

### Example 1

```javascript
sysUnlock("TEST-123");
```

The lock named 'TEST-123' is now released and may be acquired by other SIL scripts which are now doing sysLock() on the same key.

### Example 2

Similar to the example above but uses the package.

```javascript
use "system";
unlock("TEST-123");
```

The lock named 'TEST-123' is now released and may be acquired by other SIL scripts which are now doing sysLock() on the same key.

## See also