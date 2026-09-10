# Strong dependencies

## About strong dependencies

There are four standard types of dependencies, which are called 'Strong links' and have a scheduling impact. Every task on the timeline has two significant sides - to the left and to the right. These signify the Start and End Dates. Therefore, by linking two tasks (below referred to as Task A and Task B) we can expect four following combinations which are **referred to as dependency types.**

When one of the Auto-scheduling modes is enabled, such links will adjust the linked task's period. Strong links are displayed as a regular line and you can use them to indicate when a task should begin or end in relation to other tasks.

The default strong links are created during the installation:

![contentId-1918701700](/cms_trial/assets/956a2953-a91e-4368-a74e-0db2ff2bc7b3.png)

In case there are multiple dependencies targeting one task, including ASAP dependencies, the latest possible date will be set for this task.

## Strong dependencies

### End to Start

When Task A finishes, then Task B starts and Task B can’t start until Task A is done.

- Asap mode off: moving Task A to the right will also move Task B, as long as Task A's End Date is moved up to or ahead of Task B's Start Date. Moving Task A to the left has no effect on Task B. When Task B is moved to the left, it will not go further than Task A's End Date. Moving it to the right has no effect on Task A.

  ![contentId-1918701700](/cms_trial/assets/bbc3f8ed-19a0-4aff-96ac-56eb62b8ce3b.png)
- Asap mode on: moving Task A to the left or right will also move Task B, so that it starts on the first working day after A finishes. Moving Task B has no effect.

![contentId-1918701700](/cms_trial/assets/1086a5ff-ca4d-4ba3-b327-e776d343d92a.png)

### End to End

- Asap off: when Task A ends, Task B also immediately ends. Task B can’t finish until Task A is done but they don’t have to end at the same time: Task B can end any time after Task A ends. The lag time determines the minimum gap. Moving Task A to the left changes nothing. However, if Task A is moved further than Task B's End Date, Task B will be moved in order to retain the dependency (and to end at the same time). Moving Task B to the left further than Task A's End Date will automatically move Task B's end at the same time as the end of Task A. Moving Task B to the right has no effect on Task A.

  ![contentId-1918701700](/cms_trial/assets/223ec68f-b18a-4d76-bc76-f0b2c963a21e.png)

- Asap on: when Task A ends, Task B also immediately ends. Task B can’t finish until Task A is done but they don’t have to end at the same time: if the lag time is set it determines the gap between the Task B end and Task A end. Moving Task A to the left or right will also move Task B so that the gap between the tasks is equal to the lag time set.

  ![contentId-1918701700](/cms_trial/assets/3fe947fb-e2ec-4ede-97eb-b1e6602ba7e8.png)

### Start to End

- Asap off: when Task A starts, Task B can’t finish until Task A begins. Task B can finish any time after Task A begins. This type of link is rarely used. In this type of dependency, when Task A is moved to the right, if its Start Date exceeds the End Date of Task B, B will be also moved right. Moving Task A to the left changes nothing.

  ![contentId-1918701700](/cms_trial/assets/d1e47ece-f34f-412f-a022-47247ca25967.png)

- Asap on: when Task A starts, Task B can’t finish until Task A begins. Moving Task A to left or right moves the Task B so that it ends on the start date of Task A (+- lag time). Task B is not movable.

  ![contentId-1918701700](/cms_trial/assets/f4fe012d-f588-47e0-abfe-62c6e9cb528a.png)

### Start to Start

- Asap off: this means that when Task A starts, Task B will also start. Task B can’t start until Task A starts. They don’t have to start at the same time: Task B can begin any time after Task A begins. When two tasks are connected this way and task A is moved to the left, task B remains unchanged. When Task A is moved right and exceeds the Start Date of Task B, then Task B will also be moved to the right in order to start at the same time as Task A. When Task B is moved to the left, it will never go further than the start date of Task A. If Task B is moved right, Task A remains unchanged.

  ![contentId-1918701700](/cms_trial/assets/60b844ae-f116-486a-a523-933e02658737.png)

- Asap on: when Task A starts, Task B also immediately starts. Task B can’t start until Task A starts but they don’t have to start at the same time: if the lag time is set it determines the gap between the Task B start and Task A start. Moving Task A to the left or right will also move Task B so that the gap between the tasks is equal to the lag time set.

  ![contentId-1918701700](/cms_trial/assets/0d775354-91f2-4def-adc2-348be621622d.png)

## Scheduling mode vs strong dependencies

Strong dependencies do **NOT** affect **auto bottom-up** tasks (if the child tasks conflict with the change).

An auto bottom-up task can have children nested underneath it in the tree structure. In this situation task period is limited by the periods of its children (won't be affected by a strong dependency if there is a conflict):

![contentId-1918701700](/cms_trial/assets/b0079399-52de-40f0-a65d-52d380ef3e34.png)

Possible changes to make a strong dependency affect the tasks:

- changing the scheduling mode of the parent to top-down:

  ![contentId-1918701700](/cms_trial/assets/1ab6a895-379b-42f3-92a8-2479843879f2.png)
- drawing the Strong dependency to a child under the auto bottom-up parent (moving the child will expand the parent, but not move it).  
  Before:

  ![contentId-1918701700](/cms_trial/assets/980811fc-082f-4562-a921-f5437d8704c6.png)

  After:

  ![contentId-1918701700](/cms_trial/assets/19d7a90b-dc01-44f7-b38f-8e11a887093e.png)