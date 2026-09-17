# getIncomingEmail

## Description

Retrieves a structure containing information about the incoming email such as sender, recipients, subject, or body. As opposed to the server counterpart it does not receive any parameters, because you may process the original and the html body

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getIncomingEmail() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**IncomingEmail**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
IncomingEmail email = getIncomingEmail();
if(email.from != "jira-support@kepler-rominfo.com") {
	// create issue
}
```

## See also