# Create issue(s)

A workflow post function that creates one or more new issue(s). The specifications of the issue(s) to be created can be customized using the options provided.

**Note**: When creating issues using this post function, some consideration is required for specific fields in the new issue(s):

- **Sprint** - If you are setting the **Sprint** field (manually or when copying fields), and you try to assign the new issue to a closed sprint, the value will not copy. If you are adding multiple sprints to the **Sprint** field and one of those values is a closed sprint, that value will not be copied (but the other sprint values will be copied).

![JMWE for Jira Cloud create issues post function with comprehensive configuration options](/cms_trial/assets/94861a30-3240-42e9-b20c-b229b2cf7927.png)

**To add the 'Create issue' post function to a transition**:

1. Click **Edit** for the workflow that has the transition to which you wish to add the post function.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Create issue(s)** from the list of post functions.
6. Click **Add** to navigate to the *Create issue(s) post-function*screen where you can add configuration details to the post function. See below for configuration details.
7. Click **Add** to add the post function to the transition.

After adding the post function, move the post function to the appropriate position according to [Placing post functions in a transition](/cms_trial/space/JMWEC/466289149/Adding+extensions+to+transitions/) document.

## Destination

Specify the target project and issue type.

- **Project** -Set the project where you want the new issue(s) to be created. Select one of the following to set the project as:

  - **Same as the current issue** - The same project as the current issue.
  - **Calculated** - A project whose key is the value returned from the Nunjucks template.
  - **Projects** - A project selected from the list.
- **Issue type** - Select the issue type to be assigned to the newly created issue. Some factors when selecting the issue type:
- **Link type** - Select a link type from the drop-down to link the newly created issue to the current issue. The default value is "is not linked to" which will not create a link.
- **Reporter** - Set the Reporter value of the newly created issue.

  - **Custom value from script** - Set the value from a script. See **New value** below.
  - **Copy value from current issue** - Copy the Reporter value from the current issue.
  - **Copy value from other field of current issue** - Copy the value from a different User field of the current issue.
- **New value** - *Only visible when* ***Reporter****, above, is set to ‘Custom value from script’.* Enter a Nunjucks script to determine the User to assign as the Reporter.
- **Use current user when deactivated Reporter is encountered** - When the User account to be assigned as the Reporter is a deactivated account, the User who triggered the post function will be assigned instead.
- **Summary** - Set the Summary value of the newly created issue.

  - **Custom value from script** - Set the value from a script. See **New value** below.
  - **Copy value from current issue** - Copy the Summary value from the current issue.
  - **Copy value from other field of current issue** - Copy the value from a different field of the current issue.
- **New value** - *Only visible when* ***Summary****, above, is set to ‘Custom value from script’.* Enter a Nunjucks script to determine the field value.

When the issue type is:

- **Epic** - Set the **Epic Name** field with a value using the **Set fields of new issue** option (explained below).
- **Story** - You may want to add the newly created story to an Epic. In this case, you should add the **Epic link** field with the key of the Epic as the value in the **Set fields of new issue** option (explained below).
- **Sub-task**, specify its parent issue in the **Parent issue** field:

  - **Current issue** - The current issue will be the parent of the newly created issue.
  - **Another issue** - Enter a Nunjucks expression that returns the key of the parent for the newly created issue.
- **Calculated** - Enter the issue type name or ID as a static value, or use a [Nunjucks template](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/) that returns a valid issue type name or ID.

When the Project is `Same as the current project` or `Calculated` the list of issue types contains all the issue types configured in your Jira instance, even though some of them might not apply to that project.

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

## Copy fields

Specify the current issue fields to be copied to the new issue(s).

**Mode**

- **Only copy or set fields listed below** - If you select this option, only fields specified explicitly under the **Set new fields** section will be copied or set on the new issue.
- **Copy all fields that appear on the Create screen of the issue or the Request form of the customer request type to create** - If you select this option, all fields that appear on the Create screen of the issue being created or the Request form of the customer request type will automatically be copied from the current issue to the new issue.
- **Copy all fields** - If you select this option, all fields that have a value on the current issue and that apply to the issue being created will be copied from the current issue to the new issue.

Regardless of the selected option, if you add a field under the **Set new fields** section, it will always be set as configured under those options (see below). This can be useful if, for example, you want to copy the values of all fields of the original issue, but need to override the value of one or more fields; in this instance, set the **Mode** to *Copy all fields* and then also configure the specific fields for which you need to override the original value(s).

## Set new fields

Set the field values of the newly created issue, regardless of the option selected under **Copy fields to new issue(s)**.

- **Add** - Click **Add** to include a field in those set by the post function.

  - **Select field** - Select the field to set.
  - **Field value**:

    - **Copy value from current issue** - Copies the field value(s) from the current issue.
    - **Set to other field of current issue** - Sets the field to the value of another field of the current issue. Say, to set the Assignee of the newly created issues to the user in the Reporter field from the original issue.
    - **Set field value to** - Set the field to a specific value, which can include Nunjucks annotations.  
      For example: To set the Fix Version/s to 2.0, you can specify `2.0` in the value box.
  - **Ignore deactivated user(s)** - For any field that stores a User value, ignore the new value if that User is deactivated in Jira.
- Click **Edit** ( ▢ ) to edit a field that has been added.
- Click **Remove** ( ▢ ) to remove the field.

Note that you can copy the issue links of the current issue to the newly created issue by setting the`Linked Issues` field to copy the values from the current issue.

- **Additional options**

  - **Ignore fields that don't apply to the new issue** - If you add a custom field or fields above that do not apply to the issue being created (because it is configured to apply only to certain issue types or projects), the post function will fail (so you can pinpoint the problem). Select this option to ignore this error instead, which can be useful if you are creating multiple issues in different projects or of different types.
  - **Copy sub-tasks to the new issue(s)** - Copy all sub-tasks of the current issue to the newly created issue.
  - **Ignore deactivated user(s)** - If a user is deactivated in Jira, ignore the new value for all fields that store a User value.

**Note**: the following fields will not be copied to the new sub-tasks:

- created
- timetracking
- aggregatetimeoriginalestimate
- aggregatetimeestimate
- aggregateprogress
- aggregatetimespent
- issuekey
- project
- subtasks
- thumbnail
- updated
- workratio
- progress
- worklog
- lastViewed
- creator
- watches
- votes
- attachment
- comment
- timeestimate
- timespent
- issuelinks
- status

## Comments

Use this section to copy the existing comments/newly added comments of the current issue to the newly created issue.

- **Don't copy** - This is the default option. Select this option to not copy comments to the newly created issue
- **Copy only transition comments** - Select this option to copy the comment or comments added on the transition screen to the newly created issue.
- **Copy all** - Select this option to copy all the comments on the current issue to the newly created issue.
- **Add new comment** - Check this box to add a new Comment during the post function.
- **Comment** - *Only visible when ‘****Add new comment****’, above, is checked.* Enter a Nunjucks script that generates the new Comment content.

The restricted comments to which the “Run as user” does not have permissions are not copied to the newly created issue.

### Comment visibility

*This section is only visible when* ***Comments****, above, is set to any option other than* ***Don’t copy****.* This option will set the visibility of any comments that are copied from the current issue to the new issue(s).

- **Retain existing comment visibility restrictions** - This will copy the existing restrictions on individual comments to the copied comments on the new issue(s).
- **Use the following comment visibility** - Select specific visibility settings. **Note**: the selected settings will apply to *all comments* copied, no matter their visibility settings on the current issue.

  - **Restrict to Group** - Select a group to restrict comment visibility to only members of that group. Leave blank for no restrictions based on group.
  - **Restrict to Project Role** - Select a Project Role to restrict visibility to only members of that role. Leave blank for no restrictions based on role.
  - **Restrict to Internal (Jira Service Management only)** - *Only valid when using Jira Service Management*. Select this option to restrict comments to internal users only.

## Actions after issue creation

### Multiple issue creation

Use this section to create multiple issues based on the settings you provide.

- **Create multiple issues** - Select this option to create multiple issues at once. Provide an *iterator*script to control the number issues to be created. By default, the **Create issue** post function creates one new issue.
- **Iterator** - *Only visible when the previous option is selected*. Enter a Nunjucks template that must return a comma-separated list of values to iterate on. This can be either a comma-separated list of Strings, or a JSON array only if you check the "Iterator returns JSON" option. The post function iterates over the list and creates one new issue per value. If configured, a new comment is also added to the current issue for each new issue created.
- **Iterator returns JSON** - Check this box if your **Iterator** code returns a JSON array. See **Template returning a JSON array**, below, for more information and examples on how to use this option.

### Template returning a comma-separated list of Strings

If the iteration template returns `jdoe,tblack`then one issue will be created with the `it` variable containing `"jdoe"` and then another with the `it` variable containing `"tblack"`. If, in the configuration of the post function, you are setting the **Assignee** field of the newly created issues using a Nunjucks Template `{{it}}`, then the first issue will be assigned to `jdoe` and the second to `tblack`.

**Note**: If you use the technique above to assign multiple issues, when you test the Nunjucks template the tester will return only `jdoe`.

Examples:

- `Bug,Task` - This will create two issues - one a Bug and the other a Task.
- `{{issue.fields["Multi-user Picker field"] | join(",","accountId")}}` - This will create one issue per user in the Multi-user Picker field.
- `{{range(1,5)}}` - This will create 4 issues, with the `it` variable containing numbers 1 through 4.

### Template returning a JSON array

If the iteration template returns a JSON array, for example:   
 `[ {"assignee":"jdoe", "summary":"Issue for John Doe"} , {"assignee":"tblack", "summary":"Issue for Tim Black"} ]`   
and you select the **Iterator returns JSON** option, then you'll be able to use `{{it.assignee}}` as the value for the Assignee field, and `{{it.summary}}` as the value for the Summary field.

Examples:

- `{{"jira-administrators" | groupMembers | dump }}` - Create one issue per user in the 'jira-administrators' group.
- {{`issue.fields["Multi-select field"]  | dump }}` - Create one issue per selected option in the Multi-select field.

### **Post-creation script**

- **Run a Nunjucks script** - Select this option to run a Nunjucks script after each new issue is created to make additional changes to the issue, such as adding a remote link or calling an external API. In scenarios where you use this script for setting issue field values, the respective value set during issue creation is overwritten.
- **Script** - *Only visible when* ***Run a Nunjucks script after the issue(s) are created****, above, is selected.* Enter a Nunjucks script as needed.

During the execution of the script, the `newIssueKey` variable points to the newly created issue.

### Navigate to the newly created issue

- **Navigate to the newly created issue** - Select this option to automatically navigate the user to the new issue created at the end of the transition. This is applicable only when the transition is triggered from the View Issue page.

This requires the **Enable View Issue Screen Actions** option on the [JMWE Configuration page](/cms_trial/space/JMWEC/465503776/JMWE+Administration/) to be enabled.

After the issue creation, the post function stores some data:

- The key of the issue(s) it creates in an *issue property* `jmwe.last.issue.created` of the current issue (the one on which the post function runs). You can retrieve this using the `issueProperty` Nunjucks filter. This can be used in other post functions to refer to the last issue created by the Create issue post function. If multiple issues are created, then the issue property refers to the very last issue that was created.
- The key of the original issue in an *issue property* `jmwe-created-from` of the newly created issue(s). You can retrieve it later using the `issueProperty` Nunjucks filter. This can be used in other post functions to refer to the issue from which the current issue was created using the Create issue post function. You can also use it in JQL searches using the syntax: `issue.property[jmwe-created-from].key = TEST-123` where “TEST-123” was the key of the original issue.

However, there are caveats about which you need to be aware:

- Any post function that reads this property needs to run *after* the Create Issue post function finishes. You can ensure the order of post functions by using a [Shared action](https://appfire.atlassian.net/wiki/spaces/JMWE/pages/461996736) or by adding a delay; see **Delayed execution**, below.
- If two users simultaneously run a transition *on the same issue* that creates a new issue, only the last issue created will be available in the `jmwe.last.issue.created`property. So this makes the feature unreliable if you're using the Create Issue post function on multiple transitions of the same workflow.

## Settings

### Run As

Select one of the following to set the creator of the issue:

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

JMWE shows an error message on the issue view if any error occurs during the execution of the post function. *This message is displayed only if the current user is a Jira administrator.*