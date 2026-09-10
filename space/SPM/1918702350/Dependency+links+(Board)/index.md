# Dependency links (Board)

## Introduction

With the **Board** module, you can display both **strong** and **soft links**. The dependencies have additional color coding.

## Configuration

Dependencies can synchronize with Jira links in the [App's configuration](/cms_trial/space/SPM/1918698881/App+configuration/), which requires Jira admin permissions.

![image-20240925-083110.png](/cms_trial/assets/e5ecc421-a85c-4b81-97f1-8358b78eb5d3.png)

## Display dependencies

### Collapse dependencies

Task cards have a dependency counter. Dependency arrows are hidden.

![image-20240925-083357.png](/cms_trial/assets/532527d8-e6b9-41a4-ae9f-8e7bf1621fdd.png)

#### Default settings

Dependencies are collapsed by default for all users.

### Expand dependencies

Dependencies are visualized in the form of arrows connecting task cards. When you select **Expand dependencies**, you can also decide what dependencies will be visible on the board:

- Incorrect dependencies (red) - target tasks are planned in previous timeboxes.
- Dependencies at risk (orange) - target tasks are planned in the same timeboxes.
- Correct dependencies (green) - target tasks are planned in next timeboxes.

![image-20240925-084448.png](/cms_trial/assets/6a465ec4-7c7b-4404-996d-7d187d78afaa.png)

#### Browse dependencies

Click **Browse dependencies** to open dependencies in the Infobar panel.

![image-20240925-085157.png](/cms_trial/assets/36ab0aaa-6fc4-4390-b7ca-87a4d1065bcb.png)

**Soft dependencies → solid line:**

![image-20240925-085342.png](/cms_trial/assets/70db6a18-13cb-44a8-84df-506de27b65fe.png)

**Strong dependencies → dotted line:**

![image-20240925-085513.png](/cms_trial/assets/d89ef422-5195-43a8-828d-f9b808030b8d.png)

## Highlight task dependencies and related tasks

Click a task card:

- Linked task cards are highlighted (dotted line around the card border); unrelated links are greyed out.
- Arrows connecting task cards are visible (works in both the collapsed and expanded view).

![contentId-1918702350](/cms_trial/assets/efe5fe2e-1411-468b-96a7-52d73f5edfb9.png)

## Dependency counter

The dependency counter is always visible on a task card.

![image-20240925-085829.png](/cms_trial/assets/e46bb778-43d0-4370-bcc8-89d5205a7b68.png)

## Color coding

### Health status of dependencies

Dependency counters with numbers symbolize the "health status" of the task dependencies by colors.

Dependency counter coloring corresponds to the arrow colors.

![image-20240925-090555.png](/cms_trial/assets/badb256c-847f-4882-8584-3f031c76cb1a.png)

| **Color** | **Description** |
| --- | --- |
| Red | Target tasks are planned in previous timeboxes. |
| Orange | Target tasks are planned in the same timeboxes. |
| Green | Target tasks are planned in next timeboxes. |
| Purple | Target tasks are out of view. |

## Dependency list

To see the list of task dependencies, click on the **dependency counter:**

![image-20240925-090839.png](/cms_trial/assets/c336bd84-9c03-46a6-b905-686e025787c0.png)

| **Element** | **Description** |
| --- | --- |
| Dependency details | Hover the mouse to see the dependency type. contentId-1918702350 |
| Summary | Summary of a task that is on the other end of the dependency. Click on the summary to view a task in Jira.  [Unmapped macro: inline-media-image — no content to fall back on] |
| Edit | The "Edit" button appears when you hover the mouse over the dependency. Click on the icon to see the dependency details modal box. contentId-1918702350 |
| Snipe to task | Locate the task on the other end of the dependency.   [Unmapped macro: inline-media-image — no content to fall back on]  When you **snipe to task** both cards are selected (blue border around the card). contentId-1918702350 **Note**:  This doesn't apply to out-of-view tasks:   - Filtered out (task not visible because of active filters - this includes tasks that are hidden due to being planned on a lower level) - Out of Box (tasks outside of current context Box)   Out-of-view tasks are displayed in the infobar. |

## Show/hide tasks without dependencies

You can filter the view to:

- See all tasks (button not pressed - light grey background, dark icon).
- See only tasks that have dependencies (button pressed - dark grey background, light icon).

![contentId-1918702350](/cms_trial/assets/601fbce0-6003-4eb3-a4ac-3e4be8897663.png)

## Create dependencies

You can create new dependencies on both, the **Collapse**and **Expand dependencies** display modes.

### Drag-and-drop an arrow

You can create a dependency using **drag and drop**. Hover over the card, and a grey dot will appear on the right side. Drop the link on one of the other cards to create a dependency:

![contentId-1918702350](/cms_trial/assets/c4bab649-8386-489a-b925-282e61b4d265.png)

There is no limit on the mechanism - regardless of how many dependencies exist you can create new dependencies by drag-and-dropping an arrow

### Card grey dot click

Alternatively, **click on the grey dot**, and a link creation pop-up will appear. This way is much more convenient when working with numerous cards, but you need to know the Issue key of the task you want to link. Using the pop-up, you can also select the dependency type:

![contentId-1918702350](/cms_trial/assets/6648f754-862b-426b-b6ff-7a56101dc2a6.png)

## Manage existing dependencies

### Click the arrow

Click on a dependency arrow to see the pop-up.

#### Soft Dependencies

You can:

- Change the target task
- Change the dependency type
- Add a description
- Delete a dependency

![contentId-1918702350](/cms_trial/assets/5257ef99-10bf-4153-addc-499c328d080f.png)

#### Strong Dependencies

You can:

- Change the target task
- Change the dependency type
- Modify [lag time](/cms_trial/space/SPM/1918406747/Lag+time/)
- Turn on/off [the ASAP mode](/cms_trial/space/SPM/1918764948/ASAP+mode/)
- Add a description
- Delete a dependency

![contentId-1918702350](/cms_trial/assets/0085f0bd-8efe-4b0a-9a6a-7e4fac594843.png)

### Click the dependency counter

Use the **edit**button to manage existing dependencies.

![contentId-1918702350](/cms_trial/assets/365f4f48-fef6-4e3b-9f76-a9e573c6da48.png)