# Escalate Issue After Fix is Rejected

In this recipe, you will learn how to escalate an issue when the fix has been rejected a certain number of times. This scenario could arise most frequently in a **Jira Service Management** context where an end user or customer might reject a proposed fix, but the recipe can be applied to any Jira project where there is a threshold for the number of times an issue should be allowed to be re-worked before it is given extra consideration.

There are a few ways in which an issue can be marked as escalated:

- Set the native Jira `Flagged` field
- Set the priority of the issue to a high value
- Create a custom field for escalations; this method works particularly well when there are multiple types of escalations
- Create a status for Escalated issues

**Note**: If you plan to use a specific status for **Escalated** issues, the Recipe [Hold an Issue, Seek Clarification, Then Proceed](/cms_trial/space/JMWEC/466322207/Hold+an+issue%2C+proceed+when+clear/) is a better solution. That recipe can be modified to use a status for high priority issues that require immediate attention.

Using any of the methods above provides powerful options for identifying and working with issues that require immediate attention or that have proven problematic. These include:

- Creating custom dashboard widgets (see this page for more information: <https://support.atlassian.com/jira-software-cloud/docs/create-and-edit-dashboards/>)
- Creating a swimlane for escalated issues ( see this page for more information: <https://support.atlassian.com/jira-software-cloud/docs/configure-swimlanes/>)
- Adding a column to a Kanban board for escalated issues (see this page for more information: <https://support.atlassian.com/jira-software-cloud/docs/configure-columns/>)

The steps below include two options for representing the escalation of an issue. The first uses a custom field called **Escalated**, which can be either a simple escalation flag (a check box custom field) or a more complicated escalation process that can include multiple escalation types. The second uses the native Jira field `Flagged` and sets it to true.

Both of these options use a custom field to track the number of times an issue fix has been rejected, and both use a post-function on the transition that is triggered when a fix has been rejected.

---

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions for Jira Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)
- Jira Misc Custom Fields for Jira Cloud

This Recipe uses an additional Marketplace app - **Jira Misc Custom Fields (JMCF)** - to track the number of times a fix has been rejected. The custom field uses the [Transition Count](https://appfire.atlassian.net/wiki/spaces/JMCFC/pages/465600697) custom field type, which calculates the number of times an issue has been moved through a specific workflow transition.

If you do not have access to **JMCF for Jira Cloud**, it is still possible to achieve the same outcome but it will require extra steps. Instead of using a single JMCF custom field, you will need to create a standard custom Number Field and an additional post-function that increments the Number field. These additional steps are *not included* in this Recipe.

## Workflow configuration

Consider the workflow shown in **Figure 1**, right. This workflow is based on the default IT Service Management workflow.

In this configuration, the **Resolved** status is categorized as Done, but it is an unconfirmed resolution. A workflow could be configured this way to differentiate between an issue that the support team considers fixed but reporting requirements make it necessary or preferable to track closed issues separately. Additionally, an automation could be configured to close Resolved issues (and *only* Resolved issues) after several days of inactivity. Lastly, it enables the **Fix Rejected** transition, which is an integral part of this Recipe!

![JMWE for Jira Cloud workflow diagram for escalating issues after fix rejection](/cms_trial/assets/c071d4a0-2c4d-4d9f-8800-3054d77913d0.png)

## 1. Create a *Transition Count* custom field for “Rejected Count”

As noted above, this step requires an additional Marketplace App - **Jira Misc Custom Fields (JMCF)**.

Before updating your workflow, you need to add a custom field to your Jira instance; this custom field will store the number of times an issue has been moved through a transition. This custom field will track the number of times, if any, an issue is moved through the **Fix Rejected** transition.

1. Log into your Jira instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Apps**.
4. In the left-hand panel, click **Jira Misc Custom Fields** then click **My custom fields**.
5. In the upper-right corner, click **New custom field**.
6. In the window that opens, select **Transition Count** and click **Next**.
7. Select the screens on which the new field should be included. Click **Next**.
8. Configure the custom field:

   1. **Transition From Status** - Select `Resolved`.
   2. **To Status** - Select `Reopened`.
   3. Click **Save**.

![JMWE for Jira Cloud custom field configuration panel for fix rejection escalation](/cms_trial/assets/c542f7b8-4c70-4447-8e85-cc556bec4ab0.png)

## 2. (Option 1) Create a custom field for “Escalation”

This section is optional. There are Jira standard fields such as **Flagged** or **Priority** that can be used to represent an escalated issue. If you plan to use **Flagged**, it may need to be added to you issue **Field Configuration**. See this page for information on adding fields to an issue: <https://support.atlassian.com/jira-cloud-administration/docs/change-a-field-configuration/>.

*If you choose to use one of the above fields, you can skip this section.*

In this section you will create a custom field that represents the escalated state of the issue. This is a standard Jira custom field, and can be a check box for a straightforward Escalated/Not Escalated configuration. Or it can be a Select List that enables you to create multiple Escalated states, each of which could be handled differently (e.g. different teams or other, different automations for each state).

1. Log into your Jira instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Issues**.
4. In the left-hand panel, click **Custom fields**.
5. In the upper-right corner, click **Create custom field**.
6. From the list of Standard fields, select the type for your scenario:

   1. **Checkboxes** - For a single Escalated/Not Escalated setup.
   2. **Select List** - For multiple, different Escalated states.
7. Configure the field (Figure 3, right):

   1. **Name** - Enter “Escalated”.
   2. **Description** - (Optional) Enter a description.
   3. **Options** - Enter the needed options.

      1. For a **Checkbox**, create a single option suck as **True** and click **Add**.
      2. For a **Select List**, create any options needed and click **Add**.
8. Click **Create**.

![JMWE for Jira Cloud escalated field display in issue view](/cms_trial/assets/79c137c4-aebc-4bdd-b93f-9ba3b32ad110.png)

## 3. Open the workflow

Once you have the custom fields added to your issues, you can update the workflow.

To add a post-function:

1. Log into your Jira Server instance as an Administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Issues**.
4. In the left-hand panel, click **Workflows**.
5. Click **Actions (** [actionmenu icon] ) for the workflow you want to edit and select **Edit**.
6. Edit the Transition:

   1. When viewing the Workflow in **Diagram** view, select the Transition and click the **Post Functions** link. Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.

## 4. Add a *Set issue field(s)* post-function to the “Fix Rejected” transition

The last step of this Recipe is to add a [Set issue field(s)](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post-function to the transition between the **Resolved** status and the **Reopened** status. This post-function will only fire conditionally - if the **Rejected Count** field value is greater than or equal to 3, the post-function will set the **Escalated** field to True.

1. In your workflow, add a post-function to the **Fix Rejected** transition:

   1. When viewing the Workflow in **Diagram** view, select the Transition and click the **Post Functions** link. Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.
2. Select ***Set issue fields (JMWE app)*** from the list and click **Add**.
3. Configure the post-function as follows:

   1. **Target issue(s)** (**Point 1**, **Figure 4**, right) - Set to `Current issue`.
   2. **Add field(s)** (**Point 2**, **Figure 4**, right)- Select the field you’re using for escalation, e.g. `Flagged`, `Priority`, or the custom field you created in Step 2 above, `Escalated`.
   3. **Options** - Set as needed. For example, if using `Flagged` or a checkbox version of `Escalated`, set the option `Set only if field is empty` so that the post-function will only attempt to escalate an issue that isn’t already escalated.
   4. **Value** (**Point 3**, **Figure 4**, right) - Enter `True`if using checkboxes, or the value to select if using a Select List.
   5. Click **Add** (**Point 4**, **Figure 4**, right).
   6. **Send notifications** - Configure as needed.
   7. **Conditional execution** (**Point 5**, **Figure 4**, right)

      1. Check the box for `Run this post-function only if a condition is verified`.
      2. Enter the following in the code editor:   
         `{{ issue.fields["Rejected Count"] >= 3 }}`
   8. **Run as** - It is recommended to leave this set to `Addon user`.
   9. **Delayed execution** - Configure as needed.
4. Click **Add**.

![JMWE for Jira Cloud postfunction configuration dialog for fix rejection workflow](/cms_trial/assets/2ffbe57d-2017-44fd-a16d-1d2ad36b692b.png)