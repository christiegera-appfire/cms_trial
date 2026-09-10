# logPrint

## Description

Prints a message in the configured Jira logs on the specified level: **TRACE, DEBUG, INFO, WARN, ERROR, FATAL**. Logging the messages above is subject to the same configurations of the app as described here.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | logPrint(logLevel, message) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| logLevel | String | Yes | Minimum level for logging the message is written for. |
| message | String | Yes | Argument converted to a string that will be printed. |

## Return Type

**None**

## Example

```javascript
logPrint("DEBUG", "A debug Message.");
```

If the configuration level is one of **TRACE** or **DEBUG** then the message will be printed out. Otherwise if the configuration level is **INFO, WARN, ERROR** or **FATAL** the message will not be displayed. For other usages you can consult the priority level list above.

To configure the **Jira Logging level** do this in two ways:

**Temporarily**  - the logging level will be reset after Jira reboot:

1. Log in Jira using an administrator account.
2. Go to **Administration** .
3. Go to **System**  tab and select the **Troubleshooting and Support**  option.
4. Select the **Logging & Profiling**  tab.
5. Find the **Default Loggers**  paragraph with package names and their **Logging level** .
6. Search in this list for the line **com.keplerrominfo** . And select from the **Set Logging Level**  your desired level.

**Permanently**  - the logging level will **NOT**  be reset after Jira reboot, described here: [Configure Jira logging](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=Configure%20Jira%20logging&linkCreation=true&fromPageId=434733369).

## See also