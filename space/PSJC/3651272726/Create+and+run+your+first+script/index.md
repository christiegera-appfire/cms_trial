# Create and run your first script

Create your first Simple Issue Language (SIL) script and use it to change the due date of a Jira work item to five days from today. You'll learn the basic process for creating, checking, and running scripts in SIL Manager and see the result directly in Jira.

**Estimated time:** 5 minutes

## Before you begin

Make sure you have:

- Power Scripts for Jira Cloud installed.
- A Jira work item that you can use to test the script. Note the work item key; you’ll need it when configuring the Default Script Context.

## Create your first script

1. Go to **Settings** (⚙️) > **Marketplace Apps** > **Power Scripts** > **SIL Manager**.
2. In the **Files** panel, select the `silprograms` directory.

   ![PS-files-panel.png](/cms_trial/assets/9e2589cd-b4f1-44f7-8860-0a89e0ff0701.png)
3. Click **File** > **New file**, or right-click the directory and select **New** > **File**. Create a SIL file named `duedate.sil`.
4. In the editor, enter:

   `dueDate = currentDate() + "5d";`
5. Click the **Save** icon.

The `dueDate` standard variable represents the Due date field of the Jira work item. The `currentDate()` function returns the current date, and the `+` `"5d"` adds five days to the current date. You can find standard variables, functions, and other SIL syntax in [Simple Issue Language](/cms_trial/space/PSJC/434798967/Simple+Issue+Language/).

![PS-sil-example.png](/cms_trial/assets/6187d12a-616d-4285-bb14-56f87400cf63.png)

## Set the script context

Before you run the script, set the script context. This script changes the `dueDate` of a work item, so Power Scripts needs to know which one you want to change.

1. In SIL Manager, open the **Run** menu and select **Default Script Context**.
2. In the **Select context** field, enter the work item key for the Jira work item you want to use, for example, `TEST-1`.
3. Click **OK**.

The selected work item is now associated with your script. When you run the script, references such as `dueDate` apply to that work item.

![PS-default-script-context.png](/cms_trial/assets/d275991d-f0af-4d0b-a37a-31dc9476ee4d.png)

## Check and run the script

Now that you've selected the work item the script will run against, check the script for errors before running it.

1. Click the **Check** icon.
2. Review the results and confirm that the script does not contain errors.
3. Click the **Run** icon.
4. Review the execution results and confirm that the script ran successfully.

![PS-sil-script.png](/cms_trial/assets/54ad5b05-c36d-4fa7-8c8e-0b7019dd7c7f.png)

## Verify the result

1. Open the Jira work item you selected as the script context.
2. Find the **Due date** field.
3. Confirm that the due date is five days from the current date.

You have now created a SIL script, run it against a Jira work item, and used it to update Jira data.

## Watch the video

Watch the video below to see the complete process in less than 5 minutes.

## Next steps

Now that you know how to create and run a SIL script, you can use scripts to automate Jira tasks.

- Learn more about the Simple Issue Language: [Simple Issue Language](/cms_trial/space/PSJC/434798967/Simple+Issue+Language/)
- Run a script when something happens in Jira: [Automate an action with a listener](/cms_trial/space/PSJC/3650682902/Automate+an+action+with+a+listener/)
- Extend Jira searches using JQL keywords: [Extend Jira searches with JQL](/cms_trial/space/PSJC/3651731477/Extend+Jira+searches+with+JQL/)