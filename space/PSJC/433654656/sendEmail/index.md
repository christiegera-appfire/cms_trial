# sendEmail

## Description

Sends an email. **To** and **cc** are string arrays with any of email addresses, users or groups. Email is sent to all the users of the groups.  
  
**From** is optional. If missing the email is sent from the default email address configured in Jira. To pass the language specify the 'sender', 'to', 'cc', 'subject', 'body' and finally the 'language', as a string (for instance "en", "fr", "en\_US", "ro", and so on). However, this is relevant only if you use templates as they support localization.  
  
For example, an email sent with language "en" will look for templates in the folder called "en", inside the default template directory. If no such template is found, it will use the one in the default directory.  
  
Also, starting with katl-commons-1.1.1, a default template placed in the default directory is mandatory for each template name used in your SIL programs. For example, if you want to use a template "t.tpl" using language "en\_US", it is not only necessary to have "t.tpl" in the "en\_US" folder, but you have to have a file "t.tpl" in the default directory.  
  
If you don't specify the language parameter and you use templates, by default the messages are sent in the sender defined language. For the users that are Jira users ('to' or 'cc' are user names and not email addresses) the language defined in the user profile(for each user) is used for email sending. For the rest of the users the email is sent using the sender defined language.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sendEmail([from], to, [cc], subject, body\_or\_template, [language] | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| from | String | No | From address |
| to | string [] | Yes | Recipient list |
| cc | string [] | No | CC'ed recipient list |
| subject | String | Yes | Subject |
| body\_or\_template | String | Yes | Message body, either direct or a template |
| language | String | No | Language used to send the email(relevant only if you use templates) |
| issue\_key | String | No | Issue to extract attachments from |
| regex\_array | String [] | No | Name patterns to match the attachments from the issue |
| wildcard\_path\_array | String [] | No | Absolute paths containing wildcards for attaching files from disk |

## Return Type

## Examples

### Example 1

```javascript
sendEmail("projectmanager", "teamleader1", "Transition executed", currentUser() + " has executed a transition");
// here we have to, cc, subject and body.
// The from and language parameters were omitted.
```

### Example 2

If SendEmailLanguage has the value receiver\_language, testJiraUser1 is a Jira user having the defined language French and testJiraUser2 is a Jira user having the defined language German.

```javascript
string [] to = {"testJiraUser1", "testEmail@appfire.com", "testJiraUser2"};
string [] cc = {"testEmail2@appfire.com"};
sendEmail("testFrom@appfire.com", to, cc, "testSubject.tpl", "testBody.tpl");
```

Result: One email in French will be sent to testJiraUser1, one email in German for testJiraUser2 and one email in the sender defined language for testEmail@appfire.com(as to) and testEmail2@appfire.com(as cc).

### Example 3

Is similar with example 2, but here the language parameter is used.  
If SendEmailLanguage has the value receiver\_language, testJiraUser1 is a Jira user having the defined language French and testJiraUser2 is a Jira user having the defined language German.

```javascript
string [] to = {"testJiraUser1", "testEmail@appfire.com", "testJiraUser2"};
string [] cc = {"testEmail2@appfire.com"};
sendEmail("testFrom@appfire.com", to, cc, "testSubject.tpl", "testBody.tpl", "en_US");
```

Result: It will be sent one email in English(because of the en\_US language parameter)

### Example 4

This example will demonstrate the ability to attach files (to the email) selected from the attachments of the issue using regex patterns.  
We will assume that the issue has three attachments: attachment1.txt, attachment2.txt and attachment3.txt (note that this last one does not have a dot to separate the extension).  
Now let's see a few examples of regex patterns that will match some of the attachment. Note that we will use key to specify the current issue, but feel free to use any other issue key.

```javascript
sendEmail("santa@appfire.com", {"jira-users"}, {}, "santa_subject.tpl", "santa_letter.tpl", "en_US", key, {"attachment.*"});
//This will match all of the attachments. Since we are using regex patterns, attachment.* will match anything that starts with attachment.
sendEmail("santa@appfire.com", {"jira-users"}, {}, "santa_subject.tpl", "santa_letter.tpl", "en_US", key, {"attachment.\.txt"});
//This will match attachment1.txt and attachment2.txt. The first dot will match any character (the 1 and 2). Note that the second dot is escaped using double backslashes and will not match attachment3.txt.
sendEmail("santa@appfire.com", {"jira-users"}, {}, "santa_subject.tpl", "santa_letter.tpl", "en_US", key, {"attachment1\.txt", "attachment3atxt"});
//This will match attachment1.txt and attachment3.txt.
```

Don't forget to use double backslashes when escaping special characters in regex patterns.

### Example 5

You can also attach files directly from disk by specifying absolute paths. Note that you can also use \* (anything) and ? (any single char) as wildcards.

```javascript
sendEmail("santa@appfire.com", {"jira-users"}, {}, "santa_subject.tpl", "santa_letter.tpl", {"C:/gifts/jira-users*.gift"});
```

### Example 6

You can also use the JEmailMessage structure type when sending an email. This option can make the code a little cleaner.

```javascript
JEmailMessage email;
email.to = {"testJiraUser1", "testEmail@appfire.com", "testJiraUser2"};
email.subject = "Email to Santa";email.message = "Dear Santa, I want a train.";
sendEmail(email);
```

Here is the same example that includes adding attachments to the email. This requires the use of the JEmailAttachment structure type.

```javascript
JEmailMessage email;
email.to = {"testJiraUser1", "testEmail@appfire.com", "testJiraUser2"};
email.subject = "Email to Santa";
email.message = "Dear Santa, I want a train.";
for(string a in attach) {  
    JEmailAttachment att;
    att.name = a;
    att.file = getAttachmentPath(key, a);
    email.attachments += att;
}
sendEmail(email);
```

## See also