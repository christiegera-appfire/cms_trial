# Comala Document Management Cloud ISO 13485 Sections 4.2.4 & 4.2.5 (Control of Documents, Control of Records) Compliance Statement

|  |  |
| --- | --- |
| Document Version | 1.1 |

This article explains how compliance with sections 4.2.4 and 4.2.5 can be achieved when using Confluence with Comala Document Management. It also provides information about support for other standard elements and a list of the tools required for successful implementation.

Confluence is a wiki used to help teams collaborate and share knowledge efficiently. It acts as a document collaboration and repository, tracking what changed in each document, when, and by whom. Team members can create, share, and collaborate on content.

If your organization has an ISO-13485:2016 quality management system, you can leverage Confluence to meet many of the requirements of that standard.

Extending Confluence with Comala Document Management will help you meet the requirements related to the management and control of documents and records (sections 4.2.4 and 4.2.5).

Reviewing our complementary compliance statement for [FDA CFR 21 part 11](/cms_trial/space/CDMC/2192776841/Comala+Document+Management+Cloud+FDA+Title+21+CFR+Part+11+Compliance+Statement/) may also be useful.

Appfire does not claim compliance or certification of any of our tools, as it is impossible for any vendor to offer a compliant system. In addition to taking advantage of technical elements, compliant systems must implement the necessary procedural and administrative controls.

**Need Help?**

Need help setting up Confluence and Comala Document Management for controlled documents?  [Contact Us](http://appf.re/support).

---

## **1. Checklist against the ISO 13485:2016 requirements of sections 4.2.4 and 4.2.5 (Control of documents, control of records)**

| **Reference** | **Gist** | **Appfire apps** | **Confluence** | **Processes and activities** |
| --- | --- | --- | --- | --- |
| 4.2.4 (a) | Review and approve documents for adequacy prior to issue; | Comala Document Management provides a method of enforcing document review and approval processes. This approval process is supported by built-in electronic signatures and an audit log. The flexibility provided by the Comala Document Management macro language enables you to configure an approval process that reflects your defined documented approval processes and your different organizational roles. | Each Confluence page has a unique Space/Title combination.  Page versions are captured automatically, and comparisons between versions are provided.  Unique page identifiers can be allocated manually (i.e., using page properties or metadata). | Define the review and approval process that works best for you. |
| 4.2.4 (b) | Review, update as necessary, and re-approve documents; | The approval process, as provided by Comala Document Management, supports the processing of updates according to the defined approval process. |  |  |
| 4.2.4 (c) | Ensure that the current revision status and changes to documents are identified; | Comala Document Management provides the means to clearly distinguish between current and draft versions of documents. Some organizations go further and use Comala Publishing to help separate between approved pages and pages that are still in the authoring and approval process. It creates a structure of an authoring space, where approved documents are automatically published into an official space. | Confluence provides a complete history of changes to each document. If you set up a dedicated official space, this feature will show the difference between official versions of the page. |  |
| 4.2.4 (d) | Ensure that relevant versions of applicable documents are available at points of use. |  | Users can access Confluence throughout the internet (per your network and security configuration) using any device. |  |
| 4.2.4 (e) | Ensure that documents remain legible and readily identifiable; |  | Each Confluence page has a unique Space/Title combination. | Keeping your documents electronically ensures they are always legible. |
| 4.2.4 (f) | External documents are identified, and their distribution is controlled |  | Confluence provides a way to attach external files to pages, providing the structure to align external documents with your internal structures (approvals, identification, access management) |  |
| 4.2.4 (g) | Prevent deterioration or loss of documents; |  |  | Implement a backup mechanism. |
| 4.2.4 overall | Changes to documents are reviewed and approved by appropriate functions in the organization | The definition of the approval process in Comala Document Management supports a role-based approval and review process. |  |  |
| 4.2.4 overall | Documents are retained for a defined retention period |  | Confluence provides the mechanism to retain all pages, including their historical versions. | Implement a backup mechanism. |
| 4.2.5 | 1. Records are a specific type of document, 2. Segregation and limited access to sensitive information. 3. Changes to records are identifiable |  | Confluence provides facilities to limit access to documents in a granular manner.  Confluence also keeps historic versions of pages and provides comparisons between page versions. |

## **2. Tips on how Confluence and Comala can reinforce ISO 13485:2016 processes**

## 2.1 Annual reviews of documents

It is required to review all your QMS documents periodically. Comala Document Management provides a built-in way to force documents to be re-approved after a set period (if they have not been reviewed during that time), hence ensuring no document is neglected in this review.

## 2.2 Forms and standardization of document layout can be implemented using Confluence templates

Many procedures are implemented using forms or a standardized layout of documents. For example:

1. Minutes of meeting form
2. Management review form
3. Clinical protocol
4. Quality plan

Confluence page templates are an excellent way to put all the forms in the hands of your team.

## 2.3 Medical Device Files (MDF) and other special collections (i.e., DHF, FMR)

A Confluence page can be set up as the index of your MDF, with hyperlinks to all the relevant pages and files (either attachments or external links) included in your MDF. This provides an easy way to ensure that the MDF always points to the current versions of documents and prevents the duplication of information. The actual content that goes into the MDF can be, at the same time, easily retrievable to your use in a hierarchy and location that makes sense to them.

## 2.4 Internal communication

Confluence is conducive to information sharing, internal collaboration, and communication.

## 3. The toolset required to set up a document management system on Confluence

The following table shows the typical set of tools used by companies that maintain their Quality Management System in Confluence :

| **Component** | **Role** |
| --- | --- |
| Confluence | The platform for creating, storing, and using the documented information. |
| Comala Document Management | An Appfire app for Confluence that provides a way to enforce an approval process for documents. This approval process is supported by built-in electronic signatures and an audit log. The flexibility provided by the Comala Document Management macro language enables configuring an approval process that reflects your defined documented approval processes and your different organizational roles. |
| Comala Publishing (optional) | An Appfire app for Confluence that helps separate between approved pages and pages that are still in the authoring and approval process. It creates a structure of an authoring space, where approved documents are automatically published into an official space. This helps ensure that document users can always access the current approved release.  It complements the functionality of Comala Document Management but is optional. Some customers find it easier to work with a set of two spaces, or it can be used in cases with more strict auditing requirements. |
| Secure Infrastructure | Provide a secure platform where only authorized users can access and modify the data.  Backup facilities. |