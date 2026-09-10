# Add participants automatically to new Jira Service Desk requests

The **Requested Participant** field can be set like any other custom field in Jira. However, referencing a custom field by its ID is not a best practice for SIL scripting. For more information on the preferred method of referencing custom fields, go to [Custom Fields Aliases](/cms_trial/space/PSJC/496206057/Custom+fields+aliases/).

The following action automatically adds a requested participant.

```text
customfield_10301 = assignee;
```