# lastExceptionMessage

## Description

Retrieves the message from of the last error exception thrown.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | lastExceptionMessage() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**String**

## Example

```javascript
try {
    runAs("user_that_does_not_exist");
} catch string err {
     // will not catch error here
} catch {
    runnerLog("Class:" + lastExceptionClass());
     runnerLog("Message:" + lastExceptionMessage());
}
```

Output is contents of last error message similar to below:

```javascript
Class: com.keplerrominfo.sil.lang.SILInfoException
Message: [SIL Error on line: 2, column: 9] User user_that_does_not_exist does not exist.
```

## See also