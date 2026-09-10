# Most post-functions are now executed as "Jira Misc Workflow Extensions" instead of the current user

## Problem

Most post-functions now operate as the system "Jira Misc Workflow Extensions" add-on user instead of the current user. Therefore, updates will appear to be done by the JMWE add-on user rather than the user who transitioned the issue, thereby changing the Issue history and notification author.

## Solution

None. This is a security requirement of the Atlassian Connect framework.

## Related articles

|  |  |
| --- | --- |
| **Related issues** |  |