# Individuals

This tab allows you to manage resources, add new ones, and edit all its resource-related data, such as workload and holiday plans.

| **Feature** | **Description** |
| --- | --- |
| Add new individual | Add Jira users as resources and assign them to workload, holiday plans, or define skills. The list of resources is generated automatically when a box is created and shows all resources assigned to tasks in the scope of created boxes.   1. Click **Add new individual**. image-20240702-082751.png 2. Select a user from the drop-down menu. 3. Choose the **workload** and **holiday plans**. 4. Assign skills. 5. When ready, click **Add**. image-20240702-083106.png |
| Assign individuals to workload plan | Assign multiple individuals to a workload plan.   1. Expand the **Assign to** drop-down menu. 2. Select the **Workload plan** option. image-20240702-123747.png 3. Select the **workload plan** from the list. 4. Define the **Efficiency** and **Start date** fields. The end date will be adjusted automatically. 5. Select **individuals** from the list or use the **search box** to find them faster. The **Select all** and **Deselect All** options are useful when assigning multiple individuals. 6. When ready, click **Assign**.   **Workload plan efficiency**  If you want to simulate a non-human resource or use a single user to represent a team, you can use the efficiency multiplier. Alternatively, you can use it to reduce the capacity resulting from the workload plan by setting a value below 1. image-20240702-124005.png |
| Assign individuals to holiday plan | Assign multiple individuals to a holiday plan.   1. Expand the **Assign to** drop-down menu. 2. Select the **Holiday plan** option. image-20240703-062829.png 3. Select the **holiday plan** from the list. 4. Define the **start date**. The end date will be adjusted automatically based on the start date of the previous plan. 5. Select **individuals** from the list or use the **search box** to find them faster. The **Select all** and **Deselect All** options are valid when assigning multiple individuals. 6. When ready, click **Assign**. image-20240703-062958.png |
| Link to [resource detailed view](/cms_trial/space/SPM/1918700744/Individuals/) | Detailed view of a selected resource's skills, absences, workload, and holiday plans. Use this view to modify the plans and their start or end dates. image-20240702-083542.png |
| Current [workload plan](/cms_trial/space/SPM/1918506352/Workload+plans/) | A resource can be assigned to multiple workload plans, so the active plan is presented in this section. image-20240702-083747.png |
| Current [holiday plan](/cms_trial/space/SPM/1918505164/Holiday+plans/) | A resource can be assigned to multiple holiday plans, so the active plan is presented in this section. image-20240702-083837.png |
| Current [absence with the reason](/cms_trial/space/SPM/1918764834/Absences/) | The current absence period and the reason for the absence. Users can add their absences using their [My settings](/cms_trial/space/SPM/1918633316/Personal/)page**.** image-20240702-084235.png |
| Current [skills](/cms_trial/space/SPM/1918636059/Skill+management/) | The currently available skills. image-20240702-084631.png |
| Archived resources / Restore archived resources | To check archived resources:   1. Click the **More actions …** menu next to the **ARCHIVED** column. 2. Select the **ARCHIVED** label.   You can restore an archived resource by clicking the **Restore** button next to the ARCHIVED label. image-20240702-085024.png |
| Archive resources | To archive a resource:   1. Find a resource you want to archive. 2. Click the **Archive resource** button. 3. To confirm, click **Archive**.   After archiving, the resource's capacity will be zero, and the team’s availability will be set as *Unavailable* from the archive date. You can restore it anytime, but team availability must be manually adjusted. image-20240702-085453.png |

## Navigate the resource list

To find a particular resource, click on the column header menu to filter the list of available resources. You can also sort the list by alphabetical order and vice versa.

![image-20240702-091932.png](/cms_trial/assets/1b04dc42-3cb2-4c5a-9bb9-470d25cefed8.png)

### There are no limitations for resource entries

Currently, the list of resources has no number limitation. You can view and manage as many Jira entries as you want.

If you face any performance issues while loading more significant numbers of resources on the list, e.g., 10,000 or more, please contact our [Support](https://appfire.atlassian.net/servicedesk/customer/portal/11) team.

## Archived resources - impact on box modules

- Archived resources cannot be added to BigPicture teams. If you try to add an archived resource to a team, an error in the Teams module appears.

![A message that appears when a user tried to add an archived resource to a team.](/cms_trial/assets/fd54ef8c-afd0-4749-9916-dae82908d623.jpg)

Restore the archived individual first to add them to the team.

- When the resource is archived, its capacity becomes zero, and the team’s availability will be set as *Unavailable* from the archive date. You can restore it anytime, but team availability must be manually adjusted.

Archived resources are marked as **Archived** in the following modules:

#### Gantt module - Resources panel

![image-20240702-093006.png](/cms_trial/assets/6f336111-8fbd-4273-a96d-2a23f9c2d685.png)

#### Resources module

![image-20240702-093728.png](/cms_trial/assets/6f01d98f-6844-4f7f-80d8-9ccfa4c2feec.png)

#### Teams module

Archived users are advised to [close their membership period](/cms_trial/space/SPM/1918539185/End+membership/) in teams.

Upon archiving a user, the user's availability in the team is changed to *Unavailable*.

Upon restoration, the user's capacity is restored if the user is not assigned to any team. Teams availability remains *Unavailable*, and you can set it manually in the Teams module.

The **Show archived Resources** checkbox is checked by default.

![teams-archived-resource.png](/cms_trial/assets/001e132b-de50-4af6-bd99-fd63dd0e9be8.png)

#### Board module

![image2021-5-18_15-36-15.png](/cms_trial/assets/91fb492f-c6e0-4ede-aa26-54f9edcb0f35.png)

## Filter and sort

### Filter

You can filter the results based on column information:

1. Click the **More actions …** menu next to a selected column.
2. Use the search box to find results faster.

![image-20240702-094106.png](/cms_trial/assets/ca17989d-6c35-4e2b-8a2d-d6b7dd28ebec.png)

### Sort

You can sort the results based on column information.

1. Click the **More actions …** menu next to a selected column.
2. Choose the sorting direction:

   1. A-Z
   2. Z-A

![image-20240702-094429.png](/cms_trial/assets/38973e58-92fa-405b-95c6-614ca3950107.png)