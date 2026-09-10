# Create transition fails when post-functions are placed inappropriately

## Problem

When a post-function is placed at the top of the list of post-functions on the Create transition, issue creation fails and throws an error. This is a consequence of a JIRA Cloud bug: <https://ecosystem.atlassian.net/browse/ACJIRA-961>

## Solution

You need to place any JMWE post-function *after* the **Creates the issue originally** built-in post-function.

## Related articles

|  |  |
| --- | --- |
| Related issues |  |