# publish-page

## Overview

Requires the [Comala Publishing app](https://marketplace.atlassian.com/apps/143/comala-publishing?hosting=cloud&tab=overview).

Use the **publish-page** trigger action when you need greater flexibility and control over when and where a page is published to another space in your Confluence Cloud site. It’s ideal for complex workflows and staged content releases, publishing your pages automatically at different workflow stages.

![Comala visual editor publishpage trigger action configuration](/cms_trial/assets/0e0a723b-e154-4632-9e21-4eb36eee207f.png)

You can use the **Publish Page** action in a **workflow trigger** to publish a page when a specific workflow event occurs.

Adding a **Publish Page** trigger action **does not** disable the default **Comala Publishing** behavior on the transition to the final state. If both publishing actions are configured, publishing occurs on both the trigger event and the transition to the final state.

You should avoid using the **Publish Page** trigger action on a transition to the final state to prevent duplicate publishing of the same page version and publishing errors.

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if they are met, the **Publish Page** action publishes the current page to a different space in the same Confluence Cloud site using the [Comala Publishing for Cloud app](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CPCL&title=Welcome%20to%20Comala%20Publishing%20for%20Cloud).

## `"publish-page"`

When added to a workflow trigger, publishes a single page on a workflow event to a different space using [Comala Publishing for Cloud app](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CPCL&title=Welcome%20to%20Comala%20Publishing%20for%20Cloud).

- **action (*****publish-page*****)**

This trigger action is only available when [Comala Publishing Cloud](https://appfire.atlassian.net/wiki/spaces/CPCL) is installed, and the current space has been enabled as a source space for publishing to the target space.

For the workflow shown below:

![Comala custom workflow flowchart with firstpublish state](/cms_trial/assets/1e3a47cc-2a4e-420e-b4af-9a0aabb4aff6.png)

You can add the following workflow trigger using the visual editor:

![Comala visual editor trigger for firstpublish state with publishpage action](/cms_trial/assets/3055239d-6d59-4e0c-b6a3-954365105482.png)

This publishes the page on the state change to the **First Publish** state in the applied workflow.

The **Publish Page** action (the `“publish-page`” macro) publishes the content in the target space on the state change event.

![Comala page published confirmation message](/cms_trial/assets/3d03701a-a803-42b5-aa61-9bb6104be1b3.png)

The content bylines are updated on the source space page.

![Comala publishing byline with synced workflow state and publishing dialog](/cms_trial/assets/6706440b-a667-42c2-b378-f77ebff5f5c6.png)

The target space for publishing the page is configured in the [Comala Publishing space settings](https://appfire.atlassian.net/wiki/spaces/CPCL/pages/646252290). Publishing can also occur based on the configuration of the Comala Publishing app, such as a space publishing action or a single-page publishing action, including publishing on a transition to the workflow final state.

Adding a workflow trigger with a **Publish Page** action does not prevent the page from being published by the Comala Publishing app when the workflow transitions to the final state.

## Example trigger code

```text
"triggers":
[
	{"event": "on-change-state",
	"conditions":
	[
		{"state":"First Publish"}
	],
	"actions":
	[
		{"action": "publish-page"}
	]}
]
```

Workflow triggers can also be added and edited in the code editor.

![Comala code editor publishpage trigger configuration](/cms_trial/assets/a490215f-e94c-4941-a095-60d52480c204.png)