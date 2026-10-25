# Timeline mode

## Timeline mode (old navigation)

Click to expand the guide

## About the Timeline view mode

The structure of boxes in the Timeline mode is visualized in a [column view](/cms_trial/space/SPM/1918700155/Column+view+(Overview+module)/), which shows a hierarchy of boxes and their [attributes](/cms_trial/space/SPM/1918404836/Box+attributes/) (the section on the left is similar to the Hierarchy view mode).

Additionally, the boxes are represented as bars and scheduled on the timeline (the section on the right is similar to the Gantt chart). The sub-boxes are in a top-down scheduling mode, meaning they cannot exceed their parent's period.

![Timeline mode, Overview module.](/cms_trial/assets/2091475c-18f8-4286-b1b1-26073ae96074.png)

## Actions in the Timeline mode

You can carry out the following actions while in the Timeline mode in the Overview module:

### Change box hierarchy

The hierarchy of boxes visualized in the Timeline mode reflects the relationships between the parent boxes and child boxes (sub-boxes). Those relationships are represented as nestings that are governed by the [parent type](/cms_trial/space/SPM/1918832188/Box+type+attributes/) boxes.

You can rearrange the box hierarchy by manually moving (dragging) the boxes from one place to another (section on the left). This can be especially helpful when you want to quickly organize stand-alone projects into programs and portfolios.

[**Read more**](/cms_trial/space/SPM/1918535907/Box+hierarchy/)

### Manage box lifecycle (context menu)

Jira/App/Box Admins can change the status of the box and [archive](/cms_trial/space/SPM/1918634657/Archive+box/) it. This can be done by:

- **right-clicking** the box swimlane (anywhere but the box name link) (both sections)
- **right-clicking** the box bar on the timeline (right section)

<https://app.arcade.software/share/coip3EMuEu0X2Jt44TWm>

[**Read more**](/cms_trial/space/SPM/1918829911/Box+lifecycle/)

### Manage boxes (context menu)

Jira/App/Box Admins can use the same context menu to:

- configure a box
- edit a box
- archive a box
- delete a box

In addition, they can click the **Add new** (**+**) in the upper menu to [create a new box](/cms_trial/space/SPM/1918406376/Create+box/).

[**Read more**](/cms_trial/space/SPM/1918699321/Box+management/)

### Reschedule boxes (context menu and timeline)

The bars representing boxes can be:

- stretched to change their period (duration)
- moved to change their start and end dates

Alternatively, **right-click** a box (on a timeline or in the box hierarchy) to prompt the context menu. From the menu, select **Edit**.

**Limitations:**

- You can’t change the start/end date of closed and [archived boxes](/cms_trial/space/SPM/1918405770/Archived+boxes/).
- When the box type settings enforce [sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/), box periods can’t overlap.
- When the box period is based on the period of tasks, the box start/end date can’t be manually adjusted.

[**Read more**](/cms_trial/space/SPM/1918635162/Edit+box+details+(name%2C+start%2Fend+dates)/)

### Mark a box as favorite

Open the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/) and click the **star icon** next to the box name to mark it as a favorite. It will help you find the marked box easily later. The list of favorite boxes is local and not shared among other users.

### Filter the box hierarchy

Use the search and filter functionalities to narrow down the scope of visible boxes.

- When the parent boxes do not fit the applied filter or search criteria, they are faded (only on the box hierarchy side).

![Timeline mode, overview module with the search applied.](/cms_trial/assets/0d33e848-227a-496f-aa7e-87deddd866fe.png)

- If it is the child boxes that do not fit the filter or search criteria, the children will not be displayed (only on the box hierarchy side).

![Timeline mode, overview module with the search applied.](/cms_trial/assets/959229d2-8efa-4563-883b-6eb3d1665818.png)

[**Read more**](/cms_trial/space/SPM/1918505078/Favorite+%2F+Filter+by+(Overview+module)/)

### Adjust the view

Under the **View** options, you can adjust the layout of the column view and box bars:

- *Grid lines*

  - **Vertical** - depending on the scale, this option marks days, weeks, months, and years.
  - **Horizontal**
- *Hierarchy Lines*

  - **Vertical**
  - **Horizontal**
- *Label Position*

  - Hidden
  - On the taskbar
  - Next to the taskbar
- *Layout*

  - **Compact**
  - **Regular**
  - **Wide**
- *Show*

  - **Period warnings** (when enabled, the discrepancy in the period between child and parent boxes is indicated in yellow on the timeline)
  - **Show archived boxes**

### Navigate and fine-tune the timeline

#### Enable the minimap

Navigate through all your boxes using the mini-map. Click the map to adjust the main timeline.

![Screenshot shows the timeline view of the Overview module. The arrow points toward the mini map icon at bottom right. ](/cms_trial/assets/65e1287d-1ae7-4bf8-a91b-2fafd0fe02bc.png)

#### Change the granularity level and add details

The timeline navigation buttons let you adjust the timeline granularity level. Alternatively, you can use the keyboard shortcuts:

- Today
- Zoom out (**Shift** + **-**)
- Zoom in (**Shift** + **=**)
- Scale to fit (**f**) (when no tasks are selected, the app zooms out to show all your boxes. The timeline start/end date encompasses all boxes. When a task is selected, the timeline zoom level is adjusted so that the task fills the screen).
- Show on timeline: [Markers](/cms_trial/space/SPM/1918699490/Markers/) (enable the markers to remember important events throughout the box execution).
- [Week numbers](/cms_trial/space/SPM/1918801444/Week+numbers+(Gantt+chart)/) (**w**) (option availability and visibility on the timeline depend on the zoom level)

The current date is always marked with a marker, even if you have **Markers** unchecked.

![Overview timeline buttons, zoom in, zoom out, today, scale to fit, more actions.](/cms_trial/assets/0e68f024-52b1-458b-95ab-67f3f0761acb.png)

## Timeline mode (new navigation)

Click to expand the guide

## About the Timeline view mode

The structure of boxes in the Timeline mode is visualized in a [column view](/cms_trial/space/SPM/1918700155/Column+view+(Overview+module)/), which shows a hierarchy of boxes and their [attributes](/cms_trial/space/SPM/1918404836/Box+attributes/) (the section on the left is similar to the Hierarchy view mode).

Additionally, the boxes are represented as bars and scheduled on the timeline (the section on the right is similar to the Gantt chart). The sub-boxes are in a top-down scheduling mode, meaning they cannot exceed their parent's period.

![Screenshot of the Timeline mode in the Overview module.](/cms_trial/assets/21509c3b-3948-425b-bdae-552a4f2c76ae.png)

## Actions in the Timeline mode

You can carry out the following actions while in the Timeline mode in the Overview module:

### Change box hierarchy

The hierarchy of boxes visualized in Timeline mode reflects the relationships between parent and child boxes (sub-boxes). Those relationships are represented as nestings that are governed by the [parent type](/cms_trial/space/SPM/1918832188/Box+type+attributes/) boxes.

You can rearrange the box hierarchy by manually moving (dragging) the boxes from one place to another (section on the left). This can be especially helpful when you want to quickly organize stand-alone projects into programs and portfolios.

[**Read more**](/cms_trial/space/SPM/1918535907/Box+hierarchy/)

### Manage box lifecycle (context menu)

Jira/App/Box Admins can change the status of the box and [archive](/cms_trial/space/SPM/1918634657/Archive+box/) it. This can be done by:

- **Right-clicking** the box swimlane (anywhere but the box name link) (both sections).
- **Right-clicking** the box bar on the timeline (right section).

[**Read more**](/cms_trial/space/SPM/1918829911/Box+lifecycle/)

<https://app.arcade.software/share/NKL9xsVWXm7HQy3tVGoR>

### Manage boxes (context menu)

Jira/App/Box Admins can use the same context menu to:

- Configure a box
- Edit a box
- Archive a box
- Delete a box

In addition, they can click the **Create new** button to [create a new box](/cms_trial/space/SPM/1918406376/Create+box/).

[**Read more**](/cms_trial/space/SPM/1918699321/Box+management/)

### Reschedule boxes (context menu and timeline)

The bars representing boxes can be:

- Stretched to change their period (duration).
- Moved to change their start and end dates.

Alternatively, **right-click** a box (on a timeline or in the box hierarchy) to prompt the context menu. From the menu, select **Edit**.

<https://app.arcade.software/share/65oJy89XFV3RrRZLMoe5>

**Limitations:**

- You can’t change the start/end date of closed and [archived boxes](/cms_trial/space/SPM/1918405770/Archived+boxes/).
- When the box type settings enforce [sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/), box periods can’t overlap.
- When the box period is based on the period of tasks, the box start/end date can’t be manually adjusted.

[**Read more**](/cms_trial/space/SPM/1918635162/Edit+box+details+(name%2C+start%2Fend+dates)/)

### Mark a box as favorite

Open the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/) and click the **star icon** next to the box name to mark it as a favorite. It will help you find the marked box easily later. The list of favorite boxes is local and not shared among other users.

![Screenshot of marking a box as favorite in the Overview module.](/cms_trial/assets/8d0d8adf-3600-43a3-beb9-c56ae1b654d2.png)

### Filter the box hierarchy

Use the search and filter features to narrow the visible boxes.

- When the parent boxes do not fit the applied filter or search criteria, they are faded (only on the box hierarchy side).

  ![Screenshot of using the search box in the Overview module.](/cms_trial/assets/2c9b72b7-57e4-42ab-b2f2-beaa9e28b692.png)
- If it is the child boxes that do not fit the filter or search criteria, the children will not be displayed (only on the box hierarchy side).

  ![Screenshot of searching by a box name in the Overview module.](/cms_trial/assets/f1beab3f-3ed4-418d-8511-08cbd11aa075.png)

[**Read more**](/cms_trial/space/SPM/1918505078/Favorite+%2F+Filter+by+(Overview+module)/)

### Adjust the view

Under **View** > **Layout**, you can adjust the layout of the column view and box bars:

- *Grid lines*

  - **Vertical** - depending on the scale, this option marks days, weeks, months, and years.
  - **Horizontal**
- *Hierarchy Lines*

  - **Vertical**
  - **Horizontal**
- *Label Position*

  - Hidden
  - On the taskbar
  - Next to the taskbar
- *Layout*

  - **Compact**
  - **Regular**
  - **Wide**
- *Show*

  - **Period warnings** (when enabled, the discrepancy in the period between child and parent boxes is indicated in yellow on the timeline)
  - **Show archived boxes**

![Screenshot of the Layout options in the Overview module.](/cms_trial/assets/dc7f7e11-53a0-480c-804a-e32c5f6226eb.png)

### Navigate and fine-tune the timeline

#### Enable the minimap

Navigate through all your boxes using the mini-map. Click the map to adjust the main timeline.

![Screenshot of the minimap in the Overview module.](/cms_trial/assets/27c21b6b-a64d-4289-ad89-fd8ad7a1731c.png)

#### Change the granularity level and add details

The timeline navigation buttons let you adjust the timeline granularity level. Alternatively, you can use the keyboard shortcuts:

- Today
- Zoom out (**Shift** + **-**)
- Zoom in (**Shift** + **=**)
- Scale to fit (**f**) (when no tasks are selected, the app zooms out to show all your boxes. The timeline's start/end dates encompass all boxes. When a task is selected, the timeline zoom level is adjusted so that the task fills the screen.
- Show on timeline: [Markers](/cms_trial/space/SPM/1918699490/Markers/) (enable the markers to remember important events throughout the box execution).
- [Week numbers](/cms_trial/space/SPM/1918801444/Week+numbers+(Gantt+chart)/) (**w**) (option availability and visibility on the timeline depend on the zoom level)

The current date is always marked with a marker, even if you have **Markers** unchecked.

![Screenshot of the Show on timeline options in the Overview module.](/cms_trial/assets/4979cd2a-d503-4b1e-8e13-3e8591f08da1.png)