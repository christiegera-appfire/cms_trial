# Hold an issue, proceed when clear

| **Goal** | Place an issue on hold, and return it to its original status when ready |
| --- | --- |
| **Scenario** | You need to place issues in a holding status ('Blocked', for example) when work can not proceed. Additionally, when work is ready to restart you need to guarantee that the issue returns to its original status before being placed on hold. |
| **Components** | [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post function, [Build-your-own (scripted)](/cms_trial/space/JMWEC/465474365/Build-your-own+(scripted)+Condition/) condition |
| **Baseline** | - Your workflow must include a status specifically for holding issues outside the normal flow of work. - A custom field exists or is created to store the return transition for the issue (e.g. **Return to In Progress**). |

This setup can be used for a variety of scenarios. For example:

- Blocking an issue that cannot proceed for any reason (this use case)
- Requesting more information before continuing work
- Pausing work on an issue that needs to be delayed, reassigned, or moved to a future sprint

Alternatively, you could use this setup to *hide* an issue from your Kanban board by setting up the “on hold” status value under a status that is not included in the board.

---

## Requirements

- Jira Administrator login
- [Jira Misc Workflow Extensions for Jira Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe?hosting=cloud&tab=overview)
- An updated workflow that includes an on-hold status such as **Blocked** (Figure 1, right), or a workflow that can have this status added.

**Note**: The configuration requires a custom field that will store the name of the transition that should be used when the issue leaves the “on hold” status. This use case uses a standard short text custom field and a post function that creates a concatenated value that enables transition names to be more clear. For example, you will create a standard transition from the In Progress status to the hold status **Blocked**:

- **In Progress → (Transition)** ***Blocked*** **→ Blocked**

The return transition *from* Blocked *to* In Progress uses the original status value of “In Progress” to store a transition name that will return the issue to its original status:

- **Blocked → (Transition)** ***Return to In Progress*** **→ In Progress**

## Workflow configuration

**Blocked** is a status available at several points in the workflow - specifically to any status under the **In Progress** category (blue status nodes). This configuration was chosen because, at any point in the development process, it may be necessary to sidetrack an issue while waiting for the resolution of questions or problems.

![sideTrack-Workflow.png](/cms_trial/assets/7a446bac-337f-4d0d-a3e8-46c5be7186a1.png)

In this example, the workflow is configured so that:

- Only statuses that are in the **In Progress** category (blue status nodes in Figure 1, below) have transitions to a status labeled **Blocked** - the “on hold” status.
- All incoming transitions to **Blocked** use the same transition - a transition called **Blocked**.
- Outgoing transitions from **Blocked** use the formula “Return To” and the name of the original status (e.g. “Return to In Progress”)

In your Jira instance, the status values may be labeled differently, or you may have additional statuses that need to be connected to the “on hold” status. You may have multiple “on hold” status values (such as both **Blocked** and **Waiting for Clarification**). If you have different values, just substitute your status values in the steps below. If you need more than one “on hold” status, just repeat the steps below for each holding status.

## 1. Create a custom field for tracking return status

Before updating your workflow, you need to add a custom field to your Jira instance; this custom field will store the name of the transition that should be used when removing the hold from an issue.

1. Log into your Jira instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Issues**.
4. In the left-hand panel, click **Custom fields** and click **Create custom field** in the upper right corner.
5. From the list of **Standard** fields, select `Short text (plain text only)`. Click **Next**.
6. For the name, enter “Return Transition” (Figure 2, right). Enter a description if desired.
7. Click **Create**.
8. Associate the custom field with any screens that are used in the ***workflow*** being updated.
9. Click **Update**.

![contentId-466322207](/cms_trial/assets/ad7484d0-f1cf-438c-80a5-96c8ea7d571d.png)

## 2. Open the workflow

To edit a workflow:

1. Log into your Jira Server instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Issues**.
4. In the left-hand panel, click **Workflows**.
5. Click **Actions (** [actionmenu icon] ) for the workflow you want to edit and select **Edit**.

## 3. Add *Blocked* status and transitions

In the following section you will add the **Blocked** status, if it does not already exist. Additionally, you will add all necessary transitions to and from this status. **If you need to create an new status**, see this page: <https://support.atlassian.com/jira-cloud-administration/docs/configure-statuses-resolutions-and-priorities/>.

Open your workflow using the steps above, then follow these steps:

1. In the upper-left hand corner of the workflow editor, click **Add Status**.
2. Select **Blocked**, and click **Add**.
3. In the upper-left hand corner of the workflow editor, click **Add Transition**
4. On the **New Transition** tab, set the following options (**Figure 3**, right):

   1. **From status** - Select **In Progress**.
   2. **To status** - Select **Blocked**.
   3. **Name** - Enter “Blocked”.
5. Add the **Blocked** transition *from* **Code Review** to **Blocked**. In the Add Transition window, select the **Reuse a Transition** tab and select **Blocked**.
6. Add the **Blocked** transition *from* **Testing** to **Blocked**. In the Add Transition window, select the **Reuse a Transition** tab and select **Blocked**.
7. Repeat Step 4, above, to add a transition *from* **Blocked** to **In Progress**. Name the transition “Return to In Progress”.
8. Repeat Step 4, above, to add a transition *from* **Blocked** to **Code Review**. Name the transition “Return to Code Review”.
9. Repeat Step 4, above, to add a transition *from* **Blocked** to **Testing**. Name the transition “Return to Testing”.

![sideTrack-AddTransition.png](/cms_trial/assets/51226794-7a81-474c-8ec9-254c759e93fb.png)

## 4. Add a *Set issue fields* post function to the *Blocked* transition

In this section you will add a JMWE post-function to the **Request Clarification** transition. The [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post function will update the issue being transitioned with the name of the transition that should be used when moving the issue *out* of the **Blocked** status.

1. In your workflow, add a post function to the **Blocked** transition:

   1. When viewing the Workflow in **Diagram** view, select the Transition and click the **Post Functions** link. Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.
2. Select **Set issue fields (JMWE app)** from the list and click **Add**.
3. Configure the post function as follows:

   1. **Target issue(s)** (**Point 1**, **Figure 4**, right) - Set to **Current issue**.
   2. Under **Fields to update** click **Add** (**Point 2**, **Figure 4**, right).
   3. For **Field**, select **Return Transition** (**Point 3**, **Figure 4**, right).
   4. **New Value** (**Point 4**, **Figure 4**, right) - Enter the following script:   
      `{{ ["Return to ", transition.from_status] | join }}`
   5. Click **Add** (**Point 5**, **Figure 4**, right).
   6. **Additional options** - Leave blank.
4. Click **Add**.

![sideTrack-SetIssueFields.png](/cms_trial/assets/2b8326a3-1f16-4a82-a125-313cd7e6c1e8.png)

## 5. Add a *Build-your-own (scripted) Condition* to each outgoing transition

The last step in this configuration is to add a condition to each of the outgoing transitions from **Waiting for Clarification**. These conditions will guarantee that only the transition back to the original status is available.

1. In your workflow, add a condition to the **Return to In Progress** transition:

   1. When viewing the Workflow in **Diagram** view, select the Transition and click the **Conditions** link. Click **Add condition** at the top of the list of existing conditions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Conditions** tab. Click **Add condition** at the top of the list of existing post functions.
2. Select **Build-your-own (scripted) Condition (JMWE app)** from the list and click **Add**.
3. Give your condition a description, if desired.
4. Under **Choose type** select **Jira Expression**.
5. In the **Jira Expression** editor (Figure 5, right), click the **Issue Fields** tab of the Help section (**Point 1**, **Figure 5**, right).
6. From the **Select a field** pulldown menu (**Point 2**, **Figure 5**, right), select **Return Transition**.
7. Click the first box under **Testing the field’s value** (**Point 3**, **Figure 5**, right) to insert the code into the editor.
8. Replace `"A string"` with `"Return to In Progress"`.
9. Click **Add**.
10. Repeat steps 1 through 7 for the **Return to Code Review** and **Return to Testing** transitions, replacing `“A string"` in the code editor with the name of the transition.

### 🎉 Congratulations!

You can now place issues in a holding status while awaiting resolution or information from outside your team. Because Jira does not natively support Blocked issues, the addition of an “on hold” status can be a powerful tool, especially when combined with dedicated columns or swimlanes in your Kanban board. This can provide distinct visual cues to the issues that require attention!

![sideTrack-ScriptedCondition.png](/cms_trial/assets/43909e13-d1cf-471a-9c79-a8b2beaac5b3.png)