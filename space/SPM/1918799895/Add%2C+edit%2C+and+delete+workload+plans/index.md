# Add, edit, and delete workload plans

## Create new workload plans

To create a new workload plan:

1. Click the **Add new plan** button.
2. Provide:

- Name
- Code
- Description (optional field)

A newly created plan is not assigned to any resources. To specify workload plan information, go to a workload plan’s **Details** page.

![contentId-1918799895](/cms_trial/assets/0688aab4-1e1e-43af-b54a-66af3a7794aa.png)

## Edit workload plan details

To access workload plan details, click the name of the plan or the **Details** button:

![image2022-1-26_16-57-44.png](/cms_trial/assets/47cea698-6f5d-41da-92f1-a826db8da64e.png)

The following options are available on a page of each workload plan:

| **Feature** | **Description** |
| --- | --- |
| **Section on the Left:** | contentId-1918799895 |
| Name | Workload plan name. |
| Code | Workload plan code. |
| Description | Optional description field. |
| Max weekly workload | Set a weekly workload limit. |
| **Section on the right:** | contentId-1918799895 |
| Save | Save changes. |
| Delete | Remove a Workload Plan. |
| Weekly workload total | Displays a sum of distributed weekly hours. image2021-5-17_13-28-27.png |
| Workload distribution | Workload hours are marked in purple on the weekly calendar. The sum of daily working hours results in the weekly workload total.  To change the number of daily working hours, modify the number at the top of a given column. image2021-5-17_14-27-52.png To move a working hour block, use the drag-and-drop mechanism. Drag-and-drop.mov |
| Assigned resources | View and manage the list of resources assigned to a workload plan.  The list shows:   - All resources assigned to a given workload plan. - Total number of resources assigned to the plan.   A resource can be assigned to the same workload plan over different periods. image2022-1-26_17-16-36.png |
| Max weekly workload | Specified the weekly workload limit of a workload plan.  Max weekly workload will affect the weekly workload total display color. If the workload distribution of a plan (total of the purple weekly calendar on the right) exceeds the maximum weekly workload, BigPicture won't let you save a workload plan.  The Max weekly workload doesn't influence resource capacity—capacity is impacted by the actual purple workload distribution on the right. A resource's capacity is simply a sum of the actual workload distribution in the purple section on the right. image2022-1-26_17-4-23.png |
| Weekly workload total | BigPicture automatically calculates how many hours have been distributed over all weekdays in total.  The color of the font indicates that:   - Yellow - total distributed workload < Max weekly workload - Green - total distributed workload = Max weekly workload - Red - total distributed workload > Max weekly workload  image2022-1-26_17-8-8.png |
| Daily working hours | The daily working hours are the daily capacity of resources used by the Gantt, Resources, and Board modules. |

## Delete workload plans

You **can’t** delete the default plans. If a resource is assigned to a deleted plan, BigPicture assigns the default workload plan instead.

To delete a plan, click the **Delete** button on:

- The workload plans overview page

  ![contentId-1918799895](/cms_trial/assets/32a91e98-71da-4122-918e-63e1f7870427.png)
- The workload plan details page

  ![contentId-1918799895](/cms_trial/assets/3b2c38da-b91b-48ed-8969-1c6f2602d495.png)