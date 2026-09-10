# Add certain number of minutes/hours/days/weeks/months to a date

### Abstract

This code snippet adds a certain number of minutes/hours/days/weeks/months to a Date field.

### Logic

Access the date and add the number of minutes/hours/days/weeks/months to it.

### Snippet

```javascript
{{ <Date field> | dateadd(<Number of units>,"<Unit>") }}
```

### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| `<Date Object`> | Access a date field | `issue.fields.created` |
| <Number of units> | The number of units to be added | `5` |
| `<Unit>` | `is one of "days", "hours", "weeks" or "months" (or their equivalent: "d", "h", "w", "m")` | `days` |

### Examples

The output of the code snippet is a [Moment.js](/cms_trial/space/JMWEC/466323491/date+filter/) date object which you could use to:

- Set a Date/Date-time picker field - Eg: Set the Due date to issue created plus 1 month in

  - one of the Set Field Value post-functions
  - one of the Transition issue post-functions on the transition screen, if any
  - in the Create issue post-function under Set fields of new issue section

    ```javascript
    {{ issue.fields.created | dateadd(1,"m") }}
    ```
- Conditionally execute a post-function or Unlink issues - Eg: Check that the issue has been resolved for more than 10 days

  ```javascript
  {{ now > issue.fields.Resolved | dateadd(10,"d") }}
  ```
- Notify the customer that the issue will be resolved in 6 hours from now through the

  - Comment in one of the Comment issue post-functions
  - Subject/HTML body/Text body of Email issue post-function

    ```javascript
    Your issue will be resolved on/before {{ now | dateadd(6,"hours") }}
    ```
- Write a JQL search expression in the Link issues to current issue post-function - Eg: Link issues whose "Planned Delivery date" is less than two days

  ```javascript
  {{ issue.fields["Planned Delivery Date"] < now | dateadd(2,"d") | date('YYYY-MM-DD') }}
  ```

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [now variable](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/)
- [Date filter](/cms_trial/space/JMWEC/466323491/date+filter/)

### Related articles

|  |  |
| --- | --- |
| Related issues |  |