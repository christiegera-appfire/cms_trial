# Incoming Mail Processing Functions

- [attachAllFilesFromEmail](/cms_trial/space/PSJC/1001521294/attachAllFilesFromEmail/)
- [attachFileFromEmail](/cms_trial/space/PSJC/1001324700/attachFileFromEmail/)
- [getIncomingEmail](/cms_trial/space/PSJC/1002045477/getIncomingEmail/)
- [getRawIncomingEmail](/cms_trial/space/PSJC/1004503227/getRawIncomingEmail/)
- [saveAllAttachmentsFromEmail](/cms_trial/space/PSJC/1001881719/saveAllAttachmentsFromEmail/)
- [saveAttachmentFromEmail](/cms_trial/space/PSJC/1002307615/saveAttachmentFromEmail/)

As opposed to the server routines, we use full structures here because we have access to the whole email.

### **IncomingMail**

```text
string subject;
string body;
string htmlBody;
string [] to;
string [] cc;
string [] from;
string [] replyTo;
IncomingEmailHeader [] headers;
IncomingEmailAttachment [] attachments;
string contentType;
date sentAt;
date receivedAt;
int size;
IncomingMail [] embeddedMessages;
```

### IncomingEmailHeader

```text
string name;
string value;
```

### IncomingEmailAttachment

```text
string fileName;
string contentType;
int size;
byte [] content;
```

### **Example usage**

Standard processing:

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
    
    createIssue("SCRUM", "", "Task", summary , "Minor", description, {}, "", "", fields);
}
```