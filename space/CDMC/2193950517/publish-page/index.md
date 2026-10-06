# publish-page

## Overview

Requires the [Comala Publishing app](https://marketplace.atlassian.com/apps/143/comala-publishing?hosting=cloud&tab=overview).

Use the **publish-page** trigger action when you need greater flexibility and control over when and where a page is published to another space in your Confluence Cloud site. It’s ideal for complex workflows and staged content releases, publishing your pages automatically at different workflow stages.

![Comala visual editor publishpage trigger action configuration](/cms_trial/assets/1cd1110e-8961-4ab2-ba61-d27daa502f72.png)

You can use the **Publish Page** action in a **workflow trigger** to publish a page when a specific workflow event occurs.

By default, Comala Publishing publishes a page automatically when it reaches the workflow’s final state. When you add a **Publish Page** trigger action to the workflow, this automatic behavior is turned off. From that point, the page is published only on the events where you have added a **Publish Page** action. This applies as soon as the workflow contains a **Publish Page** action on any state, even if that state is never reached.

To publish the page when it reaches the final state, add a **Publish Page** action to that state. Automatic publishing is already off, so adding this action doesn't create a duplicate. The page publishes once, when it enters the final state.

If the page needs to publish at more than one point, for example on the final state and on another event, add a **Publish Page** action to each of those states.

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if they are met, the **Publish Page** action publishes the current page to a different space in the same Confluence Cloud site using the [Comala Publishing for Cloud app](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CPCL&title=Welcome%20to%20Comala%20Publishing%20for%20Cloud).

## `"publish-page"`

When added to a workflow trigger, publishes a single page on a workflow event to a different space using [Comala Publishing for Cloud app](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CPCL&title=Welcome%20to%20Comala%20Publishing%20for%20Cloud).

- **action (*****publish-page*****)**

This trigger action is only available when [Comala Publishing Cloud](https://appfire.atlassian.net/wiki/spaces/CPCL) is installed, and the current space has been enabled as a source space for publishing to the target space.

For the workflow shown below:

![Comala custom workflow flowchart with firstpublish state](/cms_trial/assets/53c33f4c-11d1-4e4d-8a0d-d7d7619c7f1b.png)

You can add the following workflow trigger using the visual editor:

![Comala visual editor trigger for firstpublish state with publishpage action](/cms_trial/assets/83d8ea1c-9d93-4e26-b6f7-0cfb7499e261.png)

This publishes the page on the state change to the **First Publish** state in the applied workflow.

The **Publish Page** action (the `“publish-page`” macro) publishes the content in the target space on the state change event.

![Comala page published confirmation message](/cms_trial/assets/524f325e-5495-4358-a156-1b2dab7aef03.png)

The content bylines are updated on the source space page.

![Comala publishing byline with synced workflow state and publishing dialog](/cms_trial/assets/d3e9f588-1d5f-4dd9-9b3b-51ce3ea6b014.png)

The target space for publishing the page is configured in the [Comala Publishing space settings](https://appfire.atlassian.net/wiki/spaces/CPCL/pages/646252290). Publishing can also occur based on the Comala Publishing app configuration, such as a space publishing action or a single-page publishing action, **including publishing on a transition to the workflow final state.**

Adding a workflow trigger with a **Publish Page** action prevents the Comala Publishing app from automatically publishing the page when it transitions to the final state. To publish on the final state, add a **Publish Page** trigger action for that state as well.

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

![Comala code editor publishpage trigger configuration](/cms_trial/assets/4a83fe4e-f95a-416b-96b5-afcf64c984b5.png)