# Fetch the value of a multi-value field when you know it has only one value

### Abstract

This code snippet retains the *only* value of a multi-valued type field which can either be an array of objects or a set of values. This snippet is useful when you know that the array has only one value and hence by applying the first or last methods you can retain it.

### Logic

Use the first/last filter to get the only object of the field and access the specific field for the required value.

### Snippet

```javascript
{# Apply the first/last filter to the array of objects. Upon that apply the field filter #}
{{ issue.fields["<Multi-valued field>"] | <filter> | field("<Value>") }}
```

### Placeholders

| **Placeholder** | **Description** | **Example** |
| --- | --- | --- |
| `<Multi-value field`> | Name of the multi-valued field | `Technical tasks` |
| `<filter>` | Filter to be applied | `first` |
| `<Value>` | Value to fetch | `value` |

Since you already know the collection of objects has *only* one value you could use the `last`filter as well.

### Examples

The output of the code snippet is the *only* value of a multi-valued field which you could use in a template, for example to:

- Set a field in one of the Set field value post-functions or the Create issue post-function under the Set fields of new issue section. Examples:

  - Assign the issue to the author of the last comment

    ```javascript
    {{ issue.fields.comment.comments | last | field("author.accountId") }}
    ```
  - Name of the issue link type of the only linked issue to the current issue

    ```javascript
    {{ issue.fields.issuelinks | first | field("type.name") }}
    ```
- Send an email to the first user of a Multi-user picker field in the Email issue post-function

  ```javascript
  {{ issue.fields["Multi-user picker"] | first | field("accountId") }}
  ```

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing the fields of an issue](/cms_trial/space/JMWEC/465373107/Issue+and+Transition+Data+in+Nunjucks/)
- [first filter](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/),[last filter](/cms_trial/space/JMWEC/465373240/Nunjucks+Filters/) and [field filter](/cms_trial/space/JMWEC/465373638/Custom+filters/)

### Related articles

|  |  |
| --- | --- |
| **Related issues** |  |