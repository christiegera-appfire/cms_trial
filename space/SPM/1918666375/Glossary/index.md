# Glossary

## Glossary (old navigation)

Click to expand the guide

### Allocation

The actual or planned workload of the individual resources or a Team. The effort expressed as the time or number of Story Points required to complete a task is evenly distributed over the task's duration.

### Baseline

To assess your project's performance over time, you can set Baselines and track deviations from your initial schedule.

The Baselines can be synchronized with Jira (Tasks require Jira Admin permissions), and the synced fields can be added to Column views or as fields to the Task / Risk Cards.

You can create and delete Baselines for all the tasks in the scope of the Box or for selected tasks only. They are displayed as bold lines, showing the position of the task at the moment of creating the Baseline.

### Basic task

The App stores basic tasks and they are NOT synchronized with Jira or other connected tools like Trello. Basic tasks can be viewed only using the App's Gantt, Scope, Board modules, or the WBS Widget.

They can coexist with other tasks, work great as placeholders or temporary tasks, simulate higher levels in the hierarchy, or serve as additional information boxes.

The Appuses them to replace non-issue Jira entities (like Components, Versions, and Projects), which it cannot recreate in Jira while cloning the scope.

### Box

A box is a customizable, structured space (container) where you organize and visualize your project, program, and portfolio elements, such as tasks, deliverables, resources, risks, and even other boxes (sub-boxes).

Boxes are equipped with all the essential tools for efficient management, allowing you to adapt seamlessly to various project management approaches, including Agile, scaled Agile, Hybrid, and Waterfall. You can also customize them to support unique methodologies that do not fall into any of those categories.

Each box can be customized based on the specific tools (modules) needed for your project, the scope of work, and the security roles required for viewing and managing the box.

### Box hierarchy

Box hierarchy is a structured system for organizing and managing the various elements of projects, programs, and portfolios.

At the top of the box hierarchy is the Home (root) box, which acts as a container for all the boxes created within your organization. Boxes created under the root can also house additional boxes (sub-boxes).

All those boxes form parent-child hierarchies, allowing you to view and aggregate project, program, or portfolio data at both high and low levels. You can view the entire box hierarchy in the Overview module using the Hierarchy and Timeline modes.

By default, only specific box types can serve as parents to other box types. However, you can redefine the parent-child relationships between your boxes and sub-boxes to create custom hierarchies that align with your business needs.

The sub-boxes can inherit specific settings from their parents or have a separate configuration.

### Box type

Box template, which defines the most relevant characteristics of a Box (node), such as:

- types of parent Boxes under which a Box of a given type can be nested
- default module configuration and names
- default column view of different modules
- default card layout
- default Period mode

Box types can be defined by BigPictures administrators.

### Box module

The following modules are available in BigGantt:

- Overview
- Gantt

The following modules are available in BigPicture:

- Overview
- Gantt
- Risks
- Roadmap
- Board
- Calendar
- Resources
- Teams

Most of the modules can be preconfigured using Box types.

### Box switcher

The box switcher, located in the upper-left corner of the application, displays the name of the current Box you are viewing. When you click it, a drop-down list containing the Box hierarchy tree is displayed. You can then select a specific Box from the hierarchy to switch to.

Use the box switcher to switch between different boxes easily. Once opened, the active box is highlighted, so you can easily switch to a sub-box or a different box.

You can browse only the Boxes to which you have permission (you can't see a box that you can't access).

The Box switcher is displayed in the Apps header for each module and in the WBS Widget and Skill Widget, which can be added to the issue screen.

### Box status

The status of the box determines your ability to modify the box details or adjust the box configuration.

This status is visible beside the box name within the box switcher. You can update it across various sections of the app. In the Overview module, you can modify it by right-clicking or using drag-and-drop while in Kanban mode. Additionally, you can adjust the status through the Board module. For sub-boxes, you can alter their status on the Scope definition page (Box configuration).

The status is indicated using colors. The following color-coded statuses are available:

- Not started - gray
- In progress - blue
- Done - green

### Capacity

The App calculates individual and team capacity.

The capacity of your resources is calculated based on Workload Plans and non-working days resulting from Holiday Plans and individual Absence Plans. It reflects the workload resources are capable of after everything has been considered.

### Column views

Column Views allow you to add different fields as columns to the task list and configure their display and aggregation settings. These settings determine how data is presented in the Gantt and Scope type module's task list.

### Connected tools

The App can connect different tools to your Jira instance. These include tools like other Jira Cloud instances, Trello, or MS Azure (coming soon). The connection field (status) informs you if your instance was already connected.

### Context Box

A Box which you are currently viewing. The Box name and its status are displayed in the Box Switcher.

### Critical path

The critical path is the longest sequence of tasks that determines the project duration. This feature highlights all the tasks on the critical path with the red color. Tasks on the Critical path will also be listed in the Gantt Infobar.

To highlight the entire sequence, you must define dependency links between tasks. Only the strong links that impact scheduling will determine the tasks on the critical path.

### Dependency

Dependencies specify the relationships between tasks, milestones, and other items that can be presented on the timeline and displayed by the Gantt and Board type modules (Gantt and Board are the default module names used). By defining dependencies, you can automate task scheduling and highlight relations between tasks without impacting the schedule. Remember that the items presented on the Gantt chart are system-wide, and changing their dependencies might affect tasks in other Boxes or connected tools.

The Gantt module takes linking to the next level, and you can use non-Jira links to define dependencies between Issues and non-issues, such as Projects, Versions, Components, Sprints and Backlog, Checklists, etc. You can visualize up to five different links. Almost any native Jira link or custom link can be synchronized.

The Board module dependencies are color-coded so that you can easily find the tasks that need your attention.

The strong dependencies between tasks impact the scheduling of those tasks (does not apply to Soft links). Linked tasks will push and pull each other in time, according to their dependency properties. Those properties and their impact work as listed below:

- Dependency type determines the dependency's direction and which of the Tasks' dates are relevant. We call them "relevant" because specific changes to those dates might cause either rescheduling of the dependent tasks or even make them impossible to perform (the app will immediately revert the task to the previously calculated dates). To get more information on those changes and their outcome, see the table at the bottom of this page. Changes of the dates that are not "relevant" do not cause rescheduling of this dependency (but might still cause changes to its parent's or children's periods).
- Lag Time is the period calculated in days by dividing the inked tasks. Lag time has the highest priority over other Dependency properties. The lag time will be respected and applied regardless of other circumstances in both ASAP and non-ASAP modes. The type of Dependency determines which date (Start or End) of the Source task the Lag Time will be added to.
- ASAP mode always schedules the Target task to occur ‘as soon as possible,’ according to dependency type. This renders the Target task strictly dependent on the Source. Therefore, it will be impossible to drag and drop it, neither to the future nor the past. The Target task will always revert to its position previously calculated by scheduling.

### Effort mode

The Resources and Gantt module show the resource workload vs capacity in three different effort mods:

- Original Estimate Mode - this mode shows the planned workload versus the resource capacity.
- Remaining estimate mode - use this mode to show workload history (Spent time) and the remaining workload versus the resource capacity.
- Story points mode - use this mode to show the planned workload versus resource capacity expressed in Story Points.

### Gadgets

Thanks to the Gadgets, you can add dynamic content to a Confluence page or the Jira application dashboard to monitor the health of projects, departments, or specific processes. This means that you can have your favorite Gantt charts and Risks all in one place and thanks to the auto-refresh all up to date.

There are three Gadgets available:

- Gantt
- Risks
- Boxes

### Holiday plans

A calendar that reflects the non-working day reduces the capacity of Teams or individual Resources (Team members).

### Inheritance mode

When creating a new Box type or moving a sub-Box to a different parent Box, thanks to the Inheritance mode, the Box type configuration can be passed on from the upper-level Box type to the sub-Box type.

Three Inheritance modes determine whether users can customize the Box settings. Inheritance modes can be set for:

- Card Views,
- Quick filters
- Column Views
- Security

### Marker

There can be several important dates that call for exceptional care and attention. You can highlight them using a marker, whatever they can be: from a crucial external event to a deadline, you name it. Once highlighted, they'll become instantly visible to all users with access to the App and appropriate security roles to view the Box content.

Markers can only be viewed using the App, and when you add a marker, it will be visible on the timeline of the following modules:

- Overview
- Gantt
- Board
- Roadmap

With live synchronization and various colors, you can make your timeline a complete source of information for everyone.

### Milestones

Any task can be converted into a milestone. On the timeline, milestones are represented as diamonds. The duration of a milestone is always one day.

Used to mark specific points along a project timeline, and they do not impact the project duration. When a task is converted to a milestone, a label can be created #milestone in a filter to show milestones only.

Milestones can be interpreted as:

- Markers of reaching an identifiable stage in any task or project.
- Software release lifecycle states.

### Multi-select

You can select multiple tasks and perform bulk operations (deleting tasks, moving them to a different place in the hierarchy, outdent, indenting, changing task color).

The following modules support multi-select:

- Overview
- Gantt
- Scope
- Board

### Non-working days

The App can recognize non-working days and adjust the task period. If you plan a task or part of your task's period on a non-working day, it will be moved, extended, or shortened.

You can define the non-working days in the Administration section:

- Absence plans
- Holiday plans
- Workload plans

Each non-working day reduces the capacity of your Resource. The App calculates the capacity and does not sync with the Host platform (you will not be able to see the capacity of your Resource directly in Jira or Trello).

### Period warning

Period warnings occur when a parent task can't be recalculated due to a constraint, such as a blocking task (a task in Locked mode), non-working day, or when you use the manual period mode.

The warning is displayed as a yellow box with a dashed-line frame and shows the position of the parent tasks calculated based on its children.

### Task Progress

You can calculate the task progress using different fields and formulas. The progress can be displayed as a column on the taskbar and the task details dialog once you click on the taskbar.

### Resources panel

The Resources panel lets you see how much work has been assigned.

With the Resource panel enabled, the workload of each resource (assignee) will be counted in hours and color-coded depending on the resource capacity.

The workload data is filter-sensitive, i.e., only the tasks in the current view are included in the workload calculation. You can use Quick Filters or the Search Box to filter out tasks and simulate different scenarios.

As a rule, the effort is distributed evenly throughout a task, but you can change how it is distributed in the Resources module. To learn more, see [Workload contouring](/cms_trial/space/SPM/1918767273/Workload+contouring/).

### Risk

Any Jira issue with the "Risk probability" and "Risk consequence" field values.

"Risk consequence" and "Risk probability" fields must be added to your Jira screen configuration scheme.

### Risks module

The risks module consists of two main elements:

- Customizable risk heat map
- Customizable risk list (register)

You can configure a risk heat-map. The heat-map can be used to show the level of risk resulting from the risk assessment by considering the category of probability or likelihood against the category of consequences or severity.

In the [app's configuration](/cms_trial/space/SPM/1918698881/App+configuration/), you can define a name for the Risks axis and set the corresponding custom.

### Scenario mode

With the Scenarios feature, you can quickly try out different variants of your plan, compare the results, and find the best one.

All task changes are stored in the Scenario history, and you can easily undo them. When you create a scenario, changes made to your tasks are synchronized with Jira or other connected tools, such as Trello, only after merging.

### Scheduling mode

The scheduling mode determines whether a task is scheduled manually or automatically, which gives you the option of deciding how much control you want over task scheduling in a box.

There are five different modes explained further below:

- Auto basic
- Auto bottom-up
- Auto top-down
- Manual
- Locked

#### Auto bottom-up

#### Auto top-down

#### Manual

#### Locked

### Scope

A defined collection of tasks makes up the Box Scope. In general, tasks can be manually added to the scope or automatically synchronized with Jira or connected tools such as Trello.

In "Scope definition," you can specify what range of tasks is included in the scope of a given Box - those are the tasks you will be able to work within the Application (visualize them on a Gantt chart, manage Risks, distribute workload, etc). The App gives you much flexibility; you can include multiple Jira projects, simultaneously include tasks from different external tools (such as Trello and Jira), or include only some tasks that meet your particular specifications. The flexibility of the setup ensures that a Box can be configured to contain precisely the tasks you need to fit your work.

### Scope type

The Scope type determines how the box's scope functions and how it is related to and impacted by other Boxes.

There are three different options:

- Own-scope - the box scope has a separate task structure and is a sub-scope scope base. Automatic rules can sync it. Use it when you want to define and extend the scope of a Box by selecting tasks from Jira and connected tools.
- Sub-scope - the box scope is always a subset of the scope already defined at an upper level of the Box hierarchy. It can be automatically synced with a value of a selected field or manually adjusted using the Board module.
- None -  the Box scope cannot be defined. Currently, you can use such a Box for calculating respective aggregates in the Box hierarchy only (visible in the Overview module). Use this setting to organize Boxes into portfolios, programs, etc. The scope is always a sum of the scopes of the sub-Boxes in the Box hierarchy.

### Search box

The Search box functionality will help you quickly find your interests and filter out unwanted tasks or Boxes. The Search box operates in two modes:

- Text search mode, which filters information based on the Jira summary field (Boxes and tasks)
- JQL mode, which, as the name suggests, filters information using JQL queries (tasks only)

The Search box is available in the following modules:

- **Overview (text search only)**
- **Gantt**
- **Scope**
- **Board**
- **Risks**
- **Calendar**
- **Resources**
- **Teams (text search only)**

Snipe to task feature allows one to search and find a task that fits search criteria quickly.

### Security

To learn more, see the [Permissions](/cms_trial/space/SPM/1918829579/Permissions/) page.

### Skills

The skills are defined at:

- The task level - skill required to complete a task. The related effort is used to calculate the skill demand and is evenly distributed over the task's duration. The skill demand will be displayed in the Resources module's Skill panel.
- The resource level - skill acquired by the resource. The resource’s time is allocated across different skills. Skills weigh most in the "Perfect match algorithm," which is approximately 80%.

Each skill has a start and end date so that you can plan the skill development over time.

### Skills Panel

Skills Panel is a part of the Resources module. It displays a comprehensive li ‘ of skill.’ Only the tasks displayed on the Resource Grid (within the visualized period) are considered. The skill effort is included in the calculation for any task that is at least partly displayed.

- Skill Capacity - total skill capacity of the currently displayed resources.
- Skill Remaining capacity - remaining availability in a given period when a resource is assigned to a task.

### Task

Any Jira issue, Trello card, or Basic task (native to the App).

### Team

The team module lets you group individual users into teams, enabling effort-based planning.

The concept of teams is used mainly in the Resources, Objectives, and Board modules, but since the information about the team can be stored as a label or a custom field, it can also be displayed using the Gantt, Scope, or Risks module by adding it to the Column View or Card View.

You can create global teams and assign them to multiple Boxes. Once created, you can easily give them to individual Boxes (a team is inherited and can't be edited on a Box level) or duplicate them in a personal Box (a team configuration is duplicated and can be further edited).

### Team Capacity

The capability to achieve a set amount of productivity within a single day is calculated as the sum of Team members' capacities. Team capacity factors in the existing manpower are known to readily possess the necessary skill set and the number of hours in a workday.

Calculating individual capacity considers team members' availability across all teams they're a part of.

### Team code

Team code identifies teams by the App's modules and, when synchronized, the Host and connected platforms. Depending on the configuration, the Team code is stored as the following fields:

- Labels type
- Select list – single choice type
- --none-- (not synchronized)

You can use these fields in your JQL to create a Jira Board dedicated to a specific team or as Quick Filters.

### Team Member

A resource assigned to a team.

### Team Member Availability

You can set availability for each team member (what percentage of their working hours is assigned to the team). Availability impacts the capacity - if a team has four members, and each is given 50% of their eight-hour day to the team, the team capacity for a day is 16 hours (if no other non-working days detract from capacity).

### Timebox

Timeboxes define consecutive timeframes used for work planning. It helps to think of them as, e.g., sprints, iterations, increments, or stages.

Those Boxes don't have their scope; they are used to organize and display tasks that have been added to the upper-level Box. The main Program/Project Box is where the tasks are added; those tasks are assigned to various Timeboxes (for example, each Iteration could correspond to a sprint).

Timeboxes are sequential - their periods don't overlap.

### Timeline

The Timeline is a common element of the following modules:

- Overview - Timeline mode - you can show and edit Boxes using drag and drop.
- Gantt - you can show Tasks, Projects, Sprints, Backlog, Components, Versions, Boxes and Markers.
- Board and Objectives - you can show Markers and Boxes.
- Resource - you can show tasks.

### Widget

There are two widgets that you can add to the Detailed issue view:

- Skill Widget
- WBS Widget

### Workload contouring (Box Configuration)

Workload distribution for a given task. Workload contouring allows you to specify how the effort of an assignee is distributed across a task period.

### Workload plan

A calendar that reflects specific working hours of an individual resource and is the basis for capacity calculation of Teams or personal Resources (Team members). Workload plans are used to define exact working hours. You can create as many as you like and assign them to your resources separately.

## Glossary (new navigation)

Click to expand the guide

### Allocation

The actual or planned workload of the individual resources or a team. The effort expressed as the time or number of Story Points required to complete a task is evenly distributed over the task's duration.

### Baseline

To assess your project's performance over time, you can set Baselines and track deviations from your initial schedule.

The Baselines can be synchronized with Jira (Tasks require Jira Admin permissions), and the synced fields can be added to Column views or as fields to the Task / Risk Cards.

You can create and delete Baselines for all the tasks in the scope of the Box or for selected tasks only. They are displayed as bold lines, showing the position of the task at the moment of creating the Baseline.

### BigPicture task

The App stores BigPicture tasks, and they are NOT synchronized with Jira or other connected tools like Trello. BigPicture tasks can be viewed only using the App's Gantt, Scope, Board modules, or the WBS Widget.

They can coexist with other tasks, work great as placeholders or temporary tasks, simulate higher levels in the hierarchy, or serve as additional information boxes.

The Appuses them to replace non-work-item Jira entities (like Components, Versions, and Spaces), which it cannot recreate in Jira while cloning the scope.

### Box

A box is a customizable, structured space (container) where you organize and visualize your project, program, and portfolio elements, such as tasks, deliverables, resources, risks, and even other boxes (sub-boxes).

Boxes are equipped with all the essential tools for efficient management, allowing you to adapt seamlessly to various project management approaches, including Agile, scaled Agile, Hybrid, and Waterfall. You can also customize them to support unique methodologies that do not fall into any of those categories.

Each box can be customized based on the specific tools (modules) needed for your project, the scope of work, and the security roles required for viewing and managing the box.

### Box hierarchy

Box hierarchy is a structured system for organizing and managing the various elements of projects, programs, and portfolios.

At the top of the box hierarchy is the Home (root) box, which acts as a container for all the boxes created within your organization. Boxes created under the root can also house additional boxes (sub-boxes).

All those boxes form parent-child hierarchies, allowing you to view and aggregate project, program, or portfolio data at both high and low levels. You can view the entire box hierarchy in the Overview module using the Hierarchy and Timeline modes.

By default, only specific box types can serve as parents to other box types. However, you can redefine the parent-child relationships between your boxes and sub-boxes to create custom hierarchies that align with your business needs.

The sub-boxes can inherit specific settings from their parents or have a separate configuration.

### Box type

Box template, which defines the most relevant characteristics of a Box (node), such as:

- types of parent Boxes under which a Box of a given type can be nested
- default module configuration and names
- default column view of different modules
- default card layout
- default Period mode

Box types can be defined by BigPictures administrators.

### Box module

The following modules are available in BigGantt:

- Overview
- Gantt

The following modules are available in BigPicture:

- Overview
- Gantt
- Risks
- Roadmap
- Board
- Calendar
- Resources
- Teams

Most of the modules can be preconfigured using Box types.

### Box switcher

The box switcher, located in the upper-left corner of the application, displays the name of the current Box you are viewing. When you click it, a drop-down list containing the Box hierarchy tree is displayed. You can then select a specific Box from the hierarchy to switch to.

Use the box switcher to switch between different boxes easily. Once opened, the active box is highlighted, so you can easily switch to a sub-box or a different box.

You can browse only the Boxes to which you have permission (you can't see a box that you can't access).

The Box switcher is displayed in the Apps header for each module and in the WBS Widget and Skill Widget, which can be added to the work item screen.

### Box status

The status of the box determines your ability to modify the box details or adjust the box configuration.

This status is visible beside the box name within the box switcher. You can update it across various sections of the app. In the Overview module, you can modify it by right-clicking or using drag-and-drop while in Kanban mode. Additionally, you can adjust the status through the Board module. For sub-boxes, you can alter their status on the Add work items from Jira page (Box configuration).

The status is indicated using colors. The following color-coded statuses are available:

- Not started - gray
- In progress - blue
- Done - green

### Capacity

The App calculates individual and team capacity.

The capacity of your resources is calculated based on Workload Plans and non-working days resulting from Holiday Plans and individual Absence Plans. It reflects the workload resources are capable of after everything has been considered.

### Column views

Column Views allow you to add different fields as columns to the task list and configure their display and aggregation settings. These settings determine how data is presented in the Gantt and Scope type module's task list.

### Connected tools

The App can connect different tools to your Jira instance. These include tools like other Jira Cloud instances, Trello, or MS Azure (coming soon). The connection field (status) informs you if your instance was already connected.

### Context Box

A Box which you are currently viewing. The Box name and its status are displayed in the Box Switcher.

### Critical path

The critical path is the longest sequence of tasks that determines the project duration. This feature highlights all the tasks on the critical path with the red color. Tasks on the Critical path will also be listed in the Gantt Infobar.

To highlight the entire sequence, you must define dependency links between tasks. Only the strong links that impact scheduling will determine the tasks on the critical path.

### Dependency

Dependencies specify the relationships between tasks, milestones, and other items that can be presented on the timeline and displayed by the Gantt and Board type modules (Gantt and Board are the default module names used). By defining dependencies, you can automate task scheduling and highlight relations between tasks without impacting the schedule. Remember that the items presented on the Gantt chart are system-wide, and changing their dependencies might affect tasks in other Boxes or connected tools.

The Gantt module takes linking to the next level, and you can use non-Jira links to define dependencies between work items and non-work items, such as Spaces, Versions, Components, Sprints and Backlog, Checklists, etc. You can visualize up to five different links. Almost any native Jira link or custom link can be synchronized.

The Board module dependencies are color-coded so that you can easily find the tasks that need your attention.

The strong dependencies between tasks impact the scheduling of those tasks (does not apply to Soft links). Linked tasks will push and pull each other in time, according to their dependency properties. Those properties and their impact work as listed below:

- Dependency type determines the dependency's direction and which of the Tasks' dates are relevant. We call them "relevant" because specific changes to those dates might cause either rescheduling of the dependent tasks or even make them impossible to perform (the app will immediately revert the task to the previously calculated dates). To get more information on those changes and their outcome, see the table at the bottom of this page. Changes of the dates that are not "relevant" do not cause rescheduling of this dependency (but might still cause changes to its parent's or children's periods).
- Lag Time is the period calculated in days by dividing the inked tasks. Lag time has the highest priority over other Dependency properties. The lag time will be respected and applied regardless of other circumstances in both ASAP and non-ASAP modes. The type of Dependency determines which date (Start or End) of the Source task the Lag Time will be added to.
- ASAP mode always schedules the Target task to occur ‘as soon as possible,’ according to dependency type. This renders the Target task strictly dependent on the Source. Therefore, it will be impossible to drag and drop it, neither to the future nor the past. The Target task will always revert to its position previously calculated by scheduling.

### Effort mode

The Resources and Gantt module show the resource workload vs capacity in three different effort mods:

- Original Estimate Mode - this mode shows the planned workload versus the resource capacity.
- Remaining estimate mode - use this mode to show workload history (Spent time) and the remaining workload versus the resource capacity.
- Story points mode - use this mode to show the planned workload versus resource capacity expressed in Story Points.

### Gadgets

Thanks to the Gadgets, you can add dynamic content to a Confluence page or the Jira application dashboard to monitor the health of projects, departments, or specific processes. This means that you can have your favorite Gantt charts and Risks all in one place and thanks to the auto-refresh all up to date.

There are three Gadgets available:

- Gantt
- Risks
- Boxes

### Holiday plans

A calendar that reflects the non-working day reduces the capacity of Teams or individual Resources (Team members).

### Inheritance mode

When creating a new Box type or moving a sub-Box to a different parent Box, thanks to the Inheritance mode, the Box type configuration can be passed on from the upper-level Box type to the sub-Box type.

Three Inheritance modes determine whether users can customize the Box settings. Inheritance modes can be set for:

- Card Views,
- Quick filters
- Column Views
- Security

### Marker

There can be several important dates that call for exceptional care and attention. You can highlight them using a marker, whatever they can be: from a crucial external event to a deadline, you name it. Once highlighted, they'll become instantly visible to all users with access to the App and appropriate security roles to view the Box content.

Markers can only be viewed using the App, and when you add a marker, it will be visible on the timeline of the following modules:

- Overview
- Gantt
- Board
- Roadmap

With live synchronization and various colors, you can make your timeline a complete source of information for everyone.

### Milestones

Any task can be converted into a milestone. On the timeline, milestones are represented as diamonds. The duration of a milestone is always one day.

Used to mark specific points along a project timeline, and they do not impact the project duration. When a task is converted to a milestone, a label can be created #milestone in a filter to show milestones only.

Milestones can be interpreted as:

- Markers of reaching an identifiable stage in any task or project.
- Software release lifecycle states.

### Multi-select

You can select multiple tasks and perform bulk operations (deleting tasks, moving them to a different place in the hierarchy, outdent, indenting, changing task color).

The following modules support multi-select:

- Overview
- Gantt
- Scope
- Board

### Non-working days

The App can recognize non-working days and adjust the task period. If you plan a task or part of your task's period on a non-working day, it will be moved, extended, or shortened.

You can define the non-working days in the Administration section:

- Absence plans
- Holiday plans
- Workload plans

Each non-working day reduces the capacity of your Resource. The App calculates the capacity and does not sync with the Host platform (you will not be able to see the capacity of your Resource directly in Jira or Trello).

### Parent task conflicts

Parent task conflicts occur when a parent task can't be recalculated due to a constraint, such as a blocking task (a task in Locked mode), non-working day, or when you use the manual period mode.

The warning is displayed as a yellow box with a dashed-line frame and shows the position of the parent tasks calculated based on its children.

### Task Progress

You can calculate the task progress using different fields and formulas. The progress can be displayed as a column on the taskbar and the task details dialog once you click on the taskbar.

### Resource panel

The Resource panel lets you see how much work has been assigned.

With the Resource panel enabled, the workload of each resource (assignee) will be counted in hours and color-coded depending on the resource capacity.

The workload data is filter-sensitive, i.e., only the tasks in the current view are included in the workload calculation. You can use Quick Filters or the Search Box to filter out tasks and simulate different scenarios.

As a rule, the effort is distributed evenly throughout a task, but you can change how it is distributed in the Resources module. To learn more, see [Workload contouring](/cms_trial/space/SPM/1918767273/Workload+contouring/).

### Risk

Any Jira work item with the "Risk probability" and "Risk consequence" field values.

"Risk consequence" and "Risk probability" fields must be added to your Jira screen configuration scheme.

### Risks module

The risks module consists of two main elements:

- Customizable risk heat map
- Customizable risk list (register)

You can configure a risk heat-map. The heat-map can be used to show the level of risk resulting from the risk assessment by considering the category of probability or likelihood against the category of consequences or severity.

In the [app's configuration](/cms_trial/space/SPM/1918698881/App+configuration/), you can define a name for the Risks axis and set the corresponding custom.

### Scenario mode

With the Scenarios feature, you can quickly try out different variants of your plan, compare the results, and find the best one.

All task changes are stored in the Scenario history, and you can easily undo them. When you create a scenario, changes made to your tasks are synchronized with Jira or other connected tools, such as Trello, only after merging.

### Scheduling mode

The scheduling mode determines whether a task is scheduled manually or automatically, which gives you the option of deciding how much control you want over task scheduling in a box.

There are five different modes explained further below:

- Auto basic
- Auto bottom-up
- Auto top-down
- Manual
- Locked

#### Auto bottom-up

#### Auto top-down

#### Manual

#### Locked

### Scope

A defined collection of tasks makes up the Box scope. In general, tasks can be manually added to the scope or automatically synchronized with Jira or connected tools such as Trello.

In Add work items from Jira you can specify what range of tasks is included in the scope of a given Box - those are the tasks you will be able to work within the Application (visualize them on a Gantt chart, manage Risks, distribute workload, etc). The App gives you much flexibility; you can include multiple Jira spaces, simultaneously include tasks from different external tools (such as Trello and Jira), or include only some tasks that meet your particular specifications. The flexibility of the setup ensures that a Box can be configured to contain precisely the tasks you need to fit your work.

### Scope type

The Scope type determines how the box's scope functions and how it is related to and impacted by other Boxes.

There are three different options:

- Own-scope - the box scope has a separate task structure and is a sub-scope scope base. Automatic rules can sync it. Use it when you want to define and extend the scope of a Box by selecting tasks from Jira and connected tools.
- Sub-scope - the box scope is always a subset of the scope already defined at an upper level of the Box hierarchy. It can be automatically synced with a value of a selected field or manually adjusted using the Board module.
- None -  the Box scope cannot be defined. Currently, you can use such a Box for calculating respective aggregates in the Box hierarchy only (visible in the Overview module). Use this setting to organize Boxes into portfolios, programs, etc. The scope is always a sum of the scopes of the sub-Boxes in the Box hierarchy.

### Search box

The Search box functionality will help you quickly find your interests and filter out unwanted tasks or Boxes. The Search box operates in two modes:

- Text search mode, which filters information based on the Jira summary field (Boxes and tasks)
- JQL mode, which, as the name suggests, filters information using JQL queries (tasks only)

The Search box is available in the following modules:

- **Overview (text search only)**
- **Gantt**
- **Scope**
- **Board**
- **Risks**
- **Calendar**
- **Resources**
- **Teams (text search only)**

Snipe to task feature allows one to search and find a task that fits search criteria quickly.

### Security

To learn more, see the [Permissions](/cms_trial/space/SPM/1918829579/Permissions/) page.

### Skills

The skills are defined at:

- The task level - skill required to complete a task. The related effort is used to calculate the skill demand and is evenly distributed over the task's duration. The skill demand will be displayed in the Resources module's Skill panel.
- The resource level - skill acquired by the resource. The resource’s time is allocated across different skills. Skills weigh most in the "Perfect match algorithm," which is approximately 80%.

Each skill has a start and end date so that you can plan the skill development over time.

### Skills Panel

Skills Panel is a part of the Resources module. It displays a comprehensive li ‘ of skill.’ Only the tasks displayed on the Resource Grid (within the visualized period) are considered. The skill effort is included in the calculation for any task that is at least partly displayed.

- Skill Capacity - total skill capacity of the currently displayed resources.
- Skill Remaining capacity - remaining availability in a given period when a resource is assigned to a task.

### Task

Any Jira work item, Trello card, or BigPicture task (native to the App).

### Team

The team module lets you group individual users into teams, enabling effort-based planning.

The concept of teams is used mainly in the Resources, Objectives, and Board modules, but since the information about the team can be stored as a label or a custom field, it can also be displayed using the Gantt, Scope, or Risks module by adding it to the Column View or Card View.

You can create global teams and assign them to multiple Boxes. Once created, you can easily give them to individual Boxes (a team is inherited and can't be edited on a Box level) or duplicate them in a personal Box (a team configuration is duplicated and can be further edited).

### Team Capacity

The capability to achieve a set amount of productivity within a single day is calculated as the sum of Team members' capacities. Team capacity factors in the existing manpower are known to readily possess the necessary skill set and the number of hours in a workday.

Calculating individual capacity considers team members' availability across all teams they're a part of.

### Team code

Team code identifies teams by the App's modules and, when synchronized, the Host and connected platforms. Depending on the configuration, the Team code is stored as the following fields:

- Labels type
- Select list – single choice type
- --none-- (not synchronized)

You can use these fields in your JQL to create a Jira Board dedicated to a specific team or as Quick Filters.

### Team Member

A resource assigned to a team.

### Team Member Availability

You can set availability for each team member (what percentage of their working hours is assigned to the team). Availability impacts the capacity - if a team has four members, and each is given 50% of their eight-hour day to the team, the team capacity for a day is 16 hours (if no other non-working days detract from capacity).

### Timebox

Timeboxes define consecutive timeframes used for work planning. It helps to think of them as, e.g., sprints, iterations, increments, or stages.

Those Boxes don't have their scope; they are used to organize and display tasks that have been added to the upper-level Box. The main Program/Project Box is where the tasks are added; those tasks are assigned to various Timeboxes (for example, each Iteration could correspond to a sprint).

Timeboxes are sequential - their periods don't overlap.

### Timeline

The Timeline is a common element of the following modules:

- Overview - Timeline mode - you can show and edit Boxes using drag and drop.
- Gantt - you can show Tasks, Spaces, Sprints, Backlog, Components, Versions, Boxes and Markers.
- Board and Objectives - you can show Markers and Boxes.
- Resource - you can show tasks.

### Widget

There are two widgets that you can add to the Detailed work item view:

- Skill Widget
- WBS Widget

### Workload contouring (Box Configuration)

Workload distribution for a given task. Workload contouring allows you to specify how the effort of an assignee is distributed across a task period.

### Workload plan

A calendar that reflects specific working hours of an individual resource and is the basis for capacity calculation of Teams or personal Resources (Team members). Workload plans are used to define exact working hours. You can create as many as you like and assign them to your resources separately.