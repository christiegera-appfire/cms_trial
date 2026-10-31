# Edit box details (name, start/end dates)

## Edit box details (old navigation)

Click to expand the guide

The box **Edit** option lets you change the following box details:

- name
- start date
- end date

Each detail field is required—you will not be able to **Save** your changes if the box name or start/end dates are empty.

![Edit box details screen.](/cms_trial/assets/742d8bd1-c077-4f32-b8d4-ed297bdaa88d.png)

## Permissions

The box edit action requires one of the following [security roles](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918633268):

- Jira Admin
- App Admin
- Box Admin
- Box Editor

## Edit box details in the Overview module

### Edit option on the context menu

In the [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/), you can edit a box in all three [view modes](/cms_trial/space/SPM/1918831037/Navigation+and+interface+(Overview+module)/) (Hierarchy, Timeline, and Kanban board) using the options menu. This box edit method applies to Home, [portfolio](/cms_trial/space/SPM/1918504271/Portfolio+boxes/), program, and project boxes.

The interactive presentation below walks you through the box editing in all Overview view modes.

<https://demo.arcade.software/08I1ec1966xIjvuZocpI>

#### Overview module: [Hierarchy mode](/cms_trial/space/SPM/1918799130/Hierarchy+mode/)

1. Go to the **Overview module** and open the **Home box**.
2. **Right-click** the box (anywhere within its swimlane but the name link).

- Alternatively: Click **More actions** (**…**) next to the box you want to edit.

1. Select **Edit** from the dropdown.

![Prompting options menu in the Overview module, hierarchy mode.](/cms_trial/assets/463489f2-f383-4d60-b7ce-8800ed0914c0.png)

1. On the **Edit details** screen, change the box details.
2. **Save** to finish the process.

#### Overview module ([Timeline mode](/cms_trial/space/SPM/1918538282/Timeline+mode/))

1. Go to the **Overview module** and open the **Home box**.
2. **Right-click** the box on the box hierarchy side (anywhere within its swimlane but the name link).

- Alternatively: **Right-click** the box bar on the timeline side.

1. Select **Edit** from the dropdown.

![Prompting options menu in the Overview module, timeline mode.](/cms_trial/assets/54ef9b3f-65aa-4b78-849a-81a539b57e85.png)

1. On the **Edit details** screen, change the box details.
2. **Save** to finish the process.

#### Overview module ([Kanban board mode](/cms_trial/space/SPM/1918700991/Kanban+board+mode/))

1. Go to the **Overview module** and open the **Home box**.
2. **Right-click** the box card (anywhere but the box name link)

- Alternatively: Click **More actions** (**…**) at the bottom of the box card.

![Prompting options menu in the Overview module, kanban board mode.](/cms_trial/assets/58eb44d3-ab16-4ce7-814d-d36a44754953.png)

### Edit box details inline

You can inline edit the box name and its period (start and end dates) directly in the Overview module ([Hierarchy](/cms_trial/space/SPM/1918799130/Hierarchy+mode/) mode only).

- Click the **Name** field and change the box name.
- Click the box **Start date** field and select a new date from the date picker.
- Click the box **End date** field and select a new date from the date picker.

![Inline editing box details. On the screen, a date picker is shown.](/cms_trial/assets/e0e2f564-bed5-4b9c-a6bc-76599b96769f.png)

## Edit box details on the box configuration page

The access to the **box configuration page** requires one of the following security roles:

- Jira Admin
- App Admin
- Box Admin

You can also change the box name and period on the box configuration page.

1. Open the box configuration page:

- Select the **Configure** option from the context menu in the Overview module (all view modes) as described in the previous section.

or

- Open a box you want to edit and click the **module switcher** > **Configuration**.

1. On the **General** > **Basic** page, rename the box and edit its period.

![Box configuration page, general settings.](/cms_trial/assets/f7c134ae-b5fc-45d1-817e-2da2a54597a0.png)

## Validate box period change

Changes in the box start/end date(s) trigger a validation check. The box’s duration is affected by its [box type settings](/cms_trial/space/SPM/1918666176/Box+configuration/).

### [Sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/)

Sequentiality settings affect box types on the same level.

![Box type configuration page, advanced settings.](/cms_trial/assets/2aee4132-40aa-49c8-b530-de103cc6b4f2.png)

- **Overlapping allowed** - periods set for boxes of the same type can overlap. The rule applies to the same-level boxes in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/).
- **Sequential** - periods set for boxes of the same type cannot overlap. The rule applies to the same-level boxes in the box hierarchy.

- Boxes in the **Auto bottom-up** [scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) and **Auto scope-based** modes can never have sequential periods, meaning they can always overlap.
- Boxes in the **Manual** and **auto top-down** modes can have their period sequential or overlapping. If they are set to **Sequential**, the same-level sequential boxes cannot overlap.
- This validation check is also triggered when you [create a new](/cms_trial/space/SPM/1918406376/Create+box/) box whose start/end dates could conflict with the period of other boxes.

![Overview module, validation error](/cms_trial/assets/396c9991-8396-47f1-9021-33d05ff6ee34.png)

### [Period mode](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/)

Box type period mode determines whether a new child box can be created with the specified start and dates.

- **Manual** - the period of a box is always set manually (no auto-scheduling adjustment).
- **Auto top-down** - the period of a box is set manually and restricts the periods of its sub-boxes.
- **Auto bottom-up** - the period of a box changes based on the period of its sub-boxes.
- **Auto scope-based** - the period of a box changes to encompass tasks in its scope.

#### Period of a box vs. period mode of its sub-boxes

Boxes in an **Auto bottom-up** period mode are affected by their children's periods, regardless of the child (sub-box) period mode.

#### Period of a box vs. period mode of its parent

- **An Auto top-down parent**:

  - limits the period of **Auto top-down** sub-boxes
  - does not affect sub-boxes in the **Manual** or **Auto scope-based** period mode
  - have its period mode overridden by the sub-box in the **Auto bottom-up** mode

Effects of the parent box period mode on a child box period are outlined in the table below.

| **Parent box →** | **box period** |
| --- | --- |
| auto bottom-up | unaffected (regardless of the child box period mode) |
| auto scope-based | unaffected (regardless of the child box period mode) |
| auto top-down | **an "auto top-down" parent limits the period of an "auto top-down" child**  Period of an "auto bottom-up" child unaffected ("auto bottom-up" child has priority over an auto "top-down parent")  Periods of "manual" and "auto scope-based" boxes unaffected |
| manual | unaffected (regardless of child period mode) |

## Limitations

### [Closed box](/cms_trial/space/SPM/1918829911/Box+lifecycle/)

- Closed boxes cannot be edited. The box configuration page cannot be accessed, either.

![Closed box. The Configure and Edit options are grayed out.](/cms_trial/assets/a93b32c2-e6b4-406e-b295-2ce3a21b8af0.png)

### Home box

- Scheduling settings are not available for the Home (root) box. But you can rename it.

![Home box basic settings. The start and end date fields are grayed out.](/cms_trial/assets/365df091-f4a4-4c62-a175-78640d6265ac.png)

The start/end dates of the Home (root) box cannot be changed. That is because they are based on the duration of the boxes in the box hierarchy:

- start date = the earliest start date of a child box
- end date = the latest end date of a child box

![Home box period based on the children boxes.](/cms_trial/assets/d7450ebe-30cd-48a8-8af5-a5ce6c18711e.png)

## Edit box details (new navigation)

Click to expand the guide

The box **Edit** option lets you change the following box details:

- name
- start date
- end date

Each detail field is required—you will not be able to **Save** your changes if the box name or start/end dates are empty.

![Edit box details screen.](/cms_trial/assets/742d8bd1-c077-4f32-b8d4-ed297bdaa88d.png)

## Permissions

The box edit action requires one of the following [security roles](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918633268):

- Jira Admin
- App Admin
- Box Admin
- Box Editor

## Edit box details in the Overview module

### Edit option on the context menu

In the [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/), you can edit a box in all three [view modes](/cms_trial/space/SPM/1918831037/Navigation+and+interface+(Overview+module)/) (Hierarchy, Timeline, and Kanban board) using the options menu.

The interactive presentation below walks you through the box editing in all Overview view modes.

<https://app.arcade.software/share/Dz7RtHUnmbrlC1duwMFo>

#### Overview module: [Hierarchy mode](/cms_trial/space/SPM/1918799130/Hierarchy+mode/)

1. Open the Main box in the Overview module.
2. In the box hierarchy, right-click the box you want to edit (anywhere within its swimlane, except the name link).

- Alternatively, click **More actions** (**…**) next to the box you want to edit.

1. Select **Edit** from the dropdown.

![Prompting options menu in the Overview module, hierarchy mode.](/cms_trial/assets/d06c4162-033e-458e-8a78-7ff0ec6a067c.png)

1. On the **Edit details** screen, change the box details.
2. **Save** to finish the process.

#### Overview module ([Timeline mode](/cms_trial/space/SPM/1918538282/Timeline+mode/))

1. Open the Main box in the Overview module.
2. In the box hierarchy, right-click the box you want to edit (anywhere within its swimlane, except the name link).

- Alternatively: **Right-click** the box bar on the timeline side.

1. Select **Edit** from the dropdown.

![Prompting options menu in the Overview module, timeline mode.](/cms_trial/assets/83c1beff-dc74-4cb8-a508-875af54eca69.png)

1. On the **Edit details** screen, change the box details.
2. **Save** to finish the process.

#### Overview module ([Kanban board mode](/cms_trial/space/SPM/1918700991/Kanban+board+mode/))

1. Open the Main box in the Overview module.
2. **Right-click** the box card (anywhere but the box name link)

- Alternatively: Click **More actions** (**…**) at the bottom of the box card.

![Prompting options menu in the Overview module, kanban board mode.](/cms_trial/assets/181f2108-bb5f-4cc6-9245-4945ab194f53.png)

### Edit box details inline

You can inline edit the box name and its period (start and end dates) directly in the Overview module (Hierarchy mode only).

- Click the **Name** field and change the box name.
- Click the box **Start date** field and select a new date from the date picker.
- Click the box **End date** field and select a new date from the date picker.

![Date picker prompted in the End Date column.](/cms_trial/assets/b8dd8438-1e4b-4acf-86b1-9742d6503804.png)

## Edit box details on the box configuration page

Access to the **box configuration page** requires one of the following security roles:

- Jira Admin
- App Admin
- Box Admin

You can also change the box name and period on the box configuration page.

1. Open the box configuration page:

- Select the **Configure** option from the context menu in the Overview module (all view modes) as described in the previous section.

or

- Open a box you want to edit and click the **module switcher** > **Configuration**.

1. On the **General** > **Basic** page, rename the box and edit its period.

![Box configuration page, general settings.](/cms_trial/assets/f7c134ae-b5fc-45d1-817e-2da2a54597a0.png)

## Validate the box period change

Changes in the box start/end date(s) trigger a validation check. The box’s duration is affected by its [box type settings](/cms_trial/space/SPM/1918666176/Box+configuration/).

### Sequentiality

[Sequentiality settings](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) affect box types on the same level.

![Box type configuration page, advanced settings.](/cms_trial/assets/6dea6d62-4df0-4851-88f9-d8afaa9dd50f.png)

- **Overlapping allowed** - periods set for boxes of the same type can overlap. The rule applies to boxes at the same level in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/).
- **Sequential** - periods set for boxes of the same type cannot overlap. The rule applies to boxes at the same level in the box hierarchy.

- Boxes in the **Auto bottom-up** [scheduling mode](/cms_trial/space/SPM/1918831395/Scheduling+mode/) and **Auto scope-based** modes can never have sequential periods, meaning they can always overlap.
- Boxes in the **Manual** and **auto top-down** modes can have their period sequential or overlapping. If they are set to **Sequential**, the same-level sequential boxes cannot overlap.
- This validation check is also triggered when you [create a new](/cms_trial/space/SPM/1918406376/Create+box/) box whose start/end dates could conflict with the period of other boxes.

![Overview module, validation error](/cms_trial/assets/396c9991-8396-47f1-9021-33d05ff6ee34.png)

### Period mode

[Box type period mode](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) determines whether a new child box can be created with the specified start and end dates.

- **Manual** - the period of a box is always set manually (no auto-scheduling adjustment).
- **Auto top-down** - the period of a box is set manually and restricts the periods of its sub-boxes.
- **Auto bottom-up** - the period of a box changes based on the period of its sub-boxes.
- **Auto scope-based** - the period of a box changes to encompass tasks in its scope.

#### Period of a box vs. period mode of its sub-boxes

Boxes in an **Auto bottom-up** period mode are affected by their children's periods, regardless of the child (sub-box) period mode.

#### Period of a box vs. period mode of its parent

- **An Auto top-down parent**:

  - limits the period of **Auto top-down** sub-boxes
  - does not affect sub-boxes in the **Manual** or **Auto scope-based** period mode
  - have its period mode overridden by the sub-box in the **Auto bottom-up** mode

The effects of the parent box period mode on the child box period are outlined in the table below.

| **Parent Box →** | **New Box (child)** |
| --- | --- |
| Auto bottom-up | Unaffected (regardless of the child's period mode) |
| Auto scope-based | Unaffected (regardless of the child’s period mode) |
| Auto top-down | - An **auto top-down** parent limits the period of an **auto top-down** child. - The period of an **auto bottom-up** child is unaffected (an **auto bottom-up** child has priority over an **auto top-down parent**). - Periods of the **manual** and **auto scope-based** boxes are unaffected. |
| Manual | Unaffected (regardless of child period mode) |

## Limitations

### Closed box

- [Closed boxes](/cms_trial/space/SPM/1918829911/Box+lifecycle/) cannot be edited. The box configuration page cannot be accessed, either.

![Closed box. The Configure and Edit options are grayed out.](/cms_trial/assets/a93b32c2-e6b4-406e-b295-2ce3a21b8af0.png)

### Home box

- Scheduling settings are not available for the Main box. But you can rename it.

The start/end dates of the Main box cannot be changed. That is because they are based on the duration of the boxes in the box hierarchy:

- start date = the earliest start date of a child box
- end date = the latest end date of a child box