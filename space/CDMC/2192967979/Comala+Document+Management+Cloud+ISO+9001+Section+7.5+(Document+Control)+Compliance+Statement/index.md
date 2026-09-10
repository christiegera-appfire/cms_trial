# Comala Document Management Cloud ISO 9001 Section 7.5 (Document Control) Compliance Statement

|  |  |
| --- | --- |
| Document Version | 1.1 |

This article explains how compliance with section 7.5 of ISO-19001:2015 can be achieved using Confluence with Comala Document Management. It also provides information about support for other standard elements and a list of the tools required for successful implementation.

Confluence is a documentation tool used to help teams collaborate and share knowledge efficiently. It acts as a home for document collaboration and a repository, keeping track of what changed in each document, when, and by whom. Team members can create, share, and collaborate on content.

If your organization has an ISO-19001:2015 quality management system, you can leverage Confluence to meet many of its requirements. We believe that using Confluence across your organization aligns well with the standard's overarching objectives, such as improved communications, decentralization of quality processes, and knowledge sharing.

Extending Confluence with Comala Document Management will help you meet the requirements related to the management and control of documents (section 7.5, Documented information) .

This article explains how compliance with section 7.5 can be achieved when using Confluence with Comala Document Management. It also provides information about support for other elements of the standard and a list of the tools required for successful implementation

Appfire does not claim compliance or certification of any of our tools, as it is impossible for any vendor to offer a compliant system. In addition to taking advantage of technical elements, compliant systems must implement the necessary procedural and administrative controls.

**Need Help?**

Need help setting up Confluence and Comala Document Management for controlled documents?  [Contact Us](http://appf.re/support).

---

## 1. Checklist against the ISO 9001:2015 requirements of section 7.5 (Documented information)

| **Reference** | **Requirement**  **(Original working is given in italics)** | **How to Achieve Compliance** |
| --- | --- | --- |
|  |  | **Appfire Apps** | **Confluence** | **Processes and activities** |
| 7.5.1 | Certain documented information is required |  | QMS documentation is maintained in one or several Confluence spaces. | Create the required documents natively within Confluence, or attach external documents. |
| 7.5.2 | Documented information should be:   1. Identified and described 2. Reviewed and approved | Comala Document Management provides a way to enforce a review and approval process for documents. This approval process is supported by built-in electronic signatures and an audit log. The flexibility provided by the Comala Document Management macro language enables configuring an approval process which reflects your defined documented approval processes and the different organizational roles you have. | Each Confluence page has a unique Space/Title combination.  Page versions are captured automatically and provide comparisons between versions.  Unique page identifier may be allocated manually (i.e., using page properties or page metadata). | Define the review and approval process which works best for you. |
| 7.5.3.1 | Documented information will be:   1. Available to users; 2. Protected (from loss, misuse) | Comala Document Management provides the means to clearly distinguish between current and draft versions of documents. Some organizations go further and are using Comala Publishing to help separate between approved pages and pages which are still in the authoring and approval process. It creates a structure of an authoring space, where approved documents are automatically published into an official space. | Users can access Confluence throughout the internet (as per your network and security configuration) using any device.  Confluence provides facilities to limit the access to documents in a granular manner. | Use Confluence within a secure infrastructure. Implement policies for access management. |
| 7.5.3.2 | 1. Users need to be able to access and use the documentation; 2. Documents need to be preserved; and dispositioned 3. Apply change control; 4. Certain external documentation should also be controlled | - Comala Document Management provides the mechanism to change control each document (see explanation for 7.5.2 above) - For external documents: they can be attached to Confluence pages, and these pages then provide the control mechanism for the external document   Comala Document Management can then be used to approve each external document in a similar way to that of internal documents. | - Confluence permission mechanism is granular enough to allow some users to have 'view only' access to documents. - Documents may be disposed by moving to a segregated area in Confluence (typically a space sub tree which is hidden from most users) | Implement backup policies.  Block Confluence pages from being deleted (through access management). |

## 2. Tips on how Confluence and Comala Document Management can reinforce ISO 9001:2015 processes

## 2.1 Improved communication (ISO 9001:2015 sections 7.4, 8.2.1, 8.4.3)

The ISO 9001:2015 requires a conscious effort to establish good communication channels:

- from the management to the entire organization
- toward customers, i.e in regard to your products and services
- with your suppliers

Confluence can be a key pillar in your communication strategy. It provides a friendly, modern environment to share documents. Moreover, it has some key features to promote effective communication.

For example:

1. Out of the box, it offers a daily digest where users may be notified about changes on pages in a compact and non-spammy manner
2. Confluence pages come with support for bi-directional communication; (permitted) users may comment on pages, share with colleagues, or start a whole discussion in a forum that is related directly to the page. This helps cultivate a culture where feedback can be given by anybody in the organization
3. Confluence comes with a powerful search engine
4. With Comala Document Management and Comala Publishing, you may create Confluence Spaces which have only official, controlled pages, that can be shared with customers and suppliers

## 2.2 Organizational knowledge (ISO 9001:2015 section 7.1.6)

From its very start, Confluence has been widely used to capture and share organizational knowledge. In particular, some of the built-in page templates are specially designed for that, i.e.: the built-in templates ‘How-to-articles', and 'Troubleshooting articles'. Making Confluence available to everyone and providing your team with the context and space to record their knowledge can, over time, create a rich reference that your team can rely on.

You can read more about this at <https://confluence.atlassian.com/doc/use-confluence-as-a-knowledge-base-218275154.html> .

## 2.3 Awareness, competence and training (ISO 9001:2015 sections 7.3, 7.2)

Comala Document Management can be used to support a training-related workflow. Users can then be assigned to approve that they have read a certain page, and this approval is recorded on the page.

## 2.4 The toolset required to set up a document management system on Confluence

The following table shows the typical set of tools used by companies that maintain their Quality Management System in Confluence :

| **Component** | **Role** |
| --- | --- |
| Confluence | The platform for creating, storing and using the documented information. |
| Comala Document Management | An Appfire app for Confluence that provides a way to enforce an approval process for documents. This approval process is supported by built-in electronic signatures and an audit log. The flexibility provided by the Comala Document Management macro language enables configuring an approval process which reflects your defined documented approval processes and the different organizational roles you have. |
| Comala Publishing  (optional) | An Appfire app for Confluence that helps separate between approved pages and pages that are still in the authoring and approval process. It creates a structure of an authoring space, where approved documents are automatically published into an official space. This helps ensure that end users of documents always access the current approved release.  It complements the functionality of Comala Document Management and is optional. Some customers find it easier to work with a set of two spaces, or it can be used in cases where there are more strict auditing requirements. |
| Secure infrastructure | Provide a secure platform, where only authorized users are accessing and modifying the data.  Backup facilities. |