# Workflow preconditions

## Configuration of preconditions

**JSU Automation Suite** preconditions allow you to execute a [post function](/cms_trial/space/JSUCLOUD/12518401/Workflow+post+functions/) under certain circumstances only; essentially they are conditions for the post function component of your rule. This lets you create complex behavior on your post functions, enabling Jira to work harder for you.

JSU's preconditions are a part of the post function section in Jira's workflow configuration. In the example below, a precondition is added to the ‘Clear Field Value’ post function.

![Diagram showing the resulting action for a JSU post function if the preconditions are met or unmet.](/cms_trial/assets/ef0390e3-427e-48ce-85fe-84cce79f302f.png)

### Choose your precondition

In the post function configuration page, select **Add Precondition** then select **Add** for the precondition that you want to evaluate.

The following preconditions are available:

- [Date Compare precondition](/cms_trial/space/JSUCLOUD/12517956/Date+Compare+precondition/)
- [Date Expression Compare precondition](/cms_trial/space/JSUCLOUD/12517966/Date+Expression+Compare+precondition/)
- [Date Window precondition](/cms_trial/space/JSUCLOUD/12518704/Date+Window+precondition/)
- [Fields Required precondition](/cms_trial/space/JSUCLOUD/12518665/Fields+Required+precondition/)
- [JQL precondition](/cms_trial/space/JSUCLOUD/12518033/JQL+precondition/)
- [Linked Status precondition](/cms_trial/space/JSUCLOUD/12518805/Linked+Status+precondition/)
- [Regular Expression precondition](/cms_trial/space/JSUCLOUD/12518693/Regular+Expression+precondition/)
- [Status Change precondition](/cms_trial/space/JSUCLOUD/12520152/Status+Change+precondition/)
- [User in Field precondition](/cms_trial/space/JSUCLOUD/12517988/User+in+Field+precondition/)
- [User in Groups precondition](/cms_trial/space/JSUCLOUD/12517924/User+in+Groups+precondition/)
- [Value Field precondition](/cms_trial/space/JSUCLOUD/12518009/Value+Field+precondition/)
- [User in Roles precondition](/cms_trial/space/JSUCLOUD/12517977/User+in+Roles+precondition/)

![Add Precondition button highlighted in the JSU Clear Field Value post function configuration page.](/cms_trial/assets/2d0a2c54-20c7-4622-bf6a-67eb6b1421e6.png)![List of available JSU preconditions.](/cms_trial/assets/1011f4e4-a59f-4dd8-9a7b-3bc1a8f6dc62.png)

### Combine multiple preconditions

You can insert multiple preconditions and combine them using the following operators:

- AND: Previous result and the current result must be true
- OR: Either the previous result or current result must be true, or both
- AND NOT: The previous result must be true, and the current result must be false
- OR NOT: Either the previous result must be true or the current result must be false, or both

They are evaluated sequentially, combining the result of the previous precondition with the result from the current one. Parentheses to define precedence are not supported.

You can rearrange the precondition by dragging the line using the handle on the left.

You can also disable the precondition by unchecking the enabled flag next to the delete button. This will leave the precondition in your configuration, but it will be ignored.

![Example setup of JSU preconditions using an If, Or, And sequence.](/cms_trial/assets/d0d7a909-5c5f-41f2-bcc4-2517dbc70f3d.png)

### The post function setting

Your post function is always aware of the preconditions you configured, however, you still need to select whether you want the precondition to be `true` or `false` for the function to be executed.

![The JSU Precondition set to True in the post function configuration page.](/cms_trial/assets/49154714-114e-4322-a914-3f084b874c66.png)

## Example

Say you want to tell the user to break up a large story into smaller stories. You can do this by creating an Update Any Issue Field post function and setting the precondition as described:

- IF Original Estimate >= 2d
- OR Story Points > 8
- AND Issue Type = Story

In other words, if you have a time estimate greater than or equal to two days or the number of story points exceeds 8 and the issue is a Story, then you want to execute the post function.

In the post function, you update the issue by adding a new comment. After you save, the overview should appear similar to the following:

![The post function summary as described in the example on this page.](/cms_trial/assets/d5fdb186-70e3-4edb-9011-938f8875bf63.png)

See [Preconditions for Post Functions](/cms_trial/space/JSUCLOUD/12518052/Update+an+issue+only+in+certain+conditions/) for more use cases.