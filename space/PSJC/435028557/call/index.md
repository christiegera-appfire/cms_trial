# call

## Description

Executes SIL script on the current host or different host. If sysname is equal to "local" or is empty "" it will execute the script on the current Jira server. The execution will automatically define a variable named 'argv' that will contain the parameters, as a string array. You can use return to return values back to the caller. A string array only. If the call is local, current issue is available. If the call is a remote call, the current context is lost as issue variables will have no meaning.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | call(sysname, silprogrampath, arguments) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| sysname | String | Yes | System name. The local system, Jira server machine, is identified by an empty string "" or by the string "local". For remote systems, it should contain the system name, as configured in the configuration page. |
| silprogrampath | String | Yes | Full path to the program being run. Absolute path, for instance "/opt/jira/home/silprograms/myprogram.sil" or "C:/Atlassian/Jira/Home/silprograms/myprogram.sil". |
| arguments | String [] | Yes | The arguments, as an array of strings. |

## Return Type

**String []**

The return from the script, as an array of strings. Values that are returned using the **return** keyword.

## Examples

```javascript
//Local script, placed in a postfunction (for instance):
string [] arrp = "param1|param2";
string [] rec;
call("", "/tmp/printme.sil", arrp); //local call
rec = call("system_remote", "c:/testme.sil", arrp); //remote call
if(isNotNull(rec)) {
  //The following code prints: "Hello", "from", "remote", "jjupin"
  for(string s in rec) {
    print(s);
  }
}
```

```javascript
//This is the remote SIl script placed in the c:/testme.sil:
string p = "Hello world!";
print("Remote called P is " + p + " Parameter at index 1 is=" + arrayGetElement(argv, 1));
return "Hello", "from", "remote", "jjupin";
```

Resolution of the remote system goes as following, as you may define the same name for a remote system in multiple places:

1. If the name of the system is empty ('') or the string 'local' it will call a local script.
2. Find the name of the system as defined by REST. If it is defined, it calls the REST remote system.
3. If it is not defined, fallback on SOAP.
4. If it is still not defined, error will appear.

For remote calls, you need additional steps (see the configuration manual).
Windows: We recommend you to use forward slashes "/" in paths instead of "\" since it will simplify your life.  
  
To configure the [Remote systems](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=Remote%20systems&linkCreation=true&fromPageId=435028557) see the configuration page.

## See also