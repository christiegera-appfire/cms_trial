# Create box in the Overview module

## Create a box in the Overview module (old navigation)

Click to expand the guide

In this article, you will learn how to add, edit, and delete Boxes using the Overview module, including adding new boxes under the Home (root) Box.

Boxes can be organized into a hierarchical structure, and their periods follow the [scheduling](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) rules.

![overview-panel.png](/cms_trial/assets/e62b6a93-f5c1-4720-ac65-8edb1ff5a364.png)

Keep in mind:

- A box type contains the default settings and rules applicable to multiple boxes (all boxes of a given type). Box type settings are adjusted in Box type administration.
- Box configuration refers to the settings of a single, individual Box. They are dependent on the Box type settings.

## Security and configuration

- You need a box admin or sub-box creator security role to create, edit, and delete boxes.
- To configure a box type information and parent types, go to **App Administration** > **Box types** > select a box type > **Basics**.
- To configure box type scheduling rules (period mode and sequentiality), go to **App Administration** > **Box types** > select a box type > **Advanced**.

## Create a box

When you create a box, you automatically become its admin (Box Admin).

The video presents how to create a box in BigPicture.

To create a new box:

1. Click the **+Add new** button.
2. Choose a **box type** and complete a **box name**.
3. Start and end dates are automatically set to today. You can edit start/end dates now or later.
4. Choose one or more Jira projects to populate the scope of a box.
5. Adjust the icon and its color for a box.
6. Click **Create**.

![Overview module, adding a new box.](/cms_trial/assets/4fa26df7-d9eb-41cc-9a3b-4ac95f66c327.png)

Alternatively, you can click in-between the items on the list:

![Overview module, plus icon between boxes.](/cms_trial/assets/169f738a-5bc5-4ba4-95f9-9dd237efe98f.png)

Next, select a box type you want to use.

The list of available box types might vary depending on where you are in the app—Home view or the Overview module of a box and where you click when adding new boxes. Make sure to define the "Parent type" correctly in the App's administration > box types (click on the box type name to edit) > General > Basics > Parent types (requires App admin security role).

![Box types choosing when adding a box.](/cms_trial/assets/14a2a3a6-ea16-401f-81e1-7ce041a74601.png)

If needed, edit the fields:

| **Field** | **Description** |
| --- | --- |
| **Box type** | Select a box type from the list. |
| **Box name** | Specify the box name. |
| **Start/end date** | Start and end dates are automatically set to today. Click to change start/end dates. Box adding panel. |
| **Icon** | Select the icon from the dropdown. Choosing an icon during box creation. |
| **Color** | Select the icon color. Choosing an icon during box creation. |
| **Projects** | **Optional field**  You can select Jira projects that will be in the scope of the new box.  Advanced [scope definition](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) options are available after the box has been created. You can base the scope on Jira boards and filters and narrow it down. Choosing a project during box creation. |

If the button is greyed out and you see the message "There are no box types available for this level":

- Same-level boxes can't be created
- Sub-boxes can't be created

![Greyed-out plus icon.](/cms_trial/assets/6e48a95a-884b-4bfa-8907-4a4b521027bc.png)

Firstly, check the "Type" of the box you are presently in.

![Program Increment in the Type column.](/cms_trial/assets/ff637e13-5880-4465-8020-c9f03cf676f7.png)

Go to "Administration" to verify box type settings. Make sure that "parent types" have been set as needed.

### Create a box based on timebox schedule

![add-timebox-schedule.png](/cms_trial/assets/3cad2a42-f38a-4def-95ee-59c1dae5f580.png)

You can create a box based on an existing timebox schedule in the Overview module:

To add a box based on timebox schedule, click the **Add New** icon and switch on the Use timebox schedule toggle. When you do it, two new options are displayed in the window:

- Preview details of the Timebox Schedule: check the list of the timebox schedule. Click one of the timebox schedules, to check its details. An App Admin can also edit timebox schedule details from this level:

  ![timebox-schedule-previw.png](/cms_trial/assets/c7d2f97c-4e6f-4ba5-b19f-b6cb1f3d9dbc.png)

  Click Select
- Select timebox schedule - choose a timebox schedule from the drop-down list and click **Create**.

Timeboxes from timebox schedule are available in the Overview module in the list and in the box switcher. In the list they can be edited by App Admin - they are greyed out for different kind of users.

For more information, check the [Timebox schedules](/cms_trial/space/SPM/1989214530/Timebox+schedules/) page.

### Create same-level and sub-boxes

The App can suggest the Start / End dates when your boxes are sequential. When overlapping is enabled, no end date will be indicated.

Go to App Administration > box types > General to change the sequentiality settings.

Click the "box type" button or use the indent/outdent arrow next to the button in the box creation dialog to switch between same-level and sub-boxes. It appears when you want to add a box by clicking in-between the items, and the box type in the row above is a parent type to other box types.

Select from the list of available box types or click the "outdent arrow' to include the same-level box types and the "indent arrow" to narrow the list to sub-box types.

![Choosing the Box Type during adding box.](/cms_trial/assets/b1108fdc-7170-43a6-854d-3b427dedef88.png)

When you click the indentation arrow, it will reverse, and the available box types are narrowed to same-level boxes only, that is, Iteration, as the Iteration box type is not a parent type to any other box types:

![Clicking the indentation arrow during bo creation.](/cms_trial/assets/8f8ec7b3-38c6-4a27-85f1-28f0c9dd652f.png)

### Next timebox naming scheme

When creating a consecutive "Sub scope" box, the App suggests a name.

The last number in the string (the name of the previous box) is incremented by 1, even if it isn't the last character in a string.

If no numbers are present, "2" is added to the end of the name string.

![Panel of adding a box.](/cms_trial/assets/0e50a3fa-fca4-437c-8212-8362b7b4e9dc.png)

## Create a box in the Overview module (new navigation)

Click to expand the guide

Learn how to add, edit, and delete boxes using the Overview module. This guide also covers adding new boxes under the Main box.

Remember:

- A box type contains the default settings and rules applicable to multiple boxes (all boxes of a given type). Box type settings are adjusted in the app Administration.
- Box configuration refers to the settings of an individual box and depends on the box type settings.

## Access and security

- You need a Box Admin or Sub-box Creator security role to create, edit, and delete boxes.
- To configure a box type information and parent types, go to **App Administration** > **Box types** > select a box type > **Basics**.
- To configure box type scheduling rules (period mode and sequentiality), go to **App Administration** > **Box types** > select a box type > **Advanced**.

When you create a box, you automatically become its admin (Box Admin).

## Create a box

To create a new box:

1. Go to the **Main box** > **Overview module**.
2. Click the **Create new** button.
3. Modal displays. On the modal, under the **Type**, select a box type (e.g., Agile).
4. In the **Name** field, enter the name of your box. You can leave the default name and edit it later.
5. Start and end dates are automatically set to the current date. You can edit them now or later.
6. Optionally, change the icon and the icon background color to improve identification within the box hierarchy.
7. Click **Create**.

![Overview module, adding a new box.](/cms_trial/assets/1761f350-3981-4b1f-9ba0-334a3f46f5f8.png)

Alternatively, you can mouse over the border between rows in the box hierarchy to display the **plus** icon. Click it to open a modal.

![Overview module, a plus icon on the task tree.](/cms_trial/assets/482d8d33-1821-4fa2-854e-de4fae54457b.png)

The list of available box types may vary depending on where you are in the app; you will see a different list of box types when using the **Create new** button in the Main box compared to when you click the plus sign under a specific box in the box hierarchy.

![List of box types on the box creation modal.](/cms_trial/assets/14a2a3a6-ea16-401f-81e1-7ce041a74601.png)

Make sure to define the **Parent type** correctly in the **Administration** > **Box types** > open a box type > **General** > **Basics** > **Parent types** (this configuration requires App Admin security role).

The box creation modal consists of the following fields:

| **Field** | **Description** |
| --- | --- |
| **Box type** | Select a box type from the list. |
| **Box name** | Enter a name for your box. |
| **Start/end date** | Start and end dates are automatically set to today. Click to change start/end dates. Box adding panel. |
| **Icon** | Select the icon from the dropdown. Choosing an icon during box creation. |
| **Color** | Select the icon background color. Choosing an icon during box creation. |
| **Jira spaces** | (Optional field and available only for the boxes with the **Own** scope)  You can select a Jira space or spaces to populate your box with the work items from that space/spaces.  Advanced [scope definition](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) options are available after the box is created. You can narrow down the scope of tasks you want to add using Jira boards and filters (**box configuration** > **Tasks** > **Work items from Jira**). Choosing a Jira space during box creation. |

If the **Create new** button is greyed out, it means that:

- Same-level boxes cannot be created
- Sub-boxes cannot be created

![Greyed-out Create new button.](/cms_trial/assets/33f2f393-1769-4f9c-b0d0-d2328359e2f0.png)

Check the type of the current box (e.g., using the **Type** column).

Then, go to **Administration** > **Box types** to verify the box type settings for your current box. Make sure that the **Parent types** are set as needed.

### Create a box based on a timebox schedule

You can create a box based on an existing timebox schedule in the Overview module:

To add a box based on a timebox schedule:

1. Click the **Create new** button.
2. On the modal, enable the **Use timebox schedule** toggle. When you do it, two additional options display:

![New box creation modal with the Use timebox schedule option enabled.](/cms_trial/assets/e059d312-4cbf-4318-b550-c6c5b8c95d51.png)

- **Preview details of the Timebox Schedules**: this option opens a modal where you can view the list of timebox schedules. Click one of the timebox schedules to preview the schedule structure and field mapping. Click **Select this timebox schedule** if you want to select the TS directly on the modal.

  ![timebox-schedule-previw.png](/cms_trial/assets/c7d2f97c-4e6f-4ba5-b19f-b6cb1f3d9dbc.png)
- Otherwise, under the **Select timebox schedule**, open a list of available timebox schedules and then select one.

1. Click **Create**.

Timeboxes from the timebox schedule are available in the Overview module in the list and on the box switcher. Only the App Admin can edit that list.

<https://app.arcade.software/share/DzhVgYdnKX0uxMRW3JiR>

For more information, check the [Timebox schedules](/cms_trial/space/SPM/1989214530/Timebox+schedules/) page.

### Create same-level and sub-boxes

The app can suggest the start/end dates when your boxes are **Sequential**. When the **Overlapping** is enabled, it will not suggest any date.

Go to **Administration** > **Box types** > select a box type > **General** and change the sequentiality settings.

1. Mouse over the border between the boxes in the box hierarchy.
2. A **plus** icon appears. Click it to open the box creation modal.
3. On the modal, select the box **Type**.
4. If you cannot see the type you want to add, use the indent/outdent arrow next to the modal to switch between the same-level and sub-boxes. The arrow appears when the box type in the row above is a parent type to other box types.
5. Select from the list of available box types or click the **outdent arrow** to include the same-level box types; use the **indent arrow** to narrow the list to sub-box types.

When you click the indentation arrow, it will reverse, and the available box types are narrowed to same-level boxes only, that is, Iteration, as the Iteration box type is not a parent type to any other box types:

![A video demonstrating how to switch between the same-level and sub-boxes using the indent and outdent arrows on the box creation modal.](/cms_trial/assets/b5243428-3db3-4563-aad3-00315e41d0e9.mp4)

### Next timebox naming scheme

When creating a consecutive **Sub scope** box, the app suggests a name.

The last number in the string (the name of the previous box) is incremented by 1, even if it isn't the last character in a string.

If no numbers are present, 2 is added to the end of the name string.

![Create a new box modal.](/cms_trial/assets/0e50a3fa-fca4-437c-8212-8362b7b4e9dc.png)