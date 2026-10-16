# Build-your-own (Nunjucks scripted) post function

This post function allows you to run an Nunjucks template (script) when a transition is triggered. This can be used to create entirely custom own post functions.

[Unmapped macro: 47fa61b6-fe1c-40c9-b236-623cdbc35833/4d8fa66b-88bf-4899-a37e-5926131c46ac/static/multiexcerpt-fast-include-block-macro — no content to fall back on]

![Scripted post function configuration screen](/cms_trial/assets/9ae373e6-b333-4590-aa2b-0adecbf1674f.png)

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

## Custom script

Configure your custom script:

- **Description** - Give the post function a meaningful description.
- **Nunjucks script** - Enter the script that should be executed when the post function runs.

## Advanced options

Expand this section to see advanced configurations including delayed execution.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post function, so that the sub-tasks are created before they are transitioned.

Where possible, it is recommended to use the [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+post+functions/) post function or [Shared action](/cms_trial/space/JMWEC/466323396/Shared+Action+post+function/) post function to execute a series of post functions in a specific sequence instead of applying a delay.