# Add a certain number of days to a date excluding the weekends

### Abstract

This code snippet adds a certain number of days to a date excluding the weekends. Currently, when you add a certain number of days to a date the weekends are included. To exclude them, you can use this snippet.

### Snippet

```javascript
{{ <fromDate> | date('businessAdd', <nod> ) | date }}
```

### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| `<fromDate`> | Date to which the number of days should be added | `now` |
| `<nod>` | Number of days to add | `22` |

Examples

The output of the code snippet is a [Moment.js](/cms_trial/space/JMWEC/466323491/date+filter/) date object which you could use to:

- Set a Date/Date-time picker field - Eg: Set the Due date to issue created plus 5 days excluding weekends in

  - one of the Set Field Value post-functions
  - in the Create issue post-function under Set fields of new issue section

    ```javascript
    {{ issue.fields.duedate | date('businessAdd', 5 ) | date }}
    ```
- Notify the customer that the issue will be resolved in 6 days from today through the

  - Comment in one of the Comment issue post-functions
  - Subject/HTML body/Text body of Email issue post-function

    ```javascript
    Your issue will be resolved on or before: {{ issue.fields.created | date('businessAdd', 6 ) | date }}
    ```

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [now variable](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/)
- [Date filter](/cms_trial/space/JMWEC/466323491/date+filter/)
- [businessAdd filter](/cms_trial/space/JMWEC/466323491/date+filter/)

### Related articles

|  |  |
| --- | --- |
| Related issues |  |