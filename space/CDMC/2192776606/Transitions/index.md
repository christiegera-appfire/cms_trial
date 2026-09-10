# Transitions

## Overview

**Workflow transition** is the action that moves a document from one **workflow state** to another. Transitions define the path a document follows through its lifecycle, such as from draft to review or from review to approval.

![Workflow overview diagram showing workflow states.](/cms_trial/assets/318cbd78-650a-438b-8296-8d8b1b97211c.png)

## Types of transitions

Each transition can be triggered manually (for example, by a user clicking a button) or automatically (for example, using a trigger or rule).

You can add multiple transitions to a state, but only one of each transition type (automatic or manual) can be added to that state. Each transition is added to a specific state and includes its type and destination state.

## Automatic transitions

These transitions occur without user interaction, based on workflow events or conditions:

### Approved transition

- Occurs when a user (or all assigned users) approves the content.
- It can only be added to a state with content review (approval).

![Workflow editor showing an approved transition configured for a workflow state.](/cms_trial/assets/4c042100-9a32-4253-bf9c-d50430421c10.png)

### Rejected transition

- Occurs when a user (or all assigned users) rejects the content.
- Can only be added to a state that has a content review (approval).

![Workflow editor showing a rejected transition configured for a workflow state.](/cms_trial/assets/20a81a77-93ee-4dd3-bad6-bbafcaa3dc92.png)

### Updated transition

The **updated** transition must be added to the state. Can be added alongside other transition options, for example, a content review or a select transition.

- Occurs when a user edits and saves a change to the content.
- An **updated** transition removes any reviewers previously assigned using the workflow dialog if the state also contains a content review.

  ![Workflow editor showing an updated transition configured for a workflow state.](/cms_trial/assets/8a0bc67c-346e-460a-9a39-19ea214225c4.png)

Adding or removing a label or attachment does not affect the **updated** transition.

### Expired transition

The expired transition must be added to the state, which must be configured with a due date.

- Occurs when a due date added to the state is reached.
- If no due date is added (or has been removed before the due date), no expiry occurs.
- The [content expiry workflow](/cms_trial/space/CDMC/2192776431/Content+expiry+workflow/) has an **expired** transition added to the **Approved** state.

  ![Workflow editor showing an expired transition configured for a workflow state.](/cms_trial/assets/ec6a37b4-f7af-400d-94ca-f378b970cc39.png)

A state can have one, more than one, or all of these possible transitions. The **approved** and **rejected** transitions are only available when the state contains an approval (content review).

Transitions can also occur due to a trigger action listening for a workflow event, such as a change of state or a page approval. These can be added to the workflow as a JSON trigger.

## Manual transitions

These require the user to trigger the transition:

- **Select** – allows the user to choose from one or more destination states when transitioning the content.

  ![Workflow editor showing a Select transition configured with multiple destination states.](/cms_trial/assets/9c58d22c-8ba2-4328-9f97-35b8983f49d2.png)

### **Select transition**

A select transition moves the page to another state based on your selection.

- When a state has select transitions configured, the *Workflow State* dialog displays a **Possible transitions** section. Each available transition is shown with its name and destination state.
- Click the transition name to move the page to the destination state.

  ![Workflow State Dialog displaying available select transitions for the current workflow state.](/cms_trial/assets/9f514976-3c63-417b-8324-80ca85684199.png)
- The **select** transition can’t be added to a state that contains an approval.

**Related topics**

- [States](/cms_trial/space/CDMC/2193066115/States/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)
- [Workflow visual builder editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/)