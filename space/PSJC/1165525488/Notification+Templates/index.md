# Notification Templates

Notification template scripts are scripts that directly relate to communication and messaging through writing to files or sending notifications, like emails, directly.

The templates will create the notification script by adding the script to the configuration that corresponds to the individual script.

**NOTE:** Because the notification scripts are a collection of other script types there isn’t a standard way to configure and test the template scripts. See each template definition for details regarding configuration and testing.

## Templates

## Send an email

A SIL action that will send a custom email to the desired address, project role, or user group.

Script type: **Workflow Action**  
For more information about configuring and testing action templates [click here](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487273).

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| From | NO | The address that the email should be sent from. |
| To | YES | The recipients email address. |
| CC | NO | List of CC email addresses. |
| Subject | YES | The subject of the email. |
| Body | YES | The text body of the email. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
string from = "jira@company.com";
string [] to = "users@company.com";
string [] cc = "propertymanagement@building.com";
string subject = "Building is on fire";
string body = "Please help, my hot yoga class is getting too hot!";

sendEmail(from, to, cc, subject, body);
```

**NOTE:** In order for this action to successfully send an email Power Scripts must first be [configured for sending emails](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488160). The default setting will not send out any emails.

**NOTE:** If using the “From” field the mail account specified in the [email configuration](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488160) must be set up to be allowed to send from multiple addresses. An example of this is when an assistant can send an email as their boss from their own email account. Otherwise, the email account specified in the email configuration will be who the email is sent from.

**NOTE:** HTML tags can be used within the body of the email.

---

## Recurrently Print in Server Log

Print text in log file recurrently.

Script type: **Recurrent (scheduled)**  
For more information about configuring and testing scheduled templates [click here](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15480692).

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
logPrint("INFO", "This is a recurrent log message");
```

---

## Recurrently Send an Email to all Admins

A recurrent SIL job that will send a custom email to the desired address.

Script type: **Recurrent (scheduled)**  
For more information about configuring and testing scheduled templates [click here](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488160).

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| From | NO | The address that the email should be sent from. |
| CC | NO | List of CC email addresses. |
| Subject | YES | The subject of the email. |
| Body | YES | The text body of the email. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
string from = "jira@company";
string [] cc = "otherpeople@company";
string subject = "You said I couldn't be more annoying";
string body = "This email that gets sent out every hour will prove you wrong!";
string[] admins = usersInGroups({"jira-administrators"});
for(number i = 0; i < size(admins); i = i + 1){
   admins[i] = userEmailAddress(admin[i]);
}

sendEmail(from, admins, cc, subject, body);
```

**NOTE:** If needed, the group used to identify the Jira admins can be changed directly in the script after it is generated.

**NOTE:** HTML tags can be used within the body of the email.

---

## Print in server log when an event is triggered

Print text in log file when an event happens.

Script type: **Listener**  
For more information about configuring and testing listener templates [click here](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15486531).

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| User | YES | The specific user for which the issue will be assigned. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
assignee = "jmuse";
```