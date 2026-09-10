# Define field values for new linked issues

---

|  |  |
| --- | --- |
| **Goal** | Automate the creation of linked issues and their associated field values |
| **Scenario** | You are a Hiring Manager and you are onboarding a new Marketing Assistant. Your tasks to complete the onboarding could include:   - *Create new contract* - *Order new computer*   Let’s see how JSU can create these linked tasks and associated issue fields when an origin Jira issue called *Hiring a Marketing Assistant* moves to in progress. |
| **JSU Components** | [Create a Linked Issue](/cms_trial/space/JSUCLOUD/12518348/Create+a+Linked+Issue+post+function/) post function |

## Example setup

Follow the interactive demo to learn how to set up this use case, or follow the numbered steps below.

## How to configure this rule

1. Create a draft of your project workflow. If you're unsure how to get to this page, follow the onboarding steps in [Edit a Jira Workflow](https://appfire.atlassian.net/wiki/spaces/JSUCLOUD/pages/12519274). You can then view your workflow in Text or Diagram mode. The steps in this use case represent Diagram mode. If you haven't already done so, switch the workflow viewer to Diagram mode.
2. We want to set the rule on the in progress transition so that two subtasks are automatically created. Select the arrow that points to the **In Progress** status to show the transition rule Options menu.

   ![Screenshot of a draft Jira workflow in diagram view with the transition options menu displayed.](/cms_trial/assets/c30dc021-4194-4667-bff1-1decc94eda47.png)
3. Select **Post Functions** from the list of options.
4. On the *Post Functions* tab, select **Add post function**.

   ![Screenshot of the Post Function tab of the Jira workflow transition page.](/cms_trial/assets/f8ce84f9-7d08-4f33-90b0-836918502b46.png)
5. Select the *Create A Linked Issue (JSU)*post function and click **Add**at the bottom of the page.

   ![List of available workflow post functions with the Create a Linked Issue post function highlighted in yellow.](/cms_trial/assets/5aac2cf9-0644-4d79-b977-b6d88dda3214.png)
6. Now, let's configure your first post function:

   1. We want to perform the automation inside the same project; for the*Target Project*, we select **Inside same project**.
   2. We want our new issue to be related via Subtask; in *The new issue will be related via* option*,* we select **Sub-Task***.*

      ![Example configuration of the Create a Linked Issue post function.](/cms_trial/assets/e4d3b4d3-865a-42bf-ac97-1eb0e12cae5e.png)
7. Now, let's configure the values of different issue fields. In this case, we want to copy a field value from the original issue (our task) to the new issue (a new subtask).   
   Select **Add configuration**at the bottom of the post function configuration page.
8. From the list of operations, select **Add**for the *Copy to New* operation.

   ![List of optional sub-functions for the Create a Linked Issue post function.](/cms_trial/assets/4686f29f-5d2c-485c-ae2c-0f9f4914aaed.png)
9. In the Copy to New sub-function configuration, let's copy the task's **Assignee** to the **Assignee** of the subtask.

   ![Copy to New sub-function set to Assignee.](/cms_trial/assets/033b74ed-7b34-4949-8e01-7ce15f69c0a8.png)
10. Next, we want to copy the value from one field to another field within the origin issue. We once again select **Add configuration*****.***
11. We want to copy the Summary field of the origin issue to the Description field of the origin issue, while prepending it with a dash. Select **Add** for the *Copy within Origin* operation*.*
12. In our second configuration, let's copy the **Summary** to **Description**. Select **prepend** and manually type in a dash symbol `-`.

For text fields, you can define the separator for the prepend or append options, for example, `:` , `--`. This allows you to set a consistent pattern for all new issues of specific issue type, for example, a bug, or onboarding subtasks.

![The Copy within Origin sub-function set to prepend Summary to Description.](/cms_trial/assets/ce0c60ee-5011-44a7-9323-13b4af9daaa8.png)

1. We will configure the last operation by setting a value for the Summary of the new subtask. Once again, we select **Add configuration**.
2. We want to set the value for the summary of the new subtask; we select **Add** for the *Set* operation.
3. In our third configuration, we set `Create contract` to **Summary**. After completing your third configuration, click **Add** to add the post function to your workflow. 

   ![The Set sub-function set to overwrite Summary with Create contract.](/cms_trial/assets/72c52c47-6f02-4ee7-9a96-67109ca6b064.png)
4. On the *Post Functions* tab, select**Add post function**.
5. Follow Steps 4 - 15 to create another subtask for ordering a PC. In this case, set the Summary of your new subtask to `order PC`.

   ![Example configuration of the Create a Linked Issue post function.](/cms_trial/assets/cc7a76bc-4970-4843-a9e6-2b284523113e.png)

   We have now added all of our post functions.

   ![Jira workflow transition summary page.](/cms_trial/assets/ad93c160-7001-4e0f-82ff-80289e1636e8.png)
6. Publish your workflow, then let's see our setup in action.

## Test the rule

1. Go to our project and create a task for hiring a Marketing Assistant.

   1. Make the **Summary**, `Hiring Marketing Assistant`*.*
   2. Add `Onboarding process`in the **Description**.
   3. Add an **Assignee.**

      ![Example Jira issue with Description and Assignee fields highlighted.](/cms_trial/assets/10a55b39-ef67-4b4f-a784-156151436797.png)
2. Change the task's status from **Backlog** to **in Progress** and watch the two subtasks appear through the automation we configured!  
   The description of your task is updated because of the *Copy Within Origin* functionality. Your new subtasks have been assigned to the assignee of the task due to the *Copy to New* functionality and their summary is set as configured by the *Set* functionality. That's it; JSU automated the work for you. 

   ![Example Jira issue with two subtasks created through the use case automation.](/cms_trial/assets/d2ce9e2b-406d-4d44-a632-e673a28fda71.png)

---

This was just one example of automating linked issues and field creation. Regardless of your needs, JSU's Create A Linked Issue post function and its operations can help you:

- copy a field value from the origin issue to a new linked issue,
- copy the value from one field to another field within the origin issue, and
- set the value of a field in a new linked issue.

## Related pages

- [Copy fields configuration](/cms_trial/space/JSUCLOUD/12518795/Copy+fields+configuration/)