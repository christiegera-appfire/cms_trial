# Related issues

Most of JSU's workflow post functions have the option to define the scope of related issues. For example, instead of copying a field within an issue for a post function, you can copy it to a subtask.

![A list of issue relation options in JSU post functions.](/cms_trial/assets/92eecb57-82a8-49eb-80ba-4a446b9ded7d.png)

## Types of issue relations

Related issues are identified by one of the following Jira concepts:

- **Issue link:**You can choose the link type to define which issues will be modified by the operation. If the post function includes the link type as ANY option, the operation will be performed on any linked issues.
- **Parent / Sub-Task:** The related issue is either the parent or a subtask.
- **Epic / Issue in** **Epic:**The other issue is either an epic related to an epic link or it is part of an epic. This is only applicable if you have Jira Software installed.
- **JQL:**Use a JQL query to retrieve the issues the post function will modify. You can use some placeholders in the JQL query, which will be replaced with the current field values of the issue in transition. For tips on writing the JQL query, see [JQL Reference](/cms_trial/space/JSUCLOUD/12518329/JQL+reference/) or our [JQL Use Cases](/cms_trial/space/JSUCLOUD/12518307/JQL+use+cases/) for some examples.

### Issue in transition

*Issue in Transition* refers to the issue for which a workflow condition is checked, a workflow validator is examined, or a workflow post function is performed; in other words, the issue that triggered a workflow condition/validator/post function to be executed.

### Source and destination

For some post functions, you can choose whether the issue in transition serves as the source or the destination. For example, the [Copy Value From Other Field](/cms_trial/space/JSUCLOUD/12518474/Copy+Value+From+Other+Field+post+function/) post function allows you to define the issue in transition as the source or destination of the copy operations. In contrast, you define the other end with an issue relation. The field value is then read from the source issue and written to the destination issue. Other post functions do not have a source and destination; you simply define the issue relation that applies to the post function. For example, the [Create a Linked Issue](/cms_trial/space/JSUCLOUD/12518348/Create+a+Linked+Issue+post+function/) post function creates a new issue and then connects it through an issue relation to the issue in transition.

### Related issues limitations

While we try to execute as many configurations as possible, you should keep some restrictions in mind.

- Copy Value From Other Field post function: There should be only one source issue; otherwise, it is unclear from which issue the value should be read. The current implementation will simply select one of them and ignore the rest.
- If you use the Create a Linked Issue post function to create a new subtask, you must also configure the post function to create the new issue as a subtask issue type. The target project must be the same as the one for the issue in transition.

[unmapped inline: placeholder]