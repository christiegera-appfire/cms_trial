# Permission errors while executing post-functions

## Problem

Some of your post-functions do not seem to be working at all, and in the logs (accessible from the [Troubleshooting and support for JIRA Misc Workflow Extensions](/cms_trial/space/JMWEC/465503894/Help+and+Support/) page) you find errors such as *unauthorized* or *You do not have the permission to see the specified issue*.

The post-function is operating on;

- a project that has a non-standard Permission Scheme (such as a Service Desk project) or is using a Security Scheme
- an issue that has a security level set or
- a transition that has a [workflow property set](https://confluence.atlassian.com/adminjiracloud/workflow-properties-776636709.html) which restricts the "Run as" user from seeing/editing the issue

## Solution

Visit the [Verifying your JIRA instance after installation](/cms_trial/space/JMWEC/465504254/Verifying+Your+JIRA+Instance/) page for a list of possible JIRA configuration issues.

## Related articles

|  |  |
| --- | --- |
| Related issues |  |