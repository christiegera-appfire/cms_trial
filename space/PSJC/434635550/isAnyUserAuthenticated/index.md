# isAnyUserAuthenticated

## Description

Verifies if there is a logged in user.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isAnyUserAuthenticated() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**Boolean**

A "true" return value means that there is a logged in user.

## Example

```javascript
if (isAnyUserAuthenticated()) {
     print(currentDate());
 }
```

Result: It will print the current date. If there is nobody logged in, the current date will not be printed.  
2012-06-20 13:39:31,629 pool-5-thread-2 INFO admin 819x261x1 1k7wpbj 127.0.0.1 /rest/keplerrominfo/jjupin/latest/rungadget/run [commons.sil.functions.StringPrintFunction] 2012-06-20 13:39:31

## See also