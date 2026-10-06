# Boxes

## About the boxes (old navigation)

Click to expand the guide

In BigPicture, boxes make managing projects and portfolios much easier. You can think of boxes as a way to group your projects, teams, products, or portfolios, much like how you would organize photos into different collections. This helps you stay organized and gain clear control over all your tasks, even if you have thousands of them.

Boxes let you organize tasks in Jira and other connected platforms. Two key points about boxes are:

1. You can create as many boxes as you need.
2. Each box can hold any number of objects, like tasks, projects, or versions, so you can group any set of Jira issues together.

The combination of boxes and advanced filters gives you a powerful way to manage everything in one place.

## [Box basic attributes](/cms_trial/space/SPM/1918404836/Box+attributes/)

Boxes have a set of inherent characteristics (attributes) that help you define the box and manage its contents. Some of those attributes are defined during the box creation, while others can be configured only after the box is created on the box configuration page.

Many of the box and [timebox attributes](/cms_trial/space/SPM/3019800816/Timebox+attributes/) are the result of the [box type attributes](/cms_trial/space/SPM/1918832188/Box+type+attributes/).

During the box creation process, you define the following basic box attributes:

![Create box dialog.](/cms_trial/assets/aeace28c-8497-41a7-bc3c-c3ab23c60b7d.png)

- Type (you specify the [box type](/cms_trial/space/SPM/1918830000/Box+types/) you want to serve as the template for your new box. The availability of the box types in the dropdown depends on the new box’s location in the box hierarchy and the supported [box parent types](/cms_trial/space/SPM/1918832188/Box+type+attributes/))
- Name (name your box to reflect the purpose or goal of the initiative, such as the project name)
- Icon and color (select the icon and icon background color for your box. This is a purely visual element that is meant to help you identify your box and does not impact any settings or box behavior. A colored icon is displayed in both the [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/) and the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/). The default setup can be changed either during the creation of a box or later in its configuration).
- Start/end date (the duration of the box. It can depend on the tasks' dates or the [period mode and sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) as defined in the box type)

Once the box is created:

- ID (the app auto-generates the box ID based on the box type you have used to create the box)
- Status (the box status is managed manually and reflects the box progress throughout its [lifecycle](/cms_trial/space/SPM/1918829911/Box+lifecycle/))

The box ID, name, icon, and status are displayed at all times in the [module switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/).

![Module switcher.](/cms_trial/assets/6e67d860-29dc-429a-9f43-74ba6cf82379.png)

On the [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page, you can further define the following:

- Lead (a leader of a project, program, portfolio, iteration, and so on. The type of leader displayed on the **General** > **Basics** page depends on the box type. On the Home/root level, you define the “Main lead”)
- Description (optional; a summary of the box content to keep other stakeholders informed. The box description is displayed in the [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/) and [columns views](/cms_trial/space/SPM/1918404907/Column+views/))

![Box configuration page.](/cms_trial/assets/9d1fa2b1-a139-402e-97d8-8e0ab9fd7daa.png)

- [Modules](/cms_trial/space/SPM/1918503298/Define+available+modules/) (module availability depends on the box type and individual box settings)
- [Security roles](/cms_trial/space/SPM/1918797447/Box-level+permissions/) (when you create a box based on a box type, default users and groups are added per the box type settings.

## [Types of boxes](/cms_trial/space/SPM/1918830000/Box+types/)

Box types are pre-configured templates that make new box creation faster. The “contents” you want to put in your box determine the type of box you want to use for your new box.

There are many different box types, but all of them can be categorized as:

- [Portfolio type](/cms_trial/space/SPM/1918634872/Create+portfolio+box/) (portfolio boxes are designed to hold any amount of project and program boxes, including their children (sub-boxes))
- Project types (project boxes, such as Agile Project box, Classic Project box, and Hybrid Project box, are designed to help you manage projects using a specific methodology)
- Sub-boxes/[timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) (sub-boxes are child boxes to any other box that holds them in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/). For a portfolio box, an Agile Project box can be a sub-box; and for an Agile box, a Sprint can be its sub-box. A sub-box that is not a portfolio, program, or project box is typically called a timebox because it has a set duration, such as Program Increment, Iteration, Stage, etc.)

In addition, you can create a custom box and configure it to perfectly fit your initiative and project management methodology.

## [Box scope type](/cms_trial/space/SPM/1918766536/Scope+types/)

Boxes can be created with different types of scope, and their scope depends on the box type settings. Moreover, each box can have a unique scope of tasks that results from the synchronization of single or multiple Jira projects or manually added Jira and [basic tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/).

The scope of the box is defined on the **box configuration** > **Tasks** > [**Scope definition**](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) page (new navigation: **box configuration** > **Tasks** > [**Work items from Jira**](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/)**)**.

## [Box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/)

Boxes can contain other boxes (sub-boxes), even if those have their own sub-boxes. The parent-child relationships allow you to build complex box hierarchies, manually [move boxes](/cms_trial/space/SPM/1918406916/Move+box+in+box+hierarchy/) along the hierarchy, and sort them.

You cannot nest any box type under every other box type—the box relationships depend on the [box type](/cms_trial/space/SPM/1918830000/Box+types/) settings where you define parent types.

## Settings that affect tasks in a box

### [Task period alignment](/cms_trial/space/SPM/1918700014/Task+period+alignment+(Automation)/)

Task period alignment is an [automatic scheduling mechanism](/cms_trial/space/SPM/1918535176/Automations/) that aligns or adjusts the tasks' start/end dates with the box's start/end dates.

### [Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/)

Field mapping ensures that the data from Jira fields inside your Jira issues correspond to the fields in BigPicture. You can configure fields on the global (general mapping) and project (custom mapping) levels.

### [Task structure](/cms_trial/space/SPM/1918832018/Task+structure/)

Task structure in your box can be generated automatically with the [structure builders](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/) or [manually](/cms_trial/space/SPM/1918669003/Manual+task+structure/) when you move and nest individual tasks by hand.

### [Default task scheduling mode](/cms_trial/space/SPM/1918667098/Configure+task+scheduling/)

The default scheduling option on the [box type](/cms_trial/space/SPM/1918830000/Box+types/) configuration page determines how new tasks added to the box will interact with the scheduling mechanism, including factors like task dependencies and parent/child relationships.

You can manually change task scheduling mode in every module and gadget that supports [column view](/cms_trial/space/SPM/1918404907/Column+views/).

### Team [task auto-assignment](/cms_trial/space/SPM/1918408224/Automatic+assignment/)

The task is automatically assigned to the team based on the task assignee. This option can be enabled on the **App Configuration** > [**Resources**](/cms_trial/space/SPM/1918636014/Resources+(App+configuration)/) page (toggle **Tasks assigned to an individual are auto-assigned to their team** option).

![App configuration page.](/cms_trial/assets/4e797b02-ede1-4941-bef7-858664f734d3.png)

## Box settings that affect task views

In BigPicture, tasks are represented in three different ways:

- as [taskbars](/cms_trial/space/SPM/1918637856/Taskbar/) in the Gantt and Resources modules
- on the [column view](/cms_trial/space/SPM/1918404907/Column+views/) in every module and gadget that supports column views. (Column views can be customized on the box/box type configuration page and in the module/[gadget](/cms_trial/space/SPM/1918830223/Gadgets/)).
- as [task cards](/cms_trial/space/SPM/1918536034/Card+views/) in the Board and Risks modules. (Card views can be customized on the box/box type configuration page).

## About the boxes (new navigation)

Click to expand the guide

In BigPicture, boxes make managing projects and portfolios much easier. You can think of boxes as a way to group your projects, teams, products, or portfolios, much like organizing photos into collections. This helps you stay organized and gain clear control over all your tasks, even if you have thousands.

Boxes let you organize tasks in Jira and other connected platforms. Two key points about boxes are:

1. You can create as many boxes as you need.
2. Each box can hold any number of objects, like tasks, projects, or versions, so you can group any set of Jira work items together.

The combination of boxes and advanced filters gives you a powerful way to manage everything in one place.

## Box basic attributes

[Boxes have a set of attributes](/cms_trial/space/SPM/1918404836/Box+attributes/) that help you define the box and manage its contents. Some of those attributes are defined during the box creation, while others can be configured only after the box is created on the box configuration page.

Many of the box and [timebox attributes](/cms_trial/space/SPM/3019800816/Timebox+attributes/) are determined by the [box type attributes](/cms_trial/space/SPM/1918832188/Box+type+attributes/).

During the box creation process, you define the following basic box attributes:

![Create box dialog.](/cms_trial/assets/aeace28c-8497-41a7-bc3c-c3ab23c60b7d.png)

- **Type** (you specify the [box type](/cms_trial/space/SPM/1918830000/Box+types/) you want to serve as the template for your new box. The availability of the box types in the dropdown depends on the new box’s location in the box hierarchy and the supported [box parent types](/cms_trial/space/SPM/1918832188/Box+type+attributes/))
- **Name** (name your box to reflect the purpose or goal of the initiative, such as the project name)
- **Icon** and **icon background color** (select the icon and icon background color for your box. This is a purely visual element that is meant to help you identify your box and does not impact any settings or box behavior. A colored icon is displayed in both the [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/) and the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/). The default setup can be changed either during the creation of a box or later in its configuration).
- **Start and end dates** (the duration of the box. It can depend on the tasks' dates or the [period mode and sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) as defined in the box type)

Once the box is created:

- **ID** (the app auto-generates the box ID based on the box type you have used to create the box)
- **Status** (the box status is managed manually and reflects the box progress throughout its [lifecycle](/cms_trial/space/SPM/1918829911/Box+lifecycle/))

The box ID, name, icon, and status are displayed at all times next to the [module switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/).

![Box status next to the box switcher.](/cms_trial/assets/336f2848-c8a0-44f0-9e48-4089e30a53fc.png)

On the [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page, you can further define the following:

- **Lead** (a leader of a project, program, portfolio, iteration, and so on. The type of leader displayed on the **General** > **Basics** page depends on the box type. On the Home/root level, you define the “Main lead”)
- **Description** (optional; a summary of the box content to keep other stakeholders informed. The box description is displayed in the [Overview module](/cms_trial/space/SPM/1918502655/Overview+module/) and [columns views](/cms_trial/space/SPM/1918404907/Column+views/))

![Basic box details in the box configuration.](/cms_trial/assets/c6952cc9-8f17-4204-8161-04061dfbd4f8.png)

- [**Modules**](/cms_trial/space/SPM/1918503298/Define+available+modules/) (module availability depends on the box type and individual box settings)
- [**Security roles**](/cms_trial/space/SPM/1918797447/Box-level+permissions/) (when you create a box based on a box type, default users and groups are added per the box type settings.

## Types of boxes

[Box types](/cms_trial/space/SPM/1918830000/Box+types/) are preconfigured templates that speed up new box creation. The “contents” you want to put in your box determine the type of box you want to use for your new box.

There are many different box types, but all of them can be categorized as:

- [Portfolio type](/cms_trial/space/SPM/1918634872/Create+portfolio+box/) (portfolio boxes are designed to hold any number of project and program boxes, including their children (sub-boxes))
- Project types (project boxes, such as Agile Project box, Classic Project box, and Hybrid Project box, are designed to help you manage projects using a specific methodology)
- Sub-boxes/[timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) (sub-boxes are child boxes to any other box in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/)). For a Portfolio box, an Agile Project box can be a sub-box; and for an Agile box, a Sprint can be its sub-box. A sub-box that is not a portfolio, program, or project box is typically called a timebox because it has a set duration, such as Program Increment, Iteration, Stage, etc.)

In addition, you can create a custom box and configure it to fit your initiative and project management methodology perfectly.

## Box scope type

Boxes can be created with [different scopes](/cms_trial/space/SPM/1918766536/Scope+types/), and their scope depends on the box type settings. Moreover, each box can have a unique scope of tasks that results from the synchronization of one or more Jira projects, or from manually added Jira and [BigPicture tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/).

The scope of the box is defined in the **box configuration** > **Tasks** > [**Work items from Jira**](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/).

## Box hierarchy

Boxes can contain other boxes (sub-boxes), even if those have their own sub-boxes. The parent-child relationships allow you to build complex [box hierarchies](/cms_trial/space/SPM/1918535907/Box+hierarchy/), manually [move boxes](/cms_trial/space/SPM/1918406916/Move+box+in+box+hierarchy/) along the hierarchy, and sort them.

You cannot nest any box type under every other box type—the box relationships depend on the [box type](/cms_trial/space/SPM/1918830000/Box+types/) settings, where you define parent types.

## Settings that affect tasks in a box

### Task period alignment

[Task period alignment](/cms_trial/space/SPM/1918700014/Task+period+alignment+(Automation)/) is an automatic scheduling mechanism that aligns or adjusts the tasks' start/end dates with the box's start/end dates.

### Field mapping

[Field mapping](/cms_trial/space/SPM/1918700586/Field+mapping/) ensures that the data from Jira fields inside your Jira work items corresponds to the fields in BigPicture. You can configure fields on the global (general mapping) and project (custom mapping) levels.

### Task structure

[Task structure](/cms_trial/space/SPM/1918832018/Task+structure/) in your box can be generated automatically with the [structure builders](/cms_trial/space/SPM/1918536846/Automatic+task+structure+(structure+builders)/) or [manually](/cms_trial/space/SPM/1918669003/Manual+task+structure/) when you move and nest individual tasks by hand.

### Default task scheduling mode

The default [task scheduling](/cms_trial/space/SPM/1918667098/Configure+task+scheduling/) option on the [box type](/cms_trial/space/SPM/1918830000/Box+types/) configuration page determines how new tasks added to the box interact with the scheduling mechanism, including factors such as task dependencies and parent/child relationships.

You can manually change the task scheduling mode in every module and gadget that supports [column view](/cms_trial/space/SPM/1918404907/Column+views/).

### Team task auto-assignment

The task is [automatically assigned to the team](/cms_trial/space/SPM/1918408224/Automatic+assignment/) based on the task assignee. This option can be enabled on the **App Configuration** > [**Resources**](/cms_trial/space/SPM/1918636014/Resources+(App+configuration)/) page (under the **Tasks assigned to an individual are auto-assigned to their team** toggle).

![Resource configuration in the App configuration.](/cms_trial/assets/4e797b02-ede1-4941-bef7-858664f734d3.png)

## Box settings that affect task views

In BigPicture, tasks are represented in three different ways:

- as [taskbars](/cms_trial/space/SPM/1918637856/Taskbar/) in the Gantt and Resources modules
- on the [column view](/cms_trial/space/SPM/1918404907/Column+views/) in every module and gadget that supports column views. (Column views can be customized on the box/box type configuration page and in the module/[gadget](/cms_trial/space/SPM/1918830223/Gadgets/)).
- as [task cards](/cms_trial/space/SPM/1918536034/Card+views/) in the Board and Risks modules. Card views can be customized on the box/box type configuration page.