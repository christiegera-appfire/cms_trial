# Troubleshooting when using workflow extensions that operate on linked issues

If any workflow extension that operates on linked issues does not work as expected, there are a few things to look out for:

1. Make sure that you have selected the right link type under the “Issue Link Type”. The link type should be the link as it appears on the issue on which the transition that needs to be validated.
2. Make sure you have placed the post-function on the right transition. The workflow extension should be added to the transition of the workflow the current issue follows. For example, if you want to copy labels from the stories of the Epic, then you need to add the “Copy field value from linked issues” post-function to the transition of the Epic workflow.
3. Beware of the default "relates to" link type, which can cause confusion. The problem stems from the fact that "relates to" is both the *inward* *direction* and the *outward direction* of the "Relates" link type. We recommend that you rename one of the directions to "is related to" to avoid confusion. This can be done on the Issue Linking Jira admin page.