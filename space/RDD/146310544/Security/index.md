# Security

This page provides details on Dashboard Hub security. You can find further information in our [Marketplace listing](https://marketplace.atlassian.com/apps/1223898/dashboard-hub-pro-charts-reports-time-in-status-for-jira?hosting=cloud&tab=privacy-and-security), and general Appfire security policies in our [Trust Center](https://trust.appfire.com/).

## Security Programs

| **Cloud Fortified** | **Bug Bounty Program** | **Self-Security Assessment** |
| --- | --- | --- |
| **Cloud Fortified** apps offer additional security, reliability and support through:  \* Cloud security participation  \* Reliability checks  \* 24hr support response time  [Learn about the Cloud Fortified apps program](https://www.atlassian.com/trust/marketplace?source=app-listing-badge) | The Atlassian Marketplace Bug Bounty Program is hosted on Bugcrowd, a SaaS platform built to crowdsource vulnerability discovery from a global pool of talented security researchers.  Learn more about the [Bug Bounty program](https://www.atlassian.com/licensing/marketplace#what-is-the-marketplace-bug-bounty-program) | The security self-assessment program is a collaboration between Atlassian and Marketplace Partners to increase security awareness and improve security practices.  Learn more about the [Self-Security Assessment program](https://developer.atlassian.com/platform/marketplace/security-self-assessment-program/) |

## Data Storage Cloud

Dashboard Hub uses an external database to store data, but **we do not store personal data**. The only data that is stored is the basic to connect and display information in your dashboards.

The app acts as a proxy, it encrypts and decrypts the data to perform requests, only if the acting user has granted access to it.

### What is stored?

**⚙️ Datasources**

A datasource connects your dashboard with the source of the data. In order to work datasources require:

- The data you introduce during the datasource creation (it changes a bit depending on the type of datasource)
- The accountId of the creator of the datasource (in compliance with the GDPR)
- The instance where it was created
- The timestamp when it was created
- The permissions to know who can access and use the datasource

When we store the credentials, we use your own instance, and **that data is encrypted too.**

**📊 Dashboards**

A dashboard displays at a glance your key indicators the way you arranged it. To retrieve the data we store:

- The dashboard name (**encrypted**)
- The accountId of the creator (in compliance with the GDPR)
- The instance where it was created
- The timestamp when it was created
- The permissions to know who can access and use the dashboard
- Slides (**encrypted**). Each slide is composed by a list of gadgets, where each of which has:

  - The datasource id
  - The gadget config

**Datasources** and **Dashboards** data are stored in a cloud based storage system, with restricted access and a backup policy.

🛡 All data is encrypted, and it requires the keys used to encrypt it initially. These keys are stored in another location.

#### **Installation data**

Dashboard Hub keeps some details of every installation in order to securely enable the communication between the source site and Dashboard Hub (URLs, keys for secure connections, etc.).

It is stored and encrypted on our own databases, and it is never exposed to anyone.

The exposition or corruption of this data would only provoke a disruption in the connection, never the leak of any customer data.

### Where is it stored?

The data is stored in different regions depending on where your product data is hosted by Atlassian and/or monday.com. You can find more details in our dedicated page to [Data Residency (Cloud)](/cms_trial/space/RDD/146309741/Data+Residency+(Cloud)/).

### What is NOT stored?

Anything else… this means Dashboard Hub has to request your data every time you open a dashboard. We will add a cache mechanism in the future to improve the performance.

### Encryption

All data related is encrypted before sending it to the external storage.

## People and Access

All connections are secured between Dashboard Hub (included its database), the Atlassian and/or monday.com platform (any product) and users, using SSL.

Dashboard Hub support team has access (role-based) to the Dashboard Hub cloud application and data, and may access customer data (site URLs, Dashboard Hub users' uuid) only for services status monitoring and performing purposes.