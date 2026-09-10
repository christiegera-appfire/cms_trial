# Transition parent issue (Deprecated)

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
| The **Transition issues** post function includes additional options for the target issue to be transitioned. | Target issues → Parent issue of the current sub-task | . |
| Transition screen → Fields | Advanced options → Transition screen → Fields |  |
| Comment | Advanced options → Transition screen → Comment | Check the **Add Comment** box to add a comment, then copy the obsolete post function comment to the new post function **Comment** field. |
| Comment visibility → Restrict to group | Advanced options → Transition screen → Comment visibility → Restrict to group |  |
| Comment visibility → Restrict to project role | Advanced options → Transition screen → Comment visibility → Restrict to project role |  |
| Comment visibility → Restrict to Internal | Advanced options → Transition screen → Comment visibility → Restrict to Internal |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that triggers a transition on the *parent issue* of the current issue.

**To add the 'Transition parent issue' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add``post function`.
5. Select `Transition parent issue` from the list of post-functions.
6. Click on `Add`to add the post-function on the transition.

   ![JMWE for Jira Cloud parent issue transition setup for subtask workflow management](/cms_trial/assets/5887e504-43ea-4579-811f-a7ee494e8bea.png)
7. Specify transition(s) either in the table or as a result of the calculated Nunjucks template. See below for more information.
8. Click on `Add` to add the post-function to the transition.
9. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=465242394) document.

When you add this post-function to a transition and trigger the transition on an issue, the add-on will transition its parent issue using the specified transition, assuming it is valid for the parent issue's current status and available to the current or selected user.

### Transition(s)

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

### **Run As**

- **Run as current user:** The current user will be the author of the transition triggered by the post-function.

- **Run as add-on user:** The add-on user will be the author of the transition triggered by the post-function.

- **Run as this user:** Any user specified in this field will be the author of the transition triggered by the post-function.

### **Transition screen**

If the transition uses a transition screen you might want/need to provide a value for fields (*such as Resolution*) present on the screen. Look below to know how to add/set/remove fields.

- **To add a field :**Select a field from the list of fields and click on`Add.`
- **To Remove an added field :** Click on `Remove` to remove a field.
- **To Set a field value :**

  - **Copy value from current issue** : Copies the field value(s) from the subtask.
  - **Set field value to**: You can set the field to a specific value, wherein the value can also include Nunjucks annotations.  
    For example : To set the Resolution to Fixed, you can specify `Fixed` in the value box.

Likewise, you might also want to provide a *comment* during that transition.**This will only work if the triggered transition is associated with a transition screen.**

- **Comment :** adds a comment to the parent issue being transitioned. The `Comment` can be any simple text, e.g. `This is a comment.` You can also use [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations in the comment using variables. To find out more about the variables, see [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/).
- **Comment visibility :**

  - **Restrict to Group :** Restricts the visibility of the comment to a specified group. When you select a valid group name in the `Restrict to Group` field, the comment will be visible only to the members of the specified group. For no restriction, leave the field blank.
  - **Restrict to Project Role :** Restricts the visibility of the comment to a selected project role. When you select a project role from the drop-down `Restrict to Project Role` field, the comment will be visible only to the members of the selected project role. For no restriction, leave the field blank.
  - **Restrict to Internal (Jira Service Desk only) :** Restricts the visibility of the comment to the Service Desk Agents and Collaborators only.

### **Conditional execution**

To execute this post-function based on the result of a Nunjucks template see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

### **Delayed execution**

The options **Run as add-on user** and **Run as this user** are useful if the current user doesn't have the permission to transition the parent issue(s).

The transition can be specified by name so that the transition can be found regardless of the parent issue's actual workflow, or by ID if disambiguation is required.