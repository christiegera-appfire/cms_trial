# Connector for Salesforce and Jira changes

**Release date**: February 13, 2025

This page includes the changes introduced to Connector for Salesforce and Jira that can affect your existing system. Review the changes carefully and perform any necessary actions to maintain the app’s functionality.

---

## **Attachment limits implemented to ensure stable performance**

**Change:**

We have introduced limits on the number and total size of attachments per synchronization to maintain optimal performance. Based on recent usage metrics, these limits have been adjusted to provide flexibility while preventing potential service disruptions.

**Limitations**

The synchronization of attachments is affected if either limit is exceeded, whichever comes first.

- Maximum number of attachments per synchronization session: 50
- Maximum total size of attachments per synchronization session: 700MB

These limits have been implemented to prevent performance degradation and service downtime. We will continue to monitor usage and assess a long-term solution as needed.

**Impact**

If your synchronization exceeds either of these limits, the attachments exceeding the limit won’t synchronize. If you don’t see the expected attachments, please contact our [support team](https://appf.re/support). To successfully complete the sync, please ensure that the number and total size of attachments remain within the allowed thresholds.

---

**Support and resources**

- For more information, refer to: [Work with attachments](/cms_trial/space/CSFJIRA/1754432218/Work+with+attachments/), [Attachment size limits](/cms_trial/space/CSFJIRA/3092024038/Work+with+attachments+in+Jira/)
- If you encounter any issues, raise a ticket with our [support team](https://appf.re/support)[.](https://appf.re/support)

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Connector for Salesforce and Jira!

---

|  |  |
| --- | --- |
| **Release date** | October 16, 2024 |
| **Highlights** | - [unmapped inline: placeholder] - [unmapped inline: placeholder] |