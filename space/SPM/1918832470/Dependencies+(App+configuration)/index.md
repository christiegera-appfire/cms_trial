# Dependencies (App configuration)

On the next pages, you can specify which Jira links will be used to visualize the task dependencies. When links are synchronized with dependency types, you can visualize and create dependencies using the Board or Gantt modules.

You can also turn off the synchronization of links, in which case adding a new dependency in the app will not create one in Jira—all dependencies created will be stored by the app only.

## **Link synchronization**

The mapped links can synchronize with Jira, but you can also create links between Jira issues and non-Jira issues such as Basic tasks, Projects, Versions, Components, Sprints or Backlog, or Trello tasks, in which case such a link will be visualized only as if, for example, there are no project links in Jira.

## Security and access

Only Jira administrators can access this page.

1. Click the **wrench** icon at the top right and select**General** from the drop-down list.

   ![contentId-1918832470](/cms_trial/assets/2d4959b8-11a6-4d55-a082-3da715582b78.png)
2. Next, go to the **Dependencies** tab.

   ![image-20250211-130856.png](/cms_trial/assets/9d1cfad0-49f6-49f4-807d-c448ca0ad284.png)

## Dependency types

There are two kinds of dependencies the Gantt and Board modules can display:

- Strong dependencies—dependencies with a scheduling impact. For example, when in auto mode, moving one linked task might update the position of the other linked tasks.
- Soft dependencies—dependencies with no scheduling impact. Moving one of the linked tasks does not affect the position of the linked issue.

By default, soft dependencies are not synchronized.

The Gantt module allows you to synchronize and display all dependency types. In auto mode, such dependencies have a scheduling impact. For Example, moving a linked task might update its successor's or predecessor's position on the timeline.

Dependencies **can’t** be synchronized and used as structure builders simultaneously.

## Constraints

- Creating a dependency can re-adjust the task period, but deleting a dependency will not move tasks on the timeline.
- You can use each link only one time.

Jira Cloud: If you can’t see a newly created link, click the **Refresh cache** button.

![image2023-7-3_9-53-16.png](/cms_trial/assets/ddab72ec-4716-4e7f-8283-47d40e18dbfd.png)