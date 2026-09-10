# sysLock

## Description

Creates a named lock. Scripts using the same lock key will be blocked and wait for the current script to release the lock.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sysLock(lockKey) | **Package** | system |
| **Alias** |  | **Pkg Usage** | lock(lockKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| lockKey | String | Yes | The lockKey is the issue key (Jira) or page id (Confluence), or any unique string to give the lock name. |

## Return Type

**None**

## Examples

### Example 1

```javascript
sysLock("TEST-123");
```

The lock TEST-123 is now created and can not be acquired by other SIL scripts calling sysLock with the same lock key, in this case 'TEST-123'.

### Example 2

Similar to the example above but uses the package.

```javascript
use "system";
lock("TEST-123");
```

The lock TEST-123 is now created and can not be acquired by other SIL scripts calling sysLock with the same lock key, in this case 'TEST-123'.

## See also