# Automate an action with a listener

SIL listeners run scripts automatically when specific Jira events occur. Create a listener that checks the description when a work item is created and adds a comment if it's too short.

**Estimated time:** 10 minutes

## Before you begin

Make sure you have:

- Power Scripts for Jira Cloud installed.
- A Jira project where you can create a test work item.

## Create the listener script

1. Open **SIL Manager**. Go to **Settings** (⚙️) > **Marketplace Apps** > **Power Scripts** > **SIL Manager**.
2. In the **Files** panel, select the `silprograms` folder. You can also click **File** > **New folder**, or right-click the directory and select **New** > **Folder** and create a folder for your script named `Listeners`.

   ![PS-files-panel.png](/cms_trial/assets/7f558143-da34-43e9-92f4-4490b3d2c5c9.png)
3. Select the `Listeners` folder, then click **File > New file**, or right-click the folder and select **New > File**. Name the file `short_description_listener.sil`.
4. Add the following script:

```text
if(length(description) < 50) {
    addComment(
        key,
        currentUser(),
        "Please add more information to the description. Include any helpful context, requirements, examples, or files so the team can understand the work."
    );
}
```

1. Click the **Check** icon. Review the results and confirm the script has no errors.
2. Click the **Save** icon.

The script checks the work item description. If it has fewer than 50 characters, Power Scripts adds a comment to the work item asking for more information.

## Create the listener

The script does not run automatically until you configure a listener and connect it to a Jira event.

1. Go to **Power Scripts** > **Configurations** > **Automations** > **Listeners**.
2. Click **Add listener**. The **Add New Listener** dialog opens.
3. From **Choose the script**, click the **Select** icon, locate the script you just created, and click **Select**.
4. Select **Issue Created** as the event. You can type the event name in the **Select events** field instead of scrolling through the list. When the event occurs, in this case, when a work item is created, the listener runs the script.
5. If needed, limit the listener to the project or work item type you want to use for testing.
6. Click **Add** to save the listener.

![PS-add-listener.png](/cms_trial/assets/a0858717-0d1a-43aa-9972-20fe908b9d61.png)

The listener is now configured to run your script whenever a work item is created that matches the script's conditions.

## Test the listener

1. Create a new Jira work item in the specified project. Since you selected **Issue Created** as the event, the listener only runs for new work items. Existing work items are not included.
2. Enter a description that contains fewer than 50 characters.
3. Click **Create**.

## Verify the result

Open the work item and check the comments.

If the description is less than 50 characters, Power Scripts adds the comment from your listener script.

You have now created a listener that responds automatically to a Jira event and runs a SIL script.

## Next steps

- Learn more about [SIL Listeners](/cms_trial/space/PSJC/490997990/SIL+Listeners/)