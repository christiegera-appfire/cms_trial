# Task in multiple boxes

## Box scope

A task can be in the scope of more than one Box. Below, you can find two ways to determine if a given task is in more than one Box.

You can't see Boxes if you lack permissions. If you do not have at least viewing access to a given Box, it will not be shown to you on any list. If your access is limited, contact your administrator.

### Gantt

1. Go to the Gantt module.
2. Click on a task on the Gantt timeline (don't click on the task key, as it is a link). **Now you can see a list of all Box IDs related to a given task** in a pop-up - the task is in the scope of those Boxes.

   ![box-id.png](/cms_trial/assets/407e7306-168f-47eb-8881-e628deb02525.png)
3. You can locate Boxes using their IDs:

   1. **The IDs function as links -** they will take you to the Overview module of a given Box.

      ![in-scope-indicator.png](/cms_trial/assets/c928ed5f-fdc7-41da-8712-f70360a7022b.png)
   2. You can also use the **search functionality:**

      1. **In the Box switcher.**

         ![box-search.png](/cms_trial/assets/6231d82b-0c81-4a96-a58d-72e9f88a6fae.png)
      2. **In the Overview module of the root (Home) Box.**

         ![image-20250306-102703.png](/cms_trial/assets/cd1051e7-0dbb-4f28-b54c-1dde460ff1eb.png)![image-20250306-102715.png](/cms_trial/assets/2815c511-8329-486c-ad2b-e9e9c92666d4.png)

### WBS

When the WBS widget is enabled, you can see the Boxes the task is in the scope of on a Jira issue page.

1. Make sure the WBS widget is enabled.
2. Go to the issue page in Jira.
3. If needed, expand the WBS widget.
4. Use the Box dropdown of a widget to see the list of Boxes the task is in.

![contentId-1918699867](/cms_trial/assets/d3e8adba-3900-4d8f-87b4-1e17138fcd24.png)![contentId-1918699867](/cms_trial/assets/fb4002fc-a9ba-4fe2-a7b3-bfd7511f6ede.png)![Screen Recording 2021-03-30 at 11.40.44.mov](/cms_trial/assets/cc150a6a-e5af-48de-995e-652f778fc46c.mov)

### Does scope type matter?

The App will list all Boxes a task is in the scope of (regardless of the box's scope type).

![contentId-1918699867](/cms_trial/assets/d725ac50-9d6e-455a-85b9-d26ed95bcb81.png)

Using the Gantt module provides you with a list of Box IDs. It doesn't give any information on:

- How are those boxes related to each other (nested)?
- if the Boxes have Own or Sub scope.

![contentId-1918699867](/cms_trial/assets/7f4049ab-da21-4d9f-a1c1-bf34d6d1dd61.png)

WBS provides you with information on Box hierarchy:

- you can see the Box tree.
- All Boxes that are part of the tree path are shown.
- Boxes that are a part of the structure but don't contain the task are greyed out.

![contentId-1918699867](/cms_trial/assets/fb4002fc-a9ba-4fe2-a7b3-bfd7511f6ede.png)

## Task in multiple Boxes

A single task cannot have different values in different Boxes. It has to be displayed identically in all Boxes.

Boxes display tasks based on field values in a connected tool. The App may show a Jira issue in two different Boxes, but it is still the same Jira issue, and it has the same field values. An assignee can't be a different person in one Box and different in another - an assignee is simply a value of a Jira issue displayed in a Box.

Changing the**start/end date**in one Box will cause an adjustment of the task period in another Box:

![Screen Recording 2021-03-30 at 12.47.51.mov](/cms_trial/assets/ab36d7d5-53e1-4713-a3f4-e150ded69f85.mov)

**Scheduling mode** of a task is always the same in all Boxes:

![image-20250306-102842.png](/cms_trial/assets/3fb514a1-d76d-4e92-83e6-7c5e55166be5.png)![Screen Recording 2021-03-30 at 13.00.05.mov](/cms_trial/assets/e8fb3914-73c6-4072-a70a-4f1b5ec19c69.mov)

Even settings independent from a connected tool (such as a task color) are identical in all Boxes. **Task color** is stored directly in the app and is not related to Jira.

![Screen Recording 2021-03-30 at 13.05.17.mov](/cms_trial/assets/9bfb7224-3377-41b9-b333-bd66890c18c7.mov)

## Potential Scheduling Conflicts

If you are experiencing erratic task behavior, check if the task is in the scope of multiple Boxes. Conflicting scheduling rules applied to a single task in different Boxes (such as task scheduling mode, WBS structure, and dependencies) can make the behavior of the App seem inexplicable:

- stop you from making changes in the Box you're in
- cause a seemingly strange behavior of the App
- cause an indirect circular relationship

Below you can find a few simple examples of possible situations. Remember, this is not an exhaustive list but is meant to demonstrate possible problems.

### Situation: task can't be moved

In the example:

- scheduling mode - auto top-down
- the same task has different parent tasks in two separate Boxes

The period of a child task can’t be changed in the ALFA Box because of restrictions imposed by a parent task in the BETA Box.

![image-20250306-102954.png](/cms_trial/assets/1cdecf5e-a109-4877-97a7-e6296860d5e0.png)![Screen Recording 2021-03-30 at 13.21.45.mov](/cms_trial/assets/40291a9c-840c-4c1d-8a2a-3452ecfc53d4.mov)

### Situation: task duration can't be extended

In the example:

- scheduling mode - auto bottom-up
- Task is a child in one Box, a parent in another Box

Task ALFA-9 can be moved without problems, but its duration can't be extended. Additionally, changes of period of ALFA-12 result in identical period changes of ALFA-9.

![contentId-1918699867](/cms_trial/assets/9f7410ad-4975-4fe9-8ce0-7a07f42e541e.png)![Screen Recording 2021-03-30 at 14.16.43 (2).mov](/cms_trial/assets/70a8876c-f886-4d83-a1a6-3d4765eb46b5.mov)

### Situation: dependency + parent relationship conflict

Sometimes, a task may stay in a position that defies validation rules because a new validation hasn't been triggered yet. Still, if you try to move/adjust a task (or perform any other action that is a trigger), validation will happen.

Two validation rules apply in this case:

- ALFA-9 is in auto bottom-up scheduling mode (child period dictates its period)
- Strong ASAP dependency from ALFA-1 to ALFA-9

Behavior:

![Screen Recording 2021-03-30 at 17.54.49.mov](/cms_trial/assets/0a1e4058-7527-4875-b5e0-2852d0005ad8.mov)

1. Dependency created

   ![contentId-1918699867](/cms_trial/assets/8523138d-0171-4c24-a95e-8f17efc1dc11.png)
2. Moving the child task

   ![contentId-1918699867](/cms_trial/assets/f502765a-19d8-4776-ac05-eb40bc95a516.png)
3. Moving the target task of the dependency

   ![contentId-1918699867](/cms_trial/assets/78587187-88b4-462b-a806-ed015d000a60.png)