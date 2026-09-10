# Prevent duplicate issue creation by the Create issue(s) post-function

This article describes how to avoid the creation of a second issue by the [Create issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function when the same transition is triggered a second time. For example, if you are using a Create Issue(s) post-function on the "Escalate" transition of a support workflow to create a separate "Escalation" ticket, you will want to avoid re-creating a new "Escalation" ticket if the Escalate transition is run a second time in the lifetime of the support request.

The idea is to use Conditional Execution to prevent the Create Issue(s) post-function from creating a new issue when an existing issue already created by that post-function can be found. There are multiple ways to achieve this, based on the specifics of your workflow.

Note that approaches 1 and 2 detailed below will work only when the current issue is linked to the newly created issue (using the "Link to new issue" option of the Create Issue(s) post-function). Approach 3 will work in all cases.

## Approaches

1. [Unmapped macro: legacy-content — no content to fall back on]
2. [Unmapped macro: legacy-content — no content to fall back on]
3. [Unmapped macro: legacy-content — no content to fall back on]

## Related articles

[unmapped inline: placeholder]

|  |  |
| --- | --- |
| **Related issues** |  |