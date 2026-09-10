# States

## Overview

A **workflow state** represents a specific stage in the document lifecycle. When a workflow is applied to a page or blog post in your Confluence space, a *workflow state byline* is added to the page or post, indicating the current workflow state.

Here are a few examples of workflow states:

- **Draft** – The document is being created or edited.
- **In Review** – The document is awaiting approval from assigned reviewers.
- **Approved** – The document has passed all required reviews.
- **Published** – The content is finalized and published.
- **Rejected** – The document did not pass review and needs changes.
- **Expired** – The document has passed its expiration date.

A workflow state is a milestone in your documentation process. The document can only be in one state at a time.

![Workflow state byline showing the current state and its status indicator.](/cms_trial/assets/a7380fb8-9d14-4ed2-88b6-658f434b349b.png)

Each state in a workflow has:

- a unique name
- a colored state byline circle
- an (optional) description

A state can also have several attributes, including:

- The [transitions](/cms_trial/space/CDMC/2192776606/Transitions/) available from one state to another.
- The requirement to complete a content review in the state.
- The ability to assign reviewers to the content review.
- The option to set a due date for the state's expiry.

A single state in a workflow can be set as the workflow’s final state.

Each state in a custom workflow can be edited using the [workflow builder visual editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/) and the [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/).

## Workflow state

The name of the current workflow state is displayed next to a colored status indicator circle on the page.

1. Click the **state byline** link to open the workflow dialog.
2. The workflow dialog displays the state's attributes (state name or approval name, if present; any added state description; and expiration period).

![Workflow state dialog displaying the current state name, description, and expiry information.](/cms_trial/assets/495ef1cd-6652-4e12-9d1d-f2b86e44058b.png)

### State select transition

Each workflow state can have rules or conditions associated with it, such as who can edit the page or what transitions are available.

When a state has one or more transitions configured, the *Workflow State* dialog displays a **Possible transitions** section at the bottom. Each available transition is shown as a button with its name and destination state.

![Workflow state dialog showing available transitions to other workflow states.](/cms_trial/assets/77bbbc0c-a66f-425f-a965-3604b5e7a1a1.png)

To transition to another state, click the transition button. The page moves to the destination state.

For example, a page in the *Approved* state might show two possible transitions:

- **EXPIRED** → Expired

- **UPDATED** → Review

You can’t add a select transition to a state with a content review. States with content reviews use **Approve** and **Reject** buttons instead.

![Workflow state dialog displaying Approve and Reject actions for a content review.](/cms_trial/assets/029e2a53-8830-400a-bb4e-9efc49f3c5ea.png)

### Workflow final state

A single state in a workflow can be set as a **final** state. The default state byline circle for a **final** state is **green**.

![Workflow state dialog showing a workflow's final state.](/cms_trial/assets/9885b5c3-25c2-49a3-b977-191577276020.png)

The final state is your final approved workflow state for the document. A good practice is to have no direct transitions, content reviews, or select transitions in the final state. In this case, the workflow dialog only contains a link to the document activity report.

To view which workflow is applied to the page, click the workflow title. This displays the details of the current workflow.

![Workflow details page opened from the workflow title.](/cms_trial/assets/b8b42ea8-9899-4c7b-9cca-15db16a3891d.png)

**Related topics**

- [Transitions](/cms_trial/space/CDMC/2192776606/Transitions/)
- [Workflow builder visual editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/)
- [Code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)