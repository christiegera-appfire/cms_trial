# sendHtmlEmail

## Description

Sends an email, HTML formatted. **To** and **cc**  are string arrays with any of email addresses, users or groups. Email is sent to all the users of the groups.  
**From** is optional. If missing the email is sent from the default email address configured in Jira.  
The function is the same as sendEmail() but with MIME type features. Starting with version 4.0 the engine is able to detect automatically when you send email. This function is now an alias to sendEmail(). Refer to that documentation page for details.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sendHtmlEmail([from], to, [cc], subject, body\_or\_template, [language]) or sendHtmlEmail(from, to, cc, subject, body\_or\_template, language, issue\_key, regex\_array) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**None**

To render HTML correct, write it correct: 'using the <html> and <body> tags'.

## See also