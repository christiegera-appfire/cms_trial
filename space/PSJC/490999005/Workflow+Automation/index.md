# Workflow Automation

Power Scripts lets you add custom conditions, validators, and post functions to Jira workflows by using SIL and Jira Expressions.

## **Introduction to SIL and JavaScript**

Workflows within Jira Cloud operate in the same asynchronous manner as other Jira integrations. While Jira and Power Scripts function as distinct entities, this asynchronicity presents a challenge. While it was somewhat manageable for workflow actions, it proved infeasible for conditions and validators. In these cases, you need to determine the viability of a transition before it's executed.

To address this challenge, Atlassian introduced the capability to trigger external actions asynchronously within the workflow. This ensures that any failures in such actions do not disrupt the transition process. Jira gains the freedom to silently retry action execution as needed, especially when an action fails to respond within a specified time or returns an error.

Additionally, Atlassian mandated coding standards and validators for JavaScript, ensuring they can be executed safely on the Jira host. To mitigate potential performance concerns, the scope of conditions and validators was intentionally restricted.

| **Where** | **Language** | **Obs** |
| --- | --- | --- |
| **Conditions** | JS (Jira Expressions) | <https://developer.atlassian.com/cloud/jira/software/jira-expressions-type-reference/>  synchronous, executed within the host product (Jira) |
| **Validators** | JS (Jira Expressions) |
| **Actions** (Actions) | SIL | asynchronously fired; they may be retried if declared synchronous on SIL Engine or *“fire and forget“* if declared asynchronous in execution on the SIL Engine.  Run in the Power Scripts SIL engine. |

Even if a SIL to Jira Expression translator existed, you would remain limited by the predefined constraints and criteria established by Atlassian. Your translation tool would have inherent limitations, preventing it from performing beyond these defined parameters.

## Configuring Conditions, Validators, and Post Functions

After you install Power Scripts for Jira, go to the **Administration > Workflows** page and create a workflow associated with a project.

![Jira workflow administration page showing available workflows and the Edit option.](/cms_trial/assets/40842366-34a9-46ab-a0d2-dc8d94501cbf.png)

Active workflows can't be edited. Create a draft workflow before making changes. Select the workflow and click **Edit**:

![Workflow actions menu with the Edit option selected.](/cms_trial/assets/56c9e105-1fe3-444b-ae1d-906b1eac5bf4.png)

The workflow editor opens in one of the following views.

### Text View

![Workflow editor in Text view showing workflow transitions.](/cms_trial/assets/c9144367-9a0b-4feb-b5a7-abaf6a020144.png)

1. Use the **Diagram** and **Text** buttons to switch workflow’s views.
2. Click the transition name to edit the transition.

### Diagram View

![Workflow editor in Diagram view with transitions between statuses.](/cms_trial/assets/3f7d7286-72c3-407a-a49a-c6b5c518131d.png)

1. The **Diagram** and **Text** buttons can be used to switch the view mode of the workflow.
2. In **Diagram** view, click a transition line to see the transition options.
3. Once a transition is selected you can click the **Conditions**, **Validators** and **Post Functions** link for that transition.  
   Selecting a transition displays its transition triggers, conditions, validators, and actions.

![Workflow transition details showing conditions, validators, and post functions.](/cms_trial/assets/b1f6c173-6350-446a-8079-7a310a749b5b.png)

- The transition is made possible only if the conditions are fulfilled. They may be called multiple times, are always synchronous, and run within Jira. Extensions / plugins need to use the *Jira Expressions*. A condition **must** return true or false to signal whether the condition is met or not.
- The validators must validate data before the transition is fired. Again, they may be called multiple times (for instance user corrects input errors on UI). Extensions / plugins need to use the *Jira Expressions*. A validator must return true or false and optionally the field and the error message you want to show in the user interface.
- The actions are called every time when a ticket advances from one state to another. Jira doesn't wait for them to finish, but rather triggers them on the remote extension / plugin (in our case Power Scripts). If action fails, it’s retried.

An important consequence of the above model is that conditions and validators should not have side-effects. In fact, Jira Expressions are guaranteed not to have side-effects by construction. However, actions are allowed to make any changes to the issues, including advancing the issue in the workflow, and here’s where we shine.

To create conditions, validators and actions, click the corresponding **Add <object type>** link at the top of the workflow management tab (*Add condition* / *Add validator*/ *Add action*).

### Post functions

The following image shows how to create an action.

![Add Post Function to Transition page with Power Scripts SIL Post Function option selected.](/cms_trial/assets/205d06bc-38e0-4da1-9fa1-b0d06a97d6da.png)

After you click the **Add** button, you have 3 options:

- **Template** - use the script template editor to create a new script
- **New Script** - create a new script directly in the workflow editor
- **Existing Script** - use a script that has already been written and exists in the SIL Manager

![Select script type dialog with Template, New Script, and Existing Script options.](/cms_trial/assets/0e052950-eecb-4551-a913-9c8436f9162f.png)

For this example, choose **Existing Script** and click **Next**.

![Select script location dialog opened.](/cms_trial/assets/f7820496-987d-45fd-a74e-2ab221933ac8.png)

Click the **Edit** icon (pencil) next to the **Specify script** input to select the script to use for the action.

![Select file dialog open and the test.sil file selected.](/cms_trial/assets/1515581e-937e-426c-8607-9fc4b351ed0d.png)

Click **Select** to apply the selected script as a action.

You can create a new script or pick a script that was already created in the *silprograms* folder.

Return to the transition screen to see the newly added action in the view:

![Workflow transition showing the configured Power Scripts post function.](/cms_trial/assets/35658a5e-7d53-428d-b085-8bfbe2675a5f.png)

**Important**

It is advisable to **move the action last**, like in the above image. This ensures that the issue - on which the action is triggered - is **fully updated** by Jira prior to the execution of the action.

**Publish the workflow**

A common mistake is that workflow is not published and therefore the action is not active. Publish the workflow before testing the action.

### Updating the action

To change the action you need to go through the above wizard, and this includes execution options. However, if you change the code of the action directly in the SIL Manager, the changes are immediate, the SIL Engine determines that the action has been changed and picks the changes, re-parses it and executes the new code.

### Execution of Actions (Actions)

In case you defined multiple post-functions for the same action, note that the order of execution is heavily dependent on the moment of Jira triggering them and it cannot be guaranteed. Unlike the server/DC product, you should always favor one single post-function per transition action.

Actions always run in the same engine thread that receives the HTTP request. This ensures the best performance for a variety of use cases. However, if runtime exceeds 5 seconds, use schedule functions to run the code that is taking longer or declare the action as **asynchronous**. This frees the thread to handle another request.

If the action takes too long, note that it will be retried by Jira. So even if your action is happily running with no errors, you may encounter the same trigger because Jira does not yet received a response from the first run. For long running actions always use the asynchronous execution, or schedule the execution at a later time using one of the scheduler functions.

It is recommended to measure your script performance. To do this, go to **Runtime -> Script Performance**. If you notice longer runtime on actions, delay part of the processing using scheduler functions such as runScriptIn(), or better, declare it ***asynchronous***.

### Conditions and Validators

Conditions and validators may be configured starting in the same point as for actions. They serve different purposes, but the language they are expressed in is the [Jira Expressions](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) language. Power Scripts allows you to either configure a pre-defined condition or validator (i.e. built by us) or define your own. For the purpose of this document, we will show how to define your own so you can achieve the flexibility you need in your workflows.

**Retain**

Return type for Conditions and Validators is always a boolean.

Let’s open again the transition view, but this time we will select the *Conditions* tab.

![Workflow transition screen with the Conditions tab selected.](/cms_trial/assets/04fe8fd5-1de9-470e-ac86-f01a99768259.png)

Let’s add a condition. Click **Add condition** to open the next configuration screen. Select **Power Scripts Condition**.

![Add condition dialog showing the Power Scripts Condition option.](/cms_trial/assets/51a1d4e7-f99a-4f42-82f9-ca0197b5f8bc.png)

The next screen will look familiar to you:

![Select script type page with the Write your own option selected.](/cms_trial/assets/5162a747-949e-47c9-ae35-8fd200d4468e.png)

We will choose to write our own condition. Because we want to allow the transition to happen only if there are at least 2 comments, enter the following *Jira Expression* in the code box:

```text
issue.comments.length > 1
```

like this:

![Custom workflow condition with an example Jira expression in the Enter your Javascript code field.](/cms_trial/assets/df280a77-0785-46d6-a047-2356016fed73.png)

Click **Next. C**lick **Add** when the *Final step* page opens.

![Jira workflow confirmation screen to add and save the condition.](/cms_trial/assets/39005b0f-642e-4642-bb40-c33d4a15aa77.png)

Clicking **Add** too quickly results in an incompletely configured element in the workflow. Keep in mind that we do not control the elements outside the sandbox we’re showing the wizard above.

If everything worked correctly, you’ll return to the transition view screen:

![Workflow transition screen displaying the configured condition.](/cms_trial/assets/77a11d65-8518-4642-a5bb-ee7c094f2714.png)

Add a validator. Select the *Validators* tab and click **Add validator**.

![Workflow transition screen with the Validators tab selected.](/cms_trial/assets/608ab489-f80e-4943-b115-d6365856f9fc.png)

From the list of validators, choose Power Scripts validators. We will also write code for this one too, it’s the most flexible option.

![Add Validator to Transition dialog showing Power Scripts Validator option selected.](/cms_trial/assets/be66b45c-88df-4ccc-8b95-e9e0b6f9eb42.png)

Click **Add** and select ***Write your own***. To fully customize this, we add this code, requiring it to have at least one attachment.

```text
issue.attachments.length > 0
```

![Edit script screen showing example of adding an error message for the validator, and entering Javascript.](/cms_trial/assets/27225b51-bb9d-4d5a-a6eb-5a94f0186f41.png)

Enter a message for the validator. It will be shown in the UI when the expression on the right will return false.

Once again, click **Add** for Jira to fully configure the validator:

![Jira workflow confirmation screen for adding the validator.](/cms_trial/assets/b6ecea6c-4cca-4466-a891-d6cb4a4ef38a.png)

It will return you to the transition view, where we have one condition and one validator.

![Workflow transition showing configured conditions and validators.](/cms_trial/assets/f95d2340-4872-47e4-a330-f7668a558498.png)

We are now ready to publish the workflow. After you published it, we are ready to test it. Choose an issue with at least two comments, otherwise you will not see the transition you configured (because it will be hidden by the condition that’s unfulfilled), and try to transition it. If you do not have any attachment, you will receive the error message from the validator:

![Jira workflow transition displaying a validator error message for missing attachments.](/cms_trial/assets/85c3d9f4-407e-44c7-a4eb-0c837e7d1830.png)

However, if you attach something, the transition will succeed:

![Jira issue transition completed successfully after meeting validator requirements.](/cms_trial/assets/8234bac5-67c0-494c-b2b7-95ad9948e57b.png)

**See More**

- [Writing Actions (Post-Functions)](/cms_trial/space/PSJC/490999217/Writing+Actions+(Post-Functions)/)
- [Writing Conditions and Validators](/cms_trial/space/PSJC/584581177/Writing+Conditions+and+Validators/)
- [Scripted Conditions and Validators in cloud - a new paradigm](/cms_trial/space/PSJC/804552898/Scripted+Conditions+and+Validators+in+cloud+-+a+new+paradigm/)