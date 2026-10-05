# Increase value of field

A workflow post-function that increases the value of a selected numerical field by one.

When you add this post-function to a transition and trigger the transition on an issue, the add-on increments the selected field value by one.

**Note**: This post function is applicable to numerical fields only!

![Increase Value of Field post function configuration screen](/cms_trial/assets/2ba9b984-488f-45c9-8b97-c001ea0ec362.png)

**To add the 'Increase value of field' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition to which you wish to add the post function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Increase value of field** from the list of post function.
6. Click **Add** to navigate to the *Increase value of field post-function* screen where you can add configuration details. See below for more information.
7. Click on **Add** to add the post function to the transition.

## Options

The primary option is the field that should be increased by one.

- **Field** - Select the field to increase.

Only one field can be selected for each instance of this post function.

## Advanced options

Expand this section to see advanced configurations including conditional execution, delayed execution, and whether or not Jira will send a notification when the post function is executed.

### Run as

### Conditional execution

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post function, so that the sub-tasks are created before they are transitioned.

Where possible, it is recommended to use the [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+Post-functions/) post function or [Shared action](/cms_trial/space/JMWEC/466323396/Shared+Action+post-function/) post function to execute a series of post functions in a specific sequence instead of applying a delay.

### Send notifications

Jira can sends notifications for the increment in the selected field value on the current issue. Check the box **Allow Jira to send notifications for this change** to enable notifications.