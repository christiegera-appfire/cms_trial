# Set Component/s field from a Cascading field

### Abstract

This code snippet sets the Component/s field from the value of a Cascading field. This is useful if you have a large number of Components that can be organized in categories, and want to make it easier for users to find the appropriate Component using a Cascading Select input (two dropdown lists).

### Logic

Access the Cascading custom field and return its parent and child values separated by a delimiter (that separates the categories in the Component/s)

### Snippet

```javascript
{% if issue.fields['<Name of the cascading field>'] %}
{{ issue.fields['<Name of the cascading field>'].value }}<Delimiter>{{ issue.fields['<Name of the cascading field>'] | field("child.value") }}
{% endif %}
```

### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| `<Name of the cascading field`> | Name of the field of type Cascading | `Functional Modules` |
| `<Delimiter>` | Delimiter of the parent and the child value | `/` |

### Examples

The output of this snippet is a [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) representing the name of a Component which you could use for example, to set the Component/s to `Human Resources - Recruitment`when`Human Resources`and`Recruitment`are selected as the parent and child in the Cascading select list, in:

- one of the Set field value post-functions
- the Create issue post-function under Set fields of new issue section
- one of the Transition issue post-functions on the transition screen, if any

  ```javascript
  {% if issue.fields["Functional Modules"] %}
  {{ issue.fields["Functional Modules"].value }}/{{ issue.fields["Functional Modules"] | field("child.value") }}
  {% endif %}
  ```

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing a cascading field](/cms_trial/space/JMWEC/465505179/User-created+Custom+Fields/)

### Related articles

|  |  |
| --- | --- |
| Related issues |  |