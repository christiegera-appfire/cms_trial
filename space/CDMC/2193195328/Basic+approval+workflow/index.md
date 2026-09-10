# Basic approval workflow

## Overview

The **Basic approval workflow** is a simple three-state template included with the app that ensures a clear approval process for your Confluence documents.

### **States and Transitions**

Workflow states indicate the status of the document. When the workflow is applied to a page or blog post, it can be in one of the following three states:

- Review – The document starts in this state and awaits rejection/approval.
- Rejected – If the document is not approved, it moves to the *Rejected* state.
- Approved – The document is approved and ready for publishing.

Transitions are the actions that will move the document between different states.

For example,

- Once you submit the page for review, the document is moved to the *Review* state.
- Once the assignee/reviewer approves, the document moves from *Review* to *Approved* state.
- The page automatically moves from *Review* to *Rejected* statewhen the reviewer rejects the document.

![Comala basic approval workflow state diagram](/cms_trial/assets/3ec5bee6-1720-40f7-b6a5-0e29861d8049.png)

The workflow transitions back to the **Review** state when a page editor updates a page in either the *Approved* or *Rejected* state.

## Next steps

[Apply workflows](/cms_trial/space/CDMC/2192870271/Apply+workflows/)

[Document activity](/cms_trial/space/CDMC/2193097355/Document+Activity/)