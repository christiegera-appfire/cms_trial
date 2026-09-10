# Document State

## Overview

When added to a Confluence page, the **Document State** macro displays information about the page’s current workflow state.

You can configure the macro to show one or more of the following:

- The current workflow state
- The date when the state was last changed
- The state’s expiry date (if applicable)

Dates are shown in **Confluence UTC format** for both the state change date and the expiry date.

![Comala Document State macro output showing current state](/cms_trial/assets/9ead8388-e88f-40a8-a797-683bcc6bc88b.png)

When no workflow is applied to the page, the document state macro displays the following message when editing the page and on the published page.

![Comala Document State macro rendered on a page](/cms_trial/assets/e2483af6-2e04-418f-8bf4-511fa9245b99.png)

## Add the macro

To add the document state macro,

1. Open your Confluence page and type /document state to display the document state macro option.

   ![Comala Document State macro editor configuration](/cms_trial/assets/1a05e4e9-fbba-4ebc-93d4-bab7f1b4fe55.png)
2. Select **Document State** to add the macro to the draft page.
3. Now, click the **Edit** icon on the macro to open the macro editor.

   ![Comala Document State macro with styled state display](/cms_trial/assets/a0abc2fd-bf29-49f8-a766-e85d3b5c2e59.png)
4. To configure the macro, check the boxes for one or more of the following options:

   - **Show State** – Displays the current workflow state.
   - **Show Changed Date** – Displays the date the page transitioned to its current state.
   - **Show Expiry Date** – Displays the state’s expiry date, if one is set.

   The selected options will be previewed in the macro on the draft page.

![Comala Document State macro options and output examples](/cms_trial/assets/ff7f933d-a07c-4bab-bc94-f917c877e246.png)

1. **Publish** the page to view the document state macro displayed in the page subtitle.

   ![Comala Document State macro inline state label](/cms_trial/assets/7ed5340a-31fb-442d-804e-2c5d3337aec9.png)

## Use the document state macro with other Confluence macros

The document state macro is compatible with the Confluence [Page Properties macro](https://support.atlassian.com/confluence-cloud/docs/insert-the-page-properties-macro/#Use-the-Page-Properties-macro) and the [Page Properties Report macro](https://support.atlassian.com/confluence-cloud/docs/insert-the-page-properties-report-macro/).

To use the macro,

1. Open a draft page and add the **document state** macro as a table value in the **page properties** macro.

![Comala Document State macro page properties editor](/cms_trial/assets/fc911104-1f8c-4076-bb33-0de96a85b30f.png)

1. The macro on the published page is rendered in a table.

![Comala page properties macro with Document State cell value on a page](/cms_trial/assets/efff63a6-ada9-4942-934f-177c50962b1b.png)

1. The page properties report macro can be added to a page to report the value of the example page property we created - **Comala Management App - State details**.

![Comala page properties report macro with Document State values](/cms_trial/assets/9e275ffa-228c-4d1f-a3d0-0eb157778aaa.png)

Here’s a demo video that shows how to use the document state macro.

## Exporting pages to PDF and Word

The **Document State** macro on-page information will be included when exporting the page to PDF or Word formats.

![Comala Document State macro rendered output on a published page](/cms_trial/assets/5c36420b-c33d-4953-9718-25d78cb45ffb.png)

## Page status (migration compatibility) macro

The **page status macro** displays the current workflow state.

The macro is added to a document migrated to the cloud, where the source server content includes the Comala Document Management for Server **page status macro**.

The **page status macro** is unavailable in the macro browser in a cloud site.

We recommend replacing the **page status macro** with the **document state macro** in your cloud content.

**Related topics**

- [Document approvals](/cms_trial/space/CDMC/2192777118/Document+Approvals/)

- [Document activity](/cms_trial/space/CDMC/2193097355/Document+Activity/)

- [Workflow states](/cms_trial/space/CDMC/2193066115/States/)

- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)