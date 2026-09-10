# Read-only text fields are not present in JMWE Clear fields post-function

**Observation:**

Read-only text fields are not present in [Clear fields JMWE](/cms_trial/space/JMWEC/466226128/Clear+fields/) post-function

*Custom field:*

![JMWE for Jira Cloud field selection interface showing readonly field limitations](/cms_trial/assets/2e60ba0d-d155-4029-82e0-cf1b27e848a7.png)

[Clear fields JMWE](/cms_trial/space/JMWEC/466226128/Clear+fields/) *post-function:*

![JMWE for Jira Cloud clear fields post function configuration with field options](/cms_trial/assets/4529f0d1-2648-47c7-9bf8-c4dca59533a9.png)

**Reason:**

We cannot clear read-only text fields with the Clear Fields Post function due to a Jira Cloud limitation. Please refer to the Atlassian ticket: <https://jira.atlassian.com/browse/JRACLOUD-62188>

Hence we’ve removed these types of fields from the dropdown of [Clear fields JMWE](/cms_trial/space/JMWEC/466226128/Clear+fields/) post-function: [MWEC-782](https://appfire.atlassian.net/browse/MWEC-782)