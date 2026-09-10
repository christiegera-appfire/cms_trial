# Fetch the comment added during a transition

### Abstract

This code snippet fetches the comment added during a transition

### Logic

Access the body of the last comment of the issue, if it was created less than 6 seconds before.

### Snippet

```javascript
{% if issue.fields.comment.comments and now | date('diff',issue.fields.comment.comments | last | field("created")) < 6000 %}
{{ issue.fields.comment.comments | last | field("body") }}
{% endif %}
```

### Placeholders

NA

### Examples

The output of this snippet is a [String](http://docs.oracle.com/javase/6/docs/api/index.html?java/lang/String.html) which you can use to:

- Set a text field with the comment that was just created. Eg: Set a custom text field to the comment that was just added in one of the Set field value post-functions
- Notify of the most recent comment. Eg: Adding the most recent comment on the issue to its linked issues or as subject of an Email etc

  - Comment in one of the Comment issue post-functions
  - Subject/HTML body/Text body of Email issue post-function

    ```javascript
    {% if issue.fields.comment.comments and now | date('diff',issue.fields.comment.comments | last | field("created")) < 6000 %}
    A comment: "{{ issue.fields.comment.comments | last | field("body") }}" has been added on the linked issue.
    {% endif %}
    ```

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [issue variable](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/)
- [Accessing JIRA Standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [now variable](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/)
- [date filter](/cms_trial/space/JMWEC/466323491/date+filter/), [last filter](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/) and [field filter](/cms_trial/space/JMWEC/465373638/Custom+filters/)

### Related articles

|  |  |
| --- | --- |
| Related issues |  |