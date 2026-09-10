# 7pace Timetracker for Jira Data Residency Policy

7pace Timetracker for Jira offers data residency for customer product data by storing that data in one of our supported 7pace storage regions: **European Union (EU)** or **United States (US)**. If your Atlassian Jira site is pinned to a region outside these two supported environments, 7pace Timetracker will display as **not pinned** in the Jira administration interface, and your data will reside in our default storage region (EU). This policy explains what data is covered, how residency is handled, and which limited categories of operational metadata may be processed globally.

**Summary**

7pace Timetracker currently operates two storage regions for data residency: **EU** and **US**. Customer product data covered by this policy is stored in the selected 7pace storage region. Atlassian residency locations outside the EU and US are not supported for local storage; customers pinned to other locations will see the app as "not pinned" and their data will reside in our default EU region.

---

## 📄 Scope of this Policy

This policy applies to **7pace Timetracker for Jira product data** created, uploaded, synced, or configured by customers and end users while using the app. In this document, we refer to that data as **Product Data**.

Product Data is covered by 7pace Timetracker data residency. Limited operational metadata needed to run, secure, support, route, and improve the service is not part of Product Data and may be processed outside the selected residency region as described below.

**Important**  
When this policy refers to a supported residency region, it means a **7pace Timetracker storage region** (EU or US). Atlassian residency locations outside of the EU and US are not supported for local in-country storage at this time.

---

## 🗺️ Supported Storage Regions

7pace Timetracker currently supports two storage regions for Product Data:

- **EU**
- **US**

If a customer's Atlassian residency location is the EU or US, 7pace stores Product Data in the corresponding 7pace Timetracker storage region. If a customer's Atlassian residency location is pinned to any other region, the app will display as "not pinned," and the data will be stored in the EU default region.

| Atlassian residency location | 7pace handling | Customer-facing meaning |
| --- | --- | --- |
| **European Union (EU)** | Stored in 7pace Timetracker EU | Product Data is stored in the 7pace Timetracker EU storage region. |
| **United States (US)** | Stored in 7pace Timetracker US | Product Data is stored in the 7pace Timetracker US storage region. |
| **Unsupported Locations** *(e.g., Great Britain, Germany, Canada, Australia, Japan, etc.)* | Defaulted to 7pace Timetracker EU | The app displays as **not pinned** in the Jira admin UI. Product Data is stored in the default 7pace Timetracker EU storage region. |
| **Global / Unpinned Atlassian location** | Defaulted to 7pace Timetracker EU | If no Atlassian residency location is pinned, 7pace Timetracker stores Product Data in the EU by default. |

In case of migration between regions, data will be temporarily stored in the region coordinating the migration - **European Union (EU)**.

---

## 📦 What Data is Covered by Data Residency

The following categories of Product Data are covered by 7pace data residency and are stored in the applicable 7pace Timetracker storage region:

- Worklogs and worklog comments
- Running timers
- Time periods, approvals, and approval history
- Time locks
- Custom worklog fields and their values
- Worklog layouts and related configuration
- Suggestion data derived from user activity and synced data
- Feedback questionnaire responses submitted through the product
- Customer-specific copies of Jira user identifiers used for authorization or display logic
- Role mappings, permission overrides, and related customer-specific authorization settings
- Personal reporting API tokens created by users
- Calendar integration data, including connected account metadata, synced calendar information, imported calendar events, and OAuth tokens used for Google or Microsoft Outlook calendar integrations
- Backups of regional Product Data
- Other customer-created or customer-configured product records of the same nature, including synchronization metadata directly tied to customer use of 7pace

**Residency commitment**  
Backups of Product Data remain in the same 7pace storage region as the underlying regional database.

---

## ⛔ What is Not Covered by Data Residency

Some data is needed to operate the service but is not treated as Product Data for residency purposes. This information may be processed or stored globally, provided it is limited to operational use and does not include restricted customer content.

Examples include:

- Routing metadata used to determine which 7pace Timetracker region holds a customer's Product Data, such as cloud identifiers, installation identifiers, internal tenant identifiers, database pointers, Jira base URL, feature flags, and similar operational records
- Installation, licensing, service health, and support metadata
- Application, access, audit, and operational logs
- Aggregated or anonymized product analytics
- Short-lived in-transit processing, such as request routing, webhook handling, and temporary caches
- Atlassian account profile information fetched on demand from Atlassian systems, where not stored by 7pace Timetracker as Product Data

**Operational data restrictions**  
Global logs and analytics must exclude worklog content, calendar content, Jira issue content, custom field values, credentials, and tokens. Analytics should use aggregated or anonymized information only.

---

## 🌐 Global Infrastructure and Shared Services

7pace Timetracker uses a combination of regional infrastructure and global operational services to deliver the app.

Customer Product Data is stored in the applicable supported 7pace Timetracker storage region. However, limited operational metadata may be processed by global infrastructure and shared platform services for purposes such as:

- Traffic routing and edge delivery
- Installation and uninstall handling
- Licensing and entitlement checks
- Security monitoring and abuse prevention
- Operational logging and support
- Aggregated or anonymized analytics

This includes shared Appfire platform services that support operational workflows across multiple Appfire products. These services may process limited operational metadata globally even when Product Data is resident in a supported 7pace Timetracker storage region.

**What we do not claim**  
We do not claim that all 7pace-related processing occurs only within the selected storage region. Our residency commitment applies to **Product Data** as defined in this policy. Limited operational metadata may still be processed by global infrastructure and shared services.

## 🤝 Third-Party Services

7pace Timetracker may rely on subprocessors and external platforms to provide the service. Depending on the feature used, these may include regional hosting providers, Atlassian services, content delivery and routing providers, analytics services, and calendar integration providers such as Google or Microsoft.

Where these services are used in connection with Product Data, 7pace Timetracker is designed so that Product Data stored by 7pace Timetracker remains in the applicable supported storage region. Some third parties may still process limited operational metadata or in-transit data globally as part of service delivery.

### 📋 Examples of Service Roles

- Regional cloud infrastructure hosts the 7pace application and regional databases.
- Edge and routing services help connect users to the service and direct traffic to the appropriate region.
- Atlassian platform services provide installation events and product integration behavior.
- Calendar providers process data when a user chooses to connect a calendar account.
- Analytics providers may receive aggregated or anonymized usage information.

For more information, check [Subprocessors in Appfire Trust Center](https://trust.appfire.com/?itemUid=e3fae2ca-94a9-416b-b577-5c90e382df57&source=title).

---

## ➡ Region Changes and Migrations

If Atlassian notifies 7pace Timetracker that a customer's residency location has changed between our supported regions (EU and US), 7pace may migrate the customer's Product Data to the newly applicable 7pace Timetracker storage region.

Migration may involve temporary service interruption. Where a move is required between 7pace Timetracker regions, 7pace Timetracker targets a migration window of up to 90 minutes.

**Practical effect**  
If a customer migrates their Atlassian site from the EU to the US, 7pace Timetracker will migrate their Product Data from the 7pace Timetracker EU storage region to the 7pace Timetracker US storage region.

---

## 💡 Examples

- If a customer's Atlassian location is **EU**, Product Data is stored in **7pace Timetracker EU**.
- If a customer's Atlassian location is **US**, Product Data is stored in **7pace Timetracker US**.
- If a customer's Atlassian location is **Great Britain** (unsupported region), the app displays as **not pinned** in the Jira admin UI, and Product Data is stored in **7pace Timetracker EU** by default.
- If a customer's Atlassian location is **Canada** (unsupported region), the app displays as **not pinned** in the Jira admin UI, and Product Data is stored in **7pace Timetracker EU** by default.
- If a customer's Atlassian location is **Global** or unpinned, Product Data is stored in **7pace Timetracker EU by default**.

---

## ❓ Frequently Asked Questions

### Does 7pace Timetracker store data in every Atlassian residency location?

No. 7pace Timetracker currently operates two storage regions only: EU and US. For any other Atlassian residency location, 7pace Timetracker does not offer local storage, and the app will display as **not pinned** in the Jira admin UI.

### What data is covered by 7pace Timetracker data residency?

Data residency covers Product Data created, uploaded, synced, or configured in 7pace Timetracker, including worklogs, timers, approvals, custom field values, calendar integration data, OAuth tokens, personal reporting API tokens, and regional backups.

### Are logs, analytics, and routing metadata stored in the same region as Product Data?

Not necessarily. Limited operational metadata, logs, and aggregated or anonymized analytics may be processed globally, provided restricted customer content and sensitive secrets are excluded from those payloads.

### What happens if my Atlassian location is Great Britain, Canada, or another unsupported location?

If your Atlassian site is located in a region other than the EU or US, the 7pace Timetracker app will display as **not pinned** in your Jira admin UI. Your Product Data will be stored securely in our default storage region, the **European Union (EU)**.

### What happens if my Atlassian site is not pinned to a residency location?

If the Atlassian site is Global or otherwise unpinned, 7pace Timetracker stores Product Data in the EU by default.