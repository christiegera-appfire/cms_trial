# Set entity property value

A workflow post-function that sets the value of an entity property of the current issue, current issue's project or current user. The value can be provided either as text (with optional Nunjucks annotations) or as a JSON value.

When you add this post-function to a transition and trigger the transition, the add-on sets the specified entity property of the selected target (either the current issue, the current issue's project, or the current user) to the specified value. The value can be provided either as text (with optional [Nunjucks](http://mozilla.github.io/nunjucks/templating.html)annotations) or as a JSON value.

- In the case of text, the value can be a simple string (for text typed fields), the string representation of a number, date or boolean value, or the string representation of a complex value, such as a Version name, a username, a Project key, etc. You can also use [Nunjucks](http://mozilla.github.io/nunjucks/templating.html)to insert dynamic values (issue, transition, or current user information).
- In the case of a JSON value, which requires the option `Treat value as JSON` (explained below), it can be a String, a Number, a Boolean or an Object. It can also be an array of such values.

To find out more about the type of value expected by this post-function for different field types, see [Expected value for each field type](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/).

![Set Entity Property Value post function configuration screen](/cms_trial/assets/db7ff712-49a4-4b2a-a524-9854bb6a79d1.png)

**To add 'Set entity property value' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition to which you wish to add the post function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Set Entity Property value** from the list of post function.
6. Click **Add** to navigate to the *Set Entity Property value post-function* screen where you can add configuration details. See below for more information.
7. Click on **Add** to add the post function to the transition.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

## Entity and Property name

Select the entity for which the property should be set, the property name, and the value to use:

- **Entity**

  - **Current issue** - Set a property of the current issue (the issue that triggered the post function).
  - **Current issue’s project** - Set a property on the current issue’s project.
  - **Current user or Run as user** - Set a property on the user who triggered the post function - either the current user (default) or the user set under **Run as**, below.
- **Property name** - The name of the property to set.
- **Value** - The value for the property.

## Options

- **Treat value as JSON** - Sets the property value to a JSON object or an array of objects. It will take the `Value` in the value template and parse it like a JSON string into a JavaScript object. This will be passed back to Jira as the value of the property. To learn about the *JSON value* expected by the post-function, see [Expected value for each field type](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/).
- **Set only if property is empty** - Sets the value of the selected property only if the property is empty.
- **Ignore empty value** - The post function will not set the selected property if the Nunjucks template that returns the **Value** is empty or null.

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

### Run As

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

### Conditional execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.