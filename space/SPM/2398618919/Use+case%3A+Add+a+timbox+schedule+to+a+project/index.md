# Use case: Add a timbox schedule to a project

|  |  |
| --- | --- |
| **Goal** | **Add a standardized timebox schedule to a project**  You want to standardize planning across teams working in recurring cycles, like sprints, program increments, or quarters, by following a global schedule that is uniform across global teams and boxes. |
| **Scenario** | You manage an Agile, Hybrid, or SAFe project, or utilize similar frameworks. You want to work according to a consistent time-based and pre-defined structure to reduce repetitive setup work and ensure alignment across teams.  Alternatively, you work according to classic frameworks like Waterfall, and you want to visualize fiscal years or quarters on the Gantt timeline. |
| **Key benefits** | - Predefined timebox hierarchy and schedule that ensures consistency and alignment across the organization - Significantly reduced manual work - If a timebox schedule needs an update:    - App Admin updates it only in one place (reduced workload)   - the change is reflected in all connected boxes (reduced human errors, and no intervention required from Box Admins) |

## Preconditions

- app admin An App Admin created a timebox schedule (TS) for your organization. If not, your Admin can find instructions on how to set up and assign a TS on the following page: [Timebox schedules](/cms_trial/space/SPM/1989214530/Timebox+schedules/)

## Add a timebox schedule to your project step by step

Timebox schedules (TS) are managed by App Admins only. TS can be applied to only those boxes that have no local timeboxes set up on the [*Work items from Jira*](/cms_trial/space/SPM/2400714956/Populate+a+box+with+Jira+work+items/) page.

There are three ways a timebox can be added to a project:

- APP admin App Admin can assign a TS to the existing box on the [**App Administration**](/cms_trial/space/SPM/1918829342/App+administration/) > **Timebox schedules** page.
- box admin sub-box creator Box Admin or Sub-box Creator can assign a TS to a new box during the box creation process.
- box admin Box Admin can assign a TS to an existing box on the **box configuration** > **Tasks** > **Work items from Jira** page.

### Scenario 1: A Jira/App Admin assigns a TS to your box

For an App Admin to set up a new timebox schedule, they need to:

1. Go to the **App Administration** > **Timebox schedules** page.
2. If no timebox was created yet, click the **+Add new** button and fill in basic TS details (name, levels, and start date).
3. On the TS page, click the **Assign to boxes** button and select boxes from the list.

![Timebox schedule settings page.](/cms_trial/assets/c023f95c-a106-495f-8d1c-9ca35157b5c2.png)

When your App Admin adds a timebox schedule to your box, the timebox hierarchy, dates, and field mapping are already set up for you. The global teams associated with the timebox schedule are added, too.

Box Admins can define which Jira work items they want to include in the box to ensure all the tasks appear in the respective timeboxes.

However, you can still check if the TS was added to your box and see it visualized in the respective modules. See the [Expected outcomes](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/2396389835/Use+case+Add+a+timbox+schedule+to+a+project#Expected-outcome) section on this page.

Note that the timeboxes resulting from the timebox schedule, unlike the “local” timeboxes, are not listed under the parent box in the Overview module. For that reason, you cannot view or access them yet.

![A parent box with no timeboxes listed under it due to the active timebox schedule.](/cms_trial/assets/d6a7ec1e-49cb-48ea-8664-2d9efcd434f6.png)

### Scenario 2: Assign a TS during the box creation

1. Open the Overview module and go to the Home box.
2. Click the **+Add new** button.
3. On the box creation modal, toggle the **Use timebox schedule** option.
4. Select the timebox schedule from the list. If there are several timebox schedules on the list and you are not sure which one is applicable to your project, contact your App Admin.

![Assigning timebox schedule during the box creation process.](/cms_trial/assets/582b0ad2-a855-402b-a390-5c09d7ad6d59.png)

1. Fill in the box details (name, dates, icon, and color)
2. Click **Create** to finish.

Your box is now created, and a timebox schedule is assigned along with the associated global teams. You can proceed to the *Work items from Jira* page to define the tasks you want to include in the box and customize other box settings (if needed).

### Scenario 3: Assign a TS on the *Add work items from Jira* page

1. Open your box and go to **Configuration** > **Tasks** > **Add work items from Jira** page.
2. Enable the **Timeboxes** option and select **Timebox schedule**.
3. Click the dropdown to open the list of available timebox schedules and select the one that is applicable to your box.

![Timebox schedule dropdown on the work items from jira page.](/cms_trial/assets/af1c7b18-f435-4e35-9f52-ea02dd15134e.png)

1. Click the **Save** button to finish the process.
2. The selected timebox schedule is now added to your box.

## Expected outcomes

Whether you assigned the TS to a new box or your App Admin assigned it to an existing box, the outcome is the same. You can check whether the TS is active in your box in the following ways:

| **Module or page** | **Action** | **Screenshot** |
| --- | --- | --- |
| Overview | The **+Add new** button is grayed out on the parent box level. This is because you can no longer add new timeboxes to that box. | The add new button is unavailable in boxes with the timebox schedule added. |
| On the Home box level, the **timebox icon** in the **TS** column indicates that the timebox schedule is active. | TS column in the overview module. |
| Gantt | When you enable **Timeboxes**, they will appear on the Gantt timeline. | Timebox schedule visualized on the Gantt timeline. |
| Board | Timeboxes and their respective **global teams** are displayed on the Board. The App Admin can create new timeboxes on the *Administration* page.  Note that local teams are not displayed when the timebox schedule is active; only global teams can be associated with a timebox schedule. | Timebox schedule visualized on the board. |
| Objectives | Timeboxes and their respective **global teams** are displayed on the Board. The App Admin can create new timeboxes on the Administration page. | Timebox schedule visualized in the objectives module. |
| Resources | When you enable **Timeboxes**, they will appear on the resources grid. | Timebox schedule visualized on the resources grid. |
| *Work items from Jira* (box configuration page) | When the TS is active, the timebox configuration is grayed out. | Timboxes cannot be configured on the scope definition page when the timebox schedule is assigned to a box. |

## Additional resources

- [Timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/)
- [Timebox attributes](/cms_trial/space/SPM/3019800816/Timebox+attributes/)
- [Timebox schedules](/cms_trial/space/SPM/1989214530/Timebox+schedules/)