# Find the earliest unreleased version scheduled after a certain date

### Abstract

This code snippet finds the earliest unreleased version scheduled after a certain date

### Logic

Access the available versions for the issue and find the earliest unreleased version scheduled after a certain date

### Snippet

```javascript
{% set vers = {} %}
{% for v in issue | projectInfo | field("versions") %}
  {% if not v.released and v.releaseDate >= <Specific date> and (vers.releaseDate == null or vers.releaseDate > v.releaseDate) %}
    {% set vers = v %}
  {% endif %}
{% endfor %}
{{vers.name}}
```

### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| <Specific date> | Access the field of type Date | `issue.fields.duedate` |

### Examples

The output of this snippet is a [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) representing the *name* of a Version which you can use in a template, for example, to set the Fix Version/s of an issue to the earliest unreleased version scheduled after the Due date in:

- one of the Set Field Value post-functions
- one of the Transition issue post-functions on the transition screen, if any
- the Create issue post-function under Set fields of new issue section

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [projectInfo filter](/wiki/spaces/MWECS/pages/78482118/Custom+Filters#projectInfo)
- [field filter](/wiki/spaces/MWECS/pages/78482118/Custom+Filters#field)

### Related articles