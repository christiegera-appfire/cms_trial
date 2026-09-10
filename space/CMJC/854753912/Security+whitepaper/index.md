# Security whitepaper

---

## Data and configuration transfer

### How does Configuration Manager for Jira Cloud transfer data between Jira Cloud sites?

We use secure HTTPS channels with TLS 1.2+ for all data transfers between Jira Server/Data Center instances and Jira Cloud sites.

### How does Configuration Manager for Jira Cloud ensure secure network communication between Jira Cloud sites?

Data in transit is encrypted to safeguard network communication.

---

## Data analysis

### What kind of data analysis does Configuration Manager for Jira Cloud perform?

Configuration Manager for Jira Cloud performs analysis of the deployed configuration and data. The app analyzes the source Jira Cloud site’s configuration and data and shows what needs to be changed on the destination Jira Cloud site to accommodate the migrated data. If there is a fatal error in the data integrity or configuration conflict, the deployment cannot continue until that problem is resolved.

### Does Configuration Manager for Jira Cloud perform data analysis operations for purposes other than the deployment itself?

No, all analysis operations are performed only for deployment purposes.

### Does Appfire collect and preserve customer-sensitive information for a period longer than the deployment duration?

We keep all the customer-sensitive data for 30 days after the deployment. This helps our support team to act quickly and resolve any issues if necessary.

### Do we keep a customer’s data after they uninstall the app?

We can preserve the customer’s data for up to 90 days.

### Are the analysis data/results accessible to any 3rd party entities or organizations?

No. Analysis data/results are not accessible to any third-party entities.

---

## Data residency

### Which cloud service provider are we using for the deployment infrastructure?

Amazon Web Services hosts the deployment infrastructure.

### In which regions does the deployment infrastructure reside?

Currently resides in US-EAST-1, with plans to offer region selection.

### What kind of cloud service do we use for the deployment infrastructure?

The following services are utilized:  
- S3  
- RDS  
- Fargate  
- Lambda  
- DynamoDB  
- KMS  
- API Gateway  
- CloudFront

### What type of encryption service do we use to encrypt end-customer data temporarily stored in our cloud infrastructure?

Customer data is fully encrypted during temporary storage and aligned with the highest security industry standards.

### Is there any situation where we have access to customer-sensitive data or attachments during or after the deployment process?

No one has access to customer data during the deployment process. However, you can share your deployment data with our support team for quicker issue resolution purposes.

---

## Deployment statistics

### What kind of deployment statistics do we collect?

We collect anonymized (non-sensitive) statistics about deployment performance.

### For how long do we keep deployment statistics for a certain deployment?

Deployment statistics may be kept indefinitely. It’s up to the customer to decide.

### Do our deployment statistics retain any customer-related data that could be associated with our end customers in the future?

No.

### Where do we store our deployment statistics, and can 3rd party companies or organizations access them?

We store deployment statistics in a 3rd party analytics platform. All statistical data is encrypted in transit and at rest.

---

## Deployment of app data

### Are we using the same cloud service provider and already established infrastructure for 3rd party app data deployment?

Yes.

### How do we handle app data during the deployment process?

We do it the same way we manage the Jira core data.

---

## Deployment metadata storage

### For how long do we store customer or deployment-related information?

This information helps us improve the experience of future deployments so we can store it for up to 1 month after a license subscription has ended.

---

If you have any questions regarding the deployment’s security aspects or need help during your deployment process, please do not hesitate to [contact us](https://appf.re/support) – we’ll be glad to help!