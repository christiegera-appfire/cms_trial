# publish-page

## Overview

Requires the [Comala Publishing app](https://marketplace.atlassian.com/apps/143/comala-publishing?hosting=cloud&tab=overview).

Use the **publish-page** trigger action when you need greater flexibility and control over when and where a page is published to another space in your Confluence Cloud site. It’s ideal for complex workflows and staged content releases, publishing your pages automatically at different workflow stages.

![Comala visual editor publishpage trigger action configuration](/cms_trial/assets/5513d2b4-997d-42a4-8bf6-06490999684a.png)

You can use the **Publish Page** action in a **workflow trigger** to publish a page when a specific workflow event occurs.

By default, Comala Publishing publishes a page automatically when it reaches the workflow’s final state. When you add a **Publish Page** trigger action to the workflow, this automatic behavior is turned off. From that point, the page is published only on the events where you have added a **Publish Page** action. This applies as soon as the workflow contains a **Publish Page** action on any state, even if that state is never reached.

To publish a page when it reaches the final state, configure a Publish Page trigger action for that transition. Because automatic final-state publishing is disabled, this does not cause duplicate publishing.

To publish a page on the final-state transition and on other workflow events, configure a separate Publish Page trigger action for each required event.

When the workflow trigger event occurs, the trigger checks that any required conditions are met, and if they are met, the **Publish Page** action publishes the current page to a different space in the same Confluence Cloud site using the [Comala Publishing for Cloud app](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CPCL&title=Welcome%20to%20Comala%20Publishing%20for%20Cloud).

## publish-page

When added to a workflow trigger, publishes a single page on a workflow event to a different space using [Comala Publishing for Cloud app](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=CPCL&title=Welcome%20to%20Comala%20Publishing%20for%20Cloud).

- **action (*****publish-page*****)**

This trigger action is only available when [Comala Publishing Cloud](https://appfire.atlassian.net/wiki/spaces/CPCL) is installed, and the current space has been enabled as a source space for publishing to the target space.

For the workflow shown below:

![Comala custom workflow flowchart with firstpublish state](/cms_trial/assets/81536291-87e9-41a7-a8ae-e4565b9c0a08.png)

You can add the following workflow trigger using the visual editor:

![Comala visual editor trigger for firstpublish state with publishpage action](/cms_trial/assets/234af90b-8dc8-4569-afa2-491a18565b2c.png)

This publishes the page on the state change to the **First Publish** state in the applied workflow.

The **Publish Page** action (the `“publish-page`” macro) publishes the content in the target space on the state change event.

![Comala page published confirmation message](/cms_trial/assets/b95c7312-8a52-4514-8d11-8fa36eab8c05.png)

The content bylines are updated on the source space page.

![Comala publishing byline with synced workflow state and publishing dialog](/cms_trial/assets/d6547293-a7f7-4ca0-802a-115d9f1c6336.png)

The target space for publishing the page is configured in the [Comala Publishing space settings](https://appfire.atlassian.net/wiki/spaces/CPCL/pages/646252290). Comala Publishing also supports other publishing methods, such as space publishing and [single-page publishing](https://appfire.atlassian.net/wiki/spaces/CPCD/pages/1088783615).

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

![Comala code editor publishpage trigger configuration](/cms_trial/assets/107f12da-439d-4238-a095-72186a3c8348.png)