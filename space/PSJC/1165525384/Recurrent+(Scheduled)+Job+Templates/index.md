# Recurrent (Scheduled) Job Templates

Recurrent jobs are actions that occur at specified time intervals or on specific dates. These jobs are scheduled because either there is not other trigger type that can be sufficiently used, or because of other time or performance considerations. Some jobs, like jobs to trigger reindexing, may impact the performance of Jira so these can be scheduled off hours so users are not impacted. Other jobs, may rely on external factors like operations completing on external systems before the data can be synchronized. Or, another use for scheduled jobs is to create an escalation service that raises the priority on issues that are past due.

The templates will create the recurrent job by adding a new recurrent job script and its schedule to the configuration.

## Setting up the Recurrent Job Templates

Because recurrent jobs require a schedule to operate the first step will always be setting up that schedule. The options include

- **Every minute (starting immediately)** - This option may have performance implications and should be used sparingly.
- **Every 30 minutes (starting immediately)** - A better option for high priority jobs that need to happen throughout the day.
- **Every hour (starting immediately)**
- **Every 12 hours (starting immediately)**
- **Every day at 00:00 AM** - midnight
- **Every Sunday at 00:00 AM**
- **Every month on the 1st at 00:00 AM**
- **Every year on January 1st** - A great option for creating those annual tasks that always seem to get lost.

![Power Scripts for Jira Cloud request traces interface](/cms_trial/assets/2e724f2d-4600-4701-8101-866e8ffab648.png)

The other setting indicates which user the script should impersonate while running.

**NOTE:** The “Run as” setting is not required. However, this is a very important setting for scheduled jobs. Unlike every other type of automation, scheduled jobs are not initiated by a user action. Therefore, without a default user to impersonate, the script will be considered an anonymous user and thus may not have the proper permissions within Jira to carry out the desired operations.

## Testing the Script

Testing the script is as simple as completing the transition and checking if the recurrent job action occurred. For example, if the script was designed to create subtasks after the transition, check to see if the subtasks were created. If not, see this section about troubleshooting scripts.

## Templates

## Recurrently Print in Server Log

Print text in log file recurrently.

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

## Recurrently Reindex all Issues in Jira

Reindex all in the background, recurrently.

### Script

```text
admReindex(true);
```

**NOTE:** By default, this script will initiate a background reindex. If desired, this can be changed by editing the script directly and changing the **true** parameter to be **false**. Just be aware that users will not be able to use Jira while the full reindexing is running.