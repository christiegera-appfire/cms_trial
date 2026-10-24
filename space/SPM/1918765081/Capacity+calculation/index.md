# Capacity calculation

## Capacity calculation (old navigation)

Click to expand the guide

## Introduction

The capacity of the resources is calculated based on [workload plans](/cms_trial/space/SPM/1918506352/Workload+plans/) and non-working days resulting from [holiday plans](/cms_trial/space/SPM/1918505164/Holiday+plans/) and individual [absences](/cms_trial/space/SPM/1918764834/Absences/).

![Screenshot of the View menu with Capacity checked.](/cms_trial/assets/48e3f49c-dd41-48ab-b8d1-50ab6e94cceb.png)

## Individual capacity

The formula for calculating the capacity of an individual resource:

*Individual capacity per day = sum of (working hours per day - team availability per day)*

Currently, availability across different teams is not validated, so the total availability across different teams can exceed 100%.

Capacity = working hours specified in the workload plan - non-working days (in other words, how much of total work can a resource do in a period.

Example: Kate works eight hours a day. Her standard workday capacity is eight hours. If Monday is a national holiday and she has a day off, her Monday capacity is 0h).

**The calculation of individual capacity considers team members' availability across all teams.**

Example: Kate is assigned 50% availability in team Agile. Her capacity as an individual for a standard workday mentioned above is four hours. Team Agile gains four hours of capacity. In other words, half of Katie's capacity was allocated to the team effort. Her capacity as an individual has been reduced.

Individual capacity = Workload Plan value - Team allocation

If a resource is assigned to a team 100%, their individual capacity is synonymous with team capacity. So it's 100% (not 0h).

### Individual capacity in portfolio boxes

Individual capacity in [none scope boxes](/cms_trial/space/SPM/1918537743/None+(aggregations+only)/) such as the root (Home) and portfolio boxes presents:

- The user’s calendar capacity if the user is not assigned to any team.
- The user’s calendar capacity if the sum of the user’s team capacities is greater than the user’s calendar capacity.
- The sum of the user’s team capacities if the sum of the user’s team capacities is less or equal to the user’s calendar capacity.

Workload cell coloring is calculated based on the capacity selected above.

[Unmapped block: nestedExpand]

### Individual capacity in different grouping combinations

The following table presents the capacity calculation for an individual depending on the selected [grouping combination](/cms_trial/space/SPM/1918701793/Swimlanes+and+grouping/) in the Resources module.

calendar - Capacity calculated based on calendar availability.

Teams - Capacity calculated from a user’s allocation to teams within the box.

limitation - If team-based capacity is less than or equal to the calendar capacity, the team-based capacity is displayed. If team-based capacity is greater than the calendar capacity, the calendar capacity is displayed.

| **Case** | **Swimlane** | **Program**  (own-scope boxes)  Unit: Man-days | **Portfolio**  (none-scope boxes)  Unit: Man-days | **Any box**  (any box type)  Unit: % |
| --- | --- | --- | --- | --- |
| An individual is not allocated to any team | Individuals | calendar | calendar | N/A |
| Individuals then Teams | calendar | calendar | N/A |
| Individuals then Projects | calendar | calendar | N/A |
| Individuals then Skills | calendar | calendar | N/A |
| An individual is allocated to teams; allocation equals 100% (or less) | Individuals | Teams | Teams | Teams |
| Individuals then Teams | Teams | Teams | Teams |
| Individuals then Projects | Teams | Teams | Teams |
| Individuals then Skills | Teams | Teams | Teams |
| An individual is allocated to teams; allocation is greater than 100% | Individuals | Teams | limitation | Teams |
| Individuals then Teams | Teams | limitation | Teams |
| Individuals then Projects | Teams | limitation | Teams |
| Individuals then Skills | Teams | limitation | Teams |

## Team capacity

The formula for calculating the capacity of a team:

*Team capacity per day = sum of*[*individual capacities of team members*](/cms_trial/space/SPM/1918765081/Capacity+calculation/) *per day.*

Team capacity = 8h +4h (8h\*100% + 8h\*50%) = 12h

![contentId-1918765081](/cms_trial/assets/e6e1b74b-dd8b-4853-8824-37400166e3fd.png)

## Capacity = 0

Capacity is equal to 0 when a resource is unavailable on a given day (because of Workload Plans, Holiday Plans, or individual Absences).

The related user’s capacity is automatically set to 0 when the user is archived.

**Capacity can equal 0 for an individual or a Team.**

In that situation, in the Resource grid (resources module) and the Resource Panel (Gantt module), the App uses the following algorithm (applies only for tasks that have automatic contouring mode):

- **the task effort****is****distributed** **between non-working days** of the resource **if all days****from the task's period are non-working days** (sum of capacity from that period is 0),
- **The task effort****is not****distributed** **between non-working days** of the resource **if only a part****of the task's period consists of non-working days** (the sum of capacity from that period is >0).  
  In that case, task effort is distributed only between working days.

As a result, if the capacity (of a resource or a team) is 0 and there are some tasks with effort estimation in that period:

- in the Resource grid, the Workload cell is red, and it displays the Workload distributed according to the above algorithm.
- In the Resource Panel, the Workload cell is visible, red, and displays Workload distributed according to the above algorithm.

In the example below, Capacity of a resource = 0 (because of a week-long absence)

![image-20240118-080247.png](/cms_trial/assets/e3fa60e1-64b7-4ca6-85f2-873039ff6155.png)

However, the workload is distributed because the resource is absent for the duration of an entire task.

![image-20240118-080313.png](/cms_trial/assets/d7636ac5-ae52-4e5e-9df2-601b7ffd31cf.png)

**This algorithm is practical to present resource overload in the following cases:**

1. "Incorrect" allocation of a Resource to a Box (Availability of a Team Member is not matched with the task assignment of this Member in this Box, e.g., Availability=0%).
2. Tasks are assigned to a Resource with a long absence (e.g., sick leave, maternity leave, etc.)
3. The team has no Members

## Capacity details

After clicking on the capacity cell, you see a dialog box containing information on the main factors that make up daily capacity:

- Workload Plans
- Efficiency
- Holiday plans and their impact
- Absences
- Availability in teams

To see the capacity details:

1. Go to the **Individual** view in the Resources module.
2. Check the **Capacity** option in the **View**dropdown.
3. Set the **Aggregation**of the time period to **Daily**.

![nrg-capacity-details.png](/cms_trial/assets/22f6b990-1262-4612-ac4e-286d84e699b2.png)

### Capacity pop-up elements

| **Element** | **Description** |
| --- | --- |
| Date | Capacity is always checked for a particular day - date information is listed in the top right corner. image-20240118-080607.png |
| Working day/ day off | Information about whether a resource is working on a given day image-20240118-080623.png |
| Resource name and avatar | contentId-1918765081 |
| Capacity | contentId-1918765081 |
| Factors and details | Relevant elements that lead to a particular capacity are listed. contentId-1918765081 |

### Factors

The window with capacity details is divided into sections representing each factor - some sections are not shown if they are irrelevant in a given case.

- **Workload Plan** and team memberships sections are shown only if there is no Absence and nothing is planned in the Holiday Plan that would make that day a day off.
- **Absences** section is shown only if there is an absence planned for that day.

  - The user is not informed about the absence type and comments attached, as it might contain personal data. Details are available in Administration.
- **Holiday Plan** section - shown only if something is planned for that day in the Holiday Plan; if it is a regular day, the section disappears.

For example, when capacity = 0, you see the factors that lead to this result.

Case 1: Absences

![contentId-1918765081](/cms_trial/assets/9fd8f089-2fe1-4585-be0b-921861c2a733.png)

Case 2: workload plan (resource doesn't work the weekends.

![contentId-1918765081](/cms_trial/assets/ee4cd97d-0175-42fe-bcae-dfee7ec64e33.png)

Team memberships are influenced by filters on the Resources module:

- Team XYZ members (team filters)
- All team members
- Individuals with tasks

![contentId-1918765081](/cms_trial/assets/2c0989be-4508-495a-924f-4e35fe4193e4.png)

### Capacity exceeds workload plan hours

Such a situation is possible if the availability of a resource in teams exceeds 100% (across all Boxes in the App). This situation is marked in the Resources and Teams module with a **yellow border around an avatar**.

![image-20240118-080718.png](/cms_trial/assets/e0cd7ad4-8260-44a8-a282-3e7ebaee86d1.png)![image-20240118-080734.png](/cms_trial/assets/4f6024e3-ff1b-4aa6-b896-ff26c1709901.png)![image-20240118-080757.png](/cms_trial/assets/3ae02797-e2a1-47c3-9f3c-d753122e37b2.png)

To calculate the "Capacity allocation" and "Work progress" totals, the system imports the number of hours per day and hours per week from the host platform's global Timetracking configuration.

## Capacity calculation (new navigation)

Click to expand the guide

## Introduction

The capacity of the resources is calculated based on [workload plans](/cms_trial/space/SPM/1918506352/Workload+plans/) and non-working days resulting from [holiday plans](/cms_trial/space/SPM/1918505164/Holiday+plans/) and individual [absences](/cms_trial/space/SPM/1918764834/Absences/).

![Screenshot of the Capacity option enabled in the Resources module.](/cms_trial/assets/f70f4707-d5eb-487c-aa64-72a94d21eda8.png)

## Individual capacity

The formula for calculating the capacity of an individual resource:

*Individual capacity per day = sum of (working hours per day - team availability per day)*

Currently, availability across different teams is not validated, so the total availability across different teams can exceed 100%.

Capacity = working hours specified in the workload plan - non-working days (in other words, how much of the total work can a resource do in a period).

Example: Kate works eight hours a day. Her standard workday capacity is eight hours. If Monday is a national holiday and she has a day off, her Monday capacity is 0h.

**The calculation of individual capacity considers team members' availability across all teams.**

Example: Kate is assigned 50% availability in the Agile team. Her capacity as an individual for a standard workday mentioned above is four hours. Team Agile gains four hours of capacity. In other words, half of Katie's capacity was allocated to the team effort. Her capacity as an individual has been reduced.

Individual capacity = Workload Plan value - Team allocation

If a resource is assigned to a team 100%, their individual capacity is synonymous with team capacity. So it's 100% (not 0h).

### Individual capacity in portfolio boxes

Individual capacity in [none scope boxes](/cms_trial/space/SPM/1918537743/None+(aggregations+only)/) such as the root (Home) and portfolio boxes presents:

- The user’s calendar capacity if the user is not assigned to any team.
- The user’s calendar capacity if the sum of the user’s team capacities is greater than the user’s calendar capacity.
- The sum of the user’s team capacities if the sum of the user’s team capacities is less or equal to the user’s calendar capacity.

Workload cell coloring is calculated based on the capacity selected above.

[Unmapped block: nestedExpand]

### Individual capacity in different grouping combinations

The following table presents the capacity calculation for an individual depending on the selected [grouping combination](/cms_trial/space/SPM/1918701793/Swimlanes+and+grouping/) in the Resources module.

calendar - Capacity calculated based on calendar availability.

Teams - Capacity calculated from a user’s allocation to teams within the box.

limitation - If team-based capacity is less than or equal to the calendar capacity, the team-based capacity is displayed. If team-based capacity is greater than the calendar capacity, the calendar capacity is displayed.

| **Case** | **Swimlane** | **Program**  (own-scope boxes)  Unit: Man-days | **Portfolio**  (none-scope boxes)  Unit: Man-days | **Any box**  (any box type)  Unit: % |
| --- | --- | --- | --- | --- |
| An individual is not allocated to any team | Individuals | calendar | calendar | N/A |
| Individuals then Teams | calendar | calendar | N/A |
| Individuals then Projects | calendar | calendar | N/A |
| Individuals then Skills | calendar | calendar | N/A |
| An individual is allocated to teams; allocation equals 100% (or less) | Individuals | Teams | Teams | Teams |
| Individuals then Teams | Teams | Teams | Teams |
| Individuals then Projects | Teams | Teams | Teams |
| Individuals then Skills | Teams | Teams | Teams |
| An individual is allocated to teams; allocation is greater than 100% | Individuals | Teams | limitation | Teams |
| Individuals then Teams | Teams | limitation | Teams |
| Individuals then Projects | Teams | limitation | Teams |
| Individuals then Skills | Teams | limitation | Teams |

## Team capacity

The formula for calculating the capacity of a team:

*Team capacity per day = sum of individual capacities of team members per day.*

Team capacity = 8h +4h (8h\*100% + 8h\*50%) = 12h

## Capacity = 0

Capacity is equal to 0 when a resource is unavailable on a given day (because of Workload Plans, Holiday Plans, or individual Absences).

The related user’s capacity is automatically set to 0 when the user is archived.

**Capacity can equal 0 for an individual or a Team.**

In that situation, in the Resource grid (resources module) and the Resource Panel (Gantt module), the App uses the following algorithm (applies only for tasks that have automatic contouring mode):

- **The task effort****is****distributed** **between non-working days** of the resource **if all days****from the task's period are non-working days** (sum of capacity from that period is 0),
- **The task effort****is not****distributed** **between non-working days** of the resource **if only a part****of the task's period consists of non-working days** (the sum of capacity from that period is >0).  
  In that case, task effort is distributed only between working days.

As a result, if the capacity (of a resource or a team) is 0 and there are some tasks with effort estimation in that period:

- In the Resource grid, the Workload cell is red, and it displays the Workload distributed according to the above algorithm.
- In the Resource Panel, the Workload cell is visible, red, and displays Workload distributed according to the above algorithm.

In the example below, the capacity of a resource = 0 (because of a week-long absence).

![Screenshot of a resource whose capacity is 0 in the Resources module.](/cms_trial/assets/f6d5ccf1-1c70-4287-9c03-b8ae992ebd2e.png)

**This algorithm is practical to present resource overload in the following cases:**

1. "Incorrect" allocation of a Resource to a Box (Availability of a Team Member is not matched with the task assignment of this Member in this Box, e.g., Availability=0%).
2. Tasks are assigned to a Resource with a long absence (e.g., sick leave, maternity leave, etc.)
3. The team has no Members

## Capacity details

After clicking on the capacity cell, you see a dialog box containing information on the main factors that make up daily capacity:

- Workload Plans
- Efficiency
- Holiday plans and their impact
- Absences
- Availability in teams

To see the capacity details:

1. Go to the **Individuals** view in the Resources module.
2. Check the **Capacity** option in the **View**menu.
3. Set the **Aggregation**of the time period to **Daily**.

   ![Screenshot of the Capacity details window in the Resources module.](/cms_trial/assets/613f1166-39ce-4782-9b76-2d0e4d7bea55.png)

### Capacity pop-up elements

| **Element** | **Description** |
| --- | --- |
| Date | Capacity is always checked for a particular day - date information is listed in the top right corner. image-20240118-080607.png |
| Working day/ day off | Information about whether a resource is working on a given day image-20240118-080623.png |
| Resource name and avatar | contentId-1918765081 |
| Capacity | contentId-1918765081 |
| Factors and details | Relevant elements that lead to a particular capacity are listed. contentId-1918765081 |

### Factors

The window with capacity details is divided into sections representing each factor - some sections are not shown if they are irrelevant in a given case.

- **Workload Plan** and team memberships sections are shown only if there is no Absence and nothing is planned in the Holiday Plan that would make that day a day off.
- **Absences** section is shown only if there is an absence planned for that day.

  - The user is not informed about the absence type and comments attached, as it might contain personal data. Details are available in Administration.
- **Holiday Plan** section - shown only if something is planned for that day in the Holiday Plan; if it is a regular day, the section disappears.

[Unmapped block: nestedExpand]

### Capacity exceeds workload plan hours

Such a situation is possible if the availability of a resource in teams exceeds 100% (across all Boxes in the App). This situation is marked in the Resources and Teams module with a **yellow border around an avatar**.

![image-20240118-080718.png](/cms_trial/assets/e0cd7ad4-8260-44a8-a282-3e7ebaee86d1.png)![image-20240118-080734.png](/cms_trial/assets/4f6024e3-ff1b-4aa6-b896-ff26c1709901.png)

To calculate the "Capacity allocation" and "Work progress" aggregations, the system imports the number of hours per day and hours per week from the host platform's global Time Tracking configuration.