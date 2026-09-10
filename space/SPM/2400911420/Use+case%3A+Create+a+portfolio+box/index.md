# Use case: Create a portfolio box

|  |  |
| --- | --- |
| **Goal** | **Create a portfolio of boxes**  Organize your projects into a portfolio to assess how they align with the organization’s overall strategy and priorities. |
| **Scenario** | As a Project Portfolio Manager (PPM), you want to organize multiple projects and initiatives across the board into a portfolio. |
| **Key benefits** | - Ensures that all projects are aligned with the organization’s overall strategic objectives - Helps allocate resources efficiently across multiple projects to under- and overallocation - Enables organizations to prioritize projects based on their value and importance, ensuring the most critical projects are tackled first - Facilitates coordination between different projects, ensuring they don’t conflict and resources are shared effectively - Makes it easier to monitor the progress and success of projects - Provides a clear, organized way to report project statuses to stakeholders, making updates more transparent - Better performance and readability as opposed to keeping all projects in one box - Lets you view data from all the portfolio child boxes in the Gantt and Resources modules |

## Preconditions

- You can see and open the BigPicture app (you have [App User](/cms_trial/space/SPM/1918535770/App-level+permissions/) role).
- You are a Home [Box Admin or Sub-Box Creator](/cms_trial/space/SPM/1918797447/Box-level+permissions/) (to create boxes under the Home box).
- Optionally: Your organization already has at least one project or program box created that you can nest under a portfolio.

## Create a portfolio box step-by-step

1. Create a new Portfolio box under the Home box in the Overview module:

   1. Select Portfolio **project type.**
   2. **Name** your box.
   3. Define the box **start** and **end dates.**
   4. Optional: Change the **box icon** and **color.**
2. Click **Create**.

![A dialog for creating a new portfolio box in the Overview module.](/cms_trial/assets/834659cb-d65e-4eb8-94ae-94a03a6b7a81.png)

Your box is now created and listed in the box hierarchy under the Home box in the Overview module.

![A new portfolio box listed in the box hierarchy.](/cms_trial/assets/1ba96f3e-fe4e-4128-af13-0d4ac34d362b.png)

## What’s next?

### Add projects to your portfolio

The portfolio box is a [Non-scope](/cms_trial/space/SPM/1918766536/Scope+types/) type of box. It means that, unlike project boxes, you cannot populate them with tasks. Their purpose is to aggregate child boxes (the scope of the portfolio box is the sum of the scopes of the child boxes).

To make your portfolio box useful, add a new project or program box, or move an existing box under the portfolio to nest it.

![A process of nesting one box under another.](/cms_trial/assets/e4283567-7b1b-4e88-82f9-de9f6403db3e.mp4)

Note the consequences of moving a box due to the [inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/). If the existing box you want to add to the portfolio inherited some settings from its previous parent box (if it had any), those settings might be lost upon the parent's change.

### Create a portfolio of portfolios

By default, the portfolio [box type](/cms_trial/space/SPM/1918830000/Box+types/) can have only the Home box (Main) as its parent. However, it is possible to nest a portfolio box under another portfolio box. For that, you must add a portfolio as the **Parent type** to the portfolio box type’s **General** > **Basics** settings.

![Portfolio's parent types.](/cms_trial/assets/1904a02e-eff3-4d86-b654-d52e2f7bfaf8.png)

This is useful when you want to organize projects and divide them into thematic business areas or departments.

### Monitor the progress of projects and the entire portfolio

Portfolio box rolls up data from the child boxes and displays it in its swimlane. In the Overview module, you can track progress, time, the sum of task statuses, or budget for the child boxes and the portfolio.

Customize the [column view](/cms_trial/space/SPM/1918404907/Column+views/) to ensure you see the exact data you want.

![Portfolio box and child boxes in the Overview module.](/cms_trial/assets/8c4db3d9-3427-48e1-bfc4-5b5f7a8920e1.png)

Remember that the Overview module offers three views:

- [Hierarchy](/cms_trial/space/SPM/1918799130/Hierarchy+mode/) view shows the box hierarchy in a column view, where columns can be customized and aggregated.
- [Timeline](/cms_trial/space/SPM/1918538282/Timeline+mode/) view can provide the same data for the individual child boxes and portfolio as the Hierarchy view. In this view, you can additionally see boxes visualized as bars and arranged by their dates on the timeline.
- [Kanban board](/cms_trial/space/SPM/1918700991/Kanban+board+mode/) view shows only child boxes, making it a convenient way to manage box statuses. In this view, you can move boxes from one board column to another like tasks on a Jira board.

### Visualize and track portfolio projects and tasks

You cannot see project tasks in the Overview module. That’s where the Gantt module comes in.

In the Gantt module, you can see every project and the tasks in its scope in the column view and timeline. Since it gives you a complete view into the entire scope of the portfolio box, you can not only [aggregate data](/cms_trial/space/SPM/1918636993/Column+data+aggregation+methods/) in columns, but also:

- [group tasks](/cms_trial/space/SPM/1918830289/Group+tasks/) by the columns (including the **Milestone** column)
- group portfolio items by child boxes
- see baselines from different projects in one place, allowing you to spot deviations within your portfolio quickly
- leverage quick filters, date filters, and custom filters to find the exact items within your portfolio
- track workload and capacity of all resources assigned to the portfolio projects

### Manage resources on the portfolio level

With the Resources module, you can effectively manage the workload and capacity of all the individuals and teams assigned to projects in a portfolio:

- see the total workload, capacity, and remaining capacity of the resources on the portfolio level
- group the portfolio by one or two levels by Individuals, Teams, Skills, and Projects. For example, the grouping by:

  - **Teams** lists all the teams assigned to the portfolio, along with their workload, capacity, remaining capacity, and tasks
  - **Individuals** + **Project** gives insight into who is assigned to individual projects and their workload, capacity, remaining capacity, and tasks.
  - **Skills** + **Projects** gives you an idea of how skills are utilized across different projects.

## Additional resources

- [Create portfolio box](/cms_trial/space/SPM/1918634872/Create+portfolio+box/)
- [Gantt module in portfolio boxes](/cms_trial/space/SPM/1918700619/Gantt+module+in+portfolio+boxes/)
- [Resources module in portfolio boxes](/cms_trial/space/SPM/1918766197/Resources+module+in+portfolio+boxes/)