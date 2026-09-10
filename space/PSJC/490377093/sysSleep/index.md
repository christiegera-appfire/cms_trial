# sysSleep

## Description

Causes the current thread to sleep (suspends processing) for the specified interval. Do not use it in the UI processing (like synchronous workflow actions) otherwise users will be forced to wait.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sysSleep(interval) | **Package** | system |
| **Alias** |  | **Pkg Usage** | sleep(interval) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Interval | interval | Yes | Duration of time as interval. |

## Return Type

**None**

## Examples

### Example 1

```javascript
sysSleep("1s");
```

As a result the executing thread is suspended for 1 second.

### Example 2

Similar to the example above but uses the package.

```javascript
use "system";
sleep("10s");
```

As a result the executing thread is suspended for 10 seconds.

## See also