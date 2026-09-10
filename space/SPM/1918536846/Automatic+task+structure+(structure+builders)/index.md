# Automatic task structure (structure builders)

## Overview

The task structure or hierarchy within a box can be generated automatically by the app. You can set the rules to structure your tasks by activating respective structure builders.

The order of structure builders reflects the levels of the hierarchy; in other words, the first structure builder determines the highest level within the structure.

## Security and access

Only a user with a (minimum) Box Admin security role can access and change the box configuration.

1. To change the task structure configuration, go to **Box configuration** > **Tasks** > **Task structure**.

## Hierarchy in Jira

While the structure algorithm is very advanced, some hierarchies are impossible to generate automatically. This is due to Jira's limitations and because the app cannot duplicate tasks in the hierarchy. Read more about [Conflicting structure builders](/cms_trial/space/SPM/1918637077/Conflicting+structure+builders/) .

### Custom vs. templates

Different tools offer different ways to automate task structuring. Out of the box, Jira provides Task<->Sub-tasks hierarchy or Epic link-based hierarchy, but you can build a much more advanced hierarchy using the App.

### Types of structure builders

There are two types of structure builders:

- built-in
- link-based

When you activate one of the built-in structure builders, a task representing a Sprint, Component, Version, or Project will be automatically added in the task types box in the automated rules of the Scope definition page.

The link-based structure builders use a Jira link to define the parent/child relation. [Soft links](/cms_trial/space/SPM/1918832470/Dependencies+(App+configuration)/) can also be used as structure builders.

**Templates**

The table presents the available configuration options.

| **Task structure option** | **Description** | **Screenshot** |
| --- | --- | --- |
| **Agile** | Organizes tasks into a hierarchy of epics and sub-tasks, ideal for single-project Agile teams. | image-20250428-112553.png |
| **Agile (multiple projects)** | Adds the project level above epics and sub-tasks to support multiple Jira projects in one box. | image-20250428-113052.png |
| **Release** | Structures tasks by project, version, and sub-tasks, making it easy to track work across releases. | image-20250428-114108.png |
| **Objective & Key Result** | Builds the task hierarchy based on the relationships between the Objectives, Key Results, and the issues linked to them. | image-20250428-114510.png |
| **Custom** | Lets you tailor the task hierarchy to your needs by editing the Advanced configuration settings. | Expand the **Advanced Configuration** tab and enable the structure builders you want to include. The **Custom** mode will turn on automatically. image-20250428-115420.png |

To activate custom configuration, change switchers in the **Advanced Configuration** panel.

On the right-hand side of the *Advanced Configuration*, you can see the Structure Preview of the tree structure. The warning about the conflict appears when the structure cannot be generated according to the user's preference.

For example, the hierarchy with Version and Jira Sprint structure builders cannot be shown, and as a result Version and Jira Sprint will be positioned at the same level.

![Conflict in custom structure builders setup.](/cms_trial/assets/31727190-3a0d-433a-896d-c42913247cf8.png)

**Limitations**

- only built-in structure builders are visualized on the structure preview
- link-based structure builders cannot be visualized on the structure preview

![contentId-1918536846](/cms_trial/assets/3f38008b-66cf-4d4d-958d-0bd45782df2b.png)

**Inverse links**

Only link-based structure builders have an "inverse" option. When a link-based structure builder is active an additional checkbox appears on the right in the "inverse" column. When you put a checkmark in the box, links of a selected type will be used in inverse to build a structure.

![contentId-1918536846](/cms_trial/assets/38edb2bb-abea-4a90-ad9e-934cc327b2a8.png)

### Multiple link-based structure builders

When multiple link-based structure builders are active, you can select which link should be created (when you make changes in the task tree).

**Example**

Task structure configuration example:

![contentId-1918536846](/cms_trial/assets/c319fef9-6129-4e0e-a2b2-d53bb17fa74b.png)

When you reposition a task in a tree, a pop-up appears:

![contentId-1918536846](/cms_trial/assets/b368ec29-296e-45f2-b603-2bb12db8af7c.png)

### Synchronization of changes made in the app with Jira

When you manually reposition a task in the task structure, task fields are updated to match structure builders.

The sync mechanism mirrors the user's changes in the task structure in the app in Jira issues. In other words, if the user indents, outdents, or drags and drops tasks within the task structure, relevant changes in tasks' fields responsible for their position are done automatically in Jira. The fundamental prerequisite for the changes to be made is active Structure Builders.

Link-based structure builders cannot overlap with built-in structure builders.

![contentId-1918536846](/cms_trial/assets/3db4dcc8-8d31-424f-b492-3ccca4c202ad.png)

### Advanced Roadmap in Jira Cloud Premium

Advanced Roadmaps is available as part of [**Jira Software Premium**](https://www.atlassian.com/software/jira/premium) and [**Jira Software Enterprise**](https://www.atlassian.com/software/jira/enterprise)**.**

#### What is the hierarchy in Advanced Roadmaps?

Advanced Roadmaps (AR) uses the same issue hierarchy as Jira Software but can be customized and expanded to track larger goals above the epic level. For example, you can create an initiative hierarchy level to represent a program containing multiple projects or combined efforts spanning multiple teams. When positioned above the epic level, the initiative can be used as a container for epics.

Hierarchy in AR lets you create a WBS structure (similar to the task structure in the app). AR hierarchy can be activated in a Jira configuration via **Manage Apps** in a Hierarchy configuration option. Go to **Jira Administration > Manage Apps > Advanced Roadmaps for Jira > Hierarchy configuration**

Hierarchy is based on levels (with the highest at the top). The [levels above Epic can be configured](https://support.atlassian.com/jira-software-cloud/docs/upcoming-changes-epic-link-replaced-with-parent/) and additional levels of hierarchy can be added above Epic. You can change the names of these levels and structure the hierarchy to meet your needs.

Learn about how to [configure hierarchy levels](https://support.atlassian.com/jira-software-cloud/docs/configure-custom-hierarchy-levels-in-advanced-roadmaps/) or how to expose these levels in Jira.

![contentId-1918536846](/cms_trial/assets/329add42-1cd1-4f09-a75d-9b4778f50c87.png)

You can also use your AR hierarchy by adding the AR as a structure builder in the App.

#### Parent/Epic Link/Parent Link in the app

In Jira Cloud, Atlassian introduced a unification of fields responsible for some parent-child relations (Epic link, sub-task, Jira (Advanced) Roadmaps). Parent Link is now handled by the same Parent field.

It is a single way of representing parent/child relationships to give you a simple, consistent experience for all levels in your Jira Software projects. epic-link and parent-link in company-managed projects are replaced with the parent concept already used in team-managed projects.

![contentId-1918536846](/cms_trial/assets/335bcf23-98e4-404d-8030-6c4891df6cc6.png)

#### Structure builders in the app

1. With the Parent structure builder activated, the app shows a hierarchy based on a Parent link (also sub-tasks and Epic links). In this case, the Epic and Sub-Task builders are redundant.
2. With the Parent structure builder activated, the app does not allow the creation of indents that are incompatible with the Jira hierarchy.

See the screenshot![contentId-1918536846](/cms_trial/assets/29a7b9b3-cf0c-4bb1-a077-2e4e3f57d93c.png)

### Trello structure builders

When you [connect external tools](/cms_trial/space/SPM/1918405249/Integrations+(App+configuration)/), you will see an additional section with Structure builders specific to that tool. In the case of Trello, these include Boards, Lists, Checklists, and Checklist Items:

![contentId-1918536846](/cms_trial/assets/29ed2cd9-08f3-4869-b08a-f8e1f8189f94.png)

**Example**

1. Let's generate a hierarchy resembling how data is presented on a Trello Board - tasks are organized into lists on the app’s Power-Up Public Roadmap:

![contentId-1918536846](/cms_trial/assets/bf66ec4f-f0bf-4a36-9413-9a4d3c46848c.png)

1. Enable the 'Boards' and 'ListClear' structure builders.

![contentId-1918536846](/cms_trial/assets/fac9bdf5-1633-404e-b100-be6c00dbbe52.png)

1. As a result, tasks are organized in the same way as the Trello board.

![contentId-1918536846](/cms_trial/assets/3fe128bf-73ef-4daf-a85b-866a8d71d2e5.png)

## Reset the structure (WBS)

Adjust the structure builders and click **Save**. The task structure is rebuilt accordingly.

### Manual indents

Manual indents are visible in the app only (not in Jira):

- all manual changes on the tree structure by indent/outdent
- any adjustments on the Basic tasks

Manual indents do **not** create links in Jira or changes to fields (e.g., Version or Epic), as they are not connected to any structure builders.

### Clear manual indents

Clear the changes that were manually made to the task structure.

The structure that was based on the structure builders is not affected.