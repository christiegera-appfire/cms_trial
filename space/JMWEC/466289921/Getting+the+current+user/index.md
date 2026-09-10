# Getting the current user

### Abstract

This code snippet fetches the user who triggered the current transition.

### Logic

This snippet uses the [currentUser](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/) built-in variable to fetch the user object representing the user who triggered the current transition.

### Snippet

```javascript
{{ currentUser }}
```

### Examples

The output of this code snippet is a user object representing the current user which you could use to:

- Set a User picker field to the current user. Eg: Assign the issue to current user in one of the Set Field Value post-functions, using the "Treat value as JSON" option
- Set a User picker field to the current user in:

  - one of the Transition issue post-functions on the transition screen, if any
  - in the Create issue post-function under Set fields of new issue section

    ```text
    {{ currentUser.accountId }}
    ```
- Conditionally execute a post-function or Unlink issues - Eg: Check that the current user is the Reporter of the issue

  ```text
  {{ currentUser.accountId == issue.fields.reporter.accountId }}
  ```
- Notify the customer that the issue raised by them is being handled by the current user through the

  - Comment in one of the Comment issue post-functions
  - Subject/HTML body/Text body of Email issue post-function

    ```text
    Hi {{ issue.fields.reporter.accountId }}. Your issue is being handled by {{ currentUser.accountId }}.
    ```
- Write a JQL search expression in the Link issues to current issue post-function - Eg: Link issues assigned to the current user

  ```text
  assignee = {{ currentUser.accountId }}
  ```

### References

- [currentUser variable](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/)
- [Accessing the fields of an issue](/cms_trial/space/JMWEC/465373107/Issue+and+Transition+Data+in+Nunjucks/)

### Related articles

|  |  |
| --- | --- |
| **Related issues** |  |