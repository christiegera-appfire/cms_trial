# Comment linked issues (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Comment issue(s)](/cms_trial/space/JMWEC/466322568/Comment+issue(s)/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| Issue Link Type | Target issues | If the obsolete post function is set to **Any**, use **Issues linked to the current issue through any link type**.  If the obsolete post function is set to a specific link type, select **Issues linked to the current issue through the following link type**, and set the **Issue link** field to the appropriate link type. |
| Comment | Comment |  |
| Restrict to Group | Advanced options → Comment visibility → Restrict to group |  |
| Restrict to project role | Advanced options → Comment visibility → Restrict to project role |  |
| Restrict to Internal | Advanced options → Comment visibility → Restrict to Internal |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that creates a comment on all issues linked to the current issue through a selected link type. The text of the comment to be created can be any simple text or a text with Nunjucks annotations.

**To add 'Comment linked issues' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions` in the properties panel.
4. Click on `Add` `post function`.
5. Select `Comment linked issues` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.

   ![JMWE for Jira Cloud workflow transition function setup for commenting on linked issues](/cms_trial/assets/f153ac95-f898-4b4c-8544-79bbd7ae1366.png)
7. Select the link from the `Issue Link Type` drop-down.
8. Input a comment in the `Comment` field.  
   To input issue or linked issue or transition or current user information in the `Comment` field see, [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/).
9. Select the options provided to add the required parameters.
10. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=465373854) document.

Here are a few [Use cases](/cms_trial/space/JMWEC/466225276/Use+cases/) for this post-function.

When you add this post-function to a transition and trigger the transition, the add-on picks the value entered in the `Comment` field and adds it as a comment on all the issues linked to the current issue through the selected link type. The `Comment` to be created can be any simple text, e.g. `This is a comment.` You can also use [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations to insert issue, linked issue, transition and current user information into the comment text, using the 'issue', 'linkedIssue', 'transition' and 'currentUser' variables, respectively. To find out more about these variables, see [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/).

### **Comment visibility**

- **Restrict to Group:** Restricts the visibility of the comment to a specified group. When you select a valid group name in the `Restrict to Group` field, the comment will be visible only to the members of the specified group. For no restriction, leave the field blank.
- **Restrict to Project Role:** Restricts the visibility of the comment to a selected project role. When you select a project role from the `Restrict to Project Role` drop-down, the comment will be visible only to the members of the selected project role. For no restriction, leave the field blank.
- **Restrict to Internal (Jira Service Desk only):** Restricts the visibility of the comment to the Service Desk Agents and Collaborators only.

### **Run As**

- **Run as current user:** The current user will be the author of the comment created on the linked issues by the post-function.
- **Run as add-on user:** The add-on user will be the author of the comment created on the linked issues by the post-function.
- **Run as this user:** Any user selected in this field will be the author of the comment created on the linked issues by the post-function.

### **Conditional execution**

To execute this post-function based on the result of a Nunjucks template see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

### **Delayed execution**

Note that you can use this function to comment the:

- parent issue of a sub-task by using the built-in `is Subtask of` link type and vice versa using the `is Parent of` link type
- Epic of an issue by using the built-in `belongs to Epic` link type and vice-versa using the `is Epic of` link type
- Parent of the portfolio hierarchy by using the `belongs to Initiative` link type and vice-versa using the `is Initiative of` link type