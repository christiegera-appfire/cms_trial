# Find the next unreleased version

### Abstract

This code snippet fetches the next unreleased version available for the current issue

### Logic

Access the available versions for the issue and filter the next unreleased version by the version date

### Snippet

```javascript
{% set vers = {} %}
{% for v in issue | projectInfo | field("versions") %}
  {% if not v.released and (not vers.releaseDate or vers.releaseDate >= v.releaseDate) %}
    {% set vers = v %}
  {% endif %}
{% endfor %}
{{vers.name}}
```

### Placeholders

N/A

Examples

The output of this code is a String representing a Version which you could use in a template, for example, to set a Version picker field in:

- one of the Set Field Value post-functions
- one of the Transition issue post-functions on the transition screen, if any
- the Create issue post-function under Set fields of new issue section

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [projectInfo filter](/wiki/spaces/MWECS/pages/78482118/Custom+Filters#projectInfo)
- [field filter](/wiki/spaces/MWECS/pages/78482118/Custom+Filters#field)

### Related articles