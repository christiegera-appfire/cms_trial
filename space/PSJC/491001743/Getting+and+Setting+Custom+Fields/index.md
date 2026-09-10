# Getting and Setting Custom Fields

## Implicit Context

Whenever reading or storing a custom field value, the SIL Engine must be given an issue context so that it can connect those values to an issue. In most scripting environments (such as a listener or a custom workflow), the context is already provided.

### Getting a Custom Field Value by Id

|  |
| --- |
| ```text string value = customfield_1234; ``` |

### Getting a Custom Field Value by Name

|  |
| --- |
| ```text string value = #{custom field name}; ``` |

### Setting a Custom Field Value by Id

|  |
| --- |
| ```text customfield_1234 = value; ``` |

### Setting a Custom Field Value by Name

|  |
| --- |
| ```text customfield_1234 = #{custom field name}; ``` |

## Explicit Context

There are times when you must explicitly declare the context of an issue. This is especially useful when looping through an array of issues.

### Getting a Custom Field Value by Id

|  |
| --- |
| ```text string value = key.customfield_1234; ``` |

### Getting a Custom Field Value by Name

|  |
| --- |
| ```text string value = key.#{custom field name}; ``` |

### Setting a Custom Field Value by Id

|  |
| --- |
| ```text %key%.customfield_1234 = value; ``` |

### Setting a Custom Field Value by Name

|  |
| --- |
| ```text %key%.customfield_1234 = #{custom field name}; ``` |

When setting custom fields using an explicit context, you must surround the issue variable with percent signs.

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.