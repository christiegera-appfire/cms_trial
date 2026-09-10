# Set field value from User Entity Property value

A workflow post-function that sets the value of a selected field of the current issue to the value of a User Property of the current user.

When you add this post-function to a transition and trigger the transition, the add-on copies the value of the specified user property for the current user to the selected destination field. The user property is used to store extra information about a user. These properties come from the `User properties editor`page in the `Add-ons` section. These properties are different from the `User Properties` you can edit from the`User Management` section. To add/edit user properties of a user, see the [Add/edit/delete user entity properties in User property editor](/cms_trial/space/JMWEC/466256416/User+Properties+Editor/) page.

![Set field value from User Entity Property value configuration screen](/cms_trial/assets/58904be8-c2c3-4897-9179-f99232f1e2f7.png)

**To add the 'Set field value from User Entity Property value' post function to a transition:**

1. Click **Edit** for the workflow that has the transition to which you wish to add the post-function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel (or select the **Post Functions** tab).
4. Click**Add post function**.
5. Select **Set field value from User Entity Property value** from the list of post functions.
6. Click **Add.** The *Set field value from User Entity Property value post-function*screen will open, where you can configure the post function as needed. See below for more details on specific configurations.
7. Click **Add** to complete the configuration and add the post-function.

After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=MWECS&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=448497512) document.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

## Configuration

- **Field** - Select the field to set.
- **User entity property** - Enter the name of the User entity property that contains the required value.

### Options

- **Create missing value(s)** - Allows creating any missing Component/s or Version/s while setting or copying a field that expects Versions or Components. Note this is applicable for version and component fields.

When setting the **Issue Security** field, the user property must contain the *name* of the **Security Level**, which you can find by looking at the links associated with the **Add/Default/Delete** operations on the desired Security Level (on the **Edit Issue Security Levels** screen).

## Advanced Options

### Run as

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