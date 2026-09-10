# Set an Estimate of the issue to the difference of two specific dates

### Abstract

This code snippet sets an Estimate field to the difference of two specific dates of the issue.

### Logic

Access the date fields of the issue and return their difference

### Snippet

```javascript
{{ <Date object> | date('diff',<Second date>,'days') }}d
```

### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| <Date Object> | Value of the first date field | `issue.fields.updated` |
| <Second Date object> | Value of the second date field | `issue.fields.created` |

### Examples

The output of this snippet is a String representing a duration which you could use to Set an estimate field. Eg: Set the Original estimate of the issue to the difference of the issue creation and Due date in

- one of the Set Field Value post-functions
- one of the Transition issue post-functions on the transition screen, if any
- in the Create issue post-function under Set fields of new issue section

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)

### Related articles

|  |  |
| --- | --- |
| Related issues |  |