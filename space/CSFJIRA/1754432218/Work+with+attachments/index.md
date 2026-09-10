# Work with attachments

There are limits on the number and total size of attachments per synchronization to maintain optimal performance. The synchronization of attachments is affected if either limit is exceeded, whichever comes first.

- Maximum number of attachments per synchronization session: 50
- Maximum total size of attachments per synchronization session: 700MB

If your synchronization exceeds either of these limits, the attachments exceeding the limit won’t synchronize. If you don’t see the expected attachments, please contact our [support team](https://appf.re/support). To successfully complete the sync, please ensure that the number and total size of attachments remain within the allowed thresholds.

Attachments can be synchronized automatically between Jira and Salesforce when an association has been established. The attachments from opposite systems are created as native attachments in the other system, so users do not need access to both systems to get the attachments.

In a typical scenario, this is useful when a support agent in Salesforce wants to send screenshots or logs from a Case to developers in Jira. In return, when a fix is ready, a developer in Jira can send an artifact directly into the Salesforce Case. This removes the manual steps of sharing attachments between the two systems.

## Configure attachments settings

![contentId-1754432218](/cms_trial/assets/ec8a4395-9a9b-41f8-8080-22f7df22aa02.png)

The admin must turn on the attachment synchronization feature through a Connection setting called **Synchronize Attachments**.

Both Salesforce Attachments and Salesforce Files features are supported, though Salesforce Files support has to be enabled in the Connection settings after enabling the **Synchronize Attachments** setting.

For more instructions on accessing and configuring attachment settings for Connections, view [Configuring connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).

## Attachment synchronization

Attachments can be automatically or manually pushed (sent) and pulled (received).

For more information, refer to:

- [Work with attachments in Salesforce](/cms_trial/space/CSFJIRA/3091695099/Work+with+attachments+in+Salesforce/)
- [Work with attachments in Jira](/cms_trial/space/CSFJIRA/3092024038/Work+with+attachments+in+Jira/)