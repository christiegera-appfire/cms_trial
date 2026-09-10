# How does the Connector securely access Salesforce data?

## Purpose

What standards does the Connector use to securely access Salesforce data?

## Answer

Data in transit is automatically encrypted during transmission via Transport Layer Security (TLS) through the use of HTTPS. Data at rest is not encrypted, but sensitive data is masked. Some organizations may also choose to use an encrypted database (Jira stores its data in a database) or an encrypted file system.

For authentication, industry-standard JWT (JSON Web Tokens) are used as the mechanism to confirm the identity of a requestor before granting access to secured information.

If you need additional information, you can also refer to our [security statement](/cms_trial/space/CSFJIRA/2258305080/Appfire+Trust+Center/).