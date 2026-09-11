# Build a Campaign Brief Workflow with the Visual Builder Editor

## Overview

**Build a review workflow visually - no code required.**

The Visual Builder Editor in Comala Document Management for Cloud lets you create and edit workflows through a graphical interface. This guide builds a campaign-brief workflow from scratch and adds a Brand Review approval step between *Draft* and *Published*, so a Brand team signs off before anything goes live.

## The scenario

### Who this is for

A marketing team publishes campaign briefs in Confluence. With their current workflow, the brief moves straight from **Draft** to **Published** after a single approval. The team now wants to add a review step so the Brand team can check each brief before it goes live, without asking an administrator to write the workflow code.

- Each campaign brief is a Confluence page that carries the **campaign** label.
- The Brand team is automatically notified when a brief reaches its review step.
- Approved briefs publish on their own, while rejected briefs return to the author for revisions.

### What you'll build

A three-state workflow that routes every campaign-labeled brief through a Brand review before it publishes.

![Workflow diagram showing the completed three-state campaign brief workflow with a Brand Review approval before publication.](/cms_trial/assets/7f97fa17-da77-4796-aafc-e96aef8fca30.png)

### Prerequisites

- Comala Document Management for Cloud is installed on your Confluence site.
- You have space administrator permissions in the target space.
- The Brand reviewers exist as a Confluence group or as named users you can assign.
- Your campaign briefs share a content label. This guide uses **campaign**.

## Build the workflow

### 1. Open the Visual Builder Editor

- Go to your Confluence space and open **Space Settings**.
- Under *Space Apps*, select **Comala Document Management**.
- Select **Create New Workflow**.

The Visual Builder Editor opens with two panels. The **Workflow panel** on the left is where you make edits. The **Workflow Navigator** on the right shows the workflow as a live flowchart.

![Visual Builder Editor showing the Workflow panel and Workflow Navigator used to build and edit workflows.](/cms_trial/assets/38446e4f-af3e-45bd-8651-7ba58af4f19e.png)

### 2. Add the workflow details and a content label

In the **Workflow view** of the Workflow panel, set what the workflow is and where it applies.

- Enter a **name** (for example, *Campaign Brief*) and a short **description** that notes the Brand review step.
- Add the content label **campaign**. The workflow then applies only to pages that carry this label and ignores the rest of the space.
- Leave **Exclude labels** unchecked. Select it only to apply the workflow to pages *without* the label.
- Select **Apply** to save the panel.

  ![Workflow settings showing the workflow name, description, and content label configuration.](/cms_trial/assets/fdcaed1a-6919-477f-a887-64996b561b3c.png)

### 3. Add your states

States are the stages a brief moves through. Add three, in order:

- **Draft**: where authors write the brief.
- **Brand Review**: the new checkpoint for the Brand team.
- **Published**: the live, final state.

Select a state to open the **State view**, where you set its name and description. You can also set an optional **expiry due date** to time-box the review.

![State view showing the settings used to configure a workflow state.](/cms_trial/assets/759deda1-582f-49fb-b619-abf91b5035e5.png)

### 4. Add the approvals

An approval is what lets reviewers advance or send back a brief. Add one to each state that needs a sign-off.

- In **Draft**, open **Approvals**, select the **Approval** button, and name it *Submit for review*. Assign it to the brief's author or owner, then select **Apply**.

  ![Approval settings showing how to configure an approval in the Draft state.](/cms_trial/assets/03ca9a25-c65c-43b9-ae60-f6107ca2676b.png)
- In **Brand Review**, add an approval named **Brand Check** and assign it to the **Brand team** so they're notified when a brief reaches this step. Select **Apply**.

Use the **Authentication method** in the approval panel if you need an electronic signature or want to relabel the approve and reject buttons.

![Approval settings showing the authentication options for an approval.](/cms_trial/assets/ff270bf0-1630-4a2d-9d1c-89a946db67e7.png)

### 5. Connect the states with transitions

A state's **approved** and **reject** transitions become available only after that state has an approval, so add these after Step 4.

- In **Draft**, add an **Approved** transition and set its destination to **Brand Review**. A brief moves to the Brand team once it clears its first approval.

  ![Workflow diagram showing the Approved transition from Draft to Brand Review.](/cms_trial/assets/f53058ee-88d7-46f1-975f-8bd384bdb927.png)
- In **Brand Review**, set the **Approved** transition to **Published** and the **Reject** transition back to **Draft**.
- Leave **Published** with no outgoing transitions; it's the final state.

### 6. Save and exit

When the flow is complete, select **Save** in the Navigator panel to update the workflow and the app space settings, then select **Exit** to return to the workflows list.

![Workflow diagram showing the Approved and Reject transitions for the Brand Review state.](/cms_trial/assets/858bc650-53db-4338-828a-dfddbce3c3a5.png)![Visual Builder Editor showing the Save and Exit options after completing the workflow.](/cms_trial/assets/5100a6b4-7d2e-4d35-ab41-692a3429734a.png)

Prefer to check the underlying definition? The **code editor icon** switches to the JSON view at any time, and the editor supports Confluence's dark mode.

![JSON code editor showing the workflow definition generated by the Visual Builder Editor.](/cms_trial/assets/b4874515-bd47-4069-a8cc-9292c37664a2.png)

## Test the workflow

- Open a Confluence page labeled **campaign**. It enters the workflow at **Draft**.

  ![Confluence page showing the campaign workflow in the Draft state before review.](/cms_trial/assets/0c9809f2-50dc-4b90-b867-d2c97d318c09.png)
- Submit it for review. It moves to **Brand Review** and the Brand team is notified.
- When the Brand team approves, the brief moves to **Published**. If they reject it, it returns to **Draft**.

## Related topics

- [Visual builder editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/)
- [JSON code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/)
- [Workflow elements and concepts](/cms_trial/space/CDMC/2193066207/Workflow+elements+and+concepts/)