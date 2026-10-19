# Dependency loops and cross-box relationship

## Introduction

In Jira, issue links have no effect over the environment's structure and behavior. That means you can create any type of dependency between them in various combinations. Even types of dependencies that would make no logical sense or would end up in a paradox can exist in a vanilla Jira environment (such as circular dependencies).

In our application though, strong links have a direct effect on the Start and End Dates, so some combinations of links are not allowed. This refers to what we call "loops". Let's imagine the following type of inter-dependency:

- Task A (Ends) → (Starts) Task B
- Task B (Ends) → (Starts) Task A

Such a combination of links on these two tasks would result in Task A rescheduling Task B, Task B rescheduling Task A, Task A rescheduling Task B, and so on and so forth.

## Warnings

This sort of paradox would create an infinitive number of data re-calculation and could possibly crush the environment. This is why the App will not allow it and will return a warning. For example, let's try to create a link between BPV-12 and BPV-10 (parent task):

![contentId-1918700470](/cms_trial/assets/8fbf28a8-1ad6-4d14-b41a-0966d64c2972.png)

## Finding the source of constraints

Loops are very easy to detect if tasks belong to a single Box. However, at times when the same task is a component of various - multiple Boxes, each belonging to a different user, it might not be that easy.

We could cause a change that might reschedule their whole Gantt, sometimes even not realizing it (i.e. if you can not view other Boxes due to security restrictions).

You can always go directly to the issue page and check the list of Boxes with that particular issue in scope. All dependencies will be listed and you will be able to edit/delete them.

![contentId-1918700470](/cms_trial/assets/95d4d0d5-168e-4a99-bd77-d530c4656220.png)

In the Gantt module, click the task on the timeline and a pop-up will appear with all dependencies listed:

![contentId-1918700470](/cms_trial/assets/32eaf752-1f3f-42c5-b552-4c2c35f70267.png)

Dependencies outside the scope of a Box can't be edited within it (you can go to the issue page to manage them). If the issue is not in scope you will see:

![contentId-1918700470](/cms_trial/assets/bd26a208-1c6a-465e-8c4f-85b9f975676f.png)

Or:

![image-20250306-093001.png](/cms_trial/assets/5684ffba-cc9a-40a5-a615-0db9e0209ae9.png)

To delete a link on Gantt, make sure dependencies are expanded (otherwise, they will be displayed as non-interactive dots)

![image-20250306-093017.png](/cms_trial/assets/53c2d3da-6af4-455f-a4f2-d49fea832378.png)

Then, right-click on a link to see the context menu.

![contentId-1918700470](/cms_trial/assets/f6895f96-8bd5-40e4-9ff6-18258b1b4d85.png)