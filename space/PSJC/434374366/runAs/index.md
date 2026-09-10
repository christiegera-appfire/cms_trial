# runAs

## Description

Assumes a user when running a script.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | runAs(user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| User | String | Yes | Username of userkey of the selected user. |

## Return Type

**None**

## Example

```javascript
runAs("user1");
 print(currentDate());
 print(currentUser());
 runAs("admin");
```

The output in the console will be following:  
2012 -06 -20 13: 39: 31, 629 pool -5 -thread -2 **INFO user1** 819x261x1 1k7wpbj 127.0.0.1 /rest/keplerrominfo/jjupin/latest/rungadget/run[commons.sil.functions.StringPrintFunction] 2012-06-20 13:39:31  
2012-06-20 13:39:31, 629 pool-5-thread 2 **INFO user1** 819x261x1 1k7wpbj 127.0.0.1 /rest/keplerrominfo/jjupin/latest/rungadget/run[commons.sil.functions.StringPrintFunction] user1

The look-up is first made after the userkey, then after the username.

## See also