# Holiday plans

You can create unlimited holiday plans to reflect the holidays and observances. Each non-working day resulting from the holiday plan reduces the capacity (daily capacity to zero) of the assigned resource or the team.

BigPicture can calculate tasks automatically based on the assignee's working days. Jira admins can enable this feature in the BigPicture configuration.

The holidays can be grouped into a set, such as European holidays. If the organization also has offices in the United States, a holiday set can be created for that region. This expedites the planning process as information is easily accessed across the organization.

## Security and access

Only a person with the App admin or App resource admin security role can access this page.

To access this page, go to **Administration** > **Resources** > **Holiday plans**.

![Screenshot of the Holiday plans page in Administration.](/cms_trial/assets/b2341080-090b-4cfa-81ed-f6aa3d8714c1.png)

## Holiday modes

The table below shows the difference between available modes:

| **Holiday mode** | **Description** |
| --- | --- |
| Non-working days | The non-working days of the week are marked with a grey circle. |
| Fixed mode | Dates are automatically moved to the next year and marked with a red circle. |
| Floating | Dates are not automatically moved to the next year and are marked with a blue circle. |
| Extra working days | The extra days are marked with a white circle. |

You can view all the holidays and inline edit the holiday name field:

![Screenshot of a calendar with non-working days.](/cms_trial/assets/f512c16e-610b-40a5-b307-542e505b2fc5.png)

## Default holiday plan

Each task assignee is automatically assigned to the default holiday plan once a task is added to the box's scope or when the currently assigned plan is deleted.

![Screenshot of the Holiday plans page with a default holiday plan highlighted.](/cms_trial/assets/49887d72-ec23-41a3-b763-4580169441f9.png)

### Work items without assignees

When a work item has no assignee, the default holiday plan is used to schedule it.