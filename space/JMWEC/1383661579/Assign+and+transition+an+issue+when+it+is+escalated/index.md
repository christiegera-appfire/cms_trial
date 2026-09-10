# Assign and transition an issue when it is escalated

| **Goal** | When an issue is escalated, automatically assign it and move through a Transition |
| --- | --- |
| **Scenario** | You want to begin work immediately when an issue is escalated. To do this, the issue will be assigned and automatically transitioned to the **In Progress** status, and a notification sent to the assigned user. |
| **Components** | [Event-based Action](/cms_trial/space/JMWEC/465473524/Event-based+actions/): Issue updated event, [Assign issue(s)](/cms_trial/space/JMWEC/1133772861/Assign+issue(s)/) post function, [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) post function |
| **Baseline** | - Any issue that is escalated (for example, by having an **Escalated** checkbox selected) will be automatically assigned and transitioned to **In Progress**. - The issue will be assigned to the Project Lead, who can then assign it as needed. |

---

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)
- A custom field called **Escalated**, or Jira Service Management (JSM) installed on your instance which includes the **Escalated** field. See <https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/> for steps on creating a custom field.

## 1. Create the Event-based Action

1. Log into your instance as an administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Apps**.
4. In the left-hand panel under *JIRA MISC WORKFLOW EXTENSIONS,* click **Event-based actions** and click **Create new action** in the upper right corner.
5. Give your Event-based action a name and, optionally, a description.
6. Under **WHEN**, make sure **Select Event** is selected. In the right-hand panel, select **Issue Updated** (**Figure 1**, pictured right).
7. Set the other options under **WHEN** as needed.
8. Under **IF SCOPE**:

   1. Leave **Projects** set to *Any*.
   2. Leave **Issue Types** set to *Any*.
   3. Check the box for **Only apply to issues that match a Nunjucks condition**.
   4. Click the **Nunjucks** text field and enter the following (**Point 1**, **Figure 2**, right):   
      ⚠️ You **MUST** update the script below - the `<your field id>` placeholder - with the field ID of your **Escalated** field (see **Configure the Nunjucks Script**, below).

      ```text
      {% if (not context.changelog.fields["<your field id>"].from.length) 
         and (context.changelog.fields["<your field id>"].to_string == "True" )  
      %}
      	true
      {% else %}
      	false
      {% endif %}
      ```
   5. Click **Save** (**Point 2**, **Figure 2**, right)

### Configure the Nunjucks Script

The Nunjucks script in **Step 8**, above, will test if both of these conditions are true at the time the issue is updated:

- The **original** value of **Escalated** was empty AND
- The **updated** value of **Escalated** is `True`.

In other words, among the edits that occurred to trigger the event, the Escalated field was set to `True`. If the value is already `True` and other edits occur or the edits do not include the **Escalated** field, the Event will not trigger.

You **MUST** update the `<your field id>` placeholder in the script above with the field ID of your **Escalated** field. To do this:

1. Click the **Issue Fields** help tab along the bottom of the script editor.
2. Select *Escalated* from the **Select a field** pulldown menu.
3. Take note of the custom field ID displayed in the examples (Figure 3, right). In this example, the field ID is `customfield_10071`.
4. Enter your custom field ID in the script, replacing `<your field id>`.

![Event-based Action event selection screen](/cms_trial/assets/17867f3f-c259-491b-a9f0-72c843ac42a2.png)![JMWE for Jira Cloud Nunjucks condition configuration for escalated issue assignment and transition](/cms_trial/assets/6ae2997e-b36d-452c-86a6-0022aee5a0e2.png)![JMWE for Jira Cloud custom field configuration for escalated issue assignment workflow](/cms_trial/assets/2cc0b8e0-92fc-43ff-9d72-ac28a20d46e3.png)

## 2. Add the *Assign issue(s)* post function

1. Under **THEN**, click **Select Post-functions**.
2. In the right-hand panel, click **Assign issue(s)** in the list of post functions. The [*Assign issue(s)*](/cms_trial/space/JMWEC/1133772861/Assign+issue(s)/) *post-function* configuration screen will open.
3. For **Target issues** leave the default value of *Current Issue*.
4. For **Assign to** select *Project Lead*.
5. Leave **Assignment behavior** as the default value of *Always*.
6. Configure the remaining options as needed.
7. Click **Save**.

![Assign issue post function configuration screen](/cms_trial/assets/21a9b103-00aa-4aab-bfaf-1007e48b122e.png)

## 3. Add the *Transition issue(s)* post function

It is recommended that you use the transition ID when selecting transitions; if the selected transition(s) are renamed in your workflow, this post function will fail until you update the post function!

1. Under **THEN**, click **Select Post-functions** if it is not already selected.
2. Click **Add Post-function** in the upper-right corner of the right-hand panel.
3. Select **Transition issue(s)** and click **Add**. The [*Transition issue(s)*](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) *post-function* configuration screen will open.
4. Leave **Target issues** as *Current Issue*.
5. Click the **Transition Picker** button to select a Transition.
6. In the *Pick a transition* window:

   1. Select your workflow from the **Workflow name** pulldown menu.
   2. Select the transition for moving issues into the **In Progress** status (e.g. **Begun Development** in Figure 5, right).
   3. Click **Use transition ID**.
7. Configure the remaining options as needed. See [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) for more information on this post function.
8. Click **Save**.

### Alternate Configurations

Depending on the status of the issue when it is escalated, it may be necessary (or just desirable) for you to add additional transitions to this list of transitions in the post function configuration. For example, if the issue is in a holding status such as **Waiting for Info**, you may want to add the transition between that status and **In Progress** to the list, placing it below the **Begun Development** transition.

JMWE treats the list of transitions as prioritized list of transitions to attempt when the post function is triggered for an issue. It will apply the first transition that is available for the issue.

## Save and Test the Action

In the main Event-based Action editor, click **Save** to complete the configuration. To test the new action, create a new issue but leave it unassigned and in your Backlog. Then edit it to set the **Escalate** field to ‘True’. Verify that JMWE assigns the issue to your Project Lead and moves the issue to **In Progress**.

### Congratulations!

Your issues will now automatically move into your workflow when they required special attention!

![Transition Issue post function configuration screen](/cms_trial/assets/d89e2d7f-ae57-4fe5-a03f-6c4f68a415c0.png)