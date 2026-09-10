# Persistent variables outside the Issue context

The usage outside the issue context is very similar. However, due to the nature of the persistent keyword, the variable, in this case, becomes a global variable. Take for instance the following script, run from the SIL™ Runner gadget:

```java
persistent number counter = 1; 
persistent boolean flag = false; 
 
TEST-1.description += "\n" + counter + "(" + flag + ")"; 
 
flag = !flag; 
 
counter ++;
```

The **counter** variable will be incremented as before (starting from 1) and the text above will be re-appended to the issue 'TEST-1'. However, if we change just the issue, say to 'TEST-2', the counter will retain its previous value, incrementing from the value it stopped when you run the above for the TEST-1 issue. Just try it!

Persistent variables are effectively global if used outside of the issue context.

## Example Use Cases

## Stored Passwords

It is not a good practice to have passwords stored in your script. One way to achieve this is to store the password in a persistent variable. To create the password as global variable run the following script once through the [SIL Runner Gadget](/cms_trial/space/PSJC/490998687/Using+SIL+Runner+Gadget/) or the SIL Scheduler:

```java
persistent string apiPassword = "password132";
```

Then, in a script where the password is required, you can retrieve the value using the [getPersistentVar()](/cms_trial/space/PSJC/433000833/getPersistentVar/) function.

```java
HttpRequest request;
HttpHeader authHeader = httpBasicAuthHeader("admin", getPersistentVar("apiPassword"));
request.headers += authHeader;
...
```

## File Path

If you commonly use functions that require the full file path of a file you can save yourself a step by storing the root file path as a persistent variable. To create the password as global variable run the following script once through the [SIL Runner Gadget](/cms_trial/space/PSJC/490996338/SIL+Runner+Gadget+configuration/) or the SIL Scheduler:

```java
persistent string rootPath = "/var/atlassian/application-data/jira/";
```

Then, in your script, you can retrieve the value.

```java
string path = getPersistentVar("rootPath") + "silprograms/calls/test.sil";
```