# Searching and Reporting

Comala Document Management provides robust tools for tracking document workflow, approvals, and activity, making it easier to monitor and report on the lifecycle of your pages and blog posts.

## Document Activity (document-level)

The **Document Activity** is a report of the workflow-related events and actions for a page or blog post. The workflow state dialog includes a **Document Activity** option in the **Actions** menu that displays the document’s workflow history. Document Activity data can also be exported to CSV.

![image-20260629-103054.png](/cms_trial/assets/b047819e-c27d-4286-970f-864ee4474367.png)

Refer to the [Document activity report](/cms_trial/space/CDMC/2193162907/Document+activity+(document-level)/) page for more details.

## Document report (Space level)

The document report provides a list of all the approval activities in a space. The report can be filtered by one or more workflow states and assigned to the current user for approval. The report also includes the workflow applied to each document, including cases where multiple workflows are active in a space. The report can be exported to CSV for custom dashboards and cross-space reporting.

Refer to the [Document report](/cms_trial/space/CDMC/2193033420/Document+report+-+Space+level/) page for more details.

## Page macros

A macro that can be used to retrieve page metadata. Document metadata displays the metadata or workflow parameter values directly on a Confluence page. This ensures critical document data is easily accessible and visible to users.

Refer to the [Page macros](/cms_trial/space/CDMC/2193162930/Page+macros/) page for more details.

## Page macros for reporting

These macros can be used in your Confluence pages and blog posts.

- [Document state macro](/cms_trial/space/CDMC/2192677319/Document+State/)

When added to a Confluence page, the **Document State** macro displays information about the page’s current workflow state.

- [Document approvals macro](/cms_trial/space/CDMC/2192777118/Document+Approvals/)

One or more **Document approvals** macros can be added to a page to display workflow approval information. Each macro can be configured to display the approval information for a different state in the workflow.

- [Document activity macro](/cms_trial/space/CDMC/2193097355/Document+Activity/)

Add one or more **document activity** macros to a document (page or blog post) to display dynamic information for the document activity for the workflow on a page.

## Confluence Search filters for macros

Confluence provides macros that support CQL filters. These include the [content by label](https://support.atlassian.com/confluence-cloud/docs/insert-the-content-by-label-macro/) macro and the [page properties report](https://support.atlassian.com/confluence-cloud/docs/insert-the-page-properties-macro/?searchId=F8TH9RXB7) macro.

For example, the **Comala workflow state**.

![Comala filter by label macro editor with workflow state filter](/cms_trial/assets/a3eedde6-00d2-44c0-b983-f4b1a80639ad.png)

The state value is case-sensitive

Other workflow filters are:

- **Comala workflow enabled**

  - use boolean **true** to filter pages with an applied active workflow
- **Comala workflow final state**

  - use boolean **true** to filter pages in the final state of the applied workflow
- **Comala state expiration**

  - filter by state expiration by date options

### REST API CQL fields

If you are searching with a separate reporting/scripting tool, for example, [Reporting for Confluence](https://marketplace.atlassian.com/apps/186/reporting-for-confluence?hosting=cloud&tab=overview) from Appfire or [ScriptRunner for Confluence](https://marketplace.atlassian.com/apps/1215215/scriptrunner-for-confluence?hosting=cloud&tab=overview) from Adaptavist, using the Confluence REST API, the following field names are used:

| Field | Field name |
| --- | --- |
| Workflow state | `cw_state` |
| Assigned approver | `cw_approver` |
| Workflow final state (boolean: true; false) | `cw_final` |
| Workflow enabled (boolean: true; false) | `cw_enabled` |

```text
cql=cw_approver="User ID" and cw_state="Approved"
```

The `cw_state` search is case-sensitive.