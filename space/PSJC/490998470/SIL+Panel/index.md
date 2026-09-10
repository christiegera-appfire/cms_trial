# SIL Panel

SIL Panels enable you to display customized information directly within Jira issues. Using SIL Template Language, these panels present dynamic content from other issues or external databases in a formatted view, reducing the need for additional read-only fields.

Panels can be configured to appear conditionally based on project and issue types, offering tailored information display without requiring custom addon development. You implement and manage these information displays from the *SIL Issue Panels* page.

To learn more about templates, see the [SIL Template language](/cms_trial/space/PSJC/496336897/SIL+Template+language/) documentation.

---

## How to add a SIL issue panel

1. In your Jira Cloud instance, go to **Apps** > **Manage Apps** > **Power Scripts** > **Configurations**.
2. Click the *Automations* tab and select the *Panels*sub-tab.
3. Click **Add panel** andfill in the required fields:

   1. Provide a unique name for your SIL panel configuration.
   2. Select the template file (.tpl) containing your templating code. This file will be executed on every issue page for the associated project and issue types.
   3. Select the project where the panel configuration should be displayed.
   4. Choose the issue types where the panel configuration should be displayed.
   5. Depending on where you want the panel to appear on the issue page, select the panel location—left (main view) or right (side view).
4. Click **Save**.  
   The panel configuration displays as a new entry on the *SIL Issue Panels* page. Open the issue to view how the panel displays in your Jira instance.

![Power Scripts for Jira Cloud panel display settings](/cms_trial/assets/ca867fe8-8f8d-4786-b42b-48b749767f02.png)

### Panel location examples

The examples below show the same weather panel displayed in different locations on the issue page:

| **Left (main view)** | **Right (side view)** |
| --- | --- |
| Power Scripts for Jira Cloud SIL Runner gadget display | Power Scripts for Jira Cloud gadget configuration interface |

---

## How to manage your SIL issue panels

You can modify or remove a panel configuration at any time by clicking the **Edit** or **Delete** icons.

---

## More configuration guides