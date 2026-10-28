# Scenarios

## About the scenario mode

The Scenarios feature is available in the **Gantt** and **Resources modules**. You can create an unlimited number of private and public scenarios per box.

To find the optimal version of your plan, you have to consider multiple factors, such as risks and delays, and pay close attention to the availability and workload of your resources.

With the **Scenarios** feature, you can easily try out different variants of your plan, compare the results, and find the best one.

See the video to learn more.

### Synchronization

When you create a scenario, changes to your tasks will only be synchronized with Jira or connected tools, such as Trello, **after merging**. All changes made to tasks are stored in the Scenario history, and you can easily undo them.

### Undo

The Undo operation appears when you switch to the scenario mode.  
If you have two tabs open (in one tab, Resources is in the "Live" mode and, in another one, in the "Scenario" mode), the undo option is not available.

![image-20250303-104931.png](/cms_trial/assets/a1bcd2f5-d409-4d38-aef2-86e4ce7d80be.png)

## Plan work with scenarios

### Create a new scenario

1. Click the scenario drop-down at the top.
2. Select **Create new scenario**.

   ![Screenshot of creating a new scenario in the Gantt module.](/cms_trial/assets/a73c45be-4a9d-4e36-a62c-bad753220b21.png)
3. Complete:

   1. Scenario name
   2. Color
   3. Adjust scenario visibility (toggle switch private/public)

      ![Screenshot of completing the scenario details in the Gantt module.](/cms_trial/assets/6425bcd2-bf36-4aee-8ee0-73d577d55c2f.png)
4. Click **Create**.

### Edit scenario details

Click **Edit details** to change the scenario name, color, and public/private settings.

![Screenshot of editing scenario details in the Gantt module.](/cms_trial/assets/2a6c9a43-d92d-43b4-98c3-8be921fc4aad.png)

### Adjust visibility

**Method 1**

Go to **Edit details** and adjust the toggle switch (see above).

**Method 2**

Adjust directly in the scenario dropdown by clicking on the eye icon [eye icon]

### Delete a scenario

This action can't be reversed.

To delete a scenario:

1. Click the scenario drop-down at the top.
2. Click **Delete scenario**.

   ![Screenshot of deleting a scenario in the Gantt module.](/cms_trial/assets/f99b795b-d8d6-46b3-aff1-455ad5f9acdc.png)

### Switch between scenarios

Use the scenario drop-down at the top to switch between different scenarios and the live version.

**Note**:

Private scenarios are visible only to the person who created them. Make a scenario public to share it with other users.

### Scenario history

The scenario history lets you track changes. Click on the change counter at the top-right corner of the scenario box to see the list.

![Screenshot of the scenario history button in the Gantt module.](/cms_trial/assets/e0a9c188-1263-49ea-9ef6-0c945e2239d4.png)

For each change, the following information will be displayed in the history dialog:

- Order of changes
- Key and summary — issue key and summary of the changed task
- Reason
- Result type
- Live—the actual (live) period mode or period
- Scenario—period mode and period change

![Screenshot of the scenario history window in the Gantt module.](/cms_trial/assets/d4c09047-5a6f-4e37-8966-2176f4ca1119.png)

## Changes supported by the scenario mode

| **Change** | **Gantt module** | **Resources module** |
| --- | --- | --- |
| **Start date**  Updates made in Task details or drag and drop action on the timeline + resizing. | ✅ | ✅ |
| **End date**  Updates made in Task details or drag and drop on the timeline + resizing. | ✅ | ✅ |
| **Scheduling mode**  Updates made in task details pop-up. | ✅ | ✅ |
| **Original estimate, Remaining estimate, Story points**  Updates made in task details pop-up. | ❌ | ✅ |
| **Contouring mode, Workload contour**  Updates made in task details pop-up. | ❌ | ✅ |
| **Summary**  Updates made in task details pop-up. | ❌ | ✅ |

To compare scenarios, you open a new window of your browser and set to “Live”.

## Merge to live

This action can't be reversed.

Changes are synchronized with Jira or connected tools, such as Trello.

**Method 1**

Click **merge to live** at the top.

![Screenshot of the Merge to live button.](/cms_trial/assets/82161ad1-5b4d-4a73-a07b-d3a56510965c.png)

**Method 2**

Select **merge to live** from the scenario drop-down.

![Screenshot of the Merge to live option from the scenario drop-down in the Gantt module.](/cms_trial/assets/e3767743-a91e-4527-9347-77a3f2a14ed1.png)

**Method 3**

Click **Merge to live** in the **Scenario history** pop-up.

![Screenshot of the Merge to live button in the Scenario history window.](/cms_trial/assets/7e8e2aec-9dd4-4d58-a84d-3e1ecf4ba1c8.png)

## Affects

### Undo

If you have two tabs open (in one tab, Gantt is in the "Live" mode and, in another one, in the "Scenario" mode), the undo option is not available.

### Disabled options

When scenario mode is activated, some actions are disabled in a right-click menu, and a tooltip appears as below.

![Screenshot of disabled options when the scenario mode is in use in the Gantt module.](/cms_trial/assets/30f36c45-90a2-43f7-b886-514fdc64668d.png)

### Change history

Changes made in scenario mode are not logged until a scenario is merged into the live version.