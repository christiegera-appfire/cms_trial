# Transition linked issues (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| Transition → Selector/Script | Transition → Selector/Script |  |
| Transition → Workflow | Transition → Workflow |  |
| Transition → Transition name or ID | Transition → Transition name or ID |  |
| Issue Link Type | Target issues | If the obsolete post function is set to **Any**, use **Issues linked to the current issue through any link type**.  If the obsolete post function is set to a specific link type, select **Issues linked to the current issue through the following link type**, and set the **Issue link** field to the appropriate link type. |
| Transition screen → Fields | Advanced options → Transition screen → Fields |  |
| Comment | Advanced options → Transition screen → Comment | Check the **Add Comment** box to add a comment, then copy the obsolete post function comment to the new post function **Comment** field. |
| Comment visibility → Restrict to group | Advanced options → Transition screen → Comment visibility → Restrict to group |  |
| Comment visibility → Restrict to project role | Advanced options → Transition screen → Comment visibility → Restrict to project role |  |
| Comment visibility → Restrict to Internal | Advanced options → Transition screen → Comment visibility → Restrict to Internal |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that triggers a transition on all issues linked to the current issue through a selected link type.

**To add 'Transition linked issues' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Transition linked issues` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.
7. Specify transition(s) either in the table or as a result of the calculated Nunjucks template. See **Transition(s)** below for more information.
8. Select the link from the `Issue Link Type` drop-down.
9. Click on `Add` to add the post-function to the transition.
10. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=466257658) document.

When you add this post-function to a transition and trigger the transition, the add-on will trigger the specified transition on each issue linked to the current issue through the selected link type, assuming that transition is valid for the linked issue's current status, and it is available to the current or the specified user.

![JMWE for Jira Cloud linked issue transition configuration for workflow automation](/cms_trial/assets/e7366955-13fa-482b-b6a4-a46fcb1ec73a.png)

## Transition(s)

### **Trigger one of the following transitions**

Input the transition `name(s)` or `id(s)` and optionally the workflow name manually or using the Transition picker. If you do not specify the workflow name (manually) the app will not check for a specific workflow. The app triggers the *first* transition specified in the table that is applicable to the issue in context.

**To pick a transition using the Transition picker:**

- Click on Transition picker
- Choose a workflow from Workflow name
- Select a transition from the list of transitions displayed
- Finally, click on either

  - `Use Transition Name` - recommended if you want the post-function to search for the transition to trigger by name, which is useful when targeting multiple workflows.
  - `Use Transition ID` - if you want to differentiate between transitions that bear the same name.
- Click on Add.

**To remove a transition:** Click on the `Remove` link for the specific transition

**To reorder transitions:** Select and move the transition in the table to reorder the list

### **Trigger a calculated transition**

Input a Nunjucks template that returns one or more transition `name(s)` or `id(s)` and optionally the workflow name. To specify a workflow name, write a Nunjucks template that returns the transition `name` or `ID` along with the workflow name separated by `@@.`For example: `Done@@HR workflow`.

To return multiple transitions, write a Nunjucks template that returns transition `names` or `IDs` each on a separate line. For example:

```groovy
2@@Default Jira Workflow
Done@@Another workflow
Close
```

Example of a template returning transition name:

```groovy
{%if issue.fields.priority.name == "Blocker"%}
  Escalate
{% else %}
  Assign
{% endif %}
```

## Run As

- **Run as current user:** The current user will be the author of the transition triggered by the post-function.
- **Run as add-on user:** The add-on user will be the author of the transition triggered by the post-function.
- **Run as this user:** Any user selected in this field will be the author of the transition triggered by the post-function.

## Transition screen

If the transition uses a transition screen you might want/need to provide a value for fields (such as*Resolution*) present on the screen. Look below to know how to add/set/remove fields.

- **To add a field :** Select a field from the list of fields and click on`Add.`
- **To Remove an added field :** Click on `Remove` to remove a field.
- **To Set a field value:**

  - **Copy value from current issue** : Copies the field value(s) from the current issue.
  - **Set field value to**: You can set the field to a specific value, wherein the value can also include Nunjucks annotations.  
    For example : To set the Fix Version/s to 2.0, you can specify `2.0` in the value box.

Likewise, you might also want to provide a *comment* during that transition.**This will only work if the triggered transition is associated with a transition screen.**

- **Comment :** adds a comment to each linked issue being transitioned. The `Comment` can be any simple text, e.g. `This is a comment.` You can also use [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations in the comment using variables. To find out more about the variables, see [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/).

  - **Comment visibility :**

    - **Restrict to Group :** Restricts the visibility of the comment to a specified group. When you select a valid group name in the `Restrict to Group` field, the comment will be visible only to the members of the specified group. For no restriction, leave the field blank.
    - **Restrict to Project Role :** Restricts the visibility of the comment to a selected project role. When you select a project role from the drop-down `Restrict to Project Role` field, the comment will be visible only to the members of the selected project role. For no restriction, leave the field blank.
    - **Restrict to Internal (Jira Service Desk only) :** Restricts the visibility of the comment to the Service Desk Agents and Collaborators only.

## Conditional execution

To execute this post-function based on the result of a Nunjucks template see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.

The options **Run as add-on user** and **Run as this user** are useful if the current user doesn't have the permission to transition the linked issue(s).

The transition can be specified by name so that the transition can be found regardless of each linked issue's actual workflow, or by ID if disambiguation is required.

Note that you can use this function to transition:

- The parent issue of a sub-task by using the built-in `is Subtask of` link type and vice versa using the `is Parent of` link type
- The Epic of an issue by using the built-in `belongs to Epic` link type and vice-versa using the `is Epic of` link type