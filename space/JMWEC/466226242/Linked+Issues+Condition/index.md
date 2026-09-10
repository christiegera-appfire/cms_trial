# Linked Issues Condition

A workflow condition that allows you to hide/show a particular transition from the list of available workflow actions based on the current issue's linked issues. The transition to which the condition is added is available only if these linked issues respect certain conditions.

- This condition does not work with **remote links** (links to Jira issues residing on another Jira instance/server).
- Beware of the default "relates to" link type, which can cause confusion. The problem stems from the fact that "relates to" is both the *inward* *direction* and the *outward direction* of the "Relates" link type. We recommend that you rename one of the directions to "is related to" to avoid confusion. This can be done on the Issue Linking Jira admin page.
- Jira portfolio links are not supported in Jira expressions and hence not available in the condition.

![Linked Issues configuration screen](/cms_trial/assets/c549f3f2-af53-4b0b-afab-38ba0242b5d1.png)

**To add 'Linked Issues Condition' to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to configure the condition on.
2. In the Workflow Designer, select the transition.
3. Click `Conditions`in the properties panel.
4. Click `Add` `condition`.
5. Select **Linked Issues Condition** from the list of conditions.
6. Click `Add` to navigate to the **Linked Issues Condition** screen where you can configure the validator as needed. See **Configuration details**, below.
7. Click on `Add` to add the condition to the transition.
8. Publish the workflow.

When you add this condition to a transition, the add-on checks the specified condition on the linked issues that are of the specified issue link type and issue type; all the other linked issues will be considered as satisfying the condition. You can further customize the condition using the options mentioned in the next section.

## Configuration details

Configure the following:

- **What to validate**  
  **Mode**: Select one of the following conditions that the linked issues must satisfy for the transition to be hidden:

  - **Require certain linked issues**:If the linked issue(s) with the defined **Issue Link Type** and constraintsin the *What to enforce on linked issues*section do not exist, the transition is hidden.
  - **Check linked issues**:If any of the linked issue(s) with the mentioned **Issue Link Type** exists, the transition is hidden unless the respective linked issue(s) respects the constraints defined in the *What to enforce on linked issues*section.
  - **Forbid certain linked issues**: If any linked issue(s) with the defined **Issue Link Type** and constraints in the *What to enforce on linked issues*sectionexists, the transition is hidden.
- **Issue Link Type** (mandatory): Select the issue link type that links the current issue to the linked issue(s) to check the specified condition against.
- **What to enforce on linked issues**

  - **Issue Type** (mandatory): Select the issue type of the linked issues to check the specified condition against.
  - **Additional condition**: Select one of the following:

    - **None:** Select this option to add no additional condition.
    - **At least one linked issue must satisfy the condition below:** Select this option for at least one linked issue to satisfy the condition specified in **Jira expression**.
    - **Every linked issue must satisfy the condition below:** Select this option for every linked issue to satisfy the condition specified [Jira expression](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/).  
      **Jira expression** (displayed only when the options other than **None** are selected): Enter a Jira expression to be run on all linked issues. If the Jira expression evaluates to `true` for all linked issues, only then the workflow condition will pass. If it evaluates to `false` for at least one linked issue the workflow condition will fail. See [How to insert information using Jira expressions](/cms_trial/space/JMWEC/465241623/Using+Jira+Expressions/) for more details on Jira expressions.

---

#### Use case

A typical use of this workflow condition is to hide the transition on the current issue until all its linked issues satisfy certain conditions. Consider a use where you want to hide the “Start Progress” transition on the parent until it has at least one assigned subtask. To configure it:

1. Add the `Linked Issues condition`to the "Start Progress" transition.
2. Select the issue link type `is Parent Of` from the `Issue Link Type` field.
3. Select the option "At least one linked issue must satisfy the condition below"
4. Input the Jira expression:

   ```text
   linkedIssue.assignee !=null
   ```

---