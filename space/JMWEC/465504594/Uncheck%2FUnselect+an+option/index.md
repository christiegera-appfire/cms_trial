# Uncheck/Unselect an option

### Abstract

This code snippet unchecks a specific value of a standard or custom multi-valued type field (typically a [multi-select field](/cms_trial/space/JMWEC/465505179/User-created+Custom+Fields/)). The multi-valued fields can either be a collection of objects or a set of values. While unchecking all is easy (set the field with a blank value), unchecking only a particular option/value requires code.

### Logic

Iterate over the array of currently selected options and add them into a new array ignoring the option that needs to be unchecked.

### Snippet

#### For multi-select fields:

```javascript
{# Dump options that do not match the search  - Requires the "Treat as JSON" option #}
{{ issue.fields['<Name of the field>'] | filter({value:"<Value of the option to uncheck>"} , true ) | dump }}
```

#### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| `<Name of the field`> | Name of the field of type Checkboxes/Select list(multiple choices) | `Tasks list` |
| `<Value of the option to uncheck>` | Value of the option. | `Verification done` |

#### **For**multi-versions/users/components/groups fields (e.g. Fix Version/s):

```javascript
{# Dump values that do not match the search  - Requires the "Treat as JSON" option #}
{{ issue.fields['<Name of the multi-valued field>'] | filter({name:"<Value to uncheck>"} , true ) | dump }}
```

#### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| `<Name of the field`> | Name of the multi-valued field | `versions` |
| `<Value to uncheck>` | Value of the field. | `5.0.0` |

#### **For**Labels field:

```javascript
{# Dump labels that do not match the search  - Requires the "Treat as JSON" option #}
{{ issue.fields['<Labels field>'] | filter("<Label to remove>" , true ) | dump }}
```

#### Placeholders

| Placeholder | Description | Example |
| --- | --- | --- |
| `<Labels field`> | Name of the Label field | `Labels` |
| `<Label to remove>` | Label to be removed | `Merged` |

### Examples

The output of this code snippet is an array of objects which you could use to remove a particular option from the selected options of a field in one of the Set Field Value post-functions.

These code snippets require "Treat as JSON" option to be selected

- Remove the reporter from the JIRA service desk customers

  ```javascript
  {{ issue.fields['Service Desk Customers'] | filter({accountId:issue.fields.reporter.accountId} , true ) | dump }}
  ```
- Clear the option "To Print" after the print has been generated

  ```javascript
  {{ issue.fields['Documents processing'] | filter({name:"To Print"} , true ) | dump }}
  ```
- Remove the label "Merged" when QA re-opens a ticket that has been merged into master and handed over to QA.

  ```javascript
  {{ issue.fields['Labels'] | filter({name:"Merged"} , true ) | dump }}
  ```

### References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Accessing fields of an issue](/cms_trial/space/JMWEC/465373107/Issue+and+Transition+Data+in+Nunjucks/)
- [Treat value as JSON](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/)

### Related articles

|  |  |
| --- | --- |
| Related issues |  |