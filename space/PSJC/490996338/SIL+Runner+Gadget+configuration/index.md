# SIL Runner Gadget configuration

Another useful feature of Power Scripts for Jira is the ability to run SIL scripts on demandusing the SIL Runner Gadget. This enables you to configure a list of scripts that can be run at any time directly from your dashboard.

## Add a gadget to a dashboard

1. To add a SIL Runner Gadget to a dashboard, click the **Add gadget** button on your dashboard. If you don’t see this button, you are not the owner of the dashboard and don’t have permission to edit it.

   ![Power Scripts for Jira Cloud gadget configuration form](/cms_trial/assets/27fe6a71-0f9c-4ba5-8ccd-1860fa082f69.png)
2. Click **Load all gadgets** to ensure all gadgets are loaded.

   ![Power Scripts for Jira Cloud gadget parameter settings](/cms_trial/assets/ce1df473-8699-4148-8da9-883e4da6efe9.png)
3. Under the *Other* category of gadgets, you will find the **SIL Scripts Gadget.**

   ![Power Scripts for Jira Cloud gadget display configuration](/cms_trial/assets/ca0b3c57-fd88-4ddf-9818-abe701c97f5e.png)
4. Click **Add gadget.**

## Configure the gadget

To configure the gadget:

1. Click the ellipse icon in the upper right corner of the gadget.
2. Click **Edit.**

   ![Power Scripts for Jira Cloud gadget execution settings](/cms_trial/assets/35c6a1c6-088e-431f-8016-b2fce1b6f5ea.png)

   The **configuration screen** is only available to Jira administrators and system administrators and enables them to manage the list of available SIL scripts. They can add, configure security, and delete scripts or edit the parameters of a runnable SIL script.
3. Click the pencil icon to edit a script from the list.
4. Follow the steps below for instructions on how to configure a script in the gadget.

## Add or configure a gadget script

1. From the configuration screen, click the **Add** button to add a new script.

   ![Power Scripts for Jira Cloud gadget button configuration](/cms_trial/assets/9210b5dd-435d-46fb-b22c-618697b49ed3.png)
2. To add a script to the runner, give it a name and description, and select a file containing the script.

   ![Power Scripts for Jira Cloud gadget interface display](/cms_trial/assets/674b9f37-9334-49dd-8f50-17f379b7a3af.png)
3. Optionally, a custom parameters form can be created to generate a form for the script to use as input.

   ![Power Scripts for Jira Cloud scheduler interface](/cms_trial/assets/4829c344-6eb6-4aa0-84b3-7bdc6509a6d6.png)

[See more](/cms_trial/space/PSJC/435028593/Parameter+Functions/) about creating forms for the gadget.

## Add script permissions

You can also select a security option in the Gadget to restrict script usage to specific users or groups. To add a permission, click the **People** icon from the gadget configuration screen.

- **Public**: The script will be available to any user.
- **Group**: The script will be available only if the currently logged-in user is a member of the specified group (use a group picker to select a group).
- **User**: The script will be available only if the currently logged-in user is the same as the specified one (user picker is used).
- **Project role**: The script will be available only if the currently logged-in user is in a specific role on a specific project (project picker is used).

![Power Scripts for Jira Cloud scheduler configuration panel](/cms_trial/assets/1ac004a0-3f66-4431-9ffc-167e86a0f30d.png)

To edit the actual scripts, use the [SIL Manager](/cms_trial/space/PSJC/490996983/SIL+Manager/).

## More configuration guides