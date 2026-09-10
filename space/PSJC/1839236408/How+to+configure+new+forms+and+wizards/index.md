# How to configure new forms and wizards

The Forms and Wizards feature offers the following configuration approaches for creating panels in the Jira issue view:

- **Single form:** Create a standalone form that appears in a panel.
- **Wizard configuration**: By adding steps in the form configuration screen, you can turn it into a multi-step wizard.
- **Button-based configuration**: Create multiple entry points within a panel, where each button opens its own form or wizard.

There is a limitation of one form configuration per project-issue type combination. This means:

- Each issue type within a specific project can have only one form/wizard configuration assigned to it.
- The same issue type in different projects can have different form configurations.
- If you have already created forms/wizards for all available issue types in your current project, the issue type selection field will appear empty.
- To create a new form for an issue type that already has a configuration in the same project, you must first delete the existing configuration for that issue type.

---

## How to configure a single form

1. Log in to Jira as an Administrator.
2. Open **Apps** > **Manage apps** from your Jira Administration Settings.
3. Go to **Power Scripts** > **Configurations** > **Automations** > **Forms and Wizards**.
4. Click **Add form**.
5. In the *Add form configuration* dialog that opens, fill in the required information.

   1. **Name**: Type a name for the new form.
   2. **Description** (optional): Provide a short description about the new form.
   3. Leave the **Buttons** toggle turned off as illustrated in the screenshot below:

      ![single-form-config.png](/cms_trial/assets/3991c2ff-6f60-4b6c-b08d-96c39617aefd.png)
   4. Select the Jira projects where this form should appear.
   5. Select the Issue types where this form should appear.
   6. Select which side of the issue screen the form should appear on: the right or left column.
6. Click **Save**.  
   The form appears on the *Forms and Wizards*configuration page*.*
7. To add the scripts for your form, click the **Edit scripts and steps** icon in the *Operations* column.

![single-form-entry.png](/cms_trial/assets/ca28c886-bcfd-495a-86d4-e4b8168c9a88.png)

This opens the Form configuration page—a specialized version of the SIL Editor where you'll modify the three configuration scripts needed to define your form's behavior and appearance.

- The [Condition script](/cms_trial/space/PSJC/1839235280/The+Condition+script/) determines how the form appears (or doesn't appear) to users in the selected issues. All contextual factors that determine visibility and state, such as user permissions, issue status, field values, or other conditions, must be explicitly defined within the condition script.
- The [Screen script](/cms_trial/space/PSJC/1839235307/The+Screen+script/) determines what is displayed on the form.
- The [Action script](/cms_trial/space/PSJC/1839235954/The+Action+script/) determines what happens when the form is executed.

![form-scripts-config.png](/cms_trial/assets/014e93df-1a4c-4e1f-80d6-368f87c10f60.png)

1. Modify each script and save the changes you made.  
   Once configured, the script files' color changes to green.

   ![form-config-save-icon.png](/cms_trial/assets/c7c2a50c-f981-452b-b596-ec2a2369c907.png)
2. When ready, click **Back** to return to the *Forms and Wizards* page.

For detailed information about each script, see the [Forms and Wizards configuration scripts](/cms_trial/space/PSJC/1843396621/Forms+and+wizards+configuration+scripts/) section.

---

## How to configure a wizard

You configure a wizard by adding one or more steps to a single form. In the Jira issue, wizards are displayed as a progression of steps that start from the main screen of a single form.

1. In your Jira admin console, go to **Power Apps Config** > **Advanced** > **Forms and Wizards**.
2. If you already have a configured form you want to turn into a wizard, locate the form in the list.
3. If you don’t have a configured form, complete the steps in the [How to configure a single form](/cms_trial/space/PSJC/1839236408/How+to+configure+new+forms+and+wizards/) procedure.
4. In the *Operations*column of the form’s listing, click the **Edit scripts and steps** icon.

   ![form-listing-edit-icon.png](/cms_trial/assets/19954848-3265-4bde-903f-dd99208f1be1.png)
5. To add a new step, click the plus sign icon.  
   A new set of scripts appears for the new step.
6. Configure each script type by clicking the **Save** button after modifying each script.
7. To add another step, click the plus sign icon again and configure the three script types for the step.

   ![wizard-config-add-step.png](/cms_trial/assets/acf786e6-6238-439c-b071-057c07927e58.png)

   You can add as many steps as you need for your wizard, and you can also share values between wizard screens.

You can configure a wizard so that certain values on a wizard screen depend on other values from another screen. These [additional functions](/cms_trial/space/PSJC/1839236231/Wizard+functions/) can help you configure the sharing mechanism.

1. When ready, click **Back** to return to the *Forms and Wizards* page.

---

## How to create a button-based configuration

The button-based approach works by creating an initial container form with buttons enabled and configuring a separate form or wizard for each button you add. This creates a hierarchy where the container form holds the buttons, and each button opens its own fully configured form or wizard. This way, each button serves as an entry point to its own complete form or wizard. When configuring a button, you're essentially creating a separate form that will open when that button is clicked.

**Important:**

- The button-based configuration option can only be enabled during initial form creation. It cannot be enabled by editing an existing form.
- You can add, delete, or update individual buttons at any time after creating a button-based form.
- When buttons are enabled, you must configure at least one button during setup. Jira will display a warning message if you enable buttons but don't create any.

1. In your Jira admin console, go to **Power Apps Config** > **Advanced** > **Forms and Wizards**.
2. Click **Add form**.
3. In the *Add form configuration* dialog that opens, fill in the required information.

   1. **Name**: Type a name for the new container form.
   2. **Description** (optional): Provide a short description about the new form.
   3. Turn the **Buttons** toggle on as illustrated in the screenshot below:

      ![form-config-enable-buttons.png](/cms_trial/assets/1075f2a0-0488-4b75-af0d-43edf9641c64.png)
   4. Select the Jira projects where this form should appear.
   5. Select the Issue types where this form should appear.
   6. Select which side of the issue screen the form should appear on: the right or left column.
4. Click **Save**.  
   The form appears on the *Forms and Wizards*configuration page*.* As shown in the screenshot below, the buttons are enabled for this form:

   ![form-listing-buttons-enabled.png](/cms_trial/assets/f621c856-0521-41a3-bcb8-5a5dc4580f17.png)
5. To configure the buttons for your form, click the **Edit scripts and steps** icon in the *Operations* column. This opens the *Buttons*page where you add and manage the buttons' configurations.

   ![PSJC-forms-buttons.png](/cms_trial/assets/976504a5-8d59-4098-b7fe-2e6447271ba9.png)
6. Click **Add button**.
7. Provide a name for the new button and save it. Optionally, you can provide a description.
8. To configure the new button:

   1. Click the **Edit scripts and steps** icon in the *Operations* column.   
      This opens the specialized version of the SIL Editor, where you'll modify the Condition, Screen, and Action configuration scripts needed to define the behavior and appearance of the form associated with this button.
   2. Modify each script and save the changes you made.

Each button's visibility (enabled, disabled, or hidden) is controlled by its own Condition script, allowing for role-based access control.

1. Optional: To associate the button with a wizard, add steps to its form configuration.
2. When ready, click **Back** to return to the *Buttons* page.
3. Repeat steps 6 - 8 to add as many buttons as you need. Each button requires its own complete configuration with Condition, Screen, and Action scripts.
4. To change the order in which the buttons appear in the Jira issue, use the arrows in the *Order* column.

   ![config-buttons-order.png](/cms_trial/assets/b453dcba-89a8-42a9-b5eb-82fbf321265b.png)
5. When ready with all button configurations, click **Back** to return to the *Forms and Wizards* page.

---

## How forms, wizards, and buttons appear in Jira issues

Based on your configuration's **Display mode** setting, your forms, wizards, and buttons will appear in different locations within Jira issues

| **Implementation** | **Example** |
| --- | --- |
| Right column single-form | - To display the form contents, click the **Power Scripts - Power Actions** link as shown in the screenshot below: right-column-config-menu.png The form opens to display the available actions:  right-column-config-form.png |
| Right-column wizard | - A wizard configured to appear in the right-side panel of the Jira issue opens the same way as a single-form: right-column-wizard-step1.png - Once the form is open, follow the wizard’s prompts to complete the action. |
| Left-side buttons configuration | - To display the contents of a form in the left-side panel (main body) of the Jira issue, click **Apps** icon, then select the **Power Scripts - Actions Panel** option:  left-side-config-menu.png The form opens to display the available actions. In this case, it reveals a set of buttons, each one leading to another form or wizard. left-side-config-buttons.png |