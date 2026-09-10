# Jira structure builders

While the structure algorithm is very advanced, some hierarchies are impossible to generate automatically. This is due to the limitation of Jira and because the App can not duplicate task in the hierarchy. Read more about on the [Conflicting structure builders](/cms_trial/space/SPM/1918637077/Conflicting+structure+builders/) page.

## Custom vs templates

Different tools offer different ways to automate task structuring. Out of the box, Jira provides Task<->Sub-tasks hierarchy or Epic link-based hierarchy, but you can build a much more advanced hierarchy using the App.

**Templates**

![contentId-1918863244](/cms_trial/assets/ef48fb7c-e824-43be-ad5e-6159067d9681.png)

There are three templates available:

- Agile
- Agile (multiple projects)
- Release

**Custom**

When you modify the **Advanced configuration,** you automatically switch to **custom** settings.

![image-20240313-144619.png](/cms_trial/assets/197602cc-dbc6-4ad1-a032-9f172fdcc8a9.png)

## Structure Preview

On the right-hand side of the **Advanced configuration,** you can see the preview of the tree structure.

![image-20240313-144808.png](/cms_trial/assets/0a49bfba-ebc6-43fa-ad48-de11be3c9b82.png)

A warning appears on the right if the structure can't be generated because of conflicts.

![image-20240313-144946.png](/cms_trial/assets/ba975c0c-7ae8-419d-b828-0f40a5ed9ca2.png)

**Constraints**:

- Only built-in structure builders are visualized on the right.
- Link-based structure builders can't be visualized on the right.

  ![contentId-1918863244](/cms_trial/assets/874ce22b-c8cf-49e6-9c7b-fbedf262ac0f.png)

## Types of structure builders

There are two types of structure builders - built-in and link-based. When you activate one of the built-in structure builders, a task representing a Sprint, Component, Version, Project will be automatically added in the task types box in the automated rules of the Scope definition page. The link-based structure builders use a Jira link to define the parent/child relation. Soft links that are marked in the App (go to [dependency configuration](/cms_trial/space/SPM/1918832470/Dependencies+(App+configuration)/) to check the link mapping) can be used as structure builders.

Parent's movement in the structure does not replace custom Links by Epic Link. The Epic Link for the task is not changed.

![contentId-1918863244](/cms_trial/assets/40e93a81-ec03-440c-9da6-904202217bad.png)See the example

For example, the WBS - DEMO Box has a project with three tasks in the Box scope with no hierarchy:

![contentId-1918863244](/cms_trial/assets/e0e74c18-4fc5-4aa0-ac8c-6f81e07e5745.png)

Let's enable the 'Project' structure builder:

![contentId-1918863244](/cms_trial/assets/dbd4e38c-46d8-4728-a632-0066c6ca3861.png)

As a result, a new task representing the project (WD - is the project key) was added to the list as a parent task:

![contentId-1918863244](/cms_trial/assets/3371b80d-e047-410d-81e3-c3872885240b.png)

Now, let's create an Epic and the WD-1 task to it:

![contentId-1918863244](/cms_trial/assets/2f287477-e3f2-4643-8874-2fa987bde309.png)

The last step is to activate the 'Epic' structure builder:

![contentId-1918863244](/cms_trial/assets/98647bac-13ad-4caf-99e5-b336c330dbed.png)

The T1 task is now nested under the Epic parent task:

![contentId-1918863244](/cms_trial/assets/57815f98-894d-4280-af11-49b158158e00.png)

## "Parent" structure builder

'Jira Advanced roadmaps' structure builder has been replaced with the **Parent** structure builder.

Atlassian introduced a unification of fields responsible for some parent-child relations (Epic link, sub-task, Jira (Advanced) Roadmaps). Parent Link is now handled by the same field (Parent).

## Inverse links

Only link-based structure builders have an "inverse" option. When a link-based structure builder is active an additional checkbox appears on the right in the "inverse" column. When you put a checkmark in the box, links of a selected type will be used in inverse to build a structure.

In the example below, the task structure is based on "Blocks" links.

For tasks 1, 2, 3:

- 1 blocks 2
- 2 blocks 3

![contentId-1918863244](/cms_trial/assets/602fbae7-d329-4379-a28e-08d8310e815c.png)

## Multiple link-based structure builders

When multiple link-based structure builders are active, you can select which link should be created (when you make changes in the task tree).

See the example

Task structure configuration example:

![image-20240313-145338.png](/cms_trial/assets/6d524647-b714-4879-a268-ed1fa04dbaa1.png)

Result - when you reposition a task in a tree, a pop-up appears:

![contentId-1918863244](/cms_trial/assets/2d3c4470-7ed4-4ba0-8ef3-0bb86e6d7896.png)![contentId-1918863244](/cms_trial/assets/e1c2a33f-b64c-4f06-a69b-572cf5c5b877.png)![contentId-1918863244](/cms_trial/assets/476ba7c0-66d1-4f31-98d6-abbf2fbbff0e.png)![contentId-1918863244](/cms_trial/assets/bf75aa1f-8e53-4873-9748-2fbdbe3ca43a.png)