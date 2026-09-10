# Content expiry workflow

## Overview

The **Content expiry workflow** is designed to keep your content up to date. It builds on the Basic Approval workflow: approved pages expire after a set period so they can be reviewed again. It ensures regular checks for accuracy and relevance, reducing the risk of outdated information. Customizable expiration periods and email notifications enhance usability, making it a valuable tool for maintaining high-quality documentation.

The expiration time is set to five months by default. It can be modified for all pages in the space or adjusted for individual pages after they are *approved*.

## Workflow states

The content expiry workflow consists of four states:

**Review**: The page is awaiting review.

**Rejected**: The page was reviewed and rejected.

**Approved**: The page has been approved. Once the deadline is reached, this state will automatically transition to **Expired**.

**Expired**: The page has passed its expiration date. If the content is still valid, you can reapprove it.

![Comala content expiry workflow state diagram](/cms_trial/assets/531c4d82-ce24-41ed-945e-66661f1f55a9.png)

Each time the page is edited in either the ***Approved***, ***Rejected,*** or ***Expired*** state, the workflow transitions back to the ***Review***state (an **updated** transition).

## Approved state expiry

Pages in the **Approved** state have an expiry due date. The workflow dialog box in the **Approved** state displays the expiry date.

![Approved workflow dialog showing the expiry date.](/cms_trial/assets/cc0cb57f-ef70-44ad-a38e-0b895cde5d38.png)

Once this due date period has passed, the page transitions to the **Expired** state.

![Expired workflow dialog showing Approve and Reject actions.](/cms_trial/assets/22874def-49f0-4741-aa1d-17df0c5f74d3.png)

If you edit content in the **Expired** state and save the changes, the workflow automatically moves the page to the **Review** state.

You can also review content directly in the **Expired** state:

- If the content is **outdated** or needs updates, selecting **Reject** moves it to the **Rejected** state.
- If the content is still **relevant and accurate**, selecting **Approve** returns it to the **Approved** state.

## Edit the due date

You can edit the expiration date when the content is **approved**.

To edit the due date:

1. Click the expiry clock icon in the workflow dialog.

1. ![image-20260619-174858.png](/cms_trial/assets/7d59e716-37cf-4b02-bbea-e3c0235d39c6.png)

   Select the current expiry date to open the calendar.

   ![Calendar for selecting a new expiry date.](/cms_trial/assets/677ab9f7-b6a3-4079-a86c-5d12131d398d.png)

1. Choose a date and click **Save** to change the **Approved** state expiry date.

## Parameters

The **expiration** workflow parameter sets the due date. By default, it’s set to five months after the page moves to the **Approved** state.

To edit the expiration parameter:

1. Under **Space Apps**, select **Comala document management** in your Confluence space.
2. Choose the **@ Parameters** option to open the **Parameters** dialog box. This optionis displayed only when the workflow is enabled in the dashboard.

   ![Parameters page showing the expiry workflow parameter.](/cms_trial/assets/502a1c6c-cb25-4a63-b630-71dd9746aab6.png)

1. Update the expiration date as required in the **Parameters** dialog box.

   ![Parameters dialog for editing the expiry value.](/cms_trial/assets/45f0d877-57a5-4532-9a43-677f4dce29a8.png)

## Available expiration date formats

You can configure the expiration period using different formats, including:

- **Period of time:** Years, months, hours, or minutes (for example, "5 months").
- **Fixed date:** A specific date on the calendar.
- **ISO 8601 duration:** `P1Y6M` (1 year and 6 months).
- **Value reference:** Use another workflow parameter to dynamically set the expiration date.

  ![Example of supported expiry date formats in the Parameters dialog.](/cms_trial/assets/6aab3eca-afa7-40a9-8ab4-30a942e3d678.png)

The value set in the **space configuration** is applied when a workflow is first added to a page or blog post. Updating the value later in the space configuration won’t affect pages where the workflow has already been applied. Those pages will keep using the original value.