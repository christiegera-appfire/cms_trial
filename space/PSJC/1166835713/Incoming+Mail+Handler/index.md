# Incoming Mail Handler

Incoming emails can be efficiently processed using SIL scripting, providing an unparalleled level of flexibility. Review the following video for an overview of this feature.

The sample script used in the video is listed below. For more details, please see the [configuration page](/cms_trial/space/PSJC/994018140/Incoming+Mail+configuration/) that describes this feature.

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