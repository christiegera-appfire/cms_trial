# Checking the value of a multi-valued field

### Abstract

This code snippet checks the value of a standard or custom multi-valued type field (typically a [multi-select field](/cms_trial/space/JMWEC/465505179/User-created+Custom+Fields/)). The multi-valued fields can either be an array of objects or an array of values.

### Logic

Iterate over the array of objects or values and check a specific field for the required value.

### Snippet

#### For multi-select fields:

```javascript
{# Checks if a specific option is selected #}
{{ issue.fields["<Name of the field>"] | find({"value":"<Value of the desired option>"}) != null }}
```

#### Placeholders

| **Placeholder** | **Description** | **Example** |
| --- | --- | --- |
| `<Name of the field`> | Name of the multi-select field | `Checkboxes` |
| `<Value of the desired option>` | Value of the option. | `Verification done` |

#### For multi-versions/users/components/groups fields (e.g. Fix Version/s):

```javascript
{# Checks if a specific version is selected #}
{{ issue.fields["<Name of the field>"] | find({"name":"<Name of the desired version>"}) != null }}
```

#### Placeholders

| **Placeholder** | **Description** | **Example** |
| --- | --- | --- |
| `<Name of the field`> | Name of the multi-valued version field | `fixVersions` |
| `<Name of the desired version>` | Name of the version to find | `2.0` |

#### For Labels field:

```javascript
{# Checks if a specific label is present #}
{{ issue.fields["<Name of the field>"] | find("<Desired label>") != null }}
```

#### Placeholders

| **Placeholder** | **Description** | **Example** |
| --- | --- | --- |
| `<Name of the field`> | Name of the labels field | `Labels` |
| `<Desired label>` | Label to find | `New` |

### Examples

The output of this snippet is a boolean value (`true` or `false`) which you could use to conditionally execute a Post-function or Unlink issues:

- Check the issue has been flagged

  ```javascript
  {{ issue.fields["Flagged"] | find({"value":"Impediment"}) != null }}
  ```
- Check the issue has a label `Server`

  ```javascript
  {{ issue.fields["Labels"] | find("Server") != null }}
  ```
- The issue has `5.0.0` as an Affects Version/s

  ```javascript
  {{ issue.fields.versions | find({"name":"5.0.0"}) != null }}
  ```

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing the standard fields](/cms_trial/space/JMWEC/466225701/Standard+JIRA+Fields/)
- [find filter](/cms_trial/space/JMWEC/465373638/Custom+filters/)

### Related articles

[unmapped inline: placeholder]

|  |  |
| --- | --- |
| **Related issues** |  |