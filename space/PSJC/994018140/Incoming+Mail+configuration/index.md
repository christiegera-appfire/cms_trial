# Incoming Mail configuration

SIL scripting efficiently processes incoming emails, providing a high level of flexibility.

See the following video for an overview of this feature.

Transcript

With Power Scripts, you can use SIL scripts to process incoming emails and automatically create Jira work items.  
This video illustrates how to configure this feature.  
To begin, let's create the SIL script that processes incoming mail.  
Click Settings > Marketplace Apps > SIL Manager.  
Create a new file in the appropriate folder.  
Enter a name for the script, Email\_Create, in this example.  
Then, paste the sample script listed on this page into the SIL editor.  
On the "createIssue" line, replace projectkey with your Jira project key.  
In this example, the project key is TC for the Technical Communications project.  
Check the script and then save it.  
Next, let's configure the incoming mail settings.  
Click Configurations > Integrations > Incoming Mail and then click Add configuration.  
The Setup Incoming Mail Configuration page displays.  
Here, enter your email settings.  
Use the Protocol drop-down to select either POP3 or IMAP.  
In this example, we are configuring the feature for a Gmail address, so we'll select IMAP.  
Next, enter [imap.gmail.com](http://imap.gmail.com) in the Mail Host field.  
In the Port field, specify which port the email server listens on.  
Note that this field defaults to the appropriate value based on the selected Protocol.  
Then, enter the mailbox that Power Scripts will monitor for new Jira issues.  
Next, we need to specify the mailbox password.  
However, this is not the actual Gmail password.  
Instead, generate an app password for the Gmail account and use that value here.  
App passwords are available after you enable 2-Step Verification on your Google account.  
Refer to Google's documentation for the current steps.  
Next, select the script, email\_create, that was created at the beginning of this demonstration.  
Specify how often the script should check the mailbox, the maximum message size, and whether processed emails are deleted.  
Test the connection.  
A success message displays at the top of the page.  
Now, save the settings.  
On the Incoming Mail page, the Status column is set to "Processing."  
From here, you can pause processing, test the connection, edit the connection, or delete it.  
When the script identifies a new email, it processes the message and creates a work item.  
In addition to creating Jira work items, the mail integration feature can:  
Route work items to different projects based on customers or keywords.  
It can extract data from an email and automatically populate work item fields.  
To summarize, with Power Scripts, incoming emails can be efficiently processed using SIL scripts, providing the flexibility to create and update Jira work items.

---

## How to access the Incoming Mail configuration

To access the Incoming Mail configuration:

1. Click **Settings** > **Marketplace Apps**.
2. Go to **Power Scripts** > **Configurations** > **Integrations** > **Incoming Mail**.
3. Use the **Add configuration** button to create your Incoming Mail settings.

![Power Scripts for Jira Cloud incoming mail settings panel](/cms_trial/assets/c152463b-1425-48dd-8720-4120b5fa75a7.png)

---

## Key configuration settings

Configure the following mail server parameters to establish your incoming email connection:

| **Configuration setting** | **Description** |
| --- | --- |
| **Protocol** | Select a protocol that matches what's enabled on your mail server. The options are:   - POP3 (secure) - POP3 (start TLS) - IMAP |
| **Mail Host** | Enter the server's hostname or IP address. Example: [imap.gmail.com](http://imap.gmail.com) |
| **Port** | Specify the port number the mail server uses for connections. The field is pre-populated with the default port for your selected protocol. |
| **User Mailbox** | Enter the username for the mail account you want to connect to. Example: [testincomingemail@gmail.com](mailto:testincomingemail@gmail.com) |
| **Password** | Enter the authentication password for establishing the connection.  This is typically not your regular mail password. For services like Gmail, use the generated App password instead. |
| **Script** | Select the SIL script to execute when new emails arrive.  Utilize the dedicated [Incoming Mail Processing Functions](/cms_trial/space/PSJC/999162356/Incoming+Mail+Processing+Functions/) available in SIL to achieve your desired email handling goals. |
| **Mail check interval** | Specify how frequently (in minutes) the system should check for new messages in your mailbox. |
| **Maximum message size** | Set a file size limit in megabytes to prevent out-of-memory errors. Emails exceeding this limit will be skipped during processing. |
| **Delete processed emails** | Toggle this option to automatically remove emails from the mail server after processing. |

Test the connection before saving.

---

## Incoming Mail configuration management

A properly configured *Incoming Mail* setup displays below:

![Power Scripts for Jira Cloud incoming mail settings panel](/cms_trial/assets/c152463b-1425-48dd-8720-4120b5fa75a7.png)

To manage the *Incoming Mail* configuration, use the available options in the **Operations**column. You can:

- Pause mail processing
- Test the connection
- Modify the configuration settings
- Delete the configuration

The Mail configuration can display the following status indicators:

| **Status** | **Description** |
| --- | --- |
| processing | The configuration is active and checking for new emails at each configured interval. |
| disabled | Processing is manually paused and can be resumed when needed. |
| DISCONNECTED | Connection details are invalid and require updates to resume processing. |

The Processing History table displays the 10 most recent processing results with the following counters:

| **Label** | **Description** |
| --- | --- |
| Processed | The number of emails successfully processed. |
| errors | The number of emails that encountered errors during processing. |

---

## Email-to-issue conversion SIL script

This example script automates issue creation from incoming emails with the following functionality:

- Creates a new Jira issue when an email contains a project name in the subject line.
- Uses the email body as the issue description.
- Sets the reporter field to the email sender.
- Adds email CC recipients as issue watchers.
- Handles file attachments from the email.

The script also includes logic to add comments to existing issues rather than creating duplicates.

```text
IncomingEmail mail = getIncomingEmail();

string issueKey = mail.subject;
if(issueExists(issueKey)) {
    // add comment

    string commentText = mail.body;
    string userCommenting = getUserByEmail(mail.from).key;
    
    addComment(issueKey, userCommenting, commentText);
    attachAllFilesFromEmail(issueKey);
    
} else {
    // create issue
    
    string summary = mail.subject;
    string description = mail.body;
    
    string [] fields = {};
    fields += {"reporter", getUserByEmail(mail.from).key};
    
    createIssue("PROJECT NAME", "", "Task", summary , "Minor", description, {}, "", "", fields);
}
```

To learn more about the `IncomingMail` SIL structure and other useful email functions, see the [Incoming Mail Processing Functions](/cms_trial/space/PSJC/999162356/Incoming+Mail+Processing+Functions/) page.