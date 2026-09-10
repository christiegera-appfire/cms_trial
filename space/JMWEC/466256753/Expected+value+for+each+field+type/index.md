# Expected value for each field type

When setting a field value, the post-function will fail to work as expected if the input value does not match the value expected for the intended field type. This document describes the format of values expected by a field when using post-functions to set them.

The value can be a text provided in the `Value` field of:

- [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function
- [Set field value of linked issues](/cms_trial/space/JMWEC/465504997/Set+field+value+of+linked+issues+(Deprecated)/) post-function
- "User entity properties" of [User properties editor page](/cms_trial/space/JMWEC/466256416/User+Properties+Editor/), to copy the value of the specified user property for the current user using [Set field value from User Entity Property value](/cms_trial/space/JMWEC/466257282/Set+field+value+from+User+Entity+Property+value/) post-function
- [Create issue post-function](/cms_trial/space/JMWEC/466256916/Create+issue(s)/), to set fields of the newly created issue
- one of the Transition issue post-functions, to set fields on the transition screen, if any

The value can be the result of a Nunjucks template provided in the `Value` field of:

- [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function
- [Set field value of linked issues](/cms_trial/space/JMWEC/465504997/Set+field+value+of+linked+issues+(Deprecated)/) post-function
- [Create issue post-function](/cms_trial/space/JMWEC/466256916/Create+issue(s)/), to set fields of the newly created issue
- one of the Transition issue post-functions, to set fields on the transition screen, if any

## Text value

The value can be specified as text. It can be:

- a simple, constant String. For example: `This is a description`
- the String representation of a

  - Number. For example:  `3.2`
  - Date. The expected format is [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601). For example: `2016-08-05`
  - Complex (object) field. In this case, the value should be the String representation of that object. For example, to set the Fix Version/s to version 2.0, you would use the following value: `2.0`

Multiple values (for multi-valued fields) can be provided, separated by commas. For example, to specify two Affects Versions 1.0 and 2.0 write `1.0,2.0` in the Value.

For detailed information about the exact format of the expected value for each field, see:

- [Text value - Standard Jira fields](/cms_trial/space/JMWEC/466289528/Text+input+for+fields/)
- [Text value - Predefined Custom fields](/cms_trial/space/JMWEC/466289528/Text+input+for+fields/)
- [Text value - User-created custom fields](/cms_trial/space/JMWEC/466289528/Text+input+for+fields/)

You can also inject[Nunjucks annotations](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) into the text value. You might also want to look at [Issue and Transition Data in Nunjucks](/cms_trial/space/JMWEC/465373107/Issue+and+Transition+Data+in+Nunjucks/).

You can use the [Set Field Value](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function to clear a field value by leaving the `Value` field empty. Ensure that neither `Ignore empty value` nor `Add value(s) to the field` options are selected.

## JSON value

The value can be specified as a JSON value, which is a text representation of data that can be passed to Jira. This requires the `Treat value as JSON` option to be selected.

Supported value types include:

- String. For example: `"This is a description"`
- Number. For example: `3.12`
- Date. This must be a String containing an [ISO\_8601](https://en.wikipedia.org/wiki/ISO_8601) date. For example: `"2016-08-05"`
- Object. The object must contain at least one field (different from **id**) which allows the object to be identified unambiguously. For example, a user can be specified as:`{"accountId":"accountId:557058:3a41d4ee-3331-4363-8cdf-f90a2da92f7e"}`

For multi-valued fields, the value(s) must be provided as an array of values, even if only one value is provided. For example, to set the Fix Versions field to "2.0":`[{"name":"2.0"}]`

For detailed information about the JSON value expected by each field type, see

- [JSON value - Standard Jira fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/)
- [JSON value - Predefined Custom fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/)
- [JSON value - User-created custom fields](/cms_trial/space/JMWEC/466225769/JSON+input+for+fields/)

You can also inject[Nunjucks annotations](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) into the JSON value. You might also want to look at [Accessing an issue or a transition using Nunjucks annotations](https://appfire.atlassian.net/wiki/display/JMWEC/Accessing+the+details+of+an+issue+or+a+transition+in+Nunjucks).

You can use the `null` *JSON value* to clear a field (assuming the field is not required, like Summary, Description or Resolution).