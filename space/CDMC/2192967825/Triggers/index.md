# Triggers

## Overview

A **workflow trigger** adds flexibility and automation to your documentation process. When triggered, it can automatically perform one or more actions, such as changing the state, completing an approval, sending a custom email, or removing Confluence page restrictions.

### **Examples of workflow triggers:**

- **Send a notification** when a page is submitted for review.
- **Change the page state** automatically when it's edited.
- **Assign reviewers** when a page enters a specific state.
- **Add a label or comment** when a transition occurs.

Triggers can be configured to:

- Listen for **when** a single workflow `event` occurs
- Check **if** the required `conditions` are met for the event
- If met, **then** undertake one or more `actions`

## Trigger elements

Workflow triggers consist of the following elements:

[Trigger events](/cms_trial/space/CDMC/2193950329/Trigger+events/)

[Trigger conditions](/cms_trial/space/CDMC/2193852785/Trigger+conditions/)

[Trigger actions](/cms_trial/space/CDMC/2192870598/Trigger+actions/)

## Adding a trigger to a workflow

A space administrator can add one or more workflow triggers to a custom workflow using either the [visual editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/) or the [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/).

- Use the **Add trigger** dialog box in the visual editor.

![image-20260625-144910.png](/cms_trial/assets/2a7f1e29-baa8-4554-8c67-37ff2700b2d5.png)

The event and condition are chosen from a drop-down list of available options.

You can then include one or more **Actions** for the trigger using the **Add Action** option, such as the **Set Message** action.

![image-20260625-145046.png](/cms_trial/assets/1aeaa7f7-f87c-4487-8485-218f99aeead3.png)

The added trigger is automatically updated in the [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/).

![Comala code editor with saved trigger configuration](/cms_trial/assets/8c8008cc-2a1f-45fd-8db2-ff3394f33444.png)

You can also add a workflow trigger in the code editor, which includes a JSON schema to help you.

![Comala code editor JSON schema help for trigger events](/cms_trial/assets/749e2492-eee8-42bd-83ec-fc7919e387bf.png)

You can toggle between the code editor and the visual editor. Changes made in one editor are automatically updated in the other editor.

The workflow triggers added to a workflow are listed in the visual builder.

![image-20260625-145231.png](/cms_trial/assets/38e9d749-2b68-4c8d-be1a-2dfdf96f8382.png)