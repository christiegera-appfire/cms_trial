# Document Activity

## Overview

Add one or more **Document Activity** macros to a page or blog post to display the workflow activity log for that document.

![image-20260629-182338.png](/cms_trial/assets/304fbe57-e4fa-4688-a718-598caf0187bc.png)

The document activity macro information for the lifecycle of the workflow events on the document is shown as a table with the following columns:

![image-20260629-181712.png](/cms_trial/assets/700875f5-a3e2-437e-bff5-1db8af773cb1.png)

- Actor
- Action
- Comment
- Date
- State
- Version

The version includes a link to the document version.

Configure the macro to display different data columns and the maximum number of document activity entries.

When no workflow is applied to the page, the document activity report macro displays the following message when editing the page and on the published page.

![image-20260629-181811.png](/cms_trial/assets/fdbd3664-7362-4a3f-93a4-1dc427855472.png)

## Add the macro to a page

Edit the page and type /doc and select the document activity macro option.

![image-20260629-181903.png](/cms_trial/assets/274ce7b9-5d97-424d-8402-cdc8c12a5c00.png)

Choose **Document Activity** to add the macro to the draft page.

![image-20260629-182717.png](/cms_trial/assets/438ad5c6-3fd2-47a0-b5d4-763c91a7a311.png)

If a workflow is active on the draft page, the macro on that page previews any current document activity.

The default number of document activity entries displayed in the report is 25.

## Configure the macro

The macro can be configured to display a maximum number of document activity entries for the document.

![image-20260629-182816.png](/cms_trial/assets/7c2af97a-b983-4dfe-b99d-4dd07f0a8d80.png)

If a workflow has been applied to the published document, the current document's activity is displayed.

If no workflow is currently applied or there is no document activity, an empty report is displayed on the published document.

![Comala Document Activity macro with no activity entries](/cms_trial/assets/5cf6370c-9ee7-445c-b684-ebf2984208e8.png)

The maximum number of document activity entries can be set for the report. The maximum number to be shown in the macro report is 100.  
If there are more entries than the set maximum limit, the macro displays

- up to the defined limit of entries
- together with the following message with a link to the document activity report on the page with the additional entries

Showing most recent entries. There are more records in the Document Activity.

## Use with other macros

The document activity macro is compatible with the Confluence Page Properties macro and the Page Properties Report macro.

On the draft page, add the **document activity** macro as a table value in the **page properties** macro.

![Comala Document Activity macro page properties on a draft page](/cms_trial/assets/44e1714a-f9ac-45d6-b428-c2f8da9309d1.png)

Configure the document activity macro to select the document activity data to display for each entry and the number of entries to display.

The page properties report macro can then be added to a page to report on the added values.

![Comala Document Activity macro page properties report on a draft page](/cms_trial/assets/60dcc32e-d3c4-4586-9c96-dae7a74a9a9f.png)

## Exporting pages to PDF and Word

The document activity macro table of information is included when exporting to PDF or Word.

![image-20260629-184550.png](/cms_trial/assets/fadf4cc1-c941-4927-bde3-2ea98bfc94f3.png)

- User avatars are not included in the PDF or Word export
- Links are included in the Confluence version related to each document activity entry

Only the number of document activity entries specified in the macro configuration is included in the export. The link to the full Document Activity Report is not included in the PDF.

In the PDF and Word export, the date is in UTC format.

**Related topics**

- [Document Report](/cms_trial/space/CDMC/2193033420/Document+report+-+Space+level/)

- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)

- [Document Approvals](/cms_trial/space/CDMC/2192777118/Document+Approvals/)

- [States](/cms_trial/space/CDMC/2193066115/States/)