# Fetch a subset of values of a multi-valued field based on a condition

### Abstract

This code snippet filters values from a multi-valued field based on a condition

### Logic

Use the "filter" Nunjucks filter to filter the values that meet the condition

### Snippet

```javascript
{# Filter the values from the multi-valued field using "filter" filter #}
{{ issue.fields['<Multi-valued field name>'] | filter(<Condition>) | join(",","name") }}
```

### Placeholders

| **Placeholder** | **Description** | **Example** |
| --- | --- | --- |
| `<Multi-valued field name`> | Name of the multi-valued field | `Watchers` |
| `<Condition``>` | Condition to meet for the value to be filtered | `{accountId:``'accountId:5ca5b1469a000c1180956957'``}` |

### Context

The output of this snippet is a subset of the existing values of a multi-valued field which you could use in a template to:

- Set a multi-valued field to a subset of the existing values in one of the Set field value post-functions. Example: Set a Multi-user picker type field to the users in the Watchers field who belong to the Europe/Berlin time zone:

  ```javascript
  {{ issue.fields['Watchers'] | filter({"timeZone": "Europe/Berlin"}) | join(",","accountId") }}
  ```
- Send an email to all the customers watching the ticket using the Email issue post-function. For this, you need to add this script in the "Users from script" field in the post-function configuration

  ```javascript
  {{ issue.fields['Watchers'] | filter({"accountType": "customer"}) | join(",","accountId") }}
  ```

References

- [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/)
- [Treat value as JSON](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/)
- [Accessing fields of an issue](/cms_trial/space/JMWEC/465373107/Issue+and+Transition+Data+in+Nunjucks/)
- [Custom filter - filter](/cms_trial/space/JMWEC/465373638/Custom+filters/)

### Related articles

|  |  |
| --- | --- |
| **Related issues** |  |