# Duplicate box and box scope

## Duplicate box and box scope (old navigation)

Click to expand the guide

## Overview

You can create a new box by duplicating an existing box.

When you duplicate a box, the box configuration is copied. The app copies as much of the box setup as possible. Box type settings and defaults are ignored in favor of the exact setup of the box you are making a copy of.

You can't duplicate a box with all its contents and tasks.

You can use a Configuration of an existing box, duplicate it, and create a new box with an identical configuration. However, the scope of a box (tasks inside a box) isn't duplicated—tasks have to be added to the new box scope afterward.

[Box configuration settings](/cms_trial/space/SPM/1918666176/Box+configuration/) of a box are applied to the new box:

- [security (user roles)](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918633268)
- [modules and their settings](/cms_trial/space/SPM/1918503298/Define+available+modules/)
- [connected tools](/cms_trial/space/SPM/1918633230/Integrations/) and the scope owner (tool connections get replicated)

[Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) impacts the exact setup of the newly created box.

If some settings (such as [column views](/cms_trial/space/SPM/1918404907/Column+views/) or [quick filers](/cms_trial/space/SPM/1918635901/Quick+filters/)) were inherited from the upper-level boxes, if you move a new box to a different place in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/), inherited settings can be lost. Inherited settings are always based on upper-level boxes and depend on placement within the box hierarchy.

## Duplicate a box

1. Activate the actions menu

   1. by clicking on the three dots menu icon on the right OR
   2. by right-clicking on a box row
2. Select **Duplicate configuration.** A box creation pop-up appears.

![Context menu in the box tree](/cms_trial/assets/8453c4b0-05f3-45bd-bb79-c3ab5eca6b1a.png)

1. The following fields arepre-filled:

   - Type (can’t be changed)
   - Name
   - Icon
   - Start date
   - End date
   - Jira Projects(not required)

     - available only for project boxes (can’t be filled in for boxes without their own scope, such as portfolio). Box scope can be adjusted later in a box configuration.![Create new box screen.](/cms_trial/assets/8142a3e5-8f9a-455e-87d0-c09429a6e518.png)
2. Click **Create**

### What data is duplicated

| **Settings** | **Result** |
| --- | --- |
| **Box scope** | ❌ Not copied.  The scope configuration is not copied.  Box content is not replicated (spaces, tasks, issues etc). contentId-1918635048 |
| **Sub boxes** | ❌ Not copied  Child boxes are not duplicated. |
| **Reports** | ❌ Not copied  Existing reports are not duplicated. |
| **Objectives** | ❌ Not copied  Existing objectives are not duplicated. |
| **Box settings** ✅ | The following box settings are duplicated:   - Modules - the list of active/inactive modules - Task structure - Scheduling    - Task scheduling mode   - Task scheduling mode per task type   - Task period alignment - Workload contouring settings - Box roles - Column views and card views (for Overview, Gantt, Scope, Board, and Risks modules) - task templates - Baselines permissions settings - box lead |
| **Box type settings** | The following are the same for all boxes of a given type and can’t be modified for individual boxes:   - Scope type - Sequentiality - Box period mode - Scheduling - Story points - Story point conversion ratio enabled/disabled - teams enabled (inherited and manually created) |

### Box type defaults and templates

When you duplicate a box, settings are duplicated directly from the box you are making a copy of. The box type templates are ignored.

Applies to:

- Box roles
- Column views and card views
- Task templates

[Unmapped block: nestedExpand]

### Inherited settings

Inherited settings are based on a position in a box tree and can’t be duplicated.

---

## Clone a box scope

Scope cloning creates **duplicates of tasks**. This action creates tasks in a box you are currently in.

1. Configure the box scope - cloned issues will be added to a Jira project listed in the **scope definition**.

![contentId-1918635048](/cms_trial/assets/be6a65b3-248f-4137-a6ae-cbb64ec8bef5.png)

1. Click the **+** button (available in Gantt and Scope modules)
2. Select **Clone existing scope.** A dialog appears.

![contentId-1918635048](/cms_trial/assets/c90284fc-9b1d-46ae-a739-0ea5b8dfe0dc.png)

1. Select:

   1. A box that contains tasks to be copied (source of tasks)
   2. A Jira project duplicate will be created in (target project)

![contentId-1918635048](/cms_trial/assets/c52c6bae-ccba-4155-a1ce-41163520b8b6.png)

1. Click **Clone**

### What data can be cloned

| Data | Cloning result (Yes / No) |
| --- | --- |
| **Jira issue** | yes |
| Basic tasks | no |
| **Issue types** | if possible  When possible, the new issue has the same type as the one being copied.   - ⚠️ **Epics** and **sub-tasks** are cloned as the **default issue type**. This means that after cloning, your new project doesn’t have any epics or sub-tasks. - If Jira setup allows, the new issues are cloned with the same issue type. - Otherwise, the default issue type is used. |
| Task structure | No  Structure builders aren’t cloned:   - Epics and sub-tasks are cloned as the default issue type. Therefore, it is not possible for an epic-based structure to be automatically recreated. - The position of tasks manually moved can’t be recreated. - Basic tasks aren’t cloned. Therefore, task structure based on basic tasks can’t be recreated. - Versions, Components, and Sprints aren’t cloned and are not added to the target project during cloning. Therefore, the structure based on those elements cannot be automatically recreated. |
| **Dependencies** | yes |
| **Summary** | yes |
| **Start / End date** | yes  The position of tasks on the timeline is preserved.  Data is cloned according to field mapping. contentId-1918635048contentId-1918635048 |
| **Baseline start/end date** | yes |
| Other fields besides Summary and synchronized date fields | no  Examples:   - priority - assignee - labels - team |
| Skills | no |
| Manual Colors | yes |
| Milestones  (based on Jira issues) | yes |
| Milestones  (based on basic tasks) | no |
| Estimates | - Original estimate yes - Story points no - Remaining estimate no - Time spent no |
| Status | no  The initial status of a project workflow is applied to all copied tasks. |
| Version, Component, Sprint. | no  During cloning, only Jira issues are created. The app does not make any other changes in the target Jira project; no other items, such as versions, components, or sprints, are created. |
| Scheduling mode | no  The scheduling mode of duplicated tasks is set based configuration of the target box. |

### Clone failure - required fields

For a Jira issue to be created, all required fields must be filled in. The required fields are based on Jira settings and can vary from project to project.

The app copies a limited number of fields during cloning. If any required fields in the target project aren’t filled in during cloning, issues can’t be created.

**Solution 1**: make fields optional (adjust Jira settings)

**Solution 2**: import issues instead of cloning the scope

![contentId-1918635048](/cms_trial/assets/591ca4d1-ad13-476c-97bb-00d158d76f00.png)

## Export and import using Jira

You can use Jira to duplicate tasks:

1. Export the issues using Jira
2. Import data to the new target project

## Import from a file

You can import data from the following files:

- mpp
- mpx
- csv
- xlsx
- xlsx
- ods

1. Prepare the export file
2. Set up a Jira project to which the tasks will be added to
3. Add the new project to the box scope
4. Run import

![contentId-1918635048](/cms_trial/assets/39b15449-7545-4af9-967e-d96e707ad7be.png)

## Duplicate box and box scope (new navigation)

Click to expand the guide

## Overview

You can create a new box by duplicating an existing box.

When you duplicate a box, the box configuration is copied. The app copies as much of the box setup as possible. Box type settings and defaults are ignored in favor of the exact setup of the box you are making a copy of.

You can't duplicate a box with all its contents and tasks.

You can use the configuration of an existing box, duplicate it, and create a new box with an identical configuration. However, the scope of a box (tasks inside a box) isn't duplicated—tasks have to be added to the new box scope afterward.

[Box configuration settings](/cms_trial/space/SPM/1918666176/Box+configuration/) of a box are applied to the new box:

- [security (user roles)](/cms_trial/space/SPM/1918829579/Permissions/)
- [modules and their settings](/cms_trial/space/SPM/1918503298/Define+available+modules/)
- [connected tools](/cms_trial/space/SPM/1918633230/Integrations/) and the scope owner (tool connections get replicated)

[Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) impacts the exact setup of the newly created box.

If some settings (such as [column views](/cms_trial/space/SPM/1918404907/Column+views/) or [quick filers](/cms_trial/space/SPM/1918635901/Quick+filters/)) were inherited from the upper-level boxes, if you move a new box to a different place in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/), inherited settings can be lost. Inherited settings are always based on upper-level boxes and depend on placement within the box hierarchy.

## Duplicate a box

1. Activate the actions menu

   1. by clicking on the three dots menu icon on the right OR
   2. by right-clicking on a box row
2. Select **Duplicate configuration.** A box creation pop-up appears.

![Context menu in the box tree](/cms_trial/assets/8453c4b0-05f3-45bd-bb79-c3ab5eca6b1a.png)

1. The following fields arepre-filled:

   - Type (can’t be changed)
   - Name
   - Icon
   - Start date
   - End date
   - Jira spaces (not required)

     - available only for project boxes (can’t be filled in for boxes without their own scope, such as a portfolio). The box scope can be adjusted later in a box configuration.

![Screenshot of duplicating box configuration in the Overview module.](/cms_trial/assets/80be25fa-5cd4-4ffa-aeda-c1b50bb84d5b.png)

1. Click **Create.**

### What data is duplicated

| **Settings** | **Result** |
| --- | --- |
| **Box scope** | ❌ Not copied.  The scope configuration is not copied.  Box content is not replicated (spaces, tasks, work items, etc.). |
| **Sub boxes** | ❌ Not copied  Child boxes are not duplicated. |
| **Reports** | ❌ Not copied  Existing reports are not duplicated. |
| **Objectives** | ❌ Not copied  Existing objectives are not duplicated. |
| **Box settings** ✅ | The following box settings are duplicated:   - Modules - the list of active/inactive modules - Task structure - Scheduling    - Task scheduling mode   - Task scheduling mode per task type   - Task period alignment - Workload contouring settings - Box roles - Column views and card views (for Overview, Gantt, Scope, Board, and Risks modules) - Task templates - Baselines permissions settings - Box lead |
| **Box type settings** | The following are the same for all boxes of a given type and can’t be modified for individual boxes:   - Scope type - Sequentiality - Box period mode - Scheduling - Story points - Story point conversion ratio enabled/disabled - Teams enabled (inherited and manually created) |

### Box type defaults and templates

When you duplicate a box, its settings are copied directly from the box you are duplicating. The box type templates are ignored.

Applies to:

- Box roles
- Column views and card views
- Task templates

[Unmapped block: nestedExpand]

### Inherited settings

Inherited settings are based on a position in a box tree and can’t be duplicated.

## Clone from another box

Scope cloning creates **duplicates of tasks**. This action creates tasks in the box you are currently in.

1. Configure the box scope - cloned work items will be added to a Jira space listed on the **Work items from Jira** page.

   ![Screenshot of the Work items from Jira configuration page. ](/cms_trial/assets/fe9cd190-d244-4dd8-a49f-c49ca82882ee.png)
2. In the Gantt or Scope module, click **Tasks**.
3. Select **Clone from another box.** A dialog appears.

   ![Screenshot of the Clone from another box option in the Gantt module.](/cms_trial/assets/dcac2bb5-7149-4687-83d2-e9a197217f3b.png)
4. Select:

   1. A box to clone the scope from.
   2. A Jira space duplicate will be created in (target space).

      ![Screenshot of cloning the scope from another box.](/cms_trial/assets/00f470cf-9345-4189-972e-24f7c2ec3d6e.png)
5. Click **Clone.**

### What data can be cloned

| Data | Cloning result (Yes / No) |
| --- | --- |
| **Jira work items** | yes |
| BigPicture tasks | no |
| **Work item types** | if possible  When possible, the new work item has the same type as the one being copied.   - ⚠️ **Epics** and **sub-tasks** are cloned as the **default work item type**. This means that after cloning, your new project doesn’t have any epics or sub-tasks. - If the Jira setup allows, the new work items are cloned with the same work item type. - Otherwise, the default work item type is used. |
| Task structure | No  Structure builders aren’t cloned:   - Epics and sub-tasks are cloned as the default issue type. Therefore, it is not possible for an epic-based structure to be automatically recreated. - The position of tasks manually moved can’t be recreated. - BigPicture tasks aren’t cloned. Therefore, a task structure based on BigPicture tasks can’t be recreated. - Versions, Components, and Sprints aren’t cloned and are not added to the target space during cloning. Therefore, the structure based on those elements cannot be automatically recreated. |
| **Dependencies** | yes |
| **Summary** | yes |
| **Start / End date** | yes  The position of tasks on the timeline is preserved.  Data is cloned according to field mapping. contentId-1918635048contentId-1918635048 |
| **Baseline start/end date** | yes |
| Other fields besides Summary and synchronized date fields | no  Examples:   - Priority - Assignee - Labels - Team |
| Skills | no |
| Manual Colors | yes |
| Milestones  (based on Jira work items) | yes |
| Milestones  (based on BigPicture tasks) | no |
| Estimates | - Original estimate yes - Story points no - Remaining estimate no - Time spent no |
| Status | no  The initial status of a space workflow is applied to all copied tasks. |
| Version, Component, Sprint. | no  During cloning, only Jira work items are created. The app does not make any other changes in the target Jira space; no other items, such as versions, components, or sprints, are created. |
| Scheduling mode | no  The scheduling mode of duplicated tasks is set based on the configuration of the target box. |

### Clone failure - required fields

For a Jira work item to be created, all required fields must be filled in. The required fields are based on Jira settings and can vary from space to space.

The app copies a limited number of fields during cloning. If any required fields in the target space aren’t filled in during cloning, work items can’t be created.

**Solution 1**: Make fields optional (adjust Jira settings).

**Solution 2**: Import work items instead of cloning the scope.

## Export and import using Jira

You can use Jira to duplicate tasks:

1. Export the work items using Jira.
2. Import data to the new target space.

## Import from a file

You can import data from a file. For more information, see the [Import from file](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Import%20from%20a%20file&linkCreation=true&fromPageId=1918635048) page.