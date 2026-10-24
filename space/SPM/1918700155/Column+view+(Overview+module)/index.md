# Column view (Overview module)

## Column view - Overview module (old navigation)

Click to expand the guide

Get the most information out of your data. The data visible in the columns of the Overview module provides high-level insight into your data. Modify the view to best meet your needs.

## Box vs task data columns

**Box-associated columns** show data associated with Boxes (not tasks) and are visible only in the Overview module.

**Task-associated columns**show data aggregation based on individual tasks (inline editing won't be possible in the Overview module). Those columns are marked with "tasks" in the name:

[Unmapped block: nestedExpand]

![Overview module, choosing a column](/cms_trial/assets/322283fc-7a26-4e4f-8acd-588420e37edf.png)

Task information has to be edited in a module (such as Gantt - the value of the "actual cost" column associated with a particular task can be adjusted). The word "tasks" won't appear in the column name in the modules because data in the modules is associated with tasks only (not Boxes):

![actual-cost-column.png](/cms_trial/assets/96899eb0-0392-4348-911f-d05a9f8de9f6.png)

Those columns are based on [built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/).

Task value fields are available for all tasks (including [basic tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/)).

## Inline editing of box attributes

You can use [inline editing](/cms_trial/space/SPM/1918637324/Inline+edit/) to edit values directly in the Overview module.

[Unmapped block: nestedExpand]

### Limitations

Not all box attributes are editable. For **Closed** and **Archived** boxes, box attributes can't be edited.

## Aggregated box status

Aggregated box status is calculated for all Boxes.

![Statuses of aggregated boxes](/cms_trial/assets/c9bae595-47ce-48ef-bae4-0ed51a703bfe.png)

Status-based report is based on the scope of all sub-boxes. It shows issue distribution in different Jira status categories for each upper-level Box:

- To Do - grey color
- In Progress - blue color
- Done - green color

![Aggregated boxes, statuses highlighted](/cms_trial/assets/ba7a6b69-eb5e-4467-9737-f508fce11f96.png)

If a closed box does not have any aggregation yet, it is calculated once. Aggregations for all closed boxes that already have an aggregation are not calculated.

## Aggregated time-tracking report

Aggregated Box status is calculated for all Boxes.

Time-tracking report based on the scope of all sub-Boxes showing issue progress. The formula used is: 1-(Remaining estimate/Original estimate)\*100%

If a closed box does not have any aggregation yet, it is calculated once. Aggregations for all Closed Boxes that already have an aggregation are not calculated.

## Capacity column

You can have a quick overview of the team members' capacity in a given box.

The calculation is done for:

- team members only
- for the box period only

Manual changes made on Board module > Capacity planning are **not** included in the calculation

![Overview module, Capacity column highlighted](/cms_trial/assets/974c0c63-eef4-4ef8-a815-f7ce413b6bc6.png)

### Customization

You can display data in the following formats:

- Pretty (combines different units e.g., 4w 23d)
- Days
- Hours
- Decimal

![Capacity column radio buttons](/cms_trial/assets/c9193ebe-42a9-4dcd-82a9-78d2ede0bfa4.png)

### Limitations

- It is **not possible** to convert the capacity in **hours to Story Points** in this column.
- it is **not possible** to **change the aggregation** method in the column (always sum of capacity from a given Box only).

## Cost columns

The following columns can be added to the Overview module view:

- **Information associated with boxes →**values are associated with boxes only. They don't depend on task information.

  - Budget
  - Estimated Cost
  - Actual Cost
- **Information associated with tasks →** values are associated with tasks in a box.

  - Estimated Cost (Tasks)
  - Actual Cost (Tasks)

![Overview module, three columns highlighted](/cms_trial/assets/9b505d9c-32ea-428a-a7df-dc39f0a57bc7.png)

### Aggregation

Configure the table so that the app rolls up the value in the Box hierarchy (choose aggregation).

Columns can be customized, resulting in different aggregation of data:

- None
- Minimum
- Maximum
- Sum
- Sum, without a parent
- Average
- Average, without a parent
- Status in categories in %
- Children status categories
- Children's status categories in %

![Aggregation mode chosen](/cms_trial/assets/9449dfc9-0e2a-49e3-97b6-f348c94a8475.png)

[Unmapped block: nestedExpand]

**Box vs task data columns**

[Excerpt "box-vs-task-column" from page "$297698399" not found]

Corresponding columns:

| **Overview module** | **Gantt** | **Scope** | **Board** |
| --- | --- | --- | --- |
| **Actual Cost (Tasks)** | Actual cost | Actual cost | Actual cost |
| **Estimated Cost (Tasks)** | Estimated Cost | Estimated Cost | Estimated Cost |
| **Budget** | N/A | N/A | N/A |
| **Actual Cost** | N/A | N/A | N/A |
| **Estimated Cost** | N/A | N/A | N/A |

Adjust the column view. Then, use inline editing to adjust task information.

[Unmapped block: nestedExpand]

If you want to change the details of already planned tasks (tasks shown as cards assigned to sub-boxes on the left), change the filtering options in the Backlog to display all tasks.

[Unmapped block: nestedExpand]

Those columns are based on [built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/).

Fields are available for all tasks (including [basic tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/)).

**Field mapping**

**Actual cost** and **Estimated cost** fields can be mapped to a Jira field.

When fields are set to "Not Synchronized" the values are stored in the app only.

## Story points and Progress fields

Additional task calculated fields:

- Story Points
- Progress

![Story point column highlighted](/cms_trial/assets/8c74b332-5d9a-4e38-a4c5-f6f6cdf94b37.png)

Details about the box resulting from its box type settings are known to an operational user (for example, Box Editor, Box Admin) as they are visible only in [box type configuration](/cms_trial/space/SPM/1918666176/Box+configuration/), but those settings might affect your work with the boxes.

### Customization

![customization-status categories.png](/cms_trial/assets/14c32977-ef27-4126-98ba-e224b37e80d4.png)

## Box details

Any user can check details about the box resulting from its box type settings in the Overview module. Those settings might affect the User's work with the Boxes and are configured in the **Administration** > [**Box types**](/cms_trial/space/SPM/1918829342/App+administration/) section.

The following box information columns are available on the Overview module:

- [Period mode](/cms_trial/space/SPM/1918834623/Scheduling+mode+field/)
- Sequentiality
- Created date
- [Scope type](/cms_trial/space/SPM/1918766536/Scope+types/)

![overview-four-columns.png](/cms_trial/assets/6b22eeaa-3c04-451f-9906-262f50468cd8.png)

The scope type column shows the actual scope type of a box(which is set during Box creation and cannot be changed later).

[Unmapped block: nestedExpand]

## Archived boxes

You can also add an **Archived**column to the view. [Archived boxes](/cms_trial/space/SPM/1918634657/Archive+box/) are only visible in the following **View** settings.

![Overview module, archived box highlighted](/cms_trial/assets/da3cdfca-9f2c-479d-b4ba-f2192e16c7f9.png)

The data visible in the columns of the Overview module provides you with high-level insight into your data. Modify the view to best meet your needs.

## Closed date column

The **closed date** column allows you to compare the End date to the date of actual closing (changing the status to "Closed"). The user can add a 'Closed Date' column to the Overview module under the "Manage column."

The column is not inline-editable and has the same aggregations as other Date types, that is, None, Minimum, and Maximum.

![Adding column view](/cms_trial/assets/9f76f127-0947-4f0d-998a-c92dce2ad9a8.png)

## Inactive for column

Add the **Inactive for** column to see when the Box has been used for the last time.

This information is useful when:

- [auto-archiving of boxes](/cms_trial/space/SPM/1918634657/Archive+box/) is active
- you want to activate the auto-archiving of boxes - you can see which boxes will meet the criteria and be archived

You can easily [filter data](/cms_trial/space/SPM/1918503449/Filters+and+search/) using the **Inactive for** column.

![Inactive for column highlighted in the Overview module.](/cms_trial/assets/f9793da2-7c93-4570-8cf0-a3086fa74940.png)

## Column view - Overview module (new navigation)

Click to expand the guide

Get the most information out of your data. The data visible in the columns of the Overview module provides high-level insight into your data. Modify the view to best meet your needs.

## Box vs task data columns

**Box-associated columns** show data associated with boxes (not tasks) and are visible only in the Overview module.

**Task-associated columns**show data aggregation based on individual tasks (inline editing won't be possible in the Overview module). Those columns are marked with "tasks" in the name:

[Unmapped block: nestedExpand]

![Screenshot of adding columns to the view in the Overview module.](/cms_trial/assets/4e75925e-dd44-4581-969f-a94556003021.png)

Task information has to be edited in a module (such as Gantt - the value of the "actual cost" column associated with a particular task can be adjusted). The word "tasks" won't appear in the column name in the modules because data in the modules is associated with tasks only (not boxes):

![Screenshot of the Actual Cost column added to the Gantt module.](/cms_trial/assets/b6e2a920-4c31-4532-afcb-f93510114557.png)

Those columns are based on [built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/). Task value fields are available for all tasks (including [BigPicture tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/)).

## Inline editing of box attributes

You can use [inline editing](/cms_trial/space/SPM/1918637324/Inline+edit/) to edit values directly in the Overview module.

### Limitations

Not all box attributes are editable. For **Closed** and **Archived** boxes, box attributes can't be edited.

## Aggregated box status

Aggregated box status is calculated for all boxes.

The status-based report is based on the scope of all sub-boxes. It shows issue distribution in different Jira status categories for each upper-level box:

- To Do - grey color
- In Progress - blue color
- Done - green color

![Screenshot of the aggregated box status in the Overview module.](/cms_trial/assets/b136ae70-2c15-4f30-9009-9277cc3218f5.png)

If a closed box does not have any aggregation yet, it is calculated once. Aggregations for all closed boxes that already have an aggregation are not calculated.

## Aggregated time-tracking report

Aggregated Box status is calculated for all boxes.

Time-tracking report based on the scope of all sub-boxes showing issue progress. The formula used is: 1-(Remaining estimate/Original estimate)\*100%

If a closed box does not have any aggregation yet, it is calculated once. Aggregations for all closed boxes that already have an aggregation are not calculated.

## Capacity column

You can have a quick overview of the team members' capacity in a given box.

The calculation is done for:

- team members only
- for the box period only

Manual changes made in the Board module > Capacity planning are **not** included in the calculation.

![Screenshot of the Capacity column added to the view in the Overview module.](/cms_trial/assets/3d93d8af-b323-48f0-b042-2b0dcac43bbd.png)

### Customization

You can display data in the following formats:

- Pretty (combines different units e.g., 4w 23d)
- Days
- Hours
- Decimal

![Capacity column radio buttons.](/cms_trial/assets/c9193ebe-42a9-4dcd-82a9-78d2ede0bfa4.png)

### Limitations

- It is **not possible** to convert the capacity in **hours to Story Points** in this column.
- It is **not possible** to **change the aggregation** method in the column (always the sum of capacity from a given box only).

## Cost columns

The following columns can be added to the Overview module view:

- **Information associated with boxes →**values are associated with boxes only. They don't depend on task information.

  - Budget
  - Estimated Cost
  - Actual Cost
- **Information associated with tasks →** values are associated with tasks in a box.

  - Estimated Cost (Tasks)
  - Actual Cost (Tasks)

### Aggregation

Configure the table so that the app rolls up the value in the box hierarchy (choose aggregation).

Columns can be customized, resulting in different aggregations of data:

- None
- Minimum
- Maximum
- Sum
- Sum, without a parent
- Average
- Average, without a parent
- Status in categories in %
- Children status categories
- Children's status categories in %

![Aggregation mode chosen](/cms_trial/assets/9449dfc9-0e2a-49e3-97b6-f348c94a8475.png)

**Box vs task data columns**

**Box-associated columns** show data associated with boxes (not tasks) and are visible only in the Overview module.

**Task-associated columns**show data aggregation based on individual tasks (inline editing won't be possible in the Overview module). Those columns are marked with "tasks" in the name.

See the corresponding columns in the table. You can adjust the column view by [inline editing](/cms_trial/space/SPM/1918637324/Inline+edit/) in the Gantt, Scope, and Board (Backlog) modules.

| **Overview module** | **Gantt** | **Scope** | **Board** |
| --- | --- | --- | --- |
| **Actual Cost (Tasks)** | Actual cost | Actual cost | Actual cost |
| **Estimated Cost (Tasks)** | Estimated Cost | Estimated Cost | Estimated Cost |
| **Budget** | N/A | N/A | N/A |
| **Actual Cost** | N/A | N/A | N/A |
| **Estimated Cost** | N/A | N/A | N/A |

![Screenshot of editing the Estimated Cost column in the Board module. ](/cms_trial/assets/52d2e682-5c1c-4ce2-bc48-e6c36410ccdd.png)

If you want to change the details of already planned tasks (tasks shown as cards assigned to sub-boxes on the left), change the filtering options in the Backlog to display all tasks.

![Screenshot of the Backlog panel in the Board module.](/cms_trial/assets/b4f288f4-fad4-48f4-8dd7-689c5d9d1c95.png)

Those columns are based on [built-in fields](/cms_trial/space/SPM/1918832240/Built-in+fields/). Fields are available for all tasks (including [BigPicture tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/)).

**Field mapping**

**Actual cost** and **Estimated cost** fields can be mapped to a Jira field.

When fields are set to "Not Synchronized" the values are stored in the app only.

## Story points and Progress fields

Additional task calculated fields:

- Story Points
- Progress

![Screenshot of the Story Points and Progress columns added to the view in the Overview module.](/cms_trial/assets/40ca986a-72c5-4d1e-863b-bc155eb20c53.png)

Details about the box resulting from its box type settings are known to an operational user (for example, Box Editor, Box Admin) as they are visible only in [box type configuration](/cms_trial/space/SPM/1918666176/Box+configuration/), but those settings might affect your work with the boxes.

### Customization

![Screenshot of the customization options for the Status column. ](/cms_trial/assets/14c32977-ef27-4126-98ba-e224b37e80d4.png)

## Box details

Any user can check details about the box resulting from its box type settings in the Overview module. Those settings might affect the User's work with the Boxes and are configured in the **Administration** > [**Box types**](/cms_trial/space/SPM/1918829342/App+administration/) section.

The following box information columns are available on the Overview module:

- [Period mode](/cms_trial/space/SPM/1918834623/Scheduling+mode+field/)
- Sequentiality
- Created date
- [Scope type](/cms_trial/space/SPM/1918766536/Scope+types/)

The scope type column shows the actual scope type of a box(which is set during box creation and cannot be changed later).

[Unmapped block: nestedExpand]

## Archived boxes

You can also add an **Archived**column to the view. [Archived boxes](/cms_trial/space/SPM/1918634657/Archive+box/) are only visible in the following **View** settings.

![Screenshot of the Archived column added to the view in the Overview module.](/cms_trial/assets/766d34a6-2393-4149-addc-faf490672a83.png)

## Closed date column

The **closed date** column lets you compare the end date to the actual closing date (changing the status to closed). The user can add the **Closed Date** column to the Overview.

The column is not inline-editable and has the same aggregations as other date types, that is, None, Minimum, and Maximum.

![Screenshot of adding the Closed date column to the view in the Overview module.](/cms_trial/assets/8dd25b03-0b48-4c4b-8650-444d631ef92a.png)

## Inactive for column

Add the **Inactive for** column to see when the box was last used.

This information is useful when:

- [Auto-archiving of boxes](/cms_trial/space/SPM/1918634657/Archive+box/) is active
- You want to activate the auto-archiving of boxes - you can see which boxes will meet the criteria and be archived

You can easily [filter data](/cms_trial/space/SPM/1918503449/Filters+and+search/) using the **Inactive for** column.

![Screenshot of the Inactive For column added to the view in the Overview module.](/cms_trial/assets/59272489-1e93-48da-a1b9-d4ce632a3d61.png)