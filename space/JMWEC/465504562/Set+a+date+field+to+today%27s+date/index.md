# Set a date field to today's date

### Abstract

This code snippet sets a date field to today's date

### Logic

Pass today's date

### Snippet

```javascript
{{ now }}
```

### Context

The output of the code snippet is a [Moment.js](/cms_trial/space/JMWEC/466323491/date+filter/) date object which you could use to:

- Set a Date/Date-time picker field - Eg: Set the Due date to today in

  - one of the Set Field Value post-functions
  - one of the Transition issue post-functions on the transition screen, if any
  - in the Create issue post-function under Set fields of new issue section
- Conditionally execute a post-function or Unlink issues - Eg: Estimated delivery date is less than today

  ```javascript
  {{ issue.fields["Estimated Delivery Date"] < now }}
  ```
- Notify the customer when the issue has been rejected as invalid through the

  - Comment in one of the Comment issue post-functions
  - Subject/HTML body/Text body of Email issue post-function

    ```javascript
    Your issue has been rejected on {{ now | date('dddd, MMMM Do YYYY') }} since it is invalid.
    ```
- Write a JQL search expression in Link issues to current issue post-function. Eg: Link issues which have been created since yesterday

  ```javascript
  created >= {{ now | date('subtract' , 1 , 'days') }}
  ```

### References

- [date filter](/cms_trial/space/JMWEC/466323491/date+filter/)
- [Accessing the fields of an issue](/cms_trial/space/JMWEC/465373107/Issue+and+Transition+Data+in+Nunjucks/)

### Related articles

|  |  |
| --- | --- |
| Related issues |  |