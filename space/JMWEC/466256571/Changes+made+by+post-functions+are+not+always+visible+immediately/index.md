# Changes made by post-functions are not always visible immediately

## Problem

Changes made by JMWE post-functions are *not* *always* visible just after the post-function execution. This is because JMWE post-functions (as any other post-functions implemented by JIRA Cloud add-ons) are processed asynchronously, after the transition completes. This helps ensure the stability and performance of your JIRA instance.

This problem is tracked by Atlassian at: <https://ecosystem.atlassian.net/browse/ACJIRA-1098>

## Workaround

You can either manually refresh the page to see the changes done by the post-function, or enable the "Auto-refresh issues" option in the [Configuration](/cms_trial/space/JMWEC/466288938/JMWE+Configuration/) page. This option is enabled by default.

## Related articles

|  |  |
| --- | --- |
| Related issues |  |